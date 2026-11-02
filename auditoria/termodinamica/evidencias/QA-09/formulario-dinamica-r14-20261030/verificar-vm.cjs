// Ambiente DOM reduzido para ensaiar o código de produção, sem navegador.
'use strict';
const fs = require('fs'), vm = require('vm'), assert = require('assert');
const fixture = JSON.parse(fs.readFileSync(0, 'utf8'));
class El {
  constructor() { this.hidden = false; this.textContent = ''; this.listeners = {}; this.attrs = {}; this.value = ''; }
  addEventListener(event, cb) { this.listeners[event] = cb; }
  setAttribute(k,v) { this.attrs[k] = v; }
  fire(event) { assert(this.listeners[event]); this.listeners[event](); }
  focus() { this.focused = true; }
}
const cards = fixture.cards.map(c => {
  let f = new El(); f.id = c.id; f.dataset = {busca:c.busca, grupo:c.grupo};
  f.expr = new El(); f.reveal = new El(); f.reveal.hidden = true;
  f.querySelector = s => ({'.formula-expressao':f.expr, '.formula-revelar':f.reveal})[s];
  return f;
});
const groups = fixture.grupos.map(id => {
  let g = new El(); g.id = id; g.querySelectorAll = s => { assert.equal(s,'.formula-card'); return cards.filter(c => c.dataset.grupo === id); }; return g;
});
const ids = Object.fromEntries(['formula-busca','formula-assunto','formula-memorizar','formula-contagem','formula-vazio','formula-instrucao','formula-limpar','formula-imprimir'].map(x => [x,new El()]));
ids['formula-assunto'].value = 'todos'; ids['formula-instrucao'].hidden = true;
const ferramentas = new El(), indice = new El(); ferramentas.hidden = true; let printed = 0;
const document = {
  querySelector: s => {assert.equal(s,'.formulario-ferramentas');return ferramentas;},
  querySelectorAll: s => ({'.formula-card':cards,'.formula-grupo':groups,'.formulario-indice a':[indice]})[s],
  getElementById: s => {assert(ids[s],s);return ids[s];}
};
vm.runInNewContext(fs.readFileSync(process.argv[2],'utf8'), {document, window:{print:()=>printed++}});
const visible = () => cards.filter(c => !c.hidden).map(c => c.id);
assert.equal(ferramentas.hidden,false);
ids['formula-busca'].value = '  CARNOT  '; ids['formula-busca'].fire('input');
assert.deepEqual(visible(), ['formula-temperatura','formula-eficiencia','formula-cop-refrigerador','formula-cop-bomba-calor','formula-carnot','formula-limites-carnot','formula-cop-carnot']);
assert.equal(ids['formula-contagem'].textContent,'7 de 100 fichas');
ids['formula-assunto'].value = 'segunda-lei'; ids['formula-assunto'].fire('change');
assert.deepEqual(visible(),['formula-eficiencia','formula-cop-refrigerador','formula-cop-bomba-calor','formula-carnot','formula-limites-carnot','formula-cop-carnot']);
assert.equal(ids['formula-contagem'].textContent,'6 de 100 fichas');
ids['formula-busca'].value = 'ENTRÓPIA'; ids['formula-assunto'].value = 'todos'; ids['formula-busca'].fire('input');
assert.equal(visible().length,17); assert.equal(ids['formula-contagem'].textContent,'17 de 100 fichas');
ids['formula-busca'].value = 'xyz_ausente_0198'; ids['formula-busca'].fire('input');
assert.equal(visible().length,0); assert.equal(ids['formula-vazio'].hidden,false); assert(groups.every(g=>g.hidden));
ids['formula-limpar'].fire('click'); assert.equal(visible().length,100); assert(ids['formula-vazio'].hidden); assert(ids['formula-busca'].focused); assert(groups.every(g=>!g.hidden));
ids['formula-memorizar'].fire('click'); assert.equal(ids['formula-memorizar'].attrs['aria-pressed'],'true'); assert(cards.every(c=>c.expr.hidden && !c.reveal.hidden));
cards[0].reveal.fire('click'); assert.equal(cards[0].expr.hidden,false); assert.equal(cards[0].reveal.attrs['aria-expanded'],'true');
ids['formula-memorizar'].fire('click'); assert(cards.every(c=>!c.expr.hidden && c.reveal.hidden));
ids['formula-imprimir'].fire('click'); assert.equal(printed,1);
ids['formula-busca'].value='carnot'; ids['formula-busca'].fire('input'); indice.fire('click'); assert.equal(visible().length,100);
console.log(JSON.stringify({ok:true, cards:cards.length, grupos:groups.length, ambiente:'DOM simulado; não é navegador'}));
