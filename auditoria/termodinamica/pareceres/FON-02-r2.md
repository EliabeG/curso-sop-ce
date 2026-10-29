# Parecer FON-02 — rodada 2

**APROVADO. R1-A atendido integralmente; nenhum ajuste obrigatório restante.** Auditor: agente automatizado independente /root/auditor_aaa. Data: 28/10/2026. O gate de FON-02 está liberado para o coordenador selecionar a próxima correção. Este parecer não inicia outro ID.

A reauditoria examinou a reapresentação documental congelada, conforme o [parecer r1](FON-02-r1.md). As 80 listas corrigidas foram comparadas com as âncoras que a auditoria independente havia extraído e salvo antes da r2. Todas as 158 ocorrências — 141 internas e 17 externas — coincidem em destino, texto próprio e ordem, sem deduplicação. Os rótulos deixaram de incorporar texto externo às âncoras e os 78 vínculos antes omitidos foram recuperados. A separação entre fontes antecedentes e fontes acrescentadas na r1 permanece explícita. [Comparação integral](FON-02-r2-comparacao.json).

O Auditor reproduziu o comparador HTMLParser com Python 3.15.0: **87 verificações atendidas**, saída byte a byte idêntica à entregue. Apenas o diretório de leitura e o destino da saída foram adaptados para preservar o pacote congelado; parser e verificações permaneceram intactos. [Código de reprodução](FON-02-r2-reproduzir.py) e [resultado](FON-02-r2-python-reproduzido.json).

O [apoio técnico independente](FON-02-r2-tecnico.md), de /root/auditor_aaa/tecnica_fon01, concluiu 351 verificações sem falhas. Foram conferidos 19 registros de arquivos e cinco cópias r2, 55 arquivos e nove cópias r1. Somente os 80 arrays autorizados mudaram na matriz; ao repor esses campos, recupera-se integralmente a matriz anterior. Os três produtos e o catálogo de fontes novas são idênticos à r1. O marcador rodada1 do conteúdo científico foi preservado deliberadamente, e a rodada2 documental está identificada na entrega, delta, resumo e manifesto.

| Critério | Decisão |
|---|---|
| Identificação e justificação individual dos suplementos dos 80 CR | Atendido; herdado do exame científico r1, com identidade demonstrada. |
| Separação entre original, derivação, hipótese e comentário autoral | Atendido; produto r1 integralmente preservado. |
| Fidelidade e cobertura do índice antecedente, R1-A | Atendido nesta rodada, 80/80 listas e 158/158 ocorrências. |
| Coerência dos documentos derivados | Atendido:80 blocos/158 vínculos no Markdown;154 links locais resolvem. |
| Hashes legíveis, O1 | Atendido: sete hashes da nova entrega têm 64 caracteres contíguos e correspondem aos arquivos. |
| Preservação, escopo e reprodução | Atendido pelos confrontos integrais e testes registrados. |
| Inventário, identidade das respostas, pontuação e navegador | Herdados por identidade: canônico 197/29/1236 e 71+9 preservados; nenhum novo teste de navegador alegado. |

Versões aprovadas, reconferidas pelo Auditor:

| Arquivo | SHA-256 |
|---|---|
| Entrega FON-02-r2.md | 8b08a9e53b9478961484e33bd44a3d52ef66626ee08f8cc0013ad24ab1e8f256 |
| Manifesto r2 | da44635be39e5fac7151fac8f6975c0b42b70de8ad3ce15f3559c8b6de48391d |
| revisao-suplementos-80-r2.json | 4401889a58d96cad02ed12c703e180a645bf47b428fe4959d2decba5d8e2d9d1 |
| REVISAO_SUPLEMENTOS_80-r2.md | 81b610407bc2c04a187878d04013e6d42c93ca517158e5c8c82cca2d7986eda2 |
| modulos/e1-termodinamica.html | 0fc12a96fd30d366770a56c366fb61bc6a9fa7bd761e81fb40242a30f6dd78c7 |
| inventario-questoes.json | 0faacb0d84482e53afae1f8e481ce676f0e68e793376a9d4ad35a4aa6a93af8e |
| INVENTARIO_QUESTOES.md | 4c0b477b9479c6c546507535a194bb75805b2adf1bceaaa34337a20d02e3294e |

A [decisão estruturada](FON-02-r2-evidencias.json) reúne critérios e identidades. A ciência dos 80 CR, suas fontes e os testes de produto intactos não foram repetidos; a herança corresponde ao alcance efetivamente aprovado na r1, sem ampliar a atribuição do navegador do coordenador. O aceite encerra exclusivamente FON-02. Não aprova BAN-07/BAN-08 ou outros IDs e não certifica o curso inteiro como avançado. Produto, controles, checklist e pacotes autorais não foram alterados pelo Auditor.
