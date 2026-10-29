// Auditor automatizado independente. Executa comparações e funções reais isoladas;
// não simula nem declara um navegador, e não modifica arquivos do produto.
import fs from 'node:fs/promises';
import path from 'node:path';
import vm from 'node:vm';
import assert from 'node:assert/strict';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';
const raiz = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../../..');
const evidencia = path.join(raiz, 'auditoria/termodinamica/evidencias/BAN-01');
const ler = p => fs.readFile(p, 'utf8');
const [antes, depois, regAntes, regDepois, js] = await Promise.all([
  ler(path.join(evidencia, 'e1-termodinamica.antes.html')),
  ler(path.join(raiz, 'modulos/e1-termodinamica.html')),
  ler(path.join(evidencia, 'registro.antes.js')),
  ler(path.join(raiz, 'assets/registro.js')),
  ler(path.join(raiz, 'assets/curso.js'))
]);
const hash = t => crypto.createHash('sha256').update(t).digest('hex');
assert.equal(hash(antes), '10c3d92ef94136069dc94ee102fc0ff6e30b94cda82a66edf62de7d5346c015f');
assert.equal(hash(regAntes), 'd55c275daf98a485574c40661155b02d25d1636d90ec2cb856d635df0b4f95fc');
assert.equal(hash(js), '81728c9fd1e96b738410e6b51cf4ab3ed785fb17753e68a988c1dcf236d8f899');

const deltasPermitidos = [
  ['Uma válvula de estrangulamento opera adiabaticamente, sem trabalho e com pequenas mudanças de velocidade e altura.', 'Uma válvula de estrangulamento opera em regime permanente, adiabaticamente, sem trabalho e com pequenas mudanças de velocidade e altura.'],
  ['Qual trabalho específico aproximado?', 'Qual é a magnitude aproximada do trabalho específico de entrada (consumido), adotada como positiva?']
];
const r1html=await ler(path.join(evidencia,'e1-termodinamica.r1.html'));
const r1registro=await ler(path.join(evidencia,'registro.r1.js'));
assert.equal(hash(r1html),'d375695006edf96cbb709b7e85e7ebb84e94474333505768a3cccec0e94119a4');
assert.equal(hash(r1registro),'234cb179c3a7c81043d9d66ee65116b2f07503999aac6a45c433dccd51545055');
let esperadoR2=r1html;
for(const [de,para] of deltasPermitidos){assert.equal(esperadoR2.split(de).length,2);esperadoR2=esperadoR2.replace(de,para);}
assert.equal(depois,esperadoR2);
assert.equal(regDepois,r1registro.replace('"1877b147": "E"','"ab29d979": "E"').replace('"0e39d656": "C"','"83f286e2": "C"'));
function aplicarAjustesPermitidos(html){for(const [de,para] of deltasPermitidos)html=html.replace(de,para);return html;}

const regexQuestoes = /<article class="questao"[\s\S]*?<\/article>/g;
const qa = [...antes.matchAll(regexQuestoes)].map(m => m[0]);
const qd = [...depois.matchAll(regexQuestoes)].map(m => m[0]);
assert.equal(qa.length, 30); assert.equal(qd.length, 30);
assert.equal(antes.replace(regexQuestoes, ''), depois.replace(regexQuestoes, ''));

