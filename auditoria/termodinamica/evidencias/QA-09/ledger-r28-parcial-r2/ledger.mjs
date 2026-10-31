/** Ponte r27→r28: reextrai recortes e contextos; não concede aceite por identidade. */
import fs from 'node:fs';import crypto from 'node:crypto';import assert from 'node:assert/strict';import {parseHtml} from '../../../inventario/validar-inventario.mjs';
const Q='auditoria/termodinamica/evidencias/QA-09/',D=Q+'ledger-r28-parcial-r2/',P=Q+'aplicacao-conjunta-r28/',sha=x=>crypto.createHash('sha256').update(x).digest('hex');
const files={
 [D+'reconciliacao.md']:'a0f53441b052372a3d7f2df12a3b9b02218a0fbf1ef7032f4c70cbf38b812af1',
 'modulos/e1-termodinamica.html':'d7294e8ed772cf4530788586d693a6cdfbf1ef6fa05c69afbc984efc46e353d8',
 'formulas/termodinamica.html':'3157c9b114f3156e5517440d30b91ee8a4efdebcd95be8bd0c7a588f04dead46',
 [Q+'auditoria-aplicacao-r28-next-theory-20261030/parecer.md']:'0b69b0e17287a80c188fb3f8dad462ac54819d893099be6af6ff1354bdcd1b18',
 [D+'juizos.json']:'4e3a566c41cd21b057af57a194b596d7fa85e60f0ca6b7e9eae181fdc16cf908',
 [Q+'ledger-r28-parcial-r1/ledger.json']:'850dd7f87ae617348d4775fadfe97c0aaa73210207aa24400cb1b85ac72fc2db',
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
const oldr1=JSON.parse(read(Q+'ledger-r28-parcial-r1/ledger.json'));assert.deepEqual(rows,oldr1.objetos);
const oldMap=new Map(map.pares.filter(x=>x.id_r27).map(x=>[x.id_r27,x]));assert.equal(oldMap.size,i27.ocorrencias.length);
const indexNew=new Map(i28.ocorrencias.map(x=>[x.id,x]));const indexOld=new Map(i27.ocorrencias.map(x=>[x.id,x]));assert.equal(indexNew.size,11409);assert.equal(indexOld.size,11407);let newIds=new Set();
for(const p of map.pares){if(p.id_r27){let o=indexOld.get(p.id_r27);assert.ok(o);assert.equal(o.sha256_fragmento,p.sha256_r27)}if(p.id_r28){let n=indexNew.get(p.id_r28);assert.ok(n);assert.equal(n.sha256_fragmento,p.sha256_r28);assert.ok(!newIds.has(p.id_r28));newIds.add(p.id_r28)}}assert.equal(newIds.size,11409);
assert.deepEqual([i28.referencias.length,i28.recursos.length,i28.ativos_especificos.length],[816,138,6]);
for(const x of prior.registros_adicionais_por_recorte.filter(x=>x.ativo)){assert.equal(sha(fs.readFileSync(x.ativo.arquivo)),x.ativo.sha256)}
for(const [i,x] of prior.registros_explicitamente_revisados.entries()){
 let o=x.identidade_r27,p=oldMap.get(o.id),n=indexNew.get(p?.id_r28);assert.ok(p&&n,`mapeamento ${x.id_local}`);assert.equal(p.sha256_r27,o.sha256_fragmento);assert.equal(p.sha256_r28,o.sha256_fragmento);assert.equal(n.sha256_fragmento,o.sha256_fragmento);assert.equal(n.tipo,o.tipo);assert.equal(n.arquivo,o.arquivo);assert.equal(n.inicio_utf16,rows[i].r28.inicio_utf16);assert.equal(n.fim_utf16,rows[i].r28.fim_utf16);rows[i].par_inventario={id_r27:o.id,id_r28:n.id,estado:p.estado};
}
// Nas quatro figuras, reextrai também o contêiner imediato, sem promover o contexto.
for(const x of rows.filter(x=>x.tipo==='figura_svg')){
 let d=docs[x.arquivo];function parent(h,dom,start){let node=dom.nodes.find(n=>n.tag==='figure'&&n.start===start);assert.ok(node,`figura ${x.id}`);while(node&&!(node.tag==='div'&&(node.attrs.class||'').split(/\s+/).includes('bloco-aula')))node=node.parent;assert.ok(node,`entorno ${x.id}`);return h.slice(node.start,node.end)}let o=parent(d.old,d.od,x.r27.inicio_utf16),n=parent(d.now,d.nd,x.r28.inicio_utf16);x.contexto_figura={sha256_r27:sha(o),sha256_r28:sha(n),alterado:o!==n};assert.equal(o,n,`contexto alterado ${x.id}`)
}
const decisions=JSON.parse(read(D+'juizos.json'));let report=read(D+'reconciliacao.md');for(const x of decisions)assert.ok(report.includes('| '+x.id+' | '+x.juizo_local+' | '+x.efeito_deltas+' |'),`juízo ausente ${x.id}`);assert.equal(decisions.length,78);assert.deepEqual(decisions.map(x=>x.id),rows.map(x=>x.id));for(let i=0;i<78;i++){assert.ok(decisions[i].juizo_local&&decisions[i].efeito_deltas);rows[i].juizo=decisions[i];rows[i].estado='revalidado_pelo_integrador_pendente_de_auditoria_independente'}
const near=(x,y)=>assert.ok(Math.abs(x-y)<1e-9,`${x} != ${y}`);
near(9/.010,900);near(-10+120,110);near(10+(30/40)*80,70);near((900-400)/(2400-400),.25);near(.082*320/26.24,1);
near((600+900-20)/3200,.4625);near((700-300)/(2300-300),.2);near(.8*10*250,2000);near((.2+500*(.0004-.0006))/200*1e6,500);
near((140-50)/300,.3);near(6/8,.75);near(18+120/(6*2),28);near((12+24+36)/3,24);near((2*90+6*30)/8,45);near((4*80+4*20+2*20-20)/10,42);near(.5*4.2*20,42);near(.36/.0005,720);near(1000*10*(36/3600)*15,1500);
near(3/(3+2),.6);near(250*.004,1);near(200/.01,20000);near((1*20+3*60)/4,50);near((200-100)*2,200);near(300*(3-1),600);near(100*(3-1),200);
near(2*(45-20),50);near(300*.2,60);near(-30-(-180),150);near(1-300/900,2/3);near(280*.15,42);near(.001*600,.6);near(1.25*320,400);near(.8*100+.001*(400**2-300**2)/2,115);near((2*100+400+30)/3,210);near(Math.sqrt(100**2+2*1000*75),400);near((1000-500)/(2500-500),.25);near((2700-500)/(2500-500),1.1);near(-20+150,130);near(.3/.75,.4);
near(1590/3590,.4428969359331476);near(290/2490,.11646586345381526);near(3.5/5,.7);near(20/1000,.02);near(.24/.0004,600);near(.2/500*1e6+450,850);near(1000*10*(54/3600)*20,3000);near(2800+.3*200,2860);near(-.2+.3,.1);near(Math.sqrt(1*16),4);
let result={versao:'r28-parcial-r2',estado_global:'QA09_EM_CORRECAO_NAO_APROVADO',estado_ponte:'PENDENTE_AUDITORIA_INDEPENDENTE',base_r27:{ledger:Q+'ledger-r27-expandido-r3/ledger.json',sha256:files[Q+'ledger-r27-expandido-r3/ledger.json'],parecer:Q+'auditoria-ledger-r27-expandido-r3-graficos/parecer.md',parecer_sha256:files[Q+'auditoria-ledger-r27-expandido-r3-graficos/parecer.md']},entrega_r28:{arquivo:P+'entrega-r28.md',sha256:files[P+'entrega-r28.md']},parecer_aplicacao:{arquivo:Q+'auditoria-aplicacao-r28-next-theory-20261030/parecer.md',sha256:files[Q+'auditoria-aplicacao-r28-next-theory-20261030/parecer.md']},fotografias:{aula_r28:files[P+'resultado/depois-aula.html'],formulario_r28:files[P+'resultado/depois-formulario.html'],inventario_r28:files[Q+'inventario-r28.json'],mapa:files[Q+'mapa-correspondencia-inventario-r27-r28-r1.json']},colecoes:{ocorrencias:{total:11409,estado_padrao:'pendente_de_integracao'},referencias:{total:816,estado_padrao:'pendente_de_integracao'},recursos:{total:138,estado_padrao:'pendente_de_integracao'},ativos_especificos:{total:6,estado_padrao:'pendente_de_integracao'}},objetos:rows,limites:['Os 78 objetos foram reavaliados individualmente pelo integrador; a ponte aguarda parecer independente e não há aceite automático por identidade.','Nenhuma referência, recurso, pai ou filho é aprovado por esta ponte.','A aplicação r28 foi auditada em seu recorte; a ponte exige seu próprio parecer independente.']};
if(process.argv.length===2)console.log(JSON.stringify(result,null,2));else{assert.equal(process.argv.length,4);assert.equal(process.argv[2],'--verificar');assert.deepEqual(JSON.parse(fs.readFileSync(process.argv[3],'utf8')),result);console.log(JSON.stringify({ok:true,objetos:rows.length,contextos_alterados:rows.flatMap(x=>x.contextos.filter(c=>c.alterado).map(c=>[x.id,c.id])),estado:result.estado_ponte}))}
