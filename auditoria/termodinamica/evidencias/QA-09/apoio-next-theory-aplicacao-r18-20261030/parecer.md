# QA-09 — apoio estrutural independente r17→r18

Data: 30/10/2026. Apoio automatizado `/root/next_theory`; executor `/root/next_examples`; Auditor da aplicação `/root/planning`. **Resultado estrutural: sem divergência identificada nas verificações abaixo.** Não é parecer científico da aplicação nem aceite integral de QA-09. Este agente foi anteriormente Auditor das candidatas ficha 60/EX-027 e Corretor do lote que identificou as questões nas duas bases da primeira lei e entropia; por isso este apoio fica limitado a identidade e estrutura. O mérito da aplicação cabe ao Auditor da aplicação.

## Fontes e identidade

Entrega do executor SHA `6365391b3209bbfae78854eab21fb1ab4d597b49e0ebabd4fb57668e0ad26c68`. Aula r17 `6b0df1096d0b6de6995ffc51bf8489cb45ab954a7aabdeb3f48d068c9777c57c` → r18 `7f09b3f0e53e4f3ed69225adf3ce8e03fda93f132e78a1e884ca5757cc995cca`; formulário r17 `dea4923117d09fa77cabacb0b65816cbf6d57b724d88285003804a1f1440389d` → r18 `463c00149e36217404cf98bad4f5bed3db828c87d19d1c8e6038678193e9d895`. Os arquivos efetivos r18 são iguais aos snapshots do executor. Inventário r17 `b8eae39cc72cf807d7b84aad7e7a38423168b809231bc3b7f08c439d6d25163b`; r18 `717f00621d1740b4c71aeb6e9f492a621489fc86b5c1cffca59cf9584a964acc`; mapa r17→r18 `54ef57e0479f4a8143fd5c7fde4021e45330d0125da939b02bc08fe3855ac1a7`.

## Reconstrução de documentos e nós

`reconstruir.mjs`, SHA `fafdaced4a7a1495db4ca257365718f5f800b8e0ee97fa0a11eba82174efac74`, executado somente em leitura, reconstrói os dois documentos r18 byte a byte a partir das fotografias r17 e dos quatro deltas das candidatas. Compara os hashes de fragmentos e posições, reconstrói cada candidato por suas alterações literais e verifica conteúdo fora dos quatro trechos. Os 197 artigos da aula e os 197 registros do inventário oficial permanecem idênticos; no topo deste último apenas `fonte` mudou. No formulário existem 100 fichas em mesma ordem, das quais só `formula-cop-bomba-calor` mudou: 99 não alvo são byte a byte idênticas. Os 734 MathML da aula e os 191 do formulário permanecem byte a byte idênticos, assim como os valores dos atributos id/href/src e os atributos ARIA relacionados inspecionados.

O mesmo script reconstrói individualmente o HTML de **cada um dos 427 nós internos e quatro nós ancestrais** a partir dos nós correspondentes r17 e dos deltas aprovados, confrontando com os nós efetivos r18. Isso verifica o conteúdo estrutural de todos os 431 pares sinalizados; não confere automaticamente o mérito termodinâmico, apresentação visual ou equivalência de contextos não representados pelo parser.

## Mapa, referências e recursos

`mapa.py`, SHA `54537fff696a8c38f7c1878d911804adf1eac915aa1c0b87b9188bb64b1c6eb3`, reexamina 11.400 pares um a um, unicidade, hashes declarados, contexto e deslocamentos externos. Encontrou 10.969 externos com hash igual, quatro ancestrais com hash alterado, e 427 internos: 414 com hash igual e 13 alterados. Nos internos, a associação por ordem e contexto foi verificada, assim como a reconstrução literal descrita acima. Hash igual e correspondência de ordem não autorizam transferir parecer científico.

As 816 referências mantêm ordem e campos semânticos, incluindo destino e texto; fora dos blocos os deslocamentos previstos conferem. Os 138 registros de recursos mantêm identificação e destino; hashes de fontes alteradas correspondem às fotografias de origem/destino, outros são iguais. A lista de 197 artigos excluídos e os ativos específicos coincidem. Trata-se de comparação estrutural das listas: não testa acessibilidade, conteúdo de recursos visuais nem disponibilidade de URLs remotas.

Inventário oficial atual `c948abe1f4e11590aa7c7fd4f7134487d59278d5c6ff2008b164a9e07710ecc8`, nota Markdown atual `3c5cdd282fa1c5232e0cc0b7b41b2637638696d9bfc287b602287a4fba4553e5`; conteúdo pedagógico e reavaliação de FOR/FUN/BAN ficam para a auditoria principal. Não houve navegador real, leitor de tela, teste com estudantes ou revisão humana.
