// Verificação em memória e somente leitura; não aplica a candidata.
import fs from 'node:fs';import assert from 'node:assert/strict';
import {parseHtml,isInventoryArticle,sha256} from '../../../inventario/validar-inventario.mjs';
const dir='auditoria/termodinamica/evidencias/QA-09/candidata-fonte-energyplus-r12-20261030';
const m=JSON.parse(fs.readFileSync(`${dir}/manifesto.json`)), bytes=fs.readFileSync(m.documento), html=bytes.toString('utf8'), invBytes=fs.readFileSync(m.inventario), inv=JSON.parse(invBytes);
assert.equal(sha256(bytes),m.sha256_documento);assert.equal(sha256(invBytes),m.sha256_inventario);
const item=inv.referencias[m.indice_r12];assert.equal(item.arquivo,m.documento);assert.equal(item.inicio_utf16,m.inicio_utf16);assert.equal(item.fim_utf16,m.fim_utf16);assert.equal(item.valor,m.url_original);assert.equal(item.secao,m.secao);assert.equal(item.ancora,m.ancora);
const a=fs.readFileSync(`${dir}/original.html`,'utf8').replace(/\n$/,''),b=fs.readFileSync(`${dir}/candidata.html`,'utf8').replace(/\n$/,'');
assert.equal(sha256(a),m.original_fragmento_sha256);assert.equal(sha256(b),m.candidata_fragmento_sha256);assert.equal(a.replace(m.url_original,m.url_candidata),b);assert.equal(html.slice(m.inicio_utf16,m.fim_utf16),a);assert.equal(html.split(a).length-1,1);assert.equal(html.split(b).length-1,0);
const hypothetical=html.replace(a,b),before=parseHtml(html),after=parseHtml(hypothetical);assert.deepEqual(before.errors,[]);assert.deepEqual(after.errors,[]);
const signature=(d,s)=>d.nodes.filter(isInventoryArticle).map(n=>({id:n.attrs.id,sha256:sha256(s.slice(n.start,n.end))}));const prev=signature(before,html),next=signature(after,hypothetical);assert.equal(prev.length,197);assert.deepEqual(prev,next);
const n=after.nodes.find(x=>x.start===m.inicio_utf16&&x.tag==='a');assert.equal(n.attrs.href,m.url_candidata);assert.equal(n.attrs.target,'_blank');assert.equal(n.attrs.rel,'noopener noreferrer');
console.log(JSON.stringify({ok:true,html_antes:sha256(html),html_hipotetico:sha256(hypothetical),indice_r12:m.indice_r12,artigos_preservados:prev.length,original:m.original_fragmento_sha256,candidata:m.candidata_fragmento_sha256,limite:'Simulação isolada; não avalia disponibilidade na rede, a veracidade editorial, QA-09 integral ou navegador real.'},null,2));
