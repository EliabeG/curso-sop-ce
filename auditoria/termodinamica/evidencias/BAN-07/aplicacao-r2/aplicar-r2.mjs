import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import assert from 'node:assert/strict';
import {sha256,validateInventory} from '../../../inventario/validar-inventario.mjs';
const here=path.dirname(fileURLToPath(import.meta.url)),root=path.resolve(here,'../../../../..');
const readJSON=async p=>JSON.parse(await fs.readFile(p,'utf8'));
const rehearsal=await readJSON(path.join(here,'resultado-preparacao-r2.json'));
const approved=await readJSON(path.join(root,'auditoria/termodinamica/evidencias/BAN-07/preparacao-r2-definitiva/resultado-preparacao-r2.json'));
assert.deepEqual(rehearsal.arquivos_ensaio,approved.arquivos_ensaio,'Pacote diverge do material revisável');
assert.deepEqual(rehearsal.propostasJSON,approved.propostasJSON);
const stage=rehearsal.stage;const gethash=async f=>sha256(await fs.readFile(f));
const expected={
 'modulos/e1-termodinamica.html':'de614a44d796ca04268915f89f502060db2772835c072036a990802eff912b80',
 'auditoria/termodinamica/inventario/inventario-questoes.json':'7d35b07b31c7faa13eb3f98a8c73c3a9bd1c2cf146534464dfdd202e0074e4a7',
 'auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md':'dba046a5781f6bb82fef14b52af8f3285063c815b130f580edc817e9bd589fb1',
 'assets/curso.js':'a20f4d19158073a9a1c48aabdfba8fa863b02063e16061c00b16448a6ccc2e13',
 'assets/registro.js':'46da94527d6639fe0265bd766286f1ef39623966105e00bda3b31f21ca2c247c'};
