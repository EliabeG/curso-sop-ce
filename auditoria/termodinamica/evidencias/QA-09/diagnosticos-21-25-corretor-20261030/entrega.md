# QA-09 — recálculo dos diagnósticos 21–25, r1

Data: 30/10/2026. Autor: agente automatizado `/root/qa_diagnosticos`, perfil Corretor. **Estado: aguardando revisão independente.** Este lote não aplica alterações à aula nem resolve o critério integral de QA-09. Os números a seguir são dados didáticos dos próprios enunciados, e não propriedades medidas ou extraídas das fontes externas.

## Fotografia e identificação

Arquivo `modulos/e1-termodinamica.html`, SHA-256 `200f9b773050594d762cc596a5a89297024b245fc4f504081fc77baaed3db95f`; inventário `auditoria/termodinamica/evidencias/QA-09/inventario-r7.json`, SHA-256 `5090b9897a4698e0ad090f45182afba5880361aabc9fd3c3bdf848d971a85a1a`. Os cinco objetos são `div.exemplo` da seção `preparacao-questoes`, fora dos 197 artigos excluídos no inventário. Posições são unidades UTF-16, conforme r7; em outra versão é necessário reconciliação, não aceitação automática. O script `verificar.py`, executável da raiz, verifica hash integral e o fragmento bruto de cada ocorrência e refaz as contas nominais. Não substitui leitura científica nem revisão independente.

| Nº | Intervalo UTF-16 r7 | SHA-256 do fragmento |
|---|---|---|
| 21 | 532172–532785 | `08717431d6f258728f63490380fcf96a6de7363191a2c874c2c7b595ef7475f6` |
| 22 | 532785–533297 | `3e5156b9614be86d149d3154889aada0abc3f9f2d7e20c597b09b781e02ea88e` |
| 23 | 533297–534107 | `e5e87b30397cc0394b10b1194461e7bf64fd0e831184d4b91eeae0d234cd5073` |
| 24 | 534107–534813 | `a86feea2983a3c008e11db251a908fce3402af0f7b5cc0d3a33a5aaee3033fbf` |
| 25 | 534813–535662 | `f5284077b97afe5280e5635e09a6434640dfb4f805a0010b09ff33139e5c9be0` |

## 21 — enchimento adiabático

A massa final iguala a massa que entrou: m₂ = m_in; tanque inicialmente vazio, uma entrada a 320 K constante, sem saída, sem calor nem trabalho e com energia das paredes, cinética e potencial desprezadas. O balanço integrado dá U₂ = m_in h_in. Para o mesmo gás ideal de composição fixa, cₚ/cᵥ = 1,25 constante e mesma referência para u e h, resulta T₂ = (cₚ/cᵥ) T_in = 1,25 × 320 = **400 K**, como publicado. A temperatura T₂ caracteriza o estado final representativo em equilíbrio; a massa no tanque aumenta, portanto o processo não é permanente. Adiabático não implica isotérmico. O exemplo está apoiado na aula `#base-balanco-transiente`, que explicita referência comum e as hipóteses da forma reduzida; como elas não estão todas repetidas no enunciado, a adequação da dependência dessa base deve ser julgada pelo Auditor. Resultado exato no modelo com os dados nominais; não há incerteza experimental indicada.

## 22 — calor específico variável

Para o gás ideal de composição fixa e cₚ(T) fornecido na faixa, Δh = ∫₃₀₀⁴⁰⁰ (0,80 + 0,001 T) dT = 0,80(100) + 0,0005(400² − 300²) = 80 + 35 = **115 kJ/kg**. Os coeficientes têm unidades compatíveis com cₚ em kJ/(kg·K) e T em K. Na entrada, cₚ(300)=1,10 kJ/(kg·K); congelá-lo nessa faixa daria 1,10 × 100 = **110 kJ/kg**, diferente do integral. As duas contas publicadas conferem. Para esta lei linear, o valor no ponto médio é 1,15 e reproduz a integral, o que não autoriza usar o ponto médio para qualquer função. Base `#base-calor-variavel`. Igualdades exatas com valores nominais; nenhuma tolerância de medição é fornecida.

