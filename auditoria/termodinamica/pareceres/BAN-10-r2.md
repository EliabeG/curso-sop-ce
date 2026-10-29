# BAN-10 r2 — parecer independente

**Veredito: APROVADO.** Data: 28/10/2026. Auditor: agente automatizado independente `/root/auditor_aaa`. O único ajuste obrigatório R1-A foi atendido; não restam pendências neste ID e versão.

## Escopo e versão

Reauditoria restrita de CR34, seus derivados e preservação dos critérios já atendidos no [parecer r1](BAN-10-r1.md). BAN-10 exige separar documento/chave oficiais de interpretação e suplemento, pesquisar ambiguidades e impedir que uma medida inválida componha a nota de domínio. O mérito dos demais casos e a cobertura dos 197 itens permanecem fundamentados na [matriz r1](BAN-10-r1-cientifico.json), mediante identidade confirmada.

[Entrega congelada](../entregas/BAN-10-r2.md) · [manifesto r2](../evidencias/BAN-10/manifesto-r2.json).

| Arquivo | SHA-256 examinado |
| --- | --- |
| Manifesto r2 | `9e7acb7fc3b6a3a8870aa7822d3ad97b947b93770dc4ccdc325cf10759b2dc95` |
| modulos/e1-termodinamica.html | `843e16728129811b00a873fdbd42b7233e60bc41afe051a9c87a79d6a2956a14` |
| inventario/inventario-questoes.json | `8703e30d4dba156b83178a4b60f29f39fbdd6a75917b38b95cab0ffc1545a3d1` |
| inventario/INVENTARIO_QUESTOES.md | `b68f4f29ee9aa19753abb41c70d8052df6625cc0222072be08260fc15eeb9745` |
| assets/curso.js, preservado | `6a450cbfb7049b22e999e3390238fec511c2da24caa3e228871c5a3128121de6` |

## Resultado por critério

| Critério | Resultado |
| --- | --- |
| R1-A: igualdade, sinal e necessidade | **Atendido.** O original afirma ΔU>0. A análise deriva ΔU=Q se e somente se W+ΔEc+ΔEp=0 no balanço adotado e classifica cada parcela nula como condição suficiente. Retirada a inferência de que outro trabalho, sozinho, invalida C. |
| R1-A: admissibilidade física | **Atendido.** Massa/composição fixas, gás ideal simples, equilíbrios no mesmo volume, cv(T)>0 e calor exclusivamente entrante não nulo a Tb finitas positivas estão explícitos. Balanço de entropia e relação de estado fundamentam ΔS>0 ⇒ T₂>T₁ ⇒ ΔU>0, sem exigir W=0 ou caminho reversível. Tb não é confundida com temperatura uniforme do gás. |
| Decisão editorial e ensino | **Atendido.** C é reconhecida como coerente na leitura usual. CR34 permanece sem pontuação como esclarecimento pedagógico, sem alegação de invalidade ou anulação. Roteiro, análise e autocorreção fazem a distinção solicitada. |
| Metadados e representações | **Atendido.** C03/C04, três etapas e nível intermediário guiado correspondem à tarefa. Pré-requisitos/limites foram ajustados. Decisão, triagem e resumo corrigem a justificativa anterior. Recontagem independente: 169 iniciantes, 24 intermediários e quatro avançados locais; não é classificação do curso. |
| Cobertura, fontes e outras decisões | **Atendido por preservação.** As outras 196 entradas de triagem/registros e onze decisões são idênticas. Fontes oficiais, chaves e demais critérios científicos da r1 não foram reabertos sem motivo. |
| Exclusão da pontuação e continuidade | **Atendido por preservação.** JS, texto oficial, alternativas, chave, digitais e nove marcadores críticos intactos; permanecem 71 itens CR pontuáveis e nove marcações documentais. Os testes funcionais r1 continuam aplicáveis. |
| Integridade, escopo e reprodução | **Atendido.** Uma substituição de CR34 reconstrói integralmente o HTML. Os 19 campos alterados do inventário correspondem a 14 de CR34 e cinco globais; resumo conferido literalmente. Pacote, evidências, entrega e parecer r1 preservados. |

A [evidência científica r2](BAN-10-r2-cientifico.json) registra a releitura integral de CR34 e derivados, as comparações próprias e as fontes MIT já consultadas em r1. A [subauditoria técnica r2](BAN-10-r2-tecnico.json), executada por apoio independente com importação limpa, reproduziu **99/99 verificações** e o resultado canônico **197 artigos/registros, 29 recursos, 1.166 links, sem erros ou avisos**. Foram conferidas 26 entradas do manifesto e nove cópias. Não foi repetida a suíte de infraestrutura intacta.

O [navegador do coordenador](../evidencias/BAN-10/navegador-coordenador-r2.md) registra leitura de nota, roteiro, análise, integrais e autocorreção na versão final, com contadores 0/71 e 0/9 e sem novas respostas. Essa execução pertence ao coordenador, não ao Auditor. Não houve piloto, teste móvel ou auditoria integral de acessibilidade.

## Decisão

**BAN-10 r2 APROVADO. Liberação do próximo ID: sim, mediante seleção e registro pelo coordenador.** Nenhuma outra correção foi iniciada por este Auditor. BAN-07, BAN-08, FON-01 e demais IDs não recebem aceite por extensão; esta aprovação não certifica domínio dos alunos nem classifica o curso inteiro como avançado.
