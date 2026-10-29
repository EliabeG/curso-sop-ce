# BAN-08 — apoio independente AV21–AV30

Data 29/10/2026; revisor: agente automatizado `/root/auditoria_av61_70`. Escopo parcial; não aprova BAN-08 nem libera próximo ID. Produto e controle preservados.

HTML `modulos/e1-termodinamica.html`, SHA-256 `80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0`. Os hashes dos itens correspondem ao trecho `<article>...</article>` recodificado em UTF-8. Identidade não substitui análise científica. São itens autorais, não transcrição oficial.

## AV21

**B.** Para quantidade fixa e conhecida de gás ideal, `pV=nRT`; com duas propriedades físicas independentes, e denominadores não nulos, a terceira é determinada. I e II verdadeiras, III falsa. A inclui III e omite I; B I/II correta; C inclui III; D inclui III e omite I/II; E omite II. Três afirmações e cinco alternativas são contagens exatas; não há dados de estado numérico ou arredondamento a verificar, portanto tolerância de cálculo N/A. Base `#base-gas-modelo`.

Artigo SHA-256 `d30c611664194c81700bc047dc72f6f1d9242c9552a394616ba605226c6aba73`.

## AV22

**B.** `Z=pV/(nRT)=180 kJ/200 kJ=0,90`, adimensional e diferente de 1 no dado nominal. A `200/180=1,111…→1,11` inverte a razão e chama ideal valor distinto de 1; arredondamento de 1,11 tem erro <0,005. C dá 1,00 e ignora a razão; D `200−180=20 kJ` calcula diferença dimensional em lugar de Z; E repete 0,90 mas classifica incorretamente como exatamente ideal. B e E têm valor numérico idêntico e só a conclusão as distingue; nenhuma tolerância numérica isolada garante unicidade do par. Valores nominais tratados como dados exatos para o exercício, sem incerteza da medição de pV ou do cálculo de nRT informada; não se infere significância metrológica. Bases `#base-gas-modelo`, `#base-gas-energia`, `#base-leitura-matematica`.

Artigo SHA-256 `a60b027d19ccee5b6445c7865ba43a1732ddb069c63592895d523ebb82738e36`.

## AV23

**A.** Baixa pressão e temperatura suficientemente afastada da condensação favorecem gás ideal, sem garantia universal em qualquer estado. B alta pressão isoladamente não garante; C alta pressão próxima da condensação e D baixa temperatura próxima da saturação desfavorecem; E generaliza indevidamente `Z=1` para todos os gases reais. O 1 é valor ideal adimensional exato, não medição de um gás real. Sem pressão, temperatura ou Z medido, cálculo numérico e tolerância são N/A. Figura inspecionada representa recipiente, gás e vácuo sem escalas numéricas; ela não fornece dados para quantificar a idealidade: `assets/questoes-reais-e1/figura-9d164690a624.png`, SHA-256 `9d164690a6243cb31b9ea0f734b9a85ad4c6570398b9d5ef9278e4f44332bcc2`. Base `#base-gas-modelo`.

Artigo SHA-256 `52ce7c5b255380dd1c2d876058b8965c9ff3feaa6e373c57f6f8e46bd3db529b`.

## AV24

**E.** Massa e volume fixos de gás ideal, temperaturas absolutas: `p_f/p_i=T_f/T_i=360/300=1,20`. A `60` é diferença de temperaturas de 60 K, não razão; B `0,20` é aumento relativo de pressão; C `1` ignora mudança; D `300/360=0,833333…` é inversão, arredondada a 0,833 com erro <0,0005; E 1,20 correta. Dados nominais e razão correta exatos; nenhuma incerteza de sensor foi dada. Os resultados numéricos são distintos mesmo após arredondamento indicado. Bases `#base-gas-modelo`, `#base-absolutas`, `#base-leitura-matematica`.

Artigo SHA-256 `8e27e9a89a7e9cd792555923bc8888441ac0ec412520da31a5b29b2379cf79c6`.

## AV25

**C.** `p₂/p₁=2`, `V₂/V₁=1+0,50=1,5`, `T₂/T₁=3`; valor final é 300% do inicial, aumento `(3−1)×100%=200%`. A 100% considera só pressão; B 300% confunde valor relativo final com incremento; C 200% correta; D 50% considera só volume; E aumento zero ignora a triplicação. Razões são adimensionais, T e p absolutas; dados nominais e percentuais são exatos no modelo, sem incerteza ou arredondamento informados. Bases `#base-gas-modelo`, `#base-leitura-matematica`.

Artigo SHA-256 `944eadc933945dd04024af4da9585627d9484f9e2095af98a0efb541c9ff8ba1`.

## AV26

