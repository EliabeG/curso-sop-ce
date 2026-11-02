// Leitura somente: verificar identidade dos vínculos da fotografia r9.
import fs from 'node:fs';
import path from 'node:path';
import assert from 'node:assert/strict';
import {parseHtml,sha256} from '../../../inventario/validar-inventario.mjs';

const docPath='modulos/e1-termodinamica.html';
const indexPath='auditoria/termodinamica/evidencias/QA-09/inventario-r9.json';
const doc=fs.readFileSync(docPath,'utf8');
const inventory=fs.readFileSync(indexPath);
assert.equal(sha256(doc),'2d6b8fb2f9c99e04d22c19d7b32bbc3eb20577459d9132e506f9c0acef3f2fc2');
assert.equal(sha256(inventory),'023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d');
const index=JSON.parse(inventory), tree=parseHtml(doc);
assert.deepEqual(tree.errors,[]);
const expected=[
 [119,89321,'d6d480d3fb030ffff3cd6c3fe74555b47f22f4e1b28c6a6bf2401b3d78fcc342'],
 [120,89374,'578ae989d1ef66c6f397f5c8f7fc68b911970f29fb72c0db14d2d4bcd709ba25'],
 [121,89419,'4f59ebab723c05a0d6955befedf808bc4eb0696a07a27b10fdbf4b4b1130a98d'],
 [122,89470,'dc922c31288f58651630a04a615691e0794ac139c61c5a067f502dea53557981'],
 [123,89518,'4f4ad7178213c3e0f83f387b631742898594a0fc8566cad9a2afb1d4bb037bf4'],
 [124,91619,'0ad0b9d916e745d7934dd3933afff561723e336dea94e6c9e244e090ff81468c'],[125,91666,'be1a67932417e0f84d2aabd76d7bcd8fa6a9b45736ed63a83492fda52fd5d26f'],[126,91720,'3cabcce43b452ccb7f625fb1e01f9367b6561e3e8bef62d3dcd7e77bcc121bd9'],
 [127,93374,'422eff884b6a703f9e6965985c52a6e64ae9157a64f21581f02479e39e89ff4b'],
 [128,96144,'17c0d12383e3f0020bd27d1d7d89a808fb17e5aed2768e6f234cd0b6575facfa'],
 [129,96277,'d092fc46d9874ff535b58662e9a8dc1d0b45b3e535826e6402238c8db8a52161'],
 [130,98508,'24d835438be34a455077c6b66ddf1c8966bf51411e307977a1bcb9969f5a5289'],
 [131,101147,'b4dea96589f0c12bbd28c5a108e3a422a9bac54d081ca036b1a18551d5d1f068'],
 [132,104593,'3bfaff74d363de44a67b97b58bc77347c0559b9230a22bff003dc88ba07b2335'],
 [133,104826,'8f95640b19615cf68bdcc886a676e2f0eba362a4d57bd739c710f0a011cb75a6'],
 [134,106252,'1052b722eb00718d18ba9cfa64f759b9186c592dc80262aa8796e15e13ccef1c'],
 [135,108702,'f39fdd56c45ebc5be4dcb21e79f9579f0b9163ded4838b882447f95e021d936d'],
 [136,110317,'4455d32e38016510aef48a988e22c79189a2488087dd116186427fd3ba3e3970'],
 [137,111315,'4455d32e38016510aef48a988e22c79189a2488087dd116186427fd3ba3e3970'],
 [138,111543,'b47544d4dcb8ab1e9314e9a6f30fe6de31af91062a30d78690b941c4739fb858'],
 [139,113050,'028d9a744da3a7987e4200f1295ea80feb241838171a01c07317643fd661d85f'],
 [140,113328,'b2bb16a7c0fa6ccf439b985eeeb0fb76581644fda9c89c1323b28a373323a2bb']
];
const out=[];
for(const [i,start,expectedHash] of expected){
 const item=index.referencias[i];assert.equal(item.arquivo,docPath);assert.equal(item.inicio_utf16,start);assert.equal(item.tag,'a');assert.equal(item.atributo,'href');
 const match=tree.nodes.filter(n=>n.start===item.inicio_utf16&&n.end===item.fim_utf16);assert.equal(match.length,1);const node=match[0];assert.equal(node.attrs.href,item.valor);
 const hash=sha256(doc.slice(node.start,node.end));assert.equal(hash,expectedHash);
 let destination=null;if(item.valor.startsWith('#')){const id=item.valor.slice(1);const found=tree.nodes.filter(n=>n.attrs.id===id);assert.equal(found.length,1);destination={tipo:'ancora_interna',id,quantidade:found.length};}
 else if(!/^https?:/.test(item.valor)){const dest=path.resolve(path.dirname(docPath),item.valor);assert(fs.statSync(dest).isFile());destination={tipo:'arquivo_local',arquivo:path.relative('.',dest),sha256:sha256(fs.readFileSync(dest))};}
 else destination={tipo:'url_externa',acesso:'não testado por este script'};
 out.push({indice_r9:i,arquivo:item.arquivo,secao:item.secao,ancora:item.ancora,inicio_utf16:item.inicio_utf16,fim_utf16:item.fim_utf16,href:item.valor,texto:item.texto,sha256_html:hash,destino:destination});
}
console.log(JSON.stringify({ok:true,base_sha256:sha256(doc),inventario_sha256:sha256(inventory),referencias:out,limite:'Identidade e existência local; conteúdo externo, licenças, confiabilidade e validação integral exigem avaliação independente.'},null,2));
