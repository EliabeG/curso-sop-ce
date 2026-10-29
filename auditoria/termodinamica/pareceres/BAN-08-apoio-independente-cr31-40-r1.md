# BAN-08 — apoio independente CR31–CR40

Data 29/10/2026. Revisor: agente automatizado `/root/auditoria_av61_70`. Escopo parcial; não aprova BAN-08 nem libera próximo ID. Produto e controle preservados.

HTML `modulos/e1-termodinamica.html`, SHA-256 `80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0`. Os hashes por artigo são dos trechos brutos `<article>...</article>` recodificados em UTF-8. PDF de provas e chaves conferidos por hash com FON-01; a leitura visual documental é atribuída a FON-01, não repetida integralmente nesta rodada. Identidade não substitui análise científica.

Fontes: protocolo AAA SHA-256 `18f1f299556e8e60c926a1921987f6d2c10cc939aa4aef4487117dc66c344afc`; `auditoria/termodinamica/evidencias/FON-01/conferencia-80-r1.json` SHA-256 `563e70deab73fc10c6af355db9a267a5342243427529efc6407a640436278d42`; `auditoria/termodinamica/pareceres/BAN-10-r2.md` SHA-256 `f07e4534b4a4c42df78d771d0857cfc1399d3d4330a743297474ef9d69a47d9b`; `auditoria/termodinamica/pareceres/BAN-07-auditor-heranca-cr16-35-r1.md` SHA-256 `91955b0a8dd0a10c61027de8e9715e666f78fa279c65c83d1b4d1aae8e42ca03`; `auditoria/termodinamica/pareceres/BAN-07-auditor-heranca-cr36-50-r1.json` SHA-256 `a307cdf629f4b6173d8717bc473f0c455df17f0bc96b24b41ca4df86a22c09d8`. A revisão dos cálculos e condições neste relatório é deste revisor; a classificação crítica é atribuída ao trabalho BAN-10, e os pareceres BAN-07 acima são revisões prévias, sem tratar identidade como aceite numérico. Referências externas consultadas em 29/10/2026.

## CR31

**E.** Poder calorífico expressa energia liberada por quantidade especificada de combustível; no PCS a água formada é considerada condensada, no PCI permanece como vapor nas condições de referência. A resolução contrapõe liberação a absorção. **N/A numérico:** não fornece quantidade, poder calorífico ou operação quantitativa; sem arredondamento ou tolerância aplicável. A distinção requer referência de estado da água. Base `#base-termoquimica`.

Artigo SHA-256 `1195cc79755f79294771716075f277cae296343160770608c81367b2c7272bc3`; família `p24`, item original 71, prova p. 2, chave p. 1, letra E. Prova `downloads/termodinamica/provas/2024-03-24_petrobras-tecnico-operacao-2023-2_prova.pdf`, SHA-256 `54ac87a4aa4f73687e45698a7ee065e4d2331b58862265bef1fa1002abf3f7a3`; chave `downloads/termodinamica/gabaritos/2024-03-24_petrobras-tecnico-operacao-2023-2_gabarito.pdf`, SHA-256 `93d28c3a53eaf1b102081ba57971ed7b049920c1945bb71b3e14e45cb2ba6071`.

## CR32

**C.** Para os mesmos estados e condições, `ΔH_inversa = −ΔH_direta`; a pressão constante e somente trabalho de expansão, `Q_p=ΔH`. Logo reação direta exotérmica tem `ΔH<0`, a inversa `ΔH>0`. Zero é fronteira de sinal, não resultado de medição. **N/A numérico:** sem valores de Q ou ΔH, nem arredondamento a tolerar. Bases `#base-termoquimica` e `#base-balanco-fechado`.

Artigo SHA-256 `91cacfbdd2254fd2ad8c183e18f65d94da3156c40a211242599f800a554f73d9`; família `p24`, item original 72, prova p. 2, chave p. 1, letra C. Prova `downloads/termodinamica/provas/2024-03-24_petrobras-tecnico-operacao-2023-2_prova.pdf`, SHA-256 `54ac87a4aa4f73687e45698a7ee065e4d2331b58862265bef1fa1002abf3f7a3`; chave `downloads/termodinamica/gabaritos/2024-03-24_petrobras-tecnico-operacao-2023-2_gabarito.pdf`, SHA-256 `93d28c3a53eaf1b102081ba57971ed7b049920c1945bb71b3e14e45cb2ba6071`.

