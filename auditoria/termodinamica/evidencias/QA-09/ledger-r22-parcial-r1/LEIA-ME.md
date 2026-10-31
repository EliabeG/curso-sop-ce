# QA-09 — ledger parcial r22, revisão 1

30/10/2026. Autor `/root/planning`. **Pendente de auditoria independente desta integração.** Reconcilia 18 objetos anteriormente examinados: EX001–005, D26–28 e D11–20. A [reconciliação](reconciliacao-18-r21-r22.md) documenta cada resultado, hipótese, fonte e efeito dos três deltas. D14 mudou: é reavaliado em seu novo enunciado com entrada elétrica de 120 W, e não por igualdade com o antigo. D13 depende da base de radiação alterada; D14, da base de geração alterada. O ledger r21 foi reproduzido em cópia dos seus snapshots, e não é sobrescrito.

Nas coleções de 11.400 ocorrências, 816 referências, 138 relações de recursos e seis ativos específicos, todos os demais registros permanecem `pendente_de_integracao`. A classificação localizada não aprova pais, filhos, bases, fontes ou recursos. As coleções se sobrepõem e não são número de cálculos ou porcentagem de conclusão; pendência não apaga o histórico. Os 197 artigos mantêm tratamento separado; QA-09 segue em correção.

## Reprodução somente leitura

```sh
node auditoria/termodinamica/evidencias/QA-09/ledger-r22-parcial-r1/ledger.mjs --verificar auditoria/termodinamica/evidencias/QA-09/ledger-r22-parcial-r1/ledger.json
```

Sem argumento, o programa emite JSON em stdout; com `--verificar`, compara a fotografia salva. Fixa fotos, inventários, ledger e parecer r21, parecer da aplicação r22 e reconciliação; reextrai 18 objetos, reconstrói D14 pela candidata específica, confere 23 contextos com os dois alterados identificados e recalcula valores selecionados. Não consulta fontes remotas ou interpreta ciência por si. Verificação positiva e teste de estado adulterado passaram; mudança de base exige nova análise. Sem navegador real, estudantes, revisão humana ou certificação externa nesta integração.
