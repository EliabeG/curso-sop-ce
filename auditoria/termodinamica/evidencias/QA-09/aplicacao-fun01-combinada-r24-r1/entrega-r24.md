# QA-09 — aplicação combinada FUN-01 r23 → r24

30/10/2026. Executor `/root/next_examples`. **APLICADA, AGUARDANDO AUDITORIA INDEPENDENTE E REVALIDAÇÃO LOCALIZADA**. A coordenação autorizou a aplicação após parecer das três candidatas; este registro não é aceite científico da versão efetiva nem encerra QA-09.

As seis substituições das propostas delimitam o modelo de mistura de gases ideais e seu estado padrão, o líquido puro sob gravidade, e o potencial total que inclui energia gravitacional sem dupla contagem. O problema subsequente não foi automaticamente revalidado.

## Base e propostas

- Aula r23 `f847c5be0640039f1f6090407fc37f39b7833c7a97f1e5958d77f78e884ce85d`, inventário `ae7cfa82b64f1118ed292f5c9e4d42cdf6f5871db8b13598b16506bf382a905e`. Parecer aplicação r23 `QA-09-aplicacao-resumo-glossario-r23-auditoria-independente-20261030.md` SHA `d0001b287a4bbf04b02f9572e1718d3c1441bf96a39f08b98c0f33486c22e169`.
- As candidatas gases, líquido e gravidade usam o mesmo `fun01-preparacao-equilibrio`, original UTF-16 [107020,111548), SHA `6a58642fcfbbe49b936c53ea8be9c679fa45607ac3e200fcaf836e12bd1c7a2e`. Seus manifestos têm SHA `797fe338ed7108cf2e3644868ffea7d7ce900bd88511dff26df8c79c6a996e1c`, `129a789ff993feb9419ea2a327bee46a83fd9acdb595f03d0ddde73a7246b027` e `a6be90eb5c2cc40229f7807bacd90afc5e7d8db9d8807e4c4bdf4e5f5f6e2a61`.
- Parecer das candidatas `QA-09-candidatas-fun01-r23-auditoria-reference-triage-20261030.md` SHA `1416ce53a60bbb36f58cf4e5c31203971fe73de467f9a746a2535f4ea9daa600`: aprovou isoladamente as propostas e calculou combinação hipotética; não aprovou a aplicação efetiva.

## Composição e ensaio

O executor `aplicar.mjs` SHA `c94a2500d8b1db07aad57c66512a6b74c8a47cb8e301c0c71225085b00da893b` fixa hashes da r23 e dos pareceres e manifestos; confere que os três originais são idênticos e cada candidata individual corresponde a suas substituições. Localiza as seis substituições no **mesmo original**, exige unicidade e intervalos disjuntos e aplica-as em ordem de posição decrescente para montar uma única substituição do contêiner. Verifica o bloco combinado SHA `9e6c7edc5562eba7c10143cd0af90d4b61a8f6398abe96ffb39031e9a5a4e736` e a aula combinada SHA `2e59d1d896056ecd05353eefe668bab18b8ab3aa5be89d3284c64aff678805f9`, ambos previstos no parecer independente. Preserva snapshots antes/depois em `resultado/` e exige destinos novos. Deltas e as seis faixas originais constam de `resultado/edicoes-aplicadas.json` SHA `b28075447ebfbcc0fddfb74950260598a661061c91341339b94d5bd490c80e16`.

Gerador `inventariar-r24.mjs` SHA `372fa2c6e039a49a72acb0bd1c7fafa99c88c968683eb85ea1042de96b55466a`; mapeador `mapear.py` SHA `d9441f8bde8801dad81686e40b8c6b3bb59bf9b1236953e8ff20af59d1ad0409`. Ensaio de `--apply` ocorreu em cópia descartável sob `/tmp`, seguido de aplicação na base autorizada. Aula, mapa e inventário oficial do ensaio coincidem byte a byte com os efetivos; `verificacoes-ensaio.json` e `resultado/verificacoes.json` SHA `a6683d6f35bcad0baa24ccc784f9015ea3a3cac535b06967b810aaeb2e79ea40`. O status do ensaio indica auditoria pendente porque foi usado `--apply` em cópia. O executor não é transacional: falha após escritas exigiria examinar e reconciliar o estado antes de repetir; nesta execução completou sem erros.

## Fotografia efetiva

- Aula r24 `2e59d1d896056ecd05353eefe668bab18b8ab3aa5be89d3284c64aff678805f9`; formulário preservado `694ee3d26e8f5679d565986cfb0ad8c10aa98667fc8ffb62a569a87679847a58`.
- `inventario-r24.json` SHA `469e91837b8b1c5cccd6512d7f27b8b8cd6ce7f385de87b34fce6e388c7440cf`; mapa `mapa-correspondencia-inventario-r23-r24-r1.json` SHA `63b3b5fc54566c617eb025458fec7dce979369dc180d01ec3bdc4a0ff31c9044`.
- Inventário oficial JSON `b422042bf2df46dfa9b8fcb33b9aad327cc8792c3726950352055a4cd8f33fd2`; histórico Markdown `73d27a6b780c3e097f32a5a976b3ffb22e6a74d94a2340602d824cf42e58d7ab`.
- Preservados 197 artigos e registros, os 734 elementos MathML da aula em bytes, o formulário e os atributos de identidade/links/ARIA testados. Validador canônico conferiu 1263 links locais e 29 recursos sem erros ou avisos.
- Mapa de 11400 ocorrências em cada fotografia: 11381 pares externos, um ancestral e 18 internos a conferir. Há 816 referências e 138 ocorrências de recursos, sem referências novas ou alteradas. Correspondência estrutural não transfere aceite científico.

Solicita-se Auditor distinto para conferir as seis alterações efetivas, o problema/contexto e os pares mapeados, com revalidação localizada. As verificações não certificam mérito científico integral, apresentação, acessibilidade real ou aprendizagem.
