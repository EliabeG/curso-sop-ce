# QA-09 — revisão independente de valores em 12 fichas, lote 1

Data: 30/10/2026. Revisor: agente automatizado independente `/root/qa_oficina`. **Veredito: APROVADO para as ocorrências numéricas explicitamente delimitadas abaixo**, sem alteração do formulário. Isto não é aprovação das fichas completas nem de QA-09 e não libera o próximo ID.

## Critério, versão e alcance

QA-09 exige inventariar e recalcular todo o conteúdo numérico além dos itens de BAN-08, inclusive valores de fichas e cálculos em figuras e explicações. Esta é uma amostra localizada, que não satisfaz o critério integral. Examinei diretamente as 12 fichas indicadas em `formulas/termodinamica.html`, fotografia SHA-256 `c27422b409a0a755448982c4074c6d6967fd3e91d7eae20274e218530f5c37b0`, confrontando enunciado, unidades, hipóteses e a estrutura dos elementos MathML com os itens numericamente identificados no relatório do Corretor. A revisão não cobre de forma exaustiva cada fórmula, subíndice ou ocorrência das fichas nem as demais fichas, figuras, exemplos ou exercícios.

## Identidade, reprodução e leitura independente

Usei leitura própria dos artigos pelo atributo `id`, seus deslocamentos e tamanhos em bytes no resultado, além de SHA-256 independente dos fragmentos. Todos os 12 são únicos no documento e os seus hashes concordam com `resultado.json`; o conteúdo do fragmento naquela posição tem o ID registrado. Os offsets e hashes só identificam esta fotografia; alteração futura exige reconciliação pelo contexto e arquivo, sem transferência automática de aprovação.

Inspecionei a estrutura MathML — não só o texto linearizado — para expoentes das conversões, frações e índices nas fichas 10/19/30/42/57, radiciação na 57 e potências 4 e −8 na 96. A extração textual não substitui inspeção visual nem teste com tecnologia assistiva. Inspecionei o `verificar.py`: lê os arquivos, imprime saída e não grava histórico. Reexecutei redirecionando a saída para um caminho temporário; o JSON obtido corresponde semanticamente ao `resultado.json` registrado. O script não acessa fontes externas; os números abaixo foram conferidos de forma independente.

## Recálculo e limites

| Fichas | Resultado da conferência |
|---|---|
| 03, 04 | k=10³; 1 kW=1 kJ/s; 1 kPa·m³=1 kJ; 1 L=10⁻³ m³; 1 mm=10⁻³ m; 1 cm³=10⁻⁶ m³; 1 kPa=10³ Pa. Caloria **termoquímica** 4,184 J, e kcal = 4,184 kJ. Kelvin = Celsius + 273,15; diferença de 1 °C corresponde a 1 K. |
| 10, 11, 25 | O aumento `(X₂/X₁−1)100` e a redução oposta requerem X₁ positivo conforme indicado; ppm volumétrico transforma-se em fração por 10⁻⁶; 50%=0,50. A base de ppm não deve ser trocada automaticamente. |
| 12 | A constante NIST `8,314462618… J/(mol·K)` é arredondada a 8,314; dividindo por `101325×0,001=101,325 J/(atm·L)`, resulta `0,082057366… atm·L/(mol·K)`, arredondada a 0,082. Um mol contém exatamente `6,02214076×10²³` entidades especificadas. |
| 19, 30 | Teoria cinética clássica ideal fornece `3kBT/2` para energia cinética **translacional média por molécula**, não para toda a energia interna molecular. A variação cinética translacional de massa fixa é `(m/2)(v₂²−v₁²)` em J. |
| 42, 57 | `(v₂²−v₁²)/2` em J/kg divide-se por 1000 para kJ/kg, produzindo denominador 2000. Termo potencial divide-se por 1000. No bocal/difusor adiabático sem trabalho e sem variação potencial, o rearranjo dá `v₂=sqrt[v₁²+2000(h₁−h₂)]`, com entalpias em kJ/kg e radicando não negativo. |
| 60 | No mesmo ciclo, para `Win>0` e as trocas especificadas, `QH=QL+Win` implica `COPBC=COPR+1`. |
| 96 | CODATA 2022 `5,670374419…×10⁻⁸ W/(m²·K⁴)` arredonda a `5,67×10⁻⁸`; o modelo impõe superfície cinza pequena, entorno aproximadamente negro/isotérmico, visão completa e meio não participante. |

A conferência das constantes e unidades foi feita em [NIST SP 811](https://www.nist.gov/pml/special-publication-811/nist-guide-si-appendix-b-conversion-factors/nist-guide-si-appendix-b9), [NIST mol](https://www.nist.gov/pml/owm/si-units-amount-substance), [NIST CODATA 2022](https://physics.nist.gov/cuu/pdf/wallet_2022.pdf), e a energia cinética translacional em [OpenStax, seção 2.2](https://openstax.org/books/university-physics-volume-2/pages/2-2-pressure-temperature-and-rms-speed). As aproximações de R e σ são conferidas por arredondamento decimal à casa apresentada, sem inferir incerteza experimental.

| Critério da amostra | Resultado |
|---|---|
| Fonte, versão e identidade das 12 fichas | Atendido para esta fotografia, com hashes, posições e IDs únicos. |
| Números e unidades delimitados | Atendido nas condições especificadas; cálculos e valores conferem. |
| Hipóteses das relações examinadas | Atendido no alcance descrito; modelos e limites registrados. |
| Reprodução | Atendido para o script e resultado registrados; não substitui inspeção independente nem simula navegador. |
| Todas as demais ocorrências e QA-09 integral | Não atendido neste lote; trabalho remanescente e próximo ID continuam bloqueados. |

Não houve revisão humana, medição de aprendizagem, piloto, teste em navegador ou certificação. Sem ajustes obrigatórios identificados **no escopo acima**; o coordenador deve manter QA-09 em correção.

## Hashes SHA-256

- Entrega: `b2b7fc06d3e5bfb9598a0cd85da275022cfff74d7181eb0bfdbe107d27631aa4`.
- Script: `4d6fdc7e15ed1db2cbcdd899fc2f1944ad874697e22d66a5e18c9a181f8ca1f7`.
- Resultado: `891b39f95223df1e8258a4e13dd9066c743b86e19f058171803a88aabb9108b3`.
- Formulário: `c27422b409a0a755448982c4074c6d6967fd3e91d7eae20274e218530f5c37b0`.
