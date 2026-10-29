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

const folder=path.join(root,'auditoria/termodinamica/evidencias/BAN-08/aplicacao-av42-av45-av52-r1');
const beforeText=await fs.readFile(path.join(folder,'antes/modulos/e1-termodinamica.html'),'utf8');
const nowText=await fs.readFile(path.join(root,'modulos/e1-termodinamica.html'),'utf8');
if(sha256(beforeText)!=='80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0'||sha256(nowText)!=='9ec10053e40640feeb977baea742da3cbe4d546659f772f0256c6b3cb0720a55')throw Error('HTML mudou');
const before=readItems(beforeText),after=readItems(nowText);let reversed=nowText;const changes=[];
for(const [i,r] of before.entries()){const a=after[i];if(r.id!==a.id||r.chave!==a.chave)throw Error('ID/chave diferente');if(r.sha256_artigo!==a.sha256_artigo)changes.push({id:r.id,antes:r,depois:a});}
if(changes.map(x=>x.id).join(',')!=='av-e1-42,av-e1-45,av-e1-52')throw Error('Artigos diferentes do escopo');
const docBefore=parseHtml(beforeText),docNow=parseHtml(nowText);
for(const x of changes){let old=docBefore.ids.get(x.id)[0],fresh=docNow.ids.get(x.id)[0];let b=beforeText.slice(old.start,old.end),a=nowText.slice(fresh.start,fresh.end);const n=x.id.slice(-2);const candidate=await fs.readFile(path.join(root,`auditoria/termodinamica/evidencias/BAN-08/propostas-av42-av45-r1/AV${n}-candidata.html`),'utf8');if(a!==candidate)throw Error('Produto diverge de candidata '+x.id);reversed=reversed.replace(a,b);}
if(reversed!==beforeText)throw Error('Alterações fora dos artigos');
const av=after.filter(x=>x.id.startsWith('av-'));const seen=new Set();for(const x of av){if(seen.has(x.digital))throw Error('Colisão '+x.id);seen.add(x.digital);}
const snapshot=await fs.readFile(path.join(root,'auditoria/termodinamica/evidencias/BAN-08/e1-termodinamica-av42-av45-av52-r1.html'),'utf8');if(snapshot!==nowText)throw Error('Snapshot diverge');
console.log(JSON.stringify({id:'BAN-08',estado:'VALIDACAO_TECNICA_SEM_ACEITE',artigos:after.length,banco_av:av.length,colisoes:0,conteudo_fora_3_artigos:'preservado',snapshot:'identico',changes},null,2));
