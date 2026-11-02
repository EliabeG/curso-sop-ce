# QA-09 — auditoria independente dos exemplos EX-021 a EX-030, r1

Data: 30/10/2026. Revisor: agente automatizado independente `/root/audit_strategy`. Veredito: **APROVADO apenas para o recálculo e a interpretação dos dez blocos identificados abaixo**, dentro das hipóteses descritas. Não houve alteração do curso nesta rodada. QA-09 integral permanece em correção e o próximo ID não está liberado.

## Critério, versão e alcance

QA-09 exige inventariar e recalcular todo o conteúdo numérico fora dos itens de BAN-08, inclusive exemplos, oficinas, diagnósticos, fichas, projetos, figuras e explicações. Cada ocorrência precisa de referência verificável e resultado conferido. Essa revisão examina dez `div.exemplo` na aula, não a totalidade dos nós da seção, a figura de disponibilidade, os recursos vinculados nem todos os demais cálculos. As regras curriculares de item novo não convertem esta conferência localizada em aceite de uma unidade nova. Foram lidas as bases imediatamente anteriores, os dez blocos efetivos, a entrega do Corretor e os arquivos de inventário, sem tomar os resultados da entrega como prova única.

Fonte `modulos/e1-termodinamica.html`: SHA-256 `200f9b773050594d762cc596a5a89297024b245fc4f504081fc77baaed3db95f`. Inventário r7: `5090b9897a4698e0ad090f45182afba5880361aabc9fd3c3bdf848d971a85a1a`. Mapa histórico dos nomes EX: `892b63067b87316009a89a8553e8288a9bc51c2c66929b33a4fd19d927d2ede9`. Entrega examinada `exemplos-021-030-corretor-r1/relatorio.md`: `75109b9bdc3e27752d6c116a127b285c3ba93e6daaa209b2b445618366081c95`.

Os IDs EX são identificadores de mapa, não IDs do HTML. O script independente [`verificar.py`](../evidencias/QA-09/auditoria-exemplos-021-030-r1/verificar.py), SHA-256 `13364c05ca7f554b71ba69192f2b0e2fa5570b4e0b87d4e42f22ffa3bcdf22a6`, confronta para cada bloco documento, seção, posição UTF-16, título e hash do fragmento com o mapa histórico e a versão r7. Encontrou uma ocorrência para cada EX-021–030 e reconstruiu os hashes. O script lê e escreve somente na saída padrão. A saída de `conferir.py` do Corretor, inspecionado antes de executar, reproduziu byte a byte seu `resultado.json` (`96de70f6f7c7c6af787821314acef7aa6935eaf3d7855ea0697f845b12392cc0`). A igualdade de hash não transfere automaticamente aprovação para os elementos circundantes.

## Recálculos e confronto das hipóteses

