# QA-09 — ledger parcial r17, revisão 1

30/10/2026. Autor `/root/planning`. **Pendente de auditoria independente desta fotografia.** O ledger reconcilia individualmente 18 registros auditados na r16: EX001–005, D26–28 e D11–20. A [reconciliação](reconciliacao-18-r16-r17.md) documenta as contas, condições, contextos e exame da alteração de intercooling; preserva a ligação ao ledger r16 r2 e a seu parecer independente. Os antigos ledgers não são alterados.

O padrão é `pendente_de_integracao` para todos os outros registros das quatro coleções: 11.400 ocorrências, 816 referências, 138 relações de recursos e seis ativos específicos. O estado localizado não aprova automaticamente pais, descendentes, contextos, referências ou recursos; as coleções se sobrepõem e não correspondem a percentual de conclusão. Pendência de integração não apaga análise histórica. Os 197 artigos mantêm tratamento separado. QA-09 continua em correção.

## Reprodução sem escrita

```sh
node auditoria/termodinamica/evidencias/QA-09/ledger-r17-parcial-r1/ledger.mjs --verificar auditoria/termodinamica/evidencias/QA-09/ledger-r17-parcial-r1/ledger.json
```

Sem argumento o programa emite JSON em stdout; com `--verificar` confronta a fotografia salva. Confere os hashes das versões, relatórios, pareceres e parser; identidade dos 18 objetos e de seus contextos, incluindo os links para as bases (23 contêineres distintos); e contas selecionadas. O relatório dá as condições que justificam a revalidação científica; um hash por si não transfere aceite. O script não consulta fontes remotas ou avalia mérito científico por si. A verificação positiva e teste negativo em cópia passaram. Não houve teste com estudantes, navegador real, revisão humana ou certificação externa.

Próximos lotes precisam de nova reconciliação e auditor distinto, por exemplo os demais diagnósticos e exemplos, fichas cujos exames foram limitados, teoria, figuras, tabelas, fontes e ativos. Qualquer alteração da fotografia exige nova verificação de impacto, sem regravar esta pasta.
