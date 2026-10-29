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

const source=await fs.readFile(path.join(root,'modulos/e1-termodinamica.html'),'utf8');
const candidatesDir=path.join(root,'auditoria/termodinamica/evidencias/BAN-08/propostas-av42-av45-r1');
const before=readItems(source); let combined=source; const diffs=[];
for (const n of [42,45,52]) {
 const id=`av-e1-${n}`; const doc=parseHtml(source); const item=doc.ids.get(id)[0]; const original=source.slice(item.start,item.end);
 const candidate=await fs.readFile(path.join(candidatesDir,`AV${n}-candidata.html`),'utf8');
 if(combined.indexOf(original)!==combined.lastIndexOf(original))throw Error('Artigo duplicado: '+id);
 combined=combined.replace(original,candidate); const prev=before.find(x=>x.id===id);
 if(prev.sha256_artigo!==sha256(original))throw Error('Hash inconsistente');
 diffs.push({id,original:prev,candidato_sha256:sha256(candidate)});
}
const after=readItems(combined);
for(const [i,r] of before.entries()) { const a=after[i]; if(r.id!==a.id||r.chave!==a.chave)throw Error('IDs ou chaves mudaram'); const changed=r.sha256_artigo!==a.sha256_artigo; if(changed!==["av-e1-42","av-e1-45","av-e1-52"].includes(r.id))throw Error('Delta artigo inesperado '+r.id); }
for(const r of diffs) {r.candidato=after.find(x=>x.id===r.id); if(r.original.digital===r.candidato.digital)throw Error('Digital não mudou');}
const map=JSON.parse(await fs.readFile(path.join(root,'auditoria/termodinamica/evidencias/BAN-07/mapa-identidades-r1.json'),'utf8'));
for(const r of diffs){const expected=map.registros.find(x=>x.id===r.id).depois;if(expected.digital!==r.original.digital||expected.sha256_artigo!==r.original.sha256_artigo)throw Error('Histórico BAN-07 diverge: '+r.id);}
const av=after.filter(x=>x.id.startsWith('av-'));const seen=new Map();const collisions=[];for(const x of av){if(seen.has(x.digital))collisions.push([seen.get(x.digital),x.id,x.digital]);else seen.set(x.digital,x.id);}
if(collisions.length)throw Error('Colisão atual AV: '+JSON.stringify(collisions));
const historicas=map.registros.filter(x=>x.id.startsWith('av-')).flatMap(x=>[x.antes,x.depois]);
for(const d of diffs){for(const h of historicas){if(h.digital===d.candidato.digital)throw Error('Colisão da candidata com digital histórica conhecida: '+d.id+' / '+h.id);}}
console.log(JSON.stringify({metodo:'funções reais de curso.js em VM, adaptador do parser de inventário; comparação 80 AV e reversão de artigos em cópia de memória',html_sha256:sha256(source),artigos:before.length,banco_av:av.length,colisoes_av:collisions,colisoes_historicas_conhecidas:[],deltas:diffs,limites:['Sem teste de persistência em navegador; hash não demonstra validade científica.','Verificar colisões e armazenamento novamente na versão efetivamente aplicada.']},null,2));
