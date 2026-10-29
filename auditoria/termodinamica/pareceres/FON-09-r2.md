# Parecer independente — FON-09 r2

**Veredito: APROVADO.** Data: 2026-10-27. Auditor: agente automatizado Auditor AAA, distinto do Corretor. O único ajuste obrigatório da r1, **R1-A**, foi satisfeito. Não há pendência identificada para o aceite de FON-09 nesta versão.

## Recorte e critérios

A reauditoria examinou a [entrega congelada r2](C:/Users/User/Downloads/SOP-CE/auditoria/termodinamica/entregas/FON-09-r2.md), o parser, os casos de regressão e a preservação. Os critérios científicos e documentais integralmente examinados no [parecer r1](C:/Users/User/Downloads/SOP-CE/auditoria/termodinamica/pareceres/FON-09-r1.md) permanecem atendidos por identidade dos arquivos: origem oficial dos defeitos, conferência das 15 células, densidade e conversões, separação entre transcrição histórica e dados corrigidos rastreáveis, não reutilização da tabela inválida, gabarito e digital preservados, metadados e escopo.

| Critério desta reauditoria | Resultado |
| --- | --- |
| R1-A: conservar e validar o fragmento completo | **Atendido.** `indexOf` localiza o primeiro `#`; `slice` preserva todo o sufixo antes da decodificação. Os fragmentos `#page=3#extra`, `#page=3#` e a variante `%23` são rejeitados. |
| Mesmo parser aplicado a HTML | **Atendido.** `#fundamentos#extra` é tratado como ID completo e rejeitado; a existência de `fundamentos` isoladamente não o valida. |
| Contrato anterior e casos positivos | **Atendido.** Casos de PDF, existência de arquivo, HTML e outros recursos mantêm o comportamento esperado. A regra de página continua exigindo inteiro positivo seguro. |
| Delta restrito | **Atendido.** A substituição do único trecho declarado reconstrói literalmente 100% do validador atual a partir da cópia r1. Não há outro delta nesse arquivo. |
| Conteúdo e histórico preservados | **Atendido.** HTML, dados, inventário e resumo idênticos à r1; cinco cópias do pacote r1, 26 evidências e cinco snapshots anteriores íntegros. Manifesto r1, infraestrutura, schema e guia também preservados. |
| Integridade da entrega r2 | **Atendido.** Cinco arquivos correntes, cinco cópias e sete evidências coincidem em hash/tamanho com o manifesto. |

## Execuções e evidências

O Auditor principal reexecutou os **25 casos independentes preparados**: todos corresponderam às expectativas. A validação canônica retornou **197 artigos/registros, 15 recursos, 1.072 links locais, zero erros e avisos**. O apoio técnico reproduziu os **20 casos entregues na r2** e os **39 casos do contrato anterior**, todos aprovados. As duas sessões usaram kernel limpo; a principal também importou o validador por URL nova, evitando cache da r1. Os testes usaram clones em memória ou fixtures temporárias, sem alterar os arquivos canônicos.

- [25 casos independentes e validação canônica](C:/Users/User/Downloads/SOP-CE/auditoria/termodinamica/pareceres/FON-09-r2-casos-independentes.json).
- [Hashes, preservação e reconstrução literal do delta](C:/Users/User/Downloads/SOP-CE/auditoria/termodinamica/pareceres/FON-09-r2-integridade.json).
- [Reexecução técnica dos testes entregues e contrato anterior](C:/Users/User/Downloads/SOP-CE/auditoria/termodinamica/pareceres/FON-09-r2-tecnico.json).
- [Conferência científica independente herdada da r1](C:/Users/User/Downloads/SOP-CE/auditoria/termodinamica/pareceres/FON-09-r1-ciencia.json).

## Versão aprovada

Manifesto r2 SHA-256: `2432e805d567c6c773763a902505ce524b56b4b09c944ee592431241c3aabf88`.

| Arquivo | SHA-256 |
| --- | --- |
| HTML E1 | `6ed5c74f03b2ce449f88e79d143c904442c524166a83afce8f12441d391a6625` |
| Dados CR68 | `828b967f1318924742e8b30aca8575549301afcccaad395f9ed5bcee2fc46456` |
| Inventário | `af30160109fa7e9e007e6de74eb1836896194ff90888aec75e0f8a4a86675618` |
| Resumo do inventário | `1505e80c437fdd6dbbea40973155446ec859ba2fb363752217346876a8fb43db` |
| Validador | `0bd26bcf6288b3bd159ac7c167bfeb4a1a49bbebe784d26a3a93739fcb7790d5` |

As consultas físicas e os testes de navegador não foram repetidos na r2: o conteúdo correspondente é idêntico. Permanecem os limites honestamente registrados na r1. O validador confere sintaxe e existência do PDF, não sua quantidade real de páginas; a paginação dos documentos utilizados foi conferida documentalmente.

**FON-09 r2 APROVADO: satisfeita a condição para o coordenador liberar a próxima correção.** A recomendação de dependência para BAN-10 permanece válida conforme a r1. Este parecer não inicia nem aprova BAN-10, FON-01 ou BAN-08 e não declara o curso inteiro como avançado concluído.
