import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import assert from 'node:assert/strict';
import crypto from 'node:crypto';
const dir = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(dir, '../../../..');
function innerElement(raw,tag,className){ var opener=new RegExp('<'+tag+'\\b[^>]*class="'+className+'"[^>]*>').exec(raw); if(!opener) throw Error('Missing '+className); var tokens=new RegExp('<\\/?'+tag+'\\b[^>]*>','g'); tokens.lastIndex=opener.index+opener[0].length; var depth=1,m; while((m=tokens.exec(raw))){depth+=m[0].startsWith('</')?-1:1;if(depth===0)return raw.slice(opener.index+opener[0].length,m.index);}throw Error('Unclosed '+className); }
function textDigital(raw){return raw.replace(/<math\b([^>]*)>[\s\S]*?<\/math>/g,(all,attrs)=>{var m=/data-formula-original="([^"]*)"/.exec(attrs);return m?m[1]:all;}).replace(/<[^>]*>/g,'').replace(/[ \t\n\r\f\v\u00a0]+/g,' ').replace(/^ | $/g,'');}
function fnv(str){var h=0x811c9dc5;for(var c of str){h^=c.codePointAt(0);h=Math.imul(h,0x01000193)>>>0;}return h.toString(16).padStart(8,'0');}
function parseQuestion(raw){ var id=/id="(q-e1-\d{2})"/.exec(raw)[1];var key=/data-gabarito="([A-E])"/.exec(raw)[1];var options=[...innerElement(raw,'ol','q-alternativas').matchAll(/<li data-letra="([A-E])">([\s\S]*?)<\/li>/g)].map(m=>({letter:m[1],html:m[2],raw:m[0]})); var stem=innerElement(raw,'div','q-enunciado');return {id,key,options,stem,fingerprint:fnv([textDigital(stem),...options.map(o=>textDigital(o.html)),key].join('␞'))};}
const qRE=/<article\b[^>]*\bid="q-e1-\d{2}"[^>]*>[\s\S]*?<\/article>/g;
const before=await fs.readFile(path.join(dir,'e1-termodinamica.antes.html'),'utf8');
const after=await fs.readFile(path.join(root,'modulos/e1-termodinamica.html'),'utf8');
const rb=await fs.readFile(path.join(dir,'registro.antes.js'),'utf8');
const ra=await fs.readFile(path.join(root,'assets/registro.js'),'utf8');
const mapping=JSON.parse(await fs.readFile(path.join(dir,'mapeamento.json'),'utf8'));
const oldQ=[...before.matchAll(qRE)].map(m=>m[0]),newQ=[...after.matchAll(qRE)].map(m=>m[0]);
assert.equal(oldQ.length,30);assert.equal(newQ.length,30);assert.equal(mapping.itens.length,30);
assert.equal(before.replace(qRE,'<QUESTAO/>'),after.replace(qRE,'<QUESTAO/>'),'Conteudo fora das 30 questoes');
const oldReg=JSON.parse(rb.slice(rb.indexOf('{'),rb.lastIndexOf('}')+1));
const newReg=JSON.parse(ra.slice(ra.indexOf('{'),ra.lastIndexOf('}')+1));
const rows=[];
for(let i=0;i<30;i++){
 const o=parseQuestion(oldQ[i]),n=parseQuestion(newQ[i]),m=mapping.itens[i];
 assert.equal(o.id,'q-e1-'+String(i+1).padStart(2,'0'));assert.equal(n.id,o.id);assert.equal(m.id,o.id);
 assert.deepEqual(n.options.map(x=>x.letter),[...'ABCDE']);assert.equal(n.options.length,5);
 assert.equal(new Set(n.options.map(x=>x.html)).size,5,'Alternativas repetidas');
 assert.equal(n.key,m.gabarito_novo);assert.equal(o.key,m.gabarito_anterior);
 assert.equal(n.stem,o.stem,'Enunciado alterado');
 for(const opt of o.options){assert.equal(n.options.find(x=>x.letter===m.antiga_para_nova[opt.letter]).html,opt.html,'Alternativa ou associacao alterada');}
 assert.equal(n.options.find(x=>x.letter===n.key).html,o.options.find(x=>x.letter===o.key).html,'Resposta correta mudou');
 assert.equal((newQ[i].match(/<p class="q-gabarito">Gabarito: ([A-E])<\/p>/)||[])[1],n.key);
 const oldJust=innerElement(oldQ[i],'ul','q-justificativas'),newJust=innerElement(newQ[i],'ul','q-justificativas');
 if(oldJust.includes('data-item=')){assert.equal(newJust,oldJust);}else{
  const a=[...oldJust.matchAll(/<li data-letra="([A-E])">([\s\S]*?)<\/li>/g)],b=[...newJust.matchAll(/<li data-letra="([A-E])">([\s\S]*?)<\/li>/g)];
  assert.equal(a.length,5);assert.equal(b.length,5);assert.deepEqual(b.map(x=>x[1]),[...'ABCDE']);for(const x of a)assert.equal(b.find(y=>y[1]===m.antiga_para_nova[x[1]])[2],x[2]);
 }
 const skeleton=q=>q.replace(/<ol class="q-alternativas">[\s\S]*?<\/ol>/,'<OPCOES/>').replace(/<ul class="q-justificativas">[\s\S]*?<\/ul>/,'<JUSTIFICATIVAS/>').replace(/data-gabarito="[A-E]"/,'data-gabarito="*"').replace(/(<p class="q-gabarito">Gabarito: )[A-E]/,'$1*');
 assert.equal(skeleton(newQ[i]),skeleton(oldQ[i]),'Outras partes do item alteradas');
 assert.equal(oldReg.modulos.e1.questoes[o.fingerprint],o.key);assert.equal(newReg.modulos.e1.questoes[n.fingerprint],n.key);
 assert.equal(m.digital_anterior,o.fingerprint);assert.equal(m.digital_nova,n.fingerprint);assert.notEqual(o.fingerprint,n.fingerprint);
 rows.push({id:n.id,gabarito:n.key,digital:n.fingerprint,status:'verificado'});
}
assert.equal(Object.keys(newReg.modulos.e1.questoes).length,30);
assert.equal(new Set(rows.map(x=>x.digital)).size,30);
assert.equal(rows.filter(x=>x.digital in oldReg.modulos.e1.questoes).length,0,'Colisao com digitais anteriores');
oldReg.modulos.e1.questoes={};newReg.modulos.e1.questoes={};assert.deepEqual(newReg,oldReg,'Registro fora do mapa E1 mudou');
const mask=/((?:^|\n)    "e1": \{[\s\S]*?      "questoes": \{)([\s\S]*?)(\n      \})/;
assert.equal(rb.replace(mask,'$1<MAPA>$3'),ra.replace(mask,'$1<MAPA>$3'),'Bytes do registro fora do mapa E1 mudaram');
const seq=rows.map(x=>x.gabarito).join('');
assert.notEqual(seq,'ABCDE'.repeat(6));
const periods=[];for(let p=1;p<=15;p++)if([...seq].every((c,i)=>c===seq[i%p]))periods.push(p);
assert.deepEqual(periods,[]);assert.equal(new Set(Array.from({length:6},(_,i)=>seq.slice(5*i,5*i+5))).size,6);
const sha=x=>crypto.createHash('sha256').update(x).digest('hex');
export const resultado={id:'BAN-01',rodada:1,tipo:'Verificacao estatica reproduzivel; nao e teste de navegador',itens_verificados:30,sequencia:seq,contagens:Object.fromEntries([...'ABCDE'].map(l=>[l,seq.split(l).length-1])),periodos_globais_1_a_15:periods,alteracoes_fora_do_escopo:false,colisoes_de_digitais:0,sha256:{html_antes:sha(before),html_depois:sha(after),registro_antes:sha(rb),registro_depois:sha(ra)},itens:rows};
