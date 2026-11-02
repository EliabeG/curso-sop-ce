# QA-09 — auditoria independente da candidata do diagnóstico 23, r13

Data: 30/10/2026. Auditor automatizado `/root/planning`, distinto do Corretor `/root/next_examples`. **Veredito: APROVADA como proposta isolada, no alcance abaixo.** A candidata ainda não está aplicada nem auditada na versão efetiva. QA-09 integral permanece em correção; não há liberação do próximo ID.

## Critério e identidade

QA-09 exige conferência do conteúdo numérico, inclusive dos diagnósticos. A [auditoria de 21–25](QA-09-diagnosticos21-25-r13-auditoria-independente-20261030.md) apontou que as entradas numéricas do nº 23 estavam expressas em kJ/kg sem nomear a propriedade específica. Esta avaliação abrange apenas a candidata destinada a corrigir esse ponto; não aprova os demais diagnósticos nem QA-09 integral.

Aula r13 SHA-256 `f19000a7ddb1f3552b9633b0efec266fb3f6c5e5065808505a2f65b2005aefbc`; inventário r13 `0df99b79bcc2350581fcdded72435d30d07858de237a549e6228ca73682f8d9b`. O bloco original `#preparacao-questoes`, diagnóstico 23, ocupa o intervalo UTF-16 534074–534884 e tem SHA-256 `e5e87b30397cc0394b10b1194461e7bf64fd0e831184d4b91eeae0d234cd5073`; a candidata tem hash `7ff95d0d97ccbf5c2fa3475c0d5d4019fb2657686e4daebc3d55536fc9b66d10`. A [análise do Corretor](../evidencias/QA-09/candidata-diagnostico23-r13-20261030/analise.md) tem SHA-256 `8874ab2c141a284414967921712ab96ebc500c9b9bc05588e2bcb284ad9030c9`.

## Exame científico e textual

O original identificava vazões e valores de 100 e 400 kJ/kg, sem especificar a grandeza. O contramodelo do parecer anterior usa esses valores como energias internas de um gás ideal fictício de calor específico constante: com cᵥ=0,718 e R=0,287 kJ/(kg·K), cₚ=1,005 e referência comum compatível, h₁≈139,972 e h₂≈559,889 kJ/kg; o balanço adiabático para as vazões 2 e 1 kg/s dá h₃≈279,944 kJ/kg. Os números são hipotéticos e não descrevem a intenção do enunciado; mostram que a unidade sozinha não distingue u de h.

A candidata identifica expressamente as **entalpias específicas** de entrada como 100 e 400 kJ/kg, mantendo as vazões mássicas e as demais frases, a resolução e os links. Com escoamento permanente, uma saída, sem trabalho, variações cinética/potencial desprezíveis e entalpias na mesma referência e apropriadas aos estados, a conservação de massa dá 3 kg/s. Para as entalpias nomeadas, `h₃=(2×100+1×400)/3=200 kJ/kg`; com 30 kW recebidos, `(600+30)/3=210 kJ/kg`. O balanço determina h, não temperatura ou fase sem informação adicional. Os valores são dados nominais, não medições.

Examinei a referência local `#base-misturador-correntes`: ela explicita o balanço estacionário e a necessidade de referências de entalpia compatíveis. A candidata elimina o contramodelo por nomear a grandeza, sem alterar a função do exercício ou entregar os resultados. O [MIT](https://web.mit.edu/16.unified/OldFiles/www/FALL/thermodynamics/notes/node17.html), consultado em 30/10/2026 na auditoria do achado, apresenta `h=u+pv` e seu uso em escoamento; não é a fonte dos dados fictícios.

## Reprodução e decisão

O verificador independente [verificar.mjs](../evidencias/QA-09/auditoria-candidata-diagnostico23-r13-20261030/verificar.mjs), SHA-256 `fc3c8cd1f7917e4495fa2057ab9140303ee42459531f0f2c3d3544d8ad752b8d`, reextraiu original por posição e hash, verificou sua ocorrência única, reconstruiu o único delta literal e, em simulação em memória, preservou os 197 artigos em ordem. Também reproduziu as duas respostas e o contramodelo. O teste não grava a aula, não comprova aplicação efetiva e não substitui navegador real.

| Critério localizado | Resultado |
|---|---|
| Identidade, contexto, unicidade e delta | Atendidos na fotografia r13. |
| Ambiguidade de propriedade e contramodelo | Resolvidos na proposta ao nomear as entalpias específicas. |
| Hipóteses, unidades e solução | Conferidas no modelo explicitado e em sua base. |
| Aplicação, novo mapa e regressão | Ainda não examinados; requerem auditoria após aplicação. |
| QA-09 integral e próximo ID | Não atendidos; permanecem bloqueados. |

Para aplicação, reconfirmar hashes e identidade; congelar a versão, produzir novo inventário e mapa sem sobrescrever históricos, verificar as questões, referências e dependências e solicitar parecer independente da versão efetiva. Nenhum teste com alunos, revisão humana ou certificação externa foi realizado. A proposta aprovada não classifica o curso como avançado.
