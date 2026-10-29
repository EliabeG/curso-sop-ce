# BAN-08 — apoio independente AV41–AV50

Data 29/10/2026; revisor: agente automatizado `/root/auditoria_av61_70`. Escopo parcial; não aprova BAN-08 nem libera próximo ID. Produto e controle preservados.

HTML `modulos/e1-termodinamica.html`, SHA-256 `80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0`. Os hashes dos itens correspondem ao trecho `<article>...</article>` recodificado em UTF-8. Identidade não substitui análise científica. São itens autorais, não transcrição oficial.

## AV41

**D.** No equilíbrio de fases de substância pura com mesma temperatura e pressão, `μ_liq=μ_vap`; quantidades e densidades podem diferir, de modo que A e B não são exigências. C temperaturas diferentes contraria equilíbrio térmico; E ausência de moléculas de vapor contradiz coexistência; D é a condição química correta. **N/A numérico:** não há valores de μ, densidade, massa ou T nem tolerância de cálculo. Base `#base-equilibrio-fases`.

Artigo SHA-256 `a8e35c751d06cd54ab69a365bf3e2e989296dd85b57c4bd8b5f57125f73d0bb9`.

## AV42

**E sob o modelo convencional da base, com ressalva de totalidade.** `W=1000 kJ`, `Q_H=4000 kJ`, `η=W/Q_H=0,25=25%`; se esses são o calor total recebido e o trabalho líquido, `Q_L=4000−1000=3000 kJ`. A `1000/3000=33,333…%→33,3%` usa denominador de rejeição; B 100% não é a razão; C `4000/1000=400%` inverte a razão; D `3000/4000=75%` é fração rejeitada; E 25% correta. A aproximação 33,3% tem erro <0,05 ponto percentual; demais resultados são exatos para valores nominais. Não há incerteza medida informada.

**Limite de suficiência a adjudicar:** a base `#base-eficiencia-cop`, acessível antes da resposta, apresenta um motor com `Q_H`, `Q_L` e `W=Q_H−Q_L`; o comando menciona 4000 kJ de uma fonte, sem declarar literalmente que essa é toda a entrada térmica. Sem essa interpretação de totalidade, por exemplo um segundo aporte de 1000 kJ e rejeição de 4000 kJ dariam o mesmo trabalho líquido de 1000 kJ e eficiência por calor total de 20%, não oferecida. Com entradas ambas a 600 K e rejeição a 300 K, a geração total de entropia seria `4000/300−5000/600=5 kJ/K>0`, compatível com a segunda lei. O exemplo não declara falsa a conta convencional e não reivindica que tenha sido intenção do autor incluir outras fontes; aponta condição relevante para interpretação e para os valores de rejeição do comentário. BAN-07 anterior aprovou E sob modelo usual; recomendo ao Auditor decidir suficiência diante do precedente de CR45, sem alterar produto nesta revisão. Bases `#base-eficiencia-cop`, `#base-leitura-matematica`.

Artigo SHA-256 `83c8604cddfbc4d5f0d6782bd8605ff8eb9d462661716b4d69fc2abbdfbb89a9`.

## AV43

**D.** `ΔS_total=−0,50+0,60=+0,10 kJ/K` para água e vizinhança isolados: geração positiva é compatível com segunda lei e indica irreversibilidade. A `+1,10` soma módulos e chama reversível geração positiva; B `−0,10` troca sinal e seria inadmissível no conjunto isolado; C zero não é a soma e congelamento é possível; D +0,10 correta; E considera apenas água. Valores nominais e operações exatos, sem incertezas; a segunda lei exige `ΔS_total≥0`, não que cada parte aumente. Base `#base-entropia`.

Artigo SHA-256 `8d32bb5b9ad7673e2a58d15b3e6ea37751add3e2d9b7b3f3376a390cd3c6ba68`.

## AV44

