# QA-09 — auditoria independente da aplicação de flashcards e ficha 80

Data: 30/10/2026. Revisor: agente automatizado independente `/root/qa_diagnosticos`. **Veredito: APROVADO para a aplicação localizada das sete alterações da aula e da ficha 80 na versão examinada.** QA-09 permanece em correção e o próximo ID não está liberado.

## Critério, versões e alcance

QA-09 requer levantamento e recálculo de todo o conteúdo numérico fora dos 197 artigos, incluindo fichas e explicações. Esta avaliação cobre apenas as oito alterações aprovadas como candidatas isoladas, sua aplicação, o mapeamento r8→r9 e o impacto localizado de FOR-01 e dos bancos. Não cobre a totalidade de QA-09 ou de qualquer unidade curricular. A entrega do Corretor `auditoria/termodinamica/evidencias/QA-09/aplicacao-flashcards-ficha80-r1/entrega-r1.md` tem SHA-256 `5e236f0085ccdf3a2af0a7afda1368fa8c49cb2ee821b1ba24c9c0123e54fc49`.

Fotografia anterior: aula `57b13f0d6386764f1cc46ce543013b0eb75f7bfa97ffbd63ea331f38bfc5af8c`, formulário `c27422b409a0a755448982c4074c6d6967fd3e91d7eae20274e218530f5c37b0`, inventário r8 `ae75a258398c385398567457d98ebd49b9838c0c9a4eedc69ea8d2d72981b687`. Versão efetiva: aula `2d6b8fb2f9c99e04d22c19d7b32bbc3eb20577459d9132e506f9c0acef3f2fc2`, formulário `cda652563a79c49a6c3d527ad1400c7f7597d33c9b8523ed8a26047b25c69feb`, inventário r9 `023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d` e mapa r8→r9 `d210e8c7efd4520e0d2036c4ebd2ec90762f684ffe8378b5fd71fdbd43d15b90`.

## Identidade, conteúdo e ciência

Reconstituí separadamente as duas fontes anteriores a partir dos oito pares aprovados. Cada original aparece exatamente uma vez na fotografia respectiva, cada candidata exatamente uma vez na versão atual, e os hashes dos fragmentos sem a quebra final conferem com a configuração. As duas reconstruções reproduzem os arquivos efetivos e suas fotografias `depois` **byte a byte**. Logo, no delta examinado não houve mudança adicional nas duas fontes.

A conferência direta dos fragmentos efetivos confirma:

- COP distingue refrigeração de bomba de calor em ciclo por compressão com acionamento somente por trabalho, preservando calor útil e trabalho de entrada na mesma base; não apresenta a razão como definição universal de absorção.
- Válvula, compressor e trocador explicitam regime permanente, relações de entrada/saída e as demais condições necessárias para as expressões de entalpia, trabalho e geração de entropia. O resumo distingue massa fixa de volume de controle estacionário com uma entrada e uma saída; não trata genericamente a entropia média de um volume transiente como constante.
- Os dois cartões de pressão intermediária especificam gás ideal, estágios estacionários adiabáticos, mesmos calores específicos e eficiência isentrópica constante, mesma vazão, resfriamento perfeito e demais hipóteses. Com `a=(γ−1)/γ>0`, `r₁r₂=p₃/p₁` fixo e trabalho proporcional a `(r₁ᵃ−1)+(r₂ᵃ−1)`, a soma é mínima em r₁=r₂, logo `p_i=√(p₁p₃)`. Para 1 e 16 bar absolutos, resulta 4 bar. Não se garante o ótimo para equipamentos que violem o modelo.
- A ficha 80 explicita `Q̇in>0` e `Ẇt>Ẇc` para interpretar o quociente como rendimento de motor, tanto no texto visível quanto em `data-busca`. A diferença algébrica permanece válida independentemente do sinal. Para dados hipotéticos, `(1000−400)/1200=0,5`; Q̇in=0 tornaria o quociente indefinido e trabalho líquido negativo não representaria motor produtor líquido. Essas restrições não bastam, sozinhas, para comprovar a viabilidade termodinâmica de um ciclo real.

