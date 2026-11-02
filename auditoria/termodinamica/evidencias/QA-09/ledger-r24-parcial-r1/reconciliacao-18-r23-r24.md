# QA-09 — revalidação individual de 18 objetos r23 na r24

30/10/2026. Responsável `/root/planning`; **integração pendente de Auditor independente**. Reli os 18 objetos EX001–005, D26–28 e D11–20, suas hipóteses, resultados e bases na r24, no alcance dos pareceres históricos. Em cópia temporária dos snapshots r23 reproduzi o ledger r23 e consultei o parecer independente. Reextraí cada recorte por documento, seção, tipo, posição UTF-16 e hash; os 23 contêineres associados foram confrontados e nenhum mudou. Identidade do recorte ou base auxilia localização, mas não aprova automaticamente pais, filhos ou fontes.

## Efeito da preparação FUN-01

Li a seção `#fun01-preparacao-equilibrio` efetiva e seu parecer de aplicação r24. As seis alterações no mesmo contêiner delimitam potencial químico em mistura de gases ideais com estado padrão e pressões positivas, líquido puro incompressível em equilíbrio hidrostático, e distinção entre potencial químico intrínseco e potencial total que incorpora gravidade. Os 18 objetos não utilizam esse bloco como dado numérico ou destino direto; seus próprios modelos continuam válidos nas condições reexaminadas.

D11 trata equilíbrio de fases com transferência permitida: na interface local, com o mesmo potencial externo por espécie nos dois lados, a igualdade dos potenciais totais também significa igualdade dos potenciais intrínsecos, sem impor densidades iguais; se a comparação envolver alturas ou potenciais externos distintos, a contribuição correspondente deve ser incluída, como explicado na preparação. Isso não altera a pergunta qualitativa de D11 nem transforma seu modelo em regra para comparar alturas arbitrárias. EX005 usa pV=nRT com constante aproximada indicada, não a expressão de potencial de mistura. D26 e D27 seguem seus próprios balanços cíclico/de mistura, sem depender dos novos números da preparação; D28 é balanço de espécie, não critério de potencial químico. As bases de radiação, geração, mistura e fase e os demais contextos foram relidos nos limites dos pareceres anteriores; D14 mantém a entrada elétrica explícita e D17 a perda externa.

Revisitei a [aula MIT de mistura de gases ideais](https://ocw.mit.edu/courses/3-020-thermodynamics-of-materials-spring-2021/mit3_020s21_l13.pdf) e a [teoria de soluções MIT](https://ocw.mit.edu/courses/3-20-materials-at-equilibrium-sma-5111-fall-2003/764ba46faf34fb6f2439c6b52eb37fb9_mixtures.pdf), no alcance dos modelos, sem atribuir a elas os valores fictícios; as demais fontes estão nos pareceres históricos. Os 18 recálculos e limites são:

| Objeto | Resultado e condição verificada na r24 |
|---|---|
| EX001 | 9/0,010=4,5/0,005=900 kg/m³; amostra homogênea dividida na mesma condição. |
| EX002 | −10+120=110 °C; intervalo de 120 °C tem magnitude 120 K; span não é incerteza. |
| EX003 | 10+(30/40)(90−10)=70; interpolação afim na base, sem provar calibração real. |
| EX004 | (900−400)/(2400−400)=0,25; título mássico da mistura saturada em equilíbrio com entalpias de mesma referência, não fração de volume. |
| EX005 | 0,082×320/26,24=1 atm, na aproximação da constante e condições dadas. |
| D26 | 600+900−20=1480 kJ/kg; calor recebido 3200 kJ/kg, rendimento 46,25%, rejeição 1720 kJ/kg; a primeira lei não prova viabilidade pela segunda. |
| D27 | y=(700−300)/(2300−300)=0,20; (1−y)×10×250=2000 kW; mistura permanente adiabática, sem trabalho, energias cinética/potencial desprezíveis e referências compatíveis. |
| D28 | [0,20+500(0,0004−0,0006)]/200=0,0005 h⁻¹=500 ppm/h inicialmente; estacionário 800 ppm no modelo diluído e bem misturado, fluxos iguais, sem fontes extras. |
| D11 | Igualdade dos potenciais químicos dos componentes comuns em equilíbrio com transferência permitida, sem exigir densidades iguais; calor latente sozinho não garante COP ou segurança. |
| D12 | (140−50)/300=30%; volumes à sucção 6/8=75%; válvulas fechadas na compressão antes da descarga no modelo indicado. |
| D13 | U₂/U₁=0,7 implica queda de 30% da taxa com área e diferença média mantidas; contato sólido conduz em vácuo e radiação dispensa gás. |
| D14 | 60×2=120 W; 18+120/(6×2)=28 °C média da face, regime permanente, demais faces isoladas, h uniforme e radiação desprezada. |
| D15 | (12+24+36)/3=24 °C; capacidades iguais e constantes, isolamento e modelo sensível. |
| D16 | (2×90+6×30)/8=45 °C; capacidades constantes e interações extras desprezíveis. |
| D17 | (4×80+4×20+2×20−20)/10=42 °C; perda negativa, recipiente contabilizado uma vez, modelo sensível sem trabalho relevante. |
| D18 | 0,5×4,2×20=42 kJ < 0,2×334=66,8 kJ; fundem 42/334≈0,126 kg e restam 0,074 kg, coexistência a 0 °C sob o modelo. |
| D19 | 20×300 mL/min=0,36 m³/h; 0,36/0,0005=720 m³/h, regime estacionário, bem misturado, mesma referência volumétrica e ausência de fontes extras. |
| D20 | 36/3600=0,010 m³/s; ρgV̇H=1500 W, rendimento 50%; potência elétrica não é determinada sem dados do motor. |

Dados são nominais; arredondamentos não são incerteza experimental. Os demais registros, pais, descendentes, fontes, bases e recursos permanecem pendentes de integração; não há transferência de aceites por hash. Não houve navegador real, estudantes, revisão humana ou certificação externa. QA-09 permanece em correção.