**A.** Sistema fechado em ciclo: `ΔU_ciclo=0`; se todas as etapas adiabáticas, `Q_líquido=0`; se também `ΔEc=ΔEp=0`, primeira lei dá `W_líquido=0`. I, II e III verdadeiras; B omite I/III, C omite I, D omite III e E omite II/III. Zeros são exatos sob condições ideais, não valores medidos; sem quantidades numéricas ou arredondamento, tolerância de medida N/A. A conclusão é para ciclo completo, não exige trabalho nulo em cada etapa. Bases `#base-carnot-prova`, `#base-trabalho-fronteira`.

Artigo SHA-256 `192525a6985a995bb6e73ab56148c54fd89b7e2ed2dd7315aaba7db5d56386b9`.

## AV45

**E sob modelo de duas fontes e totalidade das trocas.** Com `Q_H=1000 kJ`, `T_H=600 K`, `T_L=300 K`, ciclo entre as duas fontes e sem outras trocas de energia além do calor das duas fontes e do trabalho líquido, `η_C=1−300/600=0,50`, `W_máx=500 kJ`, `Q_L,mín=500 kJ`. A `1000×300/(600+300)=333,333… kJ→333,3 kJ`, erro <0,05 kJ, e daria `η≈66,7%`; B 1000 dá trabalho nulo, não rejeição mínima; C 300 daria 70%; D zero daria 100%; E 500 é limite reversível. Resultados nominais exatos salvo arredondamento indicado; sem incerteza empírica informada. Bases `#base-carnot-prova`, `#base-limite-carnot` explicitam duas fontes.

**Limite de suficiência a adjudicar:** o artigo menciona fonte quente, fria e Q recebido, mas não diz textualmente que não há outras fontes ou interações de energia. Os valores publicados são corretos na convenção de máquina de duas fontes ensinada na base, assumida no BAN-07; se outras entradas forem permitidas, a comparação pode mudar. Como exemplo, 1000 kJ adicionais da mesma temperatura quente tornam a rejeição mínima ao reservatório frio 1000 kJ para o ciclo reversível de 600/300 K; não se pode inferir o mínimo de 500 kJ a partir de uma única parcela de 1000 kJ. O exemplo evidencia a hipótese de totalidade, não acusa erro aritmético nem atribui intenção ao autor. Recomendo adjudicação de clareza/suficiência pelo Auditor à luz do precedente CR45.

Artigo SHA-256 `3babe8cb08138fd4ad42f7358c5208b70974370d17a62d30490075e7b5019b50`.

## AV46

**B.** Carnot motor reversível entre duas temperaturas distintas tem quatro etapas: duas isotérmicas reversíveis para trocas de calor e duas adiabáticas reversíveis que conectam as temperaturas. A duas isobáricas e duas isocóricas não define Carnot; B correta; C quatro isotermas na mesma temperatura não conecta fontes distintas; D troca isotermas por isocóricas; E adiabáticas irreversíveis violam reversibilidade. Duas e quatro são contagens exatas; temperaturas e calor não são dados numéricos, logo tolerância de medida N/A. Base `#base-carnot-prova`.

Artigo SHA-256 `0c048ab1b4c1148d9a424b0a9b55a2ddb097ba7fc79dc6a22b04c6447538721b`.

## AV47

**A.** Centrífugos são associados a grandes vazões e alternativos podem atender vazões menores e razões de pressão elevadas, como orientação geral; curvas e gás definem escolha. B afirma falsamente que alternativo não comprime, C ignora condições, D universaliza vazões pequenas para centrífugos, E pressupõe rendimento igual. Sem valores de pressão, vazão ou eficiência, cálculo e tolerância numéricos N/A. Base `#base-tipos-compressores`.

Artigo SHA-256 `afa4aa8e9dea38573de54e969025a80d66d7aa08af3cb3f4d98f4d8ff996e280`.

## AV48

