# QA-09 — ledger parcial r20, revisão 1

30/10/2026. Autor `/root/planning`. **Pendente de auditoria independente desta integração.** Reconcilia 18 objetos EX001–005, D26–28 e D11–20 examinados na r19. A [reconciliação](reconciliacao-18-r19-r20.md) relata recálculos, hipóteses e os efeitos das duas bases modificadas, em especial os diagnósticos D15–18 e a perda externa de D17. O ledger r19 r2 e seu parecer foram preservados e verificados em cópia dos snapshots r19; igualdade de hashes não transporta aceites automaticamente.

Para as coleções de 11.400 ocorrências, 816 referências, 138 relações de recursos e seis ativos específicos, todos os registros fora dos 18 listados permanecem `pendente_de_integracao`. Os estados localizados não aprovam bases, fontes, pais, descendentes ou recursos. As coleções se sobrepõem e não exprimem porcentagem científica ou quantidade de cálculos; pendência não apaga análises históricas. Os 197 artigos são tratados separadamente; QA-09 segue em correção.

## Reprodução somente leitura

```sh
node auditoria/termodinamica/evidencias/QA-09/ledger-r20-parcial-r1/ledger.mjs --verificar auditoria/termodinamica/evidencias/QA-09/ledger-r20-parcial-r1/ledger.json
```

Sem argumento, o script escreve JSON em stdout; com `--verificar`, compara a fotografia salva. Fixa fotos, inventários, ledger r19 r2 e pareceres, reconciliação e parser. Reextrai os 18 blocos, valida 23 contextos e links, distingue os dois contextos alterados por seus hashes r20 e recalcula valores selecionados. Não consulta fontes remotas nem interpreta ciência por si; o relatório documenta reavaliação explícita e pareceres anteriores. Verificação positiva e teste negativo de estado adulterado passaram. Mudança da foto requer nova reconciliação. Sem navegador real, alunos, revisão humana ou certificação externa nesta integração.
