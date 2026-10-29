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
const affected=['av-e1-04','av-e1-31','av-e1-62'];
const expectedProducts={
 'modulos/e1-termodinamica.html':'de614a44d796ca04268915f89f502060db2772835c072036a990802eff912b80',
 'auditoria/termodinamica/inventario/inventario-questoes.json':'7d35b07b31c7faa13eb3f98a8c73c3a9bd1c2cf146534464dfdd202e0074e4a7',
 'auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md':'dba046a5781f6bb82fef14b52af8f3285063c815b130f580edc817e9bd589fb1',
 'assets/curso.js':'a20f4d19158073a9a1c48aabdfba8fa863b02063e16061c00b16448a6ccc2e13',
 'assets/registro.js':'46da94527d6639fe0265bd766286f1ef39623966105e00bda3b31f21ca2c247c'};
const candidates={'av-e1-04':{file:'AV04-candidata.html',hash:'6ed8f664d46db759064d42ee073379bda2b8c1c7018ae3418d22774e14f72501',old:'25f60f37c5a530e2a2d19a9f0743d8941e83178ebb6663947566fd34f0bbfead',key:'D',digital:'8eaed3f8'},'av-e1-31':{file:'AV31-candidata.html',hash:'2b2015e4ce0ec1bbea95c3da375ec316239d427f44454cfa43ca007c777fff7a',old:'5ad8025f710d611c6b661937f00ff0ab4c9acc366056f9b12fa80fa81c7b8faf',key:'E',digital:'4538caee'},'av-e1-62':{file:'AV62-candidata.html',hash:'795e127dad4361f30a6056f49479171b12c849388cdcdebde7fc09561be75ae7',old:'3afa637b59ec0aa48e6885ab0877b0ed1bada0bcebe86c841d221e1559235148',key:'D',digital:'ed91f6ac'}};
const gethash=async p=>sha256(await fs.readFile(p));
for(const [p,expected] of Object.entries(expectedProducts))assert.equal(await gethash(path.join(root,p)),expected,'Produto r1 divergente: '+p);
const controlPath='auditoria/termodinamica/CONTROLE_AAA.json',controlHash=await gethash(path.join(root,controlPath));
const tmpBase=path.resolve(os.tmpdir());
const stage=await fs.mkdtemp(path.join(tmpBase,'ban07-r2-ensaio-'));
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
function avMap(doc){return doc.nodes.filter(n=>/^av-e1-\d+$/.test(n.attrs.id??'')).map(n=>({id:n.attrs.id,digital:digCtx.digitalDoBanco(adapter(doc,n)),chave:n.attrs['data-cr-gabarito']}))}
const map1=avMap(r1),map2=avMap(r2);assert.equal(map1.length,80);assert.deepEqual(map1.map(x=>x.id),map2.map(x=>x.id));
for(const id of affected){let a=map1.find(x=>x.id===id),b=map2.find(x=>x.id===id);assert.equal(a.digital,candidates[id].digital);assert.notEqual(a.digital,b.digital);assert.equal(a.chave,b.chave);}
assert.deepEqual(map1.filter((x,i)=>x.digital!==map2[i].digital).map(x=>x.id),affected);
for(const id of affected){const digital=map2.find(x=>x.id===id).digital;assert.equal(map2.filter(x=>x.digital===digital).length,1,'Colisão atual: '+id);assert.equal(map1.filter(x=>x.digital===digital).length,0,'Colisão com r1: '+id)}
const digitalResult=affected.map(id=>({id,antes:map1.find(x=>x.id===id).digital,depois:map2.find(x=>x.id===id).digital,chave:candidates[id].key}));
// Exercise the real AV storage functions with a controlled localStorage and minimum DOM.
const between=(a,b)=>{const i=source.indexOf(a),j=source.indexOf(b,i);assert.ok(i>=0&&j>i);return source.slice(i,j)};
const avCode=between('    function lerRespostas()','    function aplicarPendencias(')+between('    function aplicarPendencias(','    function atualizarRespostas(')+between('    function atualizarRespostas(','    try {\n      atualizarRespostas(lerRespostas());')+between('    function salvar(id, valor)','    function mostrarResposta(')+between('    function informarArmazenamento()','    function lerRespostas(');
class Store{constructor(){this.map=new Map()}getItem(k){return this.map.get(k)??null}setItem(k,v){this.map.set(k,String(v))}}
const store=new Store(),storeKey='sopmec:avalia:v2:e1';
const stable=map1.find(x=>!affected.includes(x.id)&&x.chave&&map2.find(y=>y.id===x.id).digital===x.digital);
function context(){const ctx={window:{localStorage:store},chave:storeKey,aviso:{textContent:''},gravacao:true,legado:false,tentativasAnteriores:false,respostas:{},pendencias:{},digitais:Object.fromEntries([...affected,stable.id].map(id=>[id,map2.find(x=>x.id===id).digital])),itens:[...affected,stable.id].map(id=>({id,querySelector:sel=>/input\[value="[A-E]"\]/.test(sel)?{}:null})),idModulo:()=> 'e1',mostrarResposta(){}};vm.createContext(ctx);vm.runInContext(avCode,ctx);return ctx}
const history=Object.fromEntries(digitalResult.map(x=>[x.antes,x.chave]));history[stable.digital]=stable.chave;store.setItem(storeKey,JSON.stringify({v:2,respostas:history}));
const ctx=context();ctx.atualizarRespostas(ctx.lerRespostas());for(const id of affected)assert.equal(ctx.respostas[id],undefined);assert.equal(ctx.respostas[stable.id],stable.chave);ctx.informarArmazenamento();assert.match(ctx.aviso.textContent,/versões anteriores preservadas/);
for(const d of digitalResult)ctx.salvar(d.id,d.chave);
const saved=JSON.parse(store.getItem(storeKey));for(const d of digitalResult){assert.equal(saved.respostas[d.antes],d.chave);assert.equal(saved.respostas[d.depois],d.chave)}
const reloaded=context();reloaded.atualizarRespostas(reloaded.lerRespostas());for(const d of digitalResult)assert.equal(reloaded.respostas[d.id],d.chave);assert.equal(reloaded.respostas[stable.id],stable.chave);reloaded.informarArmazenamento();assert.match(reloaded.aviso.textContent,/versões anteriores preservadas/);
const inventoryPath='auditoria/termodinamica/inventario/inventario-questoes.json';const inv=JSON.parse(await fs.readFile(pathIn(inventoryPath),'utf8'));const beforeInv=structuredClone(inv);const snapshot='auditoria/termodinamica/evidencias/BAN-07/e1-termodinamica.r2-ensaio.html';await fs.writeFile(pathIn(snapshot),html);
inv.fonte.sha256=sha256(html);inv.fonte.snapshot=snapshot;inv.metodo.descricao+=' BAN-07 r2 em ensaio isolado: AV04, AV31 e AV62 têm artigos revisados e novas digitais, com chaves preservadas; dependem de revisão independente e aplicação autorizada.';
for(const id of affected){const item=inv.itens.find(x=>x.id===id);assert.ok(item);const n=r2.ids.get(id)[0];item.localizacao.sha256_artigo=sha256(html.slice(n.start,n.end));}
for(let i=0;i<inv.itens.length;i++)if(!affected.includes(inv.itens[i].id))assert.deepEqual(inv.itens[i],beforeInv.itens[i]);
await fs.writeFile(pathIn(inventoryPath),JSON.stringify(inv,null,2)+'\n');
const markdown='auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md';let md=await fs.readFile(pathIn(markdown),'utf8');md+='\n## BAN-07 r2 — ensaio isolado da tríade\n\nAV04, AV31 e AV62 têm distratores e comentários substituídos, sem troca de chave; o ensaio é sujeito à auditoria independente e não aprova o banco. As digitais foram recalculadas e as tentativas antigas não foram migradas. A aplicação depende da conclusão do parecer r1 e de eventual liberação do coordenador.\n';await fs.writeFile(pathIn(markdown),md);
const validation=await validateInventory({rootDir:stage});assert.equal(validation.ok,true,JSON.stringify(validation.erros.slice(0,10)));
for(const [p,expected] of Object.entries(expectedProducts))assert.equal(await gethash(path.join(root,p)),expected,'Produto alterado durante ensaio: '+p);
assert.equal(await gethash(path.join(root,controlPath)),controlHash);
const output={id:'BAN-07',estado:'ENSAIO_ISOLADO_NAO_APLICADO_NAO_APROVADO',stage,produto_r1_preservado:true,controle_sha256:controlHash,escopo:affected,html_sha256:sha256(html),snapshot,artigos_alterados:deltas,fora_dos_artigos_identico:true,digitais:digitalResult,colisoes:'Cada nova digital é única entre os 80 AV atuais e não existe nas 80 digitais r1; não cobre outros navegadores nem históricos desconhecidos.',persistencia:{metodo:'Funções reais AV em Node/VM com DOM e localStorage simulados; respostas r1 e um item inalterado, novas respostas e recarga de contexto.',historico_antigo_preservado:true,anteriores_nao_preenchem_versoes_novas:true,item_inalterado_preservado:true,aviso:true,novas_respostas_persistem_na_recarga:true,limite:'Sem navegador real, sem armazenamento pessoal, sem teste de placar ou falhas de escrita.'},inventario:validation,arquivos_ensaio:await Promise.all(['modulos/e1-termodinamica.html',inventoryPath,markdown,snapshot].map(async arquivo=>({arquivo,sha256:await gethash(pathIn(arquivo))}))),limites:['Apenas três candidatas; AV69 não aplicada.','Estágio provisório: CR06/26 e outros achados ainda podem acrescentar obrigações.','Não é aprovação independente, aplicação ao produto nem parecer integral BAN-07.','O diretório temporário permanece para inspeção; não contém armazenamento do usuário.']};
const report=path.join(here,'resultado-ensaio-r2-triade.json');await fs.writeFile(report,JSON.stringify(output,null,2)+'\n');console.log(JSON.stringify({stage,html_sha256:output.html_sha256,digitais:digitalResult,validacao:{ok:validation.ok,itens:validation.itens_registrados,artigos:validation.artigos_encontrados,recursos:validation.recursos_verificados,links:validation.links_locais_verificados,erros:validation.erros.length,avisos:validation.avisos.length},resultado:report},null,2));
