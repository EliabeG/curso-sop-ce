# QA-09 — ledger parcial r27, revisão 1

30/10/2026. Autor `/root/planning`. **Integração pendente de auditor independente.** Revalida EX001–005, D26–28 e D11–20 da r26 r2. A [reconciliação](reconciliacao-18-r26-r27.md) explicita contas, hipóteses e efeitos da base de Carnot e dos três flashcards, incluindo D26, D12 e o modelo de turbina vinculado a D27. O ledger r26 r2 foi reproduzido em cópia dos snapshots; a r1 anterior e seu achado de identificação de D15 permanecem preservados. Hash ou mapa não transfere aceite científico por si.

Nas coleções de 11.407 ocorrências, 816 referências, 138 relações de recursos e seis ativos específicos, todos os registros fora dos 18 listados ficam `pendente_de_integracao`. O estado localizado não aprova pais, filhos, bases, fontes ou recursos; conjuntos sobrepostos não são contagem de cálculos ou percentual de conclusão. Pendência não apaga histórico. Os 197 artigos mantêm tratamento separado; QA-09 continua em correção.

## Reprodução somente leitura

```sh
node auditoria/termodinamica/evidencias/QA-09/ledger-r27-parcial-r1/ledger.mjs --verificar auditoria/termodinamica/evidencias/QA-09/ledger-r27-parcial-r1/ledger.json
```

Sem argumento emite JSON em stdout; com `--verificar` compara a fotografia salva. Fixa fotos, inventários, ledger e parecer r26, parecer da aplicação r27, reconciliação e parser; reextrai 18 objetos, confere links e 23 contextos e recalcula valores selecionados. Não consulta fontes remotas nem interpreta ciência por si. Verificação positiva e teste negativo passaram; mudanças exigem nova reconciliação. Sem navegador real, estudantes, revisão humana ou certificação externa nesta integração.
