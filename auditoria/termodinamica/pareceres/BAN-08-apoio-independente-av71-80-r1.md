# BAN-08 — apoio independente AV71–AV80

Data 29/10/2026; revisor: agente automatizado `/root/auditoria_av61_70`. Escopo parcial; não aprova BAN-08 nem libera próximo ID. Produto e controle preservados.

HTML `modulos/e1-termodinamica.html`, SHA-256 `80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0`. Os hashes dos itens correspondem ao trecho `<article>...</article>` recodificado em UTF-8. Identidade não substitui análise científica. São itens autorais, não transcrição oficial.

## AV71

**C.** Ventilador e bomba impulsionam escoamentos, caracterizando convecção forçada. A condução exclusivamente sólida não descreve os fluidos; B radiação exclusivamente omite escoamento; C correta; D exclusivamente natural ignora acionamento; E não há impedimento necessário à troca de calor. Dois equipamentos/fluídos são contagens exatas; não se fornecem temperatura, vazão ou fluxo térmico para calcular ou tolerar numericamente. Base `#base-transferencia`; [OpenStax mecanismos](https://openstax.org/books/university-physics-volume-2/pages/1-6-mechanisms-of-heat-transfer).

Artigo SHA-256 `a6822e633557838619c8a4c9fa1790c583776ef03830b6ca475f28ad6b25e2ff`.

## AV72

**B.** No escoamento paralelo as correntes entram pela mesma extremidade e seguem mesmo sentido; no contracorrente entram por extremidades opostas. A inverte; B correta; C ignora efeitos de orientação no perfil térmico; D iguala ambos a entradas opostas; E iguala ambos à mesma extremidade. Duas correntes são contagem exata; não há temperaturas, áreas ou valores de transferência a calcular, nem tolerância. Base `#base-trocadores`.

Artigo SHA-256 `9b34292c52fddf0bbfff7573258e810e24f0d3ad6cc86dc0c1eaed9743754e7d`.

## AV73

**A.** Compactação se associa a elevada área de troca por volume `A/V`, dimensão m⁻¹, e aletas podem aumentar área. B baixa razão contradiz finalidade; C armazenamento não define compactação; D, para material/área fixos em parede plana, `R_cond=L/(kA)` cresce com espessura, não necessariamente melhora condução; E nega função térmica das aletas. A correta; mais área por si não garante desempenho ilimitado ou queda de pressão fixa. Sem área, volume, k ou L numéricos, tolerância numérica N/A. Base `#base-trocadores`; [OpenStax condução](https://openstax.org/books/university-physics-volume-2/pages/1-6-mechanisms-of-heat-transfer).

Artigo SHA-256 `0726d64bef732bb8b75a4473a190e14e7b7359155533af25fd5fc6b6c5f0b34a`.

## AV74

**B.** Com área `10 m²` e diferença média `20 K` mantidas, `Q̇=UAΔT_m`: antes `500×10×20=100000 W=100 kW`; depois `250×10×20=50000 W=50 kW`. A 10→5 kW erra por fator 10; B 100→50 correta; C 100→200 pressupõe aumento; D 100→100 ignora queda em U; E 500→250 repete coeficientes como potência, sem unidades compatíveis. Queda de 50% resulta de U dividido por 2 sob os parâmetros fixados. Operações e conversão `1000 W=1 kW` são exatas para dados nominais; sem incerteza experimental declarada. Bases `#base-trocadores`, `#base-leitura-matematica`.

Artigo SHA-256 `e1cbd2e738cff1e20744251bba5ae94651ec5502fd9dc5808c1627f19b37b032`.

## AV75

**B.** Lei de Fourier com `k=10 W/(m K)` e `dT/dx=−20 K/m`: `q″_x=−10×(−20)=+200 W/m²`. A +200 W tem dimensão de potência, exigiria área; B +200 W/m² correta; C zero ignora gradiente; D −200 omite sinal da lei; E +2 resulta de dividir 20 por 10, além de não respeitar as dimensões da operação. Condutividade positiva e gradiente negativos dão fluxo no sentido +x; valores nominais exatos, sem incerteza de medição. Base `#base-transferencia`; [OpenStax Fourier](https://openstax.org/books/university-physics-volume-2/pages/1-6-mechanisms-of-heat-transfer).

Artigo SHA-256 `cf84420539a50440af16625535da0e7513c3d3de6362be04a830790f9eb9029c`.

## AV76

**C.** I verdadeira, advecção é transporte devido ao movimento global do fluido; II verdadeira, convecção combina movimento e difusão; III falsa, condutividade comum é positiva e Fourier determina sentido por `−k∇T`. A V-F-V, B F-V-V, D F-F-V e E V-V-V divergem; C V-V-F correta. Três afirmações e cinco opções são contagens exatas; sem temperaturas, condutividade ou fluxo numérico, tolerância N/A. Base `#base-transferencia`.

Artigo SHA-256 `1c62973843285a448a379f2b090961af88e38192c7728fb8d628fe4f7a4b48cb`.

## AV77

**C.** Em regime permanente, sem outras trocas ou perdas, `Q̇_H=Q̇_L+Ẇ=12+3=15 kW`. A 3 ignora retirada da sala; B `12−3=9` subtrai potência de entrada; C 15 correta; D 12 omite potência; E `12/3=4` é COP adimensional de refrigeração, não `4 kW` de calor rejeitado. Dados e operações são exatos no modelo nominal, sem incerteza experimental ou arredondamento informado. Bases `#base-refrigeracao`, `#base-eficiencia-cop`; [MIT primeira lei](https://web.mit.edu/16.unified/www/SPRING/thermodynamics/notes/node14.html).

Artigo SHA-256 `ba4e9d281b7c90b87fa9f88e4d953020a002c8903045cd2fcc0e0e55430b2820`.

## AV78

**A.** Calor latente elevado favorece calor absorvido por unidade de massa vaporizada nas condições de comparação; desempenho do ciclo depende também de estados e equipamento. B 100% não é garantido pela propriedade; C destinação ao esgoto não decorre do calor latente; D nega absorção na vaporização; E omite controle de vazamentos. O 100% é afirmação universal do distrator, não eficiência calculada; não há propriedades numéricas da amônia, carga ou massa para verificar quantitativamente nem tolerância. Base `#base-calor-latente`.

Artigo SHA-256 `eb02ebe932d364e4cd46353e409c2c75a53ec06000a2f3d95929a1289b2af8e4`.

## AV79

**E.** Com efeito do gás residual desprezível, radiação entre superfícies e condução por suportes e cabos permanecem mecanismos a considerar. A convecção intensa contradiz a hipótese; B vácuo não impede toda transferência; C desconsidera condução sólida; D nega propagação de radiação em vácuo; E correta. A existência de caminhos não garante taxa não nula sem diferença de temperatura e condições apropriadas. **N/A numérico:** faltam temperaturas, geometria e propriedades para taxa ou tolerância. Base `#base-radiacao-vacuo`; [OpenStax radiação](https://openstax.org/books/university-physics-volume-2/pages/1-6-mechanisms-of-heat-transfer).

Artigo SHA-256 `e1bcf99fdeeb7c91da73b8c89d96714294fd1c64234861d3ae7fb0b91cf78bcc`.

## AV80

**E.** Em regime permanente, geração uniforme e cinco faces isoladas: `V=2×2×1=4 m³`; geração `150 W/m³×4 m³=600 W`; face ABCD `A=2×2=4 m²`; `600 W=10 W/(m² K)×4 m²×(T_s−25 °C)`, logo `ΔT=15 K=15 °C de intervalo`, `T_s=25+15=40 °C`. A 25 °C ignoraria geração positiva; B 85 °C surge ao adotar incorretamente `1 m²`, `25+600/(10×1)=85`; C 28,75 °C surge de `A_total=2(2×2+2×1+2×1)=16 m²`, `25+600/(10×16)=28,75`, incluindo indevidamente faces isoladas; D 15 °C confunde intervalo e valor de temperatura; E 40 °C correta. A figura examinada identifica AD=2 m, DC=2 m e DH=1 m: `assets/questoes-reais-e1/figura-9d73adf962aa.png`, SHA-256 `9d73adf962aaabecba761c823d3faca4bb4dd463a7009033e7267242bce84cb2`. Operações nominais são exatas no modelo sem radiação e face uniforme; incertezas ou tolerâncias instrumentais não são fornecidas. Bases `#base-geracao-face`, `#base-transferencia`; [OpenStax convecção](https://openstax.org/books/university-physics-volume-2/pages/1-6-mechanisms-of-heat-transfer).

Artigo SHA-256 `9586c1757d18d3ba88d59485b308d8e6c92a4dd5859ffe94ff3cd7e3e9ac9a71`.

## Fontes de auditoria e limites

- `auditoria/termodinamica/PROTOCOLO_AAA.md` — SHA-256 `18f1f299556e8e60c926a1921987f6d2c10cc939aa4aef4487117dc66c344afc`
- `auditoria/termodinamica/evidencias/BAN-08/inventario-numerico-197-r1.json` — SHA-256 `5b56e8280d35d590bf11ddbff9b0e789faed257fafe1cad9c4854cc5ac5fd99f`
- `auditoria/termodinamica/pareceres/BAN-07-r3.md` — SHA-256 `009adc698bf2f88e28826b389a48e2526660efc9b7cc2ea3b598f0e06026d68b`

Cálculos e cinco alternativas de cada item examinados pelo revisor atual, com conhecimento prévio das respostas. BAN-07 é trabalho anterior atribuído; identidade não substitui revisão científica atual. Fontes MIT e OpenStax consultadas em 29/10/2026. Sem ensaio com estudantes, certificação externa, incerteza de instrumentos inferida ou aprovação global BAN-08.
