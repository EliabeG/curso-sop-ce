# QA-09 — recálculo dos exemplos EX-021 a EX-030, r1

Data: 30/10/2026. Autor: agente automatizado `/root/qa_examples`. Estado: **aguardando auditoria independente**. Os dados são do próprio curso, não de medições nem de uma prova oficial. Não houve alteração do produto e não se declara QA-09 concluído. Escopo: dez blocos `div.exemplo` fora dos 197 artigos; não se transfere o resultado aos nós ancestrais, outras explicações, imagens, ou demais ocorrências do inventário.

## Identidade e reprodução

Fonte `modulos/e1-termodinamica.html`, SHA-256 `200f9b773050594d762cc596a5a89297024b245fc4f504081fc77baaed3db95f`; inventário r7 SHA-256 `5090b9897a4698e0ad090f45182afba5880361aabc9fd3c3bdf848d971a85a1a`. Os IDs EX vêm do mapa independente histórico, não são IDs do HTML; para cada bloco, o programa localiza uma ocorrência única na mesma seção e documento, confronta título e hash original por mapa, extrai o fragmento pelos limites UTF-16 do r7 e recomputa seu SHA-256. O detalhamento de posição, hash e resultados consta em `resultado.json`.

Reproduzir da raiz: `python3 auditoria/termodinamica/evidencias/QA-09/exemplos-021-030-corretor-r1/conferir.py`. O programa apenas lê e emite JSON; não regrava evidências. SHA-256 do programa: `530e23bac6b50e9b09c4edecf326e7a36b2cb2cb6948b6ac29e8b95265cfd35f`. O programa verifica identidade e aritmética; os modelos e hipóteses abaixo foram examinados no texto da aula e não são estabelecidos pelo programa. A avaliação é exata para os valores nominais dados, ressalvado o arredondamento explicitado; não há incerteza experimental informada.

## Resultados, modelos e limites

