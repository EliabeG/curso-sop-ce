# QA-09 — revalidação individual de 18 objetos r21 na r22

30/10/2026. Responsável `/root/planning`; **integração pendente de auditor independente**. Reli na r22 os 18 objetos EX001–005, D26–28 e D11–20 e seus modelos, contas e vínculos no alcance dos relatórios históricos. Reproduzi o ledger r21 em cópia temporária dos snapshots e li seu parecer independente. No inventário r22 localizei e reextraí cada recorte individualmente; 17 são idênticos à r21 e D14 foi substituído pela candidata específica. Dos 23 contextos, 21 são idênticos e `#base-radiacao-vacuo`/`#base-geracao-face` mudaram. Igualdade de hash, índices e contextos é apoio de identidade, não aceite automático dos conteúdos, pais, filhos ou fontes.

## Avaliação das alterações e efeitos

A aplicação r22 e seu parecer independente identificam três deltas: radiação, geração e D14. Examinei novamente o contexto de D13, cujo bloco permanece igual mas depende de `#base-radiacao-vacuo`: a exigência de taxa líquida inicial não nula e superfície mais quente para a razão de perdas não altera as afirmações de D13, de que condução por contatos pode ocorrer no vácuo e radiação não exige gás; a queda de U para 0,7U com A e diferença média fixas ainda implica queda de taxa de 30%. Não se afirma que radiação líquida ou razão de duas taxas exista nas mesmas condições em todos os casos.

D14 é **novo fragmento r22**, não transferência de aceitação do fragmento antigo: confrontei o enunciado e resposta atuais com a candidata e o parecer da aplicação. Volume 2 m³, área exposta 2 m², q‴=60 W/m³ e entrada elétrica de 120 W integralmente convertida, h=6 W/(m²·K), exterior a 18 °C, bloco fechado e regime permanente de energia total, sem outras interações. A geração térmica total é 120 W, a convecção é a única saída térmica; face média 18+120/(6×2)=28 °C. Com Q̇=−120 W e Ẇ=−120 W, Q̇−Ẇ=0; a conversão q‴V e a alimentação elétrica são a mesma energia e não somadas duas vezes. A alteração em `#base-geracao-face` esclarece a fonte energética e o mesmo balanço, sem exigir temperatura uniforme no interior. Ela não torna a alimentação de D14 igual à de EX046, de 1200 W; são casos distintos.

A base de mistura/fase e os demais contextos não foram alterados nesta aplicação, mas reli os alcances de D15–18: D17 tem perda declarada, logo usa ΣCiΔT=−20 kJ em vez da fórmula isolada; D18 usa calor latente do modelo de fases puras em equilíbrio. A seguir, resultados e hipóteses de cada objeto, sem aceitar seus contextos como registros separados:

| Objeto | Resultado e condição verificada na r22 |
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

Conferi novamente as fontes primárias de modelo: [MIT, primeira lei](https://ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_4.htm) e [MIT, transferência de calor](https://ocw.mit.edu/courses/2-051-introduction-to-heat-transfer-fall-2015/2013cba86d06ea09582d9e4d7558f514_MIT2_051F15_EqnSheet_Q1.pdf); NIST, DOE, EPA, MIT e OpenStax dos demais objetos permanecem rastreados nos pareceres anteriores. As fontes fundamentam modelos, não os dados fictícios; não são individualmente aprovadas por esta ponte. Os valores são nominais e arredondamentos não representam incerteza. Os demais registros e QA-09 permanecem pendentes de integração. Sem navegador real, estudantes, revisão humana ou certificação externa.
