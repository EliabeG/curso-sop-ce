import fs from 'node:fs/promises';
import crypto from 'node:crypto';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {parseHtml,decodeHtml,isInventoryArticle,validateInventory} from '../../inventario/validar-inventario.mjs';
const dir=path.dirname(fileURLToPath(import.meta.url));
const root=path.resolve(dir,'../../../..');
const sha=s=>crypto.createHash('sha256').update(s).digest('hex');
const read=p=>fs.readFile(path.join(root,p),'utf8');
const strip=s=>decodeHtml(s.replace(/<[^>]*>/g,' ')).replace(/\s+/g,' ').trim();
export async function verificar(){
 const checks=[]; const check=(nome,pass,detalhe)=>checks.push({nome,ok:!!pass,...(detalhe===undefined?{}:{detalhe})});
 const form=await read('formulas/termodinamica.html');const old=await fs.readFile(path.join(dir,'antes/formulas/termodinamica.html'),'utf8');
 const aula=await read('modulos/e1-termodinamica.html');const aulaOld=await fs.readFile(path.join(dir,'antes/modulos/e1-termodinamica.html'),'utf8');
 const d=parseHtml(form),b=parseHtml(old),ad=parseHtml(aula),ab=parseHtml(aulaOld);
 const cards=d.nodes.filter(n=>n.attrs.class==='formula-card'),base=b.nodes.filter(n=>n.attrs.class==='formula-card');
 check('100 fichas e IDs preservados',cards.length===100&&JSON.stringify(cards.map(x=>x.attrs.id))===JSON.stringify(base.map(x=>x.attrs.id)));
 check('11 grupos preservados',new Set(cards.map(x=>x.attrs['data-grupo'])).size===11&&cards.every((x,i)=>x.attrs['data-grupo']===base[i].attrs['data-grupo']));
 check('IDs únicos no formulário',[...d.ids.values()].every(x=>x.length===1));
 for(const n of cards){const html=form.slice(n.start,n.end);const prev=base.find(x=>x.attrs.id===n.attrs.id);const phtml=old.slice(prev.start,prev.end);const cd=parseHtml(html);const maths=html.match(/<math\b[\s\S]*?<\/math>/g)||[];
  check(n.attrs.id+': MathML preservado',JSON.stringify(maths)===JSON.stringify(phtml.match(/<math\b[\s\S]*?<\/math>/g)||[]));
  for(const kind of ['condicao','simbolos']){const el=cd.nodes.find(x=>kind==='condicao'?x.attrs.class==='formula-condicao':x.tag==='p'&&x.attrs.id?.startsWith('simbolos-'));check(n.attrs.id+': busca '+kind,!!el&&n.attrs['data-busca'].includes(strip(html.slice(el.start,el.end))));}
  for(const l of cd.nodes.filter(x=>x.attrs.class==='formula-aula')){const [p,id]=l.attrs.href.split('#');check(n.attrs.id+': vínculo '+id,p==='../modulos/e1-termodinamica.html'&&!!ad.ids.get(id));}
 }
 for(const n of d.nodes){for(const attr of ['aria-labelledby','aria-describedby','aria-controls'])if(n.attrs[attr])for(const id of n.attrs[attr].split(/\s+/))check('ARIA '+id,d.ids.has(id));}
 const art=ad.nodes.filter(isInventoryArticle),aold=ab.nodes.filter(isInventoryArticle);check('197 artigos byte a byte',art.length===197&&aold.length===197&&art.every(n=>{const p=aold.find(x=>x.attrs.id===n.attrs.id);return p&&aula.slice(n.start,n.end)===aulaOld.slice(p.start,p.end)}));
 for(const id of ['fun01-estado-equilibrio','fun02-diferenciais-caminhos']){const a=ad.ids.get(id)[0],z=ab.ids.get(id)[0];check(id+' integral preservada',aula.slice(a.start,a.end)===aulaOld.slice(z.start,z.end));}
 const inv=JSON.parse(await read('auditoria/termodinamica/inventario/inventario-questoes.json'));const invOld=JSON.parse(await fs.readFile(path.join(dir,'antes/auditoria/termodinamica/inventario/inventario-questoes.json'),'utf8'));
 check('197 registros intactos',JSON.stringify(inv.itens)===JSON.stringify(invOld.itens));const norm=x=>({...x,fonte:{...x.fonte,sha256:'HASH',snapshot:'SNAPSHOT'}});check('Inventário: somente hash e snapshot globais',JSON.stringify(norm(inv))===JSON.stringify(norm(invOld)));
 const expected=JSON.parse(await fs.readFile(path.join(dir,'deltas-aula-r1.json'),'utf8'));let replay=aulaOld;for(const x of expected){check('Delta único '+x.ancora,replay.split(x.antes).length===2);replay=replay.replace(x.antes,x.depois);}check('Aula somente deltas declarados',replay===aula);
 const edits=JSON.parse(await fs.readFile(path.join(dir,'deltas-fichas-r1.json'),'utf8'));replay=old;for(const x of edits){check('Hash/delta '+x.id,sha(x.antes)===x.sha256_antes&&sha(x.depois)===x.sha256_depois&&replay.includes(x.antes));replay=replay.replace(x.antes,x.depois);}check('Formulário somente 61 deltas declarados',edits.length===61&&replay===form);
 for(const p of ['assets/formulario-e1.js','assets/formulario-e1.css','auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md'])check('Preservado '+p,await read(p)===await fs.readFile(path.join(dir,'antes',p),'utf8'));
 const shared={'assets/curso.js':'6a450cbfb7049b22e999e3390238fec511c2da24caa3e228871c5a3128121de6','assets/registro.js':'444a13658e0b869760296826be30267215293b18c3074f283b2a1ea252e828a2','assets/curso.css':'b8ded6abc4548f378daab2e299a8a55ba81e8841c41049133a84d93848ee3eaa'};for(const[p,h]of Object.entries(shared))check('Compartilhado intacto '+p,sha(await fs.readFile(path.join(root,p)))===h);
 const perto=(a,b,tol=1e-9)=>Math.abs(a-b)<=tol*Math.max(1,Math.abs(b));
 check('30: unidades mecânicas',perto(2*(20**2-10**2)/2,300)&&perto(2*9.81*(5-1),78.48));
 check('39: energia potencial impede inferência só pela primeira lei',perto(0-0-0-10,-10),'Q=W=ΔEc=0, ΔEp=10 J dá ΔU=-10 J; é identidade de balanço, não construção de processo físico.');
 check('51: entalpia constante versus média',perto((2*300+2*500)/4,400)&&!perto(400,300),'Se h de entrada varia, a integral produz média ponderada; não o primeiro valor.');
 check('64: duas temperaturas não se cancelam com calor líquido',perto(100/500-100/250,-.2)&&100-100===0);
 const h=[200,210,3000,2200];const wt=h[2]-h[3],wb=h[1]-h[0],qin=h[2]-h[1],qout=h[3]-h[0];check('79: quatro balanços e fechamento do ciclo',perto(qin-qout,wt-wb)&&perto((wt-wb)/qin,790/2790));
 const a=2/7,p1=1,p3=16,w=pi=>Math.pow(pi/p1,a)+Math.pow(p3/pi,a)-2;check('88: igualdade das razões e mínimo',perto(4/1,16/4)&&w(4)<w(2)&&w(4)<w(8));
 for(const n of [.8,1.3]){const R=.287,T=300,pA=100,pB=400,N=10000,dp=(pB-pA)/N;let integral=0;for(let i=0;i<N;i++){const p=pA+(i+.5)*dp;integral+=R*T/pA*Math.pow(pA/p,1/n)*dp;}const f=n/(n-1)*R*T*(Math.pow(pB/pA,(n-1)/n)-1);check('89: integral vdp n='+n,perto(integral,f,1e-7));}
 check('92: gradiente negativo e calor positivo',perto((40-60)/.1,-200)&&perto(-.5*((40-60)/.1)*3,300));
 check('95: resistência cilíndrica não vira plana por conversão de área',!perto(Math.log(2)/(2*Math.PI),1/(2*Math.PI)));
 check('96: calor radiativo positivo ao sair',5.67e-8*.8*(400**4-300**4)>0&&5.67e-8*.8*(300**4-400**4)<0);
 check('98: pequena variação relativa no exemplo',perto(1e-5*80,.0008));
 check('99: geração por volume e convecção por face',perto(200*6/(20*6),10));
 const inventory=await validateInventory({rootDir:root});check('Validador canônico',inventory.ok);
 return {id:'FOR-01',rodada:1,data:'2026-10-28',ok:checks.every(x=>x.ok),total:checks.length,falhas:checks.filter(x=>!x.ok),checks,inventario:inventory,limite:'Verificação estrutural, preservação e contas autorais seletivas dos pontos alterados. A revisão científica dos 100 é registrada separadamente; não há teste com estudantes nem prova automática de todos os modelos.'};
}
