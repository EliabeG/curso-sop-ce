// Exercita o código real de busca com fichas extraídas e DOM simulado.
const fs=require('fs'),vm=require('vm');
const data=JSON.parse(fs.readFileSync(0,'utf8'));
function node(extra={}){return Object.assign({hidden:false,value:'',textContent:'',handlers:{},dataset:{},addEventListener(k,v){this.handlers[k]=v},setAttribute(k,v){this[k]=v},focus(){}},extra)}
const cards=data.map(x=>{let reveal=node(),expr=node();let c=node({id:x.id,dataset:{busca:x.busca,grupo:x.grupo}});c.querySelector=s=>s==='.formula-revelar'?reveal:expr;return c;});
let group=node();group.querySelectorAll=()=>cards;
let controls={'formula-busca':node(),'formula-assunto':node({value:'todos'}),'formula-memorizar':node(),'formula-contagem':node(),'formula-vazio':node(),'formula-instrucao':node(),'formula-limpar':node(),'formula-imprimir':node()};let tools=node({hidden:true});
let doc={querySelector:()=>tools,querySelectorAll:s=>s==='.formula-card'?cards:s==='.formula-grupo'?[group]:[],getElementById:s=>controls[s]};
vm.runInNewContext(fs.readFileSync('assets/formulario-e1.js','utf8'),{document:doc,window:{print(){}}});
if(cards.length!==100)throw Error('quantidade de fichas');
const search=(id,text)=>{let c=cards.find(x=>x.id===id);if(!c)throw Error('ficha ausente '+id);controls['formula-busca'].value=text;controls['formula-busca'].handlers.input();if(c.hidden)throw Error('busca não encontrou '+id);return controls['formula-contagem'].textContent};
const f40=search('formula-reacao','pressao termodinamica fronteira');
const f67=search('formula-calor-reversivel','fronteira massa fixa');
controls['formula-busca'].value='palavra-inexistente-987654';controls['formula-busca'].handlers.input();if(cards.some(c=>!c.hidden)||controls['formula-vazio'].hidden)throw Error('busca sem resultado');
console.log(JSON.stringify({ok:true,fichas:cards.length,ficha40:f40,ficha67:f67,busca_inexistente:controls['formula-contagem'].textContent,limite:'Node/VM e DOM simulados; não é navegador real.'},null,2));
