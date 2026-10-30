# QA-09 — ledger parcial r19, revisão 1

30/10/2026. Autor `/root/planning`. **Integração pendente de auditor independente.** O ledger revalida EX001–005, D26–28 e D11–20, os 18 objetos anteriormente auditados em r18. A [reconciliação](reconciliacao-18-r18-r19.md) registra cada resultado, hipótese e contexto e examina tanto as quatro alterações r17→r18 quanto as três alterações r18→r19. Os ledgers históricos são preservados; comparação de hash e estrutura não transfere aceites por si só.

Todos os demais registros das coleções de 11.400 ocorrências, 816 referências, 138 relações de recursos e seis ativos específicos ficam `pendente_de_integracao`. Uma linha localizada não aprova pais, descendentes, fontes ou contêineres. As coleções se sobrepõem e seus totais não são número de cálculos ou percentual de conclusão. Pendência não apaga a história; 197 artigos têm tratamento separado. QA-09 continua em correção.

## Reprodução somente leitura

```sh
node auditoria/termodinamica/evidencias/QA-09/ledger-r19-parcial-r1/ledger.mjs --verificar auditoria/termodinamica/evidencias/QA-09/ledger-r19-parcial-r1/ledger.json
```

Sem argumento o programa escreve JSON somente em stdout; com `--verificar` compara a fotografia salva. Fixa hashes de aula, formulário, inventários, ledger e parecer r18, parecer da aplicação r19 e parser; reextrai 18 recortes, confere 23 contextos e links e recalcula valores selecionados. Não consulta fontes remotas, nem interpreta ciência por si. A verificação e um teste negativo de estado adulterado passaram; mudança da base requer nova fotografia e exame de impacto. Não houve navegador, alunos, revisão humana ou certificação externa.
