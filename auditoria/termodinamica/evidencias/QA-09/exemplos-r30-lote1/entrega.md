# QA-09 — ilustrações numéricas em texto direto, r30, lote 1

30/10/2026. Autor `/root/next_examples`. **Revisão localizada, aguardando auditor independente; produto não alterado.** Examinei oito afirmações numéricas em sete parágrafos/itens de texto direto de quatro bases. Não são oito exercícios adicionais nem integram os 197 artigos. O critério é revisão individual na fotografia efetiva r30: não encontrei parecer que individualize estes oito cálculos nessa fotografia; isso não implica que sejam novos ou nunca tenham sido analisados. Em particular, o levantamento `revisao-r28-reference-2` já recalculou ΔU e potência em r27, e o parecer de pressão dessa revisão examinou seu bloco; há revisão histórica do bloco de exergia em r13 e leitura de conexão em `teoria-entropia-r30-next-theory`. As questões dos bancos e os exemplos EX numerados previamente examinados não são recontados aqui.

## Identidade e método

Aula r30 SHA-256 `c719adae3464fb56ed2b0ad7014e0721c0aab2da444fb484ec0b40c5c0c8fbd4`; inventário QA r30 `1ce69fc1ab71850abc3ab8dc3df82b04e78788b9e62a55919c609a708a7979b4`. `resultado.json` SHA `ed2ab915c0127bfbdcaea2db6771d8452c474b6a0af972a303745af0730021f9` contém âncoras de contexto, offsets UTF-16 e hashes de cada fragmento e contêiner. As duas afirmações do gás rígido e da isoterma compartilham o mesmo parágrafo; a unidade de contagem são alegações, não recortes únicos.

Reproduzir da raiz: `node auditoria/termodinamica/evidencias/QA-09/exemplos-r30-lote1/verificar.mjs`. Script somente leitura, SHA `e362e28f3bb70f85e26929805172185efc2a8f54d78dd9a7425f3aec5204473f`; confere hashes da fotografia, contexto e presença dos textos, além de refazer contas com valores transcritos. Não extrai os números por interpretação semântica e não demonstra os modelos. Os valores são nominais didáticos, não medições nem propriedades extraídas de fontes.

## Contas e hipóteses

| Afirmação | Conferência e domínio |
|---|---|
| Temperatura e intervalo, `base-absolutas` | 10 + 273,15 = **283,15 K** para o valor de 10 °C; diferença de **10 °C** corresponde a **10 K** sem somar a constante. Uma temperatura é diferente de um intervalo. |
| Gás rígido, `base-gas-modelo` | Para gás ideal em recipiente fechado, quantidade/composição e volume fixos, pressões absolutas, 350/280 = **1,25**, aumento de **25%**. Isso compara estados; não prova que todos os gases reais sigam exatamente o modelo. |
| Gás isotérmico, mesma base | Gás ideal com n e T fixos: se V₂ = V₁/3, então p₂/p₁ = V₁/V₂ = **3**. São pressões absolutas; o modelo não exige um valor para o trabalho do processo. |
| Compressibilidade, mesma base | **Z = 120/150 = 0,80**, adimensional, afastado da previsão ideal Z=1 para esse estado. Z pontualmente próximo de 1, sozinho, não garante todas as propriedades ideais. |
| Exergia, `base-exergia` | Disponibilidade de referência de 100 kJ menos 20 kJ destruídos por irreversibilidade resulta em **80 kJ** na comparação formulada. A comparação exige mesma referência e restrições; no balanço geral, transferências de exergia também contam, de modo que a conta não equivale à energia que necessariamente resta em qualquer sistema real. |
| Variação de energia, `base-leitura-matematica` | 55 − 80 = **−25 kJ**; valor final é 55 kJ. Esta operação não identifica, sem balanço adicional, calor ou trabalho. |
| Potência térmica, mesma base | **2 kJ/s × 60 s = 120 kJ** para potência térmica constante ou média equivalente. Potência elétrica nominal não é automaticamente potência térmica útil. |
| Razão e percentual, mesma base | X₂/X₁ = 1,4 com X₁ > 0: final **140%** da referência e aumento **40%**; o denominador deve ser não nulo. |

Não identifiquei erro concreto que exija proposta de alteração neste recorte. A revisão anterior da pressão média e a igualdade algébrica Q=mcᵥΔT não são objeto deste lote e não são novamente adjudicadas aqui. Tampouco se assume que a revalidação do texto direto cubra todo o respectivo contêiner ou todos os números do curso.

## Fontes e limites

[OpenStax, lei dos gases](https://openstax.org/books/chemistry/pages/9-2-relating-pressure-volume-amount-and-temperature-the-ideal-gas-law) foi consultada por pesquisa web em 30/10/2026: sustenta relações de pressão e temperatura em volume e quantidade fixos e de pressão e volume à temperatura constante; a página não fornece os valores deste lote. Para graus Celsius e kelvin, usa-se a referência NIST registrada na revisão histórica `exemplos001-005-diagnosticos26-28-r9-20261030/entrega.md`: [NIST SP 811, capítulo 8](https://www.nist.gov/pml/special-publication-811/nist-guide-si-chapter-8); não foi novamente aberta nesta execução devido a erro de acesso da ferramenta. A prova do caso de exergia depende do balanço e das restrições da própria aula, não é atribuída a uma fonte específica. O script aritmético não avalia figuras, navegador, acessibilidade, aprendizagem ou ciência fora do recorte. Solicita-se conferência independente das hipóteses e do alcance, em especial da comparação de exergia.
