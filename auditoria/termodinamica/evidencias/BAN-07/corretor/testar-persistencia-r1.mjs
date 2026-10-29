import fs from 'node:fs/promises';
import path from 'node:path';
import vm from 'node:vm';
import assert from 'node:assert/strict';
import { fileURLToPath } from 'node:url';
import { sha256 } from '../../../inventario/validar-inventario.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(here, '../../../../..');
const source = await fs.readFile(path.join(root, 'assets/curso.js'), 'utf8');
const between = (from, to) => source.slice(source.indexOf(from), source.indexOf(to, source.indexOf(from)));
const storeSource = between('  var armazenamento = (function () {', '  function registrarCorrompido(');
const stateSource = between('  var leituraQuestoesE1Invalida = false;', '  function prepararQuestao(');
const corruptSource = between('  function registrarCorrompido(', '  var PREFIXO_V1');
const warningSource = between('  function atualizarAvisoPlacar(', '  function textoTempoSimulado(');
const portalSource = between('  function progressoDoModulo(', '  function mostrarProgressoPortal(');
const results = [];
const copy = v => JSON.parse(JSON.stringify(v));
class Store {
  constructor() { this.map = new Map(); this.failRead = false; this.failWrite = false; }
  getItem(k) { if (this.failRead) throw new Error('leitura bloqueada'); return this.map.get(k) ?? null; }
  setItem(k, v) { if (this.failWrite) { const e = new Error('cota'); e.name = 'QuotaExceededError'; throw e; } this.map.set(k, String(v)); }
  removeItem(k) { if (this.failWrite) throw new Error('gravação bloqueada'); this.map.delete(k); }
  key(i) { return [...this.map.keys()][i] ?? null; }
  get length() { return this.map.size; }
}
function context(module = 'e1') {
  const store = new Store();
  const ctx = {
    window: { localStorage: store, console: { warn() {} }, CURSO_REGISTRO: { modulos: { [module]: { tipo: 'teoria', questoes: { '11112222': 'A', '33334444': 'B' } } } } },
    console: { warn() {} },
    MODULO: module, PREFIXO: 'sopmec:v2:', LETRAS: ['A', 'B', 'C', 'D', 'E'], RE_DIGITAL: /^[a-f0-9]{8}$/,
    LIMITE_ERROS: Number.MAX_SAFE_INTEGER,
    seguro(_n, f) { try { f(); } catch {} },
    inteiroValido(n, max) { return typeof n === 'number' && Number.isFinite(n) && Math.floor(n) === n && n >= 0 && (max === undefined || n <= max); },
    ctxQuestoes: { digitais: { '11112222': true, '33334444': true }, lista: [{ digital: '11112222', gabarito: 'A' }, { digital: '33334444', gabarito: 'B' }], modo: 'estudo', versao: 'atual', estado: null, placar: { aviso: { textContent: '', hidden: true } } }
  };
  vm.createContext(ctx);
  vm.runInContext(storeSource + stateSource + corruptSource + warningSource + portalSource, ctx);
  return { ctx, store, key: 'sopmec:v2:mod:' + module };
}
function test(name, run) {
  try { run(); results.push({ criterio: name, ok: true }); }
  catch (error) { results.push({ criterio: name, ok: false, erro: error.message }); }
}
const base = { v: 2, respostas: { 'aaaabbbb': 'C', '11112222': 'A' }, erros: { 'aaaabbbb': 3, '11112222': 1 }, simulado: { inicio: 1, fim: null, corrigido: false, marcadas: { 'aaaabbbb': 'D', '11112222': 'A' } } };
test('E1 conserva respostas/erros/marcações antigas sem contá-las; gravação seguinte e portal concordam', () => {
  const { ctx, store, key } = context(); store.setItem(key, JSON.stringify(base));
  ctx.ctxQuestoes.estado = ctx.lerEstadoModulo();
  assert.equal(ctx.ctxQuestoes.estado.respostas.aaaabbbb, 'C');
  assert.equal(ctx.ctxQuestoes.estado.erros.aaaabbbb, 3);
  assert.equal(ctx.ctxQuestoes.estado.simulado.marcadas.aaaabbbb, 'D');
  assert.equal(ctx.resumirEstado(ctx.ctxQuestoes.estado).respondidas, 1);
  ctx.alterarEstado(e => { e.respostas['33334444'] = 'B'; });
  const saved = JSON.parse(store.getItem(key));
  assert.equal(saved.respostas.aaaabbbb, 'C'); assert.equal(saved.erros.aaaabbbb, 3); assert.equal(saved.simulado.marcadas.aaaabbbb, 'D');
  assert.equal(saved.resumo.respondidas, 2); assert.equal(saved.resumo.acertos, 2);
  assert.equal(ctx.progressoDoModulo('e1').respondidas, 2); assert.equal(ctx.progressoDoModulo('e1').acertos, 2);
  ctx.atualizarAvisoPlacar(); assert.match(ctx.ctxQuestoes.placar.aviso.textContent, /versões anteriores preservadas/);
});
test('E1 apenas histórico não é estado vazio e não é apagado por gravação sem novas respostas', () => {
  const { ctx, store, key } = context(); const old = { v: 2, respostas: { aaaabbbb: 'C' }, erros: {}, simulado: null };
  store.setItem(key, JSON.stringify(old)); ctx.ctxQuestoes.estado = ctx.lerEstadoModulo();
  assert.equal(ctx.estadoVazio(ctx.ctxQuestoes.estado), false); assert.equal(ctx.resumirEstado(ctx.ctxQuestoes.estado).respondidas, 0);
  ctx.alterarEstado(() => {}); assert.equal(JSON.parse(store.getItem(key)).respostas.aaaabbbb, 'C');
});
test('Resumo de simulado usa somente marcações das digitais vigentes', () => {
  const { ctx, store, key } = context(); store.setItem(key, JSON.stringify(base)); ctx.ctxQuestoes.modo = 'simulado';
  ctx.ctxQuestoes.estado = ctx.lerEstadoModulo(); assert.equal(ctx.resumirEstado(ctx.ctxQuestoes.estado).respondidas, 1);
  assert.equal(ctx.resumirEstado(ctx.ctxQuestoes.estado).acertos, 1);
});
test('E1 sem histórico não mostra aviso de versões anteriores', () => {
  const { ctx, store, key } = context(); store.setItem(key, JSON.stringify({ v: 2, respostas: { '11112222': 'A' }, erros: {}, simulado: null }));
  ctx.ctxQuestoes.estado = ctx.lerEstadoModulo(); ctx.atualizarAvisoPlacar(); assert.equal(ctx.ctxQuestoes.placar.aviso.hidden, true);
});
for (const malformed of ['{invalido', 'null', '[]', '{"v":9,"respostas":{}}', '{"v":2,"respostas":[]}']) {
  test('E1 preserva disco ilegível e duas tentativas novas em memória: ' + malformed, () => {
    const { ctx, store, key } = context(); store.setItem(key, malformed); ctx.ctxQuestoes.estado = ctx.lerEstadoModulo();
    ctx.alterarEstado(e => { e.respostas['11112222'] = 'A'; });
    ctx.alterarEstado(e => { e.respostas['33334444'] = 'B'; });
    assert.equal(store.getItem(key), malformed); assert.equal(ctx.ctxQuestoes.estado.respostas['11112222'], 'A'); assert.equal(ctx.ctxQuestoes.estado.respostas['33334444'], 'B');
    ctx.atualizarAvisoPlacar(); assert.match(ctx.ctxQuestoes.placar.aviso.textContent, /formato ilegível/);
  });
}
test('Leitura bloqueada com dados anteriores nunca sobrescreve o disco', () => {
  const { ctx, store, key } = context(); const original = JSON.stringify(base); store.map.set(key, original); store.failRead = true;
  ctx.ctxQuestoes.estado = ctx.lerEstadoModulo(); ctx.alterarEstado(e => { e.respostas['33334444'] = 'B'; });
  assert.equal(store.map.get(key), original); assert.equal(ctx.ctxQuestoes.estado.respostas['33334444'], 'B');
});
test('Falha de gravação conserva disco e histórico, com nova resposta na página', () => {
  const { ctx, store, key } = context(); const original = JSON.stringify(base); store.map.set(key, original);
  ctx.ctxQuestoes.estado = ctx.lerEstadoModulo(); store.failWrite = true;
  ctx.alterarEstado(e => { e.respostas['33334444'] = 'B'; });
  assert.equal(store.map.get(key), original); assert.equal(ctx.ctxQuestoes.estado.respostas.aaaabbbb, 'C'); assert.equal(ctx.ctxQuestoes.estado.respostas['33334444'], 'B');
});
test('Outro módulo conserva filtragem anterior por digitais vigentes', () => {
  const { ctx, store, key } = context('e2'); store.setItem(key, JSON.stringify(base)); ctx.ctxQuestoes.estado = ctx.lerEstadoModulo();
  assert.equal(ctx.ctxQuestoes.estado.respostas.aaaabbbb, undefined); assert.equal(ctx.ctxQuestoes.estado.erros.aaaabbbb, undefined); assert.equal(ctx.ctxQuestoes.estado.simulado.marcadas.aaaabbbb, undefined);
  ctx.alterarEstado(e => { e.respostas['33334444'] = 'B'; });
  // O merge da camada já preservava campos de disco não presentes no patch; a leitura ativa continua filtrada.
  assert.equal(ctx.ctxQuestoes.estado.respostas.aaaabbbb, undefined); assert.equal(JSON.parse(store.getItem(key)).resumo.respondidas, 2);
});
test('Entradas inválidas não entram no histórico preservado', () => {
  const { ctx, store, key } = context(); const invalid = copy(base); invalid.respostas.bad = 'A'; invalid.respostas['ccccdddd'] = 'Z'; invalid.erros['ccccdddd'] = -1;
  store.setItem(key, JSON.stringify(invalid)); const got = ctx.lerEstadoModulo(); assert.equal(got.respostas.bad, undefined); assert.equal(got.respostas.ccccdddd, undefined); assert.equal(got.erros.ccccdddd, undefined);
});

