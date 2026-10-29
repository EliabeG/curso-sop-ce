import fs from 'node:fs';
import vm from 'node:vm';
import {parseHtml,decodeHtml,sha256} from '../../../inventario/validar-inventario.mjs';
const dir='auditoria/termodinamica/evidencias/BAN-07/propostas-r2/';
const source=fs.readFileSync('modulos/e1-termodinamica.html','utf8'),doc=parseHtml(source);
const js=fs.readFileSync('assets/curso.js','utf8');
const fn=(name,next)=>js.slice(js.indexOf('  function '+name+'('),js.indexOf('  function '+next+'('));
const ctx={Array,String,Math};vm.createContext(ctx);vm.runInContext("var SEPARADOR='␞';\n"+fn('paraArray','criar')+fn('normalizarDigital','formatarTempo')+fn('digitalDoBanco','iniciarBanco'),ctx);
function adapter(doc,node){const cache=new Map();function match(n,selector){if(selector.startsWith('.'))return(n.attrs.class??'').split(/\s+/).includes(selector.slice(1));if(selector==='input[type="radio"]')return n.tag==='input'&&n.attrs.type==='radio';return n.tag===selector}function wrap(n){if(cache.has(n))return cache.get(n);const out={nodeType:1,localName:n.tag,tagName:n.tag.toUpperCase(),hasAttribute:k=>k in n.attrs,getAttribute:k=>n.attrs[k]??null,value:n.attrs.value,id:n.attrs.id,dataset:{crGabarito:n.attrs['data-cr-gabarito']},childNodes:[],querySelectorAll:s=>doc.nodes.filter(v=>v!==n&&v.start>=n.start&&v.end<=n.end&&match(v,s)).map(wrap),querySelector:s=>out.querySelectorAll(s)[0]??null,closest:s=>{let p=n;while(p){if(match(p,s))return wrap(p);p=p.parent}return null}};cache.set(n,out);const close=doc.html.lastIndexOf('</',n.end-1),end=close>=n.openEnd?close:n.openEnd;let at=n.openEnd;for(const child of n.children){if(child.start>at)out.childNodes.push({nodeType:3,nodeValue:decodeHtml(doc.html.slice(at,child.start))});out.childNodes.push(wrap(child));at=child.end}if(end>at)out.childNodes.push({nodeType:3,nodeValue:decodeHtml(doc.html.slice(at,end))});return out}return wrap(node)}
const specs=[['06','01aa3697','C'],['26','988714ce','E'],['45','c084d78c','C']];
const current=doc.nodes.filter(n=>/^cr-e1-\d+$/.test(n.attrs.id??'')).map(n=>({id:n.attrs.id,digital:ctx.digitalDoBanco(adapter(doc,n))}));if(current.length!==80)throw Error('Não há 80 CR');
const results=[];
for(const [n,expected,key] of specs){const id='cr-e1-'+n;const node=doc.ids.get(id)[0],old=source.slice(node.start,node.end), candidate=fs.readFileSync(dir+'CR'+n+'-candidata.html','utf8');const parsed=parseHtml(candidate),article=parsed.ids.get(id)?.[0];
 const note=parsed.nodes.filter(x=>x.tag==='p'&&(x.attrs.class??'').split(/\s+/).includes('cr-suplemento'));
 if(note.length!==1)throw Error('Suplemento ausente ou duplicado '+id);const extra=candidate.slice(note[0].start,note[0].end);
 if(candidate.replace(extra,'')!==old)throw Error('Delta além do suplemento '+id);
 if(article.attrs['data-cr-gabarito']!==key||parsed.errors.length)throw Error('Chave ou estrutura '+id);
 const d1=ctx.digitalDoBanco(adapter(doc,node)),d2=ctx.digitalDoBanco(adapter(parsed,article));if(d1!==expected||d1===d2)throw Error('Digital '+id);
 const parent=note[0].parent;if(parent?.attrs.id!==id+'-enunciado')throw Error('Suplemento fora da digital '+id);
 if(current.some(x=>x.digital===d2))throw Error('Colisão CR r1 '+id);
 results.push({id,artigo_r1:sha256(old),artigo_candidato:sha256(candidate),digital_r1:d1,digital_candidata:d2,chave:key,bytes:Buffer.byteLength(candidate),suplemento:candidate.slice(note[0].start,note[0].end)});
}
if(new Set(results.map(x=>x.digital_candidata)).size!==results.length)throw Error('Colisão entre candidatos');
const expected={'modulos/e1-termodinamica.html':'de614a44d796ca04268915f89f502060db2772835c072036a990802eff912b80','auditoria/termodinamica/inventario/inventario-questoes.json':'7d35b07b31c7faa13eb3f98a8c73c3a9bd1c2cf146534464dfdd202e0074e4a7','auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md':'dba046a5781f6bb82fef14b52af8f3285063c815b130f580edc817e9bd589fb1','assets/curso.js':'a20f4d19158073a9a1c48aabdfba8fa863b02063e16061c00b16448a6ccc2e13','assets/registro.js':'46da94527d6639fe0265bd766286f1ef39623966105e00bda3b31f21ca2c247c'};const produto=Object.entries(expected).map(([arquivo,original])=>({arquivo,sha256:sha256(fs.readFileSync(arquivo)),original}));if(produto.some(x=>x.sha256!==x.original))throw Error('Produto r1 alterado');
console.log(JSON.stringify({resultados:results,colisoes:'Sem colisão com 80 CR r1 nem entre três candidatas; históricos desconhecidos não foram examinados.',produto},null,2));
