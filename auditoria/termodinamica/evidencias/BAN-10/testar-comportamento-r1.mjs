/** Executa iniciarBanco real em DOM/armazenamento controlados; não substitui navegador. */
import fs from 'node:fs/promises';
import vm from 'node:vm';
import {fileURLToPath} from 'node:url';
const root=fileURLToPath(new URL('../../../../',import.meta.url));
function element(extra={}) { return Object.assign({value:'',checked:false,hidden:false,disabled:false,textContent:'',events:{},addEventListener(k,f){this.events[k]=f;},focus(){this.focused=true;}},extra); }
function fixture(id,key,critical,digital) {
  const fields={}; for(const s of ['fieldset','.cr-feedback','.cr-acoes','.cr-resolucao','[data-cr-acao="corrigir"]','[data-cr-acao="refazer"]','.cr-meta','h3','.cr-assunto','.cr-enunciado','.cr-alternativas'])fields[s]=element({textContent:id});
  const radios=['C','E'].map(value=>element({value}));
  const item=element({id,digital,dataset:{crGabarito:key,crAvaliacao:critical?'estudo-critico':undefined,crAssunto:'gases',crBanca:'Cebraspe'},fields,radios,
    querySelector(s){if(s==='input:checked')return radios.find(x=>x.checked)||null;if(s==='input')return radios[0];if(s.startsWith('input[value='))return radios.find(x=>x.value===s.match(/"(.*?)"/)[1])||null;return fields[s]||null;},
    querySelectorAll(s){return s==='input[type="radio"]'?radios:[];},removeAttribute(s){if(s==='data-cr-resultado')delete this.dataset.crResultado;},closest(){return this;}});
  return item;
}
function setup(source,{modulo='e1',stored={},storageError=false,allCritical=false,marked=true}={}) {
  const items=[fixture('critico','E',marked,'11111111'),fixture('regular','C',allCritical,'22222222')], controls={};
  for(const name of ['assunto','banca','busca','pendentes','placar','armazenamento','vazio'])controls[name]=element();
  const lot=element({querySelector(){return items.find(x=>!x.hidden)||null;}}),visibleControls=element();
  const bank={querySelector(s){if(s==='.cr-lote')return lot;if(s==='.cr-controles')return visibleControls;return controls[s.replace('#cr-','')]||null;},querySelectorAll(s){if(s==='.concurso-item, .avalia-item')return items;if(s==='.cr-lote')return[lot];return[];},contains(i){return items.includes(i);}};
  const key='sopmec:concursos:v2:'+modulo,store=new Map([[key,JSON.stringify({v:2,respostas:stored})]]),events={};
  const window={localStorage:{getItem(k){if(storageError)throw Error('indisponível');return store.get(k)??null;},setItem(k,v){if(storageError)throw Error('indisponível');store.set(k,v);}},addEventListener(k,f){events[k]=f;}};
  const ctx={document:{getElementById(){return bank;}},window,idModulo:()=>modulo,digitalDoBanco:i=>i.digital,pluralizar:(n,a,b)=>n+' '+(n===1?a:b),reveladoresBanco:{},Array,Object,JSON};
  vm.createContext(ctx); vm.runInContext(source+'\niniciarBanco("questoes-reais","cr",'+JSON.stringify(key)+');',ctx);
  const answer=(index,value)=>{items[index].radios.forEach(r=>r.checked=r.value===value);items[index].fields['[data-cr-acao="corrigir"]'].events.click();};
  const redo=index=>items[index].fields['[data-cr-acao="refazer"]'].events.click();
  return {items,controls,store,key,events,ctx,answer,redo,lot};
}
export async function testarComportamento(){
  const js=await fs.readFile(root+'assets/curso.js','utf8'),start=js.indexOf('  function iniciarBanco(secao,'),end=js.indexOf('  function iniciarQuestoes()',start),source=js.slice(start,end);
  const checks=[],check=(nome,ok)=>{checks.push({nome,ok});if(!ok)throw Error(nome);};
  let f=setup(source);check('sem resposta: denominador exclui crítico',f.controls.placar.textContent.includes('Treino pontuável: 0 de 1 respondidas')&&f.controls.placar.textContent.includes('0 de 1 com marcação documental'));
  f.answer(0,'E');check('concordância crítica não vira acerto',f.controls.placar.textContent.includes('0 corretas')&&f.controls.placar.textContent.includes('1 de 1 com marcação documental'));
  check('feedback crítico concordante e neutro',f.items[0].fields['.cr-feedback'].textContent.includes('coincide com o gabarito oficial E')&&!f.items[0].dataset.crResultado);
  check('crítico preserva marcação e abre análise',JSON.parse(f.store.get(f.key)).respostas['11111111']==='E'&&f.items[0].fields['.cr-resolucao'].open===true);
  f.answer(1,'C');check('regular entra no numerador e denominador',f.controls.placar.textContent.includes('Treino pontuável: 1 de 1 respondidas, 1 correta e 0 incorretas'));
  check('feedback regular preservado',f.items[1].dataset.crResultado==='certo'&&f.items[1].fields['.cr-feedback'].textContent.startsWith('Resposta correta.'));
  f.redo(0);check('refazer crítico não apaga regular',f.controls.placar.textContent.includes('1 correta')&&f.controls.placar.textContent.includes('0 de 1 com marcação documental')&&!f.items[0].fields.fieldset.disabled);
  f.answer(0,'C');check('divergência crítica não vira erro',f.controls.placar.textContent.includes('0 incorretas')&&f.items[0].fields['.cr-feedback'].textContent.includes('não coincide com o gabarito oficial E'));
  f.controls.pendentes.checked=true;f.controls.pendentes.events.change();check('filtro pendentes respeita ambas marcações',f.items.every(i=>i.hidden)&&f.lot.hidden);
  f.ctx.reveladoresBanco['questoes-reais'](f.items[0]);check('link direto revela crítico e limpa filtros',!f.items[0].hidden&&!f.controls.pendentes.checked);
  f.controls.busca.value='regular';f.controls.busca.events.input();check('busca não altera agregados',f.items[0].hidden&&!f.items[1].hidden&&f.controls.placar.textContent.includes('1 correta'));
  f=setup(source,{stored:{'11111111':'E','22222222':'E','33333333':'C'}});check('resposta antiga crítica reclassificada ao carregar',f.items[0].radios.find(r=>r.value==='E').checked&&f.controls.placar.textContent.includes('0 corretas e 1 incorreta'));
  f.redo(1);check('resposta histórica não reconhecida preservada na gravação',JSON.parse(f.store.get(f.key)).respostas['33333333']==='C');
  f.store.set(f.key,JSON.stringify({v:2,respostas:{'11111111':'C','22222222':'C'}}));f.events.storage({key:f.key});check('sincronização outra aba aplica exclusão',f.controls.placar.textContent.includes('1 correta e 0 incorretas')&&f.items[0].fields['.cr-feedback'].textContent.includes('não coincide'));
  f=setup(source,{storageError:true});f.answer(0,'E');check('armazenamento negado mantém exclusão local e aviso',f.controls.placar.textContent.includes('0 corretas')&&f.controls.armazenamento.textContent.includes('não permitiu'));
  f=setup(source,{allCritical:true});f.answer(0,'E');f.answer(1,'C');check('banco só crítico não inventa denominador/percentual',f.controls.placar.textContent.includes('0 de 0 respondidas, 0 corretas e 0 incorretas')&&f.controls.placar.textContent.includes('2 de 2 com marcação documental'));
  f=setup(source,{modulo:'e2'});f.answer(0,'E');check('outro módulo ignora marcador E1 e mantém resultado',f.items[0].dataset.crResultado==='certo'&&!f.controls.placar.textContent.includes('críticos')&&f.controls.placar.textContent.includes('1 correta'));
  f=setup(source,{marked:false});f.answer(0,'C');check('E1 sem marcador mantém lógica anterior',f.items[0].dataset.crResultado==='errado'&&!f.controls.placar.textContent.includes('críticos')&&f.controls.placar.textContent.includes('1 incorreta'));
  return {id:'BAN-10',rodada:1,ok:true,verificacoes:checks.length,checks,limites:'Execução da função iniciarBanco real em DOM e armazenamento controlados; digitais fornecidas como fixture. Preservação das digitais reais e navegador documentados separadamente.'};
}