**A.** No sistema tanque–fluido fechado, com Q positivo entrante e W positivo realizado, `Q=−150 kJ`, `W=−600 kJ`, sem trabalho de fronteira e sem ΔEc/ΔEp: `ΔU=−150−(−600)=+450 kJ`. A +450 correta; B +600 omite perda; C −450 inverte resultado; D −750 contabiliza ambas como saídas; E +750 soma ambas como entradas. Dados nominais em kJ e contas exatos; sem incertezas nem arredondamento. Figura inspecionada é ilustração de tanque agitado sem dados numéricos próprios, não especifica fluxos independentes: `assets/questoes-reais-e1/figura-4c355dba6054.png`, SHA-256 `4c355dba6054f57fc26e5872ffdc1b83738a52345f31b8f994c26486651c2995`. Bases `#base-balanco-fechado`, `#base-leitura-matematica`; [MIT, primeira lei e convenções](https://web.mit.edu/16.unified/www/SPRING/thermodynamics/notes/node14.html).

Artigo SHA-256 `2d44c7a93a3d7cbe464d96fab7a2427fab1ee039ef3eeb272539d7eefe421a74`.

## AV27

**E.** Massa fixa e ar ideal com `c_v>0`, `Q=0`, trabalho líquido recebido e alterações cinética/potencial desprezíveis: `ΔU=−W>0`, e `ΔU=m∫c_v(T)dT>0` implica aumento de temperatura. A isotermia não decorre de adiabaticidade; B inverte efeito do trabalho; C confunde isolamento térmico com ausência de trabalho; D contradiz massa fixa; E correta. Zero é condição ideal exata; sem trabalho ou temperaturas numéricas, cálculo e tolerância N/A. Bases `#base-primeira-lei`, `#base-gas-energia`; [MIT primeira lei](https://web.mit.edu/16.unified/www/SPRING/thermodynamics/notes/node14.html).

Artigo SHA-256 `1cac59ad0421ba447b5d28ea97a5b47d99889dda7e6283c3d56d3a4eb05d5db1`.

## AV28

**D.** Conversão dada `Q=200 cal×4,2 J/cal=840 J`; `W=+350 J`; `ΔU=840−350=490 J`; `U_f=100+490=590 J`. A `1290=100+840+350` soma trabalho produzido como entrada; B `490` é variação, não valor final; C `940=100+840` omite trabalho; D 590 correta; E `−50=100+200−350` trata 200 cal como 200 J. Conversão de 4,2 J/cal é dada do exercício, não medição de precisão especificada; operações com valores nominais são exatas e sem incerteza ou arredondamento declarados. Bases `#base-balanco-fechado`, `#base-primeira-lei`, `#base-leitura-matematica`; [MIT primeira lei](https://web.mit.edu/16.unified/www/SPRING/thermodynamics/notes/node14.html).

Artigo SHA-256 `5ba6b332f4915122f681d9e816a36d869ac678a9ce1921e5b5d22dac5bfa35ed`.

## AV29

**E.** Pressão absoluta constante 100 kPa e compressão quase estática `ΔV=−0,010 m³`: `W=pΔV=−1 kPa·m³=−1 kJ`; `Q=−5 kJ`, `ΔU=Q−W=−4 kJ`. A `−6=−5−1` soma trabalho recebido como saída; B `+6` trata ambos como entrada; C `−5` omite trabalho; D `+4` inverte resultado; E `−4` correta. `1 kPa·m³=1 kJ` por conversão de unidades exata. Dados nominais sem incerteza informada, e não há arredondamento intermediário. Bases `#base-trabalho-fronteira`, `#base-balanco-fechado`, `#base-leitura-matematica`; [MIT primeira lei](https://web.mit.edu/16.unified/www/SPRING/thermodynamics/notes/node14.html).

Artigo SHA-256 `20636340c4eaf5d0230b128cbb6d530369b7b690ff55043e10c36ea77ef0b3a4`.

## AV30

**D.** Gás ideal de massa fixa em etapa isotérmica: `ΔU=0`; sistema fechado, só trabalho de fronteira e ΔEc/ΔEp desprezíveis, `W=Q=+300 kJ`. A −300 inverte sinal do trabalho de expansão; B +600 duplica calor; C +150 pressupõe indevidamente aumento de U; D +300 correta; E zero confunde T constante com ausência de trabalho. A figura examinada mostra A→B na mesma isoterma e expansão no eixo volume, mas não contém escala numérica p–V utilizável para cálculo de área; o calor vem do enunciado. `assets/questoes-reais-e1/figura-de4ee7b16ed4.png`, SHA-256 `de4ee7b16ed42d37537a23bbcf6cf7aee66cb447e11bb950b3c783e3a859aa1b`. Dados nominais exatos no modelo, sem arredondamento ou incerteza. Bases `#base-gas-energia`, `#base-trabalho-fronteira`, `#base-balanco-fechado`; [MIT primeira lei](https://web.mit.edu/16.unified/www/SPRING/thermodynamics/notes/node14.html).

Artigo SHA-256 `b15d6dd6aa44531627bb9a953e5d572a383804b557bb38df3869b581420c3b01`.

## Fontes de auditoria e limites

- `auditoria/termodinamica/PROTOCOLO_AAA.md` — SHA-256 `18f1f299556e8e60c926a1921987f6d2c10cc939aa4aef4487117dc66c344afc`
- `auditoria/termodinamica/evidencias/BAN-08/inventario-numerico-197-r1.json` — SHA-256 `5b56e8280d35d590bf11ddbff9b0e789faed257fafe1cad9c4854cc5ac5fd99f`
- `auditoria/termodinamica/pareceres/BAN-07-auditor-bloco-av21-25-r1.json` — SHA-256 `1c3667b498bc3562ab0b6c00b3e876847d56deacabd0fa4340a3e66c14abb54a`
- `auditoria/termodinamica/pareceres/BAN-07-auditor-bloco-av26-30-r1.json` — SHA-256 `97431c365fa7152fafe95eed92e8476ee9b38e9f3194e09fd36e74175a5b7e53`
- `auditoria/termodinamica/pareceres/BAN-07-r3.md` — SHA-256 `009adc698bf2f88e28826b389a48e2526660efc9b7cc2ea3b598f0e06026d68b`

As contas, condições e cinco juízos de cada item foram examinados pelo revisor atual, com conhecimento prévio das respostas. BAN-07 é trabalho anterior atribuído; identidade não substitui a revisão numérica atual. A fonte MIT foi consultada em 29/10/2026. Sem ensaio com estudantes, certificação externa, incerteza instrumental inferida ou aprovação global BAN-08.
