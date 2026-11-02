# QA-09 — auditoria independente dos exemplos 006–020 r25

30/10/2026. Auditor `/root/planning`, distinto do Corretor `/root/next_examples`. **Veredito do lote: AJUSTE OBRIGATÓRIO em EX-010 e sua base de equipamentos.** Os outros 14 exemplos foram conferidos apenas nos modelos e limites abaixo; não foram integrados automaticamente ao ledger, e QA-09 permanece aberto.

## EX-010 e tabela: fronteira, correntes e trabalho

Na r25, o exemplo informa vapor que entra a h₁=3000 e sai a h₂=2600 kJ/kg, vazão 2 kg/s, turbina adiabática e variações de velocidade e altura desprezíveis; conclui 400 kJ/kg e 800 kW. Esses resultados são corretos no modelo estacionário com **uma entrada e uma saída como únicas correntes**, mesma vazão e trabalho total não associado ao escoamento produzido na fronteira. O exemplo e a linha da tabela de turbina descrevem entrada/saída no singular, mas não explicitam exclusividade de correntes nem a natureza total do trabalho. A tabela também emprega relações simplificadas para compressor, válvula e bomba; suas condições de fronteira e, conforme o caso, a ausência ou contagem total dos trabalhos não associados ao escoamento precisam ser explicitadas nas respectivas linhas, sem generalizar indevidamente para quaisquer equipamentos. O resumo com uma entrada e saída aparece em outro bloco e não fixa, no enunciado local, que todos os demais fluxos inexistem.

Contramodelo algébrico com duas saídas: entrada 2 kg/s a h₁=3000, saída 1 kg/s a h₂=2600 e outra 1 kg/s a h₃=2000 kJ/kg; adiabático, permanente e energias macroscópicas desprezíveis. A conservação de energia dá Ẇ=2×3000−1×2600−1×2000=1400 kW, ou 700 kJ/kg de entrada, não 800 kW. Para mostrar que não é apenas uma violação da segunda lei, um **gás ideal sintético**, cp=1 e R=0,287 kJ/(kg·K), com h=cpT, T₁/T₂/T₃=3000/2600/2000 K e p₁/p₂/p₃=100/1/1 kPa, dá diferenças de entropia aproximadas 1,1786 e 0,9162 kJ/(kg·K), respectivamente, e Ṡger≈2,0948 kW/K>0 para as vazões indicadas. É construção matemática didática, não dados reais de vapor d’água nem demonstração de uma turbina comercial.

Solicito candidata que declare, no EX-010 e na linha de turbina, regime permanente, uma única entrada e uma única saída, trabalho total não associado ao escoamento por massa e preservação das hipóteses adiabática e de energias cinética/potencial; explicitar a potência total no exemplo. Avaliar e corrigir proporcionalmente as linhas de compressor, válvula e bomba que usam as relações restritas, bem como bocal e trocador na medida em que suas próprias relações exijam exclusividade. Uma revisão da tabela e da aplicação efetiva deve respeitar escopos e fontes; o problema não é a conta aritmética no modelo suficiente.

## Demais exemplos

