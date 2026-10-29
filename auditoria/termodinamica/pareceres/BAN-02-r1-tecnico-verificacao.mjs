/** Auditoria técnica independente BAN-02 r1. Muta somente fixtures em diretório temporário. */
import fs from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import { createHash } from 'node:crypto';
import { fileURLToPath } from 'node:url';
import { validateInventory } from '../inventario/validar-inventario.mjs';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../../..');
const hash = x => createHash('sha256').update(x).digest('hex');
const read = x => fs.readFile(path.join(root, x), 'utf8');
const canonicalPath = 'auditoria/termodinamica/inventario/inventario-questoes.json';
const canonicalText = await read(canonicalPath);
const inventory = JSON.parse(canonicalText);
const html = await read('modulos/e1-termodinamica.html');
const decode = value => value.replace(/&(#x[\da-f]+|#\d+|amp|quot|apos|lt|gt|nbsp);/gi, (whole, token) => {
  if (token.startsWith('#')) return String.fromCodePoint(token[1].toLowerCase() === 'x' ? parseInt(token.slice(2), 16) : Number(token.slice(1)));
  return ({ amp: '&', quot: '"', apos: "'", lt: '<', gt: '>', nbsp: ' ' })[token.toLowerCase()] ?? whole;
});
const plain = value => decode(value.replace(/<[^>]+>/g, '')).replace(/\s+/g, ' ').trim();
const same = (a,b) => JSON.stringify(a) === JSON.stringify(b);
const articles = [...html.matchAll(/<article\b[^>]*\bid="((?:q|cr|av)-e1-\d+)"[^>]*>[\s\S]*?<\/article>/g)].map(m => ({ id:m[1], html:m[0] }));
const byId = new Map(inventory.itens.map(i => [i.id, i]));
const structural = [];
for (const article of articles) {
  const errors = [], item = byId.get(article.id);
  const check = (ok, text) => { if (!ok) errors.push(text); };
  if (!item) { structural.push({ id:article.id, errors:['Sem registro'] }); continue; }
  const bank = article.id.split('-')[0];
  const title = plain(article.html.match(/<h3\b[^>]*>([\s\S]*?)<\/h3>/)?.[1] ?? '');
  const meta = plain(article.html.match(/<p class="cr-meta">([\s\S]*?)<\/p>/)?.[1] ?? '');
  const sourcesHtml = article.html.match(/<p class="cr-fontes">([\s\S]*?)<\/p>/)?.[1] ?? '';
  const sources = [...sourcesHtml.matchAll(/<a\b[^>]*href="([^"]+)"[^>]*>([\s\S]*?)<\/a>/g)].map(m => ({
    rotulo:plain(m[2]),
    url:decode(m[1]).startsWith('../') ? path.posix.normalize(path.posix.join('modulos',decode(m[1]))) : decode(m[1])
  }));
  const values = bank === 'q' ? [...article.html.matchAll(/<li data-letra="([A-E])">/g)].slice(0,5).map(m => m[1])
    : [...article.html.matchAll(/<input\b[^>]*type="radio"[^>]*value="([A-E])"/g)].map(m => m[1]);
  const format = same(values,['C','E']) ? 'certo_errado' : 'multipla_escolha';
  check(item.id === item.localizacao.fragmento, 'ID/fragmento divergentes');
  check(item.localizacao.arquivo === 'modulos/e1-termodinamica.html', 'Arquivo divergente');
  check(item.banco === ({q:'inicial',cr:'real',av:'avalia'})[bank], 'Banco divergente');
  check(item.titulo === title, 'Título divergente');
  check(item.localizacao.sha256_artigo === hash(article.html), 'Hash do artigo divergente');
  check(item.formato.numero_alternativas === values.length, 'Contagem de alternativas divergente');
  check(item.formato.tipo === format, 'Formato divergente');
  check(same(item.origem.fontes,sources), 'Fontes/rótulos/URLs divergem do HTML');
  if (bank === 'cr') {
    check(item.origem.atribuicao === meta, 'Atribuição CR diverge do HTML');
    check(same(item.origem.identificadores,meta.split(' · ')), 'Identificadores CR divergentes');
    check(item.origem.tipo === 'questao_real_atribuida' && item.origem.conferencia_oficial === 'nao_realizada', 'Tipo/estado de origem CR divergente');
  } else if (bank === 'av') {
    const number = article.id.split('-').at(-1);
    check(item.origem.atribuicao === meta + ' | ' + plain(sourcesHtml), 'Atribuição AV diverge do HTML');
    check(same(item.origem.identificadores,[`Transformação autoral da questão ${number}`,`ID de origem cr-e1-${number}`]), 'Identificadores AV divergentes');
    check(item.origem.tipo === 'adaptacao_autoral' && item.origem.conferencia_oficial === 'nao_aplicavel', 'Tipo/estado de origem AV divergente');
  } else {
    check(item.origem.tipo === 'autoral_inicial' && item.origem.conferencia_oficial === 'nao_aplicavel', 'Tipo/estado de origem Q divergente');
    check(item.origem.identificadores.length === 0 && sources.length === 0, 'Origem externa Q inventada');
    check(/30 questões autorais iniciais/.test(plain(html)), 'Descrição do banco inicial não sustenta autoria');
    check(item.origem.atribuicao === 'Banco inicial descrito pelo E1 como autoral. O artigo não informa autor nominal nem fonte externa.', 'Atribuição Q inesperada');
  }
  structural.push({id:item.id, banco:item.banco, formato:format, alternativas:values.length, fontes:sources.length, sha256_artigo:hash(article.html), errors});
}

