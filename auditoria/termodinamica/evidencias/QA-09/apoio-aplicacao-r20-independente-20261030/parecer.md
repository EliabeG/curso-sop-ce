# QA-09 — apoio estrutural independente da aplicação r20

30/10/2026. Auditor automatizado `/root/next_graphics`, distinto do executor `/root/next_examples`. **Apoio estrutural favorável para a fotografia r20**, restrito aos testes abaixo; a apreciação científica e o veredito de aplicação cabem ao Auditor principal `/root/planning`. Eu auditei anteriormente pontes de ledger que incluíam diagnósticos de mistura e fase; essa atuação não é apresentada aqui como novo julgamento científico independente dos textos corrigidos.

## Identidade e reconstrução

Entrega `aplicacao-mistura-fase-r20-r1/entrega-r20.md` SHA `fa4c06a19c681c0cf9122121765c732a020868fabb69014e031bcba6b75f270c`. Aula r19 `9495c5a873dc67f6f1d6dd1919caa473f481a0bc029dbe97e3490adb1b530a65` → r20 `b05a68731a6975755c0030c524e7915d7833aacb176f680b3890fe82efc803e7`; formulário integralmente igual nas duas versões `694ee3d26e8f5679d565986cfb0ad8c10aa98667fc8ffb62a569a87679847a58`. Fotos posteriores coincidem com os arquivos efetivos.

Os dois blocos `base-mistura-termica` e `base-fase-calorimetria` foram reconstruídos a partir das candidatas e do registro de edições SHA `98dfd4f4b9d762220b2884b95d4a5d25a88b144c4a4c665f340e2c16c32c4e3f`; a substituição em memória gera os bytes completos da aula r20. Os manifestos conferidos têm SHA `1b5e5b916849e75afb5ee7b70159114959385d0b4af75bbb0091b8eee66af348` e `d58de60aebce45fc0bbeaf3864e722fb752ba3bd5acd3bbddd1464fd19e62a5d`.

## Mapa e preservação

Inventário r19 SHA `ca99e56b3a5930cdd4f49f4d41a61eca19facc141b63da94dcd3b65039d03c2f`; r20 `e548f61cde56f676dd0c670924bd58e7012a2f80229231de6560cbb55831adf4`; mapa r19→r20 `324337242a6e59422c64a72565ecc0c555a3122511f1d24cd55f8343df12ec53`. Todos os 11.400 IDs de cada versão aparecem uma única vez e os hashes por linha coincidem com os inventários. São 11.284 pares externos de hash igual, um ancestral alterado que contém uma edição e 115 internos conferidos por tipo, tag, arquivo, seção, âncora e pertença ao delta: 94 em mistura, 21 em fase. Dois hashes internos mudam na mistura e quatro na fase; li os seis registros, correspondentes aos textos modificados e contêineres de equação. Pareamento de estrutura não transfere aprovação científica.

Os 197 artigos excluídos da aula mantêm bytes e hash; os 197 registros oficiais e seus demais campos permanecem iguais, exceto a fonte atualizada. Nota anterior permanece prefixo da atual. O formulário completo e seus 100 cartões mantêm os mesmos bytes; os 734 MathML da aula e 191 do formulário coincidem integralmente. Comparei as 816 referências por valores e contexto e as 138 relações de recursos por campos e hashes; apenas o hash da aula muda entre os documentos. Não se infere acesso remoto ou validação científica dessas referências.

## Reprodução e limite

`python3 auditoria/termodinamica/evidencias/QA-09/apoio-aplicacao-r20-independente-20261030/verificar.py`, SHA `748a621e848575542e90272a78741206ceecbba2f35dbc9e9bba738a024667fb`, retornou `ok=true`. O validador canônico da árvore efetiva passou com 197 artigos/itens, 1.263 links locais, 29 recursos e nenhum erro ou aviso. Ambos são verificações documentais; não provam que os inventários contenham todos os enunciados nem a precisão da ciência, representação visual ou acessibilidade. Não houve navegador real, estudantes, leitor de tela ou revisão humana. QA-09 permanece em correção.
