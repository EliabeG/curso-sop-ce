/** Ponte r27→r28: reextrai recortes e contextos; não concede aceite por identidade. */
import fs from 'node:fs';import crypto from 'node:crypto';import assert from 'node:assert/strict';import {parseHtml} from '../../../inventario/validar-inventario.mjs';
const Q='auditoria/termodinamica/evidencias/QA-09/',D=Q+'ledger-r28-parcial-r1/',P=Q+'aplicacao-conjunta-r28/',sha=x=>crypto.createHash('sha256').update(x).digest('hex');
const files={
 [Q+'ledger-r27-expandido-r3/ledger.json']:'b2a8f5bd94e00d441e6d2386f84e414cf8f3d7d6a46a653214c6a2064ced2593',
 [Q+'auditoria-ledger-r27-expandido-r3-graficos/parecer.md']:'942d848d9f4f5219b61c4b300d7138daabf52d275f5e0bea16f3785f9bbb6f29',
 [P+'entrega-r28.md']:'0b3f1ccdf854f3c5ef02536089e79cc531ff848e19eab8aee99cfcd1a9aede76',
 [P+'resultado/edicoes-aplicadas.json']:'a4f84b742e543bad7453729bc41faf9629ed2739d4c60a60a53bf2a0f7265e7a',
 [P+'resultado/antes-aula.html']:'9af8e2c9ffe509e40594d086a9ef4ad75127fb4ca873efb305d3144e08f3fc49',
 [P+'resultado/antes-formulario.html']:'16329b7369c4ba927f5f7da30551f86934aad1f6a6e55627443dea5cb9fe0c02',
 [P+'resultado/depois-aula.html']:'d7294e8ed772cf4530788586d693a6cdfbf1ef6fa05c69afbc984efc46e353d8',
 [P+'resultado/depois-formulario.html']:'3157c9b114f3156e5517440d30b91ee8a4efdebcd95be8bd0c7a588f04dead46',
 [Q+'inventario-r27.json']:'a58d7f0b0a5f097eef83ad83026ef49e801457b87f7cf2b2345c3dd915597c7c',
 [Q+'inventario-r28.json']:'0a7a12fbf0cd2a0898bcebfdfa7ae98c850bdb0bf7d2b34eea06cc6a8d9afb44',
 [Q+'mapa-correspondencia-inventario-r27-r28-r1.json']:'0e219e8d2863e3d7ced3af4857ce462ca5827bda38276da2a005e5f39e23eca2',
 'auditoria/termodinamica/inventario/validar-inventario.mjs':'0bd26bcf6288b3bd159ac7c167bfeb4a1a49bbebe784d26a3a93739fcb7790d5'};
