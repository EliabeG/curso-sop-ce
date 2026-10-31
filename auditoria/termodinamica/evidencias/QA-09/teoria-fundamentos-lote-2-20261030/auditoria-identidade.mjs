import fs from 'node:fs';
import {createHash} from 'node:crypto';
import {parseHtml} from '../../../inventario/validar-inventario.mjs';
const hash=s=>createHash('sha256').update(s).digest('hex');
const b=fs.readFileSync('modulos/e1-termodinamica.html');
const inv=fs.readFileSync('auditoria/termodinamica/evidencias/QA-09/inventario-r7.json');
if(hash(b)!=='200f9b773050594d762cc596a5a89297024b245fc4f504081fc77baaed3db95f'||hash(inv)!=='5090b9897a4698e0ad090f45182afba5880361aabc9fd3c3bdf848d971a85a1a')throw Error('Fotografia alterada');
const str=b.toString('utf8'),doc=parseHtml(str),entries=JSON.parse(inv).ocorrencias;
const positions=[91881,92203,96357,101326,102086,102479,105052,105534,108659,114112,235496,236866,239213,239807,244208,249892,251114];
for(const pos of positions){
 const es=entries.filter(x=>x.arquivo==='modulos/e1-termodinamica.html'&&x.inicio_utf16===pos&&x.tipo==='texto_direto');
 const ns=doc.nodes.filter(x=>x.start===pos); if(es.length!==1||ns.length!==1)throw Error(`identidade ${pos}`);
 const e=es[0],n=ns[0];if(n.tag!==e.tag||n.end!==e.fim_utf16)throw Error(`limites ${pos}`);
 let curr=n.openEnd,parts=[]; for(const child of n.children){if(child.start>curr)parts.push(str.slice(curr,child.start));curr=Math.max(curr,child.end)}
 if(n.end>curr)parts.push(str.slice(curr,n.end).replace(new RegExp(`</${n.tag}\\s*>\\s*$`,'i'),''));
 if(hash(parts.join(' '))!==e.sha256_fragmento)throw Error(`hash texto direto ${pos}`);
}
console.log(JSON.stringify({ok:true,trechos:positions.length,escopo:'identidade dos trechos na fotografia r7; não valida cálculo nem exatidão científica'}));
