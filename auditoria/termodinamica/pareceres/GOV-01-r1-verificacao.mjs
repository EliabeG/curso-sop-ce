// Auditor AAA automatizado. Verificação independente de integridade e vínculos;
// a pertinência didática de cada par foi examinada em leitura e está no parecer.
import fs from 'node:fs/promises';
import path from 'node:path';
import assert from 'node:assert/strict';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';
const raiz=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../../..');
const ler=p=>fs.readFile(path.join(raiz,p),'utf8');
const hash=s=>crypto.createHash('sha256').update(s).digest('hex');
const antes=await ler('auditoria/termodinamica/evidencias/GOV-01/e1-termodinamica.antes.html');
const atual=await ler('modulos/e1-termodinamica.html');
assert.equal(hash(antes),'a69846fbe1dd1bb8ef3ce3a685ffc2a308d6595a8f95a8637da523e77e231d1d');
assert.equal(hash(atual),'b4e2d672c6feecb4289ad73bb9c16000ff5156720698f10153ff93fa0b788a8e');
function intro(h){
 const marcador='<h2 id="h-objetivos">1. Objetivos e roteiro de estudo</h2>';
 const inicio=h.indexOf(marcador)+marcador.length;
 const fim=h.indexOf('<details class="guia-notacao">',inicio);
 assert.ok(inicio>=marcador.length&&fim>inicio);
 return {inicio,fim,html:h.slice(inicio,fim)};
}
const ia=intro(antes),id=intro(atual);
const leadAntes='Domine propriedades, balanços de energia, segunda lei, ciclos e aplicações em ar comprimido e vapor, com contas sem calculadora.';
const leadAtual='Estude propriedades, balanços de energia e entropia, ciclos e aplicações em ar comprimido e vapor. Treino de concursos e percurso avançado em desenvolvimento.';
assert.equal(antes.split(leadAntes).length,3);assert.equal(atual.split(leadAtual).length,3);
const mascara=(h,i)=>h.slice(0,i.inicio)+'INTRODUCAO'+h.slice(i.fim);
assert.equal(mascara(antes,ia).replaceAll(leadAntes,leadAtual),mascara(atual,id));
const reArtigo=/<article\b[^>]*\bid="(?:q|cr|av)-e1-\d{2}"[^>]*>[\s\S]*?<\/article>/g;
const artigosAntes=[...antes.matchAll(reArtigo)].map(x=>x[0]);
const artigosAtuais=[...atual.matchAll(reArtigo)].map(x=>x[0]);
assert.equal(artigosAntes.length,190);assert.deepEqual(artigosAtuais,artigosAntes);
const ids=h=>[...h.matchAll(/\bid="([^"]+)"/g)].map(m=>m[1]);
const idsAntes=ids(antes),idsAtuais=ids(atual);
assert.equal(new Set(idsAtuais).size,idsAtuais.length);
for(const nome of idsAntes)assert.ok(idsAtuais.includes(nome));
const novos=idsAtuais.filter(nome=>!idsAntes.includes(nome));
assert.deepEqual(novos,['nivel-atual-e1','alcance-e1','resultados-aprendizagem-e1',...Array.from({length:10},(_,i)=>'competencia-c'+String(i+1).padStart(2,'0')),'percurso-atual-e1']);
const destinos=[...id.html.matchAll(/href="#([^"]+)"/g)].map(m=>m[1]);
for(const destino of destinos)assert.equal(idsAntes.filter(x=>x===destino).length,1);
assert.equal(destinos.length,43);
assert.equal(/\bhidden(?:\s|=|>)/.test(id.html),false);
const linhas=[...id.html.matchAll(/<tr id="competencia-c(\d{2})">([\s\S]*?)<\/tr>/g)];
assert.equal(linhas.length,10);
const pares=[
 [['base-fronteira','q-e1-01']],
 [['substancias','q-e1-04']],
 [['base-primeira-lei','q-e1-07'],['base-turbina-potencia','q-e1-11']],
 [['base-entropia','q-e1-18'],['base-entropia-escoamento','q-e1-29']],
 [['base-exergia','av-e1-37']],
 [['base-rankine','q-e1-20'],['base-refrigeracao','q-e1-23']],
 [['base-umidade','av-e1-16'],['base-gas-modelo','av-e1-22'],['base-termoquimica','av-e1-31']],
 [['base-interpolacao','q-e1-26']],
 [['base-segunda-lei','av-e1-39']],
 []
];
for(let i=0;i<10;i++){
 const linha=linhas[i];assert.equal(linha[1],String(i+1).padStart(2,'0'));
 assert.equal((linha[2].match(/scope="row"/g)||[]).length,1);
 assert.equal((linha[2].match(/data-rotulo=/g)||[]).length,4);
 assert.ok(linha[2].includes('Em desenvolvimento:'));
 assert.deepEqual([...linha[2].matchAll(/href="#([^"]+)"/g)].map(m=>m[1]),pares[i].flat());
}
assert.ok(linhas[9][2].includes('ainda não disponíveis'));
assert.ok(linhas[9][2].includes('Não há atividade atual indicada como comprovação de C10'));
assert.ok(id.html.includes('Nível atual: intermediário'));
assert.ok(id.html.includes('não está integralmente ensinado e avaliado'));
assert.ok(id.html.includes('não promete cobrir todas as provas ou editais'));
assert.ok(id.html.includes('não abrange todos os ramos da Termodinâmica'));
const hashes={html:hash(atual)};
for(const [arquivo,esperado] of [
 ['assets/registro.js','444a13658e0b869760296826be30267215293b18c3074f283b2a1ea252e828a2'],
 ['assets/curso.js','81728c9fd1e96b738410e6b51cf4ab3ed785fb17753e68a988c1dcf236d8f899'],
 ['assets/curso.css','b8ded6abc4548f378daab2e299a8a55ba81e8841c41049133a84d93848ee3eaa']
]){hashes[arquivo]=hash(await ler(arquivo));assert.equal(hashes[arquivo],esperado);}
export const resultado={id:'GOV-01',rodada:1,revisor:'Agente automatizado Auditor AAA /root/auditor_aaa',metodo:'Verificação estática independente; sem navegador',hashes,artigos_preservados:190,BAN01_preservado:true,ids:{anteriores:idsAntes.length,atuais:idsAtuais.length,novos,duplicados:0},links_validos:destinos.length,linhas:linhas.map((l,i)=>({competencia:'C'+l[1],pares:pares[i],estado_ensino_avaliacao_avancados:'em desenvolvimento'})),conteudo_fora_do_escopo_preservado:true};
