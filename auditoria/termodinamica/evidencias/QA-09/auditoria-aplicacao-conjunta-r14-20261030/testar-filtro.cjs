// Exercício da busca real com DOM simulado, alimentado por fichas extraídas do formulário atual.
const fs=require('fs'),vm=require('vm');const data=JSON.parse(fs.readFileSync(0,'utf8'));
function node(extra={}){return Object.assign({hidden:false,value:'',textContent:'',handlers:{},dataset:{},addEventListener(k,v){this.handlers[k]=v},setAttribute(k,v){this[k]=v},focus(){}},extra)}
const cards=data.map(x=>{let reveal=node(),expr=node(),c=node({id:x.id,dataset:{busca:x.busca,grupo:x.grupo}});c.querySelector=s=>s==='.formula-revelar'?reveal:expr;return c});
let group=node();group.querySelectorAll=()=>cards;
let controls={'formula-busca':node(),'formula-assunto':node({value:'todos'}),'formula-memorizar':node(),'formula-contagem':node(),'formula-vazio':node(),'formula-instrucao':node(),'formula-limpar':node(),'formula-imprimir':node()},tools=node({hidden:true});
let doc={querySelector:()=>tools,querySelectorAll:s=>s==='.formula-card'?cards:s==='.formula-grupo'?[group]:[],getElementById:s=>controls[s]};
vm.runInNewContext(fs.readFileSync('assets/formulario-e1.js','utf8'),{document:doc,window:{print(){}}});
if(cards.length!==100)throw Error('quantidade');let results={};
for(const [id,query] of [['formula-latente','pressao termodinamica fronteira'],['formula-eficiencia','todo calor recebido rejeitado'],['formula-cop-refrigerador','trabalho outra fonte acionamento']]){
 const c=cards.find(x=>x.id===id);if(!c)throw Error('ficha ausente '+id);controls['formula-busca'].value=query;controls['formula-busca'].handlers.input();if(c.hidden)throw Error('filtro não encontrou '+id);results[id]=controls['formula-contagem'].textContent;
}
controls['formula-busca'].value='palavra-inexistente-987654';controls['formula-busca'].handlers.input();if(cards.some(c=>!c.hidden)||controls['formula-vazio'].hidden)throw Error('busca vazia');
console.log(JSON.stringify({ok:true,fichas:cards.length,buscas:results,limite:'Node/VM e DOM simulados; não é navegador real.'},null,2));
