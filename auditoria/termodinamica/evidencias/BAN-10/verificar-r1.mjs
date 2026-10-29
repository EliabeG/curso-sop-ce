import fs from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import {parseHtml,isInventoryArticle,decodeHtml,sha256,validateInventory} from '../../inventario/validar-inventario.mjs';
import {testarComportamento} from './testar-comportamento-r1.mjs';
const root=fileURLToPath(new URL('../../../../',import.meta.url));
const dir='auditoria/termodinamica/evidencias/BAN-10/';
const norm=s=>decodeHtml(s.replace(/<[^>]*>/g,'')).replace(/[ \t\n\r\f\v\u00a0]+/g,' ').trim();
const cls=(n,c)=>(n.attrs.class||'').split(/\s+/).includes(c);
function parts(doc,a){
  const inside=n=>n.start>a.start&&n.end<a.end,find=c=>doc.nodes.find(n=>inside(n)&&cls(n,c));
  const e=find('cr-enunciado'),p=[norm(doc.html.slice(e.openEnd,e.end))];
  for(const n of doc.nodes.filter(n=>n.tag==='img'&&n.start>e.start&&n.end<e.end))p.push(n.attrs.src||'',n.attrs.alt||'');
  for(const r of doc.nodes.filter(n=>inside(n)&&n.tag==='input'&&n.attrs.type==='radio')){const label=doc.nodes.find(n=>n.tag==='label'&&n.start<r.start&&n.end>r.end);p.push(r.attrs.value,norm(doc.html.slice(label.openEnd,label.end)));}
  p.push(a.attrs['data-cr-gabarito']);let h=0x811c9dc5;for(const c of p.join('␞')){h^=c.codePointAt(0);h=Math.imul(h,0x01000193)>>>0;}
  return {enunciado:doc.html.slice(e.start,e.end),alternativas:p.slice(1,-1),gabarito:p.at(-1),digital:h.toString(16).padStart(8,'0')};
}
export async function verificar(){
  const checks=[],check=(nome,ok)=>{checks.push({nome,ok});if(!ok)throw Error(nome);},read=p=>fs.readFile(root+p,'utf8');
  const h=await read('modulos/e1-termodinamica.html'),b=await read(dir+'antes/e1-termodinamica.html'),doc=parseHtml(h),old=parseHtml(b),dec=JSON.parse(await read(dir+'decisoes-r1.json')),affected=new Set(dec.itens.map(x=>x.id));
  const arts=doc.nodes.filter(isInventoryArticle),oldarts=old.nodes.filter(isInventoryArticle),triage=JSON.parse(await read(dir+'triagem-apoio-r1.json'));
  check('197 artigos/IDs e ausência de duplicação de IDs',arts.length===197&&oldarts.length===197&&[...doc.ids.values()].every(v=>v.length===1));
  check('triagem individual cobre exatamente197 da base',triage.itens.length===197&&new Set(triage.itens.map(x=>x.id)).size===197&&oldarts.every(a=>triage.itens.some(x=>x.id===a.attrs.id&&x.sha256_artigo_lido===sha256(b.slice(a.start,a.end)))));
  const identity=[];
  for(const a of oldarts){const current=doc.ids.get(a.attrs.id)[0];if(!affected.has(a.attrs.id))check('artigo preservado '+a.attrs.id,h.slice(current.start,current.end)===b.slice(a.start,a.end));
    if(cls(a,'concurso-item')||cls(a,'avalia-item')){const before=parts(old,a),after=parts(doc,current);check('identidade semântica original '+a.attrs.id,JSON.stringify(before)===JSON.stringify(after));identity.push({id:a.attrs.id,digital_antes:before.digital,digital_depois:after.digital});}}
  check('nove exclusões e71 pontuáveis no CR',arts.filter(a=>a.attrs['data-cr-avaliacao']==='estudo-critico').map(a=>a.attrs.id).sort().join(',')===dec.criticos.slice().sort().join(',')&&dec.criticos.length===9);
  for(const id of dec.criticos){const a=doc.ids.get(id)[0],raw=h.slice(a.start,a.end);check('roteiro e autocorreção sem nota '+id,raw.includes('Roteiro autoral de estudo crítico')&&raw.includes('Critério de autocorreção, sem nota')&&raw.includes('sem pontuação'));}
  for(const id of ['cr-e1-51','cr-e1-55','cr-e1-68'])check('retenção deliberada '+id,!doc.ids.get(id)[0].attrs['data-cr-avaliacao']);
  for(const id of ['cr-e1-68-dados-corrigidos','cr-e1-68-transcricao']){const a=doc.ids.get(id)[0],o=old.ids.get(id)[0];let raw=h.slice(a.start,a.end);check('FON09 conteúdo integral preservado '+id,raw===b.slice(o.start,o.end));}
  const snapshot=JSON.parse(await read(dir+'snapshot-antes.json'));for(const p of snapshot.filter(p=>['assets/registro.js','assets/curso.css'].includes(p.arquivo)))check('arquivo compartilhado intacto '+p.arquivo,sha256(await fs.readFile(root+p.arquivo))===p.sha256);
  check('dados FON09 intactos',sha256(await fs.readFile(root+'assets/termodinamica/fon09-cr68-dados-v1.json'))==='828b967f1318924742e8b30aca8575549301afcccaad395f9ed5bcee2fc46456');
  const js=await read('assets/curso.js'),oldjs=await read(dir+'antes/curso.js'),cut=s=>{const a=s.indexOf('  function iniciarBanco(secao,'),b=s.indexOf('  function iniciarQuestoes()',a);return [s.slice(0,a),s.slice(a,b),s.slice(b)];},j=cut(js),oj=cut(oldjs);
  check('JS restrito a iniciarBanco',j[0]===oj[0]&&j[2]===oj[2]);
  const inventory=JSON.parse(await read('auditoria/termodinamica/inventario/inventario-questoes.json')),oi=JSON.parse(await read(dir+'antes/inventario-questoes.json'));
  for(const x of oi.itens.filter(x=>!affected.has(x.id)))check('registro preservado '+x.id,JSON.stringify(x)===JSON.stringify(inventory.itens.find(y=>y.id===x.id)));
  for(const c of dec.itens){const a=doc.ids.get(c.id)[0];check('hash da decisão sincronizado '+c.id,c.sha256_artigo_depois===sha256(h.slice(a.start,a.end)));for(const f of c.fontes_oficiais)check('documento conferido '+c.id+' '+f.arquivo,sha256(await fs.readFile(root+f.arquivo))===f.sha256);}
  const validacao=await validateInventory({rootDir:root});check('validador canônico limpo',validacao.ok&&validacao.erros.length===0);
  const comportamento=await testarComportamento();check('comportamento dinâmico',comportamento.ok);
  return {id:'BAN-10',rodada:1,ok:true,verificacoes:checks.length,checks,identidades_bancos:identity,validacao,comportamento,sha256:{html:sha256(h),js:sha256(js)},limites:'Integridade, identidades, contratos e função real com ambiente controlado. Triagem, fontes/científica e navegador têm evidências separadas; não certifica aprendizagem nem auditoria global BAN07/08/FON01.'};
}
