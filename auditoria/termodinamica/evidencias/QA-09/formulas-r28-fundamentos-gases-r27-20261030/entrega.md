# QA-09 — fórmulas de fundamentos, gases e fases, fotografia r27

30/10/2026. Corretor `/root/next_formulas`. **Aguardando Auditor independente.** Prefixo `formulas-r28` identifica este lote de trabalho; não indica que r28 seja a fotografia avaliada. As 22 fichas 01–22 já tiveram revisões em outras fotografias; esta é nova passagem ampla da r27, não alegação de conteúdo historicamente inédito nem aprovação global de QA-09. Produto e controles não alterados.

## Identidade e testes

Formulário r27 SHA `16329b7369c4ba927f5f7da30551f86934aad1f6a6e55627443dea5cb9fe0c02`, aula r27 `9af8e2c9ffe509e40594d086a9ef4ad75127fb4ca873efb305d3144e08f3fc49`, inventário r27 `a58d7f0b0a5f097eef83ad83026ef49e801457b87f7cf2b2345c3dd915597c7c`. `identidades.json` SHA `c094d3b759f1054931c32e09edb718f105ee73ad8990e15ede8cd11e91c8537a` registra por cartão número, ID, intervalo UTF-16, SHA e quantidade de MathML. Li textos, símbolos, sinais e as 58 fórmulas MathML no escopo. `verificar.mjs` SHA `638384848cdf7c4cd22c44071de5430e6add6db86ba42c8a08b6ea0e0de64c1c` é leitura apenas e executado por `node auditoria/termodinamica/evidencias/QA-09/formulas-r28-fundamentos-gases-r27-20261030/verificar.mjs`; `ok=true` para fotos, 22 cartões, 58 blocos MathML, existência de 24 âncoras e cálculos abaixo. Contagem de MathML e existência de âncoras não substituem sua interpretação, renderização ou adequação pedagógica. Dados abaixo são nominais ou sintéticos, não medições nem atribuição de números às fontes.

## Relações e verificações

| Fichas | Modelo, sinais e resultados |
|---|---|
| 01–02 | ΔX=X₂−X₁; 55−80=−25. Potência média Q/Δt e W/Δt requer duração positiva; 120 kJ/60 s=2 kW. Q=Q̇Δt é exato para taxa constante e também para a média temporal; condição anunciada é suficiente, não única. |
| 03–04 | Prefixo k=1000, 1 kPa·m³=1 kJ, 1 L=10⁻³ m³, 1 cm³=10⁻⁶ m³; cal termoquímica=4,184 J. 27 °C=300,15 K; intervalos em K e °C são iguais, mas razões em Carnot/gás usam temperatura absoluta. |
| 05–07 | pabs=pman+patm: −20+100=80 kPa; pressão média 200 N/0,01 m²=20 kPa. Para 2 kg e 0,0025 m³, ρ=800 kg/m³ e v=0,00125 m³/kg. Para U=200 e H=300 kJ, S=4 kJ/K e m=2 kg, u=100, h=150 e s=2 nas unidades específicas. São divisões de uma amostra não vazia e volume positivo, na mesma base/estado. |
| 08–10 | Span −50→150 kPa=200 kPa; duas escalas afins com pontos (0,32),(100,212) associam Y=122 a X=50, com intervalos não nulos. Aumento 80→100 é 25% em relação a 80; a redução assinada correspondente é −25%. |
| 11–12 | 1000 ppmv=0,001; 10 ocupantes a 0,02 m³/h por pessoa produzem 0,2 m³/h nas mesmas condições de referência, para taxa uniforme ou média apropriada. m=0,028 kg e M=0,028 kg/mol dão n=1 mol e R≈296,929 J/(kg K) usando Ru≈8,314; mol representa entidades especificadas e unidades devem ser coerentes. |
| 13–16 | Gás ideal de composição fixa e grandezas absolutas: pV=mRT=nRuT e pv=RT. m=1 kg, R=0,287 kJ/(kg K), T=300 K e V=0,861 m³ dão p=100 kPa; em segundo estado p=200 kPa, T=400 K, V=0,574 m³. Relações isocórica, isotérmica e isobárica são restrições alternativas. Para p=90 kPa e os outros dados, Z=0,9; Z=1 num estado não prova idealidade de todas as propriedades. |
| 17–20 | Mesmo gás ideal: cp−cv=R e k=cp/cv. cp=1,005, cv=0,718 dão k≈1,399721; com m=2 kg e ΔT=100 K, ΔU=143,6 kJ para capacidades constantes. Média translacional clássica por molécula 3kBT/2 a 300 K dá 6,2129205×10⁻²¹ J. Se cp(T)=0,8+0,001T kJ/(kg K), a integral 300→400 K dá Δh=115 kJ/kg; não se trata de energia molecular total nem c constante em qualquer faixa. |
| 21–22 | Substância pura, equilíbrio líquido–vapor subcrítico, massas de fases não negativas e soma positiva: com mg=1 e mf=3 kg, x=0,25. Para hf=500, hg=2500 kJ/kg, h=1000 kJ/kg; y=(1−x)yf+xyg para v,u,h,s na mesma saturação. Inversão exige yg≠yf e x entre 0 e 1; fora da região bifásica não se força título. |

## Refinamentos de domínio propostos para julgamento

O Auditor da r23 considerou as fórmulas corretas no modelo físico ordinário e recomendou tornar explícitos alguns denominadores; não classifico esses refinamentos como novos erros demonstrados. Para cartões autônomos, proponho acrescentar `Δt>0` na 02; `A>0` na 05; `m>0` e `V>0` na 06; `m>0` na 07. Para a 21, igualmente pode ser explicitado `mg,mf≥0` e `mg+mf>0`; na 12, `M>0`. As condições eliminam os casos matematicamente indefinidos sem mudar fórmulas ou resultados. As demais razões de gás pressupõem estados físicos de massa, pressão, volume e temperatura positivos; verificar com Auditor se o contexto ideal já exprime isso de forma suficiente, antes de transformar recomendações em candidatas. Nenhum desses textos foi aplicado ao produto.

## Fontes consultadas

[NIST, fatores de conversão e caloria termoquímica](https://www.nist.gov/pml/special-publication-811/nist-guide-si-appendix-b-conversion-factors/nist-guide-si-appendix-b9); [NASA, equação de estado do gás ideal](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/equation-of-state-ideal-gas-2/); [NASA, cp e cv](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/specific-heats-cp-and-cv-1/); [NIST/NBS, fator de compressibilidade](https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nbsir86-3057.pdf); [MIT, energia translacional](https://ocw.mit.edu/courses/5-60-thermodynamics-kinetics-spring-2008/a48f66f75209c904d98e034be688ebe2_BTNsoSNR5B0.pdf); [DOE, propriedades e título](https://www.energy.gov/sites/default/files/2026-04/DOE-HDBK-1012-92_VOL1.pdf). As fontes dão modelos/definições, não verificam estados fictícios ou aprendizagem.

Solicita-se Auditor distinto para a interpretação da árvore MathML, hipóteses e prioridades dos refinamentos, além de fotos e cálculos. Não houve navegador real, leitor de tela, alunos, revisão humana ou certificação externa; outras 78 fichas e contextos não são cobertos por este lote.
