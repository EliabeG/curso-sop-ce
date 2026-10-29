# BAN-08 — apoio independente AV01–AV10

Data 29/10/2026; revisor: agente automatizado `/root/auditoria_av61_70`. Escopo parcial; não aprova BAN-08 nem libera próximo ID. Produto e controle preservados.

HTML `modulos/e1-termodinamica.html`, SHA-256 `80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0`. Os hashes dos itens correspondem ao trecho `<article>...</article>` recodificado em UTF-8. Identidade não substitui análise científica. São itens autorais, não transcrição oficial.

## AV01

**C.** Divisão em duas partes iguais, mesmo estado e composição: `m/2`, `V/2`, `U/2`, `H/2`; `T` e `ρ=(m/2)/(V/2)=m/V` preservadas. A: massa e V totais variam; B: U total e massa variam; C: T e ρ conservadas; D: H e V totais variam; E: T conserva, mas massa não. Metade é razão exata do modelo, sem valores medidos, unidades ou tolerância numérica informados. Bases `#base-propriedades`, `#base-medidas`.

Artigo SHA-256 `fef921d85b9f61c1e2a63b23fa1df1a9479973608dea0c768045e221f31390b5`.

## AV02

**A, única incorreta.** Energia interna é função de estado; B pressão de equilíbrio é propriedade; C calor e trabalho são transferências; D trabalho pode depender do caminho; E `ΔU=U_f−U_i` igual para mesmos estados inicial e final. Em A, o valor final não depende do caminho para o mesmo estado final. **N/A numérico:** não há valores ou operação quantitativa com resultado a arredondar, nem tolerância. Bases `#base-propriedades`, `#base-balanco-fechado`.

Artigo SHA-256 `8b7328a79ca6b50995426770504df6de88f6bf37cf7a3038fef9709847d6bc20`.

## AV03

**B.** Julgamentos I verdadeiro (movimento em líquido), II verdadeiro (vibrações em sólidos), III falso (energia cinética microscópica não é exclusiva dos gases). Assim A V-F-V, C F-F-V, D V-V-V e E F-V-V divergem; só B V-V-F satisfaz os três. I–III são rótulos, três afirmações e cinco opções são contagens exatas. Sem dados de velocidades ou energias: cálculo e tolerância numéricos N/A. Base `#base-molecular`.

Artigo SHA-256 `6e8bc6e49193f08a8c5f0ae6b4271720a23a29e7888ecfe6cf83faaa63ff85fa`.

## AV04

**D.** Aproximação de volume específico quase constante na faixa indicada, não volume nulo. A é falsa porque massa em volume de controle pode variar; B é falsa porque a pressão pode subir na bomba; C confunde incompressibilidade com `v=0`; D corresponde ao modelo; E é falsa pois T pode variar sem variação relevante de v. O zero de C é valor impossível para fluido de massa e volume finitos, não resultado de cálculo. Não há valores de variação, propriedades ou tolerância informada; N/A numérico. Base `#base-medidas`.

Artigo SHA-256 `6ed8f664d46db759064d42ee073379bda2b8c1c7018ae3418d22774e14f72501`.

## AV05

