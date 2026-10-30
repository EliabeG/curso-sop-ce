# QA-09 — reconciliação localizada diagnósticos 11–20 na r16

30/10/2026. `/root/planning`; integração pendente de auditor independente. Fonte histórica `auditoria/termodinamica/pareceres/QA-09-diagnosticos11-20-r12-auditoria-independente-20261030.md`, de `/root/next_examples`, examinou os dez recortes, hipóteses e cálculos na r12. Reli os dez blocos na r16, reavaliei as bases ligadas, examinei os deltas e refiz as contas abaixo; nenhuma linha é aprovada por igualdade de hash isolada. A r16 fixa aula SHA `55754bfc631da9010e3c9afc73e3c458e349b535c429fe98abe28998897aab23`, inventário `2c4d4da464488f7eab06b6d56d32d83b27fdbb542aaa1d847a412d18c955cbcd`.

Os dez blocos foram localizados por número, seção, fragmento UTF-16, identidade de inventário e contexto. Treze bases ligadas têm contêiner igual ao da r12; a base `#base-brayton-real` ligada ao diagnóstico 12 mudou. Li o texto atual: a relação de potência líquida como diferença entre turbina e compressor, desprezando outros consumos, permanece adequada ao enunciado que os exclui; a nova comparação adiabática de irreversibilidades tem alcance próprio e não altera o balanço de D12. Seu delta recebeu parecer independente localizado r16 em `auditoria/termodinamica/pareceres/QA-09-aplicacao-conjunta-ciclos-r16-auditoria-independente-20261030.md`. Conferir contêineres não os aprova genericamente.

| Diagnóstico | Revalidação na r16 e limite |
|---|---|
| 11 | Equilíbrio com transferência permitida iguala potencial químico de cada componente comum entre fases, não densidade ou massa. Calor latente maior é maior entalpia específica de vaporização do estado considerado, não garante COP ou segurança. |
| 12 | (140−50)/300=0,30; válvulas fechadas durante compressão antes da descarga no modelo indicado; volumes à sucção 6/8=0,75. O enunciado especifica potência e calor totais e exclui outros consumos. |
| 13 | Com área e diferença média adequadas constantes, Q₂/Q₁=U₂/U₁=0,7; queda de 30%. Contatos sólidos conduzem também em vácuo e radiação dispensa meio gasoso. |
| 14 | 2 m³×60 W/m³=120 W; área exposta 2 m²; 18+120/(6×2)=28 °C. É temperatura média da face, com isolamento das demais, h uniforme e radiação desprezada, não distribuição interna. |
| 15 | Capacidades iguais e constantes, no modelo sensível isolado: (12+24+36)/3=24 °C. |
| 16 | Capacidades constantes, sem fase, reação ou trabalho/interações relevantes no modelo sensível: (2×90+6×30)/8=45 °C. |
| 17 | Mesmo modelo sensível com recipiente incluído uma vez e perda negativa: (4×80+4×20+2×20−20)/10=42 °C. Os itens 15–17 não generalizam ΔU≈CΔT a materiais e interações arbitrários. |
| 18 | Água fornece 0,5×4,2×20=42 kJ; fusão total pede 0,2×334=66,8 kJ. Fundem 42/334≈0,126 kg; restam 0,074 kg e coexistem a 0 °C nas hipóteses adotadas. Arredondamento não é incerteza experimental. |
| 19 | 20×300 mL/min=0,36 m³/h; excesso 500 ppm=0,0005; vazão 720 m³/h. Modelo estacionário, bem misturado e nas mesmas condições volumétricas, sem fontes, sumidouros ou trocas extras; dado didático, não norma. |
| 20 | 36/3600=0,010 m³/s; ρgV̇H=1500 W; η=1500/3000=50%. H é altura manométrica total; não há potência elétrica sem rendimento do motor ou medição. |

Conferi novamente em 30/10/2026 as [notas MIT sobre equilíbrio de fases de substância pura](https://ocw.mit.edu/courses/3-020-thermodynamics-of-materials-spring-2021/mit3_020s21_l10.pdf), [DOE vol. 2 sobre transferência de calor](https://www.energy.gov/sites/default/files/2026-04/DOE-HDBK-1012-92_VOL2.pdf), [OpenStax sobre calorimetria](https://openstax.org/books/chemistry-2e/pages/5-2-calorimetry), [NISTIR 6729 sobre balanço de CO₂](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=860846) e, para energia/primeira lei, [MIT](https://web.mit.edu/16.unified/www/SPRING/thermodynamics/notes/node14.html). Essas fontes embasam modelos no alcance indicado; os números são do exercício, não foram extraídos delas. Caso alguma consulta não seja legível ou suficiente, o Auditor deve manter pendente o recorte correspondente. Sem navegador interativo, teste de estudantes ou revisão humana.

O parecer r12 e esta reconciliação não são aceite global de QA-09, contextos, fontes separadas, ocorrências descendentes, demais diagnósticos ou outros itens. Cada registro proposto é limitado à respectiva linha e depende de auditor independente da integração.
