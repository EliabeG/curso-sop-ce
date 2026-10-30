'use strict';
// Executa funções extraídas do programa real com contexto e armazenamento simulados.
// Somente leitura; não testa a integração no navegador.
const fs = require('fs'), crypto = require('crypto'), vm = require('vm'), assert = require('assert'), path = require('path');
const root = path.resolve(__dirname, '../../../../..');
const read = p => fs.readFileSync(path.join(root,p),'utf8');
const hash = s => crypto.createHash('sha256').update(s).digest('hex');
const curso = read('assets/curso.js'), registro = read('assets/registro.js');
assert.equal(hash(curso),'a20f4d19158073a9a1c48aabdfba8fa863b02063e16061c00b16448a6ccc2e13');
assert.equal(hash(registro),'46da94527d6639fe0265bd766286f1ef39623966105e00bda3b31f21ca2c247c');
assert.equal(hash(read('modulos/e1-termodinamica.html')),'f6c461f1d6039ea47dc7e97f9ad734bb0ea3fcb902f01ffdbf18d18d88e08d0e');
assert.equal(hash(read('auditoria/termodinamica/evidencias/QA-09/inventario-r15.json')),'c8c9c3a3e141eba47a16e9f85c69f97c6e8b8a55aab689c6120ef1a0070c9d9c');
const trecho = (start,end) => { const i=curso.indexOf(start), j=curso.indexOf(end,i); assert(i>=0 && j>i); return curso.slice(i,j); };
let fakeState = null;
const c = {window:{}, armazenamento:{lerJSON:()=>fakeState}, RE_DIGITAL:/^[0-9a-f]{8}$/, LETRAS:['A','B','C','D','E'], ctxQuestoes:null, Date:{now:()=>250000}};
vm.createContext(c);
vm.runInContext(registro,c);
vm.runInContext(trecho('  function formatarTempo(', '  function pluralizar(') +
 trecho('  function resumirEstado(', '  function estadoVazio(') +
 trecho('  function textoTempoSimulado(', '  function rotuloSoErros(') +
 trecho('  function progressoDoModulo(', '  function mostrarProgressoPortal('),c);
const qs=c.window.CURSO_REGISTRO.modulos.e1.questoes, keys=Object.keys(qs);
assert.equal(keys.length,30);
const wrong = l => l === 'A' ? 'B' : 'A';
const respostas = {[keys[0]]:qs[keys[0]], [keys[1]]:wrong(qs[keys[1]]), [keys[2]]:qs[keys[2]], ffffffff:'A'};
assert(!Object.hasOwn(qs,'ffffffff'));
fakeState={v:2,respostas};
const prog=c.progressoDoModulo('e1');
assert.equal(prog.total,30); assert.equal(prog.respondidas,3); assert.equal(prog.acertos,2);
c.ctxQuestoes={lista:keys.map(k=>({digital:k,gabarito:qs[k]})),modo:'estudo',versao:'teste'};
const r=c.resumirEstado({respostas});
assert.equal(r.total,30); assert.equal(r.respondidas,3); assert.equal(r.acertos,2);
assert.equal(c.textoDoPlacar('estudo',r,null,0,''),'Respondidas: 3 de 30 · Acertos: 2 (67% das respondidas)');
assert.equal(c.textoDoPlacar('estudo',{total:30,respondidas:0,acertos:0},null,0,''),'Respondidas: 0 de 30 · Acertos: 0');
assert.equal(c.formatarTempo(-1),'00:00:00'); assert.equal(c.formatarTempo(59999),'00:00:59');
assert.equal(c.formatarTempo(3661000),'01:01:01'); assert.equal(c.formatarTempo(360000000),'100:00:00');
assert.equal(c.textoDoPlacar('simulado',{total:30,respondidas:3,acertos:2},{inicio:10000,corrigido:false},3,''),'Marcadas: 3 de 30 · Tempo: 00:04:00 de 00:03:00 (tempo esgotado)');
assert.equal(c.textoDoPlacar('simulado',{total:30,respondidas:3,acertos:2},{inicio:10000,fim:70000,corrigido:true},3,''),'Simulado corrigido: 2 de 30 acertos · Tempo: 00:01:00 de 00:03:00');
console.log(JSON.stringify({ok:true, registro_e1:keys.length, hipotese:'estado e contexto simulados; não é navegador'}));
