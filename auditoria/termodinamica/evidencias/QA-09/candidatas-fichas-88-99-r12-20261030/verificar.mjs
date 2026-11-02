import fs from 'node:fs';
import crypto from 'node:crypto';
import {parseHtml} from '../../../inventario/validar-inventario.mjs';
// Simulação somente em memória, sem alterar o formulário nem evidências históricas.
const dir='auditoria/termodinamica/evidencias/QA-09/candidatas-fichas-88-99-r12-20261030';
const m=JSON.parse(fs.readFileSync(`${dir}/manifesto.json`,'utf8'));
const html=fs.readFileSync('formulas/termodinamica.html','utf8');
const inv=fs.readFileSync('auditoria/termodinamica/evidencias/QA-09/inventario-r12.json','utf8');
const sha=s=>crypto.createHash('sha256').update(s,'utf8').digest('hex');
if(sha(html)!==m.formulario_sha256||sha(inv)!==m.inventario_r12_sha256)throw Error('fotografia divergente');
let result=html;
for(const x of m.itens){
 const a=fs.readFileSync(`${dir}/${x.ficha}-original.html`,'utf8').replace(/\n$/,''),b=fs.readFileSync(`${dir}/${x.ficha}-candidata.html`,'utf8').replace(/\n$/,'');
 if(sha(a)!==x.original_sha256||sha(b)!==x.candidata_sha256||html.slice(x.inicio_utf16,x.fim_utf16)!==a||html.split(a).length!==2||result.split(a).length!==2)throw Error(`identidade ${x.ficha}`);
 if(a.split(x.antes).length!==3||a.split(x.antes).join(x.depois)!==b)throw Error(`delta ${x.ficha}`);
 const math=s=>(s.match(/<math\b[\s\S]*?<\/math>/g)??[]).join('');if(math(a)!==math(b))throw Error('MathML');result=result.replace(a,b);
}
const d0=parseHtml(html),d1=parseHtml(result),cards=d=>d.nodes.filter(n=>(n.attrs.class??'').split(/\s+/).includes('formula-card'));
let before=cards(d0),after=cards(d1);if(before.length!==100||after.length!==100||d0.errors.length||d1.errors.length)throw Error('estrutura');
for(let i=0;i<before.length;i++){let a=before[i],b=after[i];if(a.attrs.id!==b.attrs.id)throw Error('IDs');if(!m.itens.some(x=>x.ancora===a.attrs.id)&&html.slice(a.start,a.end)!==result.slice(b.start,b.end))throw Error('ficha não alvo');}
const count=s=>(s.match(/<math\b/g)??[]).length;if(count(html)!==191||count(result)!==191)throw Error('contagem MathML');
const W01=1000, extra=200, hA=10*2, deltaT= (W01+extra)/hA;if(deltaT!==60||W01/hA!==50)throw Error('teste de aporte');
const ratios=[2,3,4,5,8].map(r=>Math.pow(r,.4/1.4)+Math.pow(16/r,.4/1.4)-2);if(!(ratios[2]<ratios[0]&&ratios[2]<ratios[1]&&ratios[2]<ratios[3]&&ratios[2]<ratios[4]))throw Error('teste de ótimo');
console.log(JSON.stringify({ok:true,cartoes:100,nao_alvo_identicos:98,mathml_preservado:191,deltaT_sem_outro_aporte_K:50,deltaT_com_outro_aporte_K:deltaT,razao_otimo:4,gravado:false,parecer:'pendente'},null,2));
