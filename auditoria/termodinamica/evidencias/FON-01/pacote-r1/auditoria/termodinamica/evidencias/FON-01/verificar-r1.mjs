import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { createHash } from 'node:crypto';
import { parseHtml, isInventoryArticle, validateInventory } from '../../inventario/validar-inventario.mjs';
const base=path.dirname(fileURLToPath(import.meta.url)), root=path.resolve(base,'../../../..');
const rel='auditoria/termodinamica/evidencias/FON-01/';
const read=p=>fs.readFile(path.join(root,p));
const json=async p=>JSON.parse((await read(p)).toString('utf8').replace(/^\uFEFF/,''));
const sha=b=>createHash('sha256').update(b).digest('hex');
const checks=[];
const check=(nome,condicao,detalhe=null)=>{checks.push({nome,ok:Boolean(condicao),...(detalhe===null?{}:{detalhe})});};
const snap=await json(rel+'snapshot-antes.json');
for(const s of snap.arquivos){
 if(s.copia) check('snapshot:'+s.arquivo,sha(await read(s.copia))===s.sha256);
 if(!['modulos/e1-termodinamica.html','auditoria/termodinamica/inventario/inventario-questoes.json','auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md'].includes(s.arquivo))check('preservado:'+s.arquivo,sha(await read(s.arquivo))===s.sha256);
}
const baseline=(await read(rel+'antes/modulos/e1-termodinamica.html')).toString('utf8');
const current=(await read('modulos/e1-termodinamica.html')).toString('utf8');
const delta=await json(rel+'delta-r1.json');
let rebuilt=baseline;
for(const [i,d] of delta.html.substituicoes.entries()){check('delta-ocorrencia-unica:'+i,rebuilt.split(d.antes).length===2);rebuilt=rebuilt.replace(d.antes,d.depois);}
check('delta-reconstroi-html-integral',rebuilt===current);
check('hash-html-baseline',sha(baseline)===delta.html.sha256_antes);
check('hash-html-final',sha(current)===delta.html.sha256_depois);
check('snapshot-final',sha(await read(rel+'e1-termodinamica.r1.html'))===sha(current));
const before=parseHtml(baseline),after=parseHtml(current);
const ba=before.nodes.filter(isInventoryArticle),aa=after.nodes.filter(isInventoryArticle);
check('197-artigos',ba.length===197&&aa.length===197);
check('ids-ordem-preservados',JSON.stringify(ba.map(n=>n.attrs.id))===JSON.stringify(aa.map(n=>n.attrs.id)));
const changed=[];
for(let i=0;i<ba.length;i++){const b=ba[i],a=aa[i];if(baseline.slice(b.start,b.end)!==current.slice(a.start,a.end))changed.push(a.attrs.id);}
check('somente-cr80-muda',JSON.stringify(changed)===JSON.stringify(['cr-e1-80']),changed);
const beforeInv=await json(rel+'antes/auditoria/termodinamica/inventario/inventario-questoes.json');
const actualInv=await json('auditoria/termodinamica/inventario/inventario-questoes.json');
const expected=structuredClone(beforeInv);
expected.fonte.sha256=sha(current);expected.fonte.snapshot=rel+'e1-termodinamica.r1.html';
for(const item of expected.itens.filter(i=>i.banco==='real')){item.origem.conferencia_oficial='realizada';item.origem.evidencia_conferencia=rel+'conferencia-80-r1.json';}
const ex80=expected.itens.find(i=>i.id==='cr-e1-80'),a80=after.ids.get('cr-e1-80')[0];
ex80.localizacao.sha256_artigo=sha(current.slice(a80.start,a80.end));
ex80.origem.fontes[0].rotulo='Versão histórica (sem efeito) · PDF p. 4';
ex80.origem.fontes.unshift({rotulo:'Prova oficial atualizada em 11/05/2026 · PDF p. 5',url:'https://cdn.cebraspe.org.br/concursos/caesb_24/arquivos/905BAE8B8901D96A45D9CBF7F17341894AF8405A0E2D9122A552F640CAC8B9DB.pdf#page=5'});
check('inventario-somente-campos-autorizados',JSON.stringify(expected)===JSON.stringify(actualInv));
const noCR=actualInv.itens.filter(i=>i.banco!=='real');
check('117-registros-nao-CR-identicos',noCR.length===117&&noCR.every(i=>JSON.stringify(i)===JSON.stringify(beforeInv.itens.find(b=>b.id===i.id))));
const matrix=await json(rel+'conferencia-80-r1.json');
const rs=matrix.registros;
check('80-registros-individuais-unicos',rs.length===80&&new Set(rs.map(r=>r.id)).size===80);
check('12-familias',new Set(rs.map(r=>r.familia)).size===12);
check('80-ids-exatos',JSON.stringify(rs.map(r=>r.id).sort())===JSON.stringify(actualInv.itens.filter(i=>i.banco==='real').map(i=>i.id).sort()));
check('matriz-hash-html-corrente',matrix.fonte_entregue.sha256===sha(current));
const cache=new Map();const digest=async p=>{if(!cache.has(p))cache.set(p,sha(await read(p)));return cache.get(p);};
for(const r of rs){
 const item=actualInv.itens.find(i=>i.id===r.id),node=after.ids.get(r.id)?.[0];
 check(r.id+':campos-de-leitura',Boolean(r.identificacao.cargo_enfase&&r.identificacao.tipo_cor&&r.identificacao.data_aplicacao&&r.comparacao.contexto.nota&&r.comparacao.comando.nota&&r.comparacao.alternativas.nota&&r.comparacao.figura_tabela.nota&&r.versao_e_atos.pesquisa_atos.length));
 check(r.id+':pagina-prova-chave',Number.isInteger(r.prova.pagina_fisica)&&r.prova.pagina_fisica>0&&Number.isInteger(r.chave.pagina_fisica)&&r.chave.pagina_fisica>0);
 check(r.id+':chave',r.chave.coincide&&r.chave.valor_oficial===r.chave.valor_curso&&r.chave.valor_curso===node.attrs['data-cr-gabarito']);
 check(r.id+':hash-artigo',r.sha256_artigo_entregue===item.localizacao.sha256_artigo);
 for(const [label,d] of [['prova',r.prova],['chave',r.chave]]){check(r.id+':sha-'+label,await digest(d.arquivo)===d.sha256);check(r.id+':imagem-'+label,(await read(d.evidencia_visual)).length>0);}
 check(r.id+':indice-existe',(await read(r.versao_e_atos.indice)).length>0);
}
check('CR56-historico-E-C',JSON.stringify(rs.find(r=>r.id==='cr-e1-56').versao_e_atos).includes('E→C'));
check('CR67-historico-E-C',rs.find(r=>r.id==='cr-e1-67').versao_e_atos.pesquisa_atos[0].decisao.preliminar==='E');
check('CR80-atual-p5-historica-p4',rs.find(r=>r.id==='cr-e1-80').prova.pagina_fisica===5&&rs.find(r=>r.id==='cr-e1-80').prova_historica.pagina_fisica===4);
const canonical=await validateInventory({rootDir:root});check('validador-canonico',canonical.ok,canonical);
const result={id:'FON-01',rodada:1,data:'2026-10-28',metodo:'Verificação de escopo, identidade, completude dos campos e rastreio. Não substitui as leituras humanas/agentes registradas nem certifica ciência ou ausência universal de atos.',ok:checks.every(c=>c.ok),verificacoes:checks.length,falhas:checks.filter(c=>!c.ok),resumo:{artigos:aa.length,artigos_identicos:aa.length-changed.length,registros_CR:rs.length,outros_registros_identicos:noCR.length,pdfs_baseline_preservados:snap.arquivos.filter(s=>s.arquivo.endsWith('.pdf')).length},canonico:canonical,checks};
await fs.writeFile(path.join(base,'verificacao-r1.json'),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({ok:result.ok,verificacoes:result.verificacoes,falhas:result.falhas,resumo:result.resumo,canonico:canonical},null,2));
if(!result.ok)process.exitCode=1;
