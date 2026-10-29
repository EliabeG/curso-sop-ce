# BAN-07 — parecer independente da rodada 3

Data: 29/10/2026. Auditor: agente automatizado `/root/auditoria_av71_80`, independente do Corretor `/root/inspect_repo`. **Veredito: APROVADO para BAN-07 r3, nos arquivos e no alcance identificados abaixo.** O ajuste R2-A foi atendido e não há pendência obrigatória identificada neste ID e versão. Este parecer não libera outro ID; a coordenação conserva a decisão de fila e as restrições do mandato vigente.

## Critério e versão

BAN-07 exige conferir dados suficientes, consistência física, comando, unidades, restrições e resposta única, com distratores plausíveis baseados em erros reais; o aceite exige demonstração do gabarito e justificativa dos distratores, inclusive equivalências após arredondamento. Em estudos críticos sem nota, a revisão separa texto e chave oficiais da análise técnica, sem exigir uma resposta física unívoca quando ela não existe. Os problemas abertos são avaliados pela família de soluções e condições da rubrica, não por uma trajetória única. A plausibilidade de distratores é teórica, sem frequência observada em alunos.

[Entrega r3](../entregas/BAN-07-r3.md), SHA-256 `cd4ffc56d53f8c0a0ba429e1162c88ec10faead9bed82600a875076b5cdd95c1`; [manifesto r3](../evidencias/BAN-07/manifesto-r3.json), SHA-256 `04c677c6bd5472e65c2ba381549461df3412d6a43313721ca4caf2c071526b3b`. Conferi as 15 entradas enumeradas no manifesto, sem ausência ou divergência de hash.

| Arquivo | SHA-256 examinado |
|---|---|
| `modulos/e1-termodinamica.html` | `80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0` |
| `auditoria/termodinamica/inventario/inventario-questoes.json` | `486c53c5aa6c432831599c4eca170e4620d089b4eb15b480dbfb2cbfaf54c9ce` |
| `auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md` | `35df191e2f7964adfb7b975668491e8ba39d983a5df93640a35d3d96ae142df8` |
| `auditoria/termodinamica/evidencias/BAN-07/e1-termodinamica.r2.html` | `80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0` |
| `assets/curso.js` | `a20f4d19158073a9a1c48aabdfba8fa863b02063e16061c00b16448a6ccc2e13` |
| `assets/registro.js` | `46da94527d6639fe0265bd766286f1ef39623966105e00bda3b31f21ca2c247c` |

## R2-A e preservação

Comparei recursivamente o JSON aplicado com o [backup r2](../evidencias/BAN-07/aplicacao-r3/inventario-r2-antes.json), SHA-256 `71ac07e042aa65675fc3d4b69d8d0ae11cb66df967d45e66b1a88f4f1350e074`. Existem exatamente duas diferenças, ambas em `cr-e1-06`: `raciocinio.etapas[0]` e `vinculo_competencias.alcance` agora reconhecem a relação afim **quando ambas as escalas são lineares na altura da coluna, conforme hipótese editorial do curso**. Não atribuem essa condição à prova. As demais entradas e campos, incluindo os outros 196 registros, permanecem iguais.

O artigo exige reconhecer a relação no modelo já fornecido, sem calcular coeficientes; categoria `reconhecimento`, uma etapa, nível estimado iniciante e apoio parcial C08 continuam coerentes. `hipoteses.explicitadas`, justificativa do nível e linha Markdown já identificavam o suplemento editorial e continuam concordantes. **R2-A atendido.**

O HTML atual e o snapshot r2 são byte a byte idênticos. Essa identidade preserva os seis artigos científicos examinados na r2, seus suplementos, alternativas, comentários e chaves; os arquivos JS, os complementos de FON-01/02 e BAN-10 e o resumo Markdown também mantêm seus hashes examinados na r2. Em execução própria do validador canônico no produto atual, obtive **197 registros e artigos, 29 recursos, 1.261 links locais, zero erros e avisos**. O validador confere estrutura e rastreabilidade declaradas, não substitui o exame semântico ou o julgamento científico.

## Cobertura científica dos 197 e decisões afetadas

O [parecer r2](BAN-07-r2.md), SHA-256 `06ee05437bf9b834ba6936b269c44b30da9f265fc51b73b24ee1beaa5b65cd2f`, contém a revisão científica dos seis artigos aplicados: AV04, AV31 e AV62 com cinco alternativas cada; CR06, CR26 e CR45 com as duas marcações e hipóteses editoriais prévias. Foram demonstrados D, E, D e, sob os modelos suplementados, C, E, C, respectivamente. A r3 conserva esses artigos por identidade. Não se atribuem as hipóteses à banca nem se declara anulada qualquer chave oficial.

Na r2, a comparação direta com r1 confirmou 197 IDs e somente esses seis artigos alterados; os demais 191 e o conteúdo fora dos artigos eram idênticos. O [adendo de cobertura r1](BAN-07-r1-adendo-cobertura.md) associa os 197 itens às revisões locais e adjudicações, incluindo 30 Q, 80 CR, 80 AV e sete FUN. A ciência dos 191 é herdada por identidade e escopo, com autoria e limites das peças originais; não reivindico repetir suas soluções nesta rodada. As decisões de CR25 e os dissensos AV41/AV69 permanecem fundamentados nas peças citadas pelo adendo.

