# BAN-07 — complemento independente: CR45 r2b e reconciliação CR06

Data: 29/10/2026. Revisora: `/root/auditoria_av61_70`, agente automatizado independente do Corretor. **CR45 r2b aprovada como candidata isolada**, sujeita à decisão do Auditor principal sobre o alcance da base temporal; **CR06 mantém aprovação da redação isolada**, agora com JSON reconciliado. Nenhuma candidata foi aplicada por esta revisão. A análise não aprova produto r2 nem BAN-07 global e não libera outro ID.

## CR45 — candidato r2b

A versão anterior foi examinada em [BAN-07-candidatas-cr06-cr26-cr45-r2-independente.md](BAN-07-candidatas-cr06-cr26-cr45-r2-independente.md), SHA-256 `1113b02ee2174f144b3720dcf3ae69d2e6e4f393e116c6727c6fb96287e2ca0d`. O novo fragmento `CR45-candidata-r2b.html` tem SHA-256 `3b7e1013014ca169f810aba4973e03c1b98a8972c5648289a996b523d63ff448`; seu JSON `CR45-candidata-r2b.json` tem `5257957efbb70f493f943634bf6d130bd0cbc5b7a9cc3d264b52a7dfbe70e4ad`. Ao suplemento prévio de ciclo fechado e duas fontes, o r2b adiciona: “Os 900 kJ recebidos e os 90 kJ rejeitados são quantidades referentes ao mesmo ciclo.” A hipótese está identificada como editorial, não integra o texto oficial e é apresentada antes do campo de resposta. A exclusividade de duas fontes e a base temporal comum bloqueiam os contramodelos anteriores; não se atribui qualquer interpretação ou anulação à banca.

Com Tq=750,15 K, Tf=300,15 K, Qq=900 kJ/ciclo e Qf=90 kJ/ciclo, o ciclo fecharia energia com W=810 kJ/ciclo e η=0,90. A segunda lei requer Qf/Qq≥Tf/Tq≈0,40012; a razão dada é 0,10. A rejeição mínima seria ≈360,108 kJ/ciclo e ηCarnot≈0,59988. Logo, no modelo explicitado, a afirmativa de impossibilidade é correta: **C**; **E** negaria essa conclusão. O cálculo e o comentário publicado concordam; a diferença é muito maior do que qualquer arredondamento exibido. A limitação por duas fontes e a igualdade da base por ciclo são necessárias à conclusão, não consequências automáticas do texto da banca.

Conferi que o verificador do Corretor `verificar-CR45-r2b.mjs`, SHA-256 `4a776227e4017162ef2dcc581bfdcbe7dc60b81bbe9a8fb562534f4cabed341a`, apenas lê arquivos e imprime resultado; reproduzi-o sem gravação. Remover o único parágrafo editorial reconstitui o artigo r1 byte a byte, inclusive texto e chave oficiais, e o hash do artigo de base é `382306e2bd0381e3614cfefd799d12a1b90a06b3b78e1f2171bc5c9c67c4ba4d`. A digital vai de `c084d78c` a `9475e2f5`; o verificador não detectou colisão com as 80 digitais CR atuais ou com as candidatas CR06 e CR26 já calculadas. Não foi examinado o universo de históricos desconhecidos. O verificador também confirmou os cinco hashes de produto r1, sem mudança.

## CR06 — atualização do JSON e continuidade do parecer

O HTML candidato continua SHA-256 `873e51481bc440721e17c233292535fdf7367670ba819c954987b7c263d8420b`, idêntico ao examinado no parecer anterior; a digital candidata permanece `d63393e4`. O JSON mudou de `2fa0c64fc2c34b9b144efe6a91ba52c7469c54cdb0563d3422352bfe68434206` para `78e6688c12a1371dd4e7144ff1098fd590106c430768d43563380213064cd615`. A alteração efetiva corrige, na frase da demonstração, “A e B são constantes” para “a e b são constantes”, conforme os símbolos da equação imediatamente anterior. Reconstruí o texto anterior **somente em memória**, revertendo essa substituição; o SHA-256 resultante coincide exatamente com o hash antigo. Isso comprova que, entre os bytes comparados, a mudança foi essa troca de letras, não apenas uma afirmação do Corretor. Não salvei nem restaurei o JSON antigo.

Reexaminei o JSON atual: a derivação de TX=a+bTY e a condição βY≠0 estão corretas e agora usam a mesma notação do enunciado. O HTML, a chave C e a hipótese são os mesmos avaliados anteriormente; a aprovação local da candidata permanece sustentada, com identidade do JSON atual explicitamente atualizada. Essa conclusão não aprova de forma automática qualquer outro arquivo ou produto aplicado.

## Limites e reapresentação

| Verificação | Resultado |
|---|---|
| CR45 r2b — hipóteses e única marcação | Suficientes no modelo editorial; C correta, E falsa. |
| Preservação oficial e distinção | O único acréscimo é um parágrafo editorial; retirado, recupera r1 exatamente. |
| CR06 JSON | Alteração de “A e B” para “a e b” confirmada por reconstrução em memória do hash anterior; demonstração coerente. |
| Integridade/digitais | Cinco arquivos r1 conferem; digital CR45 r2b diferente e sem colisão no conjunto declarado. |
| Aplicação e comportamento | Não executados: dependem do produto real, inventário/registro de suplementos, teste de histórico, não migração, aviso, placar e recarga. |

CR45 r2b substitui para esta decisão a candidata anterior `49a25699d2703ffec80252139d7278dc806665feae3ad2bb30f33d0058286eec`; ela permanece preservada como histórico, com sua digital anterior `107f0566`. As conclusões sobre CR26 permanecem limitadas à candidata examinada na peça anterior. Não se afirma teste com estudantes, auditoria de acessibilidade, revisão humana ou certificação externa. O produto e o controle não foram alterados. A eventual reapresentação deve registrar a hipótese editorial no inventário de suplementos FON-02, revalidar dependências e verificar as tentativas no produto efetivamente alterado.