| ID | Conferência e hipóteses | Resultado |
|---|---|---|
| EX-021 | Misturador em regime permanente, saída única, calor e trabalho nulos, mudanças cinética e potencial desprezíveis; entalpias com referência comum, de acordo com a base anterior. Balanço de massa: 1 + 3 = 4 kg/s. Entrada de entalpia: 1×100 + 3×300 = 1.000 kJ/s = 1.000 kW. Saída: 4×250 = 1.000 kW. | h₃ = 250 kJ/kg, conforme. Isso não determina a fase da saída. |
| EX-022 | Bocal em regime permanente, adiabático, sem trabalho, altura desprezível, conforme a base. 40 kJ/kg = 40.000 J/kg; v₂² = 50² + 2×40.000 = 82.500 m²/s². | v₂ = 287,228132… m/s, coerente com 287,23 m/s; erro de arredondamento < 0,005 m/s. A raiz é a magnitude da velocidade. |
| EX-023 | Válvula em regime permanente com calor, trabalho e variações cinética/potencial desprezíveis: h₂ ≈ h₁. Para substância pura em equilíbrio bifásico na pressão de saída e entalpias com mesma referência: 400 < 950 < 2.600 kJ/kg; x₂ = (950 − 400)/(2.600 − 400). | x₂ = 0,25; frações mássicas de vapor 25% e líquido 75%. Valores da tabela são didáticos, sem comprovação de um fluido real. |
| EX-024 | Máquina cíclica operando apenas entre dois reservatórios ideais a 800 K e 400 K; QH = 600 kJ. ηC = 1 − 400/800 = 0,5; Wmáx = 300 kJ; QL,mín = 300 kJ. A proposta QL = 120 implica W = 480 kJ e η = 0,8. | A proposta satisfaz a primeira lei, mas excede o limite de Carnot; para o ciclo e as duas fontes, Sger = 120/400 − 600/800 = −0,45 kJ/K, impossível. |
| EX-025 | Gouy–Stodola com ambiente uniforme T₀ constante e comparação reversível adequada para as mesmas condições: Xdestruída = T₀Sger = 290×0,10. | 29 kJ; geração de entropia não é necessariamente a variação de entropia do sistema. Energia não é destruída. |
| EX-026 | Identidade dh = Tds + vdp para substância simples compressível, composição fixa e estados de equilíbrio; comparação isentrópica e v aproximadamente constante: Δh ≈ 0,001 m³/kg × 800 kPa. | +0,80 kJ/kg, coerente na aproximação. Não descreve por si só o trabalho de uma bomba real; 1 kPa·m³ = 1 kJ. |
| EX-027 | Ciclo térmico entre uma entrada de calor de 1.000 kJ e uma rejeição de 600 kJ; ΔE ciclo = 0 e Q/W são magnitudes positivas. | Wlíq = 400 kJ/ciclo; η = 400/1.000 = 0,40 = 40%, conforme. Temperaturas não foram dadas; não se testa limite de Carnot. |
| EX-028 | Mesmo ciclo reverso, com QL = 600 kJ e Wentrada = 200 kJ; sem outras interações líquidas, QH = QL + W. | COPR = 3; QH = 800 kJ e COPBC = 4, adimensionais. A identidade COPBC = COPR + 1 vale para o mesmo ciclo sob esse balanço. Não há temperaturas para verificar viabilidade pela segunda lei. |
| EX-029 | Modelo da base Brayton: potência líquida = turbina − compressor, desprezando outros consumos; entrada de calor de 150 kW, mantida junto com os 90 kW da turbina na comparação hipotética. | Inicial: 90 − 30 = 60 kW e η = 40%. Alternativo: 90 − 45 = 45 kW e η = 30%. A hipótese de manter valores não é afirmação de viabilidade para toda operação real. |
| EX-030 | Mesmo trabalho líquido de 120 kJ/ciclo nas duas condições, calor externo reduzido de 400 a 300 kJ/ciclo; em ambas, esse é o calor de entrada usado no denominador da eficiência. | Redução relativa = 100/400 = 25%; η passa de 30% para 40%, aumento de 10 pontos percentuais. Não foram fornecidos estados ou temperaturas para provar que um regenerador específico alcance tais valores. |

Sem divergência aritmética identificada nesses dez blocos dentro das hipóteses de suas bases; não se propõe alterar o HTML nesta entrega. A verificação de fontes de dados não autentica propriedades reais para os números hipotéticos. Confirmar os modelos, os termos e a identidade na auditoria independente; referências e figuras conectadas, demais ocorrências e recalculo global permanecem por fazer.

## Fontes de relações físicas

- [Yan, Introduction to Engineering Thermodynamics, equações de dispositivos de escoamento estacionário, capítulo 5.6](https://eng.libretexts.org/Bookshelves/Mechanical_Engineering/Introduction_to_Engineering_Thermodynamics_(Yan)/05%3A_The_First_Law_of_Thermodynamics_for_a_Control_Volume/5.06%3A_Key_equations) — balanço e modelos de dispositivos usados em EX-021–023.
- [OpenStax, University Physics Volume 2, equações da segunda lei](https://openstax.org/books/university-physics-volume-2/pages/4-key-equations) — máquina térmica, Carnot e refrigerador em EX-024 e EX-027–030.
- [OpenStax, ciclo de Carnot](https://openstax.org/books/university-physics-volume-2/pages/4-5-the-carnot-cycle) — validade do limite entre dois reservatórios.
- A base do próprio E1 fornece explicitamente as relações de Gouy–Stodola e Gibbs e as condições para EX-025/026; nesta rodada, sua interpretação e aritmética são examinadas, mas a conferência documental externa específica dessas duas relações permanece pendente para o Auditor.

Páginas externas consultadas em 30/10/2026, sem captura local ou hash de versão. O conteúdo reproduzível do cálculo está no programa, e sua correção científica e o alcance da aprovação dependem de revisão independente.