| Bloco | Verificação independente e condições aplicáveis | Conclusão |
|---|---|---|
| EX-021 | Misturador permanente, vazões 1 e 3 kg/s, entalpias 100 e 300 kJ/kg, Q̇ = Ẇ = 0 e energias cinética/potencial desprezíveis. Saída 4 kg/s: h₃ = (100 + 900)/4 = 250 kJ/kg; entrada e saída 1.000 kW. A base requer referência compatível de entalpia. | Correto no modelo. |
| EX-022 | Bocal permanente adiabático sem trabalho e altura desprezível. 40 kJ/kg = 40.000 J/kg; v₂ = √(50² + 2 × 40.000) = 287,228132… m/s. | 287,23 m/s arredonda corretamente: intervalo [287,225; 287,235) m/s. |
| EX-023 | Válvula h₂ ≈ h₁ sob as hipóteses da base; na pressão de saída, 400 < 950 < 2.600 kJ/kg. Então x = 550/2.200 = 0,25. A aplicação exige substância pura e equilíbrio líquido–vapor. | 25% de vapor e 75% de líquido corretos no modelo. Os valores são didáticos, não dados validados de fluido real. |
| EX-024 | Dois reservatórios a 800 e 400 K, recebendo 600 kJ: ηC = 0,5, Wmáx = 300 kJ, QL,mín = 300 kJ. Proposta: W = 600 − 120 = 480 kJ, η = 0,8, Sger = 120/400 − 600/800 = −0,45 kJ/K. | A primeira lei fecha, mas a proposta viola a segunda lei. |
| EX-025 | Ambiente de referência uniforme a 290 K e Sger = 0,10 kJ/K: Xdestruída = 290 × 0,10 = 29 kJ. A comparação de trabalho útil perdido requer mesmas condições e referência reversível apropriada. | Correto no escopo da base; destruição de exergia não é destruição de energia. |
| EX-026 | Composição fixa e substância simples compressível: dh = Tds + vdp; para variação isentrópica e v aproximadamente constante, Δh ≈ 0,001 × 800 = 0,80 kJ/kg. | Correto na aproximação; não implica automaticamente o trabalho real de bomba. |
| EX-027 | Ciclo com entrada 1.000 kJ e rejeição 600 kJ: W = 400 kJ/ciclo; η = 400/1.000 = 40%. | Correto; sem temperaturas não se determina o limite de Carnot específico. |
| EX-028 | Para o mesmo ciclo, QL = 600 kJ, W = 200 kJ: COPR = 3; QH = 800 kJ e COPBC = 4. | Correto; não foram dadas temperaturas para verificar o limite de segunda lei. |
| EX-029 | Q̇in = 150 kW e Ẇt = 90 kW mantidos: Ẇlíq = 60 e 45 kW para consumos de 30 e 45 kW; eficiências 40% e 30%. | Correto como comparação hipotética, sem afirmar viabilidade operacional universal. |
| EX-030 | Redução de (400 − 300)/400 = 25%; com 120 kJ/ciclo de trabalho líquido, eficiência de 30% para 40%, isto é, aumento de 10 pontos percentuais. | Correto no modelo hipotético; estados não comprovam projeto físico específico. |

Os resultados são exatos para valores nominais no modelo, exceto o arredondamento explicitado para EX-022; não foi apresentada incerteza instrumental. As condições dos blocos foram confrontadas com as bases imediatamente anteriores: misturador, bocal e válvula na seção energia; Carnot, exergia e relação de Gibbs na segunda lei; ciclos e regeneração na seção ciclos.

## Fontes e limites documentais

As relações foram confrontadas com [Yan, balanços de escoamento estacionário](https://eng.libretexts.org/Bookshelves/Mechanical_Engineering/Introduction_to_Engineering_Thermodynamics_(Yan)/05%3A_The_First_Law_of_Thermodynamics_for_a_Control_Volume/5.06%3A_Key_equations), [OpenStax, conservação, eficiência e COP](https://openstax.org/books/university-physics-volume-2/pages/4-key-equations) e [OpenStax, ciclo de Carnot](https://openstax.org/books/university-physics-volume-2/pages/4-5-the-carnot-cycle). A identidade de Gibbs foi confrontada com o material original do [MIT, Combined First and Second Law Expressions, p. 1B-5](https://live.ocw.mit.edu/courses/16-050-thermal-energy-fall-2002/0d600615983322e758cd9d75fa3b6758_04_part1b.pdf); a relação de exergia com [Tu e Chen, Rethinking Loss of Available Work and Gouy–Stodola Theorem, DOI 10.1115/1.4066860](https://dspace.mit.edu/entities/publication/4c0436a6-92b2-4940-a245-1e9becbb30ba). O último artigo discute limites da interpretação de perda de trabalho para sistemas não necessariamente ligados ao ambiente; o parecer mantém a comparação expressamente condicionada a referência e restrições. Fontes externas consultadas em 30/10/2026, sem captura local ou hash; apoiam as relações, não são origem dos números hipotéticos do curso.

## Quadro de critérios

| Critério | Decisão e limite |
|---|---|
| Identidade de cada bloco e versão efetiva | Atendido para EX-021–030, por documento, seção, título, posição e SHA-256. |
| Contas, unidades, sinais e precisão exibida | Atendido no modelo nominal dos dez exemplos. |
| Hipóteses e referências das relações | Atendido no alcance descrito, considerando as bases; dados hipotéticos não são medições. |
| Conteúdo de figuras, demais explicações e recursos | Fora do alcance desta revisão; permanecem em QA-09. |
| Critério integral de QA-09 | Não atendido nesta revisão parcial. |
| Liberação do próximo ID | Não liberada. |

Nenhuma simulação de estudante, teste em navegador real, revisão humana ou certificação externa foi realizada nesta rodada. Não se infere aprendizagem a partir da revisão de contas.
