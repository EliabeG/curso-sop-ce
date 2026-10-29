# BAN-08 — apoio independente CR61–CR70

Data 29/10/2026. Revisor: agente automatizado `/root/auditoria_av61_70`. Escopo parcial; não aprova BAN-08 nem libera próximo ID. Produto e controle preservados.

HTML `modulos/e1-termodinamica.html`, SHA-256 `80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0`. Os hashes por artigo são dos trechos brutos `<article>...</article>` recodificados em UTF-8. PDFs de provas e chaves conferidos por hash com FON-01; a leitura visual documental é atribuída a FON-01, não repetida integralmente nesta rodada. Identidade não substitui análise científica.

## CR61

**E.** A eficiência volumétrica é volume fresco admitido referido às condições de entrada dividido pelo volume deslocado no período, não sempre `1`. Gás residual reexpande e ocupa parte do deslocamento; aquecimento, perdas e vazamentos também podem influenciar o resultado. A unidade 1 é um limite de idealização, adimensional, não um resultado calculado para todo compressor. Faltam valores de folga, pressões e volume: não há cálculo numérico ou tolerância de arredondamento aplicável. Base `#base-eficiencia-volumetrica`.

Artigo SHA-256 `745cde3da24b14b573ac4b3fb6cca25d7e1cf90b099d9a8f05adcbd86bb86143`; família `tm`, item original 58, prova p. 1, chave p. 1, letra E. Prova `downloads/termodinamica/provas/2023-10-15_tbg-tecnico-gasoduto-mecanica_prova.pdf`, SHA-256 `154317cd7e60869143739bba27d18d33fdc788b0269a09be2dd873b33dbf5cc4`; chave `downloads/termodinamica/gabaritos/2023-10-15_tbg-tecnico-gasoduto-mecanica_gabarito.pdf`, SHA-256 `1ebd87b8d6d1cd8a679b575de3a0e901d1283c8b6b92e7a916e775d7cdeb9f7d`.

## CR62

