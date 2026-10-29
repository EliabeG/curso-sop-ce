import fs from 'node:fs/promises';
import crypto from 'node:crypto';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {parseHtml,decodeHtml,isInventoryArticle,validateInventory} from '../../inventario/validar-inventario.mjs';
const dir=path.dirname(fileURLToPath(import.meta.url)),root=path.resolve(dir,'../../../..');
const read=p=>fs.readFile(path.join(root,p),'utf8');
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const strip=s=>decodeHtml(s.replace(/<[^>]*>/g,' ')).replace(/\s+/g,' ').trim();
export async function verificar(){
 const checks=[];const check=(nome,ok,detalhe)=>checks.push({nome,ok:!!ok,...(detalhe===undefined?{}:{detalhe})});
 const base='auditoria/termodinamica/evidencias/FOR-01/';
 const manifestRaw=await read(base+'manifesto-r1.json'),manifest=JSON.parse(manifestRaw);
 check('Manifesto r1 imutável',sha(manifestRaw)==='b8beebf1ee084ce8387f79c104194b44932e9af656889bcddadae94343ce2f5b');
 check('Entrega r1 imutável',sha(await fs.readFile(path.join(root,manifest.entrega.arquivo)))===manifest.entrega.sha256);
 check('Parecer r1 imutável',sha(await fs.readFile(path.join(root,'auditoria/termodinamica/pareceres/FOR-01-r1.md')))==='363575e3c97b729560bce956a90902bdf2934f32025c6826a279be96a1d1519f');
 for(const x of manifest.arquivos){const p=x.copia??x.arquivo;check('Histórico r1 '+p,sha(await fs.readFile(path.join(root,p)))===x.sha256);}
 const names=['formulas/termodinamica.html','modulos/e1-termodinamica.html'];
 const [form,aula]=await Promise.all(names.map(read));const [old,oldAula]=await Promise.all(names.map(p=>read(base+'pacote-r1/'+p)));
 const d=parseHtml(form),b=parseHtml(old),ad=parseHtml(aula),ab=parseHtml(oldAula);
 const cards=d.nodes.filter(x=>x.attrs.class==='formula-card'),bcards=b.nodes.filter(x=>x.attrs.class==='formula-card');
 check('100 fichas / IDs preservados',cards.length===100&&JSON.stringify(cards.map(x=>x.attrs.id))===JSON.stringify(bcards.map(x=>x.attrs.id)));
 check('11 grupos preservados',new Set(cards.map(x=>x.attrs['data-grupo'])).size===11&&cards.every((x,i)=>x.attrs['data-grupo']===bcards[i].attrs['data-grupo']));
 const math=form.match(/<math\b[\s\S]*?<\/math>/g)||[],bmath=old.match(/<math\b[\s\S]*?<\/math>/g)||[];check('191 elementos MathML preservados',math.length===191&&JSON.stringify(math)===JSON.stringify(bmath));
 const changed=cards.map((x,i)=>form.slice(x.start,x.end)===old.slice(bcards[i].start,bcards[i].end)?null:i+1).filter(Boolean);check('Somente fichas 23/46/79/84',JSON.stringify(changed)==='[23,46,79,84]');
 const delta=JSON.parse(await read(base+'deltas-fichas-r1-r2.json'));let replay=old;
 for(const x of delta){const mask=s=>s.replace(/data-busca="[^"]*"/,'data-busca="BUSCA"').replace(/<p class="formula-condicao">[\s\S]*?<\/p>/,'<p class="formula-condicao">CONDICAO</p>');check(x.id+': só condição e busca',mask(x.antes)===mask(x.depois));check(x.id+': hashes do delta',sha(x.antes)===x.sha256_antes&&sha(x.depois)===x.sha256_depois);replay=replay.replace(x.antes,x.depois);const node=d.ids.get(x.id)[0],html=form.slice(node.start,node.end),cond=strip(html.match(/<p class="formula-condicao">([\s\S]*?)<\/p>/)[1]);check(x.id+': busca sincronizada',node.attrs['data-busca'].includes(cond));check(x.id+': exclusão inequívoca',cond.includes('qualquer trabalho não associado ao escoamento, recebido ou fornecido, inclusive elétrico')&&cond.includes('pv já integra h'));}
 check('Formulário reconstruído apenas pelo delta',replay===form);
 const da=JSON.parse(await read(base+'deltas-aula-r1-r2.json'));check('Somente três alvos autorizados',JSON.stringify(da.map(x=>x.ancora))==='["base-calor-latente","base-rankine","base-refrigeracao"]');replay=oldAula;for(const x of da){check('Delta aula único '+x.ancora,replay.split(x.antes).length===2);replay=replay.replace(x.antes,x.depois);}check('Aula reconstruída apenas pelo delta',replay===aula);
 const articles=ad.nodes.filter(isInventoryArticle),ba=ab.nodes.filter(isInventoryArticle);check('197 artigos byte a byte',articles.length===197&&ba.length===197&&articles.every(x=>{const p=ba.find(y=>x.attrs.id===y.attrs.id);return p&&aula.slice(x.start,x.end)===oldAula.slice(p.start,p.end)}));
 for(const id of ['fun01-estado-equilibrio','fun02-diferenciais-caminhos']){const x=ad.ids.get(id)[0],y=ab.ids.get(id)[0];check(id+' integral preservada',aula.slice(x.start,x.end)===oldAula.slice(y.start,y.end));}
 const ir=await read('auditoria/termodinamica/inventario/inventario-questoes.json'),ib=await read(base+'pacote-r1/auditoria/termodinamica/inventario/inventario-questoes.json'),i=JSON.parse(ir),j=JSON.parse(ib);check('197 registros preservados',JSON.stringify(i.itens)===JSON.stringify(j.itens));const norm=x=>({...x,fonte:{...x.fonte,sha256:'HASH',snapshot:'SNAPSHOT'}});check('Inventário só hash/snapshot globais',JSON.stringify(norm(i))===JSON.stringify(norm(j)));
 const rr=JSON.parse(await read(base+'revisao-100-r2.json')),rb=JSON.parse(await read(base+'revisao-100-r1.json'));check('Registro científico muda somente quatro fichas',rr.fichas.length===100&&JSON.stringify(rr.fichas.filter((x,i)=>JSON.stringify(x)!==JSON.stringify(rb.fichas[i])).map(x=>x.numero))==='[23,46,79,84]');check('Documentação r2: 191 elementos',rr.contagem.elementos_mathml===191);
 for(const p of ['assets/formulario-e1.js','assets/formulario-e1.css','assets/curso.js','assets/curso.css','assets/registro.js','auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md'])check('Infraestrutura/resumo intactos '+p,await read(p)===await read(base+'pacote-r1/'+p));
 const m=.02,hfg=1000,T=300,Q=0,Wel=m*hfg,Wnon=-Wel,dH=m*hfg,Sgen=dH/T;
 check('Resistor: balanço geral fecha',Q-Wnon===dH&&dH===20);
 check('Resistor: redução Q=ṁhfg falha',Q!==dH);
 check('Resistor: fora da hipótese publicada',Wnon!==0&&[23,46,79,84].every(n=>{const x=cards[n-1],c=strip(form.slice(x.start,x.end));return c.includes('recebido ou fornecido, inclusive elétrico')}));
 check('Resistor: entropia gerada não negativa',Sgen>0,'No modelo saturado puro a T constante, hfg=T·sfg; Sgen=ṁsfg=Wel,in/T>0 para VC adiabático. Dados 1000 kJ/kg e 300 K são autorais, não tabela de fluido real.');
 const inventory=await validateInventory({rootDir:root});check('Validação canônica',inventory.ok);
 return {id:'FOR-01',rodada:2,data:'2026-10-28',ok:checks.every(x=>x.ok),total:checks.length,falhas:checks.filter(x=>!x.ok),checks,inventario:inventory,contraprova:{natureza:'Caso autoral de verificação, sem propriedade experimental',mdot_kg_s:m,hfg_kJ_kg:hfg,T_K:T,Qdot_kW:Q,Wdot_nao_fluxo_kW:Wnon,Wel_in_kW:Wel,mdot_delta_h_kW:dH,Sger_kW_K:Sgen,interpretacao:'O resistor está dentro da fronteira. Energia entra como trabalho elétrico; a adiabaticidade só anula calor. A r2 exclui esse caso do modelo reduzido e mantém pv em h.'},limite:'Reauditoria restrita a R1-A e preservação. Os 913 checks r1 não foram repetidos; demais critérios são herdados por identidade.'};
}
