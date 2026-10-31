# QA-09 — aplicação de radiação, geração e diagnóstico 14, r21 → r22

30/10/2026. Executor `/root/next_examples`. **APLICADA, AGUARDANDO AUDITORIA INDEPENDENTE E REVALIDAÇÃO LOCALIZADA.** Aplicação autorizada pela coordenação após parecer sobre as propostas. Esta entrega não é parecer independente, nem encerra QA-09.

A radiação passa a explicitar superfície mais quente e razão com taxa líquida inicial não nula; o balanço de geração identifica conversão e a fonte que sustenta a energia total; D14 identifica 120 W de entrada elétrica convertida integralmente, sem dupla contagem. Os demais dados, a solução e resposta de D14 permanecem preservados.

## Base e aprovações

- Aula r21 `239fb6d9f307170adbb74e389b798d1ff3c9b8e0d8d2d6d874457b8a65f40238`; inventário `d1d480c1c4ce0a31f9f4f0b8bf234be60c9867feae9336fbeefb06162e2826f1`. Parecer da aplicação r21 `QA-09-aplicacao-oficina-ex046-r21-auditoria-independente-20261030.md`, SHA `9120c14a6ef6fc57a708dfaa977bc29f878b2218c4795dc78ff477243436054b`.
- Propostas, na ordem radiação, geração e D14: manifestos `a7b4877d109906aba6d4f51be22420274ff2936c6f68179bf4819bbd69309ceb`, `2616d8bf3b2477c68fc048c4add550fba0d18983edc5a196af060d7f7240e765`, `fbc5a66bcca961949af11ab5f4aacd21bda5c855964412439cc89b54f2c23015`, em `candidata-{radiacao-pontes,geracao-pontes,d14-fonte}-r21-next-theory-20261030/`.
- Parecer independente das três candidatas `QA-09-candidatas-pontes-d14-r21-auditoria-reference-triage-20261030.md`, SHA `10ac8b030cd6043b2a4d6ed66bc35e9713db7ea10aca3964c929d6402aa22c97`; o HTML combinado previsto é `ddf6edd271e38eb318ff1756cfa60f5bc8632882357de2401c114479cb3a432f`.

## Execução e rastreabilidade

Executor `aplicar.mjs` SHA `97622e51fce670cdea272b34920b229844530372f05a87d4fb3642a5d79ea866` verifica hashes de documentos, inventários, pareceres, três manifestos e fragmentos, offsets UTF-16, unicidade, substituições e hash combinado aprovado. Exige destinos ainda ausentes e grava snapshots em `resultado/`. Mapeador `mapear.py` SHA `936a08cdea0716c0fa19159b61c989ff765a82a5b4bcb436839c25a567e153b4`; gerador `inventariar-r22.mjs` SHA `44311743245349cc45a336b212d1415b68933ac6ae7965837ed0f9ebb174725c`.

O executor foi ensaiado com `--apply` em cópia descartável sob `/tmp` e depois aplicado à base efetiva autorizada. Aula, inventário oficial e mapa do ensaio coincidiram byte a byte com os efetivos. `verificacoes-ensaio.json` e `resultado/verificacoes.json` têm SHA `c1af2b10ab9edf079c9ea8c29259ca93537556bd5c4a16440d1a1538d836abc3`; o status do ensaio assinala auditoria pendente porque usou `--apply` em cópia. Deltas `resultado/edicoes-aplicadas.json` SHA `b8fb1d8c6f705be88e44612a446f9d61e4426a248681047f994f1348403f4095`.

O executor não é transacional. Se houver falha após escrita, é necessário examinar e reconciliar o estado antes de nova execução; nesta execução o comando terminou e as verificações passaram.

## Fotografia efetiva

- Aula r22 SHA `ddf6edd271e38eb318ff1756cfa60f5bc8632882357de2401c114479cb3a432f`; formulário integralmente preservado SHA `694ee3d26e8f5679d565986cfb0ad8c10aa98667fc8ffb62a569a87679847a58`.
- `inventario-r22.json` SHA `6e68d5a9e5cfec73aa2a5ce24121ede1c3a155ca2a5783cf6f17ca95eee8061b`; `mapa-correspondencia-inventario-r21-r22-r1.json` SHA `75dd6be7387e4dce4c1b7717a9a6416b5c3329e01776e146a83708fdd47bb8a6`.
- Inventário oficial JSON SHA `93c240357e0e79784e21e791e0e18dd5d0324ddad6175bd0ec5ac47506e86836`; histórico Markdown SHA `7ae4e23da59766de6d1f41b006968d926a46f788e79c7cd6e0dfa39379462f68`.
- Preservados 197 artigos e registros, todos os 734 elementos MathML da aula em bytes e atributos ID, href, src e ARIA testados. O validador verificou 1263 links locais e 29 recursos, sem erros/avisos.
- Mapa: 11400 ocorrências em cada fotografia: 11350 pareadas externas, 2 ancestrais e 48 internas a conferir; 816 referências e 138 ocorrências de recursos, sem referências novas ou alteradas. Esses pares não implicam transferência automática de aceite.

Solicita-se auditoria distinta para os três deltas na versão efetiva, mapa e validação localizada. As verificações automáticas não certificam mérito científico integral, apresentação, acessibilidade real ou aprendizagem.
