# QA-09 — aplicação conjunta de pressão, substâncias/ciclos e fichas de máquinas r27 → r28

30/10/2026. Executor `/root/next_examples`. **APLICADA, AGUARDANDO AUDITORIA INDEPENDENTE E REVALIDAÇÃO LOCALIZADA.** A coordenação autorizou a aplicação após pareceres das três propostas. Este registro não aprova cientificamente a versão efetiva nem encerra QA-09.

A aula recebeu a distinção entre pressão média e local em face plana, as condições de classificação de substância pura em equilíbrio líquido–vapor e os calores específicos constantes nas expressões fechadas ar-padrão. O formulário recebeu esclarecimentos nas fichas 43–45, 71–72 e 79 sobre correntes e trabalho não associado ao escoamento. Há três contêineres na aula e seis fichas no formulário; as nove regiões são disjuntas por documento. Os modelos, alternativas e limites são descritos nas candidatas e pareceres, não inferidos da contagem de regiões.

## Base e pareceres

- Aula r27 `9af8e2c9ffe509e40594d086a9ef4ad75127fb4ca873efb305d3144e08f3fc49`, formulário `16329b7369c4ba927f5f7da30551f86934aad1f6a6e55627443dea5cb9fe0c02`, inventário QA-09 `a58d7f0b0a5f097eef83ad83026ef49e801457b87f7cf2b2345c3dd915597c7c`; parecer r27 SHA `fb60390d209f81bb4bcca7fddfb62756b399d7da5ec93bf42220550fb95eb501`.
- Pressão: manifesto `70a4aa3e86d7604ee1281d493d702db8678b6517d88e8fbc9f61b7acde61e718`; parecer `auditoria-candidata-pressao-r28/parecer.md` SHA `84b0529c245994c4ed1fdac1bd246c11303ec1137dfe5dcdb9434c7efecbd83f`. Fui autor desse parecer sobre proposta de outro agente e executor da aplicação; o Auditor da aplicação deve ser distinto.
- Substâncias/ciclos: manifesto `536c06caca6923b0e431995fefb682bd196bc1ab95cf75c5ad2bd2cb5db60be6`; parecer `auditoria-candidata-substancias-r28/parecer.md` SHA `014b5a8e660ccdc9f5c5aab4541c2963ba2f158e23f5f7ec05377f9abe0fa39a`.
- Fichas de máquinas: manifesto `c8e9722f71bf08f28c0d97191a3c300f47a89054b9c9bc2bfd1682e3d4100be9`; parecer `auditoria-candidata-fichas-r28/parecer.md` SHA `92c9da7d254131e2aafc40dbad964b053e4cc9ad0e28ad583c6650479eb950e4`.

## Guardas e ensaio

`aplicar.mjs` SHA `3ad504998cf18aa9f89c270983f05c98c6aefd8f68a5a3d053cdd36e83e0b938` exige hashes das fotos, inventário oficial, quatro pareceres, três manifestos e todos os fragmentos; reconstitui as substituições, inclusive as duplicadas em texto visível e atributo de busca das fichas. Rejeita sobreposições e destinos preexistentes, calcula deslocamentos UTF-16 separados por documento e exige os hashes combinados previstos em memória. Antes das escritas, compara os 197 artigos, as 94 fichas não alvo, MathML e atributos ID/links/ARIA. Os nove intervalos e hashes constam em `resultado/edicoes-aplicadas.json` SHA `a4f84b742e543bad7453729bc41faf9629ed2739d4c60a60a53bf2a0f7265e7a`; snapshots antes/depois e inventários anteriores estão em `resultado/`.

A primeira fixture parcial passou pelo cálculo e mapa mas o validador falhou por ausência, na cópia, de PDFs e evidências locais referenciados pelos artigos. Essa falha ocorreu somente na cópia; nenhum resultado dela foi considerado ensaio aprovado. `montar-fixture.py` SHA `b40fff678f4b781631b877abc51de7a809fa746d816734d1b15c19c16cc3f457` montou nova cópia mínima de 25 MB com produto e arquivos de dependência local do inventário; nela, o executor completo e o validador passaram. Em seguida foi aplicado na base autorizada. Aula, formulário, inventário oficial e mapa coincidiram byte a byte com o ensaio. `verificacoes-ensaio.json` e `resultado/verificacoes.json` SHA `c1e1ff6da59cd5c098325597b7fb6967f6ff45c362140dce6d0e5bb60fca02d2`. O executor não é transacional: eventual falha após escrita exigiria examinar e reconciliar o estado antes de repetir; a execução efetiva completou sem erro.

Gerador `inventariar-r28.mjs` SHA `4bce09265481b96861791ed40839a49591dd0a88f2195dcc1c45b2708844da13`; mapeador `mapear.py` SHA `8a8eafa6acb54688d84c21b12271cc2f2b7470256b971b76da0da2d4bb709aed`. O preparo anterior limitado à pressão permanece preservado em `aplicacao-pressao-r28/`; não é a aplicação combinada.

## Fotografia efetiva

- Aula r28 SHA `d7294e8ed772cf4530788586d693a6cdfbf1ef6fa05c69afbc984efc46e353d8`; formulário SHA `3157c9b114f3156e5517440d30b91ee8a4efdebcd95be8bd0c7a588f04dead46`.
- `inventario-r28.json` SHA `0a7a12fbf0cd2a0898bcebfdfa7ae98c850bdb0bf7d2b34eea06cc6a8d9afb44`; mapa `mapa-correspondencia-inventario-r27-r28-r1.json` SHA `0e219e8d2863e3d7ced3af4857ce462ca5827bda38276da2a005e5f39e23eca2`.
- Inventário oficial JSON SHA `c7e74e1225da021725bc3c8e0652cadcf42eb0f4a8488f7beb97c631e092cd78`; histórico Markdown SHA `8802bf07dd555b135dc733a196d1de3ad8a103689e564dca8476a9849ee4e8d3`.
- Preservados 197 artigos/registros e 94 fichas não alvo; preservados em bytes 734 MathML da aula e 191 do formulário. Validador canônico examinou 1263 links locais e 29 recursos sem erros ou avisos.
- Mapa: 11407 ocorrências r27 e 11409 r28; 10889 pares externos, 6 ancestrais e 512 internos a conferir, 2 adicionadas/reestruturadas; 816 referências e 138 ocorrências de recursos, nenhuma referência nova ou alterada. Essas categorias não transferem aceite científico.

Solicita-se Auditor distinto para os nove deltas efetivos, pares internos/ancestrais e dois nós adicionais, além de revalidação localizada de contextos afetados. Não houve teste de navegador, leitor de tela, estudantes, revisão humana ou certificação externa.
