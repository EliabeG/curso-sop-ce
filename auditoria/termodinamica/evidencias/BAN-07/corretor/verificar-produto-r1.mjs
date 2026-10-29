import fs from 'node:fs/promises';
import path from 'node:path';
import vm from 'node:vm';
import { fileURLToPath } from 'node:url';
import { parseHtml, isInventoryArticle, validateInventory, sha256 } from '../../../inventario/validar-inventario.mjs';
const here = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(here, '../../../../..');
const base = path.join(root, 'auditoria/termodinamica/evidencias/BAN-07');
const read = rel => fs.readFile(path.join(root, rel), 'utf8');
const json = async p => JSON.parse(await fs.readFile(p, 'utf8'));
const plan = (await json(path.join(base, 'diagnostico-197-integrado-r1.json'))).implementacao_proposta;
const checks = [];
const check = (criterio, ok, detalhe) => checks.push({ criterio, ok: Boolean(ok), detalhe });
const snapshot = await json(path.join(base, 'snapshot-antes.json'));
const expectedFiles = ['modulos/e1-termodinamica.html', 'assets/curso.js', 'assets/registro.js', 'auditoria/termodinamica/inventario/inventario-questoes.json', 'auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md'];
const actualFiles = [];
for (const entry of snapshot.arquivos) {
  if (sha256(await read(entry.arquivo)) !== entry.sha256) actualFiles.push(entry.arquivo);
}
check('Somente cinco arquivos de produto previstos foram alterados', JSON.stringify(actualFiles.sort()) === JSON.stringify(expectedFiles.sort()), actualFiles);
const beforeHtml = await fs.readFile(path.join(base, 'antes/modulos/e1-termodinamica.html'), 'utf8');
const afterHtml = await read('modulos/e1-termodinamica.html');
const before = parseHtml(beforeHtml), after = parseHtml(afterHtml);
const articles = doc => doc.nodes.filter(isInventoryArticle);
const old = articles(before), now = articles(after);
const raw = (doc, n) => doc.html.slice(n.start, n.end);
check('197IDs e ordem preservados', old.length === 197 && JSON.stringify(old.map(n => n.attrs.id)) === JSON.stringify(now.map(n => n.attrs.id)), now.length);
const changes = [];
for (let i = 0; i < old.length; i++) {
  const a = old[i], b = now[i];
  if (raw(before, a) !== raw(after, b)) changes.push(a.attrs.id);
  check('Chave preservada ' + a.attrs.id, a.attrs['data-gabarito'] === b.attrs['data-gabarito'] && a.attrs['data-cr-gabarito'] === b.attrs['data-cr-gabarito'], null);
}
check('Exatamente25artigos previstos', JSON.stringify(changes.sort()) === JSON.stringify([...plan.artigos].sort()), changes);
const removeArticles = doc => { let s = doc.html; for (const n of articles(doc).reverse()) s = s.slice(0, n.start) + '<!--' + n.attrs.id + '-->' + s.slice(n.end); return s; };
check('HTML fora dos197artigos preservado', removeArticles(before) === removeArticles(after), null);
const maths = doc => doc.nodes.filter(n => n.tag === 'math').map(n => sha256(raw(doc, n)));
check('734elementosMathML preservados integralmente', maths(before).length === 734 && JSON.stringify(maths(before)) === JSON.stringify(maths(after)), maths(after).length);
const replacements = (await json(path.join(here, 'delta-artigos-r1.json'))).substituicoes;
let reconstructed = beforeHtml;
for (const entry of replacements) {
  const doc = parseHtml(reconstructed), n = articles(doc).find(n => n.attrs.id === entry.id);
  const article = raw(doc, n), pieces = article.split(entry.antes);
  check('Quantidade da substituição ' + entry.id, pieces.length - 1 === entry.ocorrencias, entry.motivo);
  reconstructed = reconstructed.slice(0, n.start) + pieces.join(entry.depois) + reconstructed.slice(n.end);
}
check('58substituições reproduzem integralmente oHTML final', reconstructed === afterHtml, sha256(reconstructed));
const priorInventory = await json(path.join(base, 'antes/auditoria/termodinamica/inventario/inventario-questoes.json'));
const inventory = await json(path.join(root, 'auditoria/termodinamica/inventario/inventario-questoes.json'));
const changedRecords = inventory.itens.filter((r, i) => JSON.stringify(r) !== JSON.stringify(priorInventory.itens[i])).map(r => r.id);
check('Somente25registros previstos do inventário mudaram', JSON.stringify(changedRecords.sort()) === JSON.stringify([...plan.artigos].sort()), changedRecords);
const reg = source => { const s = { window: {} }; vm.runInNewContext(source, s); return JSON.parse(JSON.stringify(s.window.CURSO_REGISTRO)); };
const oldRegistry = reg(await fs.readFile(path.join(base, 'antes/assets/registro.js'), 'utf8'));
const newRegistry = reg(await read('assets/registro.js'));
delete oldRegistry.modulos.e1.questoes; delete newRegistry.modulos.e1.questoes;
check('Registro fora das digitaisQ E1 preservado', JSON.stringify(oldRegistry) === JSON.stringify(newRegistry), null);
const validation = await validateInventory({ rootDir: root });
check('Validador canônico', validation.ok, validation);
await fs.writeFile(path.join(here, 'validacao-inventario-r1.json'), JSON.stringify(validation, null, 2) + '\n');
const report = { id: 'BAN-07', rodada: 1, data: '2026-10-28', autor: '/root/corretor_aaa', html_sha256: sha256(afterHtml), arquivos_alterados: actualFiles, artigos_alterados: changes, verificacoes: checks.length, falhas: checks.filter(c => !c.ok), resultados: checks, limite: 'Conferência estrutural do Corretor; ciência individual e navegador são evidências separadas; não é parecer independente.' };
await fs.writeFile(path.join(here, 'verificacao-produto-r1.json'), JSON.stringify(report, null, 2) + '\n');
console.log(JSON.stringify({ verificacoes: checks.length, falhas: report.falhas }, null, 2));
process.exitCode = report.falhas.length ? 1 : 0;
