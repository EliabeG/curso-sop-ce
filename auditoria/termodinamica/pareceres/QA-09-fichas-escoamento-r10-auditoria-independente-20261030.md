# QA-09 — auditoria independente das fichas 47–56, r10

Data: 30/10/2026. Revisor automatizado independente `/root/next_theory`, distinto do Corretor `/root/next_formulas`. **Veredito: AJUSTES OBRIGATÓRIOS**, restritos à explicitação da referência volumétrica de G nas fichas 52 e 53. Não foi encontrado outro erro no recorte dos testes das demais fichas. QA-09 integral não está aprovado e o próximo ID continua bloqueado.

## Escopo e fotografia

QA-09 exige inventariar e recalcular o conteúdo numérico fora dos 197 artigos, incluindo fichas e demais atividades, com referências e resultados verificáveis. Este parecer cobre apenas as dez fichas identificadas, modelos e testes numéricos da entrega; a regra curricular comum não é substituída por uma revisão localizada de fichas.

Formulário `formulas/termodinamica.html` SHA-256 `01d5d79639cd17dfcaea38479019cf719e2601f5b35d446ab562e50d381fa5c9`; inventário r10 SHA-256 `3497cbf9ffcbe0a1e2eb84eeb9e34c0cf6e0ed63a2747795bf75832454e2f6c`. A [entrega do Corretor](../evidencias/QA-09/fichas-escoamento-r10-20261030/entrega.md), SHA-256 `79b6e1f8eca8c9abc24f9af60c1ee530138cbe3ef399c9f796cd2476d9846488`, documenta as âncoras, offsets e hashes de cada ficha. Li diretamente os dez cartões completos, suas condições e estrutura de 15 MathML. [Meu script independente](../evidencias/QA-09/auditoria-fichas-escoamento-r10-20261030/verificar.py), SHA-256 `bf86ce0e450708c580e5e36f66a4b99c46078a6fc0fa33c1328b841e4b7eae8c`, verificou arquivo/inventário, os dez hashes/IDs/offsets, parsing XML dos MathML e recálculos; passou sem gravação. Executei também o script read-only do Corretor. Parsing e conferência estática não demonstram renderização em navegador.

## Ajuste obrigatório — fichas 52 e 53

Os cartões especificam que as **vazões de entrada e saída** têm a mesma referência T,p e descrevem G como geração de CO₂ em m³/h ou m³/s. Eles não explicitam que a taxa volumétrica de CO₂ **G também deve ser convertida à mesma base de temperatura e pressão** da vazão de ventilação e das frações volumétricas. O texto vinculado da aula diz genericamente que vazões volumétricas são referidas às mesmas condições, o que pode abranger G; ainda assim, a hipótese não fica explícita quando o aluno consulta as fichas isoladamente. A relação está correta se as bases já forem compatíveis.

Contraste fictício com gás ideal à mesma pressão: se o volume de CO₂ gerado for informado como 0,010 m³/h a 600 K, ele corresponde a 0,005 m³/h a 300 K. Para o teste da entrega, V=300 m³, V̇=30 m³/h e Ce−Ci=−0,0002, inserir erroneamente 0,010 dá `dCi/dt=+13,333 ppm/h`; converter G para 0,005 na base do ambiente dá `−3,333 ppm/h`. Para o teste estacionário Ci−Ce=0,001, a mesma geração convertida leva a 5 m³/h, não 10 m³/h. São testes de consistência de unidade física, não medições nem um projeto de ventilação. Admitiu-se pressão igual, comportamento ideal e referência volumétrica no ambiente; com pressões diferentes, também é necessário convertê-las.

**Solicitação:** explicitar na condição de ambas as fichas que G e V̇ são vazões volumétricas referidas ao mesmo T,p compatível com o ambiente/modelo; indicar conversão quando os dados forem fornecidos em outra base. Manter a aproximação de CO₂ diluído, o volume/densidade constantes e as demais hipóteses. Preparar candidatos isolados, verificar conteúdo visível e índice de busca, reconciliação das posições/fotografia e efeito sobre FOR-01; nova auditoria deve examinar a versão efetivamente aplicada. Não afirmar que a base geral esteja ausente: ela já contém menção à referência comum.

## Demais verificações

| Fichas | Resultado independente no recorte |
|---|---|
| 47–50 | Trocador de duas correntes adiabático ao exterior: perda da quente 2×100=200 kW é ganho da fria 1×200=200 kW. Massa: 3−1=2 kg/s de acumulação. Energia transiente 20−10+2×100−1×50=160 kW; integrada 20−10+3×100−1×50=260 kJ, com entalpias constantes no intervalo. A entalpia inclui trabalho de escoamento e W exclui essa parcela. |
| 51 | Tanque inicialmente vazio e rígido, uma entrada, nenhuma saída, Q=W=0 e demais hipóteses indicadas: balanço dá m₂u₂=m_in h_in e m₂=m_in. Com gás ideal de composição fixa, cp/cv constantes e referência comum, T₂=(cp/cv)Tin=1,25×320=400 K. Não decorre de adiabaticidade isolada. |
| 52–53 | As contas 13,333 ppm/h e 10 m³/h da entrega são corretas **se** G foi dado na base volumétrica ambiente; a falta de explicitação dessa condição no cartão motivou o ajuste acima. |
| 54–56 | 600/300=2 h⁻¹ para vazão exterior; potência hidráulica 1000×9,81×0,01×20=1962 W e 1962/2616=0,75 para potência de eixo; mistura em regime permanente dá h₃=200 kJ/kg sem calor/trabalho e 210 kJ/kg com 30 kW recebidos. As referências de h devem ser coerentes, e o modelo de bomba usa carga total. |

Os valores são dados artificiais e não medições. Igualdades são exatas nos modelos nominais, exceto aproximações decimais declaradas; não foi inferida incerteza experimental.

## Fontes e decisão

Abri [MIT, primeira lei em volume de controle](https://www.ocw.mit.edu/courses/2-611-marine-power-and-propulsion-fall-2006/81d9f26805d769136b097b2cb3df9376_05first_law.pdf), [NISTIR 6729, balanço de CO₂, eq. 4](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=860846), e [DOE, manual PSAT p.17 do PDF](https://www.energy.gov/sites/default/files/2014/04/f15/psat_user_manual.pdf) para o conceito de potência ao fluido e eficiência em relação ao eixo. A URL DOE inicialmente listada pelo Corretor retornou 404 nesta ferramenta; o Corretor substituiu na entrega pela cópia PDF acessada e o hash desta versão é o informado acima. As fontes fornecem os modelos, não os números fictícios. A conversão de G ilustrada acima é uma consequência do modelo de gás ideal, não dado extraído do NIST.

| Critério localizado | Resultado |
|---|---|
| Identidade, cálculos e estrutura das dez fichas | Atendido para a versão r10 e os testes indicados. |
| Hipóteses da referência de G nas fichas 52/53 | **Não atendido:** explicitação necessária para uso isolado. |
| Fichas restantes no alcance dos testes | Sem outra divergência identificada, sem aceitar automaticamente todos os recursos. |
| QA-09 integral e liberação do próximo ID | Não atendidos; próximo ID permanece bloqueado. |

Não houve navegador real, avaliação com alunos, revisão humana ou certificação externa. A mudança de versão exige reconciliação individual de posição e impacto antes de associar este parecer a outra fotografia.
