/** Somente leitura: reconstrução r29 a partir dos snapshots r28 e manifesto aprovado. */
import fs from 'node:fs'; import assert from 'node:assert/strict'; import {spawnSync} from 'node:child_process'; import {parseHtml,isInventoryArticle,sha256} from '../../../inventario/validar-inventario.mjs';
const q='auditoria/termodinamica/evidencias/QA-09/', p=q+'aplicacao-refrigeracao-r29/', c=q+'candidata-refrigeracao-r29-r2/', o=p+'resultado/';
const read=f=>fs.readFileSync(f,'utf8'), check=(f,h)=>assert.equal(sha256(read(f)),h,f);
check(c+'manifesto.json','baadc04397c422c6a68089376272983a67bab336a44be9ce7064323254c6458e');
const m=JSON.parse(read(c+'manifesto.json'));
for(const [doc,before,after,base,result] of [['modulos/e1-termodinamica.html','antes-aula.html','depois-aula.html','d7294e8ed772cf4530788586d693a6cdfbf1ef6fa05c69afbc984efc46e353d8',m.sha_hipotetico.aula],['formulas/termodinamica.html','antes-formulario.html','depois-formulario.html','3157c9b114f3156e5517440d30b91ee8a4efdebcd95be8bd0c7a588f04dead46',m.sha_hipotetico.formulario]]) {
 check(o+before,base);check(o+after,result);check(doc,result);
 const old=read(o+before), now=read(doc);let build=old;
 for(const e of m.edicoes.filter(x=>x.documento===doc).sort((a,b)=>b.inicio_utf16-a.inicio_utf16)) {
  const orig=read(c+e.id+'-original.html').slice(0,-1),cand=read(c+e.id+'-candidata.html').slice(0,-1);assert.equal(sha256(orig),e.original_sha256);assert.equal(sha256(cand),e.candidata_sha256);assert.equal(build.slice(e.inicio_utf16,e.fim_utf16),orig);let patched=orig;
  for(const s of e.substituicoes){assert.equal(patched.split(s.antes).length-1,s.quantidade);patched=patched.replaceAll(s.antes,s.depois)}assert.equal(patched,cand);build=build.slice(0,e.inicio_utf16)+cand+build.slice(e.fim_utf16);
 }
 assert.equal(build,now);const a=parseHtml(old),b=parseHtml(now);assert.equal(a.errors.length+b.errors.length,0);const tag=(d,s,t)=>d.nodes.filter(x=>x.tag===t).map(x=>s.slice(x.start,x.end));assert.deepEqual(tag(a,old,'math'),tag(b,now,'math'));
 if(doc.startsWith('modulos')){const arts=(d,s)=>d.nodes.filter(isInventoryArticle).map(x=>s.slice(x.start,x.end));assert.equal(arts(a,old).length,197);assert.deepEqual(arts(a,old),arts(b,now));}
 else {const cards=(d,s)=>d.nodes.filter(x=>x.tag==='article'&&(x.attrs.class||'').split(/\s+/).includes('formula-card')&&!['formula-refrigeracao','formula-condensador'].includes(x.attrs.id)).map(x=>s.slice(x.start,x.end));assert.equal(cards(a,old).length,98);assert.deepEqual(cards(a,old),cards(b,now));}
}
const old=JSON.parse(read(o+'inventario-oficial-antes.json')),now=JSON.parse(read('auditoria/termodinamica/inventario/inventario-questoes.json'));assert.deepEqual(old.itens,now.itens);assert.equal(now.itens.length,197);assert.equal(now.fonte.sha256,m.sha_hipotetico.aula);
check(q+'inventario-r29.json','f6237de0c999a66c1edbb74f18911d4bd13ba0352d305b32329f3d7f4fd05db8');check(q+'mapa-correspondencia-inventario-r28-r29-r1.json','a05800b66c6d56aa791cb16a251007ee26c6d4fef50c2fe7b42a2a104e8b21ba');
const val=spawnSync('node',['auditoria/termodinamica/inventario/validar-inventario.mjs'],{encoding:'utf8'});assert.equal(val.status,0,val.stderr);assert.equal(JSON.parse(val.stdout).ok,true);console.log('OK: reconstrução exata r29; 197 artigos/registros, 98 fichas, MathML, hashes de inventário e mapa e validador oficial.');
