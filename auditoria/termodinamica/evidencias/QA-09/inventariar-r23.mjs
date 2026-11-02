import fs from 'node:fs';
import path from 'node:path';
import {parseHtml,isInventoryArticle,decodeHtml,sha256} from '../../inventario/validar-inventario.mjs';

// Inventário estrutural conservador, não calcula nem determina mérito científico.
const files=['modulos/e1-termodinamica.html','formulas/termodinamica.html'];
const out={estado:'PENDENTE_DE_TRIAGEM_E_RECALCULO',metodo:'Fragmentos de texto diretamente pertencentes a cada nó mais objetos pedagógicos, MathML, imagens e atributos significativos; âncoras e intervalos são relacionados ao SHA do documento. Não deduz não aplicabilidade de busca por algarismos.',limites:['O parser é um tokenizador, não um navegador; a apresentação dinâmica e o conteúdo visual dos SVGs e recursos dependem de inspeção humana.','Registros se sobrepõem deliberadamente: textos e fórmulas dentro de exemplos, diagnósticos, tabelas e fichas não são ocorrências independentes automaticamente.','Os 197 artigos BAN-08 são segregados pelo identificador e hash do documento; referências e material de fora deles continuam no escopo.','Não foi realizado recálculo, conferência de fontes ou revisão independente.'],documentos:[],ocorrencias:[],referencias:[],recursos:[],ativos_especificos:[],artigos_excluidos:[]};
const category=n=>{const c=(n.attrs.class??'').split(/\s+/);if(c.includes('formula-card'))return 'ficha_formula';if(c.includes('exemplo'))return 'exemplo_ou_diagnostico';if(c.includes('caso'))return 'caso_oficina';if(c.includes('flashcard'))return 'flashcard';if(c.includes('equacao'))return 'equacao_contextualizada';if(c.includes('tabela')||n.tag==='table')return 'tabela';if(n.tag==='math')return 'mathml';if(n.tag==='svg'||n.tag==='img'||n.tag==='figure')return 'figura';if(n.tag==='section')return 'secao';return null};
const nearest=n=>{for(let x=n;x;x=x.parent)if(x.attrs.id)return x.attrs.id;return null};
const section=n=>{for(let x=n;x;x=x.parent)if(x.tag==='section')return x.attrs.id??null;return null};
const clean=s=>decodeHtml(s.replace(/<!--[\s\S]*?-->/g,' ').replace(/<[^>]*>/g,' ')).replace(/\s+/g,' ').trim();
const rel=p=>p.split(path.sep).join('/');
for(const file of files){
 const bytes=fs.readFileSync(file),html=bytes.toString('utf8'),doc=parseHtml(html),arts=file.startsWith('modulos/')?doc.nodes.filter(isInventoryArticle):[];
 if(doc.errors.length||file.startsWith('modulos/')&&arts.length!==197)throw Error('Parser ou conjunto BAN-08 inesperado');
 const inside=n=>arts.some(a=>a.start<=n.start&&n.end<=a.end);
 out.documentos.push({arquivo:file,sha256:sha256(bytes),total_nos:doc.nodes.length,nos_fora:doc.nodes.filter(n=>!inside(n)).length,artigos_excluidos:arts.length,erros_parser:doc.errors});
 for(const a of arts)out.artigos_excluidos.push({id:a.attrs.id,sha256_fragmento:sha256(html.slice(a.start,a.end))});
 let by={};
 for(const n of doc.nodes){
  if(inside(n))continue;
  const cat=category(n),base={arquivo:file,secao:section(n),ancora:nearest(n),tag:n.tag,inicio_utf16:n.start,fim_utf16:n.end,linha:html.slice(0,n.start).split('\n').length};
  if(cat){by[cat]=(by[cat]??0)+1;let text=clean(html.slice(n.start,n.end));out.ocorrencias.push({...base,id:`${file}:${n.start}:${cat}`,tipo:cat,sha256_fragmento:sha256(html.slice(n.start,n.end)),trecho:text.slice(0,350),estado:'PENDENTE',observacao:cat==='exemplo_ou_diagnostico'&&section(n)==='preparacao-questoes'?'diagnóstico da seção 8.2':null});}
  // Captura integral de texto direto de todos os nós, sem repetir descendentes.
  if(!['script','style','head','meta','link'].includes(n.tag)){
   let pos=n.openEnd,parts=[];for(const child of n.children){if(child.start>pos)parts.push(html.slice(pos,child.start));pos=Math.max(pos,child.end)}if(n.end>pos)parts.push(html.slice(pos,n.end).replace(new RegExp(`</${n.tag}\\s*>\\s*$`,'i'),''));let raw=parts.join(' '),text=clean(raw);if(text)out.ocorrencias.push({...base,id:`${file}:${n.start}:texto`,tipo:'texto_direto',sha256_fragmento:sha256(raw),texto:text,estado:'PENDENTE_TRIAGEM'});
  }
  const attrs=Object.fromEntries(Object.entries(n.attrs).filter(([key])=>/^(?:alt|title|aria-label|value|min|max|step|data-.+)$/i.test(key)));if(Object.keys(attrs).length)out.ocorrencias.push({...base,id:`${file}:${n.start}:atributos`,tipo:'atributos_significativos',atributos:attrs,sha256_fragmento:sha256(html.slice(n.start,n.openEnd)),estado:'PENDENTE_TRIAGEM'});
  for(const attr of ['href','src','poster','data'])if(n.attrs[attr]&&(['a','link','script','img','object','source','image','use'].includes(n.tag))){let value=n.attrs[attr],rec={...base,atributo:attr,valor:value,texto:clean(html.slice(n.start,n.end)).slice(0,250)};out.referencias.push(rec);if(!/^(?:#|[a-z][a-z\d+.-]*:|\/\/)/i.test(value)){let target=path.resolve(path.dirname(file),decodeURIComponent(value.split(/[?#]/)[0]));if(fs.existsSync(target)&&fs.statSync(target).isFile())out.recursos.push({origem:file,referencia:value,arquivo:rel(path.relative('.',target)),sha256:sha256(fs.readFileSync(target)),papel:['script','img','object','source','image','use'].includes(n.tag)?'recurso_carregado':'documento_ou_fonte_vinculada',estado:'PENDENTE_AVALIACAO_DE_ESCOPO'});}}
 }
 out.documentos.at(-1).contagens_objetos=by;
}
for(const name of fs.readdirSync('assets/termodinamica')){const file=`assets/termodinamica/${name}`;if(fs.statSync(file).isFile())out.ativos_especificos.push({arquivo:file,sha256:sha256(fs.readFileSync(file)),estado:'PENDENTE_AVALIACAO_DE_ESCOPO',observacao:'Confrontar uso fora dos 197 artigos, vínculos de dados e scripts e aceites anteriores; não presumir que todo o arquivo pertence ao escopo.'});}
const diag=out.ocorrencias.filter(x=>x.tipo==='exemplo_ou_diagnostico'&&x.secao==='preparacao-questoes');
if(diag.length!==28)throw Error(`Quantidade de diagnósticos inesperada: ${diag.length}`);
diag.forEach((x,i)=>x.diagnostico=i+1);
out.resumo={diagnosticos:diag.length,exemplos_incluindo_diagnosticos:out.ocorrencias.filter(x=>x.tipo==='exemplo_ou_diagnostico').length,casos_oficina:out.ocorrencias.filter(x=>x.tipo==='caso_oficina').length,flashcards:out.ocorrencias.filter(x=>x.tipo==='flashcard').length,fichas:out.ocorrencias.filter(x=>x.tipo==='ficha_formula').length,mathml:out.ocorrencias.filter(x=>x.tipo==='mathml').length,figuras:out.ocorrencias.filter(x=>x.tipo==='figura').length,textos_diretos:out.ocorrencias.filter(x=>x.tipo==='texto_direto').length,referencias:out.referencias.length,recursos_unicos:[...new Set(out.recursos.map(r=>r.arquivo))].length};
const dest='auditoria/termodinamica/evidencias/QA-09/inventario-r23.json';if(fs.existsSync(dest))throw Error('Destino r21 já existe');fs.writeFileSync(dest,JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify({arquivo:dest,sha256:sha256(fs.readFileSync(dest)),resumo:out.resumo,documentos:out.documentos},null,2));