## CR33

**E.** Recipiente fechado, rígido e isolado, massa e composição fixas, sem outras interações de trabalho e desprezando ΔEc e ΔEp: `Q=W=0`, `ΔU=Q−W=0`. Para gás ideal `U=U(T)` e capacidade térmica positiva, `ΔT=0`; para expansão efetiva `V₂>V₁`, `ΔS=mR ln(V₂/V₁)>0`, apesar de `ΔT=0`. Esses zeros são exatos no modelo; o enunciado não dá valores para calcular magnitudes ou tolerância numérica. A figura recriada examinada não fornece razão de volumes: `assets/questoes-reais-e1/figura-9d164690a624.png`, SHA-256 `9d164690a6243cb31b9ea0f734b9a85ad4c6570398b9d5ef9278e4f44332bcc2`. Bases `#base-expansao-livre`, `#base-entropia-gas`.

Artigo SHA-256 `06e5d8361e1d50448ff26839517404fe07244c5ec74c1594371c11da6536997a`; família `to`, item original 72, prova p. 3, chave p. 1, letra E. Prova `downloads/termodinamica/provas/2023-10-15_tbg-engenheiro-junior-operacoes_prova.pdf`, SHA-256 `53a8bc2a9cf4142dc548da37f1fa1fe57f46b51408df9de69a0c53bd9d75f356`; chave `downloads/termodinamica/gabaritos/2023-10-15_tbg-engenheiro-junior-operacoes_gabarito.pdf`, SHA-256 `680734f6b47d1381d312a1792ec4818d034812d02661ed1933f477697b399a78`.

## CR34

