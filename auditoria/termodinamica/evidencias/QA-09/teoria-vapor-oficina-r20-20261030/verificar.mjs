import fs from 'node:fs';
import {parseHtml,sha256} from '../../../inventario/validar-inventario.mjs';
const d='auditoria/termodinamica/evidencias/QA-09/', h=fs.readFileSync(d+'aplicacao-mistura-fase-r20-r1/resultado/depois-aula.html','utf8'), ib=fs.readFileSync(d+'inventario-r20.json');
if(sha256(h)!=='b05a68731a6975755c0030c524e7915d7833aacb176f680b3890fe82efc803e7'||sha256(ib)!=='e548f61cde56f676dd0c670924bd58e7012a2f80229231de6560cbb55831adf4')throw Error('identidade');
const p=parseHtml(h);if(p.errors.length)throw Error('parser');
const blocos=[['base-vapor-industrial',401887,403360,'cbd7d434779e2735d1b557edcb34efef963dfac5aeea4ac370dbc8b18a04bd3b'],['cobertura99-estado',464014,466408,'d8b7a8b53b7db7fcc0f3f1fd8b8a58c2f8d489e7583efd0f4c08596b542616cb'],['cobertura99-trabalho',466408,468536,'e9356e4155ae358b3b027e4e97673cd35a897f70237487b1ea493cd2b44938c9'],['cobertura99-balancos',468536,470827,'4451335fe6fe7961c9651fe5488f717dfa0f8ae1a4e2fbc776897ec890f36a65'],['cobertura99-limites',470827,472831,'bf4fb0e14c504c3e030f83b0cea8e460b4471ae0244934d50cf66417a5a41374']];
for(const [id,s,e,sha] of blocos){let ns=p.nodes.filter(n=>n.attrs.id===id);if(ns.length!==1)throw Error(id);let n=ns[0].tag==='h3'?ns[0].parent:ns[0];if(n.start!==s||n.end!==e||sha256(h.slice(s,e))!==sha)throw Error('bloco '+id)}
const x=(1380-500)/(2700-500), x2=(2040-500)/(2700-500), w1=150*(.30-.10), w2=(200+100)/2*(.30-.10),wc=120*(.15-.40),du=-10-wc, wt=-50-2*(2800-3200),wp=15+3*(290-250),sg1=400/300-1000/600,sg2=600/300-900/500;
const valores={titulo:x, massa_vapor:5*x, massa_liquido:5*(1-x),titulo2:x2,vapor2:8*x2,liquido2:8*(1-x2),trabalho1:w1,trabalho2:w2,compressao:wc,energia_interna:du,potencia_turbina:wt,potencia_compressor:wp,rendimento_motor:600/1000,carnot_motor:1-300/600,entropia_motor:sg1,rendimento_motor2:300/900,carnot_motor2:1-300/500,entropia_motor2:sg2};
const approx=(a,b)=>Math.abs(a-b)<1e-10;
for(const [a,b] of [[x,.4],[5*x,2],[x2,.7],[8*x2,5.6],[8*(1-x2),2.4],[w1,30],[w2,30],[wc,-30],[du,20],[wt,750],[wp,135],[sg1,-1/3],[sg2,.2]])if(!approx(a,b))throw Error('conta');
console.log(JSON.stringify({ok:true,blocos:blocos.map(([id,inicio,fim,sha])=>({id,inicio,fim,sha})),valores,limite:'Identidade e aritmética; hipóteses e fontes examinadas manualmente.'},null,2));
