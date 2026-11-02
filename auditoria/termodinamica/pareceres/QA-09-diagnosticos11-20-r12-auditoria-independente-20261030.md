# QA-09 — auditoria independente de diagnósticos 11–20, r12

Data: 30/10/2026. Auditor automatizado `/root/next_examples`, distinto do Corretor `/root/next_theory`. **Veredito localizado: APROVADO para os dez diagnósticos no contexto das bases e com os limites abaixo.** Não conclui QA-09 nem libera outro ID.

## Critério e identidade

QA-09 exige conferência rastreável das ocorrências numéricas fora dos 197 artigos; esta revisão cobre apenas os dez blocos, enunciados, soluções e bases necessárias às contas. Examinei a aula r12 SHA-256 `f76c39a3e1d8c349ebf0df72cc20a3ab21c68960c8451799bad90a9dcc4bd8c7`, inventário r12 `457a56300aab8f612ebb7f136c7c2f62520abb49c005c209a238925179248d0e` e [entrega do Corretor](../evidencias/QA-09/diagnosticos11-20-r12-20261030/entrega.md) SHA-256 `8d58bac8a35a633c76b1ad5e0e474ce8c32de80d786c12c24c5c24210eaaac17`. Reextraí os dez blocos por documento, seção, número, intervalos UTF-16 e SHA do fragmento; nenhuma conclusão de mérito se baseia apenas em igualdade de hash com fotografias anteriores. O [verificador independente](../evidencias/QA-09/auditoria-diagnosticos11-20-r12-20261030/verificar.py), SHA-256 `9dde8f52c8e99ee1d5573dcdeb8fdb0039155d5ad0d20737d77ced73b56724b3`, reproduziu a identificação e as contas em frações exatas sem gravar arquivos. O verificador do Corretor também passou.

## Revisão científica e aritmética

- **11:** para fases em equilíbrio com transferência permitida, o potencial químico de cada componente comum é igual entre elas; não é necessário que densidade ou massa de cada fase coincidam. O [MIT, notas 10, p. 3](https://ocw.mit.edu/courses/3-020-thermodynamics-of-materials-spring-2021/mit3_020s21_l10.pdf) sustenta o caso de substância pura; misturas exigem as restrições de cada componente. Calor latente alto significa maior entalpia específica de vaporização no estado especificado, sem inferir COP ou segurança isoladamente.
- **12:** `(140−50)/300=0,30` e `6/8=0,75`, nas condições de sucção da base; na compressão antes da descarga, válvulas fechadas no modelo alternativo indicado. O enunciado fornece todos os consumos de potência e calor recebido. Valores não demonstram eficiência de uma instalação real.
- **13:** com área e diferença média apropriada constantes, a razão de taxas é 0,7 e a queda é 30%. Convecção dos fluidos e condução da parede são mecanismos do modelo; contato sólido pode conduzir mesmo em vácuo e radiação não exige gás. O [DOE, transferência de calor](https://www.energy.gov/sites/default/files/2026-04/DOE-HDBK-1012-92_VOL2.pdf) distingue esses modos.
- **14:** geração `60×2=120 W`, face exposta `2 m²`, então temperatura média da face `18+120/(6×2)=28 °C`, em regime permanente, radiação desprezada, h uniforme e demais faces isoladas. Não determina distribuição interna de temperatura nem dimensão de transferência detalhada.
- **15–17:** capacidades constantes e modelo sensível de sólidos/líquidos da base, em que ΔU≈CΔT, energia de mistura, efeitos de pressão/deformação e interações externas não declaradas são desprezíveis. As contas são `(12+24+36)/3=24 °C`, `(2×90+6×30)/8=45 °C` e `(4×80+4×20+2×20−20)/10=42 °C`. No 17 o recipiente entra uma vez e a perda externa tem sinal negativo. Essas relações não são universais para materiais com energia dependente de volume, pressão ou mistura; esse domínio é necessário para interpretar os diagnósticos, sem inferir um modelo real de instalação.
- **18:** água pode ceder `0,5×4,2×20=42 kJ`; fundir 0,2 kg de gelo exige `66,8 kJ`. Massa fundida `42/334=21/167≈0,1257485 kg` e restante `62/835≈0,0742515 kg`, arredondando para 0,126 e 0,074 kg. No modelo de coexistência à pressão/temperatura indicadas, Tf=0 °C. Os intervalos de arredondamento de cada massa são ±0,0005 kg, não incerteza experimental.
- **19:** `20×300 mL/min=6000 mL/min=0,36 m³/h`; excesso de 500 ppm é fração 0,0005, logo `V̇=0,36/0,0005=720 m³/h`. Exige modelo estacionário, mistura perfeita, mesmas condições volumétricas e nenhuma fonte/sumidouro ou troca entre zonas além das declaradas. É dado fictício, não um limite regulatório. O [NISTIR 6729](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=860846) fundamenta o balanço de zona única, não os dados do exercício.
- **20:** `36/3600=0,010 m³/s`; `ρgV̇H=1000×10×0,010×15=1500 W`; eficiência da bomba `1500/3000=0,5`. H é altura manométrica total no modelo da base; a potência de eixo não determina a potência elétrica sem rendimento do motor ou medição.

As entradas são hipotéticas e os valores exatos no modelo nominal, exceto arredondamentos explicitados. Os dados não foram extraídos das fontes técnicas citadas. O resultado de 15–17 depende dos limites do modelo sensível, enquanto o calor latente de 18 usa fases coexistentes à temperatura dada; não extrapolar esses casos para materiais, fases ou interações arbitrárias. O [OpenStax sobre calorimetria](https://openstax.org/books/chemistry-2e/pages/5-2-calorimetry) e a [primeira lei do MIT](https://web.mit.edu/16.unified/www/SPRING/thermodynamics/notes/node14.html) apoiam o modelo e sua delimitação.

| Critério localizado | Resultado |
|---|---|
| Identidade e versão dos dez diagnósticos | Atendido por documento, contexto, posição e SHA r12. |
| Cálculos, unidades, arredondamentos e modelos | Atendido no escopo e sob hipóteses acima; d11 é sobretudo qualitativo. |
| Fontes e bases ligadas | Conferidas no recorte, não uma revisão integral de todas as fontes ou da aula. |
| Transferência de pareceres anteriores | Não presumida; a revisão atual é localizada e os aceites históricos mantêm sua fotografia. |
| Critério integral QA-09 e próximo ID | Não atendidos; continuam em correção e bloqueados. |

Não houve teste em navegador real, leitor de tela, revisão humana, aplicação com alunos ou certificação externa. As fórmulas, figuras e seções externas aos blocos não são automaticamente aprovadas por este parecer.