- **006:** gás ideal de massa e composição fixas, p/T absolutas: 1,5×1,2=1,8 e aumento 80%, não 180%.
- **007:** modelo de umidade ideal à mesma T, mesma fase de referência e fator de intensificação desprezado: 0,60/0,80=0,75, queda 25% da pressão parcial e 20 pontos percentuais de umidade relativa.
- **008:** fases puras, T e p fixas, potenciais compatíveis e persistência das fases: (7−5)×0,02=0,04 kJ=40 J no sentido líquido→vapor, desfavorecido. Para tratar transferência finita como igualdade exata, os potenciais e as fases devem persistir; os valores são didáticos.
- **009:** para gás ideal de composição fixa e cp(T)=0,90+0,0002T, integração de 300 a 500 K dá 180+16=196 kJ/kg; cp inicial daria 192, e ponto médio é exato para essa função linear.
- **011:** tanque fechado rígido, único trabalho de eixo e variações cinética/potencial desprezíveis: ΔU=−40−(−250)=210 kJ.
- **012:** fator adotado 4,2 J/cal dá Q=420 J, ΔU=300 J e U₂=350 J; 4,184 J/cal levaria a 348,4 J, uma convenção diferente.
- **013:** trabalho de fronteira único 200×(−0,020)=−4 kJ e ΔU=−7−(−4)=−3 kJ. No exemplo separado do tanque rígido, ΔT=35/(1×0,70)=50 K.
- **014:** gás ideal de massa fixa e estados com pV=300 kPa·m³ têm ΔU=0; caminhos quase estáticos dão 300×2=600 e 100×2=200 kJ de trabalho. O gráfico é dependência; não foi auditado como objeto visual neste recorte.
- **015:** expansão livre de gás ideal em volume rígido isolado, mesma T inicial/final, m=1 kg e R=0,287: ΔS=0,287 ln 2≈0,198933 kJ/K, arredondado 0,199; Sger=ΔS. A trajetória real não é reversível.
- **016:** no modelo sensível de água na mesma fase, Q=2×4,2×30=252 kJ; potência útil 0,8×2=1,6 kJ/s, tempo 157,5 s.
- **017:** mistura isolada do mesmo líquido, c constante e recipiente desprezível, no modelo sensível da base atual: (1×20+3×60)/4=50 °C.
- **018:** capacidades 4, 4 e 2 kJ/K e temperaturas iniciais 80, 20 e 20 °C, saldo externo Eext=0: (320+80+40)/10=44 °C. A soma externa nula não exige que cada interação individual seja nula; o recipiente participa uma vez.
- **019:** água fornece 0,5×4,2×20=42 kJ. Para 0,10 kg de gelo são necessários 33,4 kJ e Tf=8,6/(0,60×4,2)≈3,41 °C; para 0,30 kg fundem 42/334≈0,126 kg e restam fases a 0 °C, sob hipóteses de pressão e equilíbrio declaradas.
- **020:** tanque inicialmente vazio, rígido, adiabático e sem trabalho, uma entrada de entalpia constante, parede e variações cinética/potencial desprezíveis, cp/cv constante: u₂=hin e T₂=1,4×300=420 K. O enchimento acumula massa; não é escoamento permanente no tanque.

As bases de mistura e mudança de fase efetivas foram lidas, inclusive os limites de energia sensível, energia de mistura, trabalho de fronteira e Qfase=ΔH. Os valores são nominais; arredondamentos não representam incerteza experimental.

## Identidade, fontes e limites

Aula r25 SHA `ea0a7e3877c0a0250dac3d9c993c7922a03400929eb7a5dad39fcb27e3263c7e`; inventário `6798d317db30bd69435ed14862cc03cd0f0c6313e40408dd8831052285984116`; entrega `05418aff6d82688aaf96ad2ba4698ca2f52f59e7e393a9e156b594d92a55cc56`. Executei o verificador do Corretor e comparei sua saída à evidência. Meu verificador somente leitura `auditoria/termodinamica/evidencias/QA-09/auditoria-exemplos-006-020-r25-independente-r1/verificar.py`, SHA `08c5c9a5d1e177345df896af91cee9417b000a7fa05fd37ca8f68596780734ac`, reextrai os 15 recortes e contextos do inventário e recalcula valores e contramodelo. Scripts de identidade e aritmética não julgam hipóteses ou imagens por si.

Consultei [MIT, balanço de escoamento](https://ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_6.htm), [MIT, potencial químico](https://ocw.mit.edu/courses/5-60-thermodynamics-kinetics-spring-2008/b312114e4e885b69b5746dcad660cc4f_lec_18.pdf), [ASHRAE, psicrometria ideal](https://handbook.ashrae.org/Handbooks/F21/SI/F21_Ch01/F21_Ch01_si.aspx), [OpenStax, calorimetria](https://openstax.org/books/chemistry-2e/pages/5-2-calorimetry), [OpenStax, mudança de fase](https://openstax.org/books/physics/pages/11-3-phase-change-and-latent-heat), [MIT, tanque evacuado](https://web.mit.edu/16.unified/OldFiles/www/FALL/thermodynamics/notes/node17.html) e [NIST, calorias](https://www.nist.gov/pml/special-publication-811/nist-guide-si-footnotes) no alcance dos modelos; nenhuma é fonte dos dados fictícios. Não houve teste em navegador, leitor de tela, estudantes, revisão humana ou certificação externa. Outros nós, fontes, figuras e QA-09 integral continuam pendentes.
