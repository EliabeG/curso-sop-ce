# BAN-07 r1 — parecer pontual independente CR45

Data: 29/10/2026. Revisor: `/root/auditoria_av61_70`, agente automatizado. **Resultado: AJUSTE OBRIGATÓRIO proposto, sujeito à adjudicação do Auditor principal.** A conclusão anterior de que não havia ajuste em CR45 deve ser revista no ponto da suficiência anterior à tentativa. Este parecer é pontual e não aprova BAN-07 nem libera próximo ID.

## Versão, escopo e fontes

CR45 é o item oficial Cebraspe TRF6, cargo 11, questão 51. O enunciado diz ser impossível uma máquina térmica receber 900 kJ de uma fonte a 477 °C e rejeitar 90 kJ por ciclo para um dissipador a 27 °C. A chave definitiva é C. Confirmei visualmente o item e a chave na p. 1 de suas imagens documentais. Não há figura pertinente a este item, nem no artigo nem na página da prova: os gráficos e figuras da página pertencem a outras questões. Não se infere que eles restrinjam CR45.

- HTML `modulos/e1-termodinamica.html`, SHA-256 `de614a44d796ca04268915f89f502060db2772835c072036a990802eff912b80`; artigo bruto `cr-e1-45`, SHA-256 `382306e2bd0381e3614cfefd799d12a1b90a06b3b78e1f2171bc5c9c67c4ba4d`, coincide com a preparação e a herança.
- Parecer de herança `BAN-07-auditor-heranca-cr36-50-r1.json`, SHA-256 `a307cdf629f4b6173d8717bc473f0c455df17f0bc96b24b41ca4df86a22c09d8`: o agente `/root/auditor_ban07_final` reconheceu que o original não explicita outras trocas, mas julgou esse limite não bloqueante. A preparação `BAN-07-leitura-base.json`, SHA-256 `d71452ed79437c69f454706c7645b47b5e3b7f2a41e228f0ea37ac078a2a9913`, é de `/root/auditor_aaa` e contém o cálculo sob duas fontes. A presente revisão não atribui a esses agentes o contramodelo abaixo.
- Prova local `downloads/termodinamica/provas/2025-01-19_trf6-analista-engenharia-mecanica_prova.pdf`, SHA-256 `74a764fdb11ca13d527674c39206f44cbd4b5b1392cdee1f8bce9d8016ac4d79`; gabarito `downloads/termodinamica/gabaritos/2025-01-19_trf6-analista-engenharia-mecanica_gabarito.pdf`, `0b5abca04a6892f48c7541018106445f6619f5f5863e061f631f0249899795e3`. As imagens p.1 de prova e gabarito registradas em FON-01 foram vistas nesta revisão: respectivamente SHA-256 `5726776fa459fea543551975ba19390759804f9349db78d322d141ecf0b9940e` e `64233fb2c8516238cf95fb083f0f2c3b029c181c173d517990f7194d5a4e18f3`. Os PDFs correspondem aos hashes documentais; não se afirma nova pesquisa de atos além de FON-01.

## Modelo publicado e sua condição

Na interpretação **das duas trocas de calor como totais**, máquina cíclica e somente trabalho líquido adicional, Tq=750,15 K e Tf=300,15 K. Pela primeira lei W=900−90=810 kJ, de modo que η=90%. Carnot dá η≤1−300,15/750,15≈59,988%, ou Qf≥900×300,15/750,15≈360,108 kJ. Como 90 kJ está abaixo desse mínimo, o dispositivo é impossível nesse modelo; C é correto e E errado nesse recorte. A solução é numericamente correta e deixa explícito, **depois** da tentativa, que está adotando somente as duas trocas. O enunciado reproduzido não diz que elas sejam todas as trocas.

Examinei as bases acessíveis `#base-carnot-prova`, `#base-limite-carnot` e `#base-leitura-matematica`. A primeira deriva Qf/Tf−Qq/Tq≥0 para conjunto isolado composto pela máquina e as duas fontes, e a segunda apresenta Carnot *entre duas fontes*. Elas ensinam quando esse modelo vale; não dizem que a descrição de CR45 esgota suas trocas. O exemplo entre duas fontes não impõe essa condição a qualquer enunciado que mencione uma fonte e um dissipador. A resolução só revela a exclusividade após a escolha, de modo que não sana a suficiência antes da tentativa.

