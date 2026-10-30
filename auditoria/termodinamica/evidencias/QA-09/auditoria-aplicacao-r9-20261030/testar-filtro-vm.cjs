// Teste dos controles reais em DOM simulado. Recebe JSON de extrair-fichas.py pelo stdin.
const fs=require('fs'),vm=require('vm');const data=JSON.parse(fs.readFileSync(0,'utf8'));
function node(extra={}){return Object.assign({hidden:false,value:'',textContent:'',handlers:{},dataset:{},addEventListener(k,v){this.handlers[k]=v},setAttribute(k,v){this[k]=v},focus(){}},extra)}
const cards=data.map(x=>{let reveal=node(),expr=node();let c=node({id:x.id,dataset:{busca:x.busca,grupo:x.grupo}});c.querySelector=s=>s==='.formula-revelar'?reveal:expr;return c;});let group=node();group.querySelectorAll=()=>cards;
let controls={'formula-busca':node(),'formula-assunto':node({value:'todos'}),'formula-memorizar':node(),'formula-contagem':node(),'formula-vazio':node(),'formula-instrucao':node(),'formula-limpar':node(),'formula-imprimir':node()};let tools=node({hidden:true});
let doc={querySelector:()=>tools,querySelectorAll:s=>s==='.formula-card'?cards:s==='.formula-grupo'?[group]:[],getElementById:s=>controls[s]};vm.runInNewContext(fs.readFileSync('assets/formulario-e1.js','utf8'),{document:doc,window:{print(){}}});
let card=cards.find(x=>x.id==='formula-brayton-liquido');if(!card||cards.length!==100)throw Error('identidade das fichas');
controls['formula-busca'].value='rendimento motor';controls['formula-busca'].handlers.input();if(card.hidden)throw Error('ficha 80 não encontrada');let encontrados=controls['formula-contagem'].textContent;
controls['formula-busca'].value='termo-inexistente-984123';controls['formula-busca'].handlers.input();if(!card.hidden||controls['formula-vazio'].hidden)throw Error('busca inexistente não esvaziou');let nenhum=controls['formula-contagem'].textContent;
controls['formula-memorizar'].handlers.click();if(!card.querySelector('.formula-expressao').hidden)throw Error('modo memorização não ocultou');card.querySelector('.formula-revelar').handlers.click();if(card.querySelector('.formula-expressao').hidden)throw Error('revelação falhou');
console.log(JSON.stringify({cartoes:cards.length,busca_motor:encontrados,busca_inexistente:nenhum,memorizacao:'passou',ambiente:'Node/VM; DOM e agrupamento simulados, não navegador'}));
