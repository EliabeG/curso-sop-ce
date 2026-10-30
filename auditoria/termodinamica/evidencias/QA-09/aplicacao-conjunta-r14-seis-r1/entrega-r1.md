# QA-09 — aplicação das seis candidatas na fotografia r14

30/10/2026. Executor automatizado `/root/next_examples`. Aplicado com sinal da coordenação, após pareceres independentes favoráveis às candidatas isoladas e ensaio; **aguarda auditoria independente da versão efetiva**. QA-09 permanece aberto.

O escopo aplicado é o das fichas 23/58/59, diagnóstico 23, contextualização OpenStax/MIT e base isentrópica r2. WIKA permaneceu fora desta aplicação; seu estado e eventual uso serão examinados separadamente. A operação registrou fotografias antes/depois em `resultado/`, as edições em `resultado/edicoes-aplicadas.json` e as verificações em `resultado/verificacoes.json`.

Fotografia efetiva:

- Aula `modulos/e1-termodinamica.html`: SHA-256 `572b172b29e1aa26873d191ebd827414c99f3122491c6d4c8129a69443f7389c`.
- Formulário `formulas/termodinamica.html`: SHA-256 `3ea110fda92c74253b69d89f5a6e62b288aa3bd99db6a51b54a6c67c8af82fce`.
- Inventário oficial JSON: `51fc95f2d08d2f923ec650e568666cc6bc1cb28d76b8b0db2d1a55dcdb6bb37e`; Markdown: `720934cfd43a307c853b12401ea1f19e81582e3cf64c6269c2bbe166c45bfc77`.
- Fotografia estrutural `inventario-r14.json`: `6505b06f3f3ef15bc2904f8a604f6e1f0fa6cf22af822394b2c2a871437b6175`; mapa `mapa-correspondencia-inventario-r13-r14-r1.json`: `a43156dad32d5529850bdd4c40209c68a772fee45cfd8651e3f9b0becaa1ff07`.
- Verificações `resultado/verificacoes.json`: `1b2e721f467483eff71be4860ffb034766c7ff4330a5bca419b6fcf8f50b59cd`; registro de edições: `08b9cc3de0359438725ba5d29cc8cb9f2af883c221edfc1e13dd723c09b038dc`.

Esses hashes de aula, formulário, inventário estrutural e mapa coincidem com o ensaio anterior. Foram preservados byte a byte os 197 artigos e seus 197 registros, as outras 97 fichas e todos os 734 MathML da aula e 191 do formulário. O mapa conservou 815 referências prévias, registrou uma nova referência MIT e preservou 138 relações de recursos. Há 11.178 pares externos de hash igual, 5 contextos ancestrais alterados, 214 pares internos e 2 ocorrências adicionadas ou reestruturadas que requerem conferência localizada. O validador canônico passou com 1263 links locais e 29 recursos.

Solicita-se ao Auditor distinto confrontar fotografias, seis deltas, pareceres correspondentes, registros do inventário oficial, contextos alterados, referência MIT, mapa e alcance FOR-01/FUN/BAN. Preservação automática de hash não transfere aprovação sem exame. Não houve teste de navegador, leitor de tela, estudantes, revisão humana ou certificação externa. O resultado não demonstra conclusão do curso ou QA-09.
