# Aplicação conjunta r20 → r21 — EX-046 e entropia da oficina

Estado: **APLICADA, AGUARDANDO AUDITORIA INDEPENDENTE E REVALIDAÇÃO LOCALIZADA**. A autorização de aplicação conjunta foi dada pela coordenação após os pareceres das duas candidatas. Este registro não constitui aceite científico da aplicação nem fechamento de QA-09.

## Identidade e aprovação

- Fonte r20: `modulos/e1-termodinamica.html` SHA-256 `b05a68731a6975755c0030c524e7915d7833aacb176f680b3890fe82efc803e7`. Formulário, antes e depois: `694ee3d26e8f5679d565986cfb0ad8c10aa98667fc8ffb62a569a87679847a58`.
- EX-046: somente `candidata-ex046-r20-20261030-r3`, manifesto `a453b56ec947c4d536ab7656543304afcb279acbb52a679cd95950a1dbc221e6`, fragmento candidato `b4d9dafa1f27c766cc44a698709d74f5fbe3ee09cc587c8def6e0709e2f36c55`; parecer `QA-09-candidata-ex046-r3-r20-auditoria-independente-20261030.md`, SHA `c81e514296b3df47bdbff560de6056b3300524faefe7053bed69ce782a320667`.
- Oficina: `candidata-entropia-oficina-r20-20261030`, manifesto `b8a2879422c561eb2e3f42996d781e88c7896d75d9085fb8b4ddeb8172e3ac52`, parecer `QA-09-candidata-entropia-oficina-r20-auditoria-reference-triage-20261030.md`, SHA `ceaccc705434ece169a161a47c76e85e6e74f1e2a4670886531d11ac9b6bcb83`.
- Aplicação r20 previamente examinada em `QA-09-aplicacao-mistura-fase-r20-auditoria-independente-20261030.md`, SHA `05d422302a58ecbfbd5c8a6651c137dd04b214a08c07b975d77276b5a5673b11`.

No EX-046 foi explicitada a alimentação elétrica de 1200 W, inteiramente convertida na geração térmica de 1200 W que sai por convecção, sem somar as duas como entradas distintas. Na oficina delimitou-se a geração de entropia ao conjunto correspondente, incluindo as interfaces; não se atribui ao interior do reservatório a geração total. Dados e resultados originais foram preservados. A candidata r1 foi rejeitada quanto ao balanço energético; o diretório r2 sofreu colisão entre autores e permanece preservado no estado inconsistente, sem alegação de recuperação. Nenhuma delas autoriza esta aplicação.

## Ensaio e execução

O executor `aplicar.mjs` (SHA `caa5014e84c78f05b1ea144da25bc08ea4d612258f286b59ca32ea1ca072919c`) fixa hashes da r20, pareceres e manifestos, identifica trechos e substituições, exige destinos novos, preserva snapshots e valida os arquivos finais. `mapear.py` SHA `cda3a488bf57996cdc3a63977c342570a04b33773935a41300e0f88147292e30`; `inventariar-r21.mjs` SHA `4f629a69239b308459cd0302aa30dcdfeef6e343d6e5891d5649fb85185a994f`.

Em cópia descartável `/tmp`, as candidatas r1 e r2 foram inseridas, cada uma por vez, no caminho da r3 e rejeitadas pela guarda de identidade, sem alteração da aula; o parecer r3 adulterado foi rejeitado pelo SHA. O teste reproduzível `testar-guardas.py`, SHA `e31d572b98e8c6995b657bbeb64b72db67ef90c59ef1b0a9f0afc6471e327056`, executa esses casos somente em uma cópia r20 sob `/tmp`. Em seguida, a aplicação com os bytes válidos passou no ensaio; aula, mapa e inventário oficial resultantes foram comparados byte a byte com a execução efetiva. `verificacoes-ensaio.json` e `resultado/verificacoes.json` têm SHA `27b3df7c30ea98e13a2771b6f0d4e1619dadb1acb6cd481fc903f4b8bfaadcdf`. O ensaio usou `--apply` em cópia, portanto o estado registrado nele é o mesmo marcador de auditoria pendente, não uma indicação de alteração no produto.

O executor não é transacional: em caso de falha após o início das escritas seria necessário examinar e reconciliar o estado, não executar novamente às cegas. Nesta execução o comando completou e a validação terminou sem erros ou avisos.

## Fotografia efetiva e conferências

- Aula r21 SHA `239fb6d9f307170adbb74e389b798d1ff3c9b8e0d8d2d6d874457b8a65f40238`.
- Inventário r21 `inventario-r21.json` SHA `d1d480c1c4ce0a31f9f4f0b8bf234be60c9867feae9336fbeefb06162e2826f1`.
- Mapa `mapa-correspondencia-inventario-r20-r21-r1.json` SHA `6930666290d17dc5fc1d7c1375d4bf1a454d5a509d4578be691b58f463cdb99c`.
- Inventário oficial JSON SHA `8cb04d06ee8ede09ec33a9aac93c3192b32dab7183dfebcdc08ce66dc9d72864`; histórico Markdown SHA `4afae09ac21880c86db086486be7ce220bad08d399b0346452419e82b5e167c1`.
- Deltas em `resultado/edicoes-aplicadas.json`, SHA `7f0fe20342a1ef32aa119817ffa3710b4584b587c0761b0834e895c4596430f2`; snapshots antes/depois estão em `resultado/`.
- 197 artigos e 197 registros preservados, 734 elementos MathML da aula preservados em bytes, atributos de identidade/links/ARIA preservados; formulário integralmente idêntico. O validador canônico conferiu 1263 links locais e 29 recursos.
- Mapa: 11400 ocorrências em cada fotografia; 11380 pareadas externas, 2 com contexto ancestral e 18 internas a conferir; 816 referências e 138 ocorrências de recursos, sem referências novas ou alteradas. A classificação “conferir” requer revisão contextual, não representa aceite automático.

Solicita-se auditoria independente da aplicação efetiva, incluindo os deltas, pressupostos e a correspondência, e a revalidação localizada. Os testes estruturais não certificam nível avançado, correção científica integral ou aprendizagem.
