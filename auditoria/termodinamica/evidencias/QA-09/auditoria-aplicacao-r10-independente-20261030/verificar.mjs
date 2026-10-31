// Auditoria independente, somente leitura: reconstrução e regressão do delta r9→r10.
import fs from 'node:fs';
import {parseHtml,isInventoryArticle,sha256} from '../../../inventario/validar-inventario.mjs';
const root='auditoria/termodinamica/evidencias/QA-09/aplicacao-pressao-fichas-r10-r1/';
const editions=JSON.parse(fs.readFileSync(root+'config.json','utf8')).edicoes;
const files=[['modulos/e1-termodinamica.html','antes-aula.html','depois-aula.html','2d6b8fb2f9c99e04d22c19d7b32bbc3eb20577459d9132e506f9c0acef3f2fc2','a8bed8a91a36a1c1f41cd75e3c1858fecb4e14a506e582ad1fdb186d275805e3'],['formulas/termodinamica.html','antes-formulario.html','depois-formulario.html','cda652563a79c49a6c3d527ad1400c7f7597d33c9b8523ed8a26047b25c69feb','01d5d79639cd17dfcaea38479019cf719e2601f5b35d446ab562e50d381fa5c9']];
const check=(v,s)=>{if(!v)throw Error(s)};
let parsed={};
for(const [path,oldname,newname,oldhash,newhash] of files){
 let before=fs.readFileSync(root+oldname,'utf8'), after=fs.readFileSync(path,'utf8');
 check(sha256(before)===oldhash && sha256(after)===newhash,'hash de documento '+path);
 check(after===fs.readFileSync(root+newname,'utf8'),'snapshot posterior '+path);
 let reconstructed=before;
 for(const e of editions.filter(x=>x.documento===path)){
  let old=fs.readFileSync(e.original,'utf8').replace(/\n$/,''),candidate=fs.readFileSync(e.candidata,'utf8').replace(/\n$/,'');
  check(sha256(old)===e.original_sha256&&sha256(candidate)===e.candidata_sha256,'hash candidato '+e.id);
  check(reconstructed.split(old).length===2,'origem não única '+e.id);
  reconstructed=reconstructed.replace(old,candidate);
  check(after.split(candidate).length===2,'candidata não única '+e.id);
 }
 check(reconstructed===after,'reconstrução divergente '+path);
 let a=parseHtml(before),b=parseHtml(after);check(!a.errors.length&&!b.errors.length,'parser '+path);
 const raw=(doc,source,test)=>doc.nodes.filter(test).map(n=>[n.attrs.id??null,source.slice(n.start,n.end)]);
 let mathOld=raw(a,before,n=>n.tag==='math'), mathNew=raw(b,after,n=>n.tag==='math');
 check(JSON.stringify(mathOld)===JSON.stringify(mathNew),'MathML divergente '+path);
 parsed[path]={before,after,a,b,math:mathOld.length,raw};
}
let p=parsed['modulos/e1-termodinamica.html'];
let aa=p.raw(p.a,p.before,isInventoryArticle),ab=p.raw(p.b,p.after,isInventoryArticle);
check(aa.length===197&&JSON.stringify(aa)===JSON.stringify(ab),'artigos');
p=parsed['formulas/termodinamica.html'];
const ficha=n=>n.tag==='article' && (n.attrs.class??'').split(/\s+/).includes('formula-card');
let fa=p.raw(p.a,p.before,ficha),fb=p.raw(p.b,p.after,ficha);
check(fa.length===100&&fb.length===100,'contagem de fichas');
let changed=fa.map((x,i)=>JSON.stringify(x)===JSON.stringify(fb[i])?null:x[0]).filter(Boolean);
check(JSON.stringify(changed.sort())===JSON.stringify(['formula-calor-reversivel','formula-reacao'].sort()),'fichas divergentes');
check(p.math===191,'contagem MathML formulário');
const i0=JSON.parse(fs.readFileSync(root+'inventario-oficial-antes.json','utf8')),i1=JSON.parse(fs.readFileSync('auditoria/termodinamica/inventario/inventario-questoes.json','utf8'));
check(JSON.stringify(i0.itens)===JSON.stringify(i1.itens) && i1.itens.length===197,'registros');
check(Object.keys(i0).every(k=>k==='fonte'||JSON.stringify(i0[k])===JSON.stringify(i1[k])),'campos adicionais do inventário');
check(i1.fonte.sha256===sha256(parsed['modulos/e1-termodinamica.html'].after),'fonte oficial');
check(p.after.includes('href="../modulos/e1-termodinamica.html#base-entropia"') && parsed['modulos/e1-termodinamica.html'].after.includes('id="base-entropia"'),'destino ficha 67');
console.log(JSON.stringify({ok:true,deltas:editions.length,artigos:aa.length,registros:i1.itens.length,fichas:fa.length,fichas_alteradas:changed,mathml_formulario:p.math,mathml_aula:parsed['modulos/e1-termodinamica.html'].math,limite:'Verifica delta, não toda correção científica ou navegador.'},null,2));
