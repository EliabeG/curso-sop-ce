import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { createHash } from 'node:crypto';
import { parseHtml, decodeHtml } from '../../inventario/validar-inventario.mjs';
const dir=path.dirname(fileURLToPath(import.meta.url));
const sha=b=>createHash('sha256').update(b).digest('hex');
const readJson=async p=>JSON.parse((await fs.readFile(path.join(dir,p),'utf8')).replace(/^\uFEFF/,''));
const html=await fs.readFile(path.join(dir,'antes/modulos/e1-termodinamica.html'),'utf8');
const baselineSha='81eedea9f3731979125724ebb52d839ca68930164b7d7570a2a646d6f5bed2fe';
if(sha(html)!==baselineSha)throw Error('A base anterior difere da declarada.');
const r1=await readJson('revisao-suplementos-80-r1.json'),r2=structuredClone(r1),doc=parseHtml(html);
const ancestor=(node,predicate)=>{for(let n=node.parent;n;n=n.parent)if(predicate(n))return n;return null;};
const arrays=new Map(r2.registros.map(r=>[r.id,[]]));
for(const a of doc.nodes.filter(n=>n.tag==='a')){
 const article=ancestor(a,n=>n.tag==='article');
 if(!article||!arrays.has(article.attrs.id))continue;
 if(ancestor(a,n=>(n.attrs.class||'').split(/\s+/).includes('cr-fontes')))continue;
 const href=a.attrs.href||'';
 if(!/^(#|https?:)/.test(href))continue;
 // Limite estrutural do elemento a: nenhum fechamento alheio é procurado por regex.
 const inner=html.slice(a.openEnd,a.end).replace(/<\/a\s*>\s*$/i,'');
 const label=decodeHtml(inner.replace(/<[^>]*>/g,'')).replace(/\s+/g,' ').trim();
 arrays.get(article.attrs.id).push({alvo:href,rotulo:label});
}
const deltas=[];
for(const r of r2.registros){
 const original=r.fontes.ensino_e_fundamentos_ja_vinculados;
 const links=arrays.get(r.id);
 deltas.push({id:r.id,campo:'fontes.ensino_e_fundamentos_ja_vinculados',antes:original,depois:links});
 r.fontes.ensino_e_fundamentos_ja_vinculados=links;
}
const count=[...arrays.values()].flat();
if(arrays.size!==80||count.length!==158)throw Error('Cobertura fora de80/158.');
await fs.writeFile(path.join(dir,'revisao-suplementos-80-r2.json'),JSON.stringify(r2,null,2)+'\n');
const delta={id:'FON-02',rodada:2,data:'2026-10-28',correcao:'R1-A',base:{arquivo:'antes/modulos/e1-termodinamica.html',sha256:baselineSha},regra:'Âncoras descendentes dos80CR na base anterior, fora de .cr-fontes, com href # ou http(s). Ordem e ocorrências preservadas, sem deduplicação; rótulo é o texto interno da própria âncora, entidades HTML decodificadas e espaços normalizados. Fontes novas da r1 continuam separadas.',matriz:{sha256_r1:sha(await fs.readFile(path.join(dir,'revisao-suplementos-80-r1.json'))),sha256_r2:sha(await fs.readFile(path.join(dir,'revisao-suplementos-80-r2.json'))),metadados:'Todos os campos fora dos80arrays são preservados, inclusive rodada1 da matriz científica. A reapresentação documental rodada2 é identificada nos arquivos/manifesto/delta/entrega.'},resumo:{registros:80,ocorrencias_antes:80,ocorrencias_depois:158,internas:count.filter(x=>x.alvo.startsWith('#')).length,externas:count.filter(x=>/^https?:/.test(x.alvo)).length,registros_com_omissoes:deltas.filter(x=>x.depois.length>x.antes.length).length},alteracoes:deltas};
await fs.writeFile(path.join(dir,'delta-r2.json'),JSON.stringify(delta,null,2)+'\n');
let md='# FON-02 r2 — vínculos antecedentes dos 80 CR\n\nData: 28/10/2026. Correção documental de R1-A. A ciência e a classificação individual permanecem na [revisão r1](REVISAO_SUPLEMENTOS_80-r1.md); a [matriz r2](revisao-suplementos-80-r2.json) muda apenas os 80 arrays de vínculos antecedentes. Seus demais campos, inclusive o marcador rodada 1 do conteúdo científico, foram preservados literalmente.\n\n## Origem e separação temporal\n\nEstes 158 vínculos pertencem ao HTML anterior às alterações FON-02, SHA-256 '+baselineSha+'. São 141 internos e 17 externos, na ordem do artigo, sem deduplicação. Excluem-se os rodapés documentais .cr-fontes e links de arquivos locais, já rastreados em campos próprios. Os rótulos abaixo contêm somente o texto da âncora, com espaços normalizados. As fontes acrescentadas ou reconfirmadas na r1 continuam separadas no [catálogo preservado](fontes-r1.json) e no campo primarias_acrescentadas_ou_reconfirmadas; não foram misturadas a este conjunto.\n\n';
for(const r of r2.registros){md+='## '+r.id+'\n\n';for(const [i,a] of r.fontes.ensino_e_fundamentos_ja_vinculados.entries()){const target=a.alvo.startsWith('#')?'../../../../modulos/e1-termodinamica.html'+a.alvo:a.alvo;md+=(i+1)+'. ['+a.rotulo.replaceAll('[','\\[').replaceAll(']','\\]')+']('+target+') — destino literal: '+a.alvo+'\n';}md+='\n';}
md+='## Verificação e limites\n\nA comparação independente usa HTMLParser da biblioteca padrão Python para reconstruir o mesmo conjunto sem importar o extrator Node. Confere todos os IDs, ocorrências, destinos, rótulos e ordem contra a matriz, além de preservar o restante por comparação estrutural. O [delta](delta-r2.json) contém antes/depois dos 80 arrays. Produto, inventário, resumo canônico, fontes novas e pacote r1 permanecem byte a byte idênticos. Não houve nova leitura científica, nova consulta de fontes ou novo teste de navegador nesta reapresentação.\n';
await fs.writeFile(path.join(dir,'REVISAO_SUPLEMENTOS_80-r2.md'),md);
console.log(JSON.stringify({registros:arrays.size,ocorrencias:count.length,internas:delta.resumo.internas,externas:delta.resumo.externas,matriz:delta.matriz.sha256_r2}));
