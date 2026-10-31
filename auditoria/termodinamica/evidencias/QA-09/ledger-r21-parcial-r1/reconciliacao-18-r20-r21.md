# QA-09 — revalidação individual de 18 objetos r20 na r21

30/10/2026. Responsável `/root/planning`; **integração aguarda auditor independente**. Reli na r21 os 18 objetos EX001–005, D26–28 e D11–20, condições, resultados, fontes e vínculos no alcance dos relatórios históricos. Reproduzi em cópia temporária dos snapshots r20 o gerador e ledger auditado daquela versão (18 registros/23 contextos). Os recortes foram reextraídos do inventário r21; dos 23 contextos, 22 permanecem iguais e `#base-geracao-face` mudou devido à aplicação do EX046. Identidade e mapas são suporte de localização, não aprovação científica de contextos ou descendentes.

## EX046, oficina e D14

Li os dois deltas e o parecer de aplicação r21. O EX046 corrigido identifica a alimentação elétrica de 1200 W como fonte da geração térmica de 1200 W, e essa mesma energia sai por convecção; não é somada duas vezes. A alteração ocorre dentro de `#base-geracao-face`, ligada ao D14, e altera seu hash: examinei novamente o texto da base e o próprio D14, e não presumi aceitação pela identidade do exemplo. O D14 fornece volume 2 m³, geração térmica volumétrica 60 W/m³, apenas uma face convectiva exposta de 2 m², demais faces isoladas termicamente, h=6 W/(m²·K), exterior a 18 °C, regime permanente e radiação desprezada. No modelo térmico com geração total especificada e ausência de outras saídas relevantes, 60×2=120 W e a temperatura média da face é 18+120/(6×2)=28 °C. Uma realização em regime permanente de energia total deve possuir fonte energética compatível com a geração térmica; o D14 não especifica qual é, e não se atribui a ele automaticamente a alimentação de 1200 W do EX046. Um aporte térmico adicional fora da geração informada ou outra saída exigiria novo balanço.

O outro delta explicita a fronteira de entropia da oficina e suas interfaces; nenhum dos 18 objetos usa esse trecho como dado. Por exemplo, D26 calcula o balanço energético de seu ciclo nominal sob suas próprias condições, e D28 usa conservação de espécie e não geração de entropia. As bases de mistura e fase anteriormente alteradas foram relidas para D15–18, inclusive a perda de D17; não foram modificadas na r21. Os demais resultados permanecem válidos somente nos modelos e limites a seguir:

| Objeto | Resultado e condição verificada na r21 |
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

As referências e suas limitações permanecem documentadas nos relatórios e pareceres anteriores. Não reclassifico fontes ou recursos como registros individualmente aprovados; os dados são nominais e arredondamentos não são incerteza. Os demais objetos, pais, descendentes, contêineres e recursos permanecem pendentes de integração. Sem navegador real, estudantes, revisão humana ou certificação externa; QA-09 continua em correção.
