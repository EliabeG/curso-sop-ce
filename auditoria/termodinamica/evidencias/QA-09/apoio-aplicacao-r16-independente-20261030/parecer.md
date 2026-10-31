# QA-09 — apoio estrutural independente da aplicação efetiva r16

Data: 30/10/2026. `/root/next_graphics`; executor `/root/next_formulas`. **Apoio estrutural favorável, limitado à fotografia e às conferências abaixo.** Fui Auditor das candidatas 89/90, do mecanismo de ensaio r16 e identifiquei ressalvas na teoria; a auditoria científica e o veredito da aplicação são do Auditor principal distinto `/root/planning`. Este parecer não encerra QA-09 nem transfere aceites anteriores.

## Identidade e reconstrução

Entrega do executor `aplicacao-conjunta-r16-r1/entrega-r16.md`, SHA `23000a62d5f844d37de7513e1ea177d0f3300ce1a1e179fe77b4d5032a0006fe`. Aula efetiva e snapshot posterior `55754bfc631da9010e3c9afc73e3c458e349b535c429fe98abe28998897aab23`; formulário efetivo e snapshot posterior `dea4923117d09fa77cabacb0b65816cbf6d57b724d88285003804a1f1440389d`. Antes, respectivamente `f6c461f1d6039ea47dc7e97f9ad734bb0ea3fcb902f01ffdbf18d18d88e08d0e` e `3ea110fda92c74253b69d89f5a6e62b288aa3bd99db6a51b54a6c67c8af82fce`.

A partir dos snapshots anteriores, os cinco intervalos UTF-16 em `edicoes-aplicadas.json` SHA `544ea43568eed6ef44aaf6710a81cd11b815bc6bf7bf8da3a36c6f96b4a449b7`, e os fragmentos de candidatas de manifestos identificados, reconstruí os dois documentos integralmente em memória, obtendo os bytes efetivos. São os três blocos COP, Carnot, Brayton e as fichas 89/90. Os hashes dos recortes de antes/depois e o registro das edições coincidem com o mapa. A comparação estrutural não substitui releitura científica da versão aplicada.

## Impactos e mapa

Inventário r15 SHA `c8c9c3a3e141eba47a16e9f85c69f97c6e8b8a55aab689c6120ef1a0070c9d9c`; r16 `2c4d4da464488f7eab06b6d56d32d83b27fdbb542aaa1d847a412d18c955cbcd`; mapa efetivo SHA `a3edb9fab577c58e5b3df4831ee8cfb09d8e8b39bf92d1efcd5e0a5f39b2d4d0`, idêntico ao mapa cujo ensaio auditei em `auditoria-ensaio-conjunto-r16-20261030/parecer.md`. Todos os 11.399 IDs anteriores e 11.400 posteriores aparecem uma única vez e os hashes por par conferem com os inventários. Permanecem 11.021 pares externos, três ancestrais, 375 internos que exigem conferência e um nó adicionado/reestruturado. Na auditoria do mesmo mapa no ensaio, inspecionei os 11 hashes internos alterados e o texto novo de COP; pareamento por sequência e contexto não comprova semanticamente cada ocorrência.

Recomparei independentemente os 197 fragmentos de artigo e seus hashes; os 197 registros oficiais mantêm os mesmos itens e demais campos fora de `fonte`, que aponta à aula e snapshot efetivos. A nota oficial preserva todo o conteúdo anterior como prefixo e acrescenta registro r16. As outras 98 fichas são idênticas byte a byte; os 734 MathML da aula e 191 do formulário coincidem integralmente, em ordem. Os campos de 816 referências e 138 relações de recursos coincidem; para recursos diferentes dos dois documentos alterados, os hashes permanecem iguais. Os hashes destes dois documentos são atualizados conforme suas versões.

Executei o validador canônico na árvore efetiva: 197 artigos/itens, 1.263 links locais e 29 recursos, sem erros ou avisos. São verificações documentais, não validação de conteúdo físico, didático, apresentação, gabarito ou aprendizagem.

## Reprodução e limites

`python3 auditoria/termodinamica/evidencias/QA-09/apoio-aplicacao-r16-independente-20261030/verificar.py`, SHA `35dde09f22d87719c507a6b2daec5e293d3d7470ab347197f35160b640f2a670`, retornou `ok: true`. O teste é somente leitura e usa os inventários fornecidos, de modo que não prova captura de todos os conteúdos; comparação estrutural não substitui auditoria do significado, fontes, imagem ou navegação. Não houve navegador, leitor de tela, estudantes ou revisão humana. O parecer científico localizado, a reconciliação integral e QA-09 permanecem com o Auditor principal e a coordenação.