**B.** Tempo em segundo, temperatura termodinâmica em kelvin e quantidade de matéria em mol. A minuto e grau Celsius não são unidades de base; C joule mede energia; D Fahrenheit não é base e kg é massa; E hora não é base e newton é força. Não há valores numéricos de medida, conversões a calcular ou tolerância: N/A numérico. Base `#base-medidas`, [BIPM, unidades de base](https://www.bipm.org/en/measurement-units/si-base-units).

Artigo SHA-256 `8860a27c54eebc598b479ab61197026acb81cf4d81a143876bfe55fea2a6fa4c`.

## AV06

**C.** Pares nominais `(Y,X)=(20,0)` e `(70,100)` fixam, para escalas lineares, inclinação `(100−0)/(70−20)=2` unidades X por unidade Y e intercepto `−40` unidades X: `X=2(Y−20)=2Y−40`. Em `Y=45`, `X=50`; posição fracionária `(45−20)/(70−20)=1/2`. A `45` confunde as escalas; B `70` é coordenada Y do segundo ponto; C `50` correta; D `90=2×45` omite origem; E `25=45−20` omite ganho. Só C fornece o valor calculado. A distância até o distrator numérico mais próximo é 5 unidades X: tolerância de comparação menor que 2,5 evitaria sobreposição de vizinhanças iguais, mas não representa incerteza real. Os dados nominais são exatos no modelo e não são informadas incertezas de calibração. Figura inspecionada: esquema genérico, sem números de calibração, `assets/questoes-reais-e1/figura-922604ee21ac.png`, SHA-256 `922604ee21ac25fec713806a3102c7b775b9cd16ba2c77054cb45d976226b17e`; não medir distâncias do desenho. Bases `#base-leitura-matematica`, `#base-instrumentos`.

Artigo SHA-256 `89dc4205deb6e31424ecf39c1abc0a270339b7200d33d281f528f7c28762e87d`.

## AV07

**E.** No manômetro de Bourdon descrito, deformação do tubo responde à diferença de pressão; A é princípio de termômetro de líquido, B não mede energia interna diretamente, C não mede umidade, D não é medidor de vazão por rotações, E pressão. Não se generaliza que nenhum elemento Bourdon possa integrar um sistema termométrico. **N/A numérico:** sem grandeza medida ou resultado numérico; tolerância não se aplica. Base `#base-instrumentos`.

Artigo SHA-256 `f6c6439615c358a02d91c7dbc1450c5550f193cc38a4af0f5e8c8a2958804251`.

## AV08

**C.** `span=limite superior−limite inferior`; `20 °C + 80 °C de intervalo=100 °C`. A `80 °C` confunde intervalo e limite, B `20 °C` repete inferior, C `100 °C` é correta, D `180 °C=20+2×80` duplica o span, E `60 °C=80−20` subtrai indevidamente. Intervalo de 80 °C corresponde a 80 K de diferença, sem converter o valor absoluto usando apenas fator multiplicativo. Menor separação da opção correta é 20 °C; tolerância numérica estritamente menor que 10 °C impediria sobreposição de vizinhanças iguais, mas valores são nominais, não foi dada incerteza do instrumento. Bases `#base-instrumentos`, `#base-leitura-matematica`; [NIST temperatura](https://www.nist.gov/pml/owm/si-units-temperature).

Artigo SHA-256 `2cbb9953a0ca46eda6b4cf9144bd13b7d0849822d9ed02ecaa0c6d010f3b7d07`.

## AV09

**B.** I verdadeira: kelvin é unidade de base de temperatura termodinâmica; II verdadeira: intervalo `Δ10 °C=Δ10 K`; III falsa porque `T/K=t/°C+273,15` dá `10+273,15=283,15 K`, não 10 K, diferença de 273,15 K. A inclui III falsa; B contém I e II; C omite II; D inclui III e omite I/II; E inclui III e omite I. As conversões e o deslocamento são exatos; os dados são nominais e não se informou incerteza ou arredondamento. A verificação da sequência depende das três afirmações, não só de proximidade numérica. Bases `#base-absolutas`, `#base-medidas`; [NIST](https://www.nist.gov/pml/owm/si-units-temperature) e [BIPM](https://www.bipm.org/en/measurement-units/si-base-units).

Artigo SHA-256 `c132589fa0387abc5108633a2b130632334db4cebf0479b9442bc9158ae78f30`.

## AV10

**B.** `ρ=m/V=12 kg/0,015 m³=800 kg/m³`, propriedade intensiva para amostra homogênea no mesmo estado. O inverso `v=V/m=0,015/12=0,00125 m³/kg`, logo A dá volume específico, não massa específica; C `80 kg/m³` erra por fator 10; D `0,18` provém de `12×0,015` e tem dimensão kg·m³, além de classificação errada; E dá `800 kg/m³` mas chama extensiva a propriedade. B e E têm valores numéricos idênticos e só o par valor/classificação distingue a resposta: nenhuma tolerância numérica isolada resolve essa distinção. Considerando os dados nominais como exatos, divisão e recíproco são exatos; nenhuma incerteza das medições foi informada. Bases `#base-leitura-matematica`, `#base-medidas`, `#base-propriedades`.

Artigo SHA-256 `a4e565a479f34fa4e36835bcb186f5b99d0f3ce3000b500f458c4c1c1863032e`.

## Fontes de auditoria e limites

- `auditoria/termodinamica/PROTOCOLO_AAA.md` — SHA-256 `18f1f299556e8e60c926a1921987f6d2c10cc939aa4aef4487117dc66c344afc`
- `auditoria/termodinamica/evidencias/BAN-08/inventario-numerico-197-r1.json` — SHA-256 `5b56e8280d35d590bf11ddbff9b0e789faed257fafe1cad9c4854cc5ac5fd99f`
- `auditoria/termodinamica/pareceres/BAN-07-auditor-bloco-av06-10-r1.json` — SHA-256 `f9871fce521b27846f99ec35c94888b6297b953dfa7312193914e9d27b95d17f`
- `auditoria/termodinamica/pareceres/BAN-07-r2-cientifico-independente.md` — SHA-256 `a803a1a25575bba920eea8960186e73cc4cdc4878a23cfac0cc199f0ef592abf`
- `auditoria/termodinamica/pareceres/BAN-07-r3.md` — SHA-256 `009adc698bf2f88e28826b389a48e2526660efc9b7cc2ea3b598f0e06026d68b`

As contas e os cinco juízos de cada item foram examinados pelo revisor atual, com conhecimento prévio das respostas. BAN-07 é trabalho anterior atribuído, e a identidade não substitui a revisão numérica atual. Fontes NIST e BIPM consultadas em 29/10/2026. Critérios geométricos de separação são critérios auxiliares, não especificações de instrumento ou incertezas de medição. Sem ensaio com estudantes, certificação externa, ou aprovação global BAN-08.