**Chave documental C, estudo crítico fora da nota.** Há duas válvulas: na reexpansão inicial do gás retido na folga ambas podem estar fechadas; a entrada só abre quando a diferença de pressão supera a resistência da válvula, e na admissão propriamente dita a descarga fica fechada. “Durante esse movimento” pode abranger toda a descida ou apenas a fase de admissão, e a direção “desce” depende da orientação. A letra C é documental; o estudo não atribui uma intenção à banca nem anulação. Contagem das duas válvulas é exata; sem volumes, pressões ou instantes numéricos, cálculo e tolerância são N/A. Base `#base-valvulas-compressor`; [GUNT ET 508, reexpansão](https://gunt.de/en/products/fluid-machinery/driven-machines/fans-and-compressors/simulation-of-a-two-stage-air-compressor/061.50800/et508/glct-1:pa-148:ca-752:pr-240).

Artigo SHA-256 `5f44da84f65dd8f11782a7923c5b3741171d0b8e5529d77273820740c7348b1a`; família `tm`, item original 59, prova p. 1, chave p. 1, letra C. Prova `downloads/termodinamica/provas/2023-10-15_tbg-tecnico-gasoduto-mecanica_prova.pdf`, SHA-256 `154317cd7e60869143739bba27d18d33fdc788b0269a09be2dd873b33dbf5cc4`; chave `downloads/termodinamica/gabaritos/2023-10-15_tbg-tecnico-gasoduto-mecanica_gabarito.pdf`, SHA-256 `1ebd87b8d6d1cd8a679b575de3a0e901d1283c8b6b92e7a916e775d7cdeb9f7d`.

## CR63

**E.** Turbina a gás convencional é associada a Brayton; Stirling ideal tem quatro etapas, duas isotérmicas e duas isocóricas, com regeneração e aquecimento externo. Essas contagens são exatas; **N/A numérico:** não são fornecidas temperaturas, calor, trabalho ou rendimento para calcular, e não há tolerância numérica. Base `#base-comparar-ciclos`.

Artigo SHA-256 `777d85e75efa77ab3c17204d511d215d72be4519ee59f4b06e371c9d9bc30695`; família `tm`, item original 60, prova p. 1, chave p. 1, letra E. Prova `downloads/termodinamica/provas/2023-10-15_tbg-tecnico-gasoduto-mecanica_prova.pdf`, SHA-256 `154317cd7e60869143739bba27d18d33fdc788b0269a09be2dd873b33dbf5cc4`; chave `downloads/termodinamica/gabaritos/2023-10-15_tbg-tecnico-gasoduto-mecanica_gabarito.pdf`, SHA-256 `1ebd87b8d6d1cd8a679b575de3a0e901d1283c8b6b92e7a916e775d7cdeb9f7d`.

## CR64

**C.** Pistão e parafuso são deslocamento positivo: aprisionam gás e reduzem o volume de câmara; no parafuso, esse volume ocorre entre rotores e carcaça. A analogia é do mecanismo, sem equiparar desempenhos ou admitir compressão com temperatura arbitrária. **N/A numérico:** faltam volumes, pressões e dados de processo para cálculo ou tolerância. Base `#base-tipos-compressores`.

Artigo SHA-256 `5cb37f5064e8114789a60496810e7ebd847a164bcb798385e5c0f5b37fef7313`; família `tm`, item original 81, prova p. 3, chave p. 1, letra C. Prova `downloads/termodinamica/provas/2023-10-15_tbg-tecnico-gasoduto-mecanica_prova.pdf`, SHA-256 `154317cd7e60869143739bba27d18d33fdc788b0269a09be2dd873b33dbf5cc4`; chave `downloads/termodinamica/gabaritos/2023-10-15_tbg-tecnico-gasoduto-mecanica_gabarito.pdf`, SHA-256 `1ebd87b8d6d1cd8a679b575de3a0e901d1283c8b6b92e7a916e775d7cdeb9f7d`.

## CR65

**C sob modelo da resolução.** Escoamento permanente de uma entrada e uma saída, `ṁ_entrada=ṁ_saída=ṁ`, sem calor, ΔEc ou ΔEp relevantes e sem trabalhos adicionais: `Ẇ_eixo=ṁ(h₁−h₂)`, logo trabalho produzido positivo implica `h₁>h₂`. As unidades `(kg/s)(kJ/kg)=kJ/s=kW` conferem; trabalho de escoamento `pv` já está incluído em entalpia, evitando dupla contagem. A adiabática pode ser irreversível e não é automaticamente isentrópica. Uma entrada e uma saída são contagens exatas; sem vazão e entalpias, valor e tolerância numéricos são N/A. Base `#base-turbina-potencia`; [MIT balanço permanente](https://web.mit.edu/16.unified/OldFiles/www/SPRING/thermodynamics/notes/node18.html).

Artigo SHA-256 `9322946ef9f40d87e6ff05c7a9d49c484260044be286ecbe9153b3a05dedeeda`; família `tse`, item original 71, prova p. 2, chave p. 1, letra C. Prova `downloads/termodinamica/provas/2024-12-08_justica-eleitoral-tse-cpnuje-engenharia-mecanica_prova.pdf`, SHA-256 `fae9b7159587bd52cfe63f1bffce4894bdd4b3419ae449740c70ff0b021c5ce6`; chave `downloads/termodinamica/gabaritos/2024-12-08_justica-eleitoral-tse-cpnuje-engenharia-mecanica_gabarito.pdf`, SHA-256 `ab2116cb79da87ca206b7156c345d493d87032ee1f2fb8514137ced96e437baf`.

## CR66

**E.** Em um trocador casco e tubos usual, dois fluidos escoam separados pela parede; há convecção nos lados e condução através da parede, não mistura intencional como princípio. Vazamento é possível, mas não constitui funcionamento normal. A contagem de dois fluidos e uma parede separadora é exata no arranjo descrito; sem temperaturas, área ou coeficientes não há cálculo numérico nem tolerância. Base `#base-trocadores`.

Artigo SHA-256 `3c495fe75122088861c7e8de6a39ceccefaf8486532bbaad7e755d48a7ec1850`; família `p23`, item original 82, prova p. 4, chave p. 1, letra E. Prova `downloads/termodinamica/provas/2023-04-30_petrobras-tecnico-operacao-2023-1_prova.pdf`, SHA-256 `316cbcef37c0b0f7521e4d864d5e3f0ee44a16c62d0c627b9a8385df2e917b53`; chave `downloads/termodinamica/gabaritos/2023-04-30_petrobras-tecnico-operacao-2023-1_gabarito.pdf`, SHA-256 `e70aeafd5bc25bc37f6ac89bdce6c98bcdb88f76fc29cae094ca5f847b8a5eec`.

## CR67

**C.** Dilatação tende a alterar o comprimento; restrições podem desenvolver tensões e esforços. Juntas ou flexibilidade acomodam deslocamento dentro dos limites de projeto, sem garantia para qualquer carga ou temperatura. **N/A numérico:** não há comprimento, coeficiente ou temperatura na resolução; não se pode calcular deslocamento ou tolerância. Base `#base-dilatacao`.

Artigo SHA-256 `ce6a14b96095bd3f2b7633028a51832b69ffbc9350cb7d81dfced776b51a6d56`; família `p23`, item original 84, prova p. 4, chave p. 1, letra C. Prova `downloads/termodinamica/provas/2023-04-30_petrobras-tecnico-operacao-2023-1_prova.pdf`, SHA-256 `316cbcef37c0b0f7521e4d864d5e3f0ee44a16c62d0c627b9a8385df2e917b53`; chave `downloads/termodinamica/gabaritos/2023-04-30_petrobras-tecnico-operacao-2023-1_gabarito.pdf`, SHA-256 `e70aeafd5bc25bc37f6ac89bdce6c98bcdb88f76fc29cae094ca5f847b8a5eec`.

## CR68

**C no modelo de radiação indicado; mantido no treino, não estudo crítico sem nota.** Para superfície cinzenta diante de grande vizinhança isotérmica, `Q̇_rad=εσA(T_s⁴−T_v⁴)` em W, com T em K, `σ` em W/(m² K⁴), A em m², ε adimensional e `T_s>T_v`. Mantidos T, área e geometria, a redução de ε reduz a parcela radiativa; não garante igual redução de convecção/condução ou temperatura constante no equipamento real. Faltam emissividades, área e temperaturas de superfície e vizinhança: cálculo de potência e tolerância numérica são N/A. [OpenStax §1.6](https://openstax.org/books/university-physics-volume-2/pages/1-6-mechanisms-of-heat-transfer), base `#base-radiacao-vacuo`.

**Dados suplementares FON-09, auditados mesmo não sendo necessários à resposta:** `1.000 kg/cm³ = 10⁹ kg/m³`, pois `1 cm³=10⁻⁶ m³`. A referência de água líquida a 25 °C e 101,325 kPa é `997,04764 kg/m³`; 1.000 kg/m³ supera-a em `2,95236 kg/m³`, ou `0,2961102%` relativamente à referência, coerente com `≈0,296%`. É aproximação didática na condição declarada, não propriedade constante exata nem pressão necessariamente vigente nos pontos 1 e 2. O original também cita 74 kPa, 133 °C, 5 m e 10 m/s²; esses dados não participam do julgamento de emissividade e não autorizam potência radiativa, cálculo da pressão dos pontos ou uma validação da instalação neste item.

**Reprodução das 15 células corrigidas, tripla (T °C, v líquido m³/kg, v vapor m³/kg):** 101,325 kPa `(99,974; 0,00104344; 1,6732)`; 150 `(111,349; 0,00105273; 1,1593)`; 200 `(120,210; 0,00106052; 0,88568)`; 250 `(127,411; 0,00106722; 0,71866)`; 300 `(133,522; 0,00107317; 0,60576)`. A primeira linha confere com captura WebBook `99,974296; 0,0010434411; 1,6732012`, arredondada respectivamente a 0,001 °C, 10⁻⁸ e 10⁻⁴ m³/kg; limites de meio passo são 0,0005 °C, 5×10⁻⁹ e 5×10⁻⁵ m³/kg. As outras quatro linhas coincidem com [NISTIR 5078 tabela 2, p. impressa 12](https://www.nist.gov/document/nistir5078-tab2pdf#page=2): MPa × 1000 = kPa e cm³/g × 0,001 = m³/kg, ambas conversões exatas. A precisão impressa da fonte é mantida; não implica incerteza experimental da instalação.

**Confronto das 15 células históricas:** ao adotar tolerância de meia unidade na última casa decimal impressa, na linha 101,325 kPa a temperatura `100` e o líquido `0,00104` são compatíveis com os valores de referência, mas o vapor `1,695` difere em `0,0217988 m³/kg`, contra tolerância `0,0005 m³/kg`. Em cada uma das quatro demais linhas, temperatura, líquido e vapor são todos incompatíveis com suas respectivas casas impressas: total 13 incompatíveis e duas compatíveis. A tabela histórica não é usada para cálculo e permanece identificada como transcrição da prova; os dados FON-09 são correção editorial, não errata oficial. A evidência anterior [FON-09 r2](../pareceres/FON-09-r2.md) e auditoria científica r1 são atribuídas ao Auditor anterior; neste exame comparei os valores de tabela e captura e refiz os arredondamentos e conversões.

Artigo SHA-256 `6cfcf2558f6d3651a9b87e8fd4b66b8e29561f17686b4e52b2f40d15ac42fcb8`; família `p24`, item original 85, prova p. 3, chave p. 1, letra C. Prova `downloads/termodinamica/provas/2024-03-24_petrobras-tecnico-operacao-2023-2_prova.pdf`, SHA-256 `54ac87a4aa4f73687e45698a7ee065e4d2331b58862265bef1fa1002abf3f7a3`; chave `downloads/termodinamica/gabaritos/2024-03-24_petrobras-tecnico-operacao-2023-2_gabarito.pdf`, SHA-256 `93d28c3a53eaf1b102081ba57971ed7b049920c1945bb71b3e14e45cb2ba6071`.

## CR69

**C.** Transferência do fluido quente para parede por convecção, através da parede por condução e para fluido frio por convecção; incrustação adiciona resistência térmica. A sequência não fornece taxa sem temperaturas, geometria e coeficientes. Dois fluidos e três etapas são contagens exatas; **N/A para valor e tolerância numéricos**. Base `#base-trocadores`.

Artigo SHA-256 `5fe27c3eaca7cf1d4f584a1720a66065312dcd074301366a59e6cc96387df14f`; família `p24`, item original 90, prova p. 4, chave p. 1, letra C. Prova `downloads/termodinamica/provas/2024-03-24_petrobras-tecnico-operacao-2023-2_prova.pdf`, SHA-256 `54ac87a4aa4f73687e45698a7ee065e4d2331b58862265bef1fa1002abf3f7a3`; chave `downloads/termodinamica/gabaritos/2024-03-24_petrobras-tecnico-operacao-2023-2_gabarito.pdf`, SHA-256 `93d28c3a53eaf1b102081ba57971ed7b049920c1945bb71b3e14e45cb2ba6071`.

## CR70

**E.** Em condução unidimensional de material com `k>0`, `q″=−k dT/dx`; o fluxo aponta contra o gradiente e, espontaneamente, do quente ao frio. Unidades `k` em W/(m K), gradiente K/m e `q″` em W/m². Não há valores de `k`, gradiente ou fluxo a calcular, nem tolerância numérica; o sinal é conclusão simbólica. Base `#base-transferencia`; [OpenStax condução](https://openstax.org/books/university-physics-volume-2/pages/1-6-mechanisms-of-heat-transfer).

Artigo SHA-256 `9cf98a0db0efa097c58cac9de03b4212f1e3683f067a14688ae605350ac0ac52`; família `to`, item original 88, prova p. 3, chave p. 1, letra E. Prova `downloads/termodinamica/provas/2023-10-15_tbg-engenheiro-junior-operacoes_prova.pdf`, SHA-256 `53a8bc2a9cf4142dc548da37f1fa1fe57f46b51408df9de69a0c53bd9d75f356`; chave `downloads/termodinamica/gabaritos/2023-10-15_tbg-engenheiro-junior-operacoes_gabarito.pdf`, SHA-256 `680734f6b47d1381d312a1792ec4818d034812d02661ed1933f477697b399a78`.

## Fontes de auditoria e limites

- `auditoria/termodinamica/PROTOCOLO_AAA.md` — SHA-256 `18f1f299556e8e60c926a1921987f6d2c10cc939aa4aef4487117dc66c344afc`
- `auditoria/termodinamica/evidencias/FON-01/conferencia-80-r1.json` — SHA-256 `563e70deab73fc10c6af355db9a267a5342243427529efc6407a640436278d42`
- `auditoria/termodinamica/pareceres/BAN-10-r2.md` — SHA-256 `f07e4534b4a4c42df78d771d0857cfc1399d3d4330a743297474ef9d69a47d9b`
- `auditoria/termodinamica/pareceres/FON-09-r1-ciencia.json` — SHA-256 `12b6e6375947803b5696ab1e818c1a67852b478424540425f32e31b6a001b904`
- `auditoria/termodinamica/pareceres/FON-09-r2.md` — SHA-256 `efc7142890a7758e8e29cf31cda96e62b641a215d565f1a30c7d90669a84aa60`
- `assets/termodinamica/fon09-cr68-dados-v1.json` — SHA-256 `828b967f1318924742e8b30aca8575549301afcccaad395f9ed5bcee2fc46456`
- `auditoria/termodinamica/evidencias/FON-09/apoio-webbook-saturacao-101325.html` — SHA-256 `ccbfe0998477db30e1acd2c81acb035df65e5aea580dd8147accb5b6f4d88b34`
- `auditoria/termodinamica/evidencias/FON-09/apoio-webbook-densidade-25c-101325.html` — SHA-256 `7bc6b02309d877723dd721a9eab8f9f2ee817d8fa2008c7b4c7de12373f5a01e`

As relações e contas deste parecer foram examinadas pelo revisor atual; FON-01 responde pela leitura documental anterior, BAN-10 pela classificação de uso e FON-09 pelas provas e consultas originais capturadas. As fontes NIST e OpenStax foram consultadas em 29/10/2026; a linha atmosférica e densidade acima usam as capturas identificadas, não se alega nova consulta dinâmica WebBook. Os hashes identificam versões, não demonstram correção por si só. Este apoio é parcial e não substitui decisão do Auditor; não são alegados teste com estudantes, avaliação experimental de incerteza ou aceite global.
