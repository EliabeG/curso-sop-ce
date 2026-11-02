# QA-09 — auditoria independente da candidata de pressão média

30/10/2026. Auditor `/root/next_examples`, distinto do Corretor `/root/reference_triage`; fui autor do parecer que identificou a lacuna e declaro esse vínculo. **APROVADA ISOLADAMENTE a candidata sobre a fotografia r27** no alcance descrito. Não houve aplicação nem aprovação global de QA-09.

## Conteúdo e contramodelos

Em face plana de área A>0, a pressão média sobre essa face é F⊥/A quando F⊥ representa a força normal de pressão exercida sobre ela na mesma convenção de pressão; se a distribuição é uniforme, média e valor local coincidem. A candidata informa que, se variar, a pressão local pode diferir da média e qualifica 200 N/0,010 m² como 20 kPa **médios**, sem inferir uniformidade. A restrição a face plana evita confundir a média escalar com força vetorial resultante sobre uma superfície curva. Não se deve substituir F⊥ pela força líquida em lados diferentes de uma parede sem considerar referência e pressão de cada face; essa interpretação faz parte do alcance da revisão, não um cálculo novo do enunciado.

Contramodelo de duas metades de 0,005 m² a 10 e 30 kPa: forças 50 e 150 N, média 200/0,010=20 kPa, porém locais de 10 e 30. Com pressão uniforme de 20 kPa, a mesma força seria obtida e o valor local coincidiria com a média; a força total sozinha não determina qual distribuição ocorre. A [NASA Glenn](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/aerodynamic-force/) descreve contribuições de pressão locais normais e sua integração vetorial. Os valores são sintéticos, não medições da fonte.

A proposta altera exclusivamente a frase sobre pressão dentro de `base-leitura-matematica`; preserva o restante, inclusive comparação manométrica/absoluta e o exemplo algébrico Q=mcᵥΔT, que não foi declarado erro físico universal no parecer de origem.

## Identidade e reprodução

Aula r27 SHA `9af8e2c9ffe509e40594d086a9ef4ad75127fb4ca873efb305d3144e08f3fc49`; inventário `a58d7f0b0a5f097eef83ad83026ef49e801457b87f7cf2b2345c3dd915597c7c`. Candidata `candidata-pressao-media-r28/analise.md` SHA `92f22ca84507bb478933faa66b1536057cb6257d77a378255912832945060158`, manifesto SHA `70a4aa3e86d7604ee1281d493d702db8678b6517d88e8fbc9f61b7acde61e718`, original e candidato sem quebra terminal SHA `d47da4d96ec04dd847dd24240bdf7cc1b7eebbb2ec64e57ccc0ca4ca70a5699d` e `ab0ba4e1a7987da8310584579cb39198001fbe1c77a974d4e75d236408664cf0`. O intervalo r27 é UTF-16 [34919,37843).

Executei o verificador do autor `verificar.mjs` SHA `09419a981109e25c38f52419d1dbe4681d75f7cac832e3793c829ce736928941`: `ok`, HTML hipotético `3486b562ad7e8ec563fbf191775642628617f0436fe831b5e3a91e4f503bf49c`, 197 artigos e 734 MathML. Meu teste somente leitura `verificar.py` nesta pasta, SHA `34d61bd120b22b595344129d44e8c3bef58ba5e55cf28161a1e7d119f6ea7560`, reconstrói a substituição e confere identidade, posição, original/candidato, mesmo HTML hipotético, artigos, MathML e 3195 atributos de ID/links/ARIA em ordem; também reproduz média e contramodelo. A simulação não grava o produto.

Após eventual aplicação, conferir a fotografia efetiva, inventário/mapa e pedir auditor distinto da aplicação. O teste textual não substitui navegador, leitor de tela, alunos, revisão humana ou certificação externa.
