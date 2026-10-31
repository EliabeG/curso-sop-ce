# QA-09 — revalidação individual de 18 objetos r19 na r20

30/10/2026. Responsável `/root/planning`; **integração aguarda auditor independente**. Reexaminei na r20 os 18 objetos EX001–005, D26–28 e D11–20 e seus dados, cálculos, hipóteses e vínculos. Em cópia temporária, com snapshots de aula e formulário r19, reproduzi o verificador do ledger r19 r2 (18 objetos/23 contextos) e examinei seu parecer independente. Cada recorte da r20 foi reextraído pelo inventário, e os 23 contêineres contextuais foram confrontados entre versões; 21 são idênticos e dois mudaram. A identidade de hash auxilia a localização, não é a razão exclusiva para a revalidação e não aprova contêineres, filhos ou fontes separadas.

## Efeito direto das bases alteradas

As únicas alterações r19→r20 são `#base-mistura-termica` e `#base-fase-calorimetria`, examinadas na aplicação r20 e seu parecer independente. Não se trata de bases estruturalmente idênticas: a primeira fixa que o conjunto é fechado e isolado, sem trabalho relevante, reação ou mudança de fase, e que ΣCi(Tf−Ti) representa a variação de energia, com efeitos de mistura, pressão e deformação desprezíveis; a segunda identifica ℓ como magnitude da diferença de entalpia para substância pura em equilíbrio e limita Q=ΔH à etapa fechada a pressão constante, sem energia cinética/potencial e somente trabalho de fronteira pΔV. As alterações são compatíveis com os cálculos abaixo, sob as condições de cada diagnóstico.

- **D15:** a base modificada fornece o modelo sensível; três porções da mesma substância, capacidades constantes e iguais, isolamento e ausência de fase nova, com energia de mistura e efeitos de pressão/deformação desprezíveis, dão 24 °C. A média não é universal.
- **D16:** o enunciado exclui reação e mudança de fase; a base atual explicita capacidades constantes e o modelo sensível sem interações externas relevantes. (2×90+6×30)/8=45 °C, sob essas hipóteses, não para qualquer propriedade de material ou energia de mistura.
- **D17:** a perda externa de 20 kJ está explicitamente declarada no diagnóstico: não se aplica ao conjunto sua fórmula isolada ΣCiΔT=0, mas o modelo sensível permanece válido com ΣCiΔT=−20 kJ. As capacidades 4, 4 e 2 kJ/K e as temperaturas 80, 20 e 20 °C dão Tf=42 °C; recipiente contado uma vez e trabalho relevante ausente.
- **D18:** o enunciado adota água e gelo, 0 °C, calor específico e latente nominais, conjunto isolado e recipiente desprezível. No modelo de fases puras em equilíbrio, à pressão/temperatura de transição adotadas, a etapa de fusão sob as condições de calor/entalpia acima exige 0,2×334=66,8 kJ; a água oferece 42 kJ. Funde 42/334≈0,126 kg, resta ≈0,074 kg e Tf=0 °C. Essas hipóteses não garantem aplicação a qualquer mistura ou pressão.

As outras 21 bases e os 18 recortes são estruturalmente preservados. A revisão do significado e das contas foi repetida, sem promover pais, descendentes, fontes ou recursos. Os resultados individuais são:

| Objeto | Resultado e condição verificada na r20 |
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

Fontes NIST, DOE, EPA, MIT e OpenStax e seus limites permanecem rastreados nos relatórios anteriores e no parecer r20; fontes não são individualmente aprovadas por esta ponte. Valores didáticos são nominais, não medições, e arredondamentos não são incerteza experimental. Os demais registros mantêm estado pendente de integração. Não houve navegador real, estudantes, revisão humana ou certificação externa. QA-09 continua em correção.