const fixtureRoot = await fs.mkdtemp(path.join(os.tmpdir(),'ban02-auditor-independent-'));
for (const directory of ['modulos','snapshots','assets','pareceres']) await fs.mkdir(path.join(fixtureRoot,directory),{recursive:true});
const resource = '<svg xmlns="http://www.w3.org/2000/svg"><text>300 K</text></svg>';
const makeArticle = (id, format = 'multipla_escolha') => {
  const bank = /^q-/.test(id) ? 'inicial' : /^cr-/.test(id) ? 'real' : /^av-/.test(id) ? 'avalia' : format === 'projeto' ? 'projeto' : 'aberto';
  const options = format === 'multipla_escolha' ? '<ol class="q-alternativas"><li>300</li><li>400</li><li>500</li></ol>' : format === 'certo_errado' ? '<input type="radio" value="C"><input type="radio" value="E">' : '';
  return `<article id="${id}" data-inventario="e1" data-banco="${bank}" data-formato="${format}"><p>Fixture independente</p><img src="../assets/modelo.svg"><a href="#base">Base</a>${options}</article>`;
};
const fixtureArticles = [makeArticle('q-e1-100'),makeArticle('cr-e1-100','certo_errado'),makeArticle('av-e1-100'),makeArticle('projeto-e1-avancado','projeto'),makeArticle('aberto-e1-ensaio','resposta_aberta')];
const fixtureHtml = '<!doctype html><html><body><h2 id="base">Base</h2>'+fixtureArticles.join('\n')+'</body></html>';
const fixture = structuredClone(inventory);
fixture.fonte = {arquivo:'modulos/e1.html',snapshot:'snapshots/e1.html',sha256:hash(fixtureHtml)};
fixture.itens = fixtureArticles.map((article,index) => {
  const item = structuredClone(inventory.itens[0]);
  item.id = article.match(/id="([^"]+)"/)[1];
  item.banco = article.match(/data-banco="([^"]+)"/)[1];
  item.localizacao = {arquivo:'modulos/e1.html',fragmento:item.id,sha256_artigo:hash(article),recursos:[{arquivo:'assets/modelo.svg',sha256:hash(resource)}]};
  item.origem = {tipo:'fixture_auditor',atribuicao:'Fixture técnica sem valor pedagógico',identificadores:[],fontes:[],conferencia_oficial:'nao_aplicavel'};
  const type = article.match(/data-formato="([^"]+)"/)[1];
  item.formato = {tipo:type,comando:'Fixture',numero_alternativas:type === 'multipla_escolha' ? 3 : type === 'certo_errado' ? 2 : 0};
  item.exposicao_previa = {estado:'desconhecida',relacoes:[],limite_da_verificacao:'Fixture'};
  return item;
});
async function restore() {
  await fs.writeFile(path.join(fixtureRoot,'modulos/e1.html'),fixtureHtml);
  await fs.writeFile(path.join(fixtureRoot,'snapshots/e1.html'),fixtureHtml);
  await fs.writeFile(path.join(fixtureRoot,'assets/modelo.svg'),resource);
  await fs.writeFile(path.join(fixtureRoot,'pareceres/estado.md'),'# Conferência\n\nRegistro técnico fictício.\n<h2 id="gabarito">Gabarito</h2>');
}
const tests = [];
async function test(name, expected, change = async () => {}) {
  await restore();
  const data = structuredClone(fixture);
  await change(data);
  const result = await validateInventory({rootDir:fixtureRoot,inventory:data});
  tests.push({caso:name,esperado_ok:expected,observado_ok:result.ok,passou:result.ok === expected,erros:result.erros});
}
await test('Positivo: Q100, CR100, AV100, projeto e aberto no mesmo contrato',true);
await test('Positivo: estados realizada e verificado com evidências locais',true,d=>{
  d.itens[0].origem.conferencia_oficial='realizada'; d.itens[0].origem.evidencia_conferencia='pareceres/estado.md#conferência';
  d.itens[0].revisao.gabarito='verificado'; d.itens[0].revisao.evidencia_gabarito='pareceres/estado.md#gabarito';
});
await test('Positivo: ajustes obrigatórios com evidência local',true,d=>{d.itens[0].revisao.gabarito='ajustes_obrigatorios';d.itens[0].revisao.evidencia_gabarito='pareceres/estado.md';});
await test('Positivo: gabarito pendente',true,d=>{d.itens[0].revisao.gabarito='pendente';});
const mutations = [
  ['Omissão de registro',d=>d.itens.pop()],
  ['Registro órfão',d=>{d.itens[0].id='q-e1-999';d.itens[0].localizacao.fragmento='q-e1-999';}],
  ['Registro duplicado',d=>d.itens.push(structuredClone(d.itens[0]))],
  ['Hash da fonte desatualizado',d=>d.fonte.sha256='0'.repeat(64)],
  ['Hash do artigo desatualizado',d=>d.itens[0].localizacao.sha256_artigo='0'.repeat(64)],
  ['Hash do recurso desatualizado',d=>d.itens[0].localizacao.recursos[0].sha256='0'.repeat(64)],
  ['Recurso carregado omitido',d=>d.itens[0].localizacao.recursos=[]],
  ['Recurso declarado duplicado',d=>d.itens[0].localizacao.recursos.push(structuredClone(d.itens[0].localizacao.recursos[0]))],
  ['Etapas com quantidade inconsistente',d=>d.itens[0].raciocinio.numero_etapas=99],
  ['Exposição declarada sem relação',d=>d.itens[0].exposicao_previa.estado='relacao_identificada'],
  ['Exposição desconhecida com relação',d=>d.itens[0].exposicao_previa.relacoes=[{id_ou_ancora:'base',tipo:'relacao_tematica',evidencia:'Fixture'}]],
  ['Exposição com destino ausente',d=>{d.itens[0].exposicao_previa.estado='relacao_identificada';d.itens[0].exposicao_previa.relacoes=[{id_ou_ancora:'ausente',tipo:'relacao_tematica',evidencia:'Fixture'}];}],
  ['Realizada sem evidência',d=>d.itens[0].origem.conferencia_oficial='realizada'],
  ['Verificado sem evidência',d=>d.itens[0].revisao.gabarito='verificado'],
  ['Ajustes obrigatórios sem evidência',d=>d.itens[0].revisao.gabarito='ajustes_obrigatorios'],
  ['Evidência opcional ausente',d=>d.itens[0].origem.evidencia_conferencia='pareceres/ausente.md'],
  ['Evidência opcional remota',d=>d.itens[0].origem.evidencia_conferencia='https://example.org/parecer'],
  ['Evidência opcional com âncora ausente',d=>d.itens[0].origem.evidencia_conferencia='pareceres/estado.md#ausente'],
  ['Origem local inexistente',d=>d.itens[0].origem.fontes=[{rotulo:'Origem',url:'fonte-inexistente.pdf'}]],
  ['Banco incompatível',d=>d.itens[0].banco='real'],
  ['Formato incompatível com marca explícita',d=>d.itens[0].formato.tipo='certo_errado'],
  ['Número de alternativas incompatível',d=>d.itens[0].formato.numero_alternativas=5],
  ['Campo obrigatório vazio',d=>d.itens[0].pre_requisitos=['  ']],
  ['Campo desconhecido',d=>d.itens[0].desconhecido=true],
  ['Classificação ainda pendente',d=>d.itens[0].nivel.estimado='a_classificar'],
  ['Caminho fora da raiz',d=>d.itens[0].localizacao.recursos[0].arquivo='../fora.svg'],
  ['Versão antiga',d=>d.schema_version='1.0']
];
for (const [name,change] of mutations) await test(name,false,change);
await test('Fonte física alterada fora do artigo',false,async()=>fs.appendFile(path.join(fixtureRoot,'modulos/e1.html'),'\n<!-- mudança -->'));
await test('Artigo físico alterado com hash global e snapshot renovados',false,async d=>{
  const altered=fixtureHtml.replace('Fixture independente','Fixture alterada');
  await fs.writeFile(path.join(fixtureRoot,'modulos/e1.html'),altered);
  await fs.writeFile(path.join(fixtureRoot,'snapshots/e1.html'),altered);
  d.fonte.sha256=hash(altered);
});
await test('Recurso físico alterado sem mudança no HTML',false,async()=>fs.appendFile(path.join(fixtureRoot,'assets/modelo.svg'),'<!-- 500 K -->'));
await test('Snapshot físico alterado',false,async()=>fs.appendFile(path.join(fixtureRoot,'snapshots/e1.html'),'x'));
await test('Novo Q101 não cadastrado mesmo com hash global renovado',false,async d=>{
  const altered=fixtureHtml.replace('</body>',makeArticle('q-e1-101')+'</body>');
  await fs.writeFile(path.join(fixtureRoot,'modulos/e1.html'),altered);
  await fs.writeFile(path.join(fixtureRoot,'snapshots/e1.html'),altered);
  d.fonte.sha256=hash(altered);
});
await test('Novo projeto não cadastrado mesmo com hash global renovado',false,async d=>{
  const altered=fixtureHtml.replace('</body>',makeArticle('novo-projeto','projeto')+'</body>');
  await fs.writeFile(path.join(fixtureRoot,'modulos/e1.html'),altered);
  await fs.writeFile(path.join(fixtureRoot,'snapshots/e1.html'),altered);
  d.fonte.sha256=hash(altered);
});
await test('Artigo duplicado na fonte com hash global renovado',false,async d=>{
  const altered=fixtureHtml.replace('</body>',fixtureArticles[0]+'</body>');
  await fs.writeFile(path.join(fixtureRoot,'modulos/e1.html'),altered);
  await fs.writeFile(path.join(fixtureRoot,'snapshots/e1.html'),altered);
  d.fonte.sha256=hash(altered);
});
const resourceVariants = [
  ['srcset','<img srcset="../assets/extra.svg 1x, ../assets/modelo.svg 2x">'],
  ['poster','<video poster="../assets/extra.svg"></video>'],
  ['object data','<object data="../assets/extra.svg"></object>'],
  ['SVG image href','<svg><image href="../assets/extra.svg"></image></svg>'],
  ['SVG use xlink:href','<svg><use xlink:href="../assets/extra.svg"></use></svg>'],
  ['CSS inline url','<div style="background-image:url(../assets/extra.svg)"></div>'],
  ['link download','<a href="../assets/extra.svg" download>Dados</a>'],
  ['link dados obrigatório','<a href="../assets/extra.svg" data-recurso="obrigatorio">Dados</a>']
];
for (const [label,markup] of resourceVariants) {
  for (const declared of [false,true]) await test(`${declared?'Aceita':'Rejeita'} ${label} com recurso ${declared?'declarado':'omitido'}`,declared,async d=>{
    const newArticle=fixtureArticles[0].replace('</article>',markup+'</article>');
    const altered=fixtureHtml.replace(fixtureArticles[0],newArticle);
    await fs.writeFile(path.join(fixtureRoot,'modulos/e1.html'),altered);
    await fs.writeFile(path.join(fixtureRoot,'snapshots/e1.html'),altered);
    await fs.writeFile(path.join(fixtureRoot,'assets/extra.svg'),resource);
    d.fonte.sha256=hash(altered);
    d.itens[0].localizacao.sha256_artigo=hash(newArticle);
    if(declared)d.itens[0].localizacao.recursos.push({arquivo:'assets/extra.svg',sha256:hash(resource)});
  });
}
await test('Rejeita imagem remota ainda que hashes locais estejam atualizados',false,async d=>{
  const newArticle=fixtureArticles[0].replace('</article>','<img src="https://example.org/figura.png"></article>');
  const altered=fixtureHtml.replace(fixtureArticles[0],newArticle);
  await fs.writeFile(path.join(fixtureRoot,'modulos/e1.html'),altered);
  await fs.writeFile(path.join(fixtureRoot,'snapshots/e1.html'),altered);
  d.fonte.sha256=hash(altered);d.itens[0].localizacao.sha256_artigo=hash(newArticle);
});
await test('Aceita novo artigo Q101 quando também cadastrado',true,async d=>{
  const article=makeArticle('q-e1-101');
  const altered=fixtureHtml.replace('</body>',article+'</body>');
  await fs.writeFile(path.join(fixtureRoot,'modulos/e1.html'),altered);
  await fs.writeFile(path.join(fixtureRoot,'snapshots/e1.html'),altered);
  d.fonte.sha256=hash(altered);
  const item=structuredClone(d.itens[0]);
  item.id='q-e1-101';item.localizacao.fragmento=item.id;item.localizacao.sha256_artigo=hash(article);d.itens.push(item);
});
await restore();
const hashes = {};
for (const filename of [canonicalPath,'auditoria/termodinamica/inventario/inventario.schema.json','auditoria/termodinamica/inventario/validar-inventario.mjs','auditoria/termodinamica/inventario/LEIA-ME.md','auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md','auditoria/termodinamica/evidencias/BAN-02/testar-validador-r1.mjs','modulos/e1-termodinamica.html','assets/registro.js','assets/curso.js','assets/curso.css']) hashes[filename]=hash(await fs.readFile(path.join(root,filename)));
export const report = {
  natureza:'Auditoria técnica independente; não é parecer geral nem autorização para próximo ID',
  hashes,
  validacao_real:await validateInventory({rootDir:root}),
  estrutura_individual:structural,
  resumo_estrutural:{artigos:articles.length,registros:inventory.itens.length,ids_unicos:new Set(articles.map(a=>a.id)).size,divergencias:structural.filter(i=>i.errors.length),formatos:structural.reduce((acc,i)=>(acc[i.formato]=(acc[i.formato]??0)+1,acc),{})},
  testes_proprios:tests,
  resumo_testes:{total:tests.length,passaram:tests.filter(t=>t.passou).length,falhas:tests.filter(t=>!t.passou)},
  fixture_temporaria:fixtureRoot,
  limites:['Não consultou PDFs externos; fontes e atribuições comparadas somente ao HTML congelado.','Não examina mérito pedagógico, solução, gabaritos nem suficiência de hipóteses.','Nenhum teste de navegador; produto não modificado.','Não constitui auditoria genérica adversarial do parser HTML ou implementação completa JSON Schema.']
};
