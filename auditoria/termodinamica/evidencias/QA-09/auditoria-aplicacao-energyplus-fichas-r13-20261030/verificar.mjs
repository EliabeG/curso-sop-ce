// Verificação independente de três substituições; somente leitura.
import fs from 'node:fs';
import {parseHtml,isInventoryArticle,sha256} from '../../../inventario/validar-inventario.mjs';
const root='auditoria/termodinamica/evidencias/QA-09/';
const d=root+'aplicacao-energyplus-fichas-r13-r1/resultado/';
const ef=root+'candidata-fonte-energyplus-r12-20261030/';
const cf=root+'candidatas-fichas-88-99-r12-20261030/';
const records=[{doc:'modulos/e1-termodinamica.html',id:'energyplus',original:ef+'original.html',candidata:ef+'candidata.html',h0:'478506a79ba58dcafb2637025e844fd8c3767f6e1146e634430ed01ca6747e5a',h1:'b7514dac2be1dfdb41a8751e56764c7bbab727e2c8f66e81bffd459c8b5b528e'},
{doc:'formulas/termodinamica.html',id:'88',original:cf+'88-original.html',candidata:cf+'88-candidata.html',h0:'bd19218dd4ad251d9debfc2b70b19102da7fb7996c82ea98ab2e61582ce7008d',h1:'ac1e873b4de6822bd57453234a46c8fcea1271d017367aeb97f4330cff7e11e9'},
{doc:'formulas/termodinamica.html',id:'99',original:cf+'99-original.html',candidata:cf+'99-candidata.html',h0:'e4b32d03b87cfde282b239623549998f6852a206208271b5c1147773f97fd6db',h1:'5262a7c0d1bb26b99a8c185827a28f547cf819fa6f3b1455b374a67f29bf17bd'}];
const files=[['modulos/e1-termodinamica.html','antes-aula.html','depois-aula.html','f76c39a3e1d8c349ebf0df72cc20a3ab21c68960c8451799bad90a9dcc4bd8c7','f19000a7ddb1f3552b9633b0efec266fb3f6c5e5065808505a2f65b2005aefbc'],['formulas/termodinamica.html','antes-formulario.html','depois-formulario.html','6857fd83e0b2e49c804903cff1dea4128a665ab22eb27bac4ab15d6c557ff756','5f3f31a4801f96a2b78b40c75d37392f6b16d264901ac313ac00458901970285']];
const check=(v,m)=>{if(!v)throw Error(m)};let parsed={};
for(const [path,oldname,newname,oldhash,newhash] of files){
 let before=fs.readFileSync(d+oldname,'utf8'),after=fs.readFileSync(path,'utf8');
 check(sha256(before)===oldhash&&sha256(after)===newhash&&after===fs.readFileSync(d+newname,'utf8'),'hash/snapshot '+path);
 let reconstructed=before;
 for(const e of records.filter(x=>x.doc===path)){
  let a=fs.readFileSync(e.original,'utf8').replace(/\n$/,''),b=fs.readFileSync(e.candidata,'utf8').replace(/\n$/,'');
  check(sha256(a)===e.h0&&sha256(b)===e.h1&&reconstructed.split(a).length===2&&after.split(b).length===2,'fragmento '+e.id);
  reconstructed=reconstructed.replace(a,b);
 }
 check(reconstructed===after,'reconstrução '+path);
 let a=parseHtml(before),b=parseHtml(after);check(!a.errors.length&&!b.errors.length,'parser');
 const raw=(doc,source,test)=>doc.nodes.filter(test).map(n=>[n.attrs.id??null,source.slice(n.start,n.end)]);
 let ma=raw(a,before,n=>n.tag==='math'),mb=raw(b,after,n=>n.tag==='math');check(JSON.stringify(ma)===JSON.stringify(mb),'MathML');
 parsed[path]={before,after,a,b,raw,math:ma.length};
}
let p=parsed['modulos/e1-termodinamica.html'];const A=p.raw(p.a,p.before,isInventoryArticle),B=p.raw(p.b,p.after,isInventoryArticle);
check(A.length===197&&JSON.stringify(A)===JSON.stringify(B),'artigos');
p=parsed['formulas/termodinamica.html'];const ficha=n=>n.tag==='article'&&(n.attrs.class??'').split(/\s+/).includes('formula-card');
const fa=p.raw(p.a,p.before,ficha),fb=p.raw(p.b,p.after,ficha);check(fa.length===100&&fb.length===100,'fichas');
let changed=[];for(let i=0;i<fa.length;i++){check(fa[i][0]===fb[i][0],'ordem');if(fa[i][1]!==fb[i][1])changed.push(fa[i][0])}
check(JSON.stringify(changed.sort())===JSON.stringify(['formula-intermediaria','formula-geracao'].sort())&&p.math===191,'fichas não alvo ou MathML');
const i0=JSON.parse(fs.readFileSync(d+'inventario-oficial-antes.json','utf8')),i1=JSON.parse(fs.readFileSync('auditoria/termodinamica/inventario/inventario-questoes.json','utf8'));
check(i0.itens.length===197&&JSON.stringify(i0.itens)===JSON.stringify(i1.itens),'itens');
check(Object.keys(i0).every(k=>k==='fonte'||JSON.stringify(i0[k])===JSON.stringify(i1[k]))&&i1.fonte.sha256===sha256(parsed['modulos/e1-termodinamica.html'].after),'fonte');
const target='https://bigladdersoftware.com/epx/docs/24-1/engineering-reference/carbon-dioxide-predictor-corrector.html';
check(parsed['modulos/e1-termodinamica.html'].after.includes(target),'referência');
const insideFicha=n=>{for(let q=n.parent;q;q=q.parent)if(ficha(q))return true;return false};
const links=p.b.nodes.filter(n=>n.tag==='a'&&insideFicha(n)&&(n.attrs.href??'').startsWith('../modulos/e1-termodinamica.html#'));
const targetIds=new Set(parsed['modulos/e1-termodinamica.html'].b.nodes.map(n=>n.attrs.id).filter(Boolean));
check(links.length===103&&links.every(n=>targetIds.has(n.attrs.href.split('#')[1])),'links das fichas');
check(Math.sqrt(1*16)===4&&1000/20===50&&(1000+200)/20===60,'contas nominais');
console.log(JSON.stringify({ok:true,deltas:3,artigos:197,registros:197,fichas:100,fichas_alteradas:changed,mathml_aula:parsed['modulos/e1-termodinamica.html'].math,mathml_formulario:p.math,links_fichas:links.length,limite:'Reconstrução documental; não é navegador ou comprovação empírica.'},null,2));
