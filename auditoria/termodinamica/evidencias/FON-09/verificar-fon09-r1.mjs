/** Integridade e conversões FON-09; a leitura das fontes é documentada separadamente. */
import fs from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
import {parseHtml,isInventoryArticle,decodeHtml,validateInventory} from '../../inventario/validar-inventario.mjs';
const root=fileURLToPath(new URL('../../../../',import.meta.url));
const dir='auditoria/termodinamica/evidencias/FON-09/';
const sha=x=>createHash('sha256').update(x).digest('hex');
const normal=s=>decodeHtml(s.replace(/<[^>]*>/g,'')).replace(/[ \t\n\r\f\v\u00a0]+/g,' ').trim();
function digital(html,id){
  const d=parseHtml(html),a=d.ids.get(id)[0],inside=n=>n.start>a.start&&n.end<a.end;
  const e=d.nodes.find(n=>inside(n)&&(n.attrs.class||'').split(' ').includes('cr-enunciado'));
  const parts=[normal(html.slice(e.openEnd,e.end))];
  for(const im of d.nodes.filter(n=>n.tag==='img'&&n.start>e.start&&n.end<e.end))parts.push(im.attrs.src||'',im.attrs.alt||'');
  for(const input of d.nodes.filter(n=>inside(n)&&n.tag==='input'&&n.attrs.type==='radio')){
    const label=d.nodes.find(n=>n.tag==='label'&&n.start<input.start&&n.end>input.end);
    parts.push(input.attrs.value,normal(html.slice(label.openEnd,label.end)));
  }
  parts.push(a.attrs['data-cr-gabarito']);
  let h=0x811c9dc5;for(const c of parts.join('␞')){h^=c.codePointAt(0);h=Math.imul(h,0x01000193)>>>0;}
  return h.toString(16).padStart(8,'0');
}
export async function verificarFon09(){
  const checks=[],read=p=>fs.readFile(root+p,'utf8');
  const check=(nome,ok)=>{checks.push({nome,ok});if(!ok)throw new Error(nome);};
  const html=await read('modulos/e1-termodinamica.html'),before=await read(dir+'antes/modulos/e1-termodinamica.html');
  const doc=parseHtml(html),old=parseHtml(before),id='cr-e1-68',a=doc.ids.get(id)[0],b=old.ids.get(id)[0];
  const raw=html.slice(a.start,a.end),oldraw=before.slice(b.start,b.end);
  check('somente CR68 mudou no HTML',html.slice(0,a.start)+oldraw+html.slice(a.end)===before);
  const arts=doc.nodes.filter(isInventoryArticle),oldarts=old.nodes.filter(isInventoryArticle);
  check('197 artigos e IDs únicos',arts.length===197&&oldarts.length===197&&[...doc.ids.values()].every(ns=>ns.length===1));
  for(const n of oldarts.filter(n=>n.attrs.id!==id)){const c=doc.ids.get(n.attrs.id)[0];check('artigo preservado '+n.attrs.id,html.slice(c.start,c.end)===before.slice(n.start,n.end));}
  const en=doc.ids.get('cr-e1-68-enunciado')[0],oen=old.ids.get('cr-e1-68-enunciado')[0],historic=doc.ids.get('cr-e1-68-transcricao')[0];
  check('transcrição integral preservada',html.slice(en.start,en.end)===before.slice(oen.start,oen.end));
  check('transcrição recolhida e identificada',historic.tag==='details'&&!('open' in historic.attrs)&&en.start>historic.start&&en.end<historic.end&&raw.includes('Transcrição histórica com dados inválidos'));
  const sel=(d,h,cl)=>{const n=d.nodes.find(n=>n.start>d.ids.get(id)[0].start&&n.end<d.ids.get(id)[0].end&&(n.attrs.class||'').split(' ').includes(cl));return h.slice(n.start,n.end);};
  check('alternativas preservadas',sel(doc,html,'cr-alternativas')===sel(old,before,'cr-alternativas'));
  check('resolução preservada',sel(doc,html,'cr-resolucao')===sel(old,before,'cr-resolucao'));
  const assertion=sel(old,before,'cr-afirmacao');check('afirmação ativa fora do histórico',raw.includes(assertion)&&html.indexOf(assertion,a.start)<historic.start);
  check('gabarito C preservado',a.attrs['data-cr-gabarito']==='C'&&b.attrs['data-cr-gabarito']==='C');
  const oldDigital=digital(before,id),newDigital=digital(html,id);check('digitalDoBanco preservada',oldDigital===newDigital);
  check('registro.js preservado',await read('assets/registro.js')===await read(dir+'antes/assets/registro.js'));
  const inv=JSON.parse(await read('auditoria/termodinamica/inventario/inventario-questoes.json')),oi=JSON.parse(await read(dir+'antes/auditoria/termodinamica/inventario/inventario-questoes.json'));
  check('197 registros',inv.itens.length===197&&oi.itens.length===197);
  for(const item of oi.itens.filter(x=>x.id!==id))check('registro preservado '+item.id,JSON.stringify(item)===JSON.stringify(inv.itens.find(x=>x.id===item.id)));
  const ni=inv.itens.find(x=>x.id===id),oldi=oi.itens.find(x=>x.id===id);
  for(const field of ['titulo','formato','competencias','pre_requisitos','nivel','raciocinio','vinculo_competencias','exposicao_previa'])check('campo cognitivo preservado '+field,JSON.stringify(ni[field])===JSON.stringify(oldi[field]));
  const summary=await read('auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md'),oldsummary=await read(dir+'antes/auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md');
  check('197 linhas de resumo preservadas',oldsummary.split('\n').filter(l=>l.startsWith('| [')).every(l=>summary.includes(l)));
  const data=JSON.parse(await read('assets/termodinamica/fon09-cr68-dados-v1.json'));
  check('cinco pressões e versão',data.versao==='1.0'&&data.saturacao.map(r=>r.p_kPa).join(',')==='101.325,150,200,250,300');
  for(const r of data.saturacao){
    if(r.fonte_original){check('conversões SI '+r.p_kPa,Math.abs(r.fonte_original.p_MPa*1000-r.p_kPa)<1e-10&&Math.abs(r.fonte_original.vf_cm3g*0.001-r.correto.vf_m3kg)<1e-12&&Math.abs(r.fonte_original.vg_cm3g*0.001-r.correto.vg_m3kg)<1e-12);}
    for(const k of ['T_C','vf_m3kg','vg_m3kg']){const orig=r.original[k],places=(orig.split('.')[1]||'').length;const delta=Number(orig)-r.correto[k];check('comparação de precisão '+r.p_kPa+' '+k,Math.abs(delta-r.comparacao[k].diferenca_original_menos_referencia)<1e-12&&r.comparacao[k].classificacao===(Math.abs(delta)<=0.5*10**(-places)?'compativel_com_arredondamento':'incompativel_com_precisao_publicada'));}
    for(const [key,value]of Object.entries(r.exibicao))check('valor publicado '+r.p_kPa+' '+key,raw.includes('>'+value+'</td>'));
  }
  check('2 compatíveis e13 incompatíveis',data.saturacao.flatMap(r=>Object.values(r.comparacao)).filter(x=>x.classificacao==='compativel_com_arredondamento').length===2);
  check('conversão da densidade literal',1000*data.conversoes.kg_por_cm3_para_kg_por_m3===data.densidade.valor_literal_kgm3);
  check('desvio da aproximação de densidade',Math.abs(100*(1000/data.densidade.referencia_fisica.rho_kgm3-1)-data.densidade.modelo_editorial_aproximado.erro_relativo_porcento)<1e-12);
  for(const src of data.fontes.filter(f=>f.sha256_captura))check('captura primária '+src.id,sha(await fs.readFile(root+src.captura))===src.sha256_captura);
  for(const src of data.fontes.filter(f=>f.arquivo_local))check('PDF fonte '+src.id,sha(await fs.readFile(root+src.arquivo_local))===src.sha256);
  const sat=await read(dir+'apoio-webbook-saturacao-101325.html'),rho=await read(dir+'apoio-webbook-densidade-25c-101325.html');
  for(const value of ['99.974296','0.10132500','0.0010434411','1.6732012'])check('valor na fonte WebBook '+value,sat.includes('>'+value+'</td>'));
  check('densidade na condição consultada',rho.includes('>25.000000</td>')&&rho.includes('>0.10132500</td>')&&rho.includes('>997.04764</td>'));
  for(const [file,hash]of Object.entries({'assets/curso.js':'81728c9fd1e96b738410e6b51cf4ab3ed785fb17753e68a988c1dcf236d8f899','assets/curso.css':'b8ded6abc4548f378daab2e299a8a55ba81e8841c41049133a84d93848ee3eaa','auditoria/termodinamica/inventario/inventario.schema.json':'c71033464d54e71e61d4dcbae56847a88720e5ff937c1e1f7179005ab22d149b'}))check('infraestrutura preservada '+file,sha(await fs.readFile(root+file))===hash);
  check('validador com ajuste PDF autorizado',sha(await fs.readFile(root+'auditoria/termodinamica/inventario/validar-inventario.mjs'))==='114b1a063cb2a88e505c9ecffd2b22c75f29b709419b24e9e533331fa7283b22');
  const validacao=await validateInventory({rootDir:root});check('inventário canônico',validacao.ok);
  return {id:'FON-09',rodada:1,ok:true,sha256_html:sha(html),verificacoes:checks.length,checks,digital_cr68:{antes:oldDigital,depois:newDigital,registro_js:'inalterado; mapa das30questões iniciais'},validacao,alcance:'Estrutura, identidade, preservação e conversões. A conferência documental/científica está em relatórios separados; não é parecer independente.'};
}
