# QA-09 — ledger parcial r26, revisão 1

30/10/2026. Autor `/root/planning`. **Integração pendente de auditor independente.** Revalida EX001–005, D26–28 e D11–20 a partir da fotografia r24, já que não houve ledger r25 para esse conjunto. A [reconciliação](reconciliacao-18-r24-r26.md) registra cada conta, hipóteses, fontes e efeito das aplicações r25 de fases e r26 de FUN-02, ficha 59 e EX010/tabela. No D27, o cálculo de potência é aceito apenas sob o modelo de entrada/saída únicas e trabalho total não associado ao escoamento da base ligada, que mudou na r26; o enunciado isolado não enumera todas essas hipóteses. O ledger r24 e seus pareceres são preservados; seu verificador foi reproduzido em cópia com snapshots r24. Hash ou mapa não transporta aceite por si.

Nas coleções de 11.407 ocorrências, 816 referências, 138 relações de recursos e seis ativos específicos, todos os registros fora dos 18 listados ficam `pendente_de_integracao`. Estados localizados não aprovam pais, filhos, bases, fontes ou recursos. Os conjuntos se sobrepõem e não são quantidade de cálculos ou percentual científico; pendência não apaga análises históricas. Os 197 artigos têm tratamento separado; QA-09 continua em correção.

## Reprodução somente leitura

```sh
node auditoria/termodinamica/evidencias/QA-09/ledger-r26-parcial-r1/ledger.mjs --verificar auditoria/termodinamica/evidencias/QA-09/ledger-r26-parcial-r1/ledger.json
```

Sem argumento o programa emite JSON em stdout; com `--verificar` compara a fotografia salva. Fixa fotos, inventários, ledger e parecer r24, pareceres de aplicação r25 e r26, reconciliação e parser; reextrai os 18 objetos, valida 23 contextos com a base de turbina alterada e recalcula valores selecionados. O verificador não consulta fontes remotas nem interpreta ciência por si; o relatório documenta a análise e seus limites. Verificação positiva e teste negativo passaram. Nova alteração exige reconciliação própria. Sem navegador real, estudantes, revisão humana ou certificação externa nesta integração.
