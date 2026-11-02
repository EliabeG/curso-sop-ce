# QA-09 — auditoria independente dos diagnósticos 21–25, r13

Data: 30/10/2026. Auditor automatizado `/root/planning`, distinto do Corretor `/root/next_examples`. **Veredito: AJUSTES OBRIGATÓRIOS no diagnóstico 23**, pela falta de identificação explícita da propriedade específica informada nas entradas. Não aprova integralmente o lote ou QA-09 nem libera o próximo ID.

## Escopo e identidade

QA-09 exige inventário e recálculo de todas as ocorrências numéricas além dos itens BAN-08, incluindo diagnósticos e explicações. Este parecer examina os cinco blocos de `#preparacao-questoes`, seus modelos e bases identificadas, sem avaliar toda a aula ou outras ocorrências. O parecer localizado da fotografia r7 não foi transferido automaticamente para r13; os enunciados e bases foram lidos novamente.

Aula SHA-256 `f19000a7ddb1f3552b9633b0efec266fb3f6c5e5065808505a2f65b2005aefbc`; inventário r13 `0df99b79bcc2350581fcdded72435d30d07858de237a549e6228ca73682f8d9b`; [entrega do Corretor](../evidencias/QA-09/diagnosticos21-25-r13-20261030/entrega.md) SHA-256 `8a6e204d2a42ef4c7d858a7be371224d7838a85e726a7217cd7867fa1d597165`. O verificador independente [verificar.py](../evidencias/QA-09/auditoria-diagnosticos21-25-r13-20261030/verificar.py), SHA-256 `8c34254d1bc0b12468cc56062b71ff337b16e6c28adcfacd7f06b6d035f8a9d3`, reextrai os cinco fragmentos na posição r13 e recalcula as contas e o contramodelo abaixo. O script não interpreta cientificamente os enunciados.

## Achado — diagnóstico 23

O enunciado informa correntes de “2 kg/s a 100 kJ/kg” e “1 kg/s a 400 kJ/kg”, mas não identifica a grandeza à qual esses valores se referem. A solução os trata como entalpias específicas. O contexto de misturador e a base vinculada sugerem essa leitura, porém `kJ/kg` também é unidade de outras formas de energia específica. A base explica que correntes transportam entalpia, mas não transforma automaticamente um número sem grandeza nomeada em um dado de entalpia.

Contramodelo hipotético sob um gás ideal caloricamente perfeito, sem representar os dados pretendidos pelo autor: se 100 e 400 kJ/kg forem energias internas específicas de duas correntes do mesmo gás, com `cᵥ=0,718` e `R=0,287 kJ/(kg·K)`, `cₚ=1,005` e referência comum compatível, então `h=(cₚ/cᵥ)u`. As entalpias de entrada são aproximadamente 139,972 e 559,889 kJ/kg; com as vazões do enunciado e as hipóteses de mistura estacionária adiabática sem trabalho ou variações cinética/potencial relevantes, `h₃=(2h₁+h₂)/3≈279,944 kJ/kg`, não 200. Isso não sustenta que essa interpretação era a intenção da aula; demonstra que o rótulo dos dados é necessário para determinar a conta proposta. A definição `h=u+pv` e o papel do escoamento são apresentados pelo [MIT](https://web.mit.edu/16.unified/OldFiles/www/FALL/thermodynamics/notes/node17.html), consultado em 30/10/2026.

**Ajuste obrigatório:** no enunciado do diagnóstico 23, identificar explicitamente as entalpias específicas de 100 e 400 kJ/kg das duas entradas, mantendo vazões, hipóteses, pergunta e resolução. Preparar candidata isolada, confrontar a versão e os hashes, e submeter a alteração aplicada a novo mapa, teste e auditoria independente. Para as entalpias pretendidas, a conta publicada é correta: adiabático `h₃=(2×100+1×400)/3=200 kJ/kg`; com 30 kW recebidos, `(600+30)/3=210 kJ/kg`. As entalpias devem ser apropriadas às substâncias e a uma referência compatível, conforme a base da aula.

## Demais resultados localizados

- **21:** tanque rígido, vazio inicialmente, sem saída, calor ou trabalho e com as hipóteses de energia e composição da base; `m₂=m_in`, `u₂=h_in`. Para gás ideal caloricamente perfeito e referências consistentes, `T₂=(cₚ/cᵥ)T_in=1,25×320=400 K`. A acumulação de massa exclui regime permanente durante o enchimento. Isso não implica temperatura uniforme ao longo do transiente.
- **22:** para `cₚ(T)=0,80+0,001T`, integral de 300 a 400 K dá `0,80×100+0,0005(400²−300²)=115 kJ/kg`; congelar a entrada `cₚ(300)=1,10` fornece 110 kJ/kg. O coeficiente linear usa kJ/(kg·K²); dados são autorais e não medições.
- **24:** para bocal estacionário, adiabático, sem trabalho e Δz desprezível, `v₂²=100²+2×1000×75=160.000`, logo `v₂=400 m/s`. Desprezar a entrada daria √150.000=387,2983… m/s, que arredonda a 387,30 m/s; conservação não exige reversibilidade.
- **25:** no modelo usual da base de válvula, `h₂≈h₁`. Para tabela didática da substância pura em equilíbrio, `x=(1000−500)/(2500−500)=0,25`. Com 2700 kJ/kg, o resultado algébrico 1,10 excede [0,1] e não representa título; consultar a região de vapor superaquecido à pressão de saída. As hipóteses de regime, calor, trabalho e energias cinética/potencial estão na base e não são universais.

Resultados são nominais nos modelos; o intervalo de arredondamento 387,30 m/s é [387,295;387,305), não incerteza experimental. Consultei também [NASA, conservação de energia](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/conservation-of-energy/) para termos de entalpia e velocidade, sem atribuir os números didáticos a essa fonte.

| Critério localizado | Resultado |
|---|---|
| Identidade e aritmética dos cinco blocos | Conferidas na fotografia r13; resultado do nº 23 depende da interpretação dos dados. |
| Hipóteses e modelos 21, 22, 24, 25 | Conferidos nos limites e referências citados. |
| Suficiência de dados do diagnóstico 23 | **Não atendida:** grandezas de entrada precisam ser nomeadas. |
| Critério integral QA-09 e próximo ID | Não atendidos; permanecem bloqueados. |

Não houve navegador real, revisão humana, aplicação com alunos ou certificação externa. A revisão dos outros quatro blocos não transfere automaticamente cobertura a fontes ou nós adjacentes; mudança de versão requer reconciliação.
