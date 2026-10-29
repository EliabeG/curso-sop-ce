import fs from 'node:fs/promises';
import path from 'node:path';
import vm from 'node:vm';
import { fileURLToPath } from 'node:url';
import { createHash } from 'node:crypto';

const here = path.dirname(fileURLToPath(import.meta.url));
const filename = path.resolve(here, '../../../../assets/curso.js');
const source = await fs.readFile(filename, 'utf8');
const start = source.indexOf('  var leituraQuestoesE1Invalida = false;');
const end = source.indexOf('  function prepararQuestao(q)', start);
if (start < 0 || end < 0) throw new Error('Limites das funções reais não encontrados.');
const actualFunctions = source.slice(start, end);
const tests = [];
const check = (nome, ok, obtido) => tests.push({ nome, ok: Boolean(ok), obtido });
const seed = {
  v: 2, versao: 'anterior',
  respostas: { '11111111': 'C', '22222222': 'B', '33333333': 'Z', 'invalida': 'D' },
  erros: { '11111111': 1, '22222222': 4, '33333333': -1, 'invalida': 2 },
  simulado: { inicio: 10, fim: 20, corrigido: true, marcadas: { '11111111': 'C', '22222222': 'B', '33333333': 'Z' } }
};
function run(modulo, mode, initial) {
  let disk = JSON.parse(JSON.stringify(initial));
  let deleted = false;
  const sandbox = {
    MODULO: modulo, LETRAS: ['A', 'B', 'C', 'D', 'E'], RE_DIGITAL: /^[0-9a-f]{8}$/, LIMITE_ERROS: 1000000,
    ctxQuestoes: { digitais: { '11111111': true, '44444444': true }, lista: [{ digital: '11111111', gabarito: 'C' }, { digital: '44444444', gabarito: 'D' }], modo: mode, versao: 'nova' },
    inteiroValido: (n, max = Number.MAX_SAFE_INTEGER) => Number.isSafeInteger(n) && n >= 0 && n <= max,
    registrarCorrompido: () => () => {},
    armazenamento: {
      ler: () => typeof disk === 'string' ? disk : JSON.stringify(disk),
      lerJSON: () => JSON.parse(JSON.stringify(disk)),
      gravarJSON: (_key, value) => { disk = JSON.parse(JSON.stringify(value)); return true; },
      apagar: () => { deleted = true; disk = null; return true; }
    }
  };
  vm.createContext(sandbox);
  vm.runInContext(actualFunctions, sandbox, { timeout: 1000 });
  const first = JSON.parse(JSON.stringify(sandbox.lerEstadoModulo()));
  const summary = JSON.parse(JSON.stringify(sandbox.resumirEstado(first)));
  sandbox.alterarEstado(state => { state.respostas['44444444'] = 'D'; });
  return { first, summary, saved: disk, deleted, memory: sandbox.ctxQuestoes.estado };
}
const e1 = run('e1', 'estudo', seed);
check('E1 mantém resposta antiga válida', e1.first.respostas['22222222'] === 'B', e1.first.respostas);
check('E1 mantém histórico de erros antigo', e1.first.erros['22222222'] === 4, e1.first.erros);
check('E1 mantém marcação antiga do simulado', e1.first.simulado.marcadas['22222222'] === 'B', e1.first.simulado);
check('E1 não atribui resposta antiga à versão nova', !('44444444' in e1.first.respostas), e1.first.respostas);
check('E1 só conta respostas atuais', e1.summary.respondidas === 1 && e1.summary.acertos === 1, e1.summary);
check('E1 salva resposta nova junto da antiga', e1.saved.respostas['22222222'] === 'B' && e1.saved.respostas['44444444'] === 'D', e1.saved.respostas);
check('E1 mantém erros e marcações antigos ao salvar outra resposta', e1.saved.erros['22222222'] === 4 && e1.saved.simulado.marcadas['22222222'] === 'B', e1.saved);
check('E1 resumo salvo só inclui versões atuais', e1.saved.resumo.respondidas === 2 && e1.saved.resumo.acertos === 2, e1.saved.resumo);
check('E1 rejeita letra e chave inválidas', !('33333333' in e1.first.respostas) && !('invalida' in e1.first.respostas), e1.first.respostas);
const sim = run('e1', 'simulado', seed);
check('E1 simulado só conta versões atuais', sim.summary.respondidas === 1 && sim.summary.acertos === 1, sim.summary);
const e2 = run('e2', 'estudo', seed);
check('E2 mantém filtro anterior de respostas', !('22222222' in e2.first.respostas), e2.first.respostas);
check('E2 mantém filtro anterior de erros', !('22222222' in e2.first.erros), e2.first.erros);
check('E2 mantém filtro anterior de simulado', !('22222222' in e2.first.simulado.marcadas), e2.first.simulado);
const invalid = run('e1', 'estudo', '{JSON ilegível');
check('E1 não sobrescreve JSON ilegível', invalid.saved === '{JSON ilegível' && !invalid.deleted, invalid.saved);
check('E1 retém nova tentativa na memória com JSON ilegível', invalid.memory.respostas['44444444'] === 'D', invalid.memory);
const result = {
  id: 'BAN-07', data: '2026-10-28', responsavel: '/root, coordenador',
  metodo: 'Execução em Node VM das funções reais extraídas de curso.js, com armazenamento controlado. Casos esperados independentes da implementação, sem acesso ao armazenamento do usuário.',
  sha256_curso_js: createHash('sha256').update(source).digest('hex'),
  total: tests.length, falhas: tests.filter(t => !t.ok), testes: tests,
  limites: ['Não simula DOM nem falhas da camada real de localStorage.', 'Os cenários de erro, concorrência e armazenamento completo pertencem à suíte técnica do Corretor/Auditor.']
};
await fs.writeFile(path.join(here, 'persistencia-q-coordenador-r1.json'), JSON.stringify(result, null, 2) + '\n');
console.log(JSON.stringify({ testes: result.total, falhas: result.falhas }, null, 2));
process.exitCode = result.falhas.length ? 1 : 0;
