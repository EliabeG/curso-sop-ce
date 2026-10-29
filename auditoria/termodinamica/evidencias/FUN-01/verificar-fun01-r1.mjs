/** Verificação documental FUN-01 r1; não substitui parecer científico independente. */
import fs from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
import {parseHtml,isInventoryArticle,validateInventory} from '../../inventario/validar-inventario.mjs';
import {calcularFun01} from '../../../../assets/termodinamica/fun01-calculos-v1.mjs';
const root=fileURLToPath(new URL('../../../../',import.meta.url));
const sha=x=>createHash('sha256').update(x).digest('hex');
const dir='auditoria/termodinamica/evidencias/FUN-01/';
export async function verificarFun01() {
  const checks=[];
  const read=p=>fs.readFile(root+p,'utf8');
  const check=(nome,ok)=>{checks.push({nome,ok});if(!ok)throw new Error(nome);};
  const html=await read('modulos/e1-termodinamica.html');
  const before=await read(dir+'e1-termodinamica.antes.html');
  const unit=await read(dir+'unidade-integrada-r1.html');
  const deltas=JSON.parse(await read(dir+'gov-deltas-r1.json'));
  check('unidade inserida uma única vez',html.split(unit).length===2);
  let restored=html.replace(unit,'');
  const menu='\n<li><a href="#fun01-estado-equilibrio">3.1. Estado, equilíbrio e graus de liberdade</a></li>';
  check('link de sumário único',restored.split(menu).length===2);
  restored=restored.replace(menu,'');
  check('somente seis competências autorizadas',deltas.map(d=>d.id).join(',')==='c01,c02,c07,c08,c09,c10');
  for(const d of deltas){check(`células atuais ${d.id}`,restored.includes(d.depois));restored=restored.replace(d.depois,d.antes);}
  check('restauração integral da fonte anterior após retirar somente deltas autorizados',restored===before);
  const oldDoc=parseHtml(before),doc=parseHtml(html);
  const oldArticles=oldDoc.nodes.filter(isInventoryArticle),allArticles=doc.nodes.filter(isInventoryArticle);
  check('190 artigos anteriores e 194 atuais',oldArticles.length===190 && allArticles.length===194);
  for(const old of oldArticles){const current=doc.ids.get(old.attrs.id);check(`preservação ${old.attrs.id}`,current?.length===1 && html.slice(current[0].start,current[0].end)===before.slice(old.start,old.end));}
  check('nenhum ID HTML duplicado',[...doc.ids.values()].every(nodes=>nodes.length===1));
  const unitDoc=parseHtml(unit);
  for(const n of unitDoc.nodes) if(n.attrs.href?.startsWith('#')) check(`âncora ${n.attrs.href}`,doc.ids.get(n.attrs.href.slice(1))?.length===1);
  for(const table of unitDoc.nodes.filter(n=>n.tag==='table')){
    const inside=n=>n.start>table.start && n.end<table.end;
    check('tabela com padrão responsivo e caption',table.attrs.class==='tabela'&&unitDoc.nodes.some(n=>n.tag==='caption'&&inside(n)));
    check('cabeçalhos e rótulos de células',unitDoc.nodes.filter(n=>n.tag==='th'&&inside(n)).every(n=>n.attrs.scope)&&unitDoc.nodes.filter(n=>n.tag==='td'&&inside(n)).every(n=>n.attrs['data-rotulo']));
  }
  const oldInventory=JSON.parse(await read(dir+'inventario.antes.json')),inventory=JSON.parse(await read('auditoria/termodinamica/inventario/inventario-questoes.json'));
  check('190 registros anteriores idênticos',oldInventory.itens.length===190 && oldInventory.itens.every((i,n)=>JSON.stringify(i)===JSON.stringify(inventory.itens[n])));
  check('quatro registros acrescentados',inventory.itens.length===194 && inventory.itens.slice(190).every(i=>i.banco==='aberto'&&i.formato.tipo==='resposta_aberta'));
  const shared={
    'assets/registro.js':'444a13658e0b869760296826be30267215293b18c3074f283b2a1ea252e828a2',
    'assets/curso.js':'81728c9fd1e96b738410e6b51cf4ab3ed785fb17753e68a988c1dcf236d8f899',
    'assets/curso.css':'b8ded6abc4548f378daab2e299a8a55ba81e8841c41049133a84d93848ee3eaa',
    'auditoria/termodinamica/inventario/inventario.schema.json':'c71033464d54e71e61d4dcbae56847a88720e5ff937c1e1f7179005ab22d149b',
    'auditoria/termodinamica/inventario/validar-inventario.mjs':'ddc8a6831422a868fb5a8b15b2f6653325f6644acf4f5c64dbf35bb0d2369fdd',
    'auditoria/termodinamica/inventario/LEIA-ME.md':'cdcd7e965bdc4a998b6e2fa784a53f84f295abcf9ade2d06ce62fff71d072449'
  };
  for(const [file,expected] of Object.entries(shared))check(`arquivo preservado ${file}`,sha(await fs.readFile(root+file))===expected);
  const validacao=await validateInventory({rootDir:root});check('inventário estrutural válido',validacao.ok);
  const contas=calcularFun01(JSON.parse(await read('assets/termodinamica/fun01-dados-v1.json')));
  check('28 verificações numéricas',contas.testes.length===28);
  return {ok:true,alcance:'Preservação, estrutura, vínculos e consistência numérica. Sem aceite científico automático.',sha256_html:sha(html),verificacoes:checks.length,checks,validacao,calculos:contas};
}
