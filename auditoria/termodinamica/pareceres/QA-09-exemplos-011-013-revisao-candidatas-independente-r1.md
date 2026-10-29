# QA-09 — revisão independente das candidatas EX-011 e EX-013, r1

Data: 29/10/2026. Parecer localizado de apoio independente automatizado. **As duas candidatas são tecnicamente adequadas para resolver as insuficiências adjudicadas**, sujeitas a conferência da versão aplicada e de suas dependências. Não há alteração de produto/controle nem aprovação global QA-09.

## Fotografia e delta

Documento `modulos/e1-termodinamica.html` SHA-256 `dd47dc9dbc5c22f6f74a4fa67bd28b495cff775ff8ca04cec2c76c405dfefd1a`; inventário `auditoria/termodinamica/evidencias/QA-09/inventario-r6.json` SHA-256 `a38b60799c23cf88fb0085e7c9bd82b4f22f58a4c7f89b6b418f8b3f5ae5d1aa`; adjudicação `auditoria/termodinamica/pareceres/QA-09-adjudicacao-exemplos-011-013-independente-r1.md` SHA-256 `b367184a6a866928efeaa0e9a25dc91599ff0624b6bd0e9b0cedd018533bb3d7`. Embora a adjudicação examine a fotografia anterior `49b0df4f…`, os hashes dos fragmentos originais permanecem iguais na fonte atual. Cada original ocorre exatamente uma vez nesta fonte; o trecho `antes` de cada manifesto ocorre uma vez e sua substituição literal por `depois` produz a candidata completa byte a byte. Fonte, inventário, adjudicação e hashes de ambos os fragmentos e arquivos conferem com cada manifesto. Arquivos isolados incluem uma nova linha final; hashes de fragmentos excluem-na.

## EX-011 — tanque com agitador

A candidata torna o eixo a única transferência de trabalho e identifica os 40 kJ como perda líquida de calor. Isso exclui o trabalho elétrico adicional do contramodelo adjudicado. Convenção da base: calor recebido positivo e trabalho saindo positivo, com ΔEc/ΔEp desprezíveis; logo `Q=−40 kJ`, `W_total=−250 kJ`, `ΔU=Q−W=−40−(−250)=+210 kJ`. A condição de nenhuma massa atravessando a fronteira é preservada e parede rígida não é indevidamente apresentada como impedimento de trabalho de eixo. Conta exata para dados nominais, sem tolerância instrumental fornecida.

## EX-013 — compressão e aquecimento

Na primeira parte, a candidata identifica `W=−4 kJ` como trabalho de fronteira, declara não haver outros trabalhos e identifica `Q=−7 kJ` como calor líquido. Com pressão quase estática de 200 kPa e `ΔV=−0,020 m³`, `W_b=200×(−0,020)=−4 kPa·m³=−4 kJ`; como esse é todo o trabalho, `ΔU=−7−(−4)=−3 kJ`. O trabalho adicional do contramodelo fica excluído. A segunda parte do fragmento mantém-se integralmente: 1 kg de gás ideal, cv=0,70 kJ/(kg·K), Q=35 kJ e tanque rígido sem outros trabalhos dão `ΔT=35/(1×0,70)=50 K`, com cv constante/representativo da faixa como ensinado na base. Variação em K, não temperatura absoluta final. Contas exatas no modelo para dados nominais; sem tolerância instrumental dada.

## Identidade e limites

Ambos são `div.exemplo` na seção de aula, fora dos 197 artigos BAN-08 e sem alternativas ou gabarito pontuável próprio. Os deltas preservam marcação, título e solução numérica; pela inspeção estática de `assets/curso.js`, SHA-256 `a20f4d19158073a9a1c48aabdfba8fa863b02063e16061c00b16448a6ccc2e13`, os seletores dos bancos pontuados usam `article.questao` e `.concurso-item, .avalia-item`, não esses blocos. Não houve teste de navegador ou de armazenamento. Aplicação futura altera o hash integral e exige verificar a versão efetiva, preservar arquivos e artigos, conferir elos, fotografias/inventários e revalidação localizada de evidências afetadas. O parecer não comprova a aplicação nem aprova QA-09 completo.

## Hashes SHA-256 dos artefatos

| Artefato | EX-011 | EX-013 |
|---|---|---|
| Fragmento original | `b0259df0ccfb9755fe447a080f0b4f4ae5b79a797ca924a7ad4611e8781c8c27` | `d8fc4f1313b7ac9a73c7b256aabf31ab2df4ba8026f6fd9fae89ccfd9bee1cac` |
| Fragmento candidato | `8ec6ce4013a1be49c569b5e3b8ab5e80b899cb9d250396be6023b1eecfa2d3c9` | `7438f121e00f4c757b695c3de6f881d295128696b48bad8f5d387b0e6547dfea` |
| Arquivo original | `695433219fd2c4760bb36bb0faf19e4fa33707762a5d0650eaee9a286fef05b7` | `893c5249e349e796bfcbc406b5da245b93bce0d83ec487e05ab7f681d0d0aaae` |
| Arquivo candidato | `384fa7aa002d9fac75a876f034ae4b751acd0969916121b1fbd18a266688199d` | `ca430dc39f10636fa585ab8f9ac59335f28310db28799637e5eb68c6609232ae` |
| Manifesto JSON | `1d1dee05c8cb571791a08cdb2447193aa6414dea27e345f06b953f31d556e6ae` | `5677916ceeb26a5739bfbc528b33dd286636281d752cfcb9716906ad2ce71203` |

Os arquivos ficam em `auditoria/termodinamica/evidencias/QA-09/` com os prefixos `exemplo-011-` e `exemplo-013-`. Análise do Corretor `exemplos-011-013-analise-candidatas-r1.md`: `382faf66c3f8b9b23d480060dee8055f815c08939805a9fb6f74135354cd057b`.
