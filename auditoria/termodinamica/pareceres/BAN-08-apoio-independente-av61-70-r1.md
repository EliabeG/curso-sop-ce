# BAN-08 — apoio independente AV61–AV70

Data 29/10/2026; revisor: agente automatizado `/root/auditoria_av61_70`. Escopo parcial; não aprova BAN-08 nem libera próximo ID. Produto e controle preservados.

HTML `modulos/e1-termodinamica.html`, SHA-256 `80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0`. Os hashes dos itens correspondem ao trecho `<article>...</article>` recodificado em UTF-8. Identidade não substitui análise científica. São itens autorais, não transcrição oficial.

## AV61

**D.** `η_vol=0,008/0,010=0,80=80%`, com o volume admitido referido às condições de sucção e volumes na mesma unidade; quociente adimensional. A 8% erra escala percentual; B 20% é `1−0,80`; C 100% pressupõe igualdade; D 80% correta; E `0,010/0,008=1,25=125%` inverte razão. Dados nominais e operações exatas, sem incerteza da medição ou arredondamento informados. Base `#base-eficiencia-volumetrica`.

Artigo SHA-256 `2ef609887b7c6e57a7b9a8f38f7760b69c0ffe4377c1c2b43d307101ffd1be86`.

## AV62

**D.** Na admissão normal, válvula de entrada aberta e de descarga fechada; válvula automática requer pressão na linha de sucção maior que na câmara, com diferencial suficiente para vencer sua resistência. A descreve descarga; B inverte diferencial; C duas fechadas impedem admissão; D correta; E ambas abertas não descrevem a sucção normal. Duas válvulas é contagem exata, sem pressões numéricas para cálculo ou tolerância. A etapa de admissão não se confunde com todo o retorno/reexpansão do pistão. Base `#base-valvulas-compressor`; [GUNT ET 508](https://gunt.de/en/products/fluid-machinery/driven-machines/fans-and-compressors/simulation-of-a-two-stage-air-compressor/061.50800/et508/glct-1:pa-148:ca-752:pr-240).

Artigo SHA-256 `795e127dad4361f30a6056f49479171b12c849388cdcdebde7fc09561be75ae7`.

## AV63

**D.** Brayton convencional tem duas etapas isentrópicas e duas isobáricas. A Rankine é ciclo usual a vapor, não motor de centelha; B associa a Brayton os processos indicados e Stirling a duas isotermas e duas isocóricas com regeneração; C Otto é modelo de motor com aquecimento ideal isocórico, não ciclo de vapor; D correta; E Carnot é reversível, duas isotérmicas e duas adiabáticas reversíveis, não quatro isobáricas irreversíveis. Contagens de etapas são exatas; sem dados de estado, potência ou calor para cálculo, tolerância N/A. Base `#base-comparar-ciclos`; [MIT Brayton](https://web.mit.edu/16.unified/OldFiles/www/SPRING/thermodynamics/notes/node27.html).

Artigo SHA-256 `e5ee106ebb64b6a28b89d824d5ee934c4be36dcde18a147d6d65c94bac558c00`.

## AV64

**D.** A compressão de gás aprisionado reduz volume, no pistão ou entre rotores e carcaça do parafuso. A volume constante contraria mecanismo; B descarga não é obrigatoriamente vácuo; C confunde rotor e difusor dos compressores dinâmicos; D correta; E entrada de energia mecânica é necessária no arranjo usual. Duas máquinas são contagem exata; sem volumes, pressões e trabalho não há valor numérico ou tolerância. Base `#base-tipos-compressores`.

Artigo SHA-256 `d7a2c29feee7ebd705e93fe6d8c6d222c7f365d15e9d5ffd75650f3f900c44df`.

## AV65

**C.** No modelo de uma entrada e saída, regime permanente, calor, ΔEc e ΔEp desprezíveis e trabalho útil de eixo: `Δh=3200−2800=400 kJ/kg`, `Ẇ=2 kg/s×400 kJ/kg=800 kJ/s=800 kW`. A 400 usa apenas a queda específica e omite vazão, inclusive sua unidade; B `2×3200=6400 kW` omite saída; C 800 correta; D `2×(3200+2800)=12000 kW` soma entalpias; E −800 inverte sinal de potência produzida. Valores nominais são exatos para o exercício, sem incerteza ou tolerância instrumental informada; não se pressupõe que a turbina seja reversível. Base `#base-turbina-potencia`; [MIT, balanço em regime permanente](https://web.mit.edu/16.unified/OldFiles/www/SPRING/thermodynamics/notes/node18.html).

Artigo SHA-256 `5f993c3d09879d8de3fd56710cb38d657dd3415112868673a9bed285aa473000`.

## AV66

**A, única incorreta.** Em casco e tubos íntegro, as duas correntes não se misturam como requisito; A afirma o contrário. B condução na parede, C fluido dentro dos tubos, D convecção entre fluidos e parede, E fluido no lado do casco são compatíveis com o arranjo. Duas correntes são contagem exata; sem dados de temperaturas, área ou taxa, cálculo e tolerância numéricos N/A. Base `#base-trocadores`; [OpenStax, mecanismos de transferência](https://openstax.org/books/university-physics-volume-2/pages/1-6-mechanisms-of-heat-transfer).

Artigo SHA-256 `414e4a69cb79528ed86dcb04c0172f1f99eba044f8975a08ca92bbf212601946`.

## AV67

**A.** Com dilatação linear livre e uniforme `ΔL=αLΔT=(12×10⁻⁶ K⁻¹)(20 m)(50 K)=0,012 m=12 mm`. A 12 mm correta; B 12 m exagera o resultado em 1000 vezes; C 120 mm é 10 vezes maior; D 1,2 mm é 10 vezes menor; E 0,012 mm confunde resultado em metros com milímetros. Conversão `1 m=1000 mm` é exata; dados e produto nominais são exatos na aproximação declarada. Não há incertezas de medição nem expansão adicional por restrições atribuídas. Base `#base-dilatacao`.

Artigo SHA-256 `c234657d9d082fb9ca732f48724916a7c267b2048c8fca190ae934f62fb6ba84`.

## AV68

**D.** Superfície cinza pequena cercada por grande ambiente aproximadamente negro, `T_s>T_amb`, com temperaturas absolutas, área e geometria fixas: `Q̇_rad=εσA(T_s⁴−T_amb⁴)`, portanto `Q̇_f/Q̇_i=ε_f/ε_i=0,20/0,80=0,25` e redução `1−0,25=0,75=75%`. A inverte fração remanescente e redução: 75% restante/25% reduzido; B usa diretamente ε final como 20% restante; C toma `0,80−0,20=0,60` como 60% restante e diz 40% de redução, mas essa diferença não é razão de perdas; D 25% restante/75% reduzido correta; E `0,80/0,20=4` inverte razão. A taxa em W requer `σ` em W/(m² K⁴), mas as temperaturas e a constante se cancelam; não se aplica a convecção e condução. Frações são exatas com dados nominais e modelo, sem incerteza experimental fornecida. Figura examinada apresenta componentes e rótulos 1–3 de estado, sem valores de emissividade ou temperatura adicionais: `assets/questoes-reais-e1/figura-b8d543e37fc8.png`, SHA-256 `b8d543e37fc85224e69507c5bf2aa35d6ac5aeb3eb5ae37879c4806e229f30b8`. Base `#base-radiacao-vacuo`; [OpenStax, radiação](https://openstax.org/books/university-physics-volume-2/pages/1-6-mechanisms-of-heat-transfer).

Artigo SHA-256 `856b39ea9bb6e14936108cc8f0cc0633ac20f6777777c30320e28414e1f6207d`.

## AV69

**A.** Para as duas correntes separadas por parede, sequência convecção lado quente, condução na parede, convecção lado frio. B atribui convecção à parede sólida; C mistura na parede e radiação obrigatória; D exclui condução e convecção apenas porque há metal; E mistura correntes explicitamente separadas. Duas correntes e três etapas são contagens exatas; sem temperaturas, geometria ou coeficientes, valor de calor e tolerância numérica N/A. Base `#base-trocadores`; [OpenStax, mecanismos de transferência](https://openstax.org/books/university-physics-volume-2/pages/1-6-mechanisms-of-heat-transfer).

Artigo SHA-256 `f1ade775126752789740119acdb33f04190299cc54d46883e4e0354d7c6e6fee`.

## AV70

**B.** Face quente `80 °C`, fria `20 °C`, `ΔT=60 °C` de intervalo `=60 K`; em Kelvin as temperaturas são `353,15 K` e `293,15 K`, mantendo ordenação. A inverte sentido; B quente para frio correta; C conversão de escala não é necessária para comparar; D localização externa/interna não determina direção; E fluxo líquido não é nulo para parede condutora com gradiente. Por Fourier, `q″=−k dT/dx` com `k>0`; não há k, espessura ou área para calcular fluxo ou tolerância de medição. Conversão de escala e diferença são exatas nos valores nominais. Base `#base-transferencia`; [OpenStax](https://openstax.org/books/university-physics-volume-2/pages/1-6-mechanisms-of-heat-transfer).

Artigo SHA-256 `aa3759b74d4479c6c2c7e76f4ad964b19344b6c1b13593c027dac0358a2600da`.

## Fontes de auditoria e limites

- `auditoria/termodinamica/PROTOCOLO_AAA.md` — SHA-256 `18f1f299556e8e60c926a1921987f6d2c10cc939aa4aef4487117dc66c344afc`
- `auditoria/termodinamica/evidencias/BAN-08/inventario-numerico-197-r1.json` — SHA-256 `5b56e8280d35d590bf11ddbff9b0e789faed257fafe1cad9c4854cc5ac5fd99f`
- `auditoria/termodinamica/pareceres/BAN-07-r2-cientifico-independente.md` — SHA-256 `a803a1a25575bba920eea8960186e73cc4cdc4878a23cfac0cc199f0ef592abf`
- `auditoria/termodinamica/pareceres/BAN-07-r3.md` — SHA-256 `009adc698bf2f88e28826b389a48e2526660efc9b7cc2ea3b598f0e06026d68b`

Cálculos e cinco juízos de cada item examinados pelo revisor atual, com conhecimento prévio das respostas. BAN-07 é trabalho anterior atribuído; identidade não substitui revisão científica atual. Fontes MIT, OpenStax e GUNT consultadas em 29/10/2026. Sem ensaio com estudantes, certificação externa, incerteza de instrumentos inferida ou aprovação global BAN-08.
