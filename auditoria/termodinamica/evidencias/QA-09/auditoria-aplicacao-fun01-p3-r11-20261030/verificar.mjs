// Verificação independente do único delta P3; leitura sem regravar evidências.
import fs from 'node:fs';
import {parseHtml,isInventoryArticle,sha256} from '../../../inventario/validar-inventario.mjs';
const dir='auditoria/termodinamica/evidencias/QA-09/aplicacao-fun01-p3-r11-r1/resultado/';
const pair='auditoria/termodinamica/evidencias/QA-09/fun01-p3-procedencia-candidata-r9-20261030/';
const before=fs.readFileSync(dir+'antes-aula.html','utf8'),after=fs.readFileSync('modulos/e1-termodinamica.html','utf8');
const orig=fs.readFileSync(pair+'original.html','utf8').replace(/\n$/,''),cand=fs.readFileSync(pair+'candidata.html','utf8').replace(/\n$/,'');
const check=(v,m)=>{if(!v)throw Error(m)};
check(sha256(before)==='a8bed8a91a36a1c1f41cd75e3c1858fecb4e14a506e582ad1fdb186d275805e3','base r10');
check(sha256(after)==='f76c39a3e1d8c349ebf0df72cc20a3ab21c68960c8451799bad90a9dcc4bd8c7','aula r11');
check(sha256(orig)==='7b13d7adbb3ec83f676edadbebf7a0246d139ff24bf4931350d7580708b47bd9'&&sha256(cand)==='ce23ebfff83d3172e72046551cf365a967a098b0640c01acb56480154ccd7015','fragmentos');
check(before.split(orig).length===2&&!before.includes(cand)&&after.split(cand).length===2&&before.replace(orig,cand)===after,'reconstrução literal');
check(after===fs.readFileSync(dir+'depois-aula.html','utf8'),'snapshot');
const a=parseHtml(before),b=parseHtml(after);check(!a.errors.length&&!b.errors.length,'parser');
const articles=(doc,source)=>doc.nodes.filter(isInventoryArticle).map(n=>[n.attrs.id,source.slice(n.start,n.end)]);
const A=articles(a,before),B=articles(b,after);check(A.length===197&&B.length===197,'total artigos');
let changed=[];
for(let i=0;i<197;i++){
 check(A[i][0]===B[i][0],'ordem');
 if(A[i][1]!==B[i][1]){
  changed.push(A[i][0]);
  check(A[i][0]==='fun01-e1-supercritico'&&A[i][1].replace(orig,cand)===B[i][1],'artigo P3');
  check(sha256(A[i][1])==='2fad0e042fb945eb44d0f2abe2c4e64322434195395fa4e5c084f17854f432a7'&&sha256(B[i][1])==='ab2d00867b0f11bc75810b84c74f8347e308fbf26b07f62de8fc11e0eb378c4d','hash P3');
 }
}
check(changed.length===1&&changed[0]==='fun01-e1-supercritico','outros artigos');
const m=(d,s)=>d.nodes.filter(n=>n.tag==='math').map(n=>s.slice(n.start,n.end));
check(JSON.stringify(m(a,before))===JSON.stringify(m(b,after)),'MathML');
let x=JSON.parse(fs.readFileSync(dir+'inventario-oficial-antes.json','utf8')),y=JSON.parse(fs.readFileSync('auditoria/termodinamica/inventario/inventario-questoes.json','utf8'));
check(x.itens.length===197&&y.itens.length===197,'inventário itens');
let records=0;
for(let i=0;i<197;i++){
 if(JSON.stringify(x.itens[i])!==JSON.stringify(y.itens[i])){
  records++;check(x.itens[i].id==='fun01-e1-supercritico'&&y.itens[i].id===x.itens[i].id,'registro errado');
  let copy=JSON.parse(JSON.stringify(x.itens[i]));copy.localizacao.sha256_artigo=sha256(B.find(z=>z[0]===x.itens[i].id)[1]);
  check(JSON.stringify(copy)===JSON.stringify(y.itens[i]),'campos além do hash alterados');
 }
}
check(records===1&&Object.keys(x).every(k=>k==='itens'||k==='fonte'||JSON.stringify(x[k])===JSON.stringify(y[k])),'campos globais');
check(y.fonte.sha256===sha256(after)&&y.fonte.snapshot===dir+'depois-aula.html','fonte');
check(sha256(fs.readFileSync('formulas/termodinamica.html'))==='01d5d79639cd17dfcaea38479019cf719e2601f5b35d446ab562e50d381fa5c9','formulário');
const iv0=JSON.parse(fs.readFileSync('auditoria/termodinamica/evidencias/QA-09/inventario-r10.json','utf8'));
const iv1=JSON.parse(fs.readFileSync('auditoria/termodinamica/evidencias/QA-09/inventario-r11.json','utf8'));
const target=iv0.ocorrencias.find(z=>z.id==='modulos/e1-termodinamica.html:88914:secao');
const targetAfter=iv1.ocorrencias.find(z=>z.id===target.id);
check(target&&targetAfter&&target.ancora==='fun01-estado-equilibrio'&&targetAfter.ancora===target.ancora,'ancestral');
check(sha256(before.slice(target.inicio_utf16,target.fim_utf16))===target.sha256_fragmento&&sha256(after.slice(targetAfter.inicio_utf16,targetAfter.fim_utf16))===targetAfter.sha256_fragmento,'hashes ancestral');
// Conferências aritméticas independentes em unidades inteiras (mK e kPa).
const Tc_mK=647096,pc_kPa=22064, Tcenter_mK=650000,pcenter_kPa=22100;
check(Tcenter_mK-Tc_mK===2904&&pcenter_kPa-pc_kPa===36,'margens estritas');
check(645000<Tc_mK&&655000>Tc_mK&&22000<pc_kPa&&22200>pc_kPa,'caixa A');
check(641000<Tc_mK&&20100<pc_kPa,'registros B/C');
check(700000>Tc_mK&&25000>pc_kPa,'registro D');
check(800*0.00125===1,'reciprocidade nominal');
console.log(JSON.stringify({ok:true,artigos:197,artigos_inalterados:196,alterado:changed,registros_inalterados:196,mathml:m(a,before).length,margens_estritas:{K:2.904,MPa:0.036},limite:'Integridade estrutural e contas nominais; não é teste em navegador ou comprovação de aprendizagem.'},null,2));
