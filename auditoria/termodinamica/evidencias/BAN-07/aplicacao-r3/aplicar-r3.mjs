import fs from 'node:fs/promises';
import path from 'node:path';
import assert from 'node:assert/strict';
import {fileURLToPath} from 'node:url';
import {sha256,validateInventory} from '../../../inventario/validar-inventario.mjs';
const here=path.dirname(fileURLToPath(import.meta.url)),root=path.resolve(here,'../../../../..');
const hashes={
 'modulos/e1-termodinamica.html':'80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0',
 'auditoria/termodinamica/inventario/inventario-questoes.json':'71ac07e042aa65675fc3d4b69d8d0ae11cb66df967d45e66b1a88f4f1350e074',
 'auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md':'35df191e2f7964adfb7b975668491e8ba39d983a5df93640a35d3d96ae142df8',
 'auditoria/termodinamica/evidencias/BAN-07/e1-termodinamica.r2.html':'80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0',
 'auditoria/termodinamica/evidencias/BAN-07/revisao-fon02-complementar-r2.json':'42ce5afe33e0481562c7673daaf25b359b8580b30276d9df75a1965adaa68399',
 'auditoria/termodinamica/evidencias/BAN-07/triagem-ban10-complementar-r2.json':'cc03d1fdf3a2401c93ea193ce99ed44d79c5a937d908e202ca03ee914b9d819d',
 'auditoria/termodinamica/evidencias/BAN-07/confronto-fon01-cr-r2.json':'d7fb0464f2c33701da8396a400c489dcde5096fc66de8c7d3e4d143ee7def9e4',
 'auditoria/termodinamica/evidencias/BAN-07/manifesto-r2.json':'471b222e81c17a257a008a38671eb617498720f0add1f1baf7343baa0b0b413d',
 'auditoria/termodinamica/entregas/BAN-07-r2.md':'c9b19afcf3c3ddb0f8033b6fd13090d31750d60e31c68751804159e5c9b44bee',
 'assets/curso.js':'a20f4d19158073a9a1c48aabdfba8fa863b02063e16061c00b16448a6ccc2e13',
 'assets/registro.js':'46da94527d6639fe0265bd766286f1ef39623966105e00bda3b31f21ca2c247c'};
