# QA-09 — revalidação individual de 18 objetos r24 na r26

30/10/2026. Responsável `/root/planning`; **integração pendente de Auditor independente**. Esta é uma ponte direta r24→r26: não existiu ledger r25 intermediário para estes objetos. Reproduzi o ledger r24 em cópia temporária dos snapshots e li o parecer independente daquela fotografia. Reli os 18 recortes EX001–005, D26–28 e D11–20, seus cálculos e 23 contêineres contextuais na r26. Todos os recortes são idênticos à r24, mas `#base-turbina-potencia` teve seu contêiner alterado na r26; os outros 22 contextos são iguais. Identidade e mapas auxiliam localização e não aprovam automaticamente qualquer conteúdo, pai, filho ou fonte.

## Efeitos r25 e r26

A r25 alterou a preparação `#fun01-fases` para distinguir a regra de alavanca não degenerada, xA=yA e propriedade global independente. D11 examina equilíbrio local de fases com troca permitida, não determina β por composição; continua válido comparar o potencial da mesma espécie na interface, sob a mesma contribuição externa, sem generalizar a alturas distintas. Os outros 17 recortes não usam a nova regra como dado. A aplicação r25 tem parecer independente; a r25 contém 11.405 ocorrências, com nós reestruturados, e nenhum deles recebe aprovação por esta ponte.

A r26 aplicou quatro alterações FUN-02 (escala de gás ideal, diferenciais parciais, trabalho total de fronteira e fator integrante), a ficha 59 e EX010/tabela. D27 liga ao título `#base-turbina-potencia` que pertence ao contêiner da tabela alterado: reli a linha e o diagnóstico. Para seu aquecedor aberto, y=(700−300)/(2300−300)=0,20, de 10 kg/s seguem 8 kg/s. A potência 8×250=2000 kW é revalidada **sob o modelo vinculado de turbina com uma entrada e uma saída, adiabática, energias cinética/potencial desprezíveis e trabalho total não associado ao escoamento**. O enunciado do diagnóstico não enumera sozinho todas essas condições; este alcance depende expressamente da base ligada. Não extrapolar a múltiplas saídas ou potência de um único eixo sem dados. A tabela agora explicita essas condições e mantém o trocador de duas correntes sem mistura e com transferência térmica interna permitida.

D15 trata expansão livre de gás ideal em volume rígido isolado: ΔS=mR ln2≈0,199 kJ/K é diferença de estados, sem inferir reversibilidade do processo, coerente com o esclarecimento de reversibilidade do fator integrante. EX005 usa seu próprio pV=nRT sob constante aproximada, não a duplicação irrestrita de trabalho; D12 e D26 mantêm seus balanços próprios e não utilizam a ficha59 como dado. D14 retém a entrada elétrica explícita e o modelo de geração sem dupla contagem. As relações e fontes foram examinadas nas aplicações r25/r26, inclusive [MIT, balanço em escoamento](https://ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_6.htm), [Washington, soluções ideais](https://faculty.washington.edu/jcv2/CHEM452_WI2023/html/ideal_solutions_and_colligative_properties.html) e [MIT, primeira lei](https://ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_4.htm). Elas fundamentam modelos e não são fontes dos números fictícios. Os resultados reavaliados individualmente são:

| Objeto | Resultado e condição verificada na r26 |
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

Dados são nominais e arredondamentos não são incerteza experimental. A relação de D27 depende do modelo da base vinculada, não de generalização a todas as turbinas. Os demais registros, bases, pais, filhos, referências e recursos permanecem pendentes de integração; não há transferência automática de aceite. Não houve navegador real, estudantes, revisão humana ou certificação externa. QA-09 continua em correção.
