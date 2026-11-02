# QA-09 — auditoria independente de primeira lei e entropia de escoamento, r17

Data: 30/10/2026. Auditor automatizado `/root/reference_triage`, distinto do Corretor `/root/next_theory`. **Veredito localizado: AJUSTES OBRIGATÓRIOS** para as duas interpretações abaixo. As demais contas apresentadas foram conferidas nos limites declarados. QA-09 integral permanece em correção e o próximo ID não é liberado.

## Critério, identidade e método

QA-09 exige recálculo e rastreabilidade das ocorrências numéricas fora dos 197 artigos, incluindo explicações e figuras; este parecer abrange apenas cinco blocos indicados pelo Corretor. Os blocos completos e seus elementos filhos se sobrepõem no inventário: não representam cinco provas de cobertura de todos os trechos ou equações neles contidos. [Entrega examinada](../evidencias/QA-09/teoria-primeira-lei-entropia-r17-20261030/entrega.md) SHA-256 `b24ee6ef76a36d9a87fb7451fe4fc1959769676f171ff39ac25b963fdd8a6f9a`.

Fotografia congelada r17 `auditoria/termodinamica/evidencias/QA-09/aplicacao-intercooling-r17-r1/resultado/depois-aula.html` e aula efetiva no momento do exame: SHA-256 `6b0df1096d0b6de6995ffc51bf8489cb45ab954a7aabdeb3f48d068c9777c57c`. Inventário r17 `b8eae39cc72cf807d7b84aad7e7a38423168b809231bc3b7f08c439d6d25163b`. Reconstruí independentemente os cinco fragmentos pelos intervalos UTF-16 e conferi âncora única e SHA do bloco, contexto e contas do recorte. O [verificador independente somente leitura](../evidencias/QA-09/auditoria-primeira-lei-entropia-r17-20261030/verificar.py) SHA-256 `2ed50d408289e86e65b6cc6e487a490119ac6796bd30194c114f43620966a863` foi executado a partir da raiz e passou. Fontes da própria instituição ou universidade foram consultadas pela ferramenta web em 30/10/2026; não houve navegador real.

## Ajuste obrigatório 1 — efeito líquido de calor e trabalho

Em `#base-primeira-lei`, bloco 157256–162652, SHA-256 `332677c5d3ea50033ff1c6145ba8d6d039c5b98299d830e4b7d3435f67d2fdca`, o balanço `ΔU+ΔEc+ΔEp=Q−W` e a convenção de sinais estão corretos. A frase seguinte, “Receber calor aumenta a energia do sistema”, pode ser lida como conclusão sobre a variação total, embora o saldo dependa também do trabalho. O fato de a equação estar correta não elimina essa leitura para quem estuda a frase isoladamente.

**Contramodelo fisicamente modelável:** 1 kg de gás ideal caloricamente perfeito com `cv=0,718 kJ/(kg·K)` parte de 400 K. Primeiro expande adiabática e reversivelmente, produzindo `W₁=100 kJ`, sem calor e com variações cinética/potencial desprezíveis; `T₁=400−100/0,718≈260,72 K`. Em seguida, recebe `Q₂=50 kJ` a volume constante, sem trabalho, chegando a `T₂≈330,36 K`. No processo completo `Q=+50 kJ`, `W=+100 kJ` e `ΔU=−50 kJ`: houve calor recebido e a energia interna final diminuiu. Os dados são nominais hipotéticos para ilustrar o balanço, não um ensaio experimental. Uma expansão isotérmica reversível também pode receber calor com ΔU=0 e W=Q.

