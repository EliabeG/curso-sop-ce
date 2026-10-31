/** Fotografia parcial r16, somente leitura; emite JSON ou verifica arquivo. */
import fs from 'node:fs';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
import {parseHtml} from '../../../inventario/validar-inventario.mjs';
const Q='auditoria/termodinamica/evidencias/QA-09/', D=Q+'ledger-r16-parcial-r1/';
const prior=Q+'aplicacao-pressao-fichas-r10-r1/antes-aula.html', aula='modulos/e1-termodinamica.html',form='formulas/termodinamica.html';
const hist='auditoria/termodinamica/pareceres/QA-09-exemplos001-005-diagnosticos26-28-r9-auditoria-independente-20261030.md';
const facts={
 [prior]:'2d6b8fb2f9c99e04d22c19d7b32bbc3eb20577459d9132e506f9c0acef3f2fc2',
 [aula]:'55754bfc631da9010e3c9afc73e3c458e349b535c429fe98abe28998897aab23',
 [form]:'dea4923117d09fa77cabacb0b65816cbf6d57b724d88285003804a1f1440389d',
 [Q+'inventario-r9.json']:'023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d',
 [Q+'inventario-r16.json']:'2c4d4da464488f7eab06b6d56d32d83b27fdbb542aaa1d847a412d18c955cbcd',
 [hist]:'3105042743d37cca09eb65659d43865104f2342537808438eb312cc08d210e06',
 [D+'reconciliacao-ex001-005-d26-28.md']:'0d60c27750ad5fba5991881480c2c6e25f3f30444681b8aa4aada0a89e8122b6',
 'auditoria/termodinamica/inventario/validar-inventario.mjs':'0bd26bcf6288b3bd159ac7c167bfeb4a1a49bbebe784d26a3a93739fcb7790d5'
};
const sha=x=>crypto.createHash('sha256').update(x).digest('hex');
const get=p=>{let x=fs.readFileSync(p);assert.equal(sha(x),facts[p],`SHA divergente: ${p}`);return x.toString('utf8')};
const table=[
 ['EX-001',38690,535,'Uma propriedade que não muda','fundamentos','base-medidas'],
 ['EX-002',41050,553,'Faixa de um transmissor','fundamentos','base-instrumentos'],
 ['EX-003',41765,562,'Interpolar uma leitura','fundamentos','base-instrumentos'],
 ['EX-004',55124,765,'Título a partir da entalpia','substancias','titulo-ex004'],
 ['EX-005',78267,1159,'Escolher unidades compatíveis','substancias','base-gas-modelo'],
 ['D26',536073,6835,'26. Dois estágios','preparacao-questoes',null],
 ['D27',537026,6843,'27. Extração muda','preparacao-questoes','base-misturador-correntes'],
 ['D28',538014,6852,'28. CO₂','preparacao-questoes','base-balanco-co2']
];
const hashctx={
 'base-medidas':'9ec26f2a8b0472711e69319a31d1878257d753ddc930c1f5d748f09ff452d2db',
 'base-instrumentos':'b3c0e3d23219f8da2d815afa35bf328178617539300505de961cc6c26f37ad70',
 'titulo-ex004':'9f03f42941073468e8a0844a7806e53a92903b8ee5523dadbad4ce33a9ea8079',
 'base-gas-modelo':'eac52ff635952b4f0fac43b907bcdb76401d66c9e1eb4cc9cb04a92da1ce2333',
 'base-misturador-correntes':'29175301d686504895499b382234322cd637d8489cda03c621a8ec3e1d0fae75',
 'base-balanco-co2':'ba291f67e38e109fafdc21d96ab47c55992022dd52c31b999ef6cb3922b6a212'};
