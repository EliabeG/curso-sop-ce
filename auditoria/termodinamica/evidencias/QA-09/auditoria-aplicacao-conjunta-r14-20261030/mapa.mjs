// Reconciliação independente dos nós, referências e recursos r13→r14; somente leitura.
import fs from 'node:fs';
import {parseHtml,sha256} from '../../../inventario/validar-inventario.mjs';
const base='auditoria/termodinamica/evidencias/QA-09/', dir=base+'aplicacao-conjunta-r14-seis-r1/resultado/';
const paths=[base+'inventario-r13.json',base+'inventario-r14.json',base+'mapa-correspondencia-inventario-r13-r14-r1.json'];
const expected=['0df99b79bcc2350581fcdded72435d30d07858de237a549e6228ca73682f8d9b','6505b06f3f3ef15bc2904f8a604f6e1f0fa6cf22af822394b2c2a871437b6175','a43156dad32d5529850bdd4c40209c68a772fee45cfd8651e3f9b0becaa1ff07'];
const check=(v,s)=>{if(!v)throw Error(s)};
const raw=paths.map((p,i)=>{let x=fs.readFileSync(p);check(sha256(x)===expected[i],'hash '+p);return JSON.parse(x)}),[i0,i1,map]=raw;
const names=['modulos/e1-termodinamica.html','formulas/termodinamica.html'];
const snapshots=[['antes-aula.html','depois-aula.html'],['antes-formulario.html','depois-formulario.html']];
let docs=[];for(let i=0;i<2;i++){const build=h=>{let p=parseHtml(h);check(!p.errors.length,'parser');return{html:h,nodes:new Map(p.nodes.map(n=>[`${n.start}:${n.end}:${n.tag}`,n]))}};docs.push(snapshots[i].map(n=>build(fs.readFileSync(dir+n,'utf8'))));}
function nodeHash(doc,o){let n=doc.nodes.get(`${o.inicio_utf16}:${o.fim_utf16}:${o.tag}`);check(n,'nó '+o.id);let s;
 if(o.tipo==='texto_direto'){let pos=n.openEnd,parts=[];for(const c of n.children){if(c.start>pos)parts.push(doc.html.slice(pos,c.start));pos=Math.max(pos,c.end)}if(n.end>pos)parts.push(doc.html.slice(pos,n.end).replace(new RegExp(`</${n.tag}\\s*>\\s*$`,'i'),''));s=parts.join(' ')}
 else if(o.tipo==='atributos_significativos')s=doc.html.slice(n.start,n.openEnd);else s=doc.html.slice(n.start,n.end);return sha256(s)}
const d0=new Map(i0.ocorrencias.map(o=>[o.id,o])),d1=new Map(i1.ocorrencias.map(o=>[o.id,o]));check(d0.size===11397&&d1.size===11399,'total');
let seen0=new Set(),seen1=new Set(),counts={},changed={},add=[];
for(const p of map.pares){let a=p.id_r13===null?null:d0.get(p.id_r13),b=d1.get(p.id_r14);check(b&&!seen1.has(b.id),'novo duplicado/ausente');seen1.add(b.id);counts[p.estado]=(counts[p.estado]??0)+1;
 if(p.estado==='ADICIONADO_OU_REESTRUTURADO'){check(!a&&p.sha256_r14===b.sha256_fragmento,'adicionado');let j=names.indexOf(b.arquivo);check(j>=0&&nodeHash(docs[j][1],b)===b.sha256_fragmento,'hash adicionado');add.push(b.id);continue}
 check(a&&!seen0.has(a.id),'antigo duplicado/ausente');seen0.add(a.id);for(const k of ['arquivo','secao','ancora','tag','tipo'])check(a[k]===b[k],'campo '+k+' '+a.id);
 check(a.sha256_fragmento===p.sha256_r13&&b.sha256_fragmento===p.sha256_r14,'hash mapa');if(a.sha256_fragmento!==b.sha256_fragmento)changed[p.estado]=(changed[p.estado]??0)+1;
 if(p.estado==='PAREADO_INTERNO_CONFERIR'||p.estado==='PAREADO_CONTEXTO_ANCESTRAL_CONFERIR'){let j=names.indexOf(a.arquivo);check(j>=0&&nodeHash(docs[j][0],a)===a.sha256_fragmento&&nodeHash(docs[j][1],b)===b.sha256_fragmento,'hash interno/ancestral '+a.id)}
 else if(p.estado==='PAREADO_EXTERNO'){for(const k of ['inicio_utf16','fim_utf16']){let shift=map.edicoes.filter(e=>e.documento===a.arquivo&&e.fim<=a[k]).reduce((s,e)=>s+e.delta,0);check(a[k]+shift===b[k],'deslocamento '+a.id)}}else throw Error('estado '+p.estado);
}
check(seen0.size===11397&&seen1.size===11399&&counts.PAREADO_EXTERNO===11178&&counts.PAREADO_INTERNO_CONFERIR===214&&counts.PAREADO_CONTEXTO_ANCESTRAL_CONFERIR===5&&counts.ADICIONADO_OU_REESTRUTURADO===2,'pareamento');
check(i0.referencias.length===815&&i1.referencias.length===816,'referências');
let inserted=i1.referencias.filter(x=>x.valor==='https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node33.html'&&x.ancora==='fun02-processos');check(inserted.length===1,'MIT novo');
let j=0;for(const a of i0.referencias){while(j<i1.referencias.length&&i1.referencias[j]===inserted[0])j++;let b=i1.referencias[j++];check(b,'referência ausente');for(const k of ['arquivo','secao','ancora','tag','atributo','valor','texto'])check(a[k]===b[k],'referência alterada '+a.valor)}
check(i0.recursos.length===138&&i1.recursos.length===138,'recursos');for(let n=0;n<138;n++){let a=i0.recursos[n],b=i1.recursos[n];for(const k of ['origem','referencia','arquivo','papel','estado'])check(a[k]===b[k],'recurso '+n);check(sha256(fs.readFileSync(b.arquivo))===b.sha256,'recurso hash '+n)}
check(JSON.stringify(i0.ativos_especificos)===JSON.stringify(i1.ativos_especificos),'ativos');check(JSON.stringify(i0.artigos_excluidos)===JSON.stringify(i1.artigos_excluidos),'artigos segregados');
console.log(JSON.stringify({ok:true,pares:map.pares.length,estados:counts,hashes_diferentes:changed,adicionados:add,referencias_antigas:815,referencias_novas:1,recursos:138,limite:'Confronto estrutural; sem transferência automática de aceite.'},null,2));
