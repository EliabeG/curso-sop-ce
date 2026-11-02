# QA-09 — aplicação de equilíbrio de fases FUN-01 r24 → r25

30/10/2026. Executor `/root/next_examples`. **APLICADA, AGUARDANDO AUDITORIA INDEPENDENTE E REVALIDAÇÃO LOCALIZADA.** Aplicação autorizada pela coordenação após parecer da proposta. Este registro não certifica mérito global nem encerra QA-09.

A alteração explicita domínios para pressões e divisão da regra de alavanca, o caso degenerado yA=xA e o uso de propriedade global independente quando as fases têm valores distintos, distinguindo fração mássica de molar e limites de fase incipiente. Os dados e fórmula do caso não degenerado são preservados.

## Base, aprovação e execução

- Aula r24 `2e59d1d896056ecd05353eefe668bab18b8ab3aa5be89d3284c64aff678805f9`, inventário `469e91837b8b1c5cccd6512d7f27b8b8cd6ce7f385de87b34fce6e388c7440cf`; parecer da aplicação r24 `QA-09-aplicacao-fun01-combinada-r24-auditoria-independente-20261030.md` SHA `e116e9143d5e560a8a3d82f62f20e1fe9533ada87578016d0e6ff4fc51252f0e`.
- Candidata `candidata-fun01-fases-r24-next-theory-20261030/`, manifesto SHA `41acd831e5777031626f6d09f8dd0943c5a836365499b41b60e78de1c41fd6b3`, original `e27bbd8622f3b1020c6d496a7dec7e42b4c503b7fe5b4a61d67c3560910610c8`, candidata `9c67154f940a4180fa7ca3030dcd13cff959bfd1feae9f9a6f696fc31a92d56c` sem a quebra terminal dos arquivos de fragmentos.
- Parecer `QA-09-candidata-fun01-fases-r24-auditoria-reference-triage-20261030.md` SHA `1aa75e54eb47b47997cd729d19804c19810b46146e5a42a56faf0c2ae2f5de86`, com previsão independente da aula r25 `ea0a7e3877c0a0250dac3d9c993c7922a03400929eb7a5dad39fcb27e3263c7e`.

O executor `aplicar.mjs` SHA `5a425d7df63908ba36c25cd1db9944946288609bd4531e0fc6e9f8c3fe78c123` valida hashes dos insumos, pareceres e manifesto, identidade e intervalo UTF-16, unicidade da substituição e hash final previsto; exige destinos novos e grava snapshots em `resultado/`. As edições estão registradas em `resultado/edicoes-aplicadas.json` SHA `fc3433c9a4ab51715a678640fe3353026fa20c195c7d0bf4ec9da4a8be3631e1`. Gerador `inventariar-r25.mjs` SHA `ecb25037b82f23046566440a7dbc4623d07822d93c4c5ec4b3c6f1347a9c2e10`; mapeador `mapear.py` SHA `767bc7b27e28f9ab8f17d04d304911986bf37da61fae082fe5c1411ff77ca9ff`.

Em cópia descartável sob `/tmp`, o executor com `--apply` passou; depois foi executado na base autorizada. Aula, inventário oficial e mapa do ensaio coincidiram byte a byte com a aplicação efetiva. `verificacoes-ensaio.json` e `resultado/verificacoes.json` SHA `04aa710183e2719136f0f33932a679068f50b8a3d7ac6fd85baf7474d9dd1bf3`; o status do ensaio indica auditoria pendente por uso de `--apply` em cópia. O executor não é transacional: falha após escrita exige reconciliar o estado antes de repetir; aqui o comando completou sem erros.

## Fotografia efetiva

- Aula r25 `ea0a7e3877c0a0250dac3d9c993c7922a03400929eb7a5dad39fcb27e3263c7e`; formulário preservado `694ee3d26e8f5679d565986cfb0ad8c10aa98667fc8ffb62a569a87679847a58`.
- `inventario-r25.json` SHA `6798d317db30bd69435ed14862cc03cd0f0c6313e40408dd8831052285984116`; `mapa-correspondencia-inventario-r24-r25-r1.json` SHA `2b39fde214b9e058e740fb0140f6c40105d5a710fe366ac8f147ce9ba59e4100`.
- Inventário oficial JSON SHA `f54332571e45cd5345f54cc972a909af6571bb1138e1d5a6555cc0d072f9be45`; histórico Markdown SHA `18e5cfda6abc7d90c776945921c98484e67a115317cd8051e3138321471dac0e`.
- Preservados 197 artigos e registros, 734 elementos MathML da aula em bytes, formulário e atributos ID/links/ARIA testados. O validador canônico conferiu 1263 links locais e 29 recursos, sem erros/avisos.
- Mapa: 11400 ocorrências r24 e 11405 r25; 11314 pares externos, um ancestral e 81 internos a conferir; 4 ocorrências removidas ou reestruturadas e 9 adicionadas ou reestruturadas. Há 816 referências e 138 ocorrências de recursos, sem referências novas ou alteradas. Essas classificações não transferem aceite e os itens reestruturados devem ser examinados em contexto.

Solicita-se auditor distinto para o delta efetivo, contexto e ocorrências reestruturadas, com revalidação localizada. Verificações estruturais não certificam mérito científico integral, apresentação, acessibilidade real ou aprendizagem.
