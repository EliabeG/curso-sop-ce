# QA-09 — auditoria independente da candidata FUN-01 P3, reconciliada com r10

Data: 30/10/2026. Auditor: agente automatizado `/root/next_formulas`; Corretor da candidata: `/root/next_graphics`. **Veredito: APROVADA como proposta isolada no alcance abaixo.** A aprovação não representa aplicação efetiva, nem encerra QA-09 ou libera o próximo ID.

## Identidade e revisão da mudança de fotografia

A candidata foi preparada sobre a aula r9 SHA-256 `2d6b8fb2f9c99e04d22c19d7b32bbc3eb20577459d9132e506f9c0acef3f2fc2`. Durante esta auditoria, a aula mudou para r10 SHA-256 `a8bed8a91a36a1c1f41cd75e3c1858fecb4e14a506e582ad1fdb186d275805e3`; inventário r10 SHA-256 `3497cbf9ffcbe0a1e2eb84eeb9e34c0cfb6e0ed63a2747795bf75832454e2f6c`. O verificador histórico da candidata r9 rejeitou corretamente o HTML novo: `foto da aula divergente`. **Não sobrescrevi o manifesto r9 nem contornei essa verificação.**

Reexaminei diretamente a versão r10: o artigo `fun01-e1-supercritico` continua em 125803–131220 UTF-16, SHA-256 `2fad0e042fb945eb44d0f2abe2c4e64322434195395fa4e5c084f17854f432a7`, igual ao item segregado em ambos os inventários r9 e r10. O parágrafo original continua no contexto do mesmo artigo, ocorre uma vez na aula, em 129564–130109, SHA-256 `7b13d7adbb3ec83f676edadbebf7a0246d139ff24bf4931350d7580708b47bd9`; a candidata sem quebra final tem SHA-256 `ce23ebfff83d3172e72046551cf365a967a098b0640c01acb56480154ccd7015`. Reconstrução independente confirma que trocar apenas a frase especificada produz a candidata.

- [Análise do Corretor](../evidencias/QA-09/fun01-p3-procedencia-candidata-r9-20261030/analise.md): SHA-256 `7afd8027294d800ed66abf03f85bb27520680ad5108267e8ce9de526c315d527`.
- Manifesto r9: `6814cc5a9ac1bcb4612da469184fb4d0e2298bddf87b653df6852f7edfe6658e`.
- Verificador r9: `2beadeea9234c7f99554c389279a4a21d194ed6dc7407bc134d4f7c07b4bb79a`; sua rejeição em r10 é esperada e não significa falha da candidata.

Em simulação independente somente em memória sobre r10, substituí o parágrafo único: o resultado teve SHA-256 `f76c39a3e1d8c349ebf0df72cc20a3ab21c68960c8451799bad90a9dcc4bd8c7`. Os 197 artigos mantiveram IDs e ordem; exatamente o artigo `fun01-e1-supercritico` mudou e os demais 196 permaneceram byte a byte iguais. Nenhuma modificação foi gravada no HTML por essa simulação. O hash hipotético identifica apenas esta aplicação isolada sobre r10; outros deltas concomitantes o alterarão.

## Enunciado, solução e mérito

Li o enunciado e a solução completos da versão r10. O enunciado diz que duas colunas ρ e v=1/ρ são produzidas pelo mesmo sensor. A relação funcional entre grandezas é exata e pode ser lida como definição de uma coluna invertida, mas não descreve inequivocamente o procedimento de aquisição interno. A candidata conserva a conclusão de redundância e muda “uma é calculada da outra” para “uma pode ser calculada a partir da outra, sem que isso determine como as medições foram obtidas”. Não afirma medições independentes nem as descarta; não altera o enunciado, os valores, a classificação dos estados, a resposta sobre propriedades independentes ou a rubrica.

A identidade `v=1/ρ` vincula volume específico e densidade para a mesma substância e estado; não são duas coordenadas de estado independentes. Valores nominais recíprocos ρ=800 kg/m³ e v=0,00125 m³/kg, mesmo obtidos por meios diferentes em um instrumento hipotético, não demonstram a origem instrumental nem criam independência termodinâmica. Sua concordância de medição real dependeria de incertezas e rastreabilidade, não fornecidas no enunciado. A interpretação alternativa de que a coluna é definida como calculada continua possível; o novo texto evita atribuir o processamento interno sem essa explicitação.

## Critérios e limites

| Critério localizado | Resultado |
|---|---|
| Enunciado, rubrica, valores e resultado | Preservados na proposta, pela substituição única. |
| Redundância física versus procedimento do sensor | Esclarecida, sem inventar uma origem. |
| Identidade r9 e reconciliação r10 | Conferidas para este artigo e seus fragmentos; parecer não aprova a mudança r9→r10 inteira. |
| Outras 196 questões na simulação | Idênticas e na mesma ordem; teste estático do parser. |
| Aplicação e impacto BAN-02/07/08 e FUN-01 | Pendentes: alteração real modifica o hash do artigo e seus registros e exige revalidação localizada. |
| QA-09 integral e próximo ID | Não atendidos; permanecem bloqueados. |

Após aplicação real, atualizar a identidade e o hash do item no inventário oficial, reconciliar fotografias, mapas, referências e dependências, executar os testes pertinentes e submeter a versão efetiva a novo parecer independente. Este é um problema autoral, não transcrição ou gabarito oficial. Não houve ensaio em navegador, revisão humana, teste com alunos ou certificação externa.
