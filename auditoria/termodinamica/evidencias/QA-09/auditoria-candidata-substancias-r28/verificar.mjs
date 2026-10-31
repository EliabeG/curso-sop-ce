import fs from 'node:fs';import crypto from 'node:crypto';import assert from 'node:assert/strict';import {parseHtml} from '../../../inventario/validar-inventario.mjs';
const q='auditoria/termodinamica/evidencias/QA-09/',d=q+'candidata-substancias-ciclos-r28/',sha=x=>crypto.createHash('sha256').update(x).digest('hex');
const bytes=fs.readFileSync(d+'manifesto.json');assert.equal(sha(bytes),'536c06caca6923b0e431995fefb682bd196bc1ab95cf75c5ad2bd2cb5db60be6');assert.equal(sha(fs.readFileSync(d+'analise.md')),'2cac89398ed762ecc5e5eb4b1384939952a90ffe490ff6f2d149c4ceb0258ae9');
const m=JSON.parse(bytes),source=fs.readFileSync('modulos/e1-termodinamica.html','utf8');assert.equal(sha(source),'9af8e2c9ffe509e40594d086a9ef4ad75127fb4ca873efb305d3144e08f3fc49');assert.equal(sha(fs.readFileSync('formulas/termodinamica.html')),'16329b7369c4ba927f5f7da30551f86934aad1f6a6e55627443dea5cb9fe0c02');assert.equal(sha(fs.readFileSync(q+'inventario-r27.json')),'a58d7f0b0a5f097eef83ad83026ef49e801457b87f7cf2b2345c3dd915597c7c');assert.equal(sha(fs.readFileSync(q+'auditoria-substancias-r28/parecer.md')),'8d60a5559fe8dea5147e20dceb19ecdfb45a7fc1a88782f8be444e891e804d6e');
assert.equal(m.estado,'CANDIDATA_NAO_APLICADA');assert.deepEqual(m.edicoes.map(x=>x.id),['substancias','ciclos']);let newer=source;
for(const e of [...m.edicoes].reverse()){
 const old=source.slice(e.inicio_utf16,e.fim_utf16);assert.equal(sha(old),e.original_sha256);assert.equal(fs.readFileSync(d+e.id+'-original.html','utf8'),old+'\n');let candidate=old;
 for(const sub of e.substituicoes){assert.equal(candidate.split(sub.antes).length,2);candidate=candidate.replace(sub.antes,sub.depois)}
 assert.equal(sha(candidate),e.candidata_sha256);assert.equal(fs.readFileSync(d+e.id+'-candidata.html','utf8'),candidate+'\n');
 const o=parseHtml(old),n=parseHtml(candidate);for(const tag of ['table','math'])assert.deepEqual(o.nodes.filter(x=>x.tag===tag).map(x=>old.slice(x.start,x.end)),n.nodes.filter(x=>x.tag===tag).map(x=>candidate.slice(x.start,x.end)));
 newer=newer.slice(0,e.inicio_utf16)+candidate+newer.slice(e.fim_utf16)
}
assert.equal(sha(newer),'876e05056e5aa380ffc4d48247ff354510f9d237afb4c26ef67e3c82b81aa649');let a=parseHtml(source),b=parseHtml(newer);assert.deepEqual(a.errors,[]);assert.deepEqual(b.errors,[]);
for(const [tag,count] of [['article',197],['math',734]]){let aa=a.nodes.filter(x=>x.tag===tag).map(x=>source.slice(x.start,x.end));let bb=b.nodes.filter(x=>x.tag===tag).map(x=>newer.slice(x.start,x.end));assert.equal(aa.length,count);assert.deepEqual(aa,bb)}
const attrs=d=>d.nodes.map(n=>[n.tag,Object.entries(n.attrs).filter(([k])=>['id','href','src'].includes(k)||k.startsWith('aria-'))]).filter(x=>x[1].length);assert.deepEqual(attrs(a),attrs(b));
console.log(JSON.stringify({ok:true,duas_edicoes:m.edicoes.length,substituicoes:m.edicoes.reduce((s,x)=>s+x.substituicoes.length,0),artigos:197,mathml:734,atributos:'preservados',tabelas:'preservadas',hipotetico:sha(newer),sem_alteracao_de_produto:true}));