## 23 — duas entradas e uma saída

No regime permanente, a conservação de massa fornece ṁ₃ = 2 + 1 = **3 kg/s**. Com referência de entalpia compatível, sem trabalho e sem variação relevante de energia cinética ou potencial, o fluxo de energia das entradas é 2×100 + 1×400 = **600 kW**. Adiabático: h₃=600/3=**200 kJ/kg**. Com 30 kW recebidos: h₃=(600+30)/3=**210 kJ/kg**, correspondendo a 630 kW na saída. Os números e sinais da solução conferem. O enunciado remete à base `#base-misturador-correntes`, que requer entalpias adequadas e na mesma referência; a suficiência dessa remissão para estudo independente fica sujeita à revisão. O balanço fornece entalpia, não temperatura ou fase. Exato para os dados nominais e modelo, sem tolerância experimental fornecida.

## 24 — bocal

Para uma entrada e uma saída, regime permanente, sem calor/trabalho e sem variação de energia potencial, h₁ + V₁²/2 = h₂ + V₂²/2. Com h em kJ/kg e velocidades em m/s, V₂² = 100² + 2×1000×75 = **160.000 m²/s²**, portanto a magnitude **V₂ = 400 m/s**. O exemplo alternativo que despreza a velocidade de entrada fornece √150.000 = 387,2983346… m/s, compatível com **387,30 m/s**, no intervalo [387,295; 387,305) para arredondamento usual a duas casas; isso não representa incerteza experimental. A conservação de energia não exige reversibilidade. Como ressalva de modelo, os valores de entrada, saída e vazão se referem à descrição unidimensional adotada pela base `#base-bocal-difusor`; a equação não resolve por si só todo o escoamento. Ambas as apresentações numéricas conferem sob o modelo.

## 25 — válvula e região de saída

Na base `#base-valvula-fase`, o modelo usual define regime permanente, ausência de calor e trabalho relevantes e energia cinética/potencial desprezível, com h₂≈h₁. A tabela do próprio exercício é didática, para substância pura em equilíbrio na pressão subcrítica; h_f=500 e h_g=2.500 kJ/kg e as entalpias usam a mesma referência. Para h₂=1.000 kJ/kg, x=(1.000−500)/(2.500−500)=**0,25**, adimensional e dentro de [0,1], como publicado. Para h₂=2.700 kJ/kg, a extrapolação algébrica fornece 1,10 mas está fora do domínio da fórmula de mistura saturada: **não é título físico**. Com o modelo e região de equilíbrio habituais, consultar propriedades de vapor superaquecido à pressão de saída; não substituir o quociente por 1. Estes valores de tabela não são atribuídos à fonte externa. A remissão ao “modelo usual” na base, em vez de repetição integral das hipóteses no enunciado, fica sujeita à avaliação independente. Contas exatas para dados nominais, sem especificação de incerteza.

## Fontes e alcance

- Bases internas mencionadas acima: identificadas pelo hash completo do HTML e pelas âncoras; fornecem os modelos, hipóteses e dados pedagógicos empregados aqui.
- [NASA Glenn, conservação de energia e entalpia de escoamento](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/conservation-of-energy/), consultado em 30/10/2026: apoio à relação de entalpia e energia cinética e termos de calor/trabalho; não fonte dos dados dos exercícios nem prova dos resultados específicos.
- [NASA Glenn, calores específicos e relação com entalpia](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/specific-heat-cp-cv/), consultado em 30/10/2026: apoio às propriedades do gás ideal.
- [NIST, propriedades termofísicas](https://webbook.nist.gov/chemistry/fluid/), consultado em 30/10/2026: referência para seleção de tabelas de propriedades e saturação; nenhuma consulta a substância específica ou confirmação dos valores fictícios foi feita.

Não foram alterados HTML, inventários ou registros históricos por este lote. Não houve ensaio em navegador, teste com estudante, revisão humana ou parecer independente ainda. Cabe ao Auditor conferir a versão efetiva, os cálculos, as remissões e se os enunciados necessitam explicitar hipóteses adicionais. **Nenhuma aprovação é reivindicada** e o próximo ID continua bloqueado.