// Executa as funções reais fechadas do banco AV, com DOM mínimo apenas nos pontos utilizados.
const avRead = between('    function lerRespostas()', '    function aplicarPendencias(');
const avPatch = between('    function aplicarPendencias(', '    function atualizarRespostas(');
const avUpdate = between('    function atualizarRespostas(', '    try {\n      atualizarRespostas(lerRespostas());');
const avSave = between('    function salvar(id, valor)', '    function mostrarResposta(');
const avWarning = between('    function informarArmazenamento()', '    function lerRespostas(');
function avContext() {
  const store = new Store(); const key = 'sopmec:avalia:v2:e1';
  const ctx = { window: { localStorage: store }, chave: key, aviso: { textContent: '' }, gravacao: true, legado: false, tentativasAnteriores: false, respostas: {}, pendencias: {}, digitais: { av1: '11112222', av2: '33334444' }, itens: ['av1', 'av2'].map(id => ({ id, querySelector: sel => /input\[value="[A-E]"\]/.test(sel) ? {} : null })), idModulo: () => 'e1', mostrarResposta() {} };
  vm.createContext(ctx); vm.runInContext(avRead + avPatch + avUpdate + avSave + avWarning, ctx);
  return { ctx, store, key };
}
test('AV conserva histórico sem preencher versão nova, avisa e salva a próxima resposta sem migrar letra', () => {
  const { ctx, store, key } = avContext(); store.setItem(key, JSON.stringify({ v: 2, respostas: { aaaabbbb: 'D', '11112222': 'A' } }));
  ctx.atualizarRespostas(ctx.lerRespostas()); assert.equal(ctx.respostas.av1, 'A'); assert.equal(ctx.respostas.av2, undefined);
  ctx.informarArmazenamento(); assert.match(ctx.aviso.textContent, /versões anteriores preservadas/);
  ctx.salvar('av2', 'B'); const saved = JSON.parse(store.getItem(key)); assert.equal(saved.respostas.aaaabbbb, 'D'); assert.equal(saved.respostas['33334444'], 'B');
});
test('AV JSON inválido e leitura bloqueada preservam original com nova ação pendente', () => {
  for (const blocked of [false, true]) {
    const { ctx, store, key } = avContext(); const original = blocked ? JSON.stringify({ v: 2, respostas: { aaaabbbb: 'D' } }) : '{quebrado';
    store.map.set(key, original); store.failRead = blocked; ctx.salvar('av2', 'B'); assert.equal(store.map.get(key), original); assert.equal(ctx.respostas.av2, 'B'); assert.equal(ctx.gravacao, false);
  }
});
const report = { id: 'BAN-07', rodada: 1, data: '2026-10-28', autor: '/root/corretor_aaa', metodo: 'Node/VM com funções reais e camada real de armazenamento de curso.js; localStorage e DOM mínimo simulados. Não é teste de navegador.', sha256_curso_js: sha256(source), casos: results.length, falhas: results.filter(r => !r.ok), resultados: results };
await fs.writeFile(path.join(here, 'testes-persistencia-r1.json'), JSON.stringify(report, null, 2) + '\n');
console.log(JSON.stringify({ casos: report.casos, falhas: report.falhas }, null, 2));
process.exitCode = report.falhas.length ? 1 : 0;
