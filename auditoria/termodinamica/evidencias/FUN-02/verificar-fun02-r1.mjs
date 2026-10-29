/** FUN-02: integridade, alcance e reprodução; não é parecer científico. */
import fs from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
import {parseHtml,isInventoryArticle,validateInventory,decodeHtml} from '../../inventario/validar-inventario.mjs';
import {calcularFun02} from '../../../../assets/termodinamica/fun02-calculos-v1.mjs';
const root=fileURLToPath(new URL('../../../../',import.meta.url));
const dir='auditoria/termodinamica/evidencias/FUN-02/';
const sha=x=>createHash('sha256').update(x).digest('hex');
export async function verificarFun02(){
  const checks=[],read=p=>fs.readFile(root+p,'utf8');
  const check=(nome,ok)=>{checks.push({nome,ok});if(!ok)throw new Error(nome);};
  const before=await read(dir+'e1-termodinamica.antes.html'),html=await read('modulos/e1-termodinamica.html'),unit=await read(dir+'unidade-integrada-r1.html');
  check('unidade inserida uma vez',html.split(unit).length===2);
  let restored=html.replace(unit,'');
  const menu='\n<li><a href="#fun02-diferenciais-caminhos">4.1. Diferenciais, caminhos e propriedades</a></li>';
  check('link único de sumário',restored.split(menu).length===2);restored=restored.replace(menu,'');
  const deltas=JSON.parse(await read(dir+'gov-deltas-r1.json'));
  check('seis linhas de integração curricular delimitadas',deltas.map(d=>d.id).join(',')==='c01,c02,c03,c08,c09,c10');
  for(const d of deltas){check('linha atual '+d.id,restored.includes(d.depois));restored=restored.replace(d.depois,d.antes);}
  check('reconstrução integral da fonte aprovada',restored===before);
  const doc=parseHtml(html),oldDoc=parseHtml(before),udoc=parseHtml(unit);
  const oldArticles=oldDoc.nodes.filter(isInventoryArticle),newArticles=doc.nodes.filter(isInventoryArticle);
  check('194 anteriores e197 atuais',oldArticles.length===194&&newArticles.length===197);
  for(const a of oldArticles){const b=doc.ids.get(a.attrs.id);check('artigo preservado '+a.attrs.id,b?.length===1&&html.slice(b[0].start,b[0].end)===before.slice(a.start,a.end));}
  check('IDs únicos',[...doc.ids.values()].every(n=>n.length===1));
  for(const n of udoc.nodes)if(n.attrs.href?.startsWith('#'))check('âncora '+n.attrs.href,doc.ids.get(n.attrs.href.slice(1))?.length===1);
  for(const table of udoc.nodes.filter(n=>n.tag==='table')){const inside=n=>n.start>table.start&&n.end<table.end;check('tabela acessível',table.attrs.class==='tabela'&&udoc.nodes.some(n=>n.tag==='caption'&&inside(n))&&udoc.nodes.filter(n=>n.tag==='th'&&inside(n)).every(n=>n.attrs.scope)&&udoc.nodes.filter(n=>n.tag==='td'&&inside(n)).every(n=>n.attrs['data-rotulo']));}
  const inv=JSON.parse(await read('auditoria/termodinamica/inventario/inventario-questoes.json')),oldInv=JSON.parse(await read(dir+'inventario.antes.json'));
  check('194 registros anteriores idênticos',oldInv.itens.length===194&&oldInv.itens.every((i,n)=>JSON.stringify(i)===JSON.stringify(inv.itens[n])));
  for(const item of inv.itens.slice(194)){
    const article=doc.ids.get(item.id)[0],h3=doc.nodes.find(n=>n.tag==='h3'&&n.start>article.start&&n.end<article.end);
    const title=decodeHtml(html.slice(h3.openEnd,h3.end).replace(/<[^>]*>/g,'').replace(/\s+/g,' ')).trim();
    check('título corresponde ao publicado '+item.id,item.titulo===title);
  }
  const fixed={
    'assets/registro.js':'444a13658e0b869760296826be30267215293b18c3074f283b2a1ea252e828a2',
    'assets/curso.js':'81728c9fd1e96b738410e6b51cf4ab3ed785fb17753e68a988c1dcf236d8f899',
    'assets/curso.css':'b8ded6abc4548f378daab2e299a8a55ba81e8841c41049133a84d93848ee3eaa',
    'assets/termodinamica/fun01-dados-v1.json':'a73b4d6140219cbd6b005216bb7a44db0a68b05f21ca51b7ac4b1ca782dd1448',
    'assets/termodinamica/fun01-calculos-v1.mjs':'a0fbdc4e6e7291a563db2362d26f4107ad67f56843e741d96eef8eea5a8d2a88',
    'auditoria/termodinamica/inventario/inventario.schema.json':'c71033464d54e71e61d4dcbae56847a88720e5ff937c1e1f7179005ab22d149b',
    'auditoria/termodinamica/inventario/validar-inventario.mjs':'ddc8a6831422a868fb5a8b15b2f6653325f6644acf4f5c64dbf35bb0d2369fdd',
    'auditoria/termodinamica/inventario/LEIA-ME.md':'cdcd7e965bdc4a998b6e2fa784a53f84f295abcf9ade2d06ce62fff71d072449'
  };
  for(const[file,hash]of Object.entries(fixed))check('arquivo preservado '+file,sha(await fs.readFile(root+file))===hash);
  const validacao=await validateInventory({rootDir:root});check('inventário canônico válido',validacao.ok);
  const calculos=calcularFun02(JSON.parse(await read('assets/termodinamica/fun02-dados-v1.json')));check('49 verificações de reprodução',calculos.testes.length===49);
  return {ok:true,sha256_html:sha(html),verificacoes:checks.length,checks,validacao,calculos,alcance:'Estrutura, preservação e consistência numérica. Não substitui auditoria científica/pedagógica nem piloto.'};
}