for(const [f,h] of Object.entries(expected))assert.equal(await gethash(path.join(root,f)),h,'R1 divergente: '+f);
const proposal='auditoria/termodinamica/evidencias/BAN-07/propostas-r2';
for(const [f,h] of Object.entries(rehearsal.propostasJSON))assert.equal(await gethash(path.join(root,proposal,f)),h,'Proposta JSON divergente '+f);
const htmls={'AV04-candidata.html':'6ed8f664d46db759064d42ee073379bda2b8c1c7018ae3418d22774e14f72501','AV31-candidata.html':'2b2015e4ce0ec1bbea95c3da375ec316239d427f44454cfa43ca007c777fff7a','AV62-candidata.html':'795e127dad4361f30a6056f49479171b12c849388cdcdebde7fc09561be75ae7','CR06-candidata.html':'873e51481bc440721e17c233292535fdf7367670ba819c954987b7c263d8420b','CR26-candidata.html':'7c0ed44062bd50045076b2379e2449d24ef23da635ffe8a4d751ae37fb85303f','CR45-candidata-r2b.html':'3b7e1013014ca169f810aba4973e03c1b98a8972c5648289a996b523d63ff448'};
for(const [f,h] of Object.entries(htmls))assert.equal(await gethash(path.join(root,proposal,f)),h,'Proposta HTML divergente '+f);
const originalFon='auditoria/termodinamica/evidencias/FON-02/revisao-suplementos-80-r2.json',originalBan='auditoria/termodinamica/evidencias/BAN-10/triagem-r2.json';
assert.equal(await gethash(path.join(root,originalFon)),rehearsal.historicoFonHash);assert.equal(await gethash(path.join(root,originalBan)),rehearsal.historicoBan10Hash);
const existing=new Set(Object.keys(expected).slice(0,3));
for(const row of rehearsal.arquivos_ensaio){assert.equal(await gethash(path.join(stage,row.arquivo)),row.sha256,'Arquivo da cópia diverge: '+row.arquivo);if(!existing.has(row.arquivo)){try{await fs.access(path.join(root,row.arquivo));throw Error('Arquivo de destino já existe: '+row.arquivo)}catch(e){if(e.code!=='ENOENT')throw e}}}
const checkBefore=await validateInventory({rootDir:stage});assert.equal(checkBefore.ok,true,JSON.stringify(checkBefore.erros));
const backup=path.join(here,'antes-r2');try{await fs.access(backup);throw Error('Backup pré-existente; não sobrescrever')}catch(e){if(e.code!=='ENOENT')throw e}
for(const f of existing){const dest=path.join(backup,f);await fs.mkdir(path.dirname(dest),{recursive:true});await fs.copyFile(path.join(root,f),dest);assert.equal(await gethash(dest),expected[f]);}
const journal={estado:'EM_APLICACAO',origem_stage:stage,origem_preparacao:'auditoria/termodinamica/evidencias/BAN-07/preparacao-r2-definitiva/resultado-preparacao-r2.json',arquivos:rehearsal.arquivos_ensaio,backup:'auditoria/termodinamica/evidencias/BAN-07/aplicacao-r2/antes-r2',historicos:{fon02:rehearsal.historicoFonHash,ban10:rehearsal.historicoBan10Hash},controle_antes:await gethash(path.join(root,'auditoria/termodinamica/CONTROLE_AAA.json'))};
const journalPath=path.join(here,'diario-aplicacao-r2.json');await fs.writeFile(journalPath,JSON.stringify(journal,null,2)+'\n',{flag:'wx'});
const written=[];
try{
 for(const row of rehearsal.arquivos_ensaio){const target=path.join(root,row.arquivo),temp=target+'.ban07-r2-'+process.pid+'.tmp';await fs.mkdir(path.dirname(target),{recursive:true});await fs.copyFile(path.join(stage,row.arquivo),temp);assert.equal(await gethash(temp),row.sha256);await fs.rename(temp,target);written.push(row.arquivo);}
 for(const row of rehearsal.arquivos_ensaio)assert.equal(await gethash(path.join(root,row.arquivo)),row.sha256,'Falha ao confirmar arquivo aplicado '+row.arquivo);
 const checkAfter=await validateInventory({rootDir:root});assert.equal(checkAfter.ok,true,JSON.stringify(checkAfter.erros));
 assert.equal(await gethash(path.join(root,originalFon)),rehearsal.historicoFonHash);assert.equal(await gethash(path.join(root,originalBan)),rehearsal.historicoBan10Hash);
 assert.equal(await gethash(path.join(root,'assets/curso.js')),expected['assets/curso.js']);assert.equal(await gethash(path.join(root,'assets/registro.js')),expected['assets/registro.js']);
 const result={estado:'APLICADO_AGUARDANDO_AUDITORIA',aplicador:'Agente automatizado Corretor BAN-07',autorizacao:'Liberação explícita do coordenador para aplicação r2 dos seis ajustes e documentação estritamente afetada.',arquivos:rehearsal.arquivos_ensaio,backup:journal.backup,validacao_no_produto:checkAfter,persistencia_em_copia:rehearsal.persistencia,digitais:rehearsal.digitais,colisoes:rehearsal.colisoes,sincronizacaoInventario:rehearsal.sincronizacaoInventario,historicos:journal.historicos,controle_antes:journal.controle_antes,controle_depois:await gethash(path.join(root,'auditoria/termodinamica/CONTROLE_AAA.json')),limites:['Sem teste em navegador real, armazenamento pessoal, estudantes ou validação empírica.','Confronto FON-01 verifica identidade dos fragmentos oficiais, sem nova leitura dos PDFs nesta rodada.','Aceites anteriores não se transferem automaticamente; documento para auditoria independente, sem liberação do próximo ID.']};
 await fs.writeFile(path.join(here,'verificacao-aplicacao-r2.json'),JSON.stringify(result,null,2)+'\n',{flag:'wx'});journal.estado='APLICADO_AGUARDANDO_AUDITORIA';await fs.writeFile(journalPath,JSON.stringify(journal,null,2)+'\n');console.log(JSON.stringify({estado:result.estado,validacao:{ok:checkAfter.ok,itens:checkAfter.itens_registrados,artigos:checkAfter.artigos_encontrados,recursos:checkAfter.recursos_verificados,links:checkAfter.links_locais_verificados,erros:checkAfter.erros.length,avisos:checkAfter.avisos.length},arquivos:result.arquivos},null,2));
}catch(e){for(const f of written.reverse()){const target=path.join(root,f);if(existing.has(f))await fs.copyFile(path.join(backup,f),target);else await fs.rm(target,{force:true});}journal.estado='FALHA_COM_RESTAURACAO';journal.erro=String(e);await fs.writeFile(journalPath,JSON.stringify(journal,null,2)+'\n');throw e}
