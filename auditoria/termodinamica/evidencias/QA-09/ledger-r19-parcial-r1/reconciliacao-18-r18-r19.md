# QA-09 — revalidação individual de 18 objetos r18 na r19

30/10/2026. Responsável `/root/planning`; **integração aguarda auditor independente**. Reexaminei na r19 os 18 objetos EX001–005, D26–28 e D11–20, seus enunciados, contas, hipóteses e bases, no alcance dos pareceres e relatórios históricos. Em cópia temporária com snapshots r18 executei o gerador do ledger r18 e conferi os 18 objetos e 23 contextos; li seu parecer independente e limites. Reextraí cada objeto por seção, tipo, posição UTF-16 e hash e confrontei os 23 contêineres ligados. Identidade de bytes é evidência de localização, não aceite científico automático dos contêineres ou descendentes.

## Efeito das alterações

As quatro alterações r17→r18 (primeira lei, entropia de escoamento, EX027 e ficha60) foram tratadas individualmente na reconciliação r18 e no parecer independente que a examinou; seus efeitos sobre os modelos e hipóteses destes 18 objetos foram novamente considerados. Em particular, o exemplo EX027 de máquina térmica é distinto do diagnóstico D27 do misturador; balanços de primeira lei de D17/D26 mantêm sua convenção e hipóteses; nenhum deles usa a ficha60 como dado.

A aplicação r18→r19 contém **três** deltas: notação na base de propriedades e fichas 61/80. Li o parecer independente de aplicação r19: os pares V/v, U/u e H/h ficam delimitados a totais e valores específicos por massa, sem generalizar a caixa das letras; isso é compatível com a densidade de EX001 e não altera seus dados ou resultados. As fichas 61/80 explicitam, respectivamente, o domínio motor do limite de Carnot e o calor total externo/trabalhos no rendimento; nenhum dos 18 blocos tem esses cartões como fonte de dados, inclusive D12, cujo balanço de potências vem da própria base `#base-brayton-real`. As contas e interpretações destes objetos mantêm-se no domínio explicitado. Não se declara aprovação de outras ocorrências das bases ou das fichas por esta ponte.

| Objeto | Resultado e condição verificada na r18 |
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

Fontes NIST, DOE, EPA, MIT e OpenStax e seus limites permanecem rastreados nos relatórios científicos anteriores; não reclassifico referências por essa ponte. Os dados são nominais, não medições. Os demais objetos, pais, descendentes, fontes e recursos permanecem pendentes de integração; nenhum aceite decorre automaticamente da identidade do hash. Não houve navegador real, estudantes, revisão humana ou certificação externa. QA-09 permanece em correção.