**Correção exigida:** explicitar que calor recebido é uma **contribuição positiva** ao balanço de energia e que a variação líquida também depende do trabalho e demais interações; preservar a convenção e distinguir `ΔU` do total `ΔE` quando ΔEc/ΔEp não forem desprezíveis. Submeter candidata isolada a Auditor distinto; após aplicação, reexaminar a versão efetiva e seu impacto no inventário e pareceres dependentes. A [primeira lei do MIT](https://ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_4.htm) foi consultada como apoio ao balanço, não como fonte dos números artificiais.

## Ajuste obrigatório 2 — temperatura de fronteira em volume de controle

Em `#base-entropia-escoamento`, bloco 426459–441261, SHA-256 `ecd08e62bcdc7799132b011fe111dfae8948487b8203559cd085918c95fd35ef`, o balanço estacionário `0=Σṁ_in s−Σṁ_out s+ΣQ̇_j/T_j+Ṡger` é adequado quando cada `Q̇_j` corresponde a uma parcela de fronteira com temperatura `T_j` apropriadamente uniforme, ou se representar termo diferencial corretamente integrado. A aula identifica `T_j` no ponto de transferência mas não informa nessa seção como tratar temperatura variável sobre uma área finita; chamar o calor finito de taxa “no ponto” tampouco torna explícita a operação de integração. O bloco anterior `#base-entropia` já menciona integração local para sistema fechado, mas o texto de volume de controle não explicita que essa condição também se aplica ali.

**Contraste algébrico:** duas parcelas recebidas, `100 kW` a `300 K` e `100 kW` a `600 K`, transferem `100/300+100/600=0,500 kW/K`; usar `200/450` com média aritmética dá `0,444444… kW/K`. Se a diferença de fluxos de entropia das massas for `0,600 kW/K`, o balanço de entropia estacionário dá `Ṡger=0,100 kW/K`, não `0,155556… kW/K`. As parcelas e a diferença de entropia são um teste nominal de contabilidade, não especificação completa de um equipamento. Para este exemplo, a temperatura efetiva ponderada pelo calor seria `400 K`, mas ela não é uma regra para qualquer mistura de fluxos de calor de sinais diferentes.

**Correção exigida:** definir que cada parcela discreta usa a temperatura de fronteira do lado do sistema para uma parcela efetivamente isoterma e que, quando a temperatura varia espacialmente, deve-se integrar a taxa local de calor dividida pela temperatura local sobre a fronteira, ou dividir em parcelas isótermas adequadas. Não usar uma temperatura média arbitrária; explicitar sinal de Q̇ entrando positivo. A [derivação Purdue da segunda lei para volume de controle, eqs. 4.139–4.142](https://engineering.purdue.edu/~wassgren/teaching/ME20000/NotesAndReading/Lec28_Reading_Wassgren.pdf), p. 1 do PDF, apresenta o termo de fronteira integrado. A fonte adicional MIT citada pelo Corretor excedeu o limite de tamanho da ferramenta nesta consulta: não a considero independentemente lida. Candidata e aplicação devem passar por revisões distintas, inclusive do MathML, legendas e vínculos.

## Demais contas e limitações

Conferi as unidades e contas nominais: agitador `−40−(−250)=210 kJ`; `U₂=50+100×4,2−120=350 J`; compressão `W=200×(−0,020)=−4 kJ` e `ΔU=−7−(−4)=−3 kJ`; gás no tanque `ΔT=35/(1×0,70)=50 K`; caminhos `300×2=600` e `100×2=200 kJ`; ciclo retangular horário `(200−100)×(3−1)=200 kJ`; trocador isolado externamente `−0,20+0,30=0,10 kW/K` com vazões de 1 kg/s. Convenções, hipóteses e unidade `1 kPa·m³=1 kJ` foram confrontadas na aula. Em termoquímica, `Q=ΔH` segue do balanço para o sistema fechado e as condições de pressão/trabalho declaradas; inverter os mesmos estados muda `−50` para `+50 kJ`. Consultei [DOE/AFDC para PCS/PCI](https://afdc.energy.gov/glossary), preservando a mesma base; não são dados do processo do exemplo.

| Critério localizado | Situação |
|---|---|
| Identidade e recálculos dos cinco blocos no r17 | Conferidos na extensão indicada; dados nominais e modelos explícitos. |
| Frase de calor recebido | **Não atendido:** esclarecer contribuição positiva versus saldo líquido. |
| Temperatura na parcela de calor do volume de controle | **Não atendido:** explicitar parcela isoterma ou integral espacial. |
| Correção aplicada e verificação após mudança | Pendente; exige candidata, mapa/fotografia e reauditoria da versão efetiva. |
| Figuras, demais recursos, QA-09 integral e próximo ID | Fora deste alcance; permanecem pendentes/bloqueados. |

Não se examinou a renderização visual das figuras, a totalidade das fórmulas/legendas dos blocos, aplicações com estudantes, acessibilidade, revisão humana ou certificação externa. Os resultados aprovados do recorte não se aplicam automaticamente a outras versões nem comprovam aprendizagem.