## Contramodelo: três reservatórios, máquina cíclica

Construa um conjunto de duas máquinas térmicas cíclicas acopladas a um eixo e à mesma fonte quente Tq=750,15 K. Por ciclo do conjunto:

| Submáquina | Calor recebido da fonte quente | Calor rejeitado | Trabalho produzido | Geração de entropia total dos reservatórios |
|---|---:|---:|---:|---:|
| A | 200 kJ | 90 kJ ao dissipador especificado, 300,15 K | 110 kJ | 90/300,15 − 200/750,15 ≈ 0,03324 kJ/K |
| B | 700 kJ | 300 kJ a outro dissipador, 270 K | 400 kJ | 300/270 − 700/750,15 ≈ 0,17796 kJ/K |
| Conjunto | **900 kJ** | **90 kJ ao dissipador indicado**, mais 300 kJ ao adicional | **510 kJ** | ≈ **0,21120 kJ/K** |

Cada submáquina satisfaz primeira e segunda leis. Sua eficiência é 55% para A, abaixo de 59,988% de Carnot entre 750,15/300,15 K; é 57,14% para B, abaixo de 64,007% entre 750,15/270 K. A construção pode ser feita com um motor de Carnot mais passagem de calor quente-frio em paralelo dentro de cada submáquina: em A, o motor recebe 183,37 kJ e a passagem 16,63 kJ; em B, recebe aproximadamente 624,930 kJ e a passagem 75,070 kJ. Ambas retornam ao estado inicial por ciclo e o conjunto fornece trabalho líquido. Não há fluxo de massa ou armazenamento líquido escondido. O terceiro dissipador é um acréscimo do contramodelo, **não um dado atribuído à prova**; sua função é mostrar que a redação não o exclui expressamente. O arranjo atende literalmente aos 900 kJ recebidos e 90 kJ entregues ao dissipador mencionado, embora rejeite mais calor em outro lugar.

Se o enunciado for entendido convencionalmente como duas fontes e duas trocas totais, o contramodelo deixa de ser admissível e C segue demonstrado. Se não se impuser essa exclusividade, o contraexemplo refuta a impossibilidade absoluta e apoia E. Portanto a oposição C/E para item pontuável depende de uma restrição ainda não comunicada antes da tentativa. A ambiguidade não demonstra que o gabarito oficial tenha sido anulado nem que a banca estivesse pensando em três reservatórios.

## Critérios e ação

| Critério | Juízo |
|---|---|
| Documento, fonte e chave | Texto e C oficial identificados e preservados; imagens de prova/chave conferidas. |
| Dados, hipóteses e unicidade antes da tentativa | **Não atendido sem adjudicação**: exclusividade das trocas muda a resposta e é explicitada apenas depois. |
| Solução sob a leitura declarada | Correta em temperaturas absolutas, energia e limite de Carnot; equação de duas fontes não se aplica ao contramodelo de três. |
| C/E e demonstração | C é correta no recorte de duas trocas totais; E é defensável na leitura literal mais ampla, por construção cíclica permitida. Não há alternativas numéricas concorrentes nem equivalência por arredondamento. |
| Escopo da base e figura | As bases delimitam a teoria que ensinam, mas não impõem restrição específica ao item; não há figura pertinente. |

**Ajuste proposto:** manter integralmente enunciado e chave oficiais; antes da tentativa, acrescentar hipótese editorial claramente separada do texto original de que a máquina opera em ciclo e que as duas trocas de calor descritas são as únicas, com trabalho líquido e sem outros efeitos energéticos líquidos, de modo a sustentar C; **ou** converter o original em estudo crítico fora da pontuação, explicitando ambas as leituras e o contramodelo. A reapresentação deve sincronizar explicação e inventário e verificar a identidade da questão, efeito sobre histórico e pontuação conforme a opção adotada. Não se altera nem se declara anulada a questão oficial.

O paralelo com CR26 é o ponto metodológico: hipótese adicional decisiva somente na resolução não fecha a suficiência antes da tentativa. Lá o termo omitido era energia transportada por massa; aqui é rejeição térmica adicional — os modelos não são os mesmos. Sem teste de navegador, verificação de armazenamento ou análise de outros itens nesta revisão. Nenhuma alteração de produto ou controle.
