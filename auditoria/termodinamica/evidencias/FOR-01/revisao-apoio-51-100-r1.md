# FOR-01 r1 — apoio das fichas 51–100

Registro anterior à implementação. Apoio do Corretor; não é parecer independente nem fechamento de FOR-01/FOR-02.

Foram lidas individualmente as 50 fichas (MathML, data-busca, condições e símbolos) e o conteúdo efetivo de todos os alvos. Resultado: **19 manter, 30 corrigir e 1 dependência**. “Corrigir” inclui definições locais incompletas; não significa 30 fórmulas algébricas erradas.

O [JSON](revisao-apoio-51-100-r1.json) contém por ficha: expressões originais, confronto entre representações, unidades/sinais, hipóteses, suporte da aula, motivo, proposta concreta e fontes consultadas. Nenhum arquivo de produto ou controle foi alterado.

Pontos principais para integração:

- **51:** entrada com entalpia constante; a expressão sem essa condição pede média ponderada pela massa.
- **62:** fixar QH e temperaturas para definir W máximo e rejeição mínima.
- **64 e 73:** temperatura local em cada contato; não dividir o calor líquido por uma temperatura arbitrária.
- **71–72 e 76:** explicitar regime/modelo necessário à redução por entalpia.
- **79:** vínculo parcial com #base-rankine; acrescentar o mapeamento 1–4 e os quatro balanços no próprio alvo. Proposta curta consta do JSON.
- **85:** #base-refrigeracao contém o exemplo explícito do balanço do condensador e é um alvo mais direto.
- **88:** média geométrica minimiza trabalho sob o modelo simétrico especificado; condições e demonstração de mínimo estão no JSON.
- **89:** excluir np=0 além de np=1; domínio proposto para compressão convencional: np>0, np≠1, p₂>p₁>0.
- **91–93:** definir eixo/componente de Q̇, área normal e coeficiente convectivo médio. Na 92, a fórmula já tem sinal correto; a ambiguidade é a frase “positivo no sentido 1→2”.
- **94–95:** U e média térmica compatíveis com o método; em tubos a condução tem resistência cilíndrica, não apenas troca de área.
- **98–99:** explicitar aproximação linear da dilatação e uniformidade/média das grandezas multiplicadas por área/volume.

