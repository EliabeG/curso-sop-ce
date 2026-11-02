# QA-09 — auditoria independente de referências de energia e FUN-02

Data: 30/10/2026. Auditor automatizado `/root/next_formulas`; Corretor automatizado `/root/reference_triage`. **Veredito localizado: AJUSTES OBRIGATÓRIOS na apresentação da referência 156.** A identidade dos 20 vínculos e o recorte dos demais acessos conferem como descrito abaixo. QA-09 integral permanece aberto e o próximo ID não está liberado.

## Fotografia e identidade

Examinei os índices de referência 141–160 de `inventario-r12.json`, SHA-256 `457a56300aab8f612ebb7f136c7c2f62520abb49c005c209a238925179248d0e`, e a fotografia posterior r13 (`inventario-r13.json`, SHA-256 `0df99b79bcc2350581fcdded72435d30d07858de237a549e6228ca73682f8d9b`). A aula r12 preservada em `aplicacao-energyplus-fichas-r13-r1/resultado/antes-aula.html` tem SHA-256 `f76c39a3e1d8c349ebf0df72cc20a3ab21c68960c8451799bad90a9dcc4bd8c7`; a aula r13 efetiva tem SHA-256 `f19000a7ddb1f3552b9633b0efec266fb3f6c5e5065808505a2f65b2005aefbc`.

[Entrega do Corretor](../evidencias/QA-09/referencias-fun02-r12-20261030/entrega.md) SHA-256 `0267a1f9786f84af696ef641917747d88e8af1722497e63288d348181b95de45`; `identidades.json` SHA-256 `44cd236030f06a4e6a0c4459385c61c1f3f50cc651a24643c156e6532d13949f`; `verificar.mjs` SHA-256 `64c8e9ad130d0ef93ef78663e9c92a2a801bff074b29367ca4cb1f16b318bae4`. Executei o verificador após exame de sua ausência de escrita e obtive `ok=true`. Também reconstruí independentemente em Python os fragmentos por offsets UTF-16 nas duas páginas e comparei todos os metadados do índice 141–160: hashes e campos coincidem; 11 destinos locais existem uma vez. São referências sobrepostas a outros elementos, não 20 cálculos ou porcentagem de QA-09.

## Referência 156 — generalização de expansão adiabática

O vínculo atual aparece na seção `fun02-processos`, posição UTF-16 245970–246174 e SHA-256 `e43eea573dc5d5cb3c0211609bb12ab5ed1450ef6237651d7c41cbc77b1ace95`. Ele acompanha a afirmação correta de que duas transformações adiabáticas com os mesmos estados e o mesmo balanço fechado simplificado podem ter o mesmo trabalho sem que trabalho seja propriedade. O texto ao redor da ligação **não informa que a página externa tem uma generalização não universal**.

A página [OpenStax, University Physics 2, §3.4](https://openstax.org/books/university-physics-volume-2/pages/3-4-thermodynamic-processes) foi acessada em 30/10/2026. Na subseção adiabática, ela diz em termos gerais que uma expansão deve realizar trabalho e reduzir a temperatura, e sua figura adjacente exemplifica um pistão isolado. A figura ilustra expansão com trabalho resistente, mas a frase textual é mais ampla do que essa situação: uma expansão adiabática não precisa realizar trabalho externo nem reduzir T.

Contramodelo: gás ideal de composição e massa fixas expandindo livremente para vácuo em recipiente externo fechado, rígido e isolado, sem outros trabalhos e com ΔEc/ΔEp desprezíveis. Entre estados inicial e final de equilíbrio, Q=W=ΔU=0; como u depende apenas de T, T₂=T₁. A página primária [MIT, comparação entre expansão livre e isotérmica reversível](https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node33.html), seção 4.2, expõe esse caso. Não se conclui daí que uma expansão adiabática contra pistão não possa realizar trabalho nem resfriar o gás.

**Ajuste obrigatório:** contextualizar no próprio local do link que a frase da fonte sobre expansão e queda de temperatura vale para o exemplo com trabalho resistente e não para toda expansão adiabática, e oferecer o contraponto MIT; alternativamente, substituir esse vínculo por fonte primária adequada ao argumento, preservando registro da procedência no histórico. Submeter candidata isolada a Auditor antes da aplicação e, em seguida, reavaliar a versão efetiva, os vínculos, os inventários e o alcance de FUN-02. Não alterar transcrições ou gabaritos oficiais. A ressalva científica deve alcançar o leitor da aula, não ficar somente no relatório interno.

## Demais vínculos e limites da consulta

Abri as fontes indicadas para energia cinética clássica e potencial gravitacional próximo da Terra, o apêndice de diferenciais da University of Washington, a seção de campos conservativos do OpenStax, a primeira lei do MIT e a seção de entropia do OpenStax. O primeiro material assume mecânica não relativística e referencial; o segundo exige modelo gravitacional apropriado; o teste de exatidão precisa das condições de continuidade e domínio aplicáveis e não segue de igualdade de derivadas em um único ponto. Os materiais apoiam conceitos nos contextos indicados, não comprovam automaticamente as atividades ou números que os usam. Algumas expressões da página MIT são imagens; esta etapa não valida toda a sua renderização.

| Critério localizado | Decisão |
|---|---|
| Identidade de 20 referências nas fotografias r12/r13 | Atendida para metadados, posições e hashes dos elementos examinados. |
| 11 destinos locais | Existem uma vez em r13, verificação estática. |
| Conteúdo e alcance das fontes não afetadas | Conferidos tematicamente nos limites acima; não substituem QA científico de todas as atividades. |
| Referência 156 e afirmação de expansão adiabática | Não atendido para leitura autônoma: exige contexto/correção indicada. |
| Aplicação, FUN-02 e QA-09 completo | Pendentes; outros itens e próxima ID permanecem bloqueados. |

Não houve teste em navegador, leitor de tela, revisão humana, teste com estudantes ou certificação externa. Links externos podem mudar; esta consulta não é investigação de licença ou certificação de disponibilidade futura.