Os nove estudos críticos CR04/09/24/34/35/39/62/79/80 permanecem identificados e não pontuáveis no desenho examinado; suas marcações servem à comparação documental e não provam validade física universal. CR06/26/45 são pontuáveis **nas versões com hipóteses editoriais**. Esta decisão é limitada à qualidade dos itens e modelos avaliados, não é validação empírica da dificuldade, prova de domínio ou conclusão de BAN-08.

## Impacto nos aceites anteriores

**FON-01:** na r2, a retirada dos três suplementos reconstruiu cada artigo anterior integralmente, e o parecer técnico conferiu identidade de PDFs/figuras e vínculos documentais afetados. O HTML r3 é o mesmo. Reutiliza-se a conferência oficial anterior no alcance dessas partes preservadas; não foi realizada nova pesquisa integral de documentos ou atos.

**FON-02:** o complemento r2 documenta separadamente os três suplementos editoriais, suas condições, posição e identidade; os 80 registros históricos foram confrontados com as três adições isoladas. O parecer r2 revalidou esse alcance e a r3 preserva HTML e complemento. Isto não reescreve nem constitui novo aceite global de FON-02.

**BAN-10:** a triagem complementar r2 registra as três decisões CR06/26/45, preserva a motivação histórica e distingue uso pontuável sob os modelos editoriais. O parecer r2 revalidou cientificamente essa decisão localizada; a r3 preserva artigo e complemento. As demais decisões são herdadas com seus limites e autores, não por transformar a cópia de uma triagem histórica em nova auditoria integral.

**BAN-02:** o registro CR06 agora reflete coerentemente a hipótese editorial no raciocínio e no vínculo C08. Os outros campos e registros não mudaram nesta rodada, e as revisões dos seis itens e representações foram feitas na r2, ressalvado R2-A agora atendido. A revalidação localizada é da versão do inventário examinada; não certifica a competência avançada nem a aprendizagem dos estudantes.

## Apoio técnico e limitações

Li [BAN-07-r3-tecnico-independente.md](BAN-07-r3-tecnico-independente.md), SHA-256 `6480625293498a8798a540a0f2a7394c635f67e60244b70a8179a6ba8da60c60`, e confirmei seu hash. O trabalho pertence à revisora automatizada `/root/auditoria_av61_70`, independente do Corretor: conferiu 15 entradas do manifesto, comparou os JSONs e reverteu em memória os dois campos até restaurar byte a byte o backup r2, examinou a linha Markdown e executou o validador. Sua conclusão de R2-A atendido coincide com minha comparação e julgamento próprios.

O Corretor relatou falha na primeira aplicação e restauração do inventário antes da segunda execução. O apoio leu o código atual e conferiu backup e estado final, mas não observou independentemente o instante da falha ou a restauração; o relato permanece atribuído ao Corretor. O estado final e o delta são verificáveis pelos bytes e hashes atuais.

Os testes controlados r2 de digitais, histórico e um estudo crítico foram executados com funções de produto e DOM/armazenamento simulados, e reproduzidos por apoio técnico na r2. Sua aplicabilidade é herdada na extensão pertinente porque HTML e código de banco permanecem idênticos; não foram reexecutados por mim nesta rodada. Não são testes de navegador real nesta versão, de todos os históricos pessoais, falha de gravação, leitor de tela, alunos ou psicometria. Observações de descrições alternativas e papel de figuras continuam para UX-04/BAN-09; este parecer não encerra esses IDs.

## Quadro de aceite

| Critério | Resultado |
|---|---|
| Comandos, dados, unidades, restrições e consistência | Atendido na cobertura individual dos 197, com seis artigos r2 diretamente examinados e 191 herdados por identidade e alcance. |
| Demonstração, resposta e distratores | Atendido no formato de cada item; análises individuais e dissensos atribuídos. Nove estudos críticos permanecem sem nota; sete abertos admitem famílias de resposta. |
| Equivalências e cálculos necessários | Atendido no alcance BAN-07 dos pareceres; não substitui a auditoria numérica integral BAN-08. |
| R2-A e inventário afetado | Atendido: os dois campos de CR06 expressam a condição editorial; dados restantes preservados e validador passou. |
| Fonte oficial e suplementos afetados | Atendido no alcance localizado: conteúdo oficial preservado por reconstrução; três suplementos e suas fontes/autoria distinguidos. |
| Decisões de uso e pontuação | Atendidas no alcance BAN-10 afetado, com nove críticos preservados e três CR pontuáveis somente sob suplementos. Testes dinâmicos herdados com as limitações declaradas. |
| Integridade, autoria e evidência | Atendido para os arquivos versionados e as verificações discriminadas; relato de rollback e testes alheios corretamente atribuídos. |
| Requisitos curriculares novos de §3.2 | Não aplicáveis artificialmente à revisão deste banco existente; este aceite não declara nova unidade ou competência curricular integral. |

**Decisão:** `APROVADO` para BAN-07 r3, restrito aos arquivos, hipóteses e evidências acima. Nenhuma pendência obrigatória identificada neste ID e versão. Não houve teste com estudantes, psicometria, revisão humana, certificação externa, auditoria integral de acessibilidade ou fechamento de BAN-08. Produto, controle e checklist não foram alterados por este Auditor. **O próximo ID não foi liberado por este parecer.**
