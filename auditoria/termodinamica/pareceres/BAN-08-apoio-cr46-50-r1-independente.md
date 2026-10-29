# BAN-08 — apoio científico independente CR46–CR50

Data 29/10/2026; autora do exame e revisora: agente automatizado `/root/auditor_ban08_novo`. Parcial e sem cegamento, sem aprovação global de BAN-08 ou liberação do próximo ID. Produto e controle não alterados. Versão examinada dos artigos, dados e bases do curso: `modulos/e1-termodinamica.html` SHA-256 `80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0`; hashes por ID referem-se ao trecho bruto UTF-8 `<article>...</article>`. CR46 é múltipla escolha, CR47–CR50 C/E, todos pontuáveis. As fontes originais e gabaritos são vinculados no artigo e no inventário, não foram reconferidos integralmente nesta análise; a chave não é prova científica.

Fontes de modelo acessadas em 29/10/2026: OpenStax College Physics for AP Courses, §15.4, https://openstax.org/books/college-physics-ap-courses/pages/15-4-carnots-perfect-heat-engine-the-second-law-of-thermodynamics-restated (etapas de Carnot); DOE, https://www.energy.gov/cmei/fuels/gaseous-hydrogen-compression (comparação relativa de famílias de compressor); MIT OCW 16.050, parte 2A.7, https://ocw.mit.edu/courses/16-050-thermal-energy-fall-2002/75666f9248981634a704fdf257ef529a_07_part2a.pdf (comparação real/isentrópica) e MIT OCW 2.611, https://www.ocw.mit.edu/courses/2-611-marine-power-and-propulsion-fall-2006/a11f4477fb29b02e431a21ca283e81f3_19brayton_irrev.pdf (Brayton real e regeneração). Nenhuma propriedade numérica externa é necessária para estes itens.

## CR46 — E

Hash `6db3ea19084b8ebc1743aabcf601f31f82cf56a2d5998e386e7504860cfff1b2`; base `#base-carnot-prova`. Ciclo de Carnot tem duas etapas isotérmicas reversíveis de troca de calor e duas adiabáticas reversíveis de ligação; estas são também isentrópicas. Contagem exata 2+2=4. A, B, C e D não apresentam os dois pares; E os apresenta. Não há dado experimental ou resultado numérico a arredondar; tolerância não aplicável às classificações e contagem exata.

## CR47 — C

Hash `8dbbd53e0111efaef76009a38b5c1c9ed437c6f6ecc471c0939147f903ec0786`; base `#base-tipos-compressores`. Centrífugos são uma família adequada para alta vazão e razão de pressão moderada; alternativos tendem a adequar-se a razões elevadas e menores vazões. A chave C é orientação comparativa preliminar no contexto original, não uma regra que por pressão de descarga isolada possa selecionar uma máquina ou provar superioridade universal: pressão de sucção, composição, vazão na referência e curvas são essenciais. Não há limiar nem dados para cálculo; tolerância numérica não aplicável.

## CR48 — C

Hash `d39d25c7b5b9bafac081c3c1f00b129a54f07fceea77f5354bb4632dfd439fd6`; bases `#base-brayton`, `#base-trocadores`. Regenerador pode transferir calor da exaustão para ar comprimido, preservando separação das correntes; fluxo em contracorrente é opção, desde que o perfil local de temperaturas permita fluxo da corrente quente à fria. T_exaustão,entrada>T_ar,entrada é condição de pré-aquecimento, sem assegurar potência ou efetividade arbitrárias. O enunciado afirma possibilidade, não que toda combinação de estados funcione. C compatível. Não há temperaturas, áreas, capacidades ou resultados numéricos no artigo; tolerância não aplicável à comparação qualitativa de temperatura.

## CR49 — E

Hash `8f8f133eddab5ab062c9f3a35ff78b246fa6ccd357de225593890f15c910cf9f`; base `#base-brayton-real`. No Brayton ideal simples, adição e rejeição de calor são idealizadas isobáricas; em trechos reais passivos com perdas, pressões de escoamento tipicamente diminuem. A rejeição térmica não implica elevação de pressão como regra, então a afirmação composta é falsa no modelo da base e a chave E é coerente. Não há números nem relação quantitativa que permita calcular queda; tolerância numérica não aplicável. A análise não afirma que pressão só pode cair em todo dispositivo imaginável.

## CR50 — E

Hash `b0e25a75cd24dfa1ded90bae33f09ee36222fd5d305d00607be61e818d126d3f`; bases `#base-isentropica`, `#base-brayton-real`. Regime permanente, adiabático, uma entrada/saída, ΔEC e ΔEP desprezíveis, mesmo fluido, entrada e pressão de saída para comparação de cada equipamento. Para compressor, η_c=(h2s−h1)/(h2r−h1)≤1 e portanto w_c,r≥w_c,s>0. Para turbina, η_t=(h3−h4r)/(h3−h4s)≤1 e w_t,r≤w_t,s, com ambos positivos. Ao comparar o conjunto com mesma vazão e condições declaradas, w_c,r/w_t,r≥w_c,s/w_t,s e w_líq,r=w_t,r−w_c,r≤w_t,s−w_c,s; igualdade é caso ideal e irreversibilidades efetivas tornam as comparações estritas quando presentes. Não se impõem saídas reais iguais às isentrópicas. O item diz que compressor consome menos proporção da potência da turbina; nesse modelo é E. Não há entalpias nem vazões para avaliar uma razão numérica; tolerância não aplicável às desigualdades simbólicas.

Nenhuma divergência numérica localizada; este apoio não substitui auditoria integral, teste com estudantes ou certificação externa.
