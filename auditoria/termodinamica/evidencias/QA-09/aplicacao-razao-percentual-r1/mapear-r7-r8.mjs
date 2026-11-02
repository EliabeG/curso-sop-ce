import fs from 'node:fs';
import {sha256} from '../../../inventario/validar-inventario.mjs';
const d='auditoria/termodinamica/evidencias/QA-09/',p=d+'aplicacao-razao-percentual-r1/';
const before=fs.readFileSync(p+'antes.html','utf8'),after=fs.readFileSync('modulos/e1-termodinamica.html','utf8');
const edits=JSON.parse(fs.readFileSync(p+'edicoes-aplicadas.json','utf8'));
let built='',cursor=0;
for(const e of edits){let old=fs.readFileSync(e.original,'utf8').replace(/\n$/,''),novo=fs.readFileSync(e.candidata,'utf8').replace(/\n$/,'');if(sha256(old)!==e.original_sha256||sha256(novo)!==e.candidata_sha256||before.slice(e.inicio,e.fim)!==old)throw Error('Fragmento divergente '+e.id);built+=before.slice(cursor,e.inicio)+novo;cursor=e.fim;}
if(built+before.slice(cursor)!==after)throw Error('Reconstrução do delta falhou');
const a=JSON.parse(fs.readFileSync(d+'inventario-r7.json')),b=JSON.parse(fs.readFileSync(d+'inventario-r8.json'));
if(a.ocorrencias.length!==b.ocorrencias.length||JSON.stringify(a.artigos_excluidos)!==JSON.stringify(b.artigos_excluidos)||a.artigos_excluidos.length!==197)throw Error('Mudou estrutura/artigos');
const inEdit=n=>edits.some(e=>n>=e.inicio&&n<e.fim);
const desloc=n=>edits.reduce((v,e)=>v+(n>=e.fim?e.delta:0),0);
let rows=[],errors=[];
for(let i=0;i<a.ocorrencias.length;i++){
 const x=a.ocorrencias[i],y=b.ocorrencias[i],inside=x.arquivo==='modulos/e1-termodinamica.html'&&inEdit(x.inicio_utf16);
 let ctx=['arquivo','tipo','tag','secao','ancora'].every(k=>x[k]===y[k]);
 let expected=x.inicio_utf16+(x.arquivo==='modulos/e1-termodinamica.html'?desloc(x.inicio_utf16):0);
 if(!ctx||!inside&&expected!==y.inicio_utf16){errors.push({i,anterior:x.id,atual:y.id,expected});continue;}
 rows.push({id_r7:x.id,id_r8:y.id,arquivo:x.arquivo,tipo:x.tipo,tag:x.tag,secao:x.secao,ancora:x.ancora,inicio_r7:x.inicio_utf16,inicio_r8:y.inicio_utf16,sha256_fragmento_r7:x.sha256_fragmento,sha256_fragmento_r8:y.sha256_fragmento,dentro_do_bloco_editado:inside,correspondencia:x.sha256_fragmento===y.sha256_fragmento?'CONTEUDO_IDENTICO':'CONTEUDO_ALTERADO_OU_ANCESTRAL'});
}
if(errors.length)throw Error(JSON.stringify(errors.slice(0,10)));
if(a.referencias.length!==b.referencias.length)throw Error('Quantidade de referências alterada');
for(let i=0;i<a.referencias.length;i++){
 const x=a.referencias[i],y=b.referencias[i],inside=x.arquivo==='modulos/e1-termodinamica.html'&&inEdit(x.inicio_utf16);
 let offset=x.arquivo==='modulos/e1-termodinamica.html'?desloc(x.inicio_utf16):0;
 if(!['arquivo','secao','ancora','tag','atributo','valor','texto'].every(k=>x[k]===y[k])||!inside&&x.inicio_utf16+offset!==y.inicio_utf16)throw Error('Referência não corresponde: '+i);
}
if(a.recursos.length!==b.recursos.length)throw Error('Quantidade de recursos mudou');
for(let i=0;i<a.recursos.length;i++){const x=a.recursos[i],y=b.recursos[i];if(!['origem','referencia','arquivo','papel','estado'].every(k=>x[k]===y[k]))throw Error('Recurso alterado '+i);if(x.arquivo==='modulos/e1-termodinamica.html'){if(x.sha256!==sha256(before)||y.sha256!==sha256(after))throw Error('Fotografia E1 inconsistente '+i);}else if(x.sha256!==y.sha256)throw Error('Recurso alterado '+i);}
const dif=rows.filter(x=>x.correspondencia!=='CONTEUDO_IDENTICO');
const out={estado:'MAPEAMENTO_ESTRUTURAL',limite:'Pares por ordem, documento e contexto; deslocamento verificado fora dos blocos alterados. Dentro dos blocos exige revisão individual de identidade. Hash igual não garante dependências ou transfere aceite. Referências conferidas por campos e início fora de blocos; registros de recursos comparados; visual e dinâmica requerem revisão.',base_r7:sha256(fs.readFileSync(d+'inventario-r7.json')),base_r8:sha256(fs.readFileSync(d+'inventario-r8.json')),html_r7:sha256(before),html_r8:sha256(after),edicoes:edits,total:rows.length,hash_diferente:dif.length,ids_deslocados:rows.filter(x=>x.id_r7!==x.id_r8).length,dentro_dos_blocos:rows.filter(x=>x.dentro_do_bloco_editado).length,referencias:a.referencias.length,recursos:a.recursos.length,artigos:197,correspondencias:rows};
const dest=d+'mapa-correspondencia-inventario-r7-r8-r1.json';if(fs.existsSync(dest))throw Error('Destino já existe');fs.writeFileSync(dest,JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify({...out,correspondencias:undefined,alterados:dif},null,2));
