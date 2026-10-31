# QA-09 — ledger parcial r23, revisão 1

30/10/2026. Autor `/root/planning`. **Pendente de auditor independente desta integração.** Revalida individualmente EX001–005, D26–28 e D11–20, já examinados na r22. A [reconciliação](reconciliacao-18-r22-r23.md) documenta resultados, limites, fontes e efeitos das alterações do resumo/glossário sobre os modelos relevantes. O ledger r22 foi reproduzido em cópia dos seus snapshots e permanece preservado; igualdade de hashes ou mapa não transfere aceite científico por si.

Nas coleções de 11.400 ocorrências, 816 referências, 138 relações de recursos e seis ativos específicos, todos os demais registros permanecem `pendente_de_integracao`. O estado localizado não aprova pais, filhos, bases, fontes ou recursos. Os conjuntos se sobrepõem e não representam contagem de cálculos nem percentual de conclusão; pendência não apaga análises históricas. Os 197 artigos mantêm tratamento separado. QA-09 continua em correção.

## Reprodução somente leitura

```sh
node auditoria/termodinamica/evidencias/QA-09/ledger-r23-parcial-r1/ledger.mjs --verificar auditoria/termodinamica/evidencias/QA-09/ledger-r23-parcial-r1/ledger.json
```

Sem argumento o programa emite JSON em stdout; com `--verificar`, compara a fotografia salva. Fixa hashes das fotos, inventários, ledger e parecer r22, parecer de aplicação r23, reconciliação e parser. Reextrai os 18 objetos, valida links e 23 contextos e recalcula valores selecionados. Não consulta fontes remotas nem interpreta ciência por si; o relatório documenta a revisão. Verificação positiva e teste negativo passaram. Mudança de base exige nova reconciliação. Sem navegador real, estudantes, revisão humana ou certificação externa nesta integração.
