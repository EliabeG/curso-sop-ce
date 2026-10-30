# QA-09 — aplicação conjunta do resumo e glossário r22 → r23

30/10/2026. Executor `/root/next_examples`. **APLICADA, AGUARDANDO AUDITORIA INDEPENDENTE E REVALIDAÇÃO LOCALIZADA.** A coordenação autorizou a aplicação após parecer das propostas; esta entrega não é aceite científico da versão efetiva nem encerra QA-09.

O resumo agora delimita condições e base das expressões de turbina, válvula, rendimento, COP e Carnot. O glossário delimita COP para máquinas acionadas por trabalho e distingue o fator Z da compressibilidade isotérmica. As substituições e seus contextos estão nas candidatas e no relatório de edições.

## Identidades e autorização

- Aula r22 `ddf6edd271e38eb318ff1756cfa60f5bc8632882357de2401c114479cb3a432f`, inventário `6e68d5a9e5cfec73aa2a5ce24121ede1c3a155ca2a5783cf6f17ca95eee8061b`. Auditoria da aplicação r22 `QA-09-aplicacao-pontes-d14-r22-auditoria-independente-20261030.md`, SHA `8677608758127d1ae2e67fbbd10dab58ed48f5b7e2a80f7f2cf82b85c3812db3`.
- Manifestos das candidatas resumo e glossário: respectivamente `c893fbd1e95582add646f384f187d601993286a078455736d1a12b090befdbe9` e `1c6fbe50b85c9e4dd7be36c864af7767781c9748324748548d0e1e4fc98aacbd` em `candidata-resumo-r22-next-theory-20261030/` e `candidata-glossario-r22-next-theory-20261030/`.
- Aprovação isolada `QA-09-candidatas-resumo-glossario-r22-auditoria-next-formulas-20261030.md` SHA `d17a10211b76072724c069ae3134ff2e45324bc98de6f12eb1b5a09432e0f932`. Os ensaios desse parecer foram individuais; não se alegam ensaios conjuntos nesse parecer.

## Aplicação e posição das seções

O cálculo independente em memória substituiu primeiro o intervalo mais alto e depois o mais baixo, produzindo o SHA combinado `f847c5be0640039f1f6090407fc37f39b7833c7a97f1e5958d77f78e884ce85d`. Na r22, glossário ocupa UTF-16 [1285927,1288715) e resumo [1288716,1303056), separados por uma unidade. Glossário acrescenta 252 unidades e resumo 456; na r23 os intervalos são [1285927,1288967) e [1288968,1303764). A unidade entre eles foi preservada. `resultado/edicoes-aplicadas.json` SHA `2d02029dd9bbcde19e147be8c850147e8dc9cb8e9c0b383369e67b83195e03db` registra os hashes de cada trecho.

O executor `aplicar.mjs` SHA `ede18e78e891607454bcc5f7376fe97081add94e3bc4aaf55e0e2aa10e489296` valida hashes da base e pareceres, dois manifestos/fragmentos, substituições únicas, ordem, não sobreposição e separação de uma unidade, cálculo de deslocamento e hash combinado. Ele exige destinos novos e preserva snapshots em `resultado/`. Mapeador SHA `1897c357c0377a0b294f6128d0e6bd0613a577afd4a583d3c2fb4e9b626aa512`; gerador `inventariar-r23.mjs` SHA `5eb56b53d7405b299615f3da78141a0ac152748873f4c8c12b51e227262550e4`.

Em cópia descartável sob `/tmp`, o executor com `--apply` passou; depois foi executado na base efetiva autorizada. A aula, o inventário oficial e o mapa coincidiram byte a byte entre ensaio e aplicação. `verificacoes-ensaio.json` e `resultado/verificacoes.json` SHA `45537c5a2766ea80c9f7995c1eb78168f8e88e9aa9ee56403f83ddd1f2fb2d9a`; o status do ensaio é auditoria pendente porque foi usado `--apply` na cópia. O executor não é transacional; falha após escrita exige reconciliação antes de nova execução. Aqui o comando completou e todas as verificações passaram.

## Fotografia efetiva

- Aula r23 `f847c5be0640039f1f6090407fc37f39b7833c7a97f1e5958d77f78e884ce85d`; formulário preservado integralmente `694ee3d26e8f5679d565986cfb0ad8c10aa98667fc8ffb62a569a87679847a58`.
- `inventario-r23.json` SHA `ae7cfa82b64f1118ed292f5c9e4d42cdf6f5871db8b13598b16506bf382a905e`; `mapa-correspondencia-inventario-r22-r23-r1.json` SHA `9a3c42d4f075f6a686b969a34d82ae439270fd50d49f25458b1d494caa205dd0`.
- Inventário oficial JSON SHA `001a599d968cd9b1a2773ae42ca7174c9b64d2340016e8901dd06ff6b5d92159`; histórico Markdown SHA `be8d8adfa9e1b8734f2a1f97ecf1cfaf680779ef3f8ca17d9984a398de0560ff`.
- Preservados os 197 artigos e registros, 734 elementos MathML da aula em bytes, os atributos de identidade/links/ARIA testados e o formulário. Validador canônico conferiu 1263 links locais e 29 recursos, sem erros/avisos.
- O mapa tem 11400 ocorrências em cada versão: 11104 pares externos e 296 internos a conferir. Contém 816 referências e 138 ocorrências de recursos, sem referências novas ou alteradas. O pareamento estrutural não transfere aceite de conteúdo.

Solicita-se auditoria distinta dos dois deltas efetivos, das posições adjacentes e dos 296 pares internos, com revalidação localizada. Essas verificações não certificam mérito integral, apresentação, acessibilidade real ou aprendizagem.