// Parser mínimo dos fragmentos examinados: texto literal e árvore de elementos.
// Esses 30 fragmentos não contêm entidades HTML; testar essa pré-condição evita
// confundir fonte HTML com textContent na geração da digital.
assert.equal(/&[a-zA-Z0-9#]+;/.test(qa.join('') + qd.join('')), false);
function arvore(fragmento) {
  const raiz = { nodeType: 1, childNodes: [], localName: 'fragment', atributos: {} };
  const pilha = [raiz];
  for (const token of fragmento.match(/<!--[\s\S]*?-->|<[^>]*>|[^<]+/g) || []) {
    if (token.startsWith('<!--')) continue;
    if (token.startsWith('</')) { pilha.pop(); continue; }
    if (token.startsWith('<')) {
      const nome = /^<([^\s/>]+)/.exec(token)[1];
      const atributos = Object.fromEntries([...token.matchAll(/([^\s=<>]+)="([^"]*)"/g)].map(m => [m[1], m[2]]));
      const no = {nodeType: 1, localName: nome, atributos, childNodes: [], hasAttribute(k) {return Object.hasOwn(this.atributos,k)}, getAttribute(k) {return this.atributos[k] ?? null}};
      pilha.at(-1).childNodes.push(no);
      if (!/\/>$/.test(token) && !/^(img|br|hr|input|meta|link|source|wbr)$/.test(nome)) pilha.push(no);
    } else pilha.at(-1).childNodes.push({nodeType: 3, nodeValue: token});
  }
  assert.equal(pilha.length, 1, 'Fragmento com fechamento desequilibrado');
  return raiz;
}
function classe(no, nome) {
  if (no.nodeType === 1 && (no.atributos?.class || '').split(/\s+/).includes(nome)) return no;
  for (const filho of no.childNodes || []) {const resultado=classe(filho,nome);if(resultado)return resultado;}
  return null;
}
function trecho(tag, nome, html) {
  const inicio = new RegExp('<'+tag+' class="'+nome+'">').exec(html);
  assert.ok(inicio, nome);
  let profundidade = 1;
  const tags = new RegExp('</?'+tag+'\\b[^>]*>', 'g');
  tags.lastIndex = inicio.index + inicio[0].length;
  for(let token;(token=tags.exec(html));) {
    profundidade += token[0].startsWith('</') ? -1 : 1;
    if(!profundidade)return html.slice(inicio.index+inicio[0].length,token.index);
  }
  throw Error('Trecho incompleto: '+nome);
}
function opcao(html) {return [...html.matchAll(/<li data-letra="([A-E])">([\s\S]*?)<\/li>/g)].map(m=>({letra:m[1],html:m[2]}));}
function extrairFuncao(nome) {
  const inicio = js.indexOf('  function '+nome+'(');
  assert.ok(inicio >= 0, nome);
  const fim = js.indexOf('\n  }', inicio) + 4;
  return js.slice(inicio, fim);
}
const ambiente = vm.createContext({window:{},LETRAS:[...'ABCDE'],SEPARADOR:'␞',RE_DIGITAL:/^[0-9a-f]{8}$/,LIMITE_ERROS:Number.MAX_SAFE_INTEGER,MODULO:'e1',ctxQuestoes:null});
vm.runInContext(['paraArray','normalizarDigital','textoDaDigital','fnv1a','inteiroValido','lerEstadoModulo','progressoDoModulo','mostrarCorrecao'].map(extrairFuncao).join('\n'),ambiente);
function digital(html) {
  const no=arvore(html);
  const partes=[ambiente.normalizarDigital(ambiente.textoDaDigital(classe(no,'q-enunciado')))];
  classe(no,'q-alternativas').childNodes.filter(x=>x.localName==='li').forEach(x=>partes.push(ambiente.normalizarDigital(ambiente.textoDaDigital(x))));
  partes.push(/data-gabarito="([A-E])"/.exec(html)[1]);
  return ambiente.fnv1a(partes.join('␞'));
}
const ra=JSON.parse(regAntes.slice(regAntes.indexOf('{'),regAntes.lastIndexOf('}')+1));
const rd=JSON.parse(regDepois.slice(regDepois.indexOf('{'),regDepois.lastIndexOf('}')+1));
const itens=[];
let totalAlternativas=0,totalJustificativas=0,totalProposicoes=0;
for(let i=0;i<30;i++) {
  const a=qa[i],d=qd[i],id='q-e1-'+String(i+1).padStart(2,'0');
  assert.ok(a.includes('id="'+id+'"')&&d.includes('id="'+id+'"'));
  const opA=opcao(trecho('ol','q-alternativas',a)),opD=opcao(trecho('ol','q-alternativas',d));
  assert.equal(opA.length,5);assert.equal(opD.length,5);
  assert.equal(opD.map(o=>o.letra).join(''),'ABCDE');
  assert.equal(new Set(opD.map(o=>o.html)).size,5);
  const mapa=Object.fromEntries(opA.map(o=>{const destinos=opD.filter(n=>n.html===o.html);assert.equal(destinos.length,1);return[o.letra,destinos[0].letra]}));
  assert.notEqual(JSON.stringify(mapa),JSON.stringify(Object.fromEntries([...'ABCDE'].map(x=>[x,x]))));
  const ga=/data-gabarito="([A-E])"/.exec(a)[1],gd=/data-gabarito="([A-E])"/.exec(d)[1];
  assert.equal(mapa[ga],gd);assert.equal(/<p class="q-gabarito">Gabarito: ([A-E])<\/p>/.exec(d)[1],gd);
  const ja=trecho('ul','q-justificativas',a),jd=trecho('ul','q-justificativas',d);
  if(i===12||i===17){assert.equal(ja,jd);assert.equal((ja.match(/data-item=/g)||[]).length,3);totalProposicoes+=3;}
  else {const oa=opcao(ja),od=opcao(jd);assert.equal(oa.length,5);assert.equal(od.length,5);assert.equal(od.map(o=>o.letra).join(''),'ABCDE');for(const o of oa)assert.equal(o.html,od.find(n=>n.letra===mapa[o.letra]).html);totalJustificativas+=5;}
  function mascara(h){return h.replace(/<ol class="q-alternativas">[\s\S]*?<\/ol>/,'OPCOES').replace(/<ul class="q-justificativas">[\s\S]*?<\/ul>/,'JUSTIFICATIVAS').replace(/data-gabarito="[A-E]"/,'data-gabarito="?"').replace(/(<p class="q-gabarito">Gabarito: )[A-E]/,'$1?');}
  assert.equal(mascara(aplicarAjustesPermitidos(a)),mascara(d));
  const digitalA=digital(a),digitalD=digital(d);
  assert.equal(ra.modulos.e1.questoes[digitalA],ga);assert.equal(rd.modulos.e1.questoes[digitalD],gd);
  assert.equal(digitalD in ra.modulos.e1.questoes,false);
  totalAlternativas+=5;itens.push({id,antes:ga,depois:gd,mapa,digital_antes:digitalA,digital_depois:digitalD});
}
assert.equal(Object.keys(rd.modulos.e1.questoes).length,30);assert.equal(new Set(itens.map(i=>i.digital_depois)).size,30);
const regexMapa=/("e1": \{[\s\S]*?"questoes": \{)[\s\S]*?(\n      \})/;
assert.equal(regAntes.replace(regexMapa,'$1MAPA$2'),regDepois.replace(regexMapa,'$1MAPA$2'));
const seq=itens.map(i=>i.depois).join('');
const periodos=[];for(let p=1;p<=15;p++)if([...seq].every((c,i)=>c===seq[i%p]))periodos.push(p);
assert.equal(periodos.length,0);assert.notEqual(seq,'ABCDE'.repeat(6));
const blocos=Array.from({length:6},(_,i)=>seq.slice(i*5,i*5+5));assert.equal(new Set(blocos).size,6);

// Exercita a função real de filtragem de respostas e a função real do portal,
// ambas extraídas de curso.js. O armazenamento aqui é um objeto de teste.
ambiente.ctxQuestoes={digitais:rd.modulos.e1.questoes};
ambiente.registrarCorrompido=()=>()=>{};
ambiente.window.CURSO_REGISTRO=rd;
const antigo={v:2,respostas:{...ra.modulos.e1.questoes},erros:Object.fromEntries(Object.keys(ra.modulos.e1.questoes).map(k=>[k,2])),simulado:null};
const novo={v:2,respostas:{...rd.modulos.e1.questoes},erros:{},simulado:null};
ambiente.armazenamento={lerJSON:()=>antigo};
const carregadoAntigo=ambiente.lerEstadoModulo(),portalAntigo=ambiente.progressoDoModulo('e1');
assert.equal(Object.keys(carregadoAntigo.respostas).length,0);assert.equal(Object.keys(carregadoAntigo.erros).length,0);assert.equal(portalAntigo.respondidas,0);
ambiente.armazenamento={lerJSON:()=>novo};
const carregadoNovo=ambiente.lerEstadoModulo(),portalNovo=ambiente.progressoDoModulo('e1');
assert.equal(Object.keys(carregadoNovo.respostas).length,30);assert.equal(portalNovo.respondidas,30);assert.equal(portalNovo.acertos,30);
ambiente.armazenamento={lerJSON:()=>({...novo,respostas:{...antigo.respostas,...novo.respostas}})};
assert.equal(Object.keys(ambiente.lerEstadoModulo().respostas).length,30);assert.equal(ambiente.progressoDoModulo('e1').acertos,30);

// Adaptação mínima de elementos para exercitar a correção real de cada letra;
// isso testa a função, não renderização ou acessibilidade em navegador.
let casosCorrecao=0;
for(const item of itens)for(const marcada of 'ABCDE'){
  const botoes=[...'ABCDE'].map(letra=>{const atributos={'data-letra':letra};const classes=new Set();const selo={textContent:''};return {atributos,classes,selo,getAttribute:k=>atributos[k],setAttribute:(k,v)=>atributos[k]=v,querySelector:()=>selo,classList:{remove:(...ks)=>ks.forEach(k=>classes.delete(k)),add:k=>classes.add(k)}}});
  const atributosQuestao={};
  const d={gabarito:item.depois,botoes,q:{setAttribute:(k,v)=>atributosQuestao[k]=v},feedback:{textContent:'',className:''},acoes:{hidden:true}};
  ambiente.mostrarCorrecao(d,marcada,true,true);
  assert.equal(atributosQuestao['data-respondida'],marcada);
  assert.equal(botoes.filter(b=>b.classes.has('correta')).length,1);
  assert.equal(botoes.find(b=>b.classes.has('correta')).atributos['data-letra'],item.depois);
  assert.equal(botoes.filter(b=>b.classes.has('errada')).length,marcada===item.depois?0:1);
  assert.equal(botoes.filter(b=>b.atributos['aria-pressed']==='true').length,1);
  assert.ok(d.feedback.textContent.includes(marcada===item.depois?'Você acertou.':'Você marcou '+marcada));
  assert.ok(d.feedback.textContent.includes(item.depois));
  assert.equal(d.acoes.hidden,false);casosCorrecao++;
}

export const resultado={id:'BAN-01',rodada:2,revisor:'agente automatizado Auditor AAA /root/auditor_aaa',tipo:'Estático e funções reais executadas em isolamento; sem navegador',hashes:{html:hash(depois),registro:hash(regDepois),curso_js:hash(js)},itens:30,alternativas:totalAlternativas,justificativas_por_letra:totalJustificativas,proposicoes_preservadas:totalProposicoes,casos_de_correcao:casosCorrecao,sequencia:seq,periodos_1_a_15:periodos,blocos_de_5:blocos,escopo_preservado:true,estado:{antigo_aceitas:Object.keys(carregadoAntigo.respostas).length,novo_aceitas:Object.keys(carregadoNovo.respostas).length,portal_novo_acertos:portalNovo.acertos,associacao_incorreta_de_respostas_antigas:false},mapeamento:itens};
