# FON-02 r2 — correção documental de R1-A

Data: 28/10/2026. Entrega congelada do Corretor para reauditoria.

**R1-A — correção implementada:** os 80 arrays de vínculos antecedentes foram reconstruídos a partir das âncoras reais do HTML anterior às alterações FON-02. A regex da r1 restringia destinos internos e atravessava fechamentos de âncoras; o novo extrator usa os limites estruturais de cada elemento. A correção recupera 158 ocorrências, sendo 141 internas e 17 externas, com destino, texto e ordem preservados. Não há deduplicação.

A [matriz r2](../evidencias/FON-02/revisao-suplementos-80-r2.json) muda somente registros[].fontes.ensino_e_fundamentos_ja_vinculados. Todos os demais campos são idênticos à r1, inclusive seus metadados de rodada científica; a presente reapresentação documental é identificada como r2 no delta, no resumo, no manifesto e nesta entrega. As fontes acrescentadas/reconfirmadas na r1 continuam separadas em seus campos e no catálogo preservado. O [novo resumo](../evidencias/FON-02/REVISAO_SUPLEMENTOS_80-r2.md) expõe os vínculos individualmente.

**O1:** os hashes abaixo foram obtidos diretamente dos arquivos e impressos em 64 caracteres contíguos. A tabela histórica r1 não foi reescrita.

## Comparação independente e preservação

O [extrator Node](../evidencias/FON-02/reconstruir-vinculos-r2.mjs) usa o parser HTML existente. O [comparador Python](../evidencias/FON-02/comparar-vinculos-r2.py) usa HTMLParser da biblioteca padrão e não importa o extrator Node. A [saída independente](../evidencias/FON-02/comparacao-vinculos-r2.json) passou 87 verificações: todos os 80 itens e 158 vínculos foram comparados por href/texto/ordem; todos os demais campos da matriz e os 55 arquivos do manifesto r1 permanecem idênticos. O [delta completo](../evidencias/FON-02/delta-r2.json) registra antes/depois dos 80 arrays e a regra de seleção. O [confronto do coordenador](../evidencias/FON-02/confronto-vinculos-coordenador-r2.json), com esperado extraído antes de ler a r2, confirma os mesmos resultados e é atribuído como apoio separado.

HTML, inventário, resumo canônico, fontes novas, nove cópias e todas as evidências r1 permanecem intactos. Ciência, navegação e validação canônica são herdadas por identidade, conforme permitido pelo [parecer r1](../pareceres/FON-02-r1.md); não foram repetidas nem apresentadas como novas. O [manifesto r2](../evidencias/FON-02/manifesto-r2.json) inclui cinco cópias finais e as referências imutáveis pertinentes.

| Arquivo | SHA-256 |
|---|---|
| Matriz r2 | 4401889a58d96cad02ed12c703e180a645bf47b428fe4959d2decba5d8e2d9d1 |
| Resumo de vínculos r2 | 81b610407bc2c04a187878d04013e6d42c93ca517158e5c8c82cca2d7986eda2 |
| HTML preservado | 0fc12a96fd30d366770a56c366fb61bc6a9fa7bd761e81fb40242a30f6dd78c7 |
| Inventário preservado | 0faacb0d84482e53afae1f8e481ce676f0e68e793376a9d4ad35a4aa6a93af8e |
| Resumo canônico preservado | 4c0b477b9479c6c546507535a194bb75805b2adf1bceaaa34337a20d02e3294e |
| Fontes novas r1 preservadas | 9f03b7bbde7f057a52fce320e54d8b4d57178af8ceea928cdcf235a760693ef8 |
| Comparação independente | 091bde1da79de0c8c2259e1d573881d80548d684cd5d429dd0b423abd53b393d |

Não houve edição de controles, checklist, produto ou outro ID. A entrega aguarda decisão independente do Auditor.
