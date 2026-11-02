# QA-09 — ledger parcial r16, revisão 1

30/10/2026. `/root/planning`. **Pendente de auditoria independente da integração.** A fotografia parte do inventário r16, não altera ou sobrescreve ledgers anteriores. QA-09 permanece em correção.

São classificados no escopo localizado de sua análise oito objetos `exemplo_ou_diagnostico`: EX-001–005 e diagnósticos 26–28. O documento [reconciliação](reconciliacao-ex001-005-d26-28.md) apresenta, individualmente, contas, hipóteses, contexto, limites e fontes; confronta o parecer independente r9 e faz nova leitura na r16. O ledger referencia ambas as identidades, a revisão histórica, o autor de revalidação e o hash do documento específico; a igualdade de fragmento é uma checagem adicional, não o fundamento exclusivo. Os contextos foram conferidos, mas não recebem estado de cobertura por isso. **Nenhum descendente ou ancestral é automaticamente aprovado.**

As quatro coleções são 11.400 ocorrências, 816 referências, 138 relações de recursos e seis ativos específicos. Esses conjuntos se sobrepõem e suas quantidades não medem número de cálculos ou percentual de conclusão. Todos os registros exceto os oito explicitamente listados permanecem `pendente_de_integracao`, incluindo a referência WIKA anteriormente examinada em r15, até que sua ponte com r16 seja revalidada. Pendência de integração não significa ausência de trabalho histórico nem exige, por si só, refazer toda análise. Os 197 artigos permanecem sob tratamento separado e não são aprovados por este ledger.

## Próximos lotes

1. Diagnósticos 01–25: reconciliar por objeto as revisões r9, r12 e r13 e as correções do 2 e 23 nas aplicações r10 e r14; consultar enunciado, modelo e fontes na base vigente e produzir parecer específico, com auditor independente. Priorizar os diagnósticos com base em ciclos que tiveram mudanças r16.
2. Exemplos restantes: reconciliar as revisões e correções históricas por objeto, com atenção às oficinas 047/049 e à correção do 031. Um grupo historicamente revisado não equivale a aceitação integral na fotografia atual.
3. Fichas: reconciliar primeiro as revisões cujo alcance era apenas valores/coefficientes e as correções posteriores; cada indicação deve identificar a expressão ou resultado examinado, hipótese, dependências e auditor. A revalidação localizada das fichas 89/90 na r16 não estende a análise a todas as fichas.
4. Teoria, tabelas, figuras, flashcards, atributos, referências, recursos e ativos: triagem por significado e dependências; tratar fontes bloqueadas por 403 com evidência acessível, sem presumir resultado. Incluir testes em navegador e acessibilidade no escopo próprio.

Para cada novo lote usar uma nova revisão, conservar a fotografia anterior, registrar parecer e identidade, verificar impacto de deltas e contexto, fazer recálculos necessários e manter pendente qualquer ponte sem revalidação explícita. O mapa e hashes auxiliam conferência, não transportam aceites.

## Reprodução sem escrita

```sh
node auditoria/termodinamica/evidencias/QA-09/ledger-r16-parcial-r1/ledger.mjs --verificar auditoria/termodinamica/evidencias/QA-09/ledger-r16-parcial-r1/ledger.json
```

Sem o argumento, o programa escreve JSON somente em stdout; em modo de verificação compara a fotografia salva. Fixa os hashes da aula, formulário, inventários, relatório, parecer, snapshot r9 e parser; confere oito pares individualizados e seis contêineres contextuais, além de recálculos selecionados e totais. Uma alteração de base falha e exige revisão. O programa não consulta fontes remotas, não valida ciência sozinho e não substitui o exame independente. O relatório explica quais fontes foram consultadas e a extensão dos cálculos.
