# QA-09 — ledger parcial r21, revisão 1

30/10/2026. Autor `/root/planning`. **Pendente de auditor independente desta integração.** Reconcilia os 18 objetos EX001–005, D26–28 e D11–20 auditados em r20. A [reconciliação](reconciliacao-18-r20-r21.md) registra recálculos e limites, efeitos dos dois deltas r21 e, em particular, o contexto `#base-geracao-face` alterado pelo EX046 e ligado ao D14. O ledger r20 e seus pareceres são preservados; o gerador r20 foi reproduzido em cópia dos snapshots r20. Identidade de hashes não transfere aceite científico.

Nas coleções de 11.400 ocorrências, 816 referências, 138 relações de recursos e seis ativos, todos os registros fora dos 18 listados permanecem `pendente_de_integracao`. Os estados propostos não aprovam pais, descendentes, contextos ou fontes. As coleções se sobrepõem, não são percentuais científicos nem número de cálculos; pendência não apaga histórico. Os 197 artigos são tratados separadamente e QA-09 continua em correção.

## Reprodução somente leitura

```sh
node auditoria/termodinamica/evidencias/QA-09/ledger-r21-parcial-r1/ledger.mjs --verificar auditoria/termodinamica/evidencias/QA-09/ledger-r21-parcial-r1/ledger.json
```

Sem argumento o programa emite JSON em stdout; com `--verificar`, compara a fotografia salva. Fixa hashes das fotos, inventários, pareceres e reconciliação, e reextrai 18 recortes; confere 23 contextos e links, distinguindo a base alterada por seu hash r21, e recalcula valores selecionados. Não consulta fontes remotas ou interpreta ciência por si. Verificação e teste negativo passaram. Mudança da foto exige nova reconciliação. Sem navegador real, estudantes, revisão humana ou certificação externa.
