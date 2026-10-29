import fs from 'node:fs';
import {sha256} from '../../inventario/validar-inventario.mjs';
const dir='auditoria/termodinamica/evidencias/QA-09/', html=fs.readFileSync('modulos/e1-termodinamica.html','utf8'), inventory=JSON.parse(fs.readFileSync(dir+'inventario-r2.json','utf8'));
const reports=['diagnosticos-01-05-corretor-r1.md','diagnosticos-06-10-corretor-r1.md'],contents=reports.map(x=>fs.readFileSync(dir+x,'utf8')), errors=[];
if(sha256(html)!=='9ec10053e40640feeb977baea742da3cbe4d546659f772f0256c6b3cb0720a55')errors.push('documento-base mudou');
let diagnostics=inventory.ocorrencias.filter(x=>x.diagnostico>=1&&x.diagnostico<=10).sort((a,b)=>a.diagnostico-b.diagnostico),items=[];
if(diagnostics.length!==10||diagnostics.some((x,i)=>x.diagnostico!==i+1))errors.push('IDs ausentes ou duplicados');
for(const item of diagnostics){let sha=sha256(html.slice(item.inicio_utf16,item.fim_utf16));if(sha!==item.sha256_fragmento)errors.push('fragmento divergente '+item.diagnostico);let report=item.diagnostico<=5?0:1;if(!contents[report].includes(sha)||!contents[report].includes(`## ${String(item.diagnostico).padStart(2,'0')} `))errors.push('vínculo ausente no relatório '+item.diagnostico);items.push({diagnostico:item.diagnostico,fragmento_sha256:sha,arquivo:reports[report]});}
let result={estado:errors.length?'ERRO':'OK_ESTRUTURAL',escopo:'Apenas identidades, hashes e vínculos; não comprova mérito científico, fontes remotas ou revisão independente.',erros:errors,fonte_sha256:sha256(html),inventario_sha256:sha256(fs.readFileSync(dir+'inventario-r2.json')),relatorios:reports.map((f,i)=>({arquivo:dir+f,sha256:sha256(contents[i])})),itens:items};
fs.writeFileSync(dir+'validacao-diagnosticos-01-10-r1.json',JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify(result,null,2));if(errors.length)process.exitCode=1;
