// Reconstrução e conferência independente r11→r12; leitura somente.
import fs from 'node:fs';
import {parseHtml,isInventoryArticle,sha256} from '../../../inventario/validar-inventario.mjs';
const d='auditoria/termodinamica/evidencias/QA-09/aplicacao-fichas-calorimetria-co2-r12-r1/resultado/';
const c='auditoria/termodinamica/evidencias/QA-09/candidatas-calorimetria-27-29-r11-20261030-r3/';
const co='auditoria/termodinamica/evidencias/QA-09/candidatas-co2-52-53-r11-20261030/';
const before=fs.readFileSync(d+'antes-formulario.html','utf8'),after=fs.readFileSync('formulas/termodinamica.html','utf8');
const html=fs.readFileSync('modulos/e1-termodinamica.html','utf8');
const check=(v,m)=>{if(!v)throw Error(m)};
check(sha256(before)==='01d5d79639cd17dfcaea38479019cf719e2601f5b35d446ab562e50d381fa5c9','base');
check(sha256(after)==='6857fd83e0b2e49c804903cff1dea4128a665ab22eb27bac4ab15d6c557ff756','formulário');
check(sha256(html)==='f76c39a3e1d8c349ebf0df72cc20a3ab21c68960c8451799bad90a9dcc4bd8c7','aula');
check(html===fs.readFileSync(d+'antes-aula.html','utf8')&&html===fs.readFileSync(d+'depois-aula.html','utf8'),'fotografia aula');
check(after===fs.readFileSync(d+'depois-formulario.html','utf8'),'fotografia formulário');
let recon=before;const expected=[];
for(const n of [27,28,29,52,53]){
 let path=n<50?c:co,original=fs.readFileSync(path+n+'-original.html','utf8').replace(/\n$/,''),candidate=fs.readFileSync(path+n+'-candidata.html','utf8').replace(/\n$/,'');
 check(recon.split(original).length===2&&!recon.includes(candidate)&&after.split(candidate).length===2,'unicidade '+n);
 expected.push([n,sha256(original),sha256(candidate)]);recon=recon.replace(original,candidate);
}
check(recon===after,'reconstrução');
const a=parseHtml(before),b=parseHtml(after),h=parseHtml(html);check(!a.errors.length&&!b.errors.length&&!h.errors.length,'parser');
const fichas=n=>n.tag==='article'&&(n.attrs.class??'').split(/\s+/).includes('formula-card');
const extract=(d,s,f)=>d.nodes.filter(f).map(n=>[n.attrs.id??null,s.slice(n.start,n.end)]);
const A=extract(a,before,fichas),B=extract(b,after,fichas);check(A.length===100&&B.length===100,'contagem');
let changed=[];for(let i=0;i<100;i++){check(A[i][0]===B[i][0],'ordem');if(A[i][1]!==B[i][1])changed.push(A[i][0]);}
const alvo=['formula-equilibrio-mistura','formula-recipiente-mistura','formula-fase-calorimetria','formula-co2-acumulacao','formula-co2-vazao'];
check(JSON.stringify(changed.sort())===JSON.stringify(alvo.sort()),'fichas alteradas');
const M=extract(a,before,n=>n.tag==='math'),N=extract(b,after,n=>n.tag==='math');check(M.length===191&&JSON.stringify(M)===JSON.stringify(N),'MathML');
check(h.nodes.filter(isInventoryArticle).length===197,'artigos');
check(sha256(fs.readFileSync('auditoria/termodinamica/inventario/inventario-questoes.json'))==='f2605176763a61832417506517373a16736717d5cc23de7494e901322c394856','inventário oficial');
const insideFicha=n=>{for(let p=n.parent;p;p=p.parent)if(fichas(p))return true;return false};
const links=b.nodes.filter(n=>n.tag==='a'&&insideFicha(n)&&(n.attrs.href??'').startsWith('../modulos/e1-termodinamica.html#'));
const ids=new Set(h.nodes.map(n=>n.attrs.id).filter(Boolean));
for(const n of links)check(ids.has(n.attrs.href.split('#')[1]),'destino '+n.attrs.href);
check(links.length===103,'contagem links');
console.log(JSON.stringify({ok:true,cinco:expected,fichas:100,nao_alteradas:95,mathml:191,artigos:197,links:links.length,limite:'Reconstrução estrutural não substitui leitura científica ou navegador.'},null,2));
