# QA-09 — ledger parcial r18, revisão 1

30/10/2026. Autor `/root/planning`. **Integração pendente de auditoria independente.** Este ledger revalida individualmente os 18 objetos de r17: EX001–005, D26–28 e D11–20. A [reconciliação](reconciliacao-18-r17-r18.md) registra contas, hipóteses, vínculos, os efeitos das quatro alterações e os limites. O ledger r17 e seu parecer permanecem preservados. A revisão não transfere automaticamente aceites por hash ou correspondência.

O estado padrão de ocorrências, referências, recursos e ativos é `pendente_de_integracao`; somente os 18 blocos explicitamente listados têm estado localizado proposto, sem aprovar seus pais, descendentes, fontes ou bases. Os totais são 11.400 ocorrências, 816 referências, 138 relações de recursos e seis ativos; sobrepõem-se e não são percentual de conclusão ou contagem de cálculos. Pendência não apaga revisões históricas. Os 197 artigos têm tratamento separado e QA-09 permanece em correção.

## Reprodução sem escrita

```sh
node auditoria/termodinamica/evidencias/QA-09/ledger-r18-parcial-r1/ledger.mjs --verificar auditoria/termodinamica/evidencias/QA-09/ledger-r18-parcial-r1/ledger.json
```

Sem argumentos o programa emite JSON em stdout; com `--verificar` compara a fotografia salva. Fixa hashes das fotos, inventários, pareceres e parser, reextrai 18 blocos, confronta 23 contextos e links, e recalcula valores selecionados. Não lê fontes remotas nem valida a ciência por si: o relatório explica a revisão e os pareceres que a fundamentam. Verificação positiva e teste negativo de alteração de estado passaram. Mudanças na base exigem nova fotografia e reavaliação. Não foram feitos navegador real, teste com alunos, revisão humana ou certificação externa.
