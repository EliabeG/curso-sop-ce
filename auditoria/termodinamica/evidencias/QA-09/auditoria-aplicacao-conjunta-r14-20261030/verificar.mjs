// Revisão independente dos seis deltas, executada somente em leitura.
import fs from 'node:fs';
import {parseHtml,isInventoryArticle,sha256} from '../../../inventario/validar-inventario.mjs';
const root='auditoria/termodinamica/evidencias/QA-09/',d=root+'aplicacao-conjunta-r14-seis-r1/resultado/';
const loc={
 'ficha-23':['formulas/termodinamica.html','candidatas-fichas-23-58-59-r13-20261030/23-original.html','candidatas-fichas-23-58-59-r13-20261030/23-candidata.html'],
 'ficha-58':['formulas/termodinamica.html','candidatas-fichas-23-58-59-r13-20261030/58-original.html','candidatas-fichas-23-58-59-r13-20261030/58-candidata.html'],
 'ficha-59':['formulas/termodinamica.html','candidatas-fichas-23-58-59-r13-20261030/59-original.html','candidatas-fichas-23-58-59-r13-20261030/59-candidata.html'],
 'openstax':['modulos/e1-termodinamica.html','candidata-fonte-openstax-r13-20261030/original.html','candidata-fonte-openstax-r13-20261030/candidata.html'],
 'isentropica':['modulos/e1-termodinamica.html','candidata-teoria-isentropica-r13-20261030-r2/original.html','candidata-teoria-isentropica-r13-20261030-r2/candidata.html'],
 'diagnostico-23':['modulos/e1-termodinamica.html','candidata-diagnostico23-r13-20261030/original-r13.html','candidata-diagnostico23-r13-20261030/candidata.html']};
const edits=JSON.parse(fs.readFileSync(d+'edicoes-aplicadas.json','utf8'));
const files=[['modulos/e1-termodinamica.html','antes-aula.html','depois-aula.html','f19000a7ddb1f3552b9633b0efec266fb3f6c5e5065808505a2f65b2005aefbc','572b172b29e1aa26873d191ebd827414c99f3122491c6d4c8129a69443f7389c'],['formulas/termodinamica.html','antes-formulario.html','depois-formulario.html','5f3f31a4801f96a2b78b40c75d37392f6b16d264901ac313ac00458901970285','3ea110fda92c74253b69d89f5a6e62b288aa3bd99db6a51b54a6c67c8af82fce']];
const check=(v,m)=>{if(!v)throw Error(m)};let parsed={};
check(edits.length===6&&new Set(edits.map(x=>x.id)).size===6&&edits.every(x=>loc[x.id]),'edicoes');
for(const [path,oldname,newname,oldhash,newhash] of files){
 let before=fs.readFileSync(d+oldname,'utf8'),after=fs.readFileSync(path,'utf8');
 check(sha256(before)===oldhash&&sha256(after)===newhash&&after===fs.readFileSync(d+newname,'utf8'),'fotografia '+path);
 let reconstructed=before;
 for(const e of edits.filter(x=>x.documento===path)){
  let [doc,oldpath,newpath]=loc[e.id];check(doc===path,'documento');
  let old=fs.readFileSync(root+oldpath,'utf8').replace(/\n$/,''),candidate=fs.readFileSync(root+newpath,'utf8').replace(/\n$/,'');
  check(sha256(old)===e.original_sha256&&sha256(candidate)===e.candidata_sha256,'hash '+e.id);
  check(reconstructed.split(old).length===2&&after.split(candidate).length===2,'unicidade '+e.id);
  reconstructed=reconstructed.replace(old,candidate);
 }
 check(reconstructed===after,'reconstrução '+path);
 let a=parseHtml(before),b=parseHtml(after);check(!a.errors.length&&!b.errors.length,'parser');
 const raw=(doc,s,test)=>doc.nodes.filter(test).map(n=>[n.attrs.id??null,s.slice(n.start,n.end)]);
 const ma=raw(a,before,n=>n.tag==='math'),mb=raw(b,after,n=>n.tag==='math');check(JSON.stringify(ma)===JSON.stringify(mb),'MathML');
 parsed[path]={before,after,a,b,raw,math:ma.length};
}
let p=parsed['modulos/e1-termodinamica.html'];const aa=p.raw(p.a,p.before,isInventoryArticle),ab=p.raw(p.b,p.after,isInventoryArticle);check(aa.length===197&&JSON.stringify(aa)===JSON.stringify(ab),'artigos');
p=parsed['formulas/termodinamica.html'];const isCard=n=>n.tag==='article'&&(n.attrs.class??'').split(/\s+/).includes('formula-card');
const fa=p.raw(p.a,p.before,isCard),fb=p.raw(p.b,p.after,isCard);check(fa.length===100&&fb.length===100,'fichas');
let changed=[];for(let i=0;i<fa.length;i++){check(fa[i][0]===fb[i][0],'ordem');if(fa[i][1]!==fb[i][1])changed.push(fa[i][0])}
check(JSON.stringify(changed.sort())===JSON.stringify(['formula-latente','formula-eficiencia','formula-cop-refrigerador'].sort()),'fichas alteradas');
const i0=JSON.parse(fs.readFileSync(d+'inventario-oficial-antes.json','utf8')),i1=JSON.parse(fs.readFileSync('auditoria/termodinamica/inventario/inventario-questoes.json','utf8'));
check(i0.itens.length===197&&JSON.stringify(i0.itens)===JSON.stringify(i1.itens),'itens');
check(Object.keys(i0).every(k=>k==='fonte'||JSON.stringify(i0[k])===JSON.stringify(i1[k]))&&i1.fonte.sha256===sha256(parsed['modulos/e1-termodinamica.html'].after),'fonte');
const inside=n=>{for(let q=n.parent;q;q=q.parent)if(isCard(q))return true;return false};
const links=p.b.nodes.filter(n=>n.tag==='a'&&inside(n)&&(n.attrs.href??'').startsWith('../modulos/e1-termodinamica.html#'));
const ids=new Set(parsed['modulos/e1-termodinamica.html'].b.nodes.map(n=>n.attrs.id).filter(Boolean));
check(links.length===103&&links.every(n=>ids.has(n.attrs.href.split('#')[1])),'links');
console.log(JSON.stringify({ok:true,edicoes:6,artigos:197,registros:197,fichas:100,alteradas:changed,mathml_aula:parsed['modulos/e1-termodinamica.html'].math,mathml_formulario:p.math,links_fichas:103,limite:'Estática; não comprova navegador ou aprendizagem.'},null,2));