const hash=async f=>sha256(await fs.readFile(path.join(root,f)));
for(const [f,h] of Object.entries(hashes))assert.equal(await hash(f),h,'Fonte r2 divergente: '+f);
const invPath='auditoria/termodinamica/inventario/inventario-questoes.json',originalBytes=await fs.readFile(path.join(root,invPath)),original=JSON.parse(originalBytes.toString('utf8'));
const old='Relacionar dilatação constante com transformação afim entre escalas',novo='Reconhecer a relação afim entre as escalas quando ambas são lineares na altura da coluna, conforme hipótese editorial do curso';
const raw=originalBytes.toString('utf8');assert.equal(raw.split(old).length,3,'Número inesperado de ocorrências');const updatedRaw=raw.replaceAll(old,novo);assert.equal(sha256(updatedRaw),'486c53c5aa6c432831599c4eca170e4620d089b4eb15b480dbfb2cbfaf54c9ce');
const updated=JSON.parse(updatedRaw),clone=structuredClone(updated),item=clone.itens.find(x=>x.id==='cr-e1-06');assert.deepEqual(item.raciocinio.etapas,[novo]);assert.ok(item.vinculo_competencias.alcance.includes(novo));item.raciocinio.etapas=[old];item.vinculo_competencias.alcance=item.vinculo_competencias.alcance.replace(novo,old);assert.deepEqual(clone,original,'Outros campos mudaram');
const atual=updated.itens.find(x=>x.id==='cr-e1-06');assert.equal(atual.raciocinio.numero_etapas,1);assert.equal(atual.raciocinio.categoria,'reconhecimento');assert.equal(atual.nivel.estimado,'iniciante');assert.deepEqual(atual.competencias,['C08']);
const md=(await fs.readFile(path.join(root,'auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md'),'utf8')).split(/\r?\n/).filter(x=>x.includes('#cr-e1-06)'));assert.equal(md.length,1);const cols=md[0].split('|').map(x=>x.trim()).filter(Boolean);assert.equal(cols[1],atual.competencias.join(', '));assert.equal(cols[2],atual.nivel.estimado);assert.equal(Number(cols[3]),atual.raciocinio.numero_etapas);assert.equal(cols[4],atual.nivel.justificativa);
const preview=await validateInventory({rootDir:root,inventory:updated});assert.equal(preview.ok,true,JSON.stringify(preview.erros));
const backup=path.join(here,'inventario-r2-antes.json');try { await fs.access(backup); } catch (e) { if (e.code !== 'ENOENT') throw e; await fs.copyFile(path.join(root,invPath),backup,1); } assert.equal(sha256(await fs.readFile(backup)),hashes[invPath]);
const controle='auditoria/termodinamica/CONTROLE_AAA.json',controleAntes=await hash(controle);const temp=path.join(root,invPath)+'.ban07-r3-'+process.pid+'.tmp';await fs.writeFile(temp,updatedRaw,{flag:'wx'});assert.equal(sha256(await fs.readFile(temp)),sha256(updatedRaw));
let changed=false;
try{
 await fs.rename(temp,path.join(root,invPath));changed=true;assert.equal(await hash(invPath),sha256(updatedRaw));
 const validation=await validateInventory({rootDir:root});assert.equal(validation.ok,true,JSON.stringify(validation.erros));
 const preserved=[];for(const [f,h] of Object.entries(hashes)){if(f===invPath)continue;const actual=await hash(f);assert.equal(actual,h,'Arquivo preservado mudou '+f);preserved.push({arquivo:f,sha256:h,preservado:true})}
 const result={id:'BAN-07',rodada:3,estado:'APLICADO_AGUARDANDO_AUDITORIA',ajuste:'R2-A',data:'2026-10-29',autoria:'Agente automatizado Corretor /root/inspect_repo',arquivo:invPath,sha256_antes:hashes[invPath],sha256_depois:sha256(updatedRaw),alteracoes:[{campo:'itens[id=cr-e1-06].raciocinio.etapas[0]',antes:old,depois:novo},{campo:'itens[id=cr-e1-06].vinculo_competencias.alcance',antes:'Apoio delimitado a C08: '+old+'. Não avalia integralmente a formulação avançada dessas competências.',depois:'Apoio delimitado a C08: '+novo+'. Não avalia integralmente a formulação avançada dessas competências.'}],restauracao_em_memoria_confirma_somente_dois_campos:true,outros_196_registros_preservados:true,numero_etapas_categoria_nivel_competencias_preservados:true,markdown_cr06:{arquivo:'auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md',linha:md[0],conferido_sem_alteracao:true},preservados:preserved,validacao_no_produto:validation,controle_antes:controleAntes,controle_depois:await hash(controle),backup:'auditoria/termodinamica/evidencias/BAN-07/aplicacao-r3/inventario-r2-antes.json',limites:['Alteração semântica de inventário, sem editar HTML, fonte, código ou digitais; não se declara novo teste de navegador, armazenamento ou alunos.','Resultados r2 de persistência são herdados por identidade de HTML e JS, sujeitos à avaliação independente da aplicabilidade.','Nenhum aceite prévio é transferido automaticamente; o próximo ID continua bloqueado.']};
 await fs.writeFile(path.join(here,'verificacao-r3.json'),JSON.stringify(result,null,2)+'\n',{flag:'wx'});console.log(JSON.stringify({estado:result.estado,sha256_depois:result.sha256_depois,controle_preservado:result.controle_antes===result.controle_depois,validacao:{ok:validation.ok,itens:validation.itens_registrados,artigos:validation.artigos_encontrados,recursos:validation.recursos_verificados,links:validation.links_locais_verificados,erros:validation.erros.length,avisos:validation.avisos.length}},null,2));
}catch(e){if(changed)await fs.copyFile(backup,path.join(root,invPath));throw e}
