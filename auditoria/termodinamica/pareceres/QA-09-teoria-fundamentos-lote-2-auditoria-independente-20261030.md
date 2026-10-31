# QA-09 — auditoria independente do lote de fundamentos, 30/10/2026

Revisor: agente automatizado independente `/root/qa_fichas`. **Veredito do lote: AJUSTES_OBRIGATÓRIOS** nos trechos 102479 e 114112. Os demais trechos abaixo conferem no alcance indicado. Este parecer não encerra QA-09 nem libera o próximo ID; não substitui os pareceres prévios de FUN-01/FUN-02 e exige reexaminar o alcance afetado por futuras correções.

## Critério, fotografia e identidade

QA-09 exige inventário e recálculo individual do conteúdo numérico, incluindo explicações e não apenas questões. Esta revisão cobre exclusivamente 17 trechos de texto direto do [lote do Corretor](../evidencias/QA-09/teoria-fundamentos-lote-2-20261030/entrega.md), SHA-256 `f28540fedf1a0c49eb03e938770642370c57516d5e40095085f2ceb5711b2588`, e não a totalidade de suas seções. A regra curricular comum não é encerrada por esta verificação parcial.

Fonte examinada: `modulos/e1-termodinamica.html`, SHA-256 `200f9b773050594d762cc596a5a89297024b245fc4f504081fc77baaed3db95f`; inventário r7 `5090b9897a4698e0ad090f45182afba5880361aabc9fd3c3bdf848d971a85a1a`. Posições são UTF-16 desta fotografia; foram lidos os trechos completos e, quando necessário, o contexto. O teste [auditoria-identidade.mjs](../evidencias/QA-09/teoria-fundamentos-lote-2-20261030/auditoria-identidade.mjs), SHA-256 `796e41a95745159f5e201ac111c7edf36c816aba7ab3b133846477bc0ce330d8`, conferiu documento, tipo, posição, limites e os hashes do texto direto para os 17 casos e retornou `ok=true`. Reconstitui a convenção do gerador r7 usando o parser do projeto: o hash é do texto diretamente pertencente ao nó, não necessariamente do HTML inteiro. Isso não é teste de navegador nem prova científica.

## Ajustes obrigatórios

**102479 — afirmação excessiva sobre fração molar e mássica.** A frase “só na substância pura as frações molar e mássica de vapor coincidem” não é geral. Se β é a fração molar vaporizada e Mᵥ e Mₗ as massas molares médias do vapor e do líquido, a fração mássica é

`x = β Mᵥ / [(1 − β) Mₗ + β Mᵥ]`.

Para duas fases presentes (`0 < β < 1`), `x = β` sempre que `Mᵥ = Mₗ`, inclusive em mistura. Contramodelo aritmético: duas espécies de mesma massa molar (por exemplo, isômeros), com médias de fase Mₗ=Mᵥ=58 g/mol e β=0,5, dão x=0,5 independentemente de composições diferentes. A conta `F=2−2+2=2` e o balanço molar `zA=(1−β)xA+βyA` estão corretos no escopo da regra de fases. **Ajustar a frase** para dizer que as frações em geral diferem em misturas, mas coincidem quando as massas molares médias das fases são iguais; para substância pura isso ocorre. Se mantiver a fórmula de conversão, definir claramente bases e médias.

**114112 — origem de medição não informada.** A identidade `ρ=1/v` torna os valores redundantes como coordenadas de estado, mas o enunciado apenas diz que o relatório apresenta os dois dados. A conclusão de que “uma medida foi obtida por inversão da outra” não decorre disso: medições de densidade e volume específico podem ser independentes e compatíveis. **Ajustar a justificativa** para afirmar dependência entre propriedades sem alegar como os valores foram obtidos, ou fornecer expressamente essa informação como hipótese editorial. A conclusão de que o par não fixa, por si só, o estado está correta no modelo delimitado; medições independentes ainda podem oferecer conferência experimental.

Para reapresentar, o Corretor deve atualizar o conteúdo e suas referências, conferir os hashes efetivos e o mapeamento de identidade, examinar a repercussão sobre FUN-01 e outros aceites afetados, preservar os 197 artigos e solicitar nova auditoria. Sem essa revisão, não há aceite do lote.

## Verificações dos demais trechos

