import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { createHash } from 'node:crypto';
import { parseHtml, isInventoryArticle, validateInventory } from '../../inventario/validar-inventario.mjs';
const base=path.dirname(fileURLToPath(import.meta.url)),root=path.resolve(base,'../../../..');
const rel='auditoria/termodinamica/evidencias/FON-02/';
const read=p=>fs.readFile(path.join(root,p));
const json=async p=>JSON.parse((await read(p)).toString('utf8').replace(/^\uFEFF/,''));
const sha=b=>createHash('sha256').update(b).digest('hex');
const checks=[];const check=(nome,ok,detalhe)=>checks.push({nome,ok:Boolean(ok),...(detalhe===undefined?{}:{detalhe})});
const snapshot=await json(rel+'snapshot-antes.json');
for(const s of snapshot.arquivos){check('snapshot:'+s.arquivo,sha(await read(s.copia))===s.sha256);if(!['modulos/e1-termodinamica.html','auditoria/termodinamica/inventario/inventario-questoes.json','auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md'].includes(s.arquivo))check('infraestrutura-preservada:'+s.arquivo,sha(await read(s.arquivo))===s.sha256);}
const old=(await read(rel+'antes/modulos/e1-termodinamica.html')).toString('utf8'),actual=(await read('modulos/e1-termodinamica.html')).toString('utf8');
const delta=await json(rel+'delta-r1.json');let rebuilt=old;
for(const p of delta.html.substituicoes){check('delta-ocorrencia:'+p.id,rebuilt.split(p.antes).length===2);rebuilt=rebuilt.replace(p.antes,p.depois);}
for(const id of delta.html.resumos.ids){const doc=parseHtml(rebuilt),n=doc.ids.get(id)[0],a=rebuilt.slice(n.start,n.end);check('summary-ocorrencia:'+id,a.split(delta.html.resumos.antes).length===2);rebuilt=rebuilt.slice(0,n.start)+a.replace(delta.html.resumos.antes,delta.html.resumos.depois)+rebuilt.slice(n.end);}
check('delta-reconstroi-todo-html',rebuilt===actual);
check('hashes-base-final',sha(old)===delta.html.sha256_antes&&sha(actual)===delta.html.sha256_depois);
check('snapshot-final',sha(await read(rel+'e1-termodinamica.r1.html'))===sha(actual));
const before=parseHtml(old),after=parseHtml(actual),ba=before.nodes.filter(isInventoryArticle),aa=after.nodes.filter(isInventoryArticle);
check('197-ids-e-ordem',ba.length===197&&aa.length===197&&JSON.stringify(ba.map(n=>n.attrs.id))===JSON.stringify(aa.map(n=>n.attrs.id)));
const changed=aa.filter((n,i)=>actual.slice(n.start,n.end)!==old.slice(ba[i].start,ba[i].end)).map(n=>n.attrs.id);
const bodyIDs=delta.html.substituicoes.map(p=>p.id).sort();
const bodiesChanged=aa.filter((n,i)=>actual.slice(n.start,n.end).replace(delta.html.resumos.depois,delta.html.resumos.antes)!==old.slice(ba[i].start,ba[i].end)).map(n=>n.attrs.id).sort();
check('somente21-conteudos-autorizados',bodyIDs.length===21&&JSON.stringify(bodyIDs)===JSON.stringify(bodiesChanged),bodiesChanged);
check('74-artigos-alterados123-identicos',changed.length===74,changed);
const math=doc=>doc.nodes.filter(n=>n.tag==='math').map(n=>doc.html.slice(n.start,n.end));
// O parser não conserva html como propriedade: fornecemos a cadeia explicitamente.
const mathOf=(doc,html)=>doc.nodes.filter(n=>n.tag==='math').map(n=>html.slice(n.start,n.end));
check('734-MathML-identicos',mathOf(before,old).length===734&&JSON.stringify(mathOf(before,old))===JSON.stringify(mathOf(after,actual)));
const classes=['cr-enunciado','cr-afirmacao','cr-meta','cr-fontes'];
const components=(doc,html,n)=>({atributos:n.attrs,oficiais:doc.nodes.filter(x=>x.start>n.start&&x.end<n.end&&(classes.some(c=>(x.attrs.class||'').split(/\s+/).includes(c))||['fieldset','img'].includes(x.tag))).map(x=>html.slice(x.start,x.end))});
const cr=aa.filter(n=>/^cr-e1-\d+$/.test(n.attrs.id||''));
check('80-componentes-oficiais-atributos-identicos',cr.length===80&&cr.every(n=>JSON.stringify(components(after,actual,n))===JSON.stringify(components(before,old,before.ids.get(n.attrs.id)[0]))));
check('digitais-preservadas-por-identidade-dos-componentes',cr.every(n=>JSON.stringify(components(after,actual,n))===JSON.stringify(components(before,old,before.ids.get(n.attrs.id)[0])))&&sha(await read('assets/curso.js'))===snapshot.arquivos.find(s=>s.arquivo==='assets/curso.js').sha256,'digitalDoBanco lê enunciado/imagens, opções e chave; esses componentes e a função permanecem idênticos. Não é simulação de resposta de estudante.');
check('71-treino9-estudos-criticos',cr.filter(n=>n.attrs['data-cr-avaliacao']==='estudo-critico').length===9&&cr.filter(n=>n.attrs['data-cr-avaliacao']!=='estudo-critico').length===71);
const summary=(html)=>html.match(/<details class="cr-resolucao"><summary>[\s\S]*?<\/summary>/)?.[0];
check('nove-summaries-criticos-preservados',cr.filter(n=>n.attrs['data-cr-avaliacao']==='estudo-critico').every(n=>{const b=before.ids.get(n.attrs.id)[0];return summary(actual.slice(n.start,n.end))===summary(old.slice(b.start,b.end));}));
check('71-summaries-autoria',cr.filter(n=>actual.slice(n.start,n.end).includes(delta.html.resumos.depois)).length===71);
const originalInv=await json(rel+'antes/auditoria/termodinamica/inventario/inventario-questoes.json'),inventory=await json('auditoria/termodinamica/inventario/inventario-questoes.json'),expected=structuredClone(originalInv);
expected.fonte.sha256=sha(actual);expected.fonte.snapshot=rel+'e1-termodinamica.r1.html';
for(const item of expected.itens){const n=after.ids.get(item.id)[0];item.localizacao.sha256_artigo=sha(actual.slice(n.start,n.end));}
check('inventario-somente-hashes-e-fonte',JSON.stringify(expected)===JSON.stringify(inventory));
check('123-registros-identicos',inventory.itens.filter(i=>JSON.stringify(i)===JSON.stringify(originalInv.itens.find(b=>b.id===i.id))).length===123);
const matrix=await json(rel+'revisao-suplementos-80-r1.json'),records=matrix.registros;
check('matriz80-ids-exatos',records.length===80&&new Set(records.map(r=>r.id)).size===80&&JSON.stringify(records.map(r=>r.id).sort())===JSON.stringify(cr.map(n=>n.attrs.id).sort()));
check('matriz-hash-final',matrix.fonte_entregue.sha256===sha(actual));
for(const r of records){const n=after.ids.get(r.id)[0];check(r.id+':registro-completo',r.leitura_integral&&r.diagnostico&&r.decisao.justificativa&&r.original.texto_do_bloco_original&&r.identidade.sha256_artigo_entregue===sha(actual.slice(n.start,n.end)));}
const f1=await read('auditoria/termodinamica/evidencias/FON-01/manifesto-r1.json');check('manifesto-FON01-preservado',sha(f1)==='91684a6c5dcb945ff9c8841cb6cc02ca82b50c7eb285a2a2b18863eb413dc628');
const canonical=await validateInventory({rootDir:root});check('validador-canonico',canonical.ok,canonical);
const result={id:'FON-02',rodada:1,data:'2026-10-28',metodo:'Preservação exata, delta integral, completude documental e validação canônica. Não substitui a revisão científica independente nem testa aprendizagem.',ok:checks.every(x=>x.ok),verificacoes:checks.length,falhas:checks.filter(x=>!x.ok),resumo:{artigos:197,conteudos_esclarecidos:bodyIDs.length,artigos_alterados:changed.length,artigos_identicos:197-changed.length,registros_CR:80,summaries_autoria:71,criticos:9,MathML:734},canonico:canonical,checks};
await fs.writeFile(path.join(base,'verificacao-r1.json'),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({ok:result.ok,verificacoes:result.verificacoes,falhas:result.falhas,resumo:result.resumo,canonico:canonical},null,2));
if(!result.ok)process.exitCode=1;
