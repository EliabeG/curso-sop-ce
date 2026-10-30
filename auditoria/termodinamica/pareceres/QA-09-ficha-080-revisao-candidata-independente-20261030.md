# QA-09 — revisão independente da candidata da ficha 80

Data: 30/10/2026. Revisor automatizado independente `/root/qa_examples`. **Veredito localizado: APROVADA para a candidata isolada**, sem aplicação ao formulário nesta rodada. O parecer não aprova FOR-01 ou QA-09 integral nem libera o próximo ID; a versão efetivamente aplicada exigirá nova auditoria.

## Escopo e identidade

O parecer de equipamentos identificou como ajuste obrigatório explicitar denominador positivo e trabalho líquido produzido ao interpretar η como rendimento motor. Examinei a ficha 80 `formula-brayton-liquido` e os arquivos da candidata, confrontando-os com `formulas/termodinamica.html` SHA-256 `c27422b409a0a755448982c4074c6d6967fd3e91d7eae20274e218530f5c37b0` e inventário r8 `ae75a258398c385398567457d98ebd49b9838c0c9a4eedc69ea8d2d72981b687`.

O artigo original ocorre uma vez na seção de ciclos, posições 188405–190773 UTF-16 do r8, e sua extração da fonte coincide com o arquivo isolado sem a quebra final. SHA-256 do fragmento original `be53d6d4b8ef9305ad4392713fd7ce2c59379393187d06bf0234116ffc431ea5`; candidato `9dcaed2872d4754bb8151aae1ada14a4c45a07557e6ed70ec5569b8c4cfc0897`. O candidato ainda não ocorre no formulário efetivo. O delta é apenas duas inserções da frase, uma no texto visível e outra no índice de busca; ao removê-las, a candidata retorna exatamente ao original. Os sinais > aparecem como `&gt;` na marcação.

## Verificação científica e funcional estática

No modelo indicado, apenas turbina e compressor contribuem para o trabalho útil líquido, e Ẇc é a magnitude consumida: Ẇlíq=Ẇt−Ẇc. A razão η=Ẇlíq/Q̇in requer Q̇in≠0; para interpretação de rendimento de motor com calor efetivamente recebido e produção líquida positiva, as condições acrescidas Q̇in>0 e Ẇt>Ẇc são apropriadas. Elas são necessárias nesse modelo, não demonstram sozinhas viabilidade física, conformidade com a segunda lei ou desempenho de uma instalação real.

Com os dados hipotéticos 1.000 kW de turbina, 400 kW de compressor e 1.200 kW de calor recebido, Ẇlíq=600 kW e η=0,50. Com Q̇in=0 a razão é indefinida; com Ẇt=400 e Ẇc=1.000 kW e Q̇in=1.200 kW, ela é −0,50 e não descreve produção líquida de trabalho. Esses contramodelos são de domínio matemático, não estados físicos validados. O denominador deve referir-se ao calor externo total de entrada e à mesma base temporal ou mássica que o numerador. O [MIT, aplicações da primeira lei a motores térmicos](https://ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_5.htm), e [OpenStax, máquinas térmicas](https://openstax.org/books/university-physics-volume-2/pages/4-2-heat-engines), consultados em 30/10/2026, apoiam a definição da razão, não fornecem os valores hipotéticos.

Comparei de modo independente os fragmentos e a substituição em memória: o SHA-256 da fotografia simulada é `cda652563a79c49a6c3d527ad1400c7f7597d33c9b8523ed8a26047b25c69feb`; as duas inserções são idênticas e estão nas posições esperadas. Os 191 elementos MathML são byte a byte idênticos e o número de artigos de ficha permanece 100 nessa comparação estática. O teste do Corretor inspeciona também a ordem e as demais 99 fichas em memória; não é teste de navegador nem comprova aplicação efetiva. A indicação pré-existente de uso por ciclo ou por kg deve ser lida com grandezas de energia consistentes, em vez de misturar taxas com energias; a marca pontuada do MathML representa potência.

## Quadro e consequências

| Critério da candidata | Resultado |
|---|---|
| Identidade, posição, fragmentos e delta | Atendido para a fotografia citada e a troca simulada. |
| Fórmula, sinais, denominador e domínio motor | Atendido no modelo descrito; não se infere viabilidade completa. |
| Preservação da fórmula e demais fichas | Inspeção estática da simulação sem alterações indevidas identificadas. |
| Versão aplicada, comportamento e alcance de FOR-01 | Não examinados; aguardam aplicação e nova auditoria. |
| QA-09 completo e próximo ID | Não atendido; continuam pendentes. |

Entrega examinada `ficha-080-candidata-20261030/ENTREGA.md` SHA-256 `879680daa7b424236c67e661bc903df3b3e84eb4202042ddbfb4203f01417b8e`; manifesto `076bb2b4b885507d65964dc423202d34ae05d7a2a63fce399c395d8ee808d003`; script `6359777bbe5e5365e4dc891f2dec4ebff21bd431e51f6aef4488a57a4e55ab15`. Em futura aplicação, conferir a base real, fotografias/inventário e deslocamentos, revalidar o alcance afetado de FOR-01 e submeter a versão aplicada à auditoria independente. Nenhuma revisão humana, teste com alunos, avaliação de leitor de tela ou certificação externa foi realizada.
