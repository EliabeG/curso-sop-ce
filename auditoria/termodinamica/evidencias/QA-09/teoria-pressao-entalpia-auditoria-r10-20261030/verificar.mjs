// Auditoria independente: leitura somente; recusa qualquer versão diferente.
import fs from 'node:fs';
import assert from 'node:assert/strict';
import {parseHtml,sha256} from '../../../inventario/validar-inventario.mjs';

const doc=fs.readFileSync('modulos/e1-termodinamica.html','utf8');
const inventory=fs.readFileSync('auditoria/termodinamica/evidencias/QA-09/inventario-r10.json');
const map=JSON.parse(fs.readFileSync('auditoria/termodinamica/evidencias/QA-09/mapa-correspondencia-inventario-r9-r10-r1.json'));
assert.equal(sha256(doc),'a8bed8a91a36a1c1f41cd75e3c1858fecb4e14a506e582ad1fdb186d275805e3');
assert.equal(sha256(inventory),'3497cbf9ffcbe0a1e2eb84eeb9e34c0cfb6e0ed63a2747795bf75832454e2f6c');
const inv=JSON.parse(inventory),parsed=parseHtml(doc);assert.deepEqual(parsed.errors,[]);
const samples=[
 [165435,165435,'993922dc816b0c2684ae205a1890d227bb7e606884478239f87a8737e14063d8','993922dc816b0c2684ae205a1890d227bb7e606884478239f87a8737e14063d8'],
 [197407,197407,'6f856d492c2419d1f9eb718b90e9858baa8b1b9c6a8e1dd9826b447ef8d43768','6f856d492c2419d1f9eb718b90e9858baa8b1b9c6a8e1dd9826b447ef8d43768'],
 [199954,199954,'0ca5ea6093bb2e42c319ad85401e6ccf6c88ced790993a3d0bf5fb1391201c02','35ab3e655554616a57c86dc1d4974c010d3a93858498b4310906ad3b012ee3b0'],
 [200231,200393,'1b536f3d105ae3b920527925a73a87322ee84c5848737cac4761f069ecd3198d','1b536f3d105ae3b920527925a73a87322ee84c5848737cac4761f069ecd3198d'],
 [405901,406063,'d1ccb7c4e5542572cd3b76b3230e9c837723d93c8db05bd7b349f4cf412f7f0c','4a70b05f49062ec6a83dd1c9941a72466ec9943ed49b778c6222f5467d2f2f38']
];
let matches=[];
for(const [oldStart,start,oldHash,hash] of samples){
 const key=`modulos/e1-termodinamica.html:${start}:texto`;
 const found=inv.ocorrencias.filter(o=>o.id===key);assert.equal(found.length,1);const occ=found[0];assert.equal(occ.sha256_fragmento,hash);
 const nodes=parsed.nodes.filter(n=>n.start===start&&n.end===occ.fim_utf16);assert.equal(nodes.length,1);let n=nodes[0],pos=n.openEnd,parts=[];
 for(const c of n.children){if(c.start>pos)parts.push(doc.slice(pos,c.start));pos=Math.max(pos,c.end)}
 if(n.end>pos)parts.push(doc.slice(pos,n.end).replace(new RegExp(`</${n.tag}\\s*>\\s*$`,'i'),''));
 assert.equal(sha256(parts.join(' ')),hash);
 const pairs=map.pares.filter(p=>p.id_r9===`modulos/e1-termodinamica.html:${oldStart}:texto`&&p.id_r10===key);assert.equal(pairs.length,1);assert.equal(pairs[0].sha256_r9,oldHash);assert.equal(pairs[0].sha256_r10,hash);
 matches.push({id_r9:pairs[0].id_r9,id_r10:key,tipo: pairs[0].estado,sha256:hash});
}
for(const name of ['combustao','vaporizacao']){
 const dir='auditoria/termodinamica/evidencias/QA-09/teoria-pressao-entalpia-r9-20261030/';
 let orig=fs.readFileSync(`${dir}${name}-original.html`,'utf8').replace(/\n$/,''),candidate=fs.readFileSync(`${dir}${name}-candidata.html`,'utf8').replace(/\n$/,'');
 assert.equal(doc.split(orig).length-1,0);assert.equal(doc.split(candidate).length-1,1);
}
// Frações decimais exatas nestes dados hipotéticos por escala inteira.
const U=718, W=287, Q=U+W;assert.equal(Q,1005); // décimos kJ
assert.equal(400+80,480);assert.equal(400+100,500);assert.equal(-(-50),50);
console.log(JSON.stringify({ok:true,html_sha256:sha256(doc),inventario_sha256:sha256(inventory),correspondencias:matches,contas:{ideal_gas_kJ:{deltaU:U/10,W:W/10,Q:Q/10},contraste_kJ:{Q:480,deltaH:500},reacao_reversa_kJ:50},limite:'Verificação de identidade e contas; parecer científico e contexto requerem leitura independente; não é aceite integral.'},null,2));
