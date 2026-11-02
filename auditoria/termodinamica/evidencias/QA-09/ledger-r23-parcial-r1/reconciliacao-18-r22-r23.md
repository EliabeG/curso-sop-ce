# QA-09 — revalidação individual de 18 objetos r22 na r23

30/10/2026. Responsável `/root/planning`; **integração pendente de auditor independente**. Reli os 18 objetos EX001–005, D26–28 e D11–20, seus dados, hipóteses e bases na r23 no alcance dos pareceres históricos. Reproduzi em cópia temporária dos snapshots r22 o verificador do ledger r22, incluindo a reconstrução da candidata D14, e li seu parecer independente. Cada um dos 18 recortes foi reextraído por documento, seção, tipo, posição UTF-16 e hash; os 23 contêineres associados foram confrontados. Todos os recortes e contêineres são idênticos entre as fotografias. Essa identidade apoia localização e leitura, não aprova por si só bases, filhos ou fontes.

## Efeito do resumo e glossário

Li os dois deltas r22→r23 e o parecer independente da versão aplicada. O resumo distingue turbina de uma entrada/saída, válvula sem trabalho não associado ao escoamento, calor externo total no rendimento, trabalho líquido positivo no COP e operação motora reversível no limite de Carnot. D26 continua no balanço nominal de ciclo com entradas de calor totais explícitas e mesma base de massa; D27 usa seu próprio misturador adiabático e a turbina posterior sob hipóteses declaradas, sem extrapolar o modelo de um único dispositivo a todo o circuito. D12 usa potência e calor totais do enunciado e a eficiência volumétrica na base de sucção. Nenhuma das alterações redefine seus valores.

O glossário distingue fator Z da compressibilidade isotérmica e limita COP a acionamento por trabalho. EX005 usa a relação de gás ideal e a constante aproximada da própria base, sem determinar outras propriedades pela mera igualdade Z=1; os outros registros não fazem esse uso do verbete. Nenhum dos 18 recortes ou seus 23 contêineres mudou pela aplicação. As fontes de modelo e suas limitações, incluindo NIST, DOE, EPA, MIT e OpenStax, foram examinadas nos pareceres anteriores e no parecer r23; sua identidade não é uma classificação de aprovação de cada referência.

D14 permanece a versão corrigida na r22: bloco fechado, energia total permanente, 120 W de trabalho elétrico convertidos em geração térmica, sem aporte adicional, única saída convectiva, V=A=2 em unidades apropriadas. A face tem 18+120/(6×2)=28 °C e Q̇−Ẇ=−120−(−120)=0. D13 conserva as ressalvas da base de radiação; D17 trata a perda externa declarada e D18 segue o modelo de fases em equilíbrio. Os resultados individualizados a seguir foram recalculados sem extrapolar suas hipóteses:

| Objeto | Resultado e condição verificada na r23 |
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

Dados fictícios são nominais; arredondamentos não representam incerteza. Os demais objetos, pais, filhos, fontes e recursos permanecem pendentes de integração. Não houve navegador real, estudantes, revisão humana ou certificação externa; QA-09 continua em correção.
