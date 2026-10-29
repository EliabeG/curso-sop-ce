import fs from 'node:fs/promises';
import path from 'node:path';
import vm from 'node:vm';
import { fileURLToPath } from 'node:url';
import { parseHtml, isInventoryArticle, decodeHtml, sha256 } from '../../../inventario/validar-inventario.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(here, '../../../../..');
const base = path.join(root, 'auditoria/termodinamica/evidencias/BAN-07');
const js = await fs.readFile(path.join(root, 'assets/curso.js'), 'utf8');
const fn = (name, next) => js.slice(js.indexOf('  function ' + name + '('), js.indexOf('  function ' + next + '('));
const sandbox = { Array, String, Math };
vm.createContext(sandbox);
vm.runInContext("var SEPARADOR='␞';\n" + fn('paraArray', 'criar') + fn('normalizarDigital', 'formatarTempo') + fn('digitalDoBanco', 'iniciarBanco'), sandbox);

function adapter(doc, source) {
  const adapted = new Map();
  function wrap(n) {
    if (adapted.has(n)) return adapted.get(n);
    const out = { nodeType: 1, localName: n.tag, tagName: n.tag.toUpperCase(),
      hasAttribute: key => key in n.attrs, getAttribute: key => n.attrs[key] ?? null,
      value: n.attrs.value, id: n.attrs.id,
      dataset: { crGabarito: n.attrs['data-cr-gabarito'] }, childNodes: [],
      querySelectorAll: selector => doc.nodes.filter(v => v !== n && v.start >= n.start && v.end <= n.end && match(v, selector)).map(wrap),
      querySelector: selector => out.querySelectorAll(selector)[0] ?? null,
      closest: selector => { let p = n; while (p) { if (match(p, selector)) return wrap(p); p = p.parent; } return null; }
    };
    adapted.set(n, out);
    const close = doc.html.lastIndexOf('</', n.end - 1);
    const contentEnd = close >= n.openEnd ? close : n.openEnd;
    let at = n.openEnd;
    for (const child of n.children) {
      if (child.start > at) out.childNodes.push({ nodeType: 3, nodeValue: decodeHtml(doc.html.slice(at, child.start)) });
      out.childNodes.push(wrap(child)); at = child.end;
    }
    if (contentEnd > at) out.childNodes.push({ nodeType: 3, nodeValue: decodeHtml(doc.html.slice(at, contentEnd)) });
    return out;
  }
  function match(n, selector) {
    if (selector.startsWith('.')) return (n.attrs.class ?? '').split(/\s+/).includes(selector.slice(1));
    if (selector === 'input[type="radio"]') return n.tag === 'input' && n.attrs.type === 'radio';
    return n.tag === selector;
  }
  return wrap(source);
}

function readItems(html) {
  const doc = parseHtml(html);
  return doc.nodes.filter(isInventoryArticle).map(n => {
    const item = adapter(doc, n);
    const id = n.attrs.id;
    const q = id.startsWith('q-');
    let digital = null;
    const key = n.attrs['data-gabarito'] ?? n.attrs['data-cr-gabarito'] ?? null;
    if (q) {
      const statement = item.querySelector('.q-enunciado');
      const list = item.querySelector('.q-alternativas');
      const options = list.childNodes.filter(v => v.localName === 'li');
      const parts = [sandbox.normalizarDigital(sandbox.textoDaDigital(statement)), ...options.map(li => sandbox.normalizarDigital(sandbox.textoDaDigital(li))), key];
      digital = sandbox.fnv1a(parts.join('␞'));
    } else if (id.startsWith('av-') || id.startsWith('cr-')) digital = sandbox.digitalDoBanco(item);
    return { id, chave: key, digital, sha256_artigo: sha256(html.slice(n.start, n.end)) };
  });
}

const before = readItems(await fs.readFile(path.join(base, 'antes/modulos/e1-termodinamica.html'), 'utf8'));
const after = readItems(await fs.readFile(path.join(root, 'modulos/e1-termodinamica.html'), 'utf8'));
const plan = JSON.parse(await fs.readFile(path.join(base, 'diagnostico-197-integrado-r1.json'), 'utf8')).implementacao_proposta;
const registryFile = path.join(root, 'assets/registro.js');
const registryText = await fs.readFile(path.join(base, 'antes/assets/registro.js'), 'utf8');
const regContext = { window: {} }; vm.runInNewContext(registryText, regContext);
const oldRegistry = regContext.window.CURSO_REGISTRO.modulos.e1.questoes;
const expectedRegistry = Object.fromEntries(before.filter(r => r.id.startsWith('q-')).map(r => [r.digital, r.chave]));
if (JSON.stringify(Object.entries(oldRegistry).sort()) !== JSON.stringify(Object.entries(expectedRegistry).sort())) {
  console.log(JSON.stringify({ registro: oldRegistry, calculado: expectedRegistry }));
  throw new Error('Adaptador de digital diverge do registro Q de base; não prosseguir.');
}
const rows = before.map((old, i) => {
  const now = after[i];
  if (old.id !== now.id || old.chave !== now.chave) throw new Error('ID/chave divergente: ' + old.id);
  return { id: old.id, chave: old.chave, antes: old, depois: now, artigo_alterado: old.sha256_artigo !== now.sha256_artigo, digital_alterada: old.digital !== now.digital };
});
const changedArticles = rows.filter(r => r.artigo_alterado).map(r => r.id);
const changedIdentities = rows.filter(r => r.digital_alterada).map(r => r.id);
for (const [got, expected, label] of [[changedArticles, plan.artigos, 'artigos'], [changedIdentities, plan.novas_digitais, 'digitais']]) {
  if (JSON.stringify([...got].sort()) !== JSON.stringify([...expected].sort())) throw new Error('Delta inesperado de ' + label + ': ' + JSON.stringify(got));
}
const map = { id: 'BAN-07', rodada: 1, data: '2026-10-28', metodo: 'Funções reais normalizarDigital/textoDaDigital/fnv1a/digitalDoBanco em VM; adaptador DOM sobre parser canônico, confrontado com as30digitais Q da base.', artigos: rows.length, artigos_alterados: changedArticles, digitais_alteradas: changedIdentities, letras_migradas: false, registros: rows };
await fs.writeFile(path.join(base, 'mapa-identidades-r1.json'), JSON.stringify(map, null, 2) + '\n');
const currentRegistry = Object.fromEntries(after.filter(r => r.id.startsWith('q-')).map(r => [r.digital, r.chave]));
const e1Start = registryText.indexOf('"e1": {');
const start = registryText.indexOf('"questoes": {', e1Start) + '"questoes": '.length;
const end = registryText.indexOf('\n      }', start) + '\n      }'.length;
const replacement = JSON.stringify(currentRegistry, null, 2).split('\n').map((line, i) => i ? '      ' + line : line).join('\n');
await fs.writeFile(registryFile, registryText.slice(0, start) + replacement + registryText.slice(end));
console.log(JSON.stringify({ artigos: rows.length, artigos_alterados: changedArticles.length, digitais_alteradas: changedIdentities.length, mapa_sha256: sha256(JSON.stringify(map, null, 2) + '\n') }));