function read(p){let b=fs.readFileSync(p);assert.equal(sha(b),files[p],`hash ${p}`);return b.toString('utf8')}
for(const p of Object.keys(files))read(p);
let prior=JSON.parse(read(Q+'ledger-r27-expandido-r3/ledger.json')),edits=JSON.parse(read(P+'resultado/edicoes-aplicadas.json')),map=JSON.parse(read(Q+'mapa-correspondencia-inventario-r27-r28-r1.json')),i27=JSON.parse(read(Q+'inventario-r27.json')),i28=JSON.parse(read(Q+'inventario-r28.json'));
assert.deepEqual(map.edicoes,edits);assert.equal(map.base_r27,files[Q+'inventario-r27.json']);assert.equal(map.base_r28,files[Q+'inventario-r28.json']);assert.deepEqual([i27.ocorrencias.length,i28.ocorrencias.length],[11407,11409]);
const docs={'modulos/e1-termodinamica.html':{old:read(P+'resultado/antes-aula.html'),now:read(P+'resultado/depois-aula.html')},'formulas/termodinamica.html':{old:read(P+'resultado/antes-formulario.html'),now:read(P+'resultado/depois-formulario.html')}};
for(const [doc,d] of Object.entries(docs)){
 d.od=parseHtml(d.old);d.nd=parseHtml(d.now);assert.deepEqual(d.od.errors,[]);assert.deepEqual(d.nd.errors,[]);
 for(const e of edits.filter(e=>e.documento===doc)){assert.equal(sha(d.old.slice(e.inicio,e.fim)),e.original_sha256);assert.equal(sha(d.now.slice(e.inicio_novo,e.fim_novo)),e.candidata_sha256)}
}
function shift(doc,a,b){let es=edits.filter(e=>e.documento===doc);assert.ok(es.every(e=>b<=e.inicio||a>=e.fim),`recorte cruza edição ${doc}:${a}-${b}`);let k=es.filter(e=>e.fim<=a).reduce((s,e)=>s+e.delta,0);return [a+k,b+k]}
function target(id,when){let d=docs['modulos/e1-termodinamica.html'],dom=when==='old'?d.od:d.nd,h=when==='old'?d.old:d.now,n;
 if(id==='titulo-ex004')n=dom.nodes.find(v=>v.tag==='h4'&&h.slice(v.start,v.end).includes('Título a partir da entalpia'));else{let all=dom.ids.get(id);assert.equal(all?.length,1,`destino ${id}`);n=all[0]}
 if(n.tag!=='section')while(n&&!(n.tag==='div'&&(n.attrs.class||'').split(/\s+/).includes('bloco-aula')))n=n.parent;
 assert.ok(n,`contexto ${id}`);return h.slice(n.start,n.end)
}
function context(id){let o=target(id,'old'),n=target(id,'now');return{id,sha256_r27:sha(o),sha256_r28:sha(n),alterado:o!==n}}
function item(id,doc,start,end,digest,kind,ids,legacy){let d=docs[doc],raw=d.old.slice(start,end);assert.equal(sha(raw),digest,`r27 ${id}`);let [a,b]=shift(doc,start,end);assert.equal(d.now.slice(a,b),raw,`r28 ${id}`);
 let links=[...new Set([...raw.matchAll(/href="(?:\.\.\/modulos\/e1-termodinamica\.html)?#(base-[^"]+|substancias)"/g)].map(m=>m[1]))];let all=[...new Set([...ids,...links])];let contexts=all.map(context);
 return{id,tipo:kind,arquivo:doc,r27:{inicio_utf16:start,fim_utf16:end,sha256:digest},r28:{inicio_utf16:a,fim_utf16:b,sha256:sha(d.now.slice(a,b))},links,contextos:contexts,estado:'pendente_revalidacao_individual_e_auditoria',origem_ledger:legacy};}
let rows=[];for(const x of prior.registros_explicitamente_revisados){let t=x.identidade_r27;rows.push(item(x.id_local,t.arquivo,t.inicio_utf16,t.fim_utf16,t.sha256_fragmento,'base',x.contextos.map(c=>c.id),'base-18'))}
for(const x of prior.registros_adicionais_por_recorte){let ids=x.links||[];if(x.contexto?.ancora)ids=[...ids,x.contexto.ancora];rows.push(item(x.id,x.arquivo,x.inicio_utf16,x.fim_utf16,x.sha256_fragmento,x.tipo,ids,'adicional-60'))}
assert.equal(rows.length,78);assert.equal(new Set(rows.map(x=>x.id)).size,78);
let result={versao:'r28-parcial-r1',estado_global:'QA09_EM_CORRECAO_NAO_APROVADO',estado_ponte:'PENDENTE_REVALIDACAO_INDIVIDUAL_E_AUDITORIA',base_r27:{ledger:Q+'ledger-r27-expandido-r3/ledger.json',sha256:files[Q+'ledger-r27-expandido-r3/ledger.json'],parecer:Q+'auditoria-ledger-r27-expandido-r3-graficos/parecer.md',parecer_sha256:files[Q+'auditoria-ledger-r27-expandido-r3-graficos/parecer.md']},entrega_r28:{arquivo:P+'entrega-r28.md',sha256:files[P+'entrega-r28.md']},fotografias:{aula_r28:files[P+'resultado/depois-aula.html'],formulario_r28:files[P+'resultado/depois-formulario.html'],inventario_r28:files[Q+'inventario-r28.json'],mapa:files[Q+'mapa-correspondencia-inventario-r27-r28-r1.json']},colecoes:{ocorrencias:{total:11409,estado_padrao:'pendente_de_integracao'},referencias:{total:816,estado_padrao:'pendente_de_integracao'},recursos:{total:138,estado_padrao:'pendente_de_integracao'},ativos_especificos:{total:6,estado_padrao:'pendente_de_integracao'}},objetos:rows,limites:['Correspondência é estrutural e não transfere aceites: todos os 78 objetos ficam pendentes até reavaliação e auditoria.','Nenhuma referência, recurso, pai ou filho é aprovado por esta ponte.','A aplicação r28 ainda aguarda parecer independente; não se presume validade científica.']};
if(process.argv.length===2)console.log(JSON.stringify(result,null,2));else{assert.equal(process.argv.length,4);assert.equal(process.argv[2],'--verificar');assert.deepEqual(JSON.parse(fs.readFileSync(process.argv[3],'utf8')),result);console.log(JSON.stringify({ok:true,objetos:rows.length,contextos_alterados:rows.flatMap(x=>x.contextos.filter(c=>c.alterado).map(c=>[x.id,c.id])),estado:result.estado_ponte}))}
