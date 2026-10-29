# BAN-02 r2 — conferência técnica independente do delta

Data: 27/10/2026. Autor: apoio do Auditor `/root/auditor_aaa/auditoria_tecnica_ban02`.

**Não foi identificada divergência técnica na entrega r2. Este documento não aprova BAN-02 nem libera outro ID.** A suficiência semântica das listas e o parecer geral são responsabilidade do Auditor principal.

A entrega, os manifestos e o código `verificar-r2.mjs` foram lidos antes da execução. O módulo somente lê arquivos e foi importado no Node REPL; sua função `verificarR2(root)` concluiu normalmente. Todas as **18 verificações dirigidas** passaram, e o resultado é integralmente idêntico ao `verificacao-r2.json` entregue. O validador canônico retornou 190 registros/artigos, sete recursos, 1.022 referências locais, zero erros e zero avisos.

A comparação independente dos JSON r1 e r2 percorreu todos os campos, inclusive metadados de topo, e tratou listas como campos atômicos, mantendo os itens associados pelo ID. Confirmou **112 diferenças**, iguais ao delta entregue: **83 listas de pré-requisitos (80 AV e três CR)** e **29 outros campos**. IDs e ordem foram preservados. Esta comparação confirma rastreabilidade e escopo material; não decide a qualidade científica dos valores alterados.

Foram recalculados e comparados os hashes das **22 evidências r1** enumeradas no manifesto original: todas permanecem intactas. As **15 entradas do manifesto r2** também conferem. As cinco cópias em `pacote-r2/` são idênticas aos respectivos arquivos canônicos. As cinco cópias de `pacote-r1/` conservam seus hashes registrados.

Schema, validador e guia mantêm os hashes já auditados na r1. Os quatro arquivos de produto também conferem com a evidência independente anterior. Por isso, os 56 testes de infraestrutura da r1 **não foram repetidos** nesta rodada.

| Artefato | SHA-256 |
|---|---|
| Inventário canônico r2 | `d17e2fcf73f2dbbe72005fb70ee6b36d1cad60ef90a1618abaf080d8bfd79507` |
| Resumo legível r2 | `2d82fbde8502a1f5096373f10cf0c57d2c23e7730f3a134dc2d0d7755e4b7590` |
| Schema preservado | `c71033464d54e71e61d4dcbae56847a88720e5ff937c1e1f7179005ab22d149b` |
| Validador preservado | `ddc8a6831422a868fb5a8b15b2f6653325f6644acf4f5c64dbf35bb0d2369fdd` |
| Guia preservado | `cdcd7e965bdc4a998b6e2fa784a53f84f295abcf9ade2d06ce62fff71d072449` |
| HTML do produto preservado | `b4e2d672c6feecb4289ad73bb9c16000ff5156720698f10153ff93fa0b788a8e` |
| Módulo dirigido r2 executado | `096e5064794a58b52cdcb543a3292714c4302bf77fe7350621ff23cfa992e8e6` |

As diferenças reais, cada hash conferido, a comparação dos pacotes e a saída reexecutada estão em [BAN-02-r2-tecnico-evidencias.json](BAN-02-r2-tecnico-evidencias.json). Nenhum arquivo da entrega, produto, controle ou evidência do Corretor foi modificado por este apoio.

Esta rodada não repete a análise pedagógica das 80 listas, não confere PDFs externos, não audita gabaritos e não testa navegador. A passagem das verificações dirigidas não substitui a decisão semântica independente.
