import fs from 'node:fs/promises';
import path from 'node:path';
import vm from 'node:vm';
import { fileURLToPath } from 'node:url';
import { parseHtml, isInventoryArticle, sha256, validateInventory, decodeHtml } from '../../inventario/validar-inventario.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(here, '../../../..');
const checks = [];
const check = (criterio, ok, detalhe) => checks.push({ criterio, ok: Boolean(ok), detalhe });
const read = rel => fs.readFile(path.join(root, rel));
const json = async rel => JSON.parse(await fs.readFile(path.join(root, rel), 'utf8'));
const relBase = 'auditoria/termodinamica/evidencias/BAN-07/';
const snapshot = await json(relBase + 'snapshot-antes.json');
const baseline = await json(relBase + 'baseline-retomada-coordenador-r1.json');
const permitted = new Set(['modulos/e1-termodinamica.html', 'assets/curso.js', 'assets/registro.js']);
const changed = [];
for (const row of baseline.arquivos) {
  const hash = sha256(await read(row.arquivo));
  if (hash !== row.sha256) changed.push(row.arquivo);
  check('arquivo preservado ou autorizado: ' + row.arquivo, hash === row.sha256 || permitted.has(row.arquivo), hash);
}
for (const row of snapshot.recursos_rastreaveis_preservados_por_hash) {
  check('recurso preservado: ' + row.arquivo, sha256(await read(row.arquivo)) === row.sha256, row.sha256);
}
const beforeHtml = await fs.readFile(path.join(here, 'antes/modulos/e1-termodinamica.html'), 'utf8');
const afterHtml = await fs.readFile(path.join(root, 'modulos/e1-termodinamica.html'), 'utf8');
const before = parseHtml(beforeHtml);
const after = parseHtml(afterHtml);
const articles = doc => doc.nodes.filter(isInventoryArticle);
const prior = articles(before), current = articles(after);
check('197 artigos antes e depois', prior.length === 197 && current.length === 197, [prior.length, current.length]);
check('IDs e ordem preservados', JSON.stringify(prior.map(n => n.attrs.id)) === JSON.stringify(current.map(n => n.attrs.id)), current.map(n => n.attrs.id));
const raw = (doc, n) => doc.html.slice(n.start, n.end);
const currentById = new Map(current.map(n => [n.attrs.id, n]));
const changedArticles = [];
const expectedQ = [2, 9, 13, 15, 16, 18, 19, 24, 26, 28].map(n => 'q-e1-' + String(n).padStart(2, '0'));
const expectedAV = [8, 10, 17, 18, 33, 35, 37, 38, 45, 48, 50, 57, 58, 64, 73].map(n => 'av-e1-' + String(n).padStart(2, '0'));
const expectedArticles = [...expectedQ, ...expectedAV].sort();
for (const old of prior) {
  const now = currentById.get(old.attrs.id);
  if (!now) continue;
  const id = old.attrs.id;
  const same = raw(before, old) === raw(after, now);
  if (!same) changedArticles.push(id);
  if (id.startsWith('cr-') || id.startsWith('fun')) check('artigo oficial/aberto preservado: ' + id, same, sha256(raw(after, now)));
  check('chave preservada: ' + id, old.attrs['data-gabarito'] === now.attrs['data-gabarito'] && old.attrs['data-cr-gabarito'] === now.attrs['data-cr-gabarito'], now.attrs['data-gabarito'] ?? now.attrs['data-cr-gabarito'] ?? 'rubrica aberta');
}
check('exatamente os 25 artigos previstos no plano', JSON.stringify([...changedArticles].sort()) === JSON.stringify(expectedArticles), changedArticles);
function withoutArticles(doc) {
  let text = doc.html;
  for (const n of articles(doc).reverse()) text = text.slice(0, n.start) + '<!-- ' + n.attrs.id + ' -->' + text.slice(n.end);
  return text;
}
check('HTML fora dos artigos preservado', withoutArticles(before) === withoutArticles(after), null);
const math = doc => doc.nodes.filter(n => n.tag === 'math').map(n => sha256(raw(doc, n)));
check('MathML preservado integralmente', JSON.stringify(math(before)) === JSON.stringify(math(after)), [math(before).length, math(after).length]);
function registry(text) {
  const sandbox = { window: {} };
  vm.runInNewContext(text, sandbox, { timeout: 1000 });
  return JSON.parse(JSON.stringify(sandbox.window.CURSO_REGISTRO));
}
const oldReg = registry(await fs.readFile(path.join(here, 'antes/assets/registro.js'), 'utf8'));
const newReg = registry(await fs.readFile(path.join(root, 'assets/registro.js'), 'utf8'));
const hasClass = (n, c) => (n.attrs.class ?? '').split(/\s+/).includes(c);
const within = (doc, p, pred) => doc.nodes.filter(n => n.start > p.start && n.end <= p.end && pred(n));
const norm = value => value.replace(/[ \t\n\r\f\v\u00a0]+/g, ' ').replace(/^ | $/g, '');
function text(doc, node) {
  if (node.tag === 'math' && 'data-formula-original' in node.attrs) return node.attrs['data-formula-original'];
  let result = '', cursor = node.openEnd;
  for (const child of node.children) {
    result += decodeHtml(doc.html.slice(cursor, child.start).replace(/<!--[\s\S]*?-->/g, ''));
    result += text(doc, child);
    cursor = child.end;
  }
  result += decodeHtml(doc.html.slice(cursor, node.end).replace(/<!--[\s\S]*?-->/g, '').replace(/<[^>]*>/g, ''));
  return result;
}
function fnv(value) {
  let hash = 0x811c9dc5;
  for (const char of value) { hash ^= char.codePointAt(0); hash = Math.imul(hash, 0x01000193) >>> 0; }
  return hash.toString(16).padStart(8, '0');
}
function fingerprint(doc, item) {
  const q = item.attrs.id.startsWith('q-');
  const en = within(doc, item, n => hasClass(n, q ? 'q-enunciado' : 'cr-enunciado'))[0];
  const parts = [norm(text(doc, en))];
  if (q) {
    const list = within(doc, item, n => hasClass(n, 'q-alternativas'))[0];
    for (const li of list.children.filter(n => n.tag === 'li')) parts.push(norm(text(doc, li)));
    parts.push(item.attrs['data-gabarito']);
  } else {
    for (const img of within(doc, en, n => n.tag === 'img')) parts.push(img.attrs.src ?? '', img.attrs.alt ?? '');
    for (const input of within(doc, item, n => n.tag === 'input' && n.attrs.type === 'radio')) {
      let label = input.parent;
      while (label && label.tag !== 'label') label = label.parent;
      parts.push(input.attrs.value, norm(text(doc, label)));
    }
    parts.push(item.attrs['data-cr-gabarito']);
  }
  return fnv(parts.join('␞'));
}
const identities = prior.filter(n => /^(q|cr|av)-/.test(n.attrs.id)).map(n => ({ id: n.attrs.id, antes: fingerprint(before, n), depois: fingerprint(after, currentById.get(n.attrs.id)) }));
for (const [docName, reg, key] of [['antes', oldReg, 'antes'], ['depois', newReg, 'depois']]) {
  const map = Object.fromEntries(identities.filter(x => x.id.startsWith('q-')).map(x => [x[key], currentById.get(x.id).attrs['data-gabarito']]));
  check('digitais Q reproduzem o registro ' + docName, Object.keys(map).length === 30 && Object.keys(reg.modulos.e1.questoes).length === 30 && Object.entries(map).every(([d, g]) => reg.modulos.e1.questoes[d] === g), map);
}
const changedIds = identities.filter(x => x.antes !== x.depois).map(x => x.id).sort();
const commentOnly = new Set(['q-e1-13', 'q-e1-18', 'av-e1-17', 'av-e1-18', 'av-e1-64']);
check('exatamente 20 novas digitais previstas', JSON.stringify(changedIds) === JSON.stringify(expectedArticles.filter(id => !commentOnly.has(id))), changedIds);
delete oldReg.modulos.e1.questoes;
delete newReg.modulos.e1.questoes;
check('registro fora das digitais Q de E1 preservado', JSON.stringify(oldReg) === JSON.stringify(newReg), null);
const validation = await validateInventory({ rootDir: root });
check('validador canônico do inventário', validation.ok, validation);
const result = {
  id: 'BAN-07', rodada: 1, data: '2026-10-28',
  responsavel: '/root, coordenador; conferência técnica de apoio, sem parecer de aprovação',
  arquivos_de_produto_alterados: changed, artigos_alterados: changedArticles, identidades: identities,
  html_sha256: sha256(afterHtml), verificacoes: checks.length,
  falhas: checks.filter(c => !c.ok), checks,
  limites: ['A comparação estrutural não demonstra sozinha correção científica.', 'Não executa navegação, armazenamento real ou aplicação com estudantes.']
};
await fs.writeFile(path.join(here, 'conferencia-coordenador-r1.json'), JSON.stringify(result, null, 2) + '\n');
console.log(JSON.stringify({ arquivos_alterados: changed, artigos_alterados: changedArticles, verificacoes: checks.length, falhas: result.falhas }, null, 2));
process.exitCode = result.falhas.length ? 1 : 0;
