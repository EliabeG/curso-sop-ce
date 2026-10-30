// QA-09: leitura local e provas aritméticas explícitas; não escreve arquivos.
import fs from 'node:fs';
import {parseHtml,sha256} from '../../../inventario/validar-inventario.mjs';
const f='modulos/e1-termodinamica.html', h=fs.readFileSync(f,'utf8'), invBytes=fs.readFileSync('auditoria/termodinamica/evidencias/QA-09/inventario-r8.json');
if(sha256(h)!=='57b13f0d6386764f1cc46ce543013b0eb75f7bfa97ffbd63ea331f38bfc5af8c'||sha256(invBytes)!=='ae75a258398c385398567457d98ebd49b9838c0c9a4eedc69ea8d2d72981b687')throw Error('fotografia incorreta');
const expected={1259202:'5396c6d1e1240ca66732e6820ffed475245c7fe9a6742cbc78ae7b5dc5f81bc9',1261823:'fc0033645919a017b37575607415fb2a508a9436e65183ab5f57f0b334b953f4',1264284:'46685d5f37428e0aceeb8c6cb82ff09dffb2aa8cbd017917198b9cddfd8bec3d',1265937:'7ea6e1ce9887bcdceba221a5c72c964277919fd0a800734d20977e9fa433733b',1267176:'16410bbd04aa5b7c096b50f300cb1f402d681dc2b9dada035578bc450090da4d',1269562:'602a68bb4e80c5ce1ad25e667e6dda92c0d4b8877e153df17b179056d9dd38a0',1271918:'aa949d292d261c3b94fc0d5a9982eeb8dfe39131ea4b9e3e3024c93a1b291010',1273639:'ec917b1cc90322626511f0f2d5ffa3defe30f1727b2afc85679fc1483fb91e05',1274986:'4809189c00ed5a2d213efcc8bac3ead8d5d3e486b4e8b39c0b4c6b50db99d7f3'};
const inv=JSON.parse(invBytes);for(const [p,sha] of Object.entries(expected)){const rows=inv.ocorrencias.filter(x=>x.arquivo===f&&x.tipo==='flashcard'&&x.inicio_utf16===+p);if(rows.length!==1||rows[0].sha256_fragmento!==sha||sha256(h.slice(rows[0].inicio_utf16,rows[0].fim_utf16))!==sha)throw Error('flashcard '+p)}
const pos=1283434,doc=parseHtml(h);const nodes=doc.nodes.filter(n=>n.start===pos);if(nodes.length!==1)throw Error('nó resumo');const n=nodes[0];let k=n.openEnd,a=[];for(const c of n.children){if(c.start>k)a.push(h.slice(k,c.start));k=Math.max(k,c.end)}if(n.end>k)a.push(h.slice(k,n.end).replace(new RegExp(`</${n.tag}\\s*>\\s*$`,'i'),''));if(sha256(a.join(' '))!=='1d7ef74579720bc9ba79eb30aa236c2ccd93789bdc0856fefb8bf6ccb1cda637')throw Error('resumo');
const eq=(x,y)=>{if(Math.abs(x-y)>1e-12)throw Error(`${x} != ${y}`)};
// Casos sintéticos, não exercícios publicados.
eq(1-300/600,.5);eq(Math.sqrt(1*16),4);eq(2800+((230-200)/(300-200))*(3000-2800),2860);eq(.6/.8,.75);
// Compressor não adiabático: h1=300 h2s=330 h2real=340; calor recebido q=-20 kJ/kg.
const real=340-300-(-20), ideal=330-300;eq(real,60);eq(ideal/real,.5);eq((330-300)/(340-300),.75);
// Volume de controle transiente: acumulação = entrada - saída com Q=W=0.
eq(2*300-1*250,350);
// Balanço de entropia transiente: Sgen=dS/dt + saída - entrada para Q=0.
eq(2+(3-2),3);
console.log(JSON.stringify({ok:true,flashcards:Object.keys(expected).length,resumo:1,limites:'provas sintéticas; modelos e dados devem ser lidos na aula'}));
