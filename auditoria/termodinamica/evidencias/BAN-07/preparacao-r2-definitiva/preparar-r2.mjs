import fs from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import vm from 'node:vm';
import assert from 'node:assert/strict';
import { fileURLToPath } from 'node:url';
import {parseHtml,isInventoryArticle,decodeHtml,sha256,validateInventory} from '../../../inventario/validar-inventario.mjs';

const here=path.dirname(fileURLToPath(import.meta.url));
const root=path.resolve(here,'../../../../..');
const proposalDir=path.join(root,'auditoria/termodinamica/evidencias/BAN-07/propostas-r2');
const affected=['cr-e1-06','cr-e1-26','cr-e1-45','av-e1-04','av-e1-31','av-e1-62'];
const expectedProducts={
 'modulos/e1-termodinamica.html':'de614a44d796ca04268915f89f502060db2772835c072036a990802eff912b80',
 'auditoria/termodinamica/inventario/inventario-questoes.json':'7d35b07b31c7faa13eb3f98a8c73c3a9bd1c2cf146534464dfdd202e0074e4a7',
 'auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md':'dba046a5781f6bb82fef14b52af8f3285063c815b130f580edc817e9bd589fb1',
 'assets/curso.js':'a20f4d19158073a9a1c48aabdfba8fa863b02063e16061c00b16448a6ccc2e13',
 'assets/registro.js':'46da94527d6639fe0265bd766286f1ef39623966105e00bda3b31f21ca2c247c'};
