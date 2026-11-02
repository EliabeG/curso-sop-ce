import fs from 'node:fs';
import {sha256} from '../../inventario/validar-inventario.mjs';

const dir='auditoria/termodinamica/evidencias/QA-09/';
const app=dir+'aplicacao-exemplos-011-013-r1/';
const a=JSON.parse(fs.readFileSync(dir+'inventario-r6.json','utf8'));
const b=JSON.parse(fs.readFileSync(dir+'inventario-r7.json','utf8'));
const old=fs.readFileSync(app+'antes/e1-termodinamica.html','utf8');
const now=fs.readFileSync('modulos/e1-termodinamica.html','utf8');
const edits=['011','013'].map(id=>{
  const x=JSON.parse(fs.readFileSync(`${dir}exemplo-${id}-candidata-r1.json`,'utf8'));
  const inicio=old.indexOf(x.antes);
  if(inicio<0||old.split(x.antes).length!==2)throw Error(`Trecho ${id} ausente ou duplicado`);
  return {id,inicio,fim:inicio+x.antes.length,delta:x.depois.length-x.antes.length,antes:x.antes,depois:x.depois};
}).sort((x,y)=>x.inicio-y.inicio);
if(edits.reduce((s,e)=>s.replace(e.antes,e.depois),old)!==now)throw Error('Delta inesperado');
if(a.ocorrencias.length!==b.ocorrencias.length)throw Error('Quantidade diferente');
if(JSON.stringify(a.artigos_excluidos)!==JSON.stringify(b.artigos_excluidos)||a.artigos_excluidos.length!==197)throw Error('Artigos alterados');
let errors=[],rows=[];
for(let i=0;i<a.ocorrencias.length;i++){
 const x=a.ocorrencias[i],y=b.ocorrencias[i];
 const sameContext=['arquivo','tipo','tag','secao','ancora'].every(k=>x[k]===y[k]);
 let offset=0,inside=false;
 if(x.arquivo==='modulos/e1-termodinamica.html')for(const e of edits){
   if(x.inicio_utf16>=e.fim)offset+=e.delta;
   else if(x.inicio_utf16>e.inicio)inside=true;
 }
 if(!sameContext||inside||x.inicio_utf16+offset!==y.inicio_utf16){errors.push({indice:i,anterior:x.id,atual:y.id});continue;}
 rows.push({id_r6:x.id,id_r7:y.id,arquivo:x.arquivo,tipo:x.tipo,tag:x.tag,secao:x.secao,ancora:x.ancora,inicio_r6:x.inicio_utf16,inicio_r7:y.inicio_utf16,sha256_fragmento_r6:x.sha256_fragmento,sha256_fragmento_r7:y.sha256_fragmento,correspondencia:x.sha256_fragmento===y.sha256_fragmento?'CONTEUDO_IDENTICO':'CONTEUDO_ALTERADO_OU_ANCESTRAL'});
}
const changed=rows.filter(x=>x.correspondencia!=='CONTEUDO_IDENTICO');
const out={estado:errors.length?'ERRO':'MAPEAMENTO_ESTRUTURAL',limite:'Pares por ordem, documento, tipo, tag, seção, âncora e deslocamento. Hash igual não garante contexto ou validade das dependências, nem transfere automaticamente aceites. IDs são posições, não identidade durável. Referências e recursos separados não são cobertos por este mapa. Não aprova QA-09.',base_r6:sha256(fs.readFileSync(dir+'inventario-r6.json')),base_r7:sha256(fs.readFileSync(dir+'inventario-r7.json')),html_r6:sha256(old),html_r7:sha256(now),edicoes:edits.map(({id,inicio,fim,delta})=>({id,inicio_utf16:inicio,fim_utf16:fim,delta_utf16:delta})),total:rows.length,mesmo_hash:rows.length-changed.length,hash_diferente:changed.length,ids_deslocados:rows.filter(x=>x.id_r6!==x.id_r7).length,erros:errors,correspondencias:rows};
fs.writeFileSync(dir+'mapa-correspondencia-inventario-r6-r7-r1.json',JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify({...out,correspondencias:undefined,alterados:changed},null,2));
if(errors.length)process.exitCode=1;