| Nº | ID | Decisão | Motivo concreto |
|---:|---|---|---|
| 51 | `formula-enchimento-tanque` | corrigir | Sem h_in constante, o lado direito é a entalpia média ponderada pela massa admitida, não um valor instantâneo não especificado. |
| 52 | `formula-co2-acumulacao` | corrigir | A ficha isolada permite confundir geração volumétrica com mássica ou vazão de renovação com recirculação. |
| 53 | `formula-co2-vazao` | corrigir | A redução herda hipóteses do balanço, além de dCi/dt=0; são importantes para uma ficha autônoma. |
| 54 | `formula-renovacoes` | manter | Definição, unidade e alcance estão claros. |
| 55 | `formula-bomba-potencia` | corrigir | A expressão não representa só desnível geométrico nem a eficiência conjunta motor+bomba. |
| 56 | `formula-misturador-correntes` | corrigir | Sem sinal explícito na ficha, o termo +Q̇−Ẇ pode ser usado ao contrário. |
| 57 | `formula-bocal-difusor` | manter | Forma de energia, conversão e condições estão adequadas. |
| 58 | `formula-eficiencia` | manter | A expressão não troca sinais de calor nem equipara rendimento a COP. |
| 59 | `formula-cop-refrigerador` | manter | Definição correta para a fronteira indicada. |
| 60 | `formula-cop-bomba-calor` | manter | Balanço QH=QL+Win sustenta a diferença unitária. |
| 61 | `formula-carnot` | manter | Hipóteses e limite estão corretos. |
| 62 | `formula-limites-carnot` | corrigir | Sem QH dado/fixo, aumentar QH altera o máximo de trabalho; “reservatórios fixos” sozinho não define esse limite absoluto. |
| 63 | `formula-cop-carnot` | corrigir | A relação deve excluir temperatura absoluta nula e ser autocontida quanto às siglas. |
| 64 | `formula-balanco-entropia` | corrigir | Não é erro algébrico se a integral já representa todas as transferências locais; é ambiguidade de alcance num balanço apresentado como geral. |
| 65 | `formula-entropia-isolado` | manter | É redução legítima do balanço geral sob isolamento. |
| 66 | `formula-entropia-total` | manter | A fronteira total está especificada, evitando aplicar a desigualdade a qualquer subsistema. |
| 67 | `formula-calor-reversivel` | manter | Expressão e restrição corretas; alvo amplo contém realmente o ensino pertinente. |
| 68 | `formula-entropia-tp` | corrigir | A matemática é correta; completar identificação explícita da constante específica R e de Δs evita confusão com constante universal. |
| 69 | `formula-entropia-tv` | corrigir | Completar símbolos/unidades, sem alterar expressão válida. |
| 70 | `formula-isentro-gas` | corrigir | Nenhum expoente invertido; apenas completar unidade/domínio para consulta autônoma. |
| 71 | `formula-isentropica-turbina` | corrigir | Queda de entalpia equivale a trabalho específico sob escoamento estacionário, não em qualquer turbina transiente. |
| 72 | `formula-isentropica-compressor` | corrigir | O denominador de trabalho exige a redução estacionária e os estados precisam ser identificados localmente. |
| 73 | `formula-entropia-vc` | corrigir | A forma discreta é correta para os contatos definidos. Delimitar essa discretização evita usar uma temperatura média arbitrária. |
| 74 | `formula-exergia` | manter | Relação e alcance bem delimitados; não confunde exergia destruída com transportada. |
| 75 | `formula-identidades` | manter | Nenhuma exigência indevida de processo real reversível: são identidades de propriedades. |
| 76 | `formula-entalpia-isentro` | corrigir | ds=0 sozinho não elimina contribuições químicas ou outros modos de trabalho de uma identidade mais geral. |
| 77 | `formula-gibbs-fases` | corrigir | Igualdade de μ é condição de coexistência acessível ao componente; a frase não deve sugerir critério suficiente de estabilidade nem cobrir campos sem termos adicionais. |
| 78 | `formula-entropia-c-variavel` | corrigir | Matemática correta; identificação de R deve excluir constante universal na base por kg. |
| 79 | `formula-rankine` | dependencia | Vínculo existente é parcial: a ficha reúne relações válidas que não são ensinadas integralmente no alvo. Dependência local de completar a explicação, sem ampliar FOR-02. |
| 80 | `formula-brayton-liquido` | manter | Não confunde potência bruta com útil nem calor regenerado com externo. |
| 81 | `formula-brayton-ideal` | manter | Forma correta para o Brayton simples ar-padrão; não aplicável automaticamente ao regenerativo. |
| 82 | `formula-otto` | manter | Vínculo amplo mas suficiente e expressão correta. |
| 83 | `formula-diesel` | corrigir | Acrescentar domínio operacional 1<rc<r para o Diesel convencional não degenerado e símbolos faltantes. |
| 84 | `formula-refrigeracao` | corrigir | Completar hipóteses dos trocadores e válvula torna os balanços por h verificáveis sem exigir compressor isentrópico. |
| 85 | `formula-condensador` | corrigir | Expressão correta; direcionar o link ao trecho que realmente demonstra o balanço do calor rejeitado. |
| 86 | `formula-extracao-aquecedor` | manter | A expressão é uma redução delimitada de um misturador, sem universalizar a todos os aquecedores. |
| 87 | `formula-volumetrica` | manter | Definição e referência suficientes para compressor volumétrico. |
| 88 | `formula-intermediaria` | corrigir | Média geométrica é resultado de um problema de mínimo sob modelo simétrico específico. Não é consequência universal de “dois estágios” ou da igualdade de eficiências em um ponto. |
| 89 | `formula-politropico` | corrigir | Corrigir domínio matemático e físico do modelo, preservando a expressão. |
| 90 | `formula-compressao-isotermica` | manter | Expressão correta como modelo isotérmico, sem confundir processo adiabático. |
| 91 | `formula-fourier` | corrigir | Alinhar as duas expressões e convenção geométrica evita interpretar Q̇=q″A para área oblíqua. |
| 92 | `formula-gradiente` | corrigir | Não há erro de sinal na fórmula. Corrigir a frase ambígua para se referir explicitamente à componente de Q̇. |
| 93 | `formula-newton` | corrigir | Se hc variar na área, a forma total continua válida com sua média apenas quando a diferença térmica é uniforme. |
| 94 | `formula-ua` | corrigir | A palavra “efetiva” não deve permitir uma média arbitrária; a ficha precisa ligar as grandezas ao método do arranjo. |
| 95 | `formula-resistencias` | corrigir | Evitar que o aluno transporte a parede plana para cilindro corrigindo somente a área. |
| 96 | `formula-radiacao` | corrigir | A fórmula é troca líquida da superfície, não emissão bruta; delimitar participação do meio evita aplicar em gases radiativamente participantes. |
| 97 | `formula-razao-radiativa` | manter | Não generaliza proporcionalidade para outros mecanismos ou geometrias. |
| 98 | `formula-dilatacao` | corrigir | Com α=(1/L)dL/dT constante, a integração exata dá exponencial. A fórmula é primeira ordem ou usa coeficiente secante na faixa, não identidade universal. |
| 99 | `formula-geracao` | corrigir | Produtos q‴V e hcAΔT pressupõem grandezas uniformes ou médias compatíveis. |
| 100 | `formula-geometria` | manter | Geometria e escolha de face coerentes; sem ampliação implícita para todas as faces. |

As 30 fontes utilizadas e os resultados das consultas estão no JSON, junto às relações com cada ficha. As rederivações são próprias; os trechos consultados por índice estão assim identificados. Não foi executado teste visual, auditoria numérica integral do banco ou ampliação curricular. As mudanças sugeridas devem sincronizar ficha visível, MathML quando alterado e data-busca.