**A.** Para recuperação passiva em trocador sem bomba de calor, a entrada quente deve estar acima da entrada fria; diferenças de temperatura e operação determinam quanto é recuperado. A é condição necessária; B mistura não é obrigatória; C compressor não deixa de receber trabalho; D calor espontâneo fluiria no sentido oposto; E igualdade em todo o trocador elimina força motriz térmica. Sem temperaturas, área ou efetividade, cálculo numérico e tolerância N/A. Bases `#base-brayton`, `#base-trocadores`; [US DOE, recuperador](https://www.energy.gov/hgeo/how-gas-turbine-power-plants-work).

Artigo SHA-256 `810f21fc17823ad01aee37087182a58186ca27b6c46afcf0a1c12f3dabd26f87`.

## AV49

**C, única incorreta no modelo e arranjo descritos.** A adição e B rejeição de calor são isobáricas no Brayton ideal; C troca passiva não substitui compressor nem necessariamente eleva pressão; D perdas reais nos trocadores são possíveis; E o compressor convencional consome trabalho. Sem pressões, calor ou trabalho numéricos, tolerância de cálculo N/A. Base `#base-brayton-real`; [MIT, Brayton ideal](https://web.mit.edu/16.unified/OldFiles/www/SPRING/thermodynamics/notes/node27.html).

Artigo SHA-256 `ba294a58c27857ff270db5bc1300c7823b7bee36997791c77c678e9ecb04d7d1`.

## AV50

**C.** Em regime permanente adiabático e ΔEc/ΔEp desprezíveis, `w_c=h₂−h₁` consumido e `w_t=h₃−h₄` produzido, em kJ/kg se entalpias específicas em kJ/kg. Para cada componente com mesma entrada e pressão de saída e mesmo fluido, a saída real tem entalpia ao menos tão alta quanto a saída isentrópica: `h₂,r≥h₂,s`, `h₄,r≥h₄,s`; logo `w_c,r≥w_c,s` e `w_t,r≤w_t,s`. A sugere consumo zero, B igualdade obrigatória, D inverte efeitos, E afirma rendimento acima do reversível; C corresponde à comparação. Com trabalho específico em base mássica consistente, `w_líquido=w_t−w_c` diminui na comparação. A conclusão não implica que um compressor com resfriamento tenha o mesmo limite, nem compara duas máquinas com entradas diferentes sem normalização. Sinais e igualdades limites são simbólicos; faltam entalpias ou vazões para cálculo e tolerância N/A. Bases `#base-isentropica`, `#base-brayton-real`.

Artigo SHA-256 `a81b2fc4861de1cbe533079250396bc9c268ca3b02f3d2f7a9956b1434a4d8a3`.

## Fontes de auditoria e limites

- `auditoria/termodinamica/PROTOCOLO_AAA.md` — SHA-256 `18f1f299556e8e60c926a1921987f6d2c10cc939aa4aef4487117dc66c344afc`
- `auditoria/termodinamica/evidencias/BAN-08/inventario-numerico-197-r1.json` — SHA-256 `5b56e8280d35d590bf11ddbff9b0e789faed257fafe1cad9c4854cc5ac5fd99f`
- `auditoria/termodinamica/pareceres/BAN-07-auditor-bloco-av41-45-r1.json` — SHA-256 `56a6537e706c72676f7670e5bb3428bf9a0c09874fd916a80db73ca75a58ccbc`
- `auditoria/termodinamica/pareceres/BAN-07-r3.md` — SHA-256 `009adc698bf2f88e28826b389a48e2526660efc9b7cc2ea3b598f0e06026d68b`

As contas, condições e cinco juízos de cada item foram examinados pelo revisor atual, com conhecimento prévio das respostas. BAN-07 é trabalho anterior atribuído, e identidade não substitui revisão numérica ou adjudicação. Fontes MIT, OpenStax e US DOE foram consultadas em 29/10/2026. As ressalvas de AV42/45 são submetidas ao Auditor, não alteram o aceite anterior por decisão unilateral nem estabelecem intenção do autor. Sem ensaio com estudantes, certificação externa, inferência de incerteza instrumental ou aprovação global BAN-08.
