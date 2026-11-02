# QA-09 — aplicação de refrigeração r28 → r29

**Estado: aguardando auditoria independente.** Aplicada somente a candidata `candidata-refrigeracao-r29-r2`, aprovada em `auditoria-candidata-refrigeracao-r29/parecer.md` (SHA-256 `4ccf05816e95956e01947be55df06479c5133bfc4d6136a0fefe641ff0a54bf3`); manifesto SHA-256 `baadc04397c422c6a68089376272983a67bab336a44be9ce7064323254c6458e`. Foram alterados `base-refrigeracao`, `formula-refrigeracao` e `formula-condensador`. A candidata opcional EX028 não foi aplicada, pois sobrepõe a base; a aprovação atual não autoriza presumir sua aplicação. O parecer registra a limitação de que coincidência exata pressupõe saldo nulo dos demais trabalhos, enquanto saldo desprezível dá aproximação; solicita-se exame do texto efetivo pelo auditor.

## Ordem real e incidente de procedimento

Criou-se primeiro uma cópia mínima da fotografia r28 em `/tmp/curso-r29-fixture-minima`. Por erro de diretório no comando seguinte, o executor foi iniciado no produto real, antes do ensaio na cópia. A aplicação efetiva estava autorizada, mas essa sequência contrariou a ordem solicitada. O coordenador foi avisado imediatamente. Em seguida executou-se o mesmo executor na cópia r28 criada antes da alteração, com sucesso; seus resultados foram comparados byte a byte aos efetivos. A comparação é retrospectiva e não transforma esse ensaio em teste prévio. Nenhum histórico foi sobrescrito; os snapshots antes e depois e os resultados estão em `resultado/`. O executor grava múltiplos arquivos e não é transacional.

## Fotografia e evidências (SHA-256)

| Arquivo | SHA-256 |
|---|---|
| aula r28 | `d7294e8ed772cf4530788586d693a6cdfbf1ef6fa05c69afbc984efc46e353d8` |
| formulário r28 | `3157c9b114f3156e5517440d30b91ee8a4efdebcd95be8bd0c7a588f04dead46` |
| `modulos/e1-termodinamica.html` r29 | `f932d341a543f05b9f7b31b037cb28f21f8d4e9933536656475f99fd3d3ba7d5` |
| `formulas/termodinamica.html` r29 | `b839310edfa655e1da907757119beaeacdabd7d088211ac189c38c3dbeb38932` |
| inventário oficial JSON | `f2d9b05de954341a2ca6dd46a4976c0214e71bf6d0a64659df49d92019a1f111` |
| inventário oficial Markdown | `663e953cfcc3b28fb1d43802254b8b938bc1648be7926271766b8d031e118f95` |
| `inventario-r29.json` | `f6237de0c999a66c1edbb74f18911d4bd13ba0352d305b32329f3d7f4fd05db8` |
| `mapa-correspondencia-inventario-r28-r29-r1.json` | `a05800b66c6d56aa791cb16a251007ee26c6d4fef50c2fe7b42a2a104e8b21ba` |
| `resultado/verificacoes.json` | `027fef88849a015afffe4a57b233d8593b562b9a58b41b3d275b583182507ab9` |
| `resultado/edicoes-aplicadas.json` | `2076701f368e439180de5fa896e2451f747e51130df625d4f1ef54a3eddf26a3` |
| `aplicar.mjs` | `e57a5b5fc6594f82d96971e8eda90d80b73cde2d8ab063f414994d07792470a3` |
| `mapear.py` | `b8c2a20bcdc8b5e20be331d734426892d15b490e56ec2de03f02cf052fa2df87` |
| `montar-fixture.py` | `aaaf370953f20ddc99a8becd2912ed8ed82e718e31c14fadb1f937b22be9298f` |
| `verificar.mjs` | `8e4e3725daa13f31d7500141090186b274eee8c06c47b20379304814753844a8` |
| `inventariar-r29.mjs` | `94085b5668ee53df3b3268da4ff7269819c7ef5ebf80a95661e733665f1d92b1` |

## Verificações

O ensaio retrospectivo terminou com código zero; as duas páginas, os dois inventários oficiais, a fotografia QA, o mapa, as edições e as verificações produzidas foram idênticos byte a byte aos artefatos efetivos. A execução com guardas reconstruiu três substituições aprovadas, preservou os 197 artigos e registros, 98 fichas não alvo, 734 elementos MathML na aula e 191 no formulário, e as listas de atributos id, href, src e ARIA examinadas. O mapa contém 11.409 pares, dos quais 11.095 externos, 312 internos e 2 contextos ancestrais a conferir; 816 referências e 138 recursos, com zero referências novas ou alteradas. Esses pares classificados para conferência não são aceites científicos automáticos.

O validador oficial retornou `ok`, 197 itens/artigos, 29 recursos e 1.263 links locais verificados, sem erros ou avisos. Execute da raiz `node auditoria/termodinamica/evidencias/QA-09/aplicacao-refrigeracao-r29/verificar.mjs` para reconstruir os dois documentos dos snapshots e da candidata, conferir artigos, registros, fichas, MathML, hashes da fotografia e mapa, e executar novamente o validador oficial. O teste é somente leitura e não certifica mérito científico ou QA-09 integral. A comparação com a fixture foi realizada quando ela existia no ambiente temporário, não é pressuposta como persistente.
