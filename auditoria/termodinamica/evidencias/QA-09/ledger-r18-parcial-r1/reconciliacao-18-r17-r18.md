# QA-09 — revalidação individual de 18 objetos r17 na r18

30/10/2026. Responsável `/root/planning`; **integração aguarda auditor independente**. Reexaminei os 18 objetos EX001–005, D26–28 e D11–20 individualmente na r18, suas hipóteses, vínculos e contas; o registro abaixo limita-se ao escopo já definido nos relatórios científicos r16/r17. Em cópia temporária com os snapshots r17, executei o gerador/verificador r17 e obtive 18 objetos/23 contextos; li o parecer independente r17 e seus limites. Para r18, cada recorte foi localizado no inventário por tipo, seção, número ou título e intervalo UTF-16, e reextraído. Os recortes e todos os 23 contêineres ligados aos objetos foram confrontados entre r17 e r18. Sua identidade é evidência de contexto, não um aceite automático dos contêineres, suas fontes ou descendentes.

## Efeito das quatro alterações

Li o parecer da aplicação conjunta r18 `QA-09-aplicacao-conjunta-primeira-lei-entropia-r18-auditoria-independente-20261030.md`. A nova redação de primeira lei explicita que Q é contribuição positiva e o saldo é Q−W; é compatível com os balanços de D17, D26 e demais casos, sob suas hipóteses, sem mudar resultados. A base de entropia de escoamento agora distingue parcelas isotérmicas e integral local; não altera os modelos ou dados destes 18 objetos; o balanço de espécie de D28 não é confundido com balanço de entropia. A correção de EX027 declara calores totais e única outra transferência de energia para o seu exemplo de máquina térmica, que não é o diagnóstico **D27** do misturador; não muda os 18 objetos. A ficha60 delimita trabalho líquido e COP, mas nenhum dos 18 depende dela para os resultados abaixo. D12 liga a `#base-brayton-real`, não é a ficha60, e permanece no balanço de potência explicitado. Não revalido todas as demais ocorrências dessas bases ou a ficha integralmente por este relatório.

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

As fontes (NIST, DOE, EPA, MIT e OpenStax) e seus alcances foram documentados nos relatórios r16/r17, cujas leituras científicas foram consideradas; nenhuma referência é promovida individualmente por esta ponte. Os dados são didáticos e nominais; arredondamento não é incerteza. A igualdade de documentos/fragmentos é prova de identidade, não aprovação científica isolada. Nada aqui aprova outros exemplos, diagnósticos, pais, filhos, contêineres, recursos, fontes ou o QA-09 integral. Não houve teste em navegador real, estudantes, revisão humana ou certificação externa.
