# QA-09 — revalidação individual de 18 objetos r16 na r17

30/10/2026. Responsável `/root/planning`; **aguarda auditoria independente da integração**. Escopo: os oito registros EX001–005/D26–28 da r16 r1 e os dez D11–20 da r16 r2, com os alcances explicitados nos relatórios r16 e seus pareceres independentes. Não há aprovação automática por correspondência ou hash. As 18 identidades foram reextraídas por número/título, seção, posição UTF-16 e hash; recortes e links permaneceram idênticos. Foram confrontados todos os contêineres de bases ligados pelos diagnósticos e as bases dos exemplos, total 22 âncoras únicas mais o contêiner do título EX004; a identidade do contexto não aprova cada contêiner ou seus filhos.

Li o único delta r16→r17, a candidata aplicada em `#base-brayton`, e seu parecer `QA-09-aplicacao-intercooling-r17-auditoria-independente-20261030.md`: a afirmação sobre intercooling passa a ser comparação de dois estágios adiabáticos sob condições explícitas e não altera os 18 recortes ou os 23 contêineres de contexto acima. D12 usa `#base-brayton-real`, diferente da base alterada, e seu enunciado exclui outros consumos: a conta de potência líquida e as hipóteses mantêm-se válidas; não se infere redução universal de potência da instalação. D26/27 tratam os ciclos e turbina nas hipóteses próprias dos problemas; a mudança não transforma seus dados fictícios em uma instalação específica. Em cópia temporária com snapshot r16, reexecutei a verificação completa do ledger r16 r2 e obtive 8+10 registros; examinei os dois pareceres independentes r16 r1/r2 e seus limites. Recalculei as contas para a r17 como segue.

| Objeto | Verificação r17 e condições que limitam o aceite |
|---|---|
| EX001 | 9/0,010=4,5/0,005=900 kg/m³; amostra homogênea dividida na mesma condição. |
| EX002 | −10+120=110 °C; intervalo 120 °C equivale a 120 K; não é incerteza. |
| EX003 | 10+(30/40)(90−10)=70; interpolação afim na base, sem alegação de calibração real. |
| EX004 | (900−400)/(2400−400)=0,25; qualidade mássica de mistura saturada em equilíbrio com referência de entalpia comum, não fração volumétrica. |
| EX005 | 0,082×320/26,24=1 atm, usando constante aproximada da base e condições fornecidas. |
| D26 | w=600+900−20=1480, qin=2400+800=3200, η=46,25%, qout=1720 kJ/kg; balanço de primeira lei não confirma viabilidade de segunda lei. |
| D27 | y=(700−300)/(2300−300)=0,20; (1−y)×10×250=2000 kW; mistura adiabática permanente, sem trabalho, energia cinética/potencial desprezível e entalpias compatíveis. |
| D28 | [0,20+500(0,0004−0,0006)]/200=0,0005 h⁻¹=500 ppm/h inicialmente; equilíbrio estacionário 800 ppm no modelo de mistura diluída e bem misturada, fluxos equilibrados e sem fontes extras. |
| D11 | Igualdade dos potenciais químicos de componentes comuns em equilíbrio com transferência permitida; densidades podem diferir; calor latente isoladamente não determina COP/segurança. |
| D12 | (140−50)/300=30%; volumes à sucção 6/8=75%; válvulas fechadas na compressão antes da descarga, no modelo indicado. |
| D13 | U cai para 0,7U e taxa cai 30% com área e diferença média constantes; contatos sólidos conduzem no vácuo e radiação dispensa gás. |
| D14 | geração 60×2=120 W, área 2 m², 18+120/(6×2)=28 °C média da face; regime permanente, demais faces isoladas, h uniforme e sem radiação. |
| D15 | (12+24+36)/3=24 °C, capacidades iguais e constantes no modelo sensível isolado. |
| D16 | (2×90+6×30)/8=45 °C; capacidades constantes e interações extras desprezíveis. |
| D17 | (4×80+4×20+2×20−20)/10=42 °C; perda externa negativa, recipiente uma vez e modelo sensível. |
| D18 | 0,5×4,2×20=42 kJ; 0,2×334=66,8 kJ; fundem 42/334≈0,126 kg, restam ≈0,074 kg; coexistência a 0 °C no modelo adotado. |
| D19 | 20×300 mL/min=0,36 m³/h; 0,36/0,0005=720 m³/h; regime estacionário, mesma base volumétrica, bem misturado e sem outras fontes/sumidouros. |
| D20 | 36/3600=0,010 m³/s; 1000×10×0,010×15=1500 W e 1500/3000=50%; sem dados de motor não se determina potência elétrica. |

Os dados são nominais; arredondamentos não representam incertezas experimentais. As referências científicas verificadas nas reconciliações r16 r1/r2 (NIST, DOE, EPA, MIT e OpenStax) e seus limites continuam documentadas nos relatórios originais; nenhuma fonte é reclassificada como registro individual aqui. A comparação não transfere aprovação aos descendentes, pais, contextos, referências, recursos ou a outros objetos. O ledger permanece parcial e não aprova QA-09. Não houve navegador real, estudantes, revisão humana ou certificação externa nesta integração.