| Posição | Resultado, condições e limite |
|---|---|
| 91881 | `0,012/4=0,003 m³/kg`; `3/(3+2)=0,60` na base molar; `1 cm³/g=10⁻³ m³/kg`. Correto. |
| 92203 | `12±3` com erro máximo dá [9,15], sem hipótese probabilística; o intervalo impede garantir valor >10. Correto. |
| 96357 | Para A⇌2B, `2×3−6=0 kJ/mol de extensão`; igualdade de potenciais entre espécies não é exigida. Estacionariedade não prova estabilidade. Correto nas hipóteses do contexto. |
| 101326 | `F=1−1+2=2`, `1−2+2=1`, `1−3+2=0`; não fixa frações de fase. Correto no modelo da regra de fases, sem restrições adicionais. |
| 102086 | Dados NIST a 0,10 MPa: 99,606 °C; 417,50 e 2674,9 kJ/kg; 1,04315 e 1693,9 cm³/g. Conversão e mistura com x=0,20 dão `0,33961452 m³/kg` e `868,98 kJ/kg`, sem inferir precisão adicional. Conferi a [tabela NIST, p. 11](https://www.nist.gov/document/nistir5078-tab2pdf), consulta em 30/10/2026. |
| 105052 | `0,25×400+0,75×100=175 kPa`; invertendo frações, `325 kPa`. Correto para o modelo ideal de bolha e dados fictícios. |
| 105534 | `Tc=647,096 K`, `pc=22,064 MPa` conferem com [IAPWS IF97, §3](https://iapws.org/technical-guidance/release/IF97-Rev.download), consulta em 30/10/2026. A unidade define a região supercrítica com ambas as desigualdades estritas. |
| 108659 | Parciais de A: `80×0,250=160×0,125=20 kPa`; `ln 1=0`; parciais de B: 60 e 140 kPa. Correto na mistura ideal à mesma T e sem inferir estado final. |
| 235496 | `80×0,006=0,480 kPa·m³=0,480 kJ`; inversão dos limites inverte sinal. Correto. |
| 236866 | `f=θν`, parcial em θ com ν fixo é ν; em ν=θ², `f=θ³` e derivada ao longo do caminho é `3θ²`. Correto. |
| 239213 | Na circunferência unitária, `−y dx+x dy=(sin²t+cos²t)dt=dt`, portanto integral `2π`. O furo no domínio impede aplicar condição global de simples conexão. Correto. |
| 239807 | Para Φ=`θ³+θν`, derivadas `3θ²+ν` e `θ`, com derivadas cruzadas iguais a 1. Correto. |
| 244208 | `p(1,5V₀)=2p₀`; integração linear dá `(p₀+2p₀)/2 × 0,5V₀=0,75p₀V₀`. Pressão inicial constante daria `0,50p₀V₀`. Correto para trabalho de fronteira quase estático. |
| 249892 | Derivada de `x ln x−x` é `ln x`, e diferença nos limites 1 e e é `0−(−1)=1`. Correto para x adimensional positivo. |
| 251114 | Pela cadeia, `240/(400 K)=0,600 J/(mol·K)` mantendo as mesmas outras coordenadas. Correto. |

O script do Corretor `verificar.py`, SHA-256 `d7417ba8d282a65e8e106e8f0c20d30a6433d01e5694a9eda6dbd7b13b003085`, foi inspecionado como somente leitura e retornou `ok=true`, 17 ocorrências. O `ok` cobre suas contas e marcadores, mas não detecta as afirmações incorretas apontadas acima; não é aprovação científica. Conferi também os cálculos por frações e os dois contramodelos por leitura própria; os números dos casos são nominais.

## Critérios e decisão

| Critério | Resultado |
|---|---|
| Identidade de todos os 17 trechos na fotografia | Atendido. |
| Cálculos numéricos e fontes externas examinadas | Atendido no alcance descrito. |
| Coerência das hipóteses e conclusões associadas | **Não atendido** em 102479 e 114112; ajustes acima obrigatórios. |
| Critério integral QA-09 e liberação do próximo ID | Não atendidos; demais classes e correções permanecem pendentes. |

Não houve revisão humana, estudo com alunos, ensaio em navegador ou certificação externa. Qualquer edição posterior exige reconciliar a fotografia e revalidar o alcance, não transferir os hashes automaticamente.
