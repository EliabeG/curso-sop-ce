/** Integração restrita BAN-10 sobre a base preservada; não altera controles de auditoria. */
import fs from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import {parseHtml,sha256,resourceReferences} from '../../inventario/validar-inventario.mjs';
import path from 'node:path';
const root=fileURLToPath(new URL('../../../../',import.meta.url));
const dir='auditoria/termodinamica/evidencias/BAN-10/';
const src={
 si:['BIPM, Brochura do SI, 9ª ed., v4.01 (2026), §2.3.1 e tabela 4','https://www.bipm.org/en/publications/si-brochure'],
 gas:['OpenStax, University Physics 2, §2.1, equação 2.2','https://openstax.org/books/university-physics-volume-2/pages/2-1-molecular-model-of-an-ideal-gas'],
 energia:['MIT Unified, §2.1, balanço da energia total','https://web.mit.edu/16.unified/www/SPRING/thermodynamics/notes/node14.html'],
 segunda:['OpenStax, University Physics 2, §4.4, Kelvin–Planck','https://openstax.org/books/university-physics-volume-2/pages/4-4-statements-of-the-second-law-of-thermodynamics'],
 brayton:['MIT Unified, §3.7, quatro processos do Brayton','https://web.mit.edu/16.unified/www/SPRING/propulsion/notes/node27.html'],
 volume:['H. DeVoe, Thermodynamics and Chemistry, 2ª ed., v5 (2014), §7.1, pp. 163–165','https://faculty.washington.edu/gdrobny/v5-screen.pdf#page=163'],
 compressor:['GUNT, ET 508, princípio da reexpansão no compressor alternativo','https://gunt.de/en/products/fluid-machinery/driven-machines/fans-and-compressors/simulation-of-a-two-stage-air-compressor/061.50800/et508/glct-1:pa-148:ca-752:pr-240'],
 radiacao:['OpenStax, University Physics 2, §1.6, radiação líquida','https://openstax.org/books/university-physics-volume-2/pages/1-6-mechanisms-of-heat-transfer'],
 vacuo:['NASA, Thermal Control (07/05/2026), §§7.2.1 e 7.2.3','https://www.nasa.gov/smallsat-institute/sst-soa/thermal-control/']
};
export const casos=[
 {n:'04',critico:true,fonte:'volume',original:68,key:'C',doc:'p22p',pagina:1,
 motivo:'Sensibilidades a grandezas de dimensões diferentes não são ordenáveis sem definir estado, escalas e perturbações.',
 nota:'A chave oficial C representa a comparação qualitativa usual para líquidos. O texto não define a faixa nem como comparar perturbações de temperatura e pressão; por isso esta pergunta será estudada criticamente, sem entrar no placar.',
 pergunta:'Identifique a condição omitida na comparação. É possível ordenar diretamente uma derivada por kelvin e outra por pascal? Explique como formular uma comparação física verificável.',
 analise:'Para massa fixa de líquido em uma fase, dv/v = α dT − κ<sub>T</sub> dp, com α = (1/v)(∂v/∂T)<sub>p</sub> e κ<sub>T</sub> = −(1/v)(∂v/∂p)<sub>T</sub>. α tem unidade K⁻¹ e κ<sub>T</sub>, Pa⁻¹. Devem-se comparar efeitos como |αΔT| e |κ<sub>T</sub>Δp|, na mesma faixa e com propriedades adequadas. Baixa compressibilidade não prova uma desigualdade universal entre esses efeitos. A leitura usual da chave é plausível, mas as escalas necessárias não foram especificadas.',
 criterio:'Reconhecer a leitura usual C, recusar a comparação direta entre dimensões diferentes e indicar estado/faixa e perturbações necessárias. Uma discordância fundamentada não recebe erro no placar.'},
 {n:'09',critico:true,fonte:'si',original:39,key:'E',doc:'tc',pagina:1,
 motivo:'O item omite a restrição a temperatura termodinâmica/unidade de base; grau Celsius também é unidade SI.',
 nota:'O original e a chave E são preservados. A expressão unidade de temperatura no SI não especifica a unidade de base da temperatura termodinâmica. A leitura com essa restrição é diferente da leitura literal sobre unidades SI.',
 pergunta:'Diferencie temperatura termodinâmica e temperatura Celsius. Explique em qual leitura a chave E é coerente e por que isso não permite afirmar que °C esteja fora do SI.',
 analise:'A temperatura termodinâmica usa o kelvin como unidade de base. A temperatura Celsius é t = T − 273,15 K e sua unidade SI é o grau Celsius. A chave E é coerente ao restringir a frase à unidade de base da temperatura termodinâmica; a restrição não aparece expressamente no comando. O curso não atribui essa interpretação à banca como justificativa documentada.',
 criterio:'Nomear as duas grandezas/unidades, localizar a restrição adicional e preservar a distinção entre chave documental e interpretação técnica.'},
 {n:'24',critico:true,fonte:'gas',original:52,key:'E',doc:'trf',pagina:1,
 motivo:'A razão literal entre pressão de gás e pressão de água não é determinada; a interpretação de termômetro exige a mesma amostra de gás.',
 nota:'A frase oficial compara pressões de substâncias diferentes. O quociente entre temperaturas somente resolve outra leitura, em que o ponto triplo é uma referência térmica para a mesma amostra gasosa.',
 pergunta:'Escreva a razão pedida na leitura literal e identifique o dado ausente. Depois declare explicitamente a hipótese que permite usar 373,15/273,16.',
 analise:'Na leitura literal, p<sub>gás</sub>/p<sub>água</sub> = (nR·373,15/V)/p<sub>água</sub>: falta n/V, mesmo se a pressão da água no ponto triplo fosse conhecida. O número 1 não pode ser julgado pela razão de temperaturas de substâncias diferentes. <strong>Suplemento autoral:</strong> se forem pressões da mesma amostra ideal, com n e V constantes, em equilíbrio térmico a 373,15 K e 273,16 K, então p₂/p₁ ≈ 1,366. Essa é uma leitura condicionada compatível com E, não uma emenda silenciosa ao original nem uma definição atual do kelvin.',
 criterio:'Apontar n/V ausente na leitura literal e distinguir a pressão da água da pressão do gás termométrico; só aplicar a razão térmica após declarar mesma amostra e volume.'},
 {n:'34',critico:true,fonte:'energia',original:53,key:'C',doc:'trf',pagina:1,
 motivo:'Volume constante elimina trabalho de fronteira, mas não exclui outros trabalhos nem mudanças macroscópicas de energia.',
 nota:'A leitura elementar que sustenta C usa massa fixa, somente trabalho de expansão e ausência de variações de energia cinética/potencial. O comando fornece volume constante, mas não todas essas restrições.',
 pergunta:'Qual parcela de trabalho desaparece por ser isocórico? Quais hipóteses adicionais são necessárias para concluir ΔU = Q > 0?',
 analise:'Para sistema fechado, ΔU + ΔE<sub>c</sub> + ΔE<sub>p</sub> = Q − W. Volume constante zera o trabalho de fronteira, não necessariamente trabalhos elétricos ou de eixo. Com massa fixa, esses outros trabalhos ausentes e ΔE<sub>c</sub> = ΔE<sub>p</sub> = 0, chega-se a ΔU = Q > 0 e, no gás ideal com capacidade térmica positiva, a aumento de T. Essas são condições da interpretação, não informações expressas no original.',
 criterio:'Separar trabalho de fronteira de trabalho total e declarar as condições de massa/energia. Não inferir W total nulo apenas de ΔV = 0.'},
 {n:'35',critico:true,fonte:'energia',original:54,key:'C',doc:'trf',pagina:1,
 motivo:'A conclusão usa energia interna onde a lei geral envolve energia total; faltam condições de energia cinética/potencial.',
 nota:'A chave C é coerente com o modelo em que as energias cinética e potencial não variam. Fechado e adiabático, por si sós, não impõem essas duas condições.',
 pergunta:'Reescreva o balanço antes de desprezar parcelas. Uma elevação do sistema, com trabalho recebido e sem calor, precisa aumentar sua energia interna?',
 analise:'Com Q = 0, o balanço é ΔU + ΔE<sub>c</sub> + ΔE<sub>p</sub> = −W. Portanto ΔU = −W apenas se a soma das variações macroscópicas for nula. Num levantamento ideal sem mudança de velocidade ou estado interno, o trabalho recebido pode corresponder a ΔE<sub>p</sub>, com ΔU = 0. O exemplo é um contramodelo autoral, não dado da prova. A chave conserva sentido no modelo usual de sistema em repouso e sem alteração de elevação.',
 criterio:'Manter a convenção W produzido positivo, escrever o balanço total e explicar a condição de redução a ΔU = −W.'},
 {n:'39',critico:true,fonte:'segunda',original:66,key:'C',doc:'p22p',pagina:1,
 motivo:'A conclusão de Kelvin–Planck exige explicitar calor total, trabalho líquido e ausência de outros efeitos; motor de combustão real não é automaticamente uma massa fechada cíclica.',
 nota:'O cálculo 350 × 4,2 = 1.470 J é inequívoco. O passo que conclui violação da segunda lei pressupõe uma máquina térmica cíclica ideal com essas trocas totais, não qualquer fronteira de um motor de combustão.',
 pergunta:'Declare a fronteira e o significado de calor recebido e trabalho. Em que condições a igualdade entre os dois números contradiz Kelvin–Planck? O que mudaria com fluxos de massa ou outras trocas?',
 analise:'No modelo convencional, 350 cal são todo o calor recebido de uma única fonte e 1.470 J são o trabalho líquido de um ciclo, sem outros efeitos. Então Q<sub>entra</sub> = W<sub>líq</sub>, Q<sub>rejeitado</sub> = 0, e Kelvin–Planck impede essa conversão integral. A chave C é coerente nesse recorte. Num motor de combustão real, a fronteira pode ter entrada/saída de massa e energia química; os dois números isolados não definem o balanço completo. A exclusão editorial evita premiar somente a escolha tácita de uma fronteira.',
 criterio:'Fazer a conversão correta, declarar totalidade das trocas e ciclo líquido, e distinguir modelo térmico de balanço de combustão com massa.'},
 {n:'51',critico:false,fonte:'brayton',original:98,key:'C',doc:'to',pagina:4,
 motivo:'O ciclo nomeado é tomado em seu modelo ideal convencional, cujos quatro processos não são isotérmicos; não se afirma isso para todas as modificações ou máquinas reais.',
 nota:'Mantido no treino: a identificação do ciclo Brayton remete ao modelo ideal convencional ensinado na base. A chave C refere-se a esse ciclo com processos não degenerados; não é uma afirmação sobre toda modificação tecnológica ou turbina real.',
 analise:'Compressão/expansão isentrópicas e aquecimento/resfriamento isobáricos formam o Brayton ideal convencional. A descrição do ciclo nomeado é suficiente para a leitura de reconhecimento aqui adotada; versões modificadas devem ser identificadas à parte. Não se acrescenta uma medida de autonomia avançada por reconhecer esse modelo.'},
 {n:'55',critico:false,fonte:'brayton',original:47,key:'E',doc:'tm',pagina:1,
 motivo:'Há expressão anômala oficial, porém o resfriamento isocórico já torna falsa a descrição do Brayton convencional independentemente dela.',
 nota:'Mantido no treino com ressalva documental: a expressão “pressão isentrópica” já consta da prova oficial. Não foi criada pelo curso e não é silenciosamente substituída. O resfriamento a volume constante, também escrito no original, basta para rejeitar a descrição do Brayton ideal.',
 analise:'A expressão “pressão isentrópica” não nomeia adequadamente um processo e não revela, por si, o que o autor pretendia. Independentemente de sua possível leitura, a rejeição de calor isocórica contradiz o Brayton ideal convencional, que a realiza a pressão constante. Assim E permanece justificável sem adivinhar uma correção tipográfica. Não há aqui errata oficial ou declaração de intenção da banca.'},
 {n:'62',critico:true,fonte:'compressor',original:59,key:'C',doc:'tm',pagina:1,
 motivo:'Durante esse movimento pode designar a etapa de admissão ou toda a descida, que pode incluir reexpansão com ambas as válvulas fechadas.',
 nota:'A chave C descreve a fase em que há admissão. A leitura de “durante esse movimento” como toda a descida do pistão não é equivalente quando existe volume residual.',
 pergunta:'Distinga o movimento de aumento do volume e o intervalo em que efetivamente entra gás. O que ocorre com as válvulas antes da admissão quando há gás residual?',
 analise:'Após a descarga, o gás retido na folga reexpande no início do retorno do pistão. Nessa parte, as duas válvulas podem permanecer fechadas; a admissão só começa quando a diferença de pressão a permite. Durante a admissão propriamente dita, a entrada está aberta e a descarga fechada, coerente com C. Sem delimitar o intervalo, o texto comporta essas duas leituras. “Desce” também depende da orientação; a referência física é o aumento do volume da câmara.',
 criterio:'Separar retorno/reexpansão de admissão, identificar as válvulas em cada fase e evitar transformar direção geométrica em condição universal.'},
 {n:'68',critico:false,fonte:'radiacao',original:85,key:'C',doc:'p24',pagina:3,
 motivo:'A afirmação de possibilidade de reduzir perda radiativa é válida para superfície quente com demais condições comparáveis, independentemente dos dados de água defeituosos.',
 nota:'Mantido no treino — BAN-10: a afirmação fala em possibilidade de reduzir perdas. Para uma superfície mais quente que a vizinhança, mantendo temperaturas, área e geometria comparáveis, reduzir emissividade reduz a parcela radiativa. Os dados de água não entram nesse julgamento.',
 analise:'No modelo de superfície cinzenta diante de grande vizinhança isotérmica, Q̇<sub>rad</sub> = εσA(T<sub>s</sub>⁴ − T<sub>v</sub>⁴). Com T<sub>s</sub> > T<sub>v</sub> e demais fatores mantidos, a redução de ε diminui essa parcela. Isso fundamenta a possibilidade expressa pela chave C, sem prometer redução igual de convecção/condução ou manter automaticamente T<sub>s</sub> num equipamento real. O conjunto corrigido FON-09 e sua transcrição histórica continuam separados e preservados.'},
 {n:'79',critico:true,fonte:'vacuo',original:30,key:'B',doc:'inpe',pagina:8,gabPagina:4,
 motivo:'Alto vácuo reduz troca gasosa, mas não fixa predominância radiativa frente à condução por suportes e cabos.',
 nota:'O original e a alternativa oficial B são preservados como documento. A predominância radiativa não decorre apenas de alto vácuo e da temperatura das paredes; faltam as ligações térmicas, propriedades e geometria do equipamento.',
 pergunta:'Quais mecanismos continuam possíveis? Construa duas montagens compatíveis com o enunciado, uma com radiação predominante e outra com condução predominante. Quais dados distinguiriam as duas?',
 analise:'A condução por suportes/cabos pode competir com a radiação; alto vácuo não fixa essa razão. <strong>Contramodelo autoral, não dado da prova:</strong> corpo a 300 K, área 0,10 m², superfícies negras e grande parede a 77,15 K dão aproximadamente 45,73 W radiativos. Se a ligação sólida à parede tiver condutância G = 0,01 W/K, conduz cerca de 2,23 W; com G = 0,50 W/K, conduz 111,43 W. As duas montagens respeitam o contexto térmico, mas invertem a predominância. A chave B corresponde à primeira leitura, sem ser demonstrada pelos dados originais. A troca gasosa foi desprezada nesse contramodelo; não se afirma pressão residual rigorosamente nula.',
 criterio:'Reconhecer radiação e condução sólida, apresentar condição/contramodelo que altere sua razão e não usar apenas a palavra vácuo como prova de predominância.'},
 {n:'80',critico:true,fonte:'energia',original:38,key:'D',doc:'cae',pagina:4,
 motivo:'Uniformidade espacial da superfície não determina acumulação nula; o valor único usa regime permanente e convecção como única troca exposta.',
 nota:'A chave D usa um balanço sem acumulação, com convecção como única troca da face exposta. A uniformidade espacial de Tₛ declarada no texto não estabelece constância no tempo.',
 pergunta:'Escreva o balanço com acumulação antes de usar as dimensões. Qual hipótese leva a 40 °C? Uma face espacialmente uniforme pode aquecer no tempo?',
 analise:'Com as dimensões fornecidas, V = 4 m³, A = 4 m² e geração = 400 W. No modelo de única saída por convecção, dU/dt = 400 − 40(T<sub>s</sub> − 30) W. Se dU/dt = 0, T<sub>s</sub> = 40 °C, a chave D. A igualdade espacial de temperatura sobre a face não impõe essa condição temporal. Se houver radiação ou outra saída, seu termo também deve entrar no balanço. A resolução de referência é válida sob essas hipóteses adicionais, não como determinação geral a partir da uniformidade da face.',
 criterio:'Manter o termo de acumulação, separar uniformidade espacial de regime permanente e explicitar o modelo de troca superficial antes de obter 40 °C.'}
];
export async function integrar(){
  let html=await fs.readFile(root+dir+'antes/e1-termodinamica.html','utf8');
  if(await fs.readFile(root+'modulos/e1-termodinamica.html','utf8')!==html)throw Error('HTML já mudou; não sobrescrever');
  const fonteDocs=JSON.parse(await fs.readFile(root+'downloads/termodinamica/fontes.json','utf8')).arquivos;
  const records=[];
  for(const c of casos){
    const id='cr-e1-'+c.n,doc=parseHtml(html),a=doc.ids.get(id)[0],old=html.slice(a.start,a.end);let raw=old;
    if(c.critico)raw=raw.replace('<article ','<article data-cr-avaliacao="estudo-critico" ');
    const note='<p class="cr-nota-leitura"><strong>'+(c.critico?'Estudo crítico — fora da pontuação':'Leitura técnica e uso no treino')+' (BAN-10, 27/10/2026).</strong> '+c.nota+(c.critico?' A marcação abaixo serve somente para comparar com o gabarito oficial; não recebe acerto/erro nem nota de domínio.':'')+'</p>';
    if(c.n==='68')raw=raw.replace('<p><strong>Afirmação a julgar',note+'\n<p><strong>Afirmação a julgar');
    else if(raw.includes('<p class="cr-nota-leitura">'))raw=raw.replace(/<p class="cr-nota-leitura">[\s\S]*?<\/p>/,note);
    else raw=raw.replace('<div class="cr-enunciado"',note+'\n<div class="cr-enunciado"');
    raw=raw.replace('<div class="cr-enunciado"','<p><strong>Texto oficial preservado:</strong> confira o documento original e sua página nos links deste item.</p>\n<div class="cr-enunciado"');
    if(c.critico){
      raw=raw.replace('<fieldset ', '<div class="box box-dica" role="note"><p class="box-titulo">Roteiro autoral de estudo crítico</p><p>'+c.pergunta+'</p><p>Registre sua justificativa antes de abrir a análise. A comparação automática da letra não corrige essa justificativa.</p></div>\n<fieldset ');
      raw=raw.replace(/<legend>.*?<\/legend>/,'<legend>Marcação documental: compare depois com a chave oficial; sem pontuação.</legend>');
      raw=raw.replace('>Conferir resposta</button>','>Comparar com a chave oficial</button>');
      raw=raw.replace('<summary>Ver gabarito e resolução</summary>','<summary>Ver chave oficial e análise crítica autoral</summary>');
    }
    const ref=src[c.fonte],end=raw.lastIndexOf('</details>');
    const block='<div id="'+id+'-analise-ban10"><h4>Interpretação técnica autoral — BAN-10</h4><p>'+c.analise+'</p>'+(c.criterio?'<p><strong>Critério de autocorreção, sem nota:</strong> '+c.criterio+'</p>':'')+'<p><strong>Fundamentação:</strong> <a href="'+ref[1]+'" rel="noopener noreferrer" target="_blank">'+ref[0]+'</a>. Consulta em 27/10/2026. O comentário é do curso; a letra oficial não constitui justificativa técnica da banca.</p></div>\n';
    raw=raw.slice(0,end)+block+raw.slice(end);
    const prova=fonteDocs.find(x=>x.source===c.doc&&x.tipo==='prova'),gab=fonteDocs.find(x=>x.source===c.doc&&x.tipo==='gabarito');
    const local='<p class="cr-fontes"><strong>Conferência documental BAN-10:</strong> <a data-recurso="obrigatorio" href="../downloads/termodinamica/'+prova.arquivo+'#page='+c.pagina+'">Prova local · item '+c.original+' · PDF p. '+c.pagina+'</a> · <a data-recurso="obrigatorio" href="../downloads/termodinamica/'+gab.arquivo+'#page='+(c.gabPagina||1)+'">Gabarito local · '+c.key+' · PDF p. '+(c.gabPagina||1)+'</a>'+(c.n==='79'?' (página física 4; o rodapé impresso desta folha diz “Página 1 de 11”)':'')+'. A decisão de uso no curso é editorial; não é anulação ou errata oficial.</p>\n';
    raw=raw.replace(/<\/article>$/,local+'</article>');
    html=html.slice(0,a.start)+raw+html.slice(a.end);
    records.push({...c,id,decisao:c.critico?'estudo_critico_sem_pontuacao':'manter_treino_delimitado',sha256_artigo_antes:sha256(old),sha256_artigo_depois:sha256(raw),fontes_tecnicas:[{titulo:ref[0],url:ref[1],consulta:'2026-10-27'}],fontes_oficiais:[{arquivo:'downloads/termodinamica/'+prova.arquivo,url:prova.url,pagina_pdf:c.pagina,sha256:prova.sha256},{arquivo:'downloads/termodinamica/'+gab.arquivo,url:gab.url,pagina_pdf:c.gabPagina||1,sha256:gab.sha256}]});
  }
  html=html.replace('Os originais 09, 24, 68 e 79 possuem notas de leitura sobre ambiguidades ou dados de apoio. O placar compara sua marcação com o gabarito oficial; nessas questões, estude também as ressalvas, pois acertar a alternativa oficial não elimina a limitação do enunciado.','Os itens <a href="#cr-e1-04">04</a>, <a href="#cr-e1-09">09</a>, <a href="#cr-e1-24">24</a>, <a href="#cr-e1-34">34</a>, <a href="#cr-e1-35">35</a>, <a href="#cr-e1-39">39</a>, <a href="#cr-e1-62">62</a>, <a href="#cr-e1-79">79</a> e <a href="#cr-e1-80">80</a> são <strong>estudos críticos, sem pontuação</strong>: ficam fora do denominador e dos acertos/erros. A interface registra apenas se sua letra coincide com a chave oficial e oferece roteiro de justificativa, com autocorreção separada. Os demais 71 itens permanecem no placar de treino; isso não certifica domínio avançado nem encerra a auditoria numérica geral. As marcações antigas dos estudos críticos são conservadas como histórico documental e deixam de pontuar nesta versão. <a href="#cr-e1-51">51</a>, <a href="#cr-e1-55">55</a> e <a href="#cr-e1-68">68</a> têm decisões de manutenção fundamentadas. Nenhuma exclusão editorial significa anulação pela banca.');
  await fs.writeFile(root+'modulos/e1-termodinamica.html',html);
  await fs.writeFile(root+dir+'e1-termodinamica.r1.html',html);
  await fs.writeFile(root+dir+'decisoes-r1.json',JSON.stringify({id:'BAN-10',rodada:1,data:'2026-10-27',autor:'Corretor AAA, agente automatizado',alcance:'Decisões editoriais localizadas; não são anulações oficiais, parecer de aprovação ou auditoria global BAN07/BAN08/FON01.',divergencia_cr39:'O apoio considerou o modelo usual suficiente. O Corretor escolhe exclusão conservadora por não explicitar totalidade das trocas e fronteira do motor de combustão; a chave C é coerente sob modelo térmico convencional declarado.',criticos:records.filter(x=>x.critico).map(x=>x.id),mantidos:records.filter(x=>!x.critico).map(x=>x.id),itens:records},null,2)+'\n');
  return {html_sha256:sha256(html),artigos_alterados:records.length,criticos:records.filter(x=>x.critico).length};
}