## Estrutura, mapa e impacto

Por extração independente com `lxml`, os 197 artigos com IDs são iguais e estão na mesma ordem; os 197 registros individuais do inventário oficial também são idênticos, tendo apenas a chave `fonte` atualizada. Das 100 fichas, somente a de ID `formula-brayton-liquido` mudou; as outras 99 são iguais. Comparei os 734 elementos MathML da aula e 191 do formulário sem cauda de texto adjacente: todos são iguais. Isso é confronto estrutural, não garante renderização ou leitura assistiva.

Examinei a correspondência de todos os registros dos inventários, sem IDs duplicados: 11.200 pares externos, 196 internos e um nó textual adicionado ao cartão do compressor; 11.396 ocorrências r8 e 11.397 r9. Identidade por documento, seção, âncora, tipo e tag, e os deslocamentos externos conferem. Dos 196 pares internos, 181 com hash igual têm também o elemento bruto extraído igual; 15 têm hash alterado no interior dos trechos aprovados. Outros três hashes alterados são seções ancestrais. Essas associações são estruturais e não transmitem automaticamente mérito científico a outro nó ou versão. O nó novo corresponde ao parágrafo adicional de hipóteses do compressor.

Os 815 registros de referências mantêm campos de conteúdo e posições externas esperadas; uma referência interna à ficha 80 mantém a âncora. Os 138 registros de recursos mantêm identidade e hashes, exceto atualização dos dois documentos modificados; os novos hashes foram confrontados com os arquivos efetivos. Os seis ativos específicos e os artigos segregados em r8/r9 são iguais. O validador canônico retornou `ok=true`, com 197 itens e artigos, 29 recursos e 1.263 links locais. Há 103 links das fichas para 50 destinos distintos da aula, todos existentes; existência não comprova qualidade didática. O teste BAN-08 passou seis cenários em DOM e armazenamento simulados.

Para verificar o efeito da condição adicionada ao índice de busca, executei `python3 auditoria/termodinamica/evidencias/QA-09/auditoria-aplicacao-r9-20261030/extrair-fichas.py | node auditoria/termodinamica/evidencias/QA-09/auditoria-aplicacao-r9-20261030/testar-filtro-vm.cjs`. O código real de `assets/formulario-e1.js`, com 100 fichas extraídas e DOM/agrupamento simulados, encontrou a ficha 80 ao pesquisar `rendimento motor` (3 de 100 fichas), retornou zero para termo inexistente e permitiu ocultar e revelar fórmula. Os scripts têm SHA-256 `d5d76913fe707b1437781c93fe431873fbacef27918000cc7e5debb53c0aeaba` e `20b48b064efe1590ecb8a564e7f6a4bf1962c34fc601bd489124cc2849564226`. Não é ensaio de navegador real.

No alcance desta alteração, a identidade das outras fichas, MathML, destinos e scripts, junto com a conferência científica do novo limite da ficha 80, sustentam **revalidação localizada de FOR-01** para o efeito examinado. A preservação dos artigos, registros e scripts sustenta revalidação localizada de BAN-02/07/08 para este delta. Isso não transfere automaticamente todas as conclusões anteriores para a nova versão ou revisa as fichas integralmente. Inventários e ledgers r8 continuam registros históricos; uma ponte para r9 exige identidade e reavaliação de dependências.

| Critério localizado | Resultado |
|---|---|
| Reconstrução e fidelidade dos oito deltas | Atendido nas versões efetivas identificadas. |
| Matemática, hipóteses e limite da ficha 80 | Atendido nos modelos descritos. |
| 197 artigos/registros, 99 demais fichas e MathML | Preservados no alcance comparado. |
| Mapa, referências, recursos e efeitos em FOR-01/BAN | Conferência localizada, com as limitações acima. |
| Comportamento em navegador e aprendizado | Não examinados; Node/VM é simulado e não equivale a navegador. |
| QA-09 integral e próximo ID | Não atendidos; permanecem bloqueados. |

Não houve teste com alunos, revisão humana ou certificação externa. A aprovação desta aplicação não classifica o curso inteiro como avançado.
