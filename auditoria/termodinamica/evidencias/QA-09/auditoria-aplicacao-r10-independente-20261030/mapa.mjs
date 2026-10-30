// Checagem independente dos pares r9→r10 e de seus 89 nós internos; somente leitura.
import fs from 'node:fs';
import {parseHtml,sha256} from '../../../inventario/validar-inventario.mjs';
const base='auditoria/termodinamica/evidencias/QA-09/';
const dir=base+'aplicacao-pressao-fichas-r10-r1/';
const i0=JSON.parse(fs.readFileSync(base+'inventario-r9.json','utf8'));
const i1=JSON.parse(fs.readFileSync(base+'inventario-r10.json','utf8'));
const map=JSON.parse(fs.readFileSync(base+'mapa-correspondencia-inventario-r9-r10-r1.json','utf8'));
const check=(v,s)=>{if(!v)throw Error(s)};
check(sha256(fs.readFileSync(base+'inventario-r9.json'))==='023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d','r9');
check(sha256(fs.readFileSync(base+'inventario-r10.json'))==='3497cbf9ffcbe0a1e2eb84eeb9e34c0cfb6e0ed63a2747795bf75832454e2f6c','r10');
const names=['modulos/e1-termodinamica.html','formulas/termodinamica.html'];
const snapshots=[['antes-aula.html','depois-aula.html'],['antes-formulario.html','depois-formulario.html']];
let docs=[];
for(let i=0;i<2;i++){
 const a=fs.readFileSync(dir+snapshots[i][0],'utf8'),b=fs.readFileSync(dir+snapshots[i][1],'utf8');
 const build=h=>{let p=parseHtml(h);check(!p.errors.length,'parser');return {html:h,nodes:new Map(p.nodes.map(n=>[`${n.start}:${n.end}:${n.tag}`,n]))}};
 docs.push([build(a),build(b)]);
}
const d0=new Map(i0.ocorrencias.map(o=>[o.id,o])), d1=new Map(i1.ocorrencias.map(o=>[o.id,o]));
check(d0.size===11397&&d1.size===11397&&map.pares.length===11397,'contagens');
let seen0=new Set(),seen1=new Set(),counts={},changed={};
function hashNode(doc,o){
 const n=doc.nodes.get(`${o.inicio_utf16}:${o.fim_utf16}:${o.tag}`);check(n,'nó ausente '+o.id);
 let raw;
 if(o.tipo==='texto_direto'){
  let pos=n.openEnd,parts=[];
  for(const c of n.children){if(c.start>pos)parts.push(doc.html.slice(pos,c.start));pos=Math.max(pos,c.end)}
  if(n.end>pos)parts.push(doc.html.slice(pos,n.end).replace(new RegExp(`</${n.tag}\\s*>\\s*$`,'i'),''));
  raw=parts.join(' ');
 }else if(o.tipo==='atributos_significativos')raw=doc.html.slice(n.start,n.openEnd);
 else raw=doc.html.slice(n.start,n.end);
 return sha256(raw);
}
for(const p of map.pares){
 const a=d0.get(p.id_r9),b=d1.get(p.id_r10);check(a&&b&&!seen0.has(a.id)&&!seen1.has(b.id),'duplicata/nó ausente');seen0.add(a.id);seen1.add(b.id);
 for(const key of ['arquivo','secao','ancora','tag','tipo'])check(a[key]===b[key],'campo '+key+' '+a.id);
 check(a.sha256_fragmento===p.sha256_r9&&b.sha256_fragmento===p.sha256_r10,'hash no mapa');
 counts[p.estado]=(counts[p.estado]??0)+1;if(a.sha256_fragmento!==b.sha256_fragmento)changed[p.estado]=(changed[p.estado]??0)+1;
 if(p.estado==='PAREADO_INTERNO_CONFERIR'){
  let d=names.indexOf(a.arquivo);check(d>=0,'arquivo');
  check(hashNode(docs[d][0],a)===a.sha256_fragmento&&hashNode(docs[d][1],b)===b.sha256_fragmento,'hash interno '+a.id);
 }else if(p.estado==='PAREADO_EXTERNO'){
  for(const k of ['inicio_utf16','fim_utf16']){
   const shift=map.edicoes.filter(e=>e.documento===a.arquivo&&e.fim<=a[k]).reduce((sum,e)=>sum+e.delta,0);
   check(a[k]+shift===b[k],'deslocamento externo '+a.id+' '+k);
  }
 }else throw Error('estado de mapa desconhecido '+p.estado);
}
check(counts.PAREADO_INTERNO_CONFERIR===89&&counts.PAREADO_EXTERNO===11308,'classificação');
check(JSON.stringify(i0.artigos_excluidos)===JSON.stringify(i1.artigos_excluidos),'artigos segregados');
check(i0.referencias.length===815&&i1.referencias.length===815&&i0.recursos.length===138&&i1.recursos.length===138,'referências e recursos');
let refDiff=[],resDiff=[];
for(let i=0;i<815;i++){
 const a=i0.referencias[i],b=i1.referencias[i];
 for(const k of ['arquivo','secao','ancora','tag','atributo','texto'])check(a[k]===b[k],'metadados referência '+i);
 if(a.valor!==b.valor)refDiff.push([a.ancora,a.valor,b.valor]);
}
for(let i=0;i<138;i++){
 const a=i0.recursos[i],b=i1.recursos[i];
 for(const k of ['origem','arquivo','papel','estado'])check(a[k]===b[k],'metadados recurso '+i);
 if(a.referencia!==b.referencia)resDiff.push([a.arquivo,a.referencia,b.referencia]);
 let actual=sha256(fs.readFileSync(b.arquivo));check(actual===b.sha256,'hash recurso atual '+i);
}
check(refDiff.length===1&&refDiff[0][0]==='formula-calor-reversivel'&&refDiff[0][1].endsWith('#substancias')&&refDiff[0][2].endsWith('#base-entropia'),'delta referências');
check(resDiff.length===1&&resDiff[0][0]==='modulos/e1-termodinamica.html','delta recursos');
check(JSON.stringify(i0.ativos_especificos)===JSON.stringify(i1.ativos_especificos),'ativos');
console.log(JSON.stringify({ok:true,pares:map.pares.length,estados:counts,hashes_diferentes:changed,hashes_internos_recalculados:89,referencias:815,referencia_alterada:refDiff,recursos:138,recurso_alterado:resDiff,ativos:i1.ativos_especificos.length,limite:'Associação estrutural não transfere automaticamente aprovações.'},null,2));
