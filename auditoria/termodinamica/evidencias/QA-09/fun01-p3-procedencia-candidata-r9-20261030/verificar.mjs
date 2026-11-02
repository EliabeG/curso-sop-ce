import fs from 'node:fs';
import {parseHtml,isInventoryArticle,sha256} from '../../../inventario/validar-inventario.mjs';
// Verificação em memória: não grava material ou evidências históricas.
const dir='auditoria/termodinamica/evidencias/QA-09/fun01-p3-procedencia-candidata-r9-20261030';
const m=JSON.parse(fs.readFileSync(`${dir}/manifesto.json`,'utf8')),html=fs.readFileSync(m.documento,'utf8');
const exigir=(b,msg)=>{if(!b)throw Error(msg)};
exigir(sha256(html)===m.base_sha256,'foto da aula divergente');exigir(sha256(fs.readFileSync(m.inventario_qa09))===m.inventario_sha256,'inventário divergente');
const fragment=name=>fs.readFileSync(`${dir}/${name}.html`,'utf8').replace(/\n$/,'');
const original=fragment('original'),candidata=fragment('candidata');
exigir(sha256(original)===m.original_fragmento_sha256 && sha256(candidata)===m.candidata_fragmento_sha256,'hashes dos fragmentos divergentes');
exigir(html.slice(...m.paragrafo_posicao_utf16)===original && html.split(original).length===2,'identidade/posição não única');
exigir(original.split(m.texto_antes).length===2 && candidata===original.replace(m.texto_antes,m.texto_depois),'troca não é a candidata declarada');
const prior=parseHtml(html),preview=html.replace(original,candidata),after=parseHtml(preview);exigir(!prior.errors.length&&!after.errors.length,'erro do parser');
const first=prior.nodes.filter(isInventoryArticle),last=after.nodes.filter(isInventoryArticle);exigir(first.length===197&&last.length===197,'contagem');
const target=first.find(n=>n.attrs.id===m.artigo_id),target2=last.find(n=>n.attrs.id===m.artigo_id);
exigir(!!target&&!!target2&&sha256(html.slice(target.start,target.end))===m.artigo_sha256,'artigo divergente');
for(let i=0;i<197;i++){const a=first[i],b=last[i];exigir(a.attrs.id===b.attrs.id,'ordem/ID alterados');let before=html.slice(a.start,a.end),next=preview.slice(b.start,b.end);exigir(a.attrs.id===m.artigo_id?next===before.replace(original,candidata):before===next,`alteração fora do artigo alvo: ${a.attrs.id}`);}
let oldArticle=html.slice(target.start,target.end),newArticle=preview.slice(target2.start,target2.end);exigir(oldArticle.replace(original,candidata)===newArticle,'alteração adicional no artigo');
console.log(JSON.stringify({ok:true,estado:'CANDIDATA_NAO_APLICADA',artigos_nao_alvo_identicos:196,alvo:'fun01-e1-supercritico',troca_unica:true,base_sha256:m.base_sha256,preview_sha256:sha256(preview),limites:'Simulação estrutural em memória; não substitui auditoria independente nem revalidação da versão aplicada.'},null,2));
