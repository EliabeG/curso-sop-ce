// Auditoria localizada da candidata sem alterar fontes ou evidências históricas.
import fs from 'node:fs';
import {parseHtml,isInventoryArticle,sha256} from '../../../inventario/validar-inventario.mjs';
const dir='auditoria/termodinamica/evidencias/QA-09/diagnostico02-candidata-r9-20261030/';
const html=fs.readFileSync('modulos/e1-termodinamica.html','utf8');
const inv=JSON.parse(fs.readFileSync('auditoria/termodinamica/evidencias/QA-09/inventario-r9.json','utf8'));
const manifest=JSON.parse(fs.readFileSync(dir+'manifesto.json','utf8'));
const orig=fs.readFileSync(dir+'original.html','utf8').replace(/\n$/,'');
const candidate=fs.readFileSync(dir+'candidata.html','utf8').replace(/\n$/,'');
function ok(value,message){if(!value)throw Error(message)}
ok(sha256(html)===manifest.html_sha256,'HTML diferente');
ok(sha256(fs.readFileSync('auditoria/termodinamica/evidencias/QA-09/inventario-r9.json'))===manifest.inventario_sha256,'inventário diferente');
ok(sha256(orig)===manifest.original_fragmento_sha256 && sha256(candidate)===manifest.candidata_fragmento_sha256,'hash dos fragmentos');
const matches=inv.ocorrencias.filter(x=>x.diagnostico===2 && x.tipo==='exemplo_ou_diagnostico');
ok(matches.length===1 && matches[0].id===manifest.id_inventario && matches[0].inicio_utf16===manifest.inicio_utf16 && matches[0].fim_utf16===manifest.fim_utf16 && matches[0].sha256_fragmento===sha256(orig),'identidade r9');
ok(html.slice(manifest.inicio_utf16,manifest.fim_utf16)===orig && html.split(orig).length===2 && !html.includes(candidate),'localização e unicidade');
ok(orig.split(manifest.antes).length===2 && orig.replace(manifest.antes,manifest.depois)===candidate,'delta literal');
const candidateHtml=html.replace(orig,candidate), a=parseHtml(html), b=parseHtml(candidateHtml);
ok(!a.errors.length && !b.errors.length,'erro de parser');
const articles=d=>d.nodes.filter(isInventoryArticle).map(x=>[x.attrs.id,d===a?html.slice(x.start,x.end):candidateHtml.slice(x.start,x.end)]);
const before=articles(a),after=articles(b);
ok(before.length===197 && JSON.stringify(before)===JSON.stringify(after),'artigos modificados');
ok(-20+150===130,'span');
console.log(JSON.stringify({ok:true,fragmento_original:sha256(orig),fragmento_candidato:sha256(candidate),artigos_preservados:before.length,span_130_C:true,limite:'Simulação de candidata, não confirma aplicação nem teste em navegador.'},null,2));
