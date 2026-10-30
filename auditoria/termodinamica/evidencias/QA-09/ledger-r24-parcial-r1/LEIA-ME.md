# QA-09 — ledger parcial r24, revisão 1

30/10/2026. Autor `/root/planning`. **Pendente de Auditor independente desta integração.** Revalida EX001–005, D26–28 e D11–20 anteriormente examinados na r23. A [reconciliação](reconciliacao-18-r23-r24.md) registra contas, hipóteses, vínculos e efeitos das seis edições da preparação FUN-01, incluindo a distinção do potencial intrínseco e externo no D11 e o modelo de EX005. O ledger r23 foi reproduzido em cópia com seus snapshots e permanece preservado. Hash ou correspondência não transporta aceite científico por si.

Nas coleções de 11.400 ocorrências, 816 referências, 138 relações de recursos e seis ativos específicos, todos os registros fora dos 18 listados permanecem `pendente_de_integracao`. O estado localizado não aprova pais, filhos, bases, fontes ou recursos. Os conjuntos se sobrepõem e não são número de cálculos ou porcentagem de conclusão; pendência não apaga análises históricas. Os 197 artigos são tratados separadamente; QA-09 permanece em correção.

## Reprodução somente leitura

```sh
node auditoria/termodinamica/evidencias/QA-09/ledger-r24-parcial-r1/ledger.mjs --verificar auditoria/termodinamica/evidencias/QA-09/ledger-r24-parcial-r1/ledger.json
```

Sem argumento o programa emite JSON em stdout; com `--verificar` compara a fotografia salva. Fixa hashes das fotos, inventários, ledger e parecer r23, parecer de aplicação r24, reconciliação e parser. Reextrai 18 objetos, valida links e 23 contextos e recalcula valores selecionados. Não consulta fontes remotas nem interpreta ciência por si; o relatório e pareceres documentam as hipóteses. Verificação positiva e teste negativo passaram; mudanças exigem nova reconciliação. Sem navegador real, estudantes, revisão humana ou certificação externa nesta integração.
