# QA-09 — apoio estrutural independente da aplicação r23

30/10/2026. Auditor automatizado `/root/next_graphics`, distinto do executor `/root/next_examples`. **Apoio estrutural favorável à fotografia r23** no escopo abaixo; julgamento científico e veredito da aplicação pertencem ao Auditor principal `/root/planning`. Auditei a ponte de ledger r22 e ofereci apoio estrutural à aplicação r22; não preparei as duas candidatas nem apliquei a r23. Esses vínculos não constituem auditoria científica dos deltas. QA-09 permanece em correção.

## Identidade e reconstrução

Entrega `aplicacao-resumo-glossario-r23-r1/entrega-r23.md` SHA-256 `e7c1056904b6ab472f30fe8d91d1250b0a9e9d03694865f3644138847c279936`. Aula r22 `ddf6edd271e38eb318ff1756cfa60f5bc8632882357de2401c114479cb3a432f` → r23 `f847c5be0640039f1f6090407fc37f39b7833c7a97f1e5958d77f78e884ce85d`; formulário antes/depois `694ee3d26e8f5679d565986cfb0ad8c10aa98667fc8ffb62a569a87679847a58`. Fotos posteriores coincidiam byte a byte com os arquivos efetivos durante o teste.

Reconstruí a aula inteira em memória com os dois fragmentos das candidatas, depois de verificar os hashes dos manifestos, fragmentos originais e novos e registro de edições SHA `2d02029dd9bbcde19e147be8c850147e8dc9cb8e9c0b383369e67b83195e03db`. As seções `glossario` e `resumo` têm uma unidade UTF-16 entre elas, preservada na r23; o deslocamento foi conferido no conjunto. A reconstrução prova identidade da aplicação, não mérito físico.

## Mapa e preservação

Inventário r22 SHA `6e68d5a9e5cfec73aa2a5ce24121ede1c3a155ca2a5783cf6f17ca95eee8061b`; r23 `ae7cfa82b64f1118ed292f5c9e4d42cdf6f5871db8b13598b16506bf382a905e`; mapa `9a3c42d4f075f6a686b969a34d82ae439270fd50d49f25458b1d494caa205dd0`. Cada uma das 11.400 ocorrências consta uma vez nos pares: 11.104 externos com fragmentos iguais e 296 internos a suas edições com arquivo, tipo, tag, seção e âncora correspondentes. São 55 internos do glossário e 241 do resumo; respectivamente quatro e 11 mudaram de hash. Os alterados abrangem as duas seções, o contêiner e a tabela do resumo e 11 textos internos. Correspondência e hash não transferem automaticamente aceites científicos.

Os 197 artigos e registros oficiais permanecem iguais; a fonte documental foi atualizada e a nota anterior é prefixo da atual. Formulário inteiro e 100 artigos preservam bytes. Os 734 MathML da aula e 191 do formulário coincidem em sequência. Comparei campos de 816 referências e 138 relações de recursos; hashes de recursos permanecem iguais, com atualização da aula. Isso não comprova acesso remoto ou qualidade dos conteúdos vinculados.

## Reprodução e limites

`python3 auditoria/termodinamica/evidencias/QA-09/apoio-aplicacao-r23-independente-20261030/verificar.py`, SHA `88391c2357f39ba8713dd1d87d9c2b0d493223e470094e6a6c51e4ee3b8d9487`, passou, somente leitura. O validador canônico retornou 197 artigos/itens, 1.263 links locais e 29 recursos, sem erros ou avisos. As verificações usam inventários existentes e não demonstram captura integral, mérito científico, apresentação visual, acessibilidade real ou aprendizagem. Sem navegador real, alunos, leitor de tela ou revisão humana.