**Chave documental C, estudo crítico sem nota.** No balanço `ΔU+ΔEc+ΔEp=Q−W`, com Q entrante e W realizado positivos, `ΔU=Q` equivale exatamente a `W+ΔEc+ΔEp=0`; cada parcela nula é condição suficiente, não necessária. Isocoria elimina apenas o trabalho de fronteira simples. Para massa e composição fixas de gás ideal simples, estados de equilíbrio no mesmo volume, `c_v(T)>0`, e calor exclusivamente entrante não nulo através de fronteiras com temperaturas finitas positivas, `ΔS=∫δQ/T_b+S_ger>0`; como `v₂=v₁`, `ΔS=m∫(c_v/T)dT>0` implica `T₂>T₁` e `ΔU=m∫c_v dT>0`. Não exige reversibilidade nem que W total seja zero. O texto original afirma aumento de U, não igualdade com Q; trabalho arbitrário que viole a segunda lei não é contraprova. Os zeros das hipóteses e desigualdades são simbólicos, sem dados para cálculo de magnitude ou tolerância. Fonte [MIT balanço](https://web.mit.edu/16.unified/www/SPRING/thermodynamics/notes/node14.html) e [MIT entropia do gás ideal](https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node40.html); bases `#base-balanco-fechado`, `#base-gas-energia`. Não se atribui esta demonstração autoral à banca.

Artigo SHA-256 `ba60d9d912f78315cdfe332ad32107d522a0167da5efa18185add0caa81030c5`; família `trf`, item original 53, prova p. 1, chave p. 1, letra C. Prova `downloads/termodinamica/provas/2025-01-19_trf6-analista-engenharia-mecanica_prova.pdf`, SHA-256 `74a764fdb11ca13d527674c39206f44cbd4b5b1392cdee1f8bce9d8016ac4d79`; chave `downloads/termodinamica/gabaritos/2025-01-19_trf6-analista-engenharia-mecanica_gabarito.pdf`, SHA-256 `0b5abca04a6892f48c7541018106445f6619f5f5863e061f631f0249899795e3`.

## CR35

**Chave documental C, estudo crítico sem nota.** Adiabático e fechado dão `Q=0` e `ΔU+ΔEc+ΔEp=−W`; para concluir `ΔU=−W`, exige-se `ΔEc+ΔEp=0`, não necessariamente cada termo zero. Em elevação ideal sem alteração do estado interno nem velocidade, trabalho recebido satisfaz `−W=ΔEp>0`, mas `ΔU=0`; é contramodelo, não dado original. Zero é valor ideal das hipóteses, não resultado medido. Sem valores de trabalho, massa ou altura, cálculo numérico e tolerância são N/A. Fonte [MIT balanço](https://web.mit.edu/16.unified/www/SPRING/thermodynamics/notes/node14.html), base `#base-primeira-lei`.

Artigo SHA-256 `62dea14902c59a5cfb2927125583531b5d1f6e5ccd43c796765d774171bfaafa`; família `trf`, item original 54, prova p. 1, chave p. 1, letra C. Prova `downloads/termodinamica/provas/2025-01-19_trf6-analista-engenharia-mecanica_prova.pdf`, SHA-256 `74a764fdb11ca13d527674c39206f44cbd4b5b1392cdee1f8bce9d8016ac4d79`; chave `downloads/termodinamica/gabaritos/2025-01-19_trf6-analista-engenharia-mecanica_gabarito.pdf`, SHA-256 `0b5abca04a6892f48c7541018106445f6619f5f5863e061f631f0249899795e3`.

## CR36

**E.** Adiabático implica `Q=0`, não `W=0`; expansão reversível de gás com pistão isolado pode produzir `W>0`, e com ΔEc=ΔEp=0 e sem outros trabalhos resulta `ΔU=−W<0`. Para gás ideal de composição fixa e capacidades constantes, a hipótese adicional de processo simples reversível dá `pV^k=constante`, `k=c_p/c_v`; `k` é adimensional. Os zeros e sinais são consequências exatas do modelo. Nenhum estado numérico ou magnitude é fornecido: sem tolerância numérica de cálculo. Fonte [MIT, adiabática](https://web.mit.edu/16.unified/www/SPRING/thermodynamics/notes/node17.html), bases `#base-trabalho-fronteira`, `#base-entropia`, `#base-balanco-fechado`.

Artigo SHA-256 `bcef62876e9bdf18b1a5a82bab92e3522b3afb08a57d62ff7690ba6567c0a69e`; família `tse`, item original 58, prova p. 1, chave p. 1, letra E. Prova `downloads/termodinamica/provas/2024-12-08_justica-eleitoral-tse-cpnuje-engenharia-mecanica_prova.pdf`, SHA-256 `fae9b7159587bd52cfe63f1bffce4894bdd4b3419ae449740c70ff0b021c5ce6`; chave `downloads/termodinamica/gabaritos/2024-12-08_justica-eleitoral-tse-cpnuje-engenharia-mecanica_gabarito.pdf`, SHA-256 `ab2116cb79da87ca206b7156c345d493d87032ee1f2fb8514137ced96e437baf`.

## CR37

**E.** Gouy–Stodola `W_perdido=T₀ S_ger`: K × J/K = J, com ambiente de referência a temperatura absoluta constante e comparação de trabalho útil com referência reversível adequada, mesmos estados e restrições. `S_ger≥0`, portanto a destruição de exergia é não negativa. Sem temperatura, entropia ou escala vertical numérica, não se calcula trabalho nem tolerância. A figura examinada mostra ângulos de manivela, incluindo 560, 600, 640, 680, 0, 40, 80, 120 e 160 graus; são marcações do eixo, não valores de trabalho ou insumos da solução. Figura `assets/questoes-reais-e1/figura-222735fab01e.png` SHA-256 `222735fab01e54a81e34f3bb54cfd7097a8cbc1391ebe6420d60df8b2513a9cb`. Fonte [MIT Gouy–Stodola](https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node49.html); base `#base-exergia`.

Artigo SHA-256 `e3a49cb2403795ae867f5cd76694cc11c71f3ff7c24f31727407420bdcc5fe73`; família `p22m`, item original 54, prova p. 1, chave p. 1, letra E. Prova `downloads/termodinamica/provas/2022-02-20_petrobras-engenharia-de-equipamentos-mecanica_prova.pdf`, SHA-256 `900b6b5a1cf6b3d66d676ef43de2b6f043b83da4c5367717b6ce17a268c7c9ab`; chave `downloads/termodinamica/gabaritos/2022-02-20_petrobras-engenharia-de-equipamentos-mecanica_gabarito.pdf`, SHA-256 `8fdab842bcc3d8123e4b110c3e2f42b9a747239620f7dc15f802a32a05bf6ee0`.

## CR38

**C.** Máquina térmica entre reservatórios a temperaturas constantes e absolutas `T_h>T_c>0`: `η_C=1−T_c/T_h`, adimensional. O 1 é exato; sem temperaturas numéricas não há eficiência numérica ou tolerância de arredondamento a verificar. Nenhuma máquina entre as mesmas fontes supera esse limite e outras máquinas reversíveis também o atingem; não é exclusividade de construção de Carnot. Base `#base-limite-carnot`.

Artigo SHA-256 `5233e8a9930268d3f0da527f4d83e641ffa6d2a760fd04e0a61eeb1883e82402`; família `p22m`, item original 55, prova p. 1, chave p. 1, letra C. Prova `downloads/termodinamica/provas/2022-02-20_petrobras-engenharia-de-equipamentos-mecanica_prova.pdf`, SHA-256 `900b6b5a1cf6b3d66d676ef43de2b6f043b83da4c5367717b6ce17a268c7c9ab`; chave `downloads/termodinamica/gabaritos/2022-02-20_petrobras-engenharia-de-equipamentos-mecanica_gabarito.pdf`, SHA-256 `8fdab842bcc3d8123e4b110c3e2f42b9a747239620f7dc15f802a32a05bf6ee0`.

## CR39

**Chave documental C, estudo crítico sem nota.** Conversão fornecida pela questão: `350 cal × 4,2 J/cal = 1470 J`; quociente nominal `η=1470/1470=1` ou 100%. Aritmética exata com os números declarados; o fator 4,2 é o dado do exercício, sem supor incerteza experimental ou extrapolar precisão metrológica. No modelo de máquina térmica cíclica, 350 cal são toda a entrada térmica de uma única fonte, 1470 J o trabalho líquido total e não existem outras trocas ou efeitos: `Q_rejeitado=0`, o que contraria Kelvin–Planck. Com energia química e fluxos de massa de motor real, as duas grandezas isoladas não definem esse balanço. A letra oficial é referência documental, não justificativa técnica da banca ou afirmação de anulação. Fonte [OpenStax §4.4](https://openstax.org/books/university-physics-volume-2/pages/4-4-statements-of-the-second-law-of-thermodynamics), bases `#base-segunda-lei`, `#base-balanco-fechado`.

Artigo SHA-256 `f91445144bcaca237b211f17563fcb1c4524da45c0e007944ea1038301bc8c54`; família `p22p`, item original 66, prova p. 1, chave p. 1, letra C. Prova `downloads/termodinamica/provas/2022-02-20_petrobras-engenharia-de-processamento_prova.pdf`, SHA-256 `1219213183d7a5ae1454ab297e7182d4eedf2d1f32847d0c1cfc0831ed70cbd3`; chave `downloads/termodinamica/gabaritos/2022-02-20_petrobras-engenharia-de-processamento_gabarito.pdf`, SHA-256 `62fd95ad9eb441180cbf28fbc6704a0b19c1609b034a550a184d789b270688d8`.

## CR40

**C.** Para substância simples compressível de composição fixa em estados de equilíbrio, `dh=T ds+v dp`, e em transformação isentrópica `ds=0`: `dh=v dp`. A pressão cresce e `v>0`, logo `Δh=∫ₚ₁ᵖ₂v dp>0`. Em unidades SI `v dp=(m³/kg)(Pa)=J/kg`; não se assume volume constante. Zero é condição simbólica, e nenhuma pressão, temperatura ou resultado numérico é fornecido: tolerância de cálculo é N/A. Base `#base-gibbs`.

Artigo SHA-256 `afc6cc711c91366246bbc7f1d20b52e217ec4bda325a90e34a346ae7a2afa909`; família `p22p`, item original 67, prova p. 1, chave p. 1, letra C. Prova `downloads/termodinamica/provas/2022-02-20_petrobras-engenharia-de-processamento_prova.pdf`, SHA-256 `1219213183d7a5ae1454ab297e7182d4eedf2d1f32847d0c1cfc0831ed70cbd3`; chave `downloads/termodinamica/gabaritos/2022-02-20_petrobras-engenharia-de-processamento_gabarito.pdf`, SHA-256 `62fd95ad9eb441180cbf28fbc6704a0b19c1609b034a550a184d789b270688d8`.


Limites: este exame cobre somente CR31–CR40 e não substitui a revisão do Auditor responsável. A identidade dos arquivos não demonstra por si correção científica ou literalidade; a conferência visual documental anterior é atribuída a FON-01. Não são alegados teste com estudantes, certificação externa, incerteza de instrumentos ou aceite global.
