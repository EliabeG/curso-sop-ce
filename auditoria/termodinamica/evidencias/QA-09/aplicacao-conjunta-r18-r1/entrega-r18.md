# QA-09 — aplicação conjunta r17→r18, aguardando auditoria

30/10/2026. Executor `/root/next_examples`. Aplicadas após autorização da coordenação as quatro candidatas isoladamente aprovadas: ficha 60, exemplo EX-027, base da primeira lei e base de entropia de escoamento r2. **A fotografia efetiva aguarda auditoria independente; QA-09 permanece aberto.**

O executor `aplicar.mjs` SHA `670951670208d08dfe454bb2f5980ccac8eaa7040b56fadb110515d6d55a8a96` verifica antes de escrever os hashes das bases r17, do inventário oficial e nota, dos manifestos e fragmentos, do gerador e mapa, do parecer da r17 efetiva e dos dois pareceres das quatro candidatas. Reconstitui as mudanças literais, verifica unicidade e ordena edições por documento e posição. Recusa destinos preexistentes. Foi executado integralmente em cópia descartável e passou; em outra cópia, alteração de um parecer causou rejeição antes de gravar, com aula r17 preservada. A operação é sequencial, não transacional; em falha, snapshots preservados permitem reconciliação, sem garantia de reversão automática.

## Fotografia efetiva

- Aula r17 `6b0df1096d0b6de6995ffc51bf8489cb45ab954a7aabdeb3f48d068c9777c57c` → r18 `7f09b3f0e53e4f3ed69225adf3ce8e03fda93f132e78a1e884ca5757cc995cca`.
- Formulário r17 `dea4923117d09fa77cabacb0b65816cbf6d57b724d88285003804a1f1440389d` → r18 `463c00149e36217404cf98bad4f5bed3db828c87d19d1c8e6038678193e9d895`.
- Inventário estrutural r18 `717f00621d1740b4c71aeb6e9f492a621489fc86b5c1cffca59cf9584a964acc`; mapa `mapa-correspondencia-inventario-r17-r18-r1.json` `54ef57e0479f4a8143fd5c7fde4021e45330d0125da939b02bc08fe3855ac1a7`.
- Inventário oficial JSON `c948abe1f4e11590aa7c7fd4f7134487d59278d5c6ff2008b164a9e07710ecc8`; Markdown `3c5cdd282fa1c5232e0cc0b7b41b2637638696d9bfc287b602287a4fba4553e5`.
- `resultado/verificacoes.json` SHA `eb4d203940de15db10e2327f45373a222c195c5cdf83c094e496786e5a098800`; `resultado/edicoes-aplicadas.json` `6d42381836716cacb55b44d4ee89a3783b351d17496693547103fbaba59b6f7b`. Fotografias antes/depois e controles oficiais anteriores estão em `resultado/`.

Os resultados de verificação e o mapa foram comparados byte a byte com os do ensaio. A execução verificou os 197 artigos da aula e os 197 registros oficiais, as 99 fichas não alvo, 734/191 elementos MathML, links e parser. O mapa conserva 11.400 ocorrências em cada fotografia: 10.969 pares externos, quatro contextos ancestrais e 427 pares internos a examinar; 816 referências e 138 relações de recursos mantidas. O validador canônico passou com 1.263 links locais e 29 recursos. Isso não valida URLs remotas ou mérito pedagógico.

Solicita-se ao Auditor distinto que confronte a versão efetiva, os quatro deltas e pareceres, snapshots e controles, pares internos e ancestrais, referências/recursos e efeitos localizados em FOR-01/FUN/BAN. Não houve navegador, leitor de tela, estudantes, revisão humana ou certificação externa. Nenhum aceite é automaticamente transferido por hash.
