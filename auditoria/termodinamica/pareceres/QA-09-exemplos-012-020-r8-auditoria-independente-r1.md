# QA-09 — auditoria independente dos exemplos EX-012 e EX-014–020 em r8

Data: 30/10/2026. Revisor: agente automatizado independente `/root/audit_strategy`. **Veredito localizado: APROVADO para a identidade, interpretação e recálculo dos oito blocos abaixo, nos modelos descritos.** EX-011 e EX-013 não fazem parte desta revisão. A decisão não encerra QA-09 nem libera o próximo ID.

## Versão, método e abrangência

HTML efetivo `modulos/e1-termodinamica.html`, SHA-256 `57b13f0d6386764f1cc46ce543013b0eb75f7bfa97ffbd63ea331f38bfc5af8c`; inventário r8 `ae75a258398c385398567457d98ebd49b9838c0c9a4eedc69ea8d2d72981b687`; mapa histórico dos IDs EX `892b63067b87316009a89a8553e8288a9bc51c2c66929b33a4fd19d927d2ede9`. Entrega do Corretor `exemplos-012-020-r8-corretor-20261030/entrega.md`, SHA-256 `901605b516563bfd648e32380a2c81923ee52b241dfe12a5744499c1064f04d5`; seu resultado JSON `577a64593f530cedfbfd265bcb842206ea37ab44be3890c6781f4b49652013fe` foi reproduzido byte a byte pelo script do Corretor, inspecionado antes de executar.

Confrontei diretamente os oito fragmentos efetivos, títulos e bases de balanço, caminhos, expansão livre, calorimetria, mistura, mudança de fase e transiente. Os IDs EX pertencem ao mapa histórico, não ao HTML. Script independente [`verificar.py`](../evidencias/QA-09/auditoria-exemplos-012-020-r8-r1/verificar.py), SHA-256 `c454fae2b009953bd050a03af44b5a7a1ed9c54d05317c96d81e18afa51c69d1`, confirma em r8 a ocorrência única por documento, seção, título e hash, extrai cada intervalo UTF-16 e refaz as contas com os dados nominais. Lê arquivos e escreve somente em stdout. Igualdade de fragmento não transfere automaticamente aceites de outras versões ou das bases completas.

## Conferência independente

| ID | Hipóteses e cálculo | Resultado |
|---|---|---|
| EX-012 | Sistema fechado, Q recebido e W saindo positivos; variações cinética e potencial desprezíveis. Com o fator **adotado no exercício** de 4,2 J/cal, Q = 100 × 4,2 = 420 J, ΔU = 420 − 120 = 300 J e U₂ = 50 + 300 J. | **350 J**, correto. A caloria termoquímica definida por 4,184 J produziria 348,4 J, mas não é o fator escolhido neste exemplo. |
| EX-014 | Para massa fixa de gás ideal, A: 300 kPa × 1 m³ e B: 100 kPa × 3 m³ têm pV = 300 kJ e igual T, logo ΔU = 0. Nos trajetos quase estáticos indicados, os trechos verticais têm W = 0 e os horizontais fornecem 300 × 2 e 100 × 2 kJ. | Trabalhos e calores líquidos **600 kJ** e **200 kJ**, respectivamente. O diagrama como objeto visual separado não foi auditado aqui. |
| EX-015 | Expansão livre de gás ideal isolado, rígido, massa fixa e sem trabalho: ΔU = 0 e T final igual à inicial. Por estados, ΔS = 1 × 0,287 × ln 2 = 0,19893324… kJ/K; sem entropia transferida por calor, Sger = ΔS. | **0,199 kJ/K** está no intervalo [0,1985; 0,1995) kJ/K de arredondamento. A expansão real continua irreversível. |
| EX-016 | Água em uma fase, c constante ou representativo, efeitos de pressão e trabalho desprezíveis na aproximação de calor sensível: Q = 2 × 4,2 × (50−20) = 252 kJ; 80% de 2 kW entregues fornece 1,6 kJ/s. | Tempo **157,5 s**. É uma conta do modelo apresentado. |
| EX-017 | Mesmo líquido, c constante, mistura isolada, sem trabalho relevante, reação ou mudança de fase e recipiente desprezível: Tf = (1 × 20 + 3 × 60)/4. | **50 °C**, conforme. |
| EX-018 | Capacidades de 4, 4 e 2 kJ/K, temperaturas 80, 20 e 20 °C e energia líquida externa zero: 4(Tf−80) + 4(Tf−20) + 2(Tf−20) = 0. | **44 °C**; sem a capacidade do recipiente, **50 °C**. Energia líquida externa nula não exige que cada interação separadamente seja nula. |
| EX-019 | Água/gelo a 0 °C e pressão indicada: água de 0,5 kg libera 0,5 × 4,2 × 20 = 42 kJ. Para 0,10 kg, a fusão consome 33,4 kJ e os 8,6 kJ restantes aquecem 0,60 kg de água: Tf = 3,412698… °C. Para 0,30 kg, fundir tudo exigiria 100,2 kJ; funde 42/334 = 0,1257485… kg. | **3,41 °C** e **0,126 kg**, respectivamente; intervalos de arredondamento [3,405; 3,415) °C e [0,1255; 0,1265) kg. Com gelo remanescente em equilíbrio, Tf = 0 °C. |
| EX-020 | Tanque rígido inicialmente vazio, uma entrada de entalpia constante, sem saída, Q = W = 0, parede e energias cinética/potencial desprezíveis. Mesmo gás ideal, cp/cv = 1,4 constante: m₂u₂ = mᵢₙhᵢₙ e m₂ = mᵢₙ. | T₂ = 1,4 × 300 = **420 K**. O processo acumula massa e não é permanente. |

Valores aritméticos são exatos no modelo nominal salvo os intervalos de arredondamento explicitados; não se apresenta incerteza instrumental. A referência da caloria termoquímica foi confrontada com [NIST, Guide to the SI](https://www.nist.gov/pml/special-publication-811/nist-guide-si-footnotes). Relações de entropia em expansão livre e distinção entre caminho real e caminho reversível de cálculo foram confrontadas com [MIT, Calculation of Entropy Change in Some Basic Processes](https://web.mit.edu/16.unified/www/SPRING/propulsion/notes/node40.html). O enchimento idealizado foi confrontado com [MIT, Example Applications of the First Law](https://web.mit.edu/16.unified/OldFiles/www/FALL/thermodynamics/notes/node17.html), e o balanço de fusão com [OpenStax, Phase Change and Latent Heat](https://openstax.org/books/physics/pages/11-3-phase-change-and-latent-heat). Consultas em 30/10/2026, sem captura e hash local; essas fontes apoiam as relações, não são a origem dos dados didáticos.

## Decisão de alcance

| Critério | Resultado |
|---|---|
| Identidade dos oito blocos na fotografia r8 | Atendido no escopo indicado; os intervalos e hashes são reproduzíveis pelo script independente. |
| Hipóteses, sinais, unidades, contas e arredondamento | Atendido nos modelos e limites descritos. |
| Números das bases, figuras e outras atividades | Não examinados integralmente nesta entrega; continuam em QA-09. |
| Aceite integral de QA-09 e liberação do próximo ID | Não atendidos por este parecer. |

Nenhum teste em navegador, revisão humana, estudo com estudantes ou certificação externa foi realizado nesta revisão; não se infere aprendizagem a partir de contas conferidas.
