# QA-09 — auditoria independente do ledger parcial r7

Data: 30/10/2026. Revisor: agente automatizado independente `/root/qa_diagnosticos`. Veredito: **APROVADO para uso como registro parcial de acompanhamento na fotografia identificada e dentro dos limites abaixo**. A estrutura não conclui QA-09 e não libera outro ID.

## Critério e escopo

O requisito QA-09 exige levantamento e recálculo individual do conteúdo numérico, inclusive explicações e figuras, com referência e resultado verificáveis. Esta auditoria verifica integridade, rastreabilidade e sentido dos 12 registros explicitamente integrados ao ledger esparso; não recalculei novamente os 12 exemplos nem examinei a qualidade integral dos respectivos pareceres. As regras curriculares gerais não são satisfeitas por esta ferramenta de acompanhamento.

Fotografia: HTML `modulos/e1-termodinamica.html` SHA-256 `200f9b773050594d762cc596a5a89297024b245fc4f504081fc77baaed3db95f`; formulário `formulas/termodinamica.html` `c27422b409a0a755448982c4074c6d6967fd3e91d7eae20274e218530f5c37b0`; inventário r7 `5090b9897a4698e0ad090f45182afba5880361aabc9fd3c3bdf848d971a85a1a`. Arquivos examinados: `auditoria/termodinamica/evidencias/QA-09/ledger-r7-parcial-r1/LEIA-ME.md` SHA-256 `9800c8a0f396e4e01b4c2a5fa562afc28601c68c6dd673b653cc533b989008af`; `ledger.py` `73f414972adfcc8eb796e156cbb19396d0dcd871399be91f5f03d986a327e2a7`; `ledger.json` `1b0f3faaefb646103bc35b217494e1b46186012b56eaabc8c7f9e47f11dad463`.

## Verificações independentes

- Inspecionei o gerador antes da execução: ele lê fotografias e pareceres, escreve somente em stdout e rejeita hash divergente; não regrava inventário ou evidências. O comando documentado `python3 auditoria/termodinamica/evidencias/QA-09/ledger-r7-parcial-r1/ledger.py --verificar auditoria/termodinamica/evidencias/QA-09/ledger-r7-parcial-r1/ledger.json` retornou `ok=true` e 12 registros.
- Em conferência adicional por script de leitura, confrontei os 12 índices base zero únicos contra r7, ID, documento, seção, âncora, posições, hash do fragmento UTF-16 extraído do HTML e hash do parecer de cada linha. Todos conferiram. Os dois pareceres vinculados delimitam o alcance à aplicação de EX-011/013 e ao recálculo de EX-021–030, respectivamente; a classificação do ledger remete a esses escopos e não afirma aprovação do curso.
- Contagens diretamente no r7: 11.396 ocorrências, 815 referências, 138 registros de recursos, seis ativos específicos e 197 artigos segregados. São coleções sobrepostas, não 12.355 cálculos nem porcentagem de conclusão. Valores sem registro no ledger são pendentes **de integração ao ledger**, o que não significa ausência de revisão histórica.
- Em cópia temporária das entradas, o verificador passou na versão original, rejeitou o HTML com um espaço acrescentado e rejeitou alteração de estado em `ledger.json` (código 1 nos dois casos). Essas provas não modificaram o repositório. Demonstram apenas as duas rejeições testadas, não robustez universal contra todo tipo de adulteração.
- A omissão de nós filhos, pais, referências, recursos e ativos nas linhas aprovadas impede transferência automática por sobreposição. O ledger não integra ainda diagnósticos, figuras, fichas e outros lotes posteriormente revisados; eles continuam pendentes de integração, embora pareceres possam existir. Diante de qualquer modificação do HTML prevista para o ajuste de percentual, o script deliberadamente recusará a fotografia: será preciso gerar nova fotografia e reconciliar cada identidade e dependência em vez de modificar o histórico.

| Critério localizado | Decisão |
|---|---|
| Hash e identidade da fotografia e dos 12 registros | Atendido para os arquivos e pareceres identificados. |
| Reprodutibilidade sem regravar evidências | Atendido pelo comando e testes em cópias, no ambiente examinado. |
| Regra conservadora, limites, segregação e não transferência | Atendido; contagens não representam cálculos ou progresso. |
| Cobertura do inventário e mérito científico integral | Não atendido nem alegado; revisão e integração restantes continuam abertas. |
| Critério integral QA-09 e próximo ID | Não atendido; sem liberação. |

Nenhum ensaio em navegador, revisão humana, validação com estudantes ou certificação externa foi realizado. Uma versão futura do ledger ou da fonte requer revisão de impacto, mesmo que parte dos fragmentos permaneça igual.
