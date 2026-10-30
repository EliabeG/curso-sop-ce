import fs from 'node:fs';
import crypto from 'node:crypto';
import {parseHtml} from '../../../inventario/validar-inventario.mjs';
// Simulação somente em memória, sem alterar o formulário nem evidências históricas.
const dir='auditoria/termodinamica/evidencias/QA-09/candidatas-calorimetria-27-29-r11-20261030';
const m=JSON.parse(fs.readFileSync(`${dir}/manifesto.json`,'utf8'));
const html=fs.readFileSync('formulas/termodinamica.html','utf8');
const inv=fs.readFileSync('auditoria/termodinamica/evidencias/QA-09/inventario-r11.json','utf8');
const sha=s=>crypto.createHash('sha256').update(s,'utf8').digest('hex');
if(sha(html)!==m.formulario_sha256||sha(inv)!==m.inventario_r11_sha256)throw Error('fotografia divergente');
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
const du=1*(299.5-300)-1*(1/2-1), sensible=1*(299.5-300);
if(Math.abs(du)>1e-12||Math.abs(sensible+.5)>1e-12)throw Error('contramodelo de U');
const deltaH=200,deltaPV=100*.1,deltaU=deltaH-deltaPV,W=5,Q=deltaU+W;if(Q!==195||deltaH===Q)throw Error('teste de trabalho');
console.log(JSON.stringify({ok:true,cartoes:100,nao_alvo_identicos:97,mathml_preservado:191,deltaU_vdw:du,calor_sensivel:sensible,contraste_Q:Q,contraste_deltaH:deltaH,gravado:false,parecer:'pendente'},null,2));
