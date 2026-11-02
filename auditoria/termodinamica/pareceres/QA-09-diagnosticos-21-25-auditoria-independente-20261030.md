# QA-09 — auditoria independente localizada dos diagnósticos 21–25

Data: 30/10/2026. Revisor: agente automatizado independente `/root/qa_examples`. **Veredito: APROVADO no alcance localizado dos cinco diagnósticos e desta fotografia**, sem ajustes obrigatórios identificados. QA-09 integral permanece em correção; esta revisão não libera outro ID.

## Critério e identidade

QA-09 exige inventariar e recalcular todo o conteúdo numérico além dos 197 artigos, incluindo diagnósticos, exemplos, fichas, figuras, oficinas e explicações, com referências verificáveis. A presente revisão verifica apenas os blocos de diagnóstico 21 a 25, os modelos de base imediatamente referidos e os dados e cálculos nesses blocos. Não contempla as demais ocorrências numéricas contidas nas bases, nem ciência do restante do curso.

Arquivo efetivo `modulos/e1-termodinamica.html`: SHA-256 `200f9b773050594d762cc596a5a89297024b245fc4f504081fc77baaed3db95f`; inventário r7 `auditoria/termodinamica/evidencias/QA-09/inventario-r7.json`: SHA-256 `5090b9897a4698e0ad090f45182afba5880361aabc9fd3c3bdf848d971a85a1a`; entrega `auditoria/termodinamica/evidencias/QA-09/diagnosticos-21-25-corretor-20261030/entrega.md`: SHA-256 `a7736f109e27db384898b9f44b70a5c6f7c477824bab1167da764aa2d8a49edd`; programa do Corretor `verificar.py`: SHA-256 `46c2c7c893e52e7a671f9775863ad98cd20979b3fd085a5665b81bd7f32597ac`.

Extraí diretamente do HTML os cinco trechos por posição UTF-16 e li os títulos e enunciados, sem me basear somente no resumo da entrega. Todos pertencem à seção `preparacao-questoes` e os hashes dos fragmentos coincidem com r7 e a entrega:

| Diagnóstico | Início–fim UTF-16 | SHA-256 do fragmento |
|---|---|---|
| 21 | 532172–532785 | `08717431d6f258728f63490380fcf96a6de7363191a2c874c2c7b595ef7475f6` |
| 22 | 532785–533297 | `3e5156b9614be86d149d3154889aada0abc3f9f2d7e20c597b09b781e02ea88e` |
| 23 | 533297–534107 | `e5e87b30397cc0394b10b1194461e7bf64fd0e831184d4b91eeae0d234cd5073` |
| 24 | 534107–534813 | `a86feea2983a3c008e11db251a908fce3402af0f7b5cc0d3a33a5aaee3033fbf` |
| 25 | 534813–535662 | `f5284077b97afe5280e5635e09a6434640dfb4f805a0010b09ff33139e5c9be0` |

## Recálculo e hipótese independente

- **21:** tanque inicialmente vazio, sem saída, Q e trabalho, e com energia cinética/potencial e parede desprezíveis. Com gás ideal de mesma composição, entrada a T constante e razão de calores específicos constante, massa final = massa admitida, balanço integrado dá u₂ = hᵢₙ. No modelo e referências consistentes da base `#base-balanco-transiente`, T₂ = (cₚ/cᵥ)Tᵢₙ = 1,25×320 = **400 K**. A massa acumulada muda; o processo não é permanente. A hipótese de entalpia de entrada constante é coerente com o gás ideal alimentado a 320 K constante; a base remete às referências consistentes. Não é conclusão sobre tanque com parede relevante ou outra interação.
- **22:** no gás ideal de composição fixa, integral de cₚ(T) entre 300 e 400 K = 0,8×100 + 0,001(400²−300²)/2 = 80 + 35 = **115 kJ/kg**. Fixar cₚ na entrada dá (0,8+0,001×300)×100 = **110 kJ/kg**; erro de −5 kJ/kg. A base `#base-calor-variavel` expõe a integral e as unidades. Os coeficientes são os adotados no exercício; o uso do ponto médio é exato para esta lei linear, não para qualquer lei.
- **23:** no modelo estacionário, com uma saída, sem trabalho e desprezando Ec/Ep, balanço de massa dá 3 kg/s. Balanço de energia dá (2×100+1×400)/3 = **200 kJ/kg** para Q̇=0 e (600+30)/3 = **210 kJ/kg** para Q̇=+30 kW. A base `#base-misturador-correntes` exige entalpias na mesma referência apropriada às substâncias; a remissão do bloco à base é suficiente no contexto, sem alegar que o enunciado isolado declara essa premissa. O saldo não determina fase nem temperatura.
- **24:** para escoamento unidimensional, permanente, adiabático, sem trabalho e com variação de altura desprezível, V₂ = √(100²+2×1.000×75) = **400 m/s**. Se a entrada fosse desprezada, √150.000 = 387,2983346… m/s, isto é, **387,30 m/s** a duas casas. A primeira lei não exige reversibilidade. Arredondamento inferior a 0,005 m/s; não é incerteza experimental. A conversão é 1 kJ/kg = 1.000 m²/s².
- **25:** o modelo usual da base `#base-valvula-fase` usa h₂≈h₁, uma substância pura em equilíbrio e dados de saturação à pressão subcrítica de saída. Para h₂=1.000, x=(1.000−500)/(2.500−500)=**0,25**. Para h₂=2.700, o quociente seria 1,10, fora de [0,1]: não é título e não deve ser truncado; para o modelo dado, consultar região de vapor superaquecido. As entalpias devem ter referência comum; os dados da tabela são hipotéticos.

Os cinco resultados conferem para os dados nominais e hipóteses indicadas; não há precisão instrumental informada. O diagnóstico 21 e os diagnósticos 23 e 25 dependem de bases vinculadas que explicitam as hipóteses adicionais; elas não são aceitas como universalmente aplicáveis fora desse contexto. O texto do diagnóstico 25 usa o termo “modelo usual”, definido no vínculo explícito. A aceitação aqui é contextual e não torna o enunciado isolado universal.

## Quadro de avaliação

| Critério aplicado ao lote | Resultado |
|---|---|
| Fonte, posição e hash da versão efetiva | Atendido para as cinco ocorrências identificadas; posições não são estáveis em futuras edições. |
| Hipóteses, sinais, unidades e recálculo | Atendido dentro dos modelos e limites descritos acima. |
| Referência e reprodutibilidade | Entrega cita modelos da própria aula e referências externas; comparação e contas independentes foram refeitas aqui; o script de autoria do Corretor é ferramenta complementar e não prova científica isolada. |
| Correção ou comportamento alterado | Não aplicável: nenhum arquivo de aula foi alterado por esta entrega. |
| QA-09 completo e próximo ID | Não atendido nesta revisão parcial: demais classes e ocorrências permanecem pendentes. |

Não houve revisão humana, teste com estudantes nem ensaio em navegador. A aprovação aplica-se apenas aos blocos, às relações usadas e à fotografia identificada; qualquer alteração posterior no texto ou nas dependências exige reavaliar o alcance afetado. Não aprova os 28 diagnósticos em conjunto, todas as classes ou o nível avançado do curso.
