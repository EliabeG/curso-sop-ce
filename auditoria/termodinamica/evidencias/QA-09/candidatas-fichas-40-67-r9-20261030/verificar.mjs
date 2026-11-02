import fs from 'node:fs';
import crypto from 'node:crypto';
import {parseHtml} from '../../../inventario/validar-inventario.mjs';

// Leitura e simulação em memória; não escreve no produto ou em evidências.
const root='auditoria/termodinamica/evidencias/QA-09/candidatas-fichas-40-67-r9-20261030';
const hash=s=>crypto.createHash('sha256').update(s,'utf8').digest('hex');
let html=fs.readFileSync('formulas/termodinamica.html','utf8');
let aula=fs.readFileSync('modulos/e1-termodinamica.html','utf8');
const m=JSON.parse(fs.readFileSync(`${root}/manifesto.json`,'utf8'));
if(hash(html)!==m.html_sha256)throw Error('fotografia do formulário mudou');
const before=parseHtml(html), cards=d=>d.nodes.filter(n=>(n.attrs.class??'').split(/\s+/).includes('formula-card'));
let changed=html;
for(const item of m.itens){
  let original=fs.readFileSync(`${root}/${item.ficha}-original.html`,'utf8').replace(/\n$/,'');
  let proposed=fs.readFileSync(`${root}/${item.ficha}-candidata.html`,'utf8').replace(/\n$/,'');
  if(hash(original)!==item.original_sha256||hash(proposed)!==item.candidata_sha256||html.split(original).length!==2||changed.split(original).length!==2)throw Error(`identidade ${item.ficha}`);
  if(html.slice(item.inicio_utf16,item.fim_utf16)!==original)throw Error(`posição ${item.ficha}`);
  let math=s=>(s.match(/<math\b[\s\S]*?<\/math>/g)??[]).join('');
  if(math(original)!==math(proposed))throw Error(`MathML alterado ${item.ficha}`);
  changed=changed.replace(original,proposed);
}
const after=parseHtml(changed),old=cards(before),updated=cards(after);
if(old.length!==100||updated.length!==100||before.errors.length||after.errors.length)throw Error('cartões ou parser');
for(let i=0;i<old.length;i++){
 if(old[i].attrs.id!==updated[i].attrs.id)throw Error('ordem/ID de ficha');
 if(!m.itens.some(x=>x.ancora===old[i].attrs.id)&&html.slice(old[i].start,old[i].end)!==changed.slice(updated[i].start,updated[i].end))throw Error(`alteração indevida ${old[i].attrs.id}`);
}
if(!parseHtml(aula).nodes.some(n=>n.attrs.id==='base-entropia'))throw Error('âncora da aula ausente');
const cond=(s,id)=>{let n=parseHtml(s).nodes.find(n=>n.attrs.id===id);let f=s.slice(n.start,n.end);let p=f.match(/<p class="formula-condicao">([^<]*)<\/p>/);if(!p||!n.attrs['data-busca'].includes(p[1]))throw Error(`busca e condição divergentes ${id}`);};
for(const item of m.itens)cond(changed,item.ancora);
console.log(JSON.stringify({ok:true,produtos_alterados:false,cartoes:100,demais_cartoes_iguais:98,mathml_preservado:true,destino_base_entropia_existe:true,estado:'AGUARDANDO_REVISAO_INDEPENDENTE'},null,2));