const candidates={'av-e1-04':{file:'AV04-candidata.html',hash:'6ed8f664d46db759064d42ee073379bda2b8c1c7018ae3418d22774e14f72501',old:'25f60f37c5a530e2a2d19a9f0743d8941e83178ebb6663947566fd34f0bbfead',key:'D',digital:'8eaed3f8'},'av-e1-31':{file:'AV31-candidata.html',hash:'2b2015e4ce0ec1bbea95c3da375ec316239d427f44454cfa43ca007c777fff7a',old:'5ad8025f710d611c6b661937f00ff0ab4c9acc366056f9b12fa80fa81c7b8faf',key:'E',digital:'4538caee'},'av-e1-62':{file:'AV62-candidata.html',hash:'795e127dad4361f30a6056f49479171b12c849388cdcdebde7fc09561be75ae7',old:'3afa637b59ec0aa48e6885ab0877b0ed1bada0bcebe86c841d221e1559235148',key:'D',digital:'ed91f6ac'}};
Object.assign(candidates, {
 'cr-e1-06':{file:'CR06-candidata.html',hash:'873e51481bc440721e17c233292535fdf7367670ba819c954987b7c263d8420b',old:'69c0e38652f6be60ce26064942c5df1ef936193d8f6c3b79bd6530c28e29f31e',key:'C',digital:'01aa3697'},
 'cr-e1-26':{file:'CR26-candidata.html',hash:'7c0ed44062bd50045076b2379e2449d24ef23da635ffe8a4d751ae37fb85303f',old:'4799e28ca9e9aa74d19aa5bac1560323e7d4d71e74a98e63561068afb3b802c8',key:'E',digital:'988714ce'},
 'cr-e1-45':{file:'CR45-candidata-r2b.html',hash:'3b7e1013014ca169f810aba4973e03c1b98a8972c5648289a996b523d63ff448',old:'382306e2bd0381e3614cfefd799d12a1b90a06b3b78e1f2171bc5c9c67c4ba4d',key:'C',digital:'c084d78c'}
});
const propostasJSON={
 'AV04-candidata.json':'973c4c2b82c8ae97ed4f8a784399df44d9cf3f75d80e303943844f368777b05f',
 'AV31-candidata.json':'51dcf6eeba809fdf5294ddc0b86e5d048424697041930b1fe37b5c6a706e96c1',
 'AV62-candidata.json':'4c8604d81bf884e5459d26f006c051451357d31a6085b96c8d80724345e0f0bc',
 'CR06-candidata.json':'78e6688c12a1371dd4e7144ff1098fd590106c430768d43563380213064cd615',
 'CR26-candidata.json':'e4d168b3c018caf97f4b4f57b0db4478136a2f852544653244480bb3c0951907',
 'CR45-candidata-r2b.json':'5257957efbb70f493f943634bf6d130bd0cbc5b7a9cc3d264b52a7dfbe70e4ad'
};
const gethash=async p=>sha256(await fs.readFile(p));
for(const [f,h] of Object.entries(propostasJSON))assert.equal(await gethash(path.join(proposalDir,f)),h,'JSON candidato divergente: '+f);
for(const [p,expected] of Object.entries(expectedProducts))assert.equal(await gethash(path.join(root,p)),expected,'Produto r1 divergente: '+p);
const controlPath='auditoria/termodinamica/CONTROLE_AAA.json',controlHash=await gethash(path.join(root,controlPath));
const historicoFonPath='auditoria/termodinamica/evidencias/FON-02/revisao-suplementos-80-r2.json', historicoFonHash=await gethash(path.join(root,historicoFonPath));
const historicoBan10Path='auditoria/termodinamica/evidencias/BAN-10/triagem-r2.json',historicoBan10Hash=await gethash(path.join(root,historicoBan10Path));
const tmpBase=path.resolve(os.tmpdir());
const stage=await fs.mkdtemp(path.join(tmpBase,'ban07-r2-preparacao-'));
assert.notEqual(stage,root); assert.ok(stage.startsWith(tmpBase+path.sep));
for(const d of ['assets','auditoria','downloads','formulas','modulos'])await fs.cp(path.join(root,d),path.join(stage,d),{recursive:true});
for(const f of ['index.html','README.md','PUBLICACAO.json','.nojekyll'])await fs.copyFile(path.join(root,f),path.join(stage,f));
const pathIn=p=>path.join(stage,p);
const oldHtml=await fs.readFile(pathIn('modulos/e1-termodinamica.html'),'utf8');
let html=oldHtml;
for(const id of affected){
 const d=parseHtml(html), matches=d.ids.get(id);assert.equal(matches?.length,1,id);
 const n=matches[0];assert.equal(n.tag,'article');assert.equal(n.attrs['data-cr-gabarito'],candidates[id].key);
 const old=html.slice(n.start,n.end);assert.equal(sha256(old),candidates[id].old);
 const replacement=await fs.readFile(path.join(proposalDir,candidates[id].file),'utf8');assert.equal(sha256(replacement),candidates[id].hash);
 const parsed=parseHtml(replacement);assert.equal(parsed.errors.length,0);assert.equal(parsed.ids.get(id)?.length,1);assert.equal(parsed.ids.get(id)[0].attrs['data-cr-gabarito'],candidates[id].key);
 if(id.startsWith('cr-')) { const notes=parsed.nodes.filter(x=>x.tag==='p'&&(x.attrs.class??'').split(/\s+/).includes('cr-suplemento'));assert.equal(notes.length,1);const note=notes[0];assert.equal(note.parent?.attrs.id,id+'-enunciado');assert.equal(replacement.replace(replacement.slice(note.start,note.end),''),old,'Transcrição/figura/chave oficial mudou: '+id); }

 html=html.slice(0,n.start)+replacement+html.slice(n.end);
}
await fs.writeFile(pathIn('modulos/e1-termodinamica.html'),html);
const r1=parseHtml(oldHtml),r2=parseHtml(html);
const ids1=r1.nodes.filter(isInventoryArticle).map(n=>n.attrs.id),ids2=r2.nodes.filter(isInventoryArticle).map(n=>n.attrs.id);
assert.deepEqual(ids1,ids2);const deltas=[];
for(const id of ids1){const a=r1.ids.get(id)[0],b=r2.ids.get(id)[0];if(sha256(oldHtml.slice(a.start,a.end))!==sha256(html.slice(b.start,b.end)))deltas.push(id);}
assert.deepEqual([...deltas].sort(),[...affected].sort());
const beforeOutside=ids1.reduce((s,id)=>{const n=r1.ids.get(id)[0];return s.replace(oldHtml.slice(n.start,n.end),'[ARTICLE:'+id+']')},oldHtml);
const afterOutside=ids2.reduce((s,id)=>{const n=r2.ids.get(id)[0];return s.replace(html.slice(n.start,n.end),'[ARTICLE:'+id+']')},html);
assert.equal(beforeOutside,afterOutside);
const source=await fs.readFile(pathIn('assets/curso.js'),'utf8');
const fn=(name,next)=>source.slice(source.indexOf('  function '+name+'('),source.indexOf('  function '+next+'('));
const digCtx={Array,String,Math};vm.createContext(digCtx);vm.runInContext("var SEPARADOR='␞';\n"+fn('paraArray','criar')+fn('normalizarDigital','formatarTempo')+fn('digitalDoBanco','iniciarBanco'),digCtx);
function adapter(doc,node){const cache=new Map();function match(n,selector){if(selector.startsWith('.'))return(n.attrs.class??'').split(/\s+/).includes(selector.slice(1));if(selector==='input[type="radio"]')return n.tag==='input'&&n.attrs.type==='radio';return n.tag===selector}function wrap(n){if(cache.has(n))return cache.get(n);const out={nodeType:1,localName:n.tag,tagName:n.tag.toUpperCase(),hasAttribute:k=>k in n.attrs,getAttribute:k=>n.attrs[k]??null,value:n.attrs.value,id:n.attrs.id,dataset:{crGabarito:n.attrs['data-cr-gabarito']},childNodes:[],querySelectorAll:s=>doc.nodes.filter(v=>v!==n&&v.start>=n.start&&v.end<=n.end&&match(v,s)).map(wrap),querySelector:s=>out.querySelectorAll(s)[0]??null,closest:s=>{let p=n;while(p){if(match(p,s))return wrap(p);p=p.parent}return null}};cache.set(n,out);const close=doc.html.lastIndexOf('</',n.end-1),end=close>=n.openEnd?close:n.openEnd;let at=n.openEnd;for(const child of n.children){if(child.start>at)out.childNodes.push({nodeType:3,nodeValue:decodeHtml(doc.html.slice(at,child.start))});out.childNodes.push(wrap(child));at=child.end}if(end>at)out.childNodes.push({nodeType:3,nodeValue:decodeHtml(doc.html.slice(at,end))});return out}return wrap(node)}
function bankMap(doc,prefix){return doc.nodes.filter(n=>new RegExp('^'+prefix+'-e1-\\d+$').test(n.attrs.id??'')).map(n=>({id:n.attrs.id,digital:digCtx.digitalDoBanco(adapter(doc,n)),chave:n.attrs['data-cr-gabarito']}))}
const maps={};let digitalResult=[];
for(const prefix of ['av','cr']){
 const before=bankMap(r1,prefix),after=bankMap(r2,prefix),targets=affected.filter(x=>x.startsWith(prefix+'-'));assert.equal(before.length,80);assert.deepEqual(before.map(x=>x.id),after.map(x=>x.id));
 assert.deepEqual(before.filter((x,i)=>x.digital!==after[i].digital).map(x=>x.id),targets);
 for(const id of targets){const a=before.find(x=>x.id===id),b=after.find(x=>x.id===id);assert.equal(a.digital,candidates[id].digital);assert.notEqual(a.digital,b.digital);assert.equal(a.chave,b.chave);assert.equal(after.filter(x=>x.digital===b.digital).length,1);assert.equal(before.filter(x=>x.digital===b.digital).length,0);digitalResult.push({id,antes:a.digital,depois:b.digital,chave:a.chave});}
 maps[prefix]={before,after,targets};
}
// Funções reais dos dois bancos, com armazenamento e DOM mínimos simulados.
const between=(a,b)=>{const i=source.indexOf(a),j=source.indexOf(b,i);assert.ok(i>=0&&j>i);return source.slice(i,j)};
const filterCode=between('    function filtrar()', '\n    itens.forEach(function (item) {\n      // Não pesquisa');
const bankCode=between('    function lerRespostas()','    function aplicarPendencias(')+between('    function aplicarPendencias(','    function atualizarRespostas(')+between('    function atualizarRespostas(','    try {\n      atualizarRespostas(lerRespostas());')+between('    function salvar(id, valor)','    function mostrarResposta(')+between('    function informarArmazenamento()','    function lerRespostas(');
class Store{constructor(){this.map=new Map()}getItem(k){return this.map.get(k)??null}setItem(k,v){this.map.set(k,String(v))}}
for(const prefix of ['av','cr']){
 const {before,after,targets}=maps[prefix],store=new Store(),storeKey='sopmec:'+(prefix==='av'?'avalia':'concursos')+':v2:e1';
 const stable=before.find(x=>!targets.includes(x.id)&&x.chave&&after.find(y=>y.id===x.id).digital===x.digital);
 const critical=prefix==='cr'?after.find(x=>r2.ids.get(x.id)[0].attrs['data-cr-avaliacao']==='estudo-critico'):null;
 const ids=[...targets,stable.id,...(critical?[critical.id]:[])];
 function context(){const ctx={window:{localStorage:store},chave:storeKey,aviso:{textContent:''},gravacao:true,legado:false,tentativasAnteriores:false,respostas:{},pendencias:{},digitais:Object.fromEntries(ids.map(id=>[id,after.find(x=>x.id===id).digital])),itens:ids.map(id=>({id,dataset:{crGabarito:after.find(x=>x.id===id).chave,crAvaliacao:critical?.id===id?'estudo-critico':'',crBusca:''},querySelector:sel=>/input\[value="[A-E]"\]/.test(sel)?{}:null})),idModulo:()=> 'e1',mostrarResposta(){},normalizarBusca:t=>t.toLowerCase(),busca:{value:''},assunto:{value:''},banca:{value:''},pendentes:{checked:false},lotes:[],placar:{textContent:''},temEstudosCriticos:!!critical,banco:{querySelector:()=>({hidden:true})},prefixo:prefix,estudoCritico:item=>item.dataset.crAvaliacao==='estudo-critico',pluralizar:(n,s,p)=>n+' '+(n===1?s:p)};vm.createContext(ctx);vm.runInContext(bankCode+filterCode,ctx);return ctx}
 const rows=digitalResult.filter(x=>targets.includes(x.id)),history=Object.fromEntries(rows.map(x=>[x.antes,x.chave]));history[stable.digital]=stable.chave;if(critical)history[critical.digital]=critical.chave;store.setItem(storeKey,JSON.stringify({v:2,respostas:history}));
 const ctx=context();ctx.atualizarRespostas(ctx.lerRespostas());for(const id of targets)assert.equal(ctx.respostas[id],undefined);assert.equal(ctx.respostas[stable.id],stable.chave);ctx.filtrar();if(critical)assert.match(ctx.placar.textContent,/Treino pontuável: 1 de 4 respondidas, 1 correta e 0 incorretas.*Estudos críticos: 1 de 1/);else assert.match(ctx.placar.textContent,/1 respondida no banco · 1 correta/);ctx.informarArmazenamento();assert.match(ctx.aviso.textContent,/versões anteriores preservadas/);
 for(const row of rows)ctx.salvar(row.id,row.chave);const saved=JSON.parse(store.getItem(storeKey));for(const row of rows){assert.equal(saved.respostas[row.antes],row.chave);assert.equal(saved.respostas[row.depois],row.chave)}
 const reload=context();reload.atualizarRespostas(reload.lerRespostas());for(const row of rows)assert.equal(reload.respostas[row.id],row.chave);assert.equal(reload.respostas[stable.id],stable.chave);reload.filtrar();if(critical)assert.match(reload.placar.textContent,/Treino pontuável: 4 de 4 respondidas, 4 corretas e 0 incorretas.*Estudos críticos: 1 de 1/);else assert.match(reload.placar.textContent,/4 respondidas no banco · 4 corretas/);reload.informarArmazenamento();assert.match(reload.aviso.textContent,/versões anteriores preservadas/);
}
const inventoryPath='auditoria/termodinamica/inventario/inventario-questoes.json';const inv=JSON.parse(await fs.readFile(pathIn(inventoryPath),'utf8'));const beforeInv=structuredClone(inv);const snapshot='auditoria/termodinamica/evidencias/BAN-07/e1-termodinamica.r2.html';await fs.writeFile(pathIn(snapshot),html);
inv.fonte.sha256=sha256(html);inv.fonte.snapshot=snapshot;inv.metodo.descricao+=' BAN-07 r2 submetido à auditoria: AV04, AV31, AV62, CR06, CR26 e CR45 têm artigos e digitais revisados; as três hipóteses CR são editoriais, não texto oficial, e dependem de auditoria independente e aplicação autorizada.';
for(const id of affected){const item=inv.itens.find(x=>x.id===id);assert.ok(item);const n=r2.ids.get(id)[0];item.localizacao.sha256_artigo=sha256(html.slice(n.start,n.end));}
const editoriais={
 'cr-e1-06':{texto:'Editorial do curso: ambas as escalas são lineares na altura da coluna e variam com ela.',remover:['Escalas lineares sobre a mesma propriedade termométrica']},
 'cr-e1-26':{texto:'Editorial do curso: sistema fechado; sem outras trocas além das indicadas, variações cinética/potencial desprezíveis e quilocaloria termoquímica 1 kcal = 4,184 kJ.',remover:['Sistema sem troca de massa','Variações cinética e potencial desprezíveis','1 kcal aproximadamente 4,184 kJ']},
 'cr-e1-45':{texto:'Editorial do curso: ciclo fechado com apenas dois reservatórios e trabalho líquido; os 900 e 90 kJ referem-se ao mesmo ciclo.',remover:['Apenas duas fontes térmicas e trabalho como interações do modelo']}
};
for(const [id,data] of Object.entries(editoriais)){const r=inv.itens.find(x=>x.id===id);r.hipoteses.explicitadas.push(data.texto);r.hipoteses.implicitas=r.hipoteses.implicitas.filter(x=>!data.remover.includes(x));if(id==='cr-e1-06')r.nivel.justificativa='A hipótese linear é explicitada em suplemento editorial do curso; basta reconhecer TX=a+bTY no modelo delimitado.';}
for(let i=0;i<inv.itens.length;i++)if(!affected.includes(inv.itens[i].id))assert.deepEqual(inv.itens[i],beforeInv.itens[i]);
await fs.writeFile(pathIn(inventoryPath),JSON.stringify(inv,null,2)+'\n');
const markdown='auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md';let md=await fs.readFile(pathIn(markdown),'utf8');md+='\n## BAN-07 r2 — versão submetida à auditoria\n\nAV04, AV31 e AV62 têm distratores e comentários substituídos; CR06, CR26 e CR45 recebem hipóteses editoriais antes da resposta, sem alterar texto ou chave oficiais; a versão é sujeita à auditoria independente e não aprova o banco. As digitais foram recalculadas e as tentativas antigas não foram migradas. A aplicação depende da conclusão do parecer r1 e de eventual liberação do coordenador.\n';const anterior='A hipótese linear já é dada e basta reconhecer TX=a+bTY.';
const revisada=inv.itens.find(x=>x.id==='cr-e1-06').nivel.justificativa;
assert.equal(md.split(anterior).length,2,'Linha histórica CR06 ausente ou duplicada');md=md.replace(anterior,revisada);
const sincronizacaoInventario=[];
for(const id of affected){
 const r=inv.itens.find(x=>x.id===id);const linha=md.split(/\r?\n/).filter(x=>x.includes('#'+id+')'));
 assert.equal(linha.length,1,'Linha ausente ou duplicada: '+id);
 const celulas=linha[0].split('|').map(x=>x.trim()).filter(Boolean);
 assert.equal(celulas.length,5,'Formato da linha: '+id);
 assert.equal(celulas[1],r.competencias.join(', '),'Competências divergentes: '+id);
 assert.equal(celulas[2],r.nivel.estimado,'Nível divergente: '+id);
 assert.equal(Number(celulas[3]),r.raciocinio.numero_etapas,'Etapas divergentes: '+id);
 assert.equal(celulas[4],r.nivel.justificativa,'Justificativa divergente: '+id);
 sincronizacaoInventario.push({id,competencias:celulas[1],nivel:celulas[2],etapas:Number(celulas[3]),justificativa:celulas[4],sincronizado:true});
}
md+='\nAs análises complementares de [suplementos FON-02](../evidencias/BAN-07/revisao-fon02-complementar-r2.json), [triagem BAN-10](../evidencias/BAN-07/triagem-ban10-complementar-r2.json) e [identidade documental FON-01](../evidencias/BAN-07/confronto-fon01-cr-r2.json) são provisórias e preservam os registros históricos.\n';await fs.writeFile(pathIn(markdown),md);
const fonPath='auditoria/termodinamica/evidencias/FON-02/revisao-suplementos-80-r2.json',fonBytes=await fs.readFile(pathIn(fonPath)),fon=JSON.parse(fonBytes.toString('utf8')),origFon=structuredClone(fon);
const fonExtra='auditoria/termodinamica/evidencias/BAN-07/revisao-fon02-complementar-r2.json';
fon.estado='COMPLEMENTO_BAN07_R2_SUBMETIDO_A_AUDITORIA';fon.fonte_reexaminada_BAN07={arquivo:'modulos/e1-termodinamica.html',sha256:sha256(html),snapshot};fon.complemento_BAN07={natureza:'Nova cópia complementar r2 submetida à auditoria; o relatório FON-02 r2 de origem permanece inalterado. Sem reaprovar FON-02.',fonte_anterior:fonPath,sha256_anterior:sha256(fonBytes),novos_suplementos:['cr-e1-06','cr-e1-26','cr-e1-45'],autoria:'Corretor automatizado; sujeito a revisão independente'};
for(const id of ['cr-e1-06','cr-e1-26','cr-e1-45']){const r=fon.registros.find(x=>x.id===id),n=r2.ids.get(id)[0],a=html.slice(n.start,n.end),parsed=parseHtml(a),note=parsed.nodes.find(x=>x.tag==='p'&&(x.attrs.class??'').split(/\s+/).includes('cr-suplemento'));r.suplemento_BAN07_r2={tipo:'hipotese_editorial_nao_oficial',posicao:'dentro do contêiner enunciado, depois do texto e figura oficiais e antes da marcação',html:a.slice(note.start,note.end),sha256_artigo:sha256(a),chave:candidates[id].key,criterio:'Suficiência da leitura declarada; não atribuir hipótese à banca; aprovação de FON-02 anterior não é transferida automaticamente.'};}
for(let i=0;i<fon.registros.length;i++)if(!['cr-e1-06','cr-e1-26','cr-e1-45'].includes(fon.registros[i].id))assert.deepEqual(fon.registros[i],origFon.registros[i]);
await fs.writeFile(pathIn(fonExtra),JSON.stringify(fon,null,2)+'\n');assert.equal(await gethash(pathIn(fonPath)),sha256(fonBytes));
// Extensão da triagem histórica: reavalia apenas os três itens; preserva o relatório r2.
const banBytes=await fs.readFile(pathIn(historicoBan10Path)),triagem=JSON.parse(banBytes.toString('utf8')),triagemAntes=structuredClone(triagem);
const banExtra='auditoria/termodinamica/evidencias/BAN-07/triagem-ban10-complementar-r2.json';
triagem.tipo='TRIAGEM_BAN10_COMPLEMENTADA_POR_BAN07_R2_SUBMETIDA_A_AUDITORIA';
triagem.reavaliacao_BAN07={natureza:'Releitura apenas CR06, CR26 e CR45; demais 194 classificações preservam autoria e versão anterior. Não é novo aceite BAN-10.',fonte_historica:historicoBan10Path,sha256_historico:sha256(banBytes),fonte_atual:'modulos/e1-termodinamica.html',sha256_fonte_atual:sha256(html),estado:'AGUARDA_AUDITORIA'};
triagem.classificacoes.modelo_editorial_explicito_sujeito_auditoria='O original é insuficiente para uma resposta técnica única; o curso acrescenta antes da tentativa uma hipótese editorial identificada. Permanência em pontuação sujeita a revisão independente da versão aplicada.';
for(const id of ['cr-e1-06','cr-e1-26','cr-e1-45']){const r=triagem.itens.find(x=>x.id===id),node=r2.ids.get(id)[0];r.historico_pre_BAN07={situacao:r.situacao,motivo:r.motivo,sha256_artigo_lido:r.sha256_artigo_lido};r.situacao='modelo_editorial_explicito_sujeito_auditoria';r.motivo=editoriais[id].texto+' A insuficiência do original e alternativas de estudo crítico foram adjudicadas; o modelo suplementado preserva chave documental e sua pontuação requer exame independente.';r.sha256_artigo_lido=sha256(html.slice(node.start,node.end));r.uso_proposto='pontuavel_no_modelo_editorial_sem_alterar_marcador_r1_sujeito_auditoria';}
const counts={};for(const r of triagem.itens)counts[r.situacao]=(counts[r.situacao]??0)+1;triagem.cobertura.contagem_situacoes=counts;triagem.cobertura.releitura_nesta_extensao=3;
for(let i=0;i<triagem.itens.length;i++)if(!['cr-e1-06','cr-e1-26','cr-e1-45'].includes(triagem.itens[i].id))assert.deepEqual(triagem.itens[i],triagemAntes.itens[i]);
await fs.writeFile(pathIn(banExtra),JSON.stringify(triagem,null,2)+'\n');assert.equal(await gethash(pathIn(historicoBan10Path)),sha256(banBytes));
const fon1Extra='auditoria/termodinamica/evidencias/BAN-07/confronto-fon01-cr-r2.json';
const fon1={estado:'CONFRONTO_DE_IDENTIDADE_NAO_REVALIDACAO_DOCUMENTAL',fonte_fon01:'auditoria/termodinamica/evidencias/FON-01/conferencia-80-r1.json',sha256_fonte_fon01:await gethash(pathIn('auditoria/termodinamica/evidencias/FON-01/conferencia-80-r1.json')),criterio:'Nos três fragmentos, remover somente parágrafo editorial recupera o artigo r1 byte a byte, inclusive transcrição, figuras, alternativas e chaves. Não houve nova leitura dos PDFs nem declaração de aceite FON-01 para r2.',registros:['cr-e1-06','cr-e1-26','cr-e1-45'].map(id=>({id,sha256_antes:candidates[id].old,sha256_candidata:candidates[id].hash,remocao_editorial_reconstroi_r1:true}))};await fs.writeFile(pathIn(fon1Extra),JSON.stringify(fon1,null,2)+'\n');
const validation=await validateInventory({rootDir:stage});assert.equal(validation.ok,true,JSON.stringify(validation.erros.slice(0,10)));
for(const [p,expected] of Object.entries(expectedProducts))assert.equal(await gethash(path.join(root,p)),expected,'Produto alterado durante ensaio: '+p);
assert.equal(await gethash(path.join(root,controlPath)),controlHash);assert.equal(await gethash(path.join(root,historicoFonPath)),historicoFonHash);assert.equal(await gethash(path.join(root,historicoBan10Path)),historicoBan10Hash);
const decisionPath='auditoria/termodinamica/pareceres/BAN-07-decisao-candidata-cr45-r2.md';const decisaoCR45={arquivo:decisionPath,sha256:await gethash(path.join(root,decisionPath)),limite:'A adjudicação confirmou o ajuste; parecer independente aprovou a variante r2b isolada, sem aprovar o pacote integrado.'};
const output={decisaoCR45,historicoFonHash,historicoBan10Hash,propostasJSON,sincronizacaoInventario,id:'BAN-07',estado:'PACOTE_R2_PREPARADO_EM_COPIA_NAO_APLICADO_NAO_APROVADO',stage,produto_r1_preservado:true,controle_sha256:controlHash,escopo:affected,html_sha256:sha256(html),snapshot,artigos_alterados:deltas,fora_dos_artigos_identico:true,digitais:digitalResult,colisoes:'Cada digital nova é única nos 80 itens atuais do seu banco e não existe nas 80 digitais r1 do mesmo banco; históricos desconhecidos não foram examinados.',persistencia:{metodo:'Funções reais dos bancos AV e CR em Node/VM com DOM e localStorage simulados; respostas r1 e item inalterado em cada banco, novas respostas e recarga de contexto.',historico_antigo_preservado:true,anteriores_nao_preenchem_versoes_novas:true,item_inalterado_preservado:true,aviso:true,novas_respostas_persistem_na_recarga:true,placar_funcao_real_em_vm:true,estudo_critico_excluido_do_placar_em_vm:true,limite:'Sem navegador real, sem armazenamento pessoal ou teste de falhas de escrita.'},inventario:validation,arquivos_ensaio:await Promise.all(['modulos/e1-termodinamica.html',inventoryPath,markdown,snapshot,fonExtra,banExtra,fon1Extra].map(async arquivo=>({arquivo,sha256:await gethash(pathIn(arquivo))}))),limites:['Seis candidatas; AV69 não aplicada. CR45-r2b possui aprovação isolada; o conjunto aguarda revisão independente.','Se qualquer proposta for alterada ou rejeitada, refazer o ensaio combinado e as evidências.','Não é aprovação independente, aplicação ao produto nem parecer integral BAN-07.','O diretório temporário permanece para inspeção; não contém armazenamento do usuário.']};
const report=path.join(here,'resultado-preparacao-r2.json');await fs.writeFile(report,JSON.stringify(output,null,2)+'\n');console.log(JSON.stringify({stage,html_sha256:output.html_sha256,digitais:digitalResult,validacao:{ok:validation.ok,itens:validation.itens_registrados,artigos:validation.artigos_encontrados,recursos:validation.recursos_verificados,links:validation.links_locais_verificados,erros:validation.erros.length,avisos:validation.avisos.length},resultado:report},null,2));
