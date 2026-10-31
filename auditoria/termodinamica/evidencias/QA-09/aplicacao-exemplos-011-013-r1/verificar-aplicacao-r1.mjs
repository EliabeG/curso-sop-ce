import fs from 'node:fs';
import {parseHtml,isInventoryArticle,sha256} from '../../../inventario/validar-inventario.mjs';
const d='auditoria/termodinamica/evidencias/QA-09/';
const p=d+'aplicacao-exemplos-011-013-r1/';
const old=fs.readFileSync(p+'antes/e1-termodinamica.html','utf8');
const now=fs.readFileSync('modulos/e1-termodinamica.html','utf8');
const snapshot=fs.readFileSync(p+'e1-termodinamica-depois.html','utf8');
let reconstructed=old, details=[];
for(const id of ['011','013']){
 const j=JSON.parse(fs.readFileSync(`${d}exemplo-${id}-candidata-r1.json`,'utf8'));
 const original=fs.readFileSync(`${d}exemplo-${id}-original-r1.html`,'utf8').replace(/\n$/,'');
 const candidate=fs.readFileSync(`${d}exemplo-${id}-candidata-r1.html`,'utf8').replace(/\n$/,'');
 if(sha256(original)!==j.original_sha256_fragmento||sha256(candidate)!==j.candidata_sha256_fragmento||original.replace(j.antes,j.depois)!==candidate||reconstructed.split(original).length!==2||now.split(candidate).length!==2)throw Error(`Falha ${id}`);
 reconstructed=reconstructed.replace(original,candidate);
 details.push({id,original:j.original_sha256_fragmento,candidata:j.candidata_sha256_fragmento});
}
if(reconstructed!==now||now!==snapshot)throw Error('HTML não corresponde às duas substituições');
const extract=html=>{let doc=parseHtml(html);if(doc.errors.length)throw Error(JSON.stringify(doc.errors));return doc.nodes.filter(isInventoryArticle).map(n=>({id:n.attrs.id,text:html.slice(n.start,n.end)}));};
const a=extract(old),b=extract(now);if(a.length!==197||JSON.stringify(a)!==JSON.stringify(b))throw Error('Artigos não preservados');
const prev=JSON.parse(fs.readFileSync(p+'antes/inventario-questoes.json','utf8'));
const curr=JSON.parse(fs.readFileSync('auditoria/termodinamica/inventario/inventario-questoes.json','utf8'));
if(JSON.stringify(prev.itens)!==JSON.stringify(curr.itens)||curr.itens.length!==197)throw Error('Registros alterados');
const keys=Object.keys(prev).filter(k=>JSON.stringify(prev[k])!==JSON.stringify(curr[k]));
if(JSON.stringify(keys)!=='["fonte"]'||curr.fonte.sha256!==sha256(now)||curr.fonte.snapshot!==p+'e1-termodinamica-depois.html')throw Error('Fonte de inventário inconsistente');
const out={id:'QA-09',estado:'APLICACAO_LOCAL_AGUARDANDO_AUDITORIA',html_anterior:sha256(old),html_atual:sha256(now),reconstrucao_exata:true,snapshot_igual:true,exemplos:details,artigos_identicos:a.length,registros_identicos:curr.itens.length,campos_topo_json_modificados:keys,limites:'Verificação estrutural via parser do projeto; não é teste em navegador, revisão independente ou aceite integral de QA-09.'};
console.log(JSON.stringify(out,null,2));