function context(html,doc,key){let n;
 if(key==='titulo-ex004')n=doc.nodes.find(v=>v.tag==='h4'&&html.slice(v.start,v.end).includes('Título a partir da entalpia'));
 else {assert.equal(doc.ids.get(key)?.length,1,`âncora ausente/duplicada ${key}`); n=doc.ids.get(key)[0]}
 while(n && !(n.tag==='div'&&(n.attrs.class||'').split(/\s+/).includes('bloco-aula')))n=n.parent;
 assert.ok(n,`contêiner ausente ${key}`); return html.slice(n.start,n.end);
}
function build(){
 for(const p of Object.keys(facts))get(p);
 let old=get(prior), cur=get(aula), v9=JSON.parse(get(Q+'inventario-r9.json')),v16=JSON.parse(get(Q+'inventario-r16.json'));
 let d9=parseHtml(old),d16=parseHtml(cur);assert.equal(d9.errors.length,0);assert.equal(d16.errors.length,0);
 for(const [k,h] of Object.entries(hashctx)){let a=context(old,d9,k),b=context(cur,d16,k);assert.equal(a,b,`contexto divergente ${k}`);assert.equal(sha(b),h)}
 const cols=['ocorrencias','referencias','recursos','ativos_especificos'], counts=[11400,816,138,6];assert.deepEqual(cols.map(c=>v16[c].length),counts);
 let rows=table.map(([id,pos,idx,title,secao,ctx])=>{
  const r9=v9.ocorrencias.filter(x=>x.tipo==='exemplo_ou_diagnostico'&&x.arquivo===aula&&x.inicio_utf16===pos);
  assert.equal(r9.length,1,`identidade r9 ${id}`);let u=r9[0],v=v16.ocorrencias[idx];
  assert.equal(v.tipo,u.tipo);assert.equal(v.arquivo,aula);assert.equal(v.secao,secao);assert.equal(u.secao,secao);
  let a=old.slice(u.inicio_utf16,u.fim_utf16),b=cur.slice(v.inicio_utf16,v.fim_utf16);
  assert.ok(a.includes(title)&&b.includes(title));assert.equal(a,b);assert.equal(sha(a),u.sha256_fragmento);assert.equal(sha(b),v.sha256_fragmento);
  assert.equal(v16.ocorrencias.filter(x=>x.tipo===v.tipo&&x.sha256_fragmento===v.sha256_fragmento).length,1,`identidade ambígua ${id}`);
  return {id_local:id,colecao:'ocorrencias',indice_base_zero:idx,identidade_r16:v,identidade_r9:u,
   estado:'conferido_no_escopo_localizado',escopo:'Somente dados, resultados e hipóteses individualizados no relatório de reconciliação; não se aprova automaticamente o contexto nem registros descendentes.',
   contexto:ctx?{id:ctx,sha256:hashctx[ctx]}:{id:'balanço explícito no próprio D26',sha256:v.sha256_fragmento},
   parecer_historico:hist,parecer_historico_sha256:facts[hist],auditor_historico:'/root/next_graphics',
   reconciliacao:D+'reconciliacao-ex001-005-d26-28.md',reconciliacao_sha256:facts[D+'reconciliacao-ex001-005-d26-28.md'],responsavel_revalidacao:'/root/planning'}
 });
 assert.equal(9/.010,900);assert.equal(4.5/.005,900);assert.equal(-10+120,110);assert.equal(10+30/40*(90-10),70);
 assert.equal((900-400)/(2400-400),.25);assert.ok(Math.abs(.082*320/26.24-1)<1e-12);
 assert.equal(600+900-20,1480);assert.equal((600+900-20)/(2400+800),.4625);assert.equal(3200-1480,1720);
 assert.equal((700-300)/(2300-300),.2);assert.equal(8*250,2000);
 assert.ok(Math.abs((.2+500*(.0004-.0006))/200*1e6-500)<1e-9);assert.ok(Math.abs((.0004+.2/500)*1e6-800)<1e-9);
 return {versao:'r16-parcial-r1',data:'2026-10-30',estado_global:'QA09_EM_CORRECAO_NAO_APROVADO',
 fotografia:{[aula]:facts[aula],[form]:facts[form],[Q+'inventario-r16.json']:facts[Q+'inventario-r16.json']},
 colecoes:Object.fromEntries(cols.map((c,i)=>[c,{total:counts[i],estado_padrao:'pendente_de_integracao'}])),registros_explicitamente_revisados:rows,
 limites:['A integração deste lote aguarda auditor independente. Demais ocorrências, referências, recursos e ativos permanecem pendentes de integração, sem apagar revisões históricas.',
 'Os oito blocos são avaliados exclusivamente no alcance do relatório; nós subordinados e contextos permanecem pendentes como registros separados.',
 'A igualdade de hash é apenas verificação de identidade; a revalidação individual examinou condições, contas e fontes no relatório.',
 'As coleções se sobrepõem; não são contagem de cálculos nem percentual de conclusão.',
 'Os 197 artigos são tratados separadamente; nenhum aceite é automaticamente estendido a esta fotografia.']};
}
try {let x=build(); if(process.argv.length===2)process.stdout.write(JSON.stringify(x,null,2)+'\n');
 else {assert.equal(process.argv.length,4);assert.equal(process.argv[2],'--verificar');assert.deepEqual(JSON.parse(fs.readFileSync(process.argv[3],'utf8')),x);console.log(JSON.stringify({ok:true,registros_integrados:x.registros_explicitamente_revisados.length,estado_padrao:'pendente_de_integracao',qa09:'em correção'}))}
} catch(e){console.error('ERRO:',e.message);process.exitCode=1}
