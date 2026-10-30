# QA-09 — revalidação individual de 18 objetos r26 na r27

30/10/2026. Responsável `/root/planning`; **integração pendente de Auditor independente**. Reli na r27 os 18 objetos EX001–005, D26–28 e D11–20, seus enunciados, modelos, contas e bases dentro do escopo dos pareceres históricos. Reproduzi em cópia temporária dos snapshots r26 o gerador do ledger r26 r2 e examinei o parecer independente; a r1 anterior, cujo relatório confundia D15 com EX015, permanece separada e não é promovida. Reextraí cada recorte do inventário r27 por documento, seção, posição e hash e comparei os 23 contêineres associados: todos são idênticos à r26. Esses testes de identidade não aprovam por si os contextos, pais, filhos ou fontes.

## Efeitos de Carnot e dos cartões

Reli os quatro deltas e o parecer da aplicação r27: a base de Carnot restringe as três relações a dois reservatórios de temperaturas absolutas constantes TH>TL>0 e distingue sinais de motor e ciclos reversos; os cartões esclarecem COP com trabalho líquido total, eficiência motora de Carnot e eficiência específica do compressor. Nenhuma das quatro alterações está nos 18 recortes ou nos 23 contêineres vinculados. Mesmo assim, confrontei os modelos: D26 calcula apenas balanço energético do ciclo nominal com calor total recebido e trabalho líquido na mesma base; sem temperaturas dos reservatórios não é possível certificar Carnot ou viabilidade pela segunda lei. D12 calcula rendimento líquido e eficiência **volumétrica** a sucção, não a eficiência isentrópica do cartão do compressor. D27 mantém a potência 2000 kW apenas sob o modelo vinculado de turbina de uma entrada e uma saída, trabalho total não associado ao escoamento, sem calor ou variações cinética/potencial relevantes; não se deduz potência de um eixo individual ou generalização a múltiplas saídas. Nenhum dos 18 utiliza os cartões como dados numéricos.

D11 permanece no equilíbrio local de fases para a mesma espécie com contribuição externa igual; D14 mantém a fonte elétrica explícita e a saída convectiva sem dupla contagem. D15 é o diagnóstico de mistura das porções a 12, 24 e 36 °C, não EX015; D17 considera a perda externa e D18 o modelo de fase de sua base. Reli os demais contextos e refiz os resultados abaixo, sem conferir aceite a qualquer contêiner separado:

| Objeto | Resultado e condição verificada na r27 |
|---|---|
| EX001 | 9/0,010=4,5/0,005=900 kg/m³; amostra homogênea dividida na mesma condição. |
| EX002 | −10+120=110 °C; intervalo de 120 °C tem magnitude 120 K; span não é incerteza. |
| EX003 | 10+(30/40)(90−10)=70; interpolação afim na base, sem provar calibração real. |
| EX004 | (900−400)/(2400−400)=0,25; título mássico da mistura saturada em equilíbrio com entalpias de mesma referência, não fração de volume. |
| EX005 | 0,082×320/26,24=1 atm, na aproximação da constante e condições dadas. |
| D26 | 600+900−20=1480 kJ/kg; calor recebido 3200 kJ/kg, rendimento 46,25%, rejeição 1720 kJ/kg; a primeira lei não prova viabilidade pela segunda. |
| D27 | y=(700−300)/(2300−300)=0,20; (1−y)×10×250=2000 kW; mistura permanente adiabática, sem trabalho, energias cinética/potencial desprezíveis e referências compatíveis; potência do estágio sob modelo vinculado de entrada e saída únicas e trabalho total não-fluxo. |
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

As fontes de modelo e limites, incluindo NIST, DOE, EPA, MIT e OpenStax, permanecem nos relatórios históricos e no parecer r27; não se aprova cada referência por esta ponte. Valores são didáticos e nominais; arredondamentos não representam incerteza experimental. Os demais registros, pais, filhos, bases, referências e recursos permanecem pendentes de integração. Sem navegador real, alunos, revisão humana ou certificação externa. QA-09 continua em correção.
