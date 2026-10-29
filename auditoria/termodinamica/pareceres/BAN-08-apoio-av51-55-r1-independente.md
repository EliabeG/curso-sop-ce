# BAN-08 — apoio científico independente AV51–AV55

Data 29/10/2026; autora dos cálculos e revisora: agente automatizado `/root/auditor_ban08_novo`. Revisão parcial, sem cegamento, sem aprovação global BAN-08 ou liberação de próximo ID. Produto/controle não alterados. Fonte dos artigos, dados e bases: `modulos/e1-termodinamica.html`, SHA-256 `80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0`; hashes individuais são do trecho bruto UTF-8 `<article>...</article>`. Itens autorais pontuáveis, cinco opções; links CR são origem comparativa, não fonte dos dados inventados. Valores dados são nominais; operações exatas não estabelecem precisão experimental.

Fontes de modelo acessadas em 29/10/2026: MIT OCW Unified, cap. 5, https://ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_5.htm (Brayton ideal); MIT 16.050, https://ocw.mit.edu/courses/16-050-thermal-energy-fall-2002/75666f9248981634a704fdf257ef529a_07_part2a.pdf (efeito de irreversibilidades); DOE, https://www.energy.gov/cmei/fuels/gaseous-hydrogen-compression (tipos de compressor); bases locais identificadas nos itens.

## AV51 — D

Hash `f1b1e42824eccf9cdf5c8b7eaec9559bef617e430741ccd7b29b376b20d02445`; base `#base-brayton`. Brayton ideal simples: compressão e expansão isentrópicas, duas adição/rejeição isobáricas; não exige duas etapas isotérmicas. I/II verdadeiras, III falsa, sequência V–V–F é única D; demais sequências divergem. Duas e duas são contagens exatas, sem resultado medido ou tolerância numérica pertinente.

## AV52 — D condicionado; suficiência a adjudicar

Hash `857e03ade94e02060d1f4db104c7e7f11de8396182589d3d1bc64be59351c7a8`; bases `#base-leitura-matematica`, `#base-brayton-real`. Para 200 kW de calor total, potência líquida somente turbina menos compressor, 100−40=60 kW antes e 100−50=50 kW depois; η=60/200=30% e 50/200=25%, como D e comentário; diferenças nominais 0. A inverte mudança, B mostra fração consumida 40/200=20% e 50/200=25%, C soma potências (140/200=70%, 150/200=75%), E usa 100/200=50% nos dois casos. Todas as operações são exatas nos dados; sem margem física inventada.

**Ressalva de suficiência:** a base apresenta Ẇlíq=Ẇt−Ẇc “desprezando outros consumos”, mas o comando identifica duas potências e não exclui expressamente outras. Por exemplo, um consumo auxiliar de 10 kW antes e depois mantém todos os valores enunciados e resulta em (100−40−10)/200=25% e (100−50−10)/200=20%; nenhuma opção é esse par. Assim D é calculável no modelo didático convencional, mas a suficiência antes da resposta requer adjudicação consistente com o precedente CR45 e o parecer pontual AV42/45. Se entendido exigível, fixar potência líquida como turbina menos compressor sem outros consumos e 200 kW como calor total, antes da escolha; sincronizar explicação e identidade. Não atribuo o contramodelo ao autor e não declaro ajuste global por este apoio.

## AV53 — C

Hash `3c859fe13b792cf611e2971086fa04d5d89e137e1e4dbeef904897984d37378b`; bases `#base-leitura-matematica`, `#base-brayton-real`. Redução de calor externo=300−240=60 kJ/ciclo; percentual sobre entrada inicial 60/300=0,20=20%, diferença 0 ante comentário. A=90/240=37,5% eficiência final no modelo de calor externo total, B=90/300=30% anterior, D=60/240=25% usa base final, E=240/300=80% é fração remanescente. Todos distintos e cálculos exatos nos dados; não se presume aumento de trabalho ou validação de temperaturas.

## AV54 — D

Hash `9aca957e90b81abf02e4e582b4ac3d63b73fb540f3b1267dce8b24430ca28897`; base `#base-tipos-compressores`. Axial e centrífugo são dinâmicos, pistão alternativo e parafuso de deslocamento positivo: 1–1–2–2, D. Cada alternativa restante troca pelo menos uma classe; a sequência é exata, rótulos não representam grandezas medidas; resultado e tolerância numéricos não aplicáveis.

## AV55 — B

Hash `0aab46ed4a0d48a252b7fcd59ebe6d60f5e7c40c5da0b0e9a743053145249817`; base `#base-brayton`. Compressão e expansão isentrópicas, aquecimento e resfriamento isobáricos, Wlíq=Wt−Wc no conjunto de equipamentos idealizado. A/C/D/E verdadeiras, B é incorreta porque rejeição no ciclo convencional é isobárica, não isocórica. Nenhum valor de calor, temperatura ou trabalho; tolerância numérica não aplicável ao julgamento lógico.

Sem divergência aritmética localizada; a suficiência de AV52 está destacada, não resolvida por esta peça. Não houve piloto com estudantes ou certificação externa.
