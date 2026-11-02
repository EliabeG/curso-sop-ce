# QA-09 — integração localizada das 100 fichas na fotografia r30

30/10/2026. Integrador `/root/planning`. **As 100 revalidações pelo integrador aguardam Auditor independente.** A base integra por referência o ledger `ledger-r30-direto-r2/ledger.json` SHA `58d31ac8b26366c543cc439b3b4dc0c7c9428d191949c8ac49d801b4a459dc12`, com parecer independente `auditoria-ledger-r30-direto-next-formulas-20261030/parecer.md` SHA `e0e46c5ad44ff523cdcd50ab14c156db48fb0cf756297673fa4192f1d7d5d2ee`. Os 78 objetos anteriores são preservados; 22 já são fichas, e 78 fichas novas são identificadas sem contá-las duas vezes como resultados independentes. O estado padrão das coleções permanece pendente e QA-09 aberto.

A foto é a aula `c719adae3464fb56ed2b0ad7014e0721c0aab2da444fb484ec0b40c5c0c8fbd4`, formulário `949c44fc5b96703929770b2881383d449af890616d34b9ab10b998ca96c75749` e inventário `1ce69fc1ab71850abc3ab8dc3df82b04e78788b9e62a55919c609a708a7979b4`. [Reconciliação por ficha](reconciliacao.md) SHA `1f6e770dc1f6afb070356ab5e6ecb5da053f44bc960532cf30bb90d42cd33b0f`; `notas.json` SHA `319015a059e7da5d592fd9995513e720713723fa3a949f06bc8f037ac979fc75` fixa resultado, efeito de contexto e ressalva para cada uma. Os estados expressam apenas o juízo do integrador, pendente de revisão distinta.

Oito fichas mudaram desde a r27: 43/44/45/71/72/79 na r28, 84/85 na r29 e 84 adicionalmente na r30. Os pareceres das aplicações são associados a cada ficha alterada; a r29 foi aprovada estruturalmente com ressalva, e r30 corrigiu a distinção entre igualdade exata (saldo nulo) e aproximação (saldo desprezível). Onze fichas têm contexto vinculado alterado: 01/02/03/05/10, 21/22, 82/83 e 84/85. Limites e recomendações de denominadores, modelagem e autonomia permanecem no relatório e não são apagados.

Dois esclarecimentos de evidência são registrados sem regravação histórica: o parecer das fichas 45–66 foi esclarecido por sua autora para delimitar o ajuste obrigatório na 45 e o parecer localizado favorável nas 46–66; e o parecer de next_theory sobre 84–100 continha um dígito de SHA divergente, já objeto de errata. A identidade e mérito de 84–100 nesta integração usam o parecer independente de reference_triage que fixa o SHA efetivo e identifica os ajustes então necessários em 84/85. Não se reinterpreta o histórico como aprovação global do formulário ou do curso.

## Verificação somente leitura

`node auditoria/termodinamica/evidencias/QA-09/ledger-fichas-r30-r1/ledger.mjs --verificar auditoria/termodinamica/evidencias/QA-09/ledger-fichas-r30-r1/ledger.json`

O script fixa a fotografia ativa, snapshots, inventários, os três mapas, cinco entregas/manifestos e pareceres, a base e os pareceres das aplicações. Reexecuta a triagem de cada recorte e destino, compõe identidade dos 100 registros nos mapas, confere o fragmento em cada foto, preservação de links e 191 MathML por cartão, e refaz seleção de contas. A lista de alterações/contextos é verificada exatamente. A verificação de dados, hashes e contas não substitui julgamento físico de cada ficha. Após outra aplicação, o teste exige a fotografia correta: executar em árvore isolada com snapshots ou realizar nova ponte, sem suprimir guardas.

Oito mutações somente em cópias do ledger — hash e posição de ficha, omissão, parecer, contexto, ocorrência de mapa, estado padrão e juízo — foram rejeitadas. Elas testam comparação com o ledger reconstruído, não manipulação integral de mapas ou mérito físico. `negativos.py` SHA `54da906d15f82be0b1355395770b53736032b1bc422b065ef162797e3f51c54d`; saída `negativos.txt` SHA `f5b53c900cc25b32c6b9534949a3ceb31ac649dba4291e2b6642568303a08e88`.

- `ledger.mjs` SHA `a4743af58524997a6da4685b1592851ea843d9fd8aaba383c465b930b5180012`.
- `ledger.json` SHA `08829096cacc3e90842fca2be7c80f89bbdc12311844880e0d828ee81cb5e9d2`.

Meu papel anterior como integrador do ledger de 22 fichas é declarado. Nenhum produto ou evidência antiga foi alterado; não houve navegador, leitor de tela, estudantes, revisão humana ou certificação externa.
