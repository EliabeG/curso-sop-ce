# QA-09 — auditoria independente de laboratório e oficina, 30/10/2026

Revisor: agente automatizado independente `/root/qa_fichas`. **Veredito: APROVADO no alcance localizado descrito abaixo**, sem ajuste obrigatório identificado nesse recorte. Isto não aprova QA-09 integral nem libera o próximo ID.

## Critério e fotografia

QA-09 requer inventariar e recalcular todo o conteúdo numérico além dos 197 itens revisados, incluindo exemplos, oficinas, diagnósticos, fichas, figuras e explicações. O presente parecer cobre apenas os 12 blocos e dois textos diretos identificados na [entrega](../evidencias/QA-09/laboratorio-oficina-amostra-20261030/entrega.md); não valida o restante nem conteúdo visual de figuras. A regra comum curricular para criação e conclusão de unidades não é satisfeita, nem se pretende encerrá-la, com uma conferência localizada.

Aula efetivamente lida: `modulos/e1-termodinamica.html`, SHA-256 `200f9b773050594d762cc596a5a89297024b245fc4f504081fc77baaed3db95f`; inventário r7 SHA-256 `5090b9897a4698e0ad090f45182afba5880361aabc9fd3c3bdf848d971a85a1a`; entrega do Corretor SHA-256 `abbc125319c32c51bbf58a84f20031b7707e4b25d50dde152f4a2f4755c053f5`; script do Corretor SHA-256 `c403760df81815a395ab8486669170911ce0aca5f721912d9e31b9086ff21c18`. Os deslocamentos referem-se a unidades UTF-16 nesta fotografia e são desambiguados por documento, tipo e contexto.

## Exame da versão efetiva

Li diretamente na aula cada um dos enunciados e os contextos que fixam as hipóteses. Os resultados a seguir foram recalculados com frações exatas em [auditoria-independente.py](../evidencias/QA-09/laboratorio-oficina-amostra-20261030/auditoria-independente.py), SHA-256 `88e989eff8fdca6ca55ffc937c28efdef76aba4cf21f61290f11a2237784f4fc`. O arquivo usa dados transcritos manualmente pelo Auditor: passa a ser evidência aritmética, não extrai todos os dados automaticamente e não substitui a leitura. Executou sem escrita e retornou `ok=true`, 14 fragmentos e 15 verificações aritméticas.

| Identidade r7 | Verificação independente e condições | Resultado |
|---|---|---|
| 420034 | `(230−200)/(300−200)=3/10`; `2800+(3/10)×200=2860 kJ/kg`. Mesma pressão, interpolação local, dados criados para treino. | Correto; tabela não representa propriedades reais medidas. |
| 430457 | `1×(−0,20)+1×0,30=0,10 kJ/(s·K)=0,10 kW/K`. Fronteira conjunta, permanente, adiabática ao ambiente. | Correto e não negativo. |
| 440903 | `4²=1×16`; `4/1=16/4=4`. O contexto anterior fornece gás ideal, mesma eficiência, arrefecimento perfeito e demais restrições para mínimo de trabalho. | Correto no modelo indicado; 4 bar absolutos. |
| 445929 | `−5×(−30)=150 W/m²`; `150×2=300 W` para fluxo uniforme. | Correto; sinal orientado em +x. |
| 446974 | `(40−60)/0,10=−200 K/m`; `−0,5×(−200)×3=300 W`. Perfil linear e as condições fornecidas logo depois do texto. | Correto; +100 W/m² em +x. |
| 449390 | `400×8×25=80.000 W`, `300×8×25=60.000 W`; queda `20.000/80.000=25%`. | Correto com área e diferença média efetiva fixas. |
| 450580 | `1/0,002=500`; `1/0,003=1000/3≈333,3 W/(m²·K)`; razão para o caso limpo `2/3`. | Correto com resistências referidas à mesma área e demais variáveis declaradas constantes. |
| 452097 | `0,30/0,60=1/2`. | Correto apenas para parcela radiativa nas condições dadas; não afirma redução da perda total. |
| 454697 | `10×10×10⁻⁶×80=0,008 m=8 mm`. | Correto na dilatação linear livre e uniforme. |
| 455969 | `V=3×2×1=6 m³`; `A=3×2=6 m²`; `q‴V=1200 W`; `ΔT=1200/(20×6)=10 K`; `Ts=30 °C`. | Correto no balanço estacionário com as outras faces isoladas e sem outras perdas. Não foi auditada a figura. |
| 462747 | `150×0,20=30 kJ`; `(200+100)/2×0,20=30 kJ`. | Correto para pressão externa constante no primeiro caminho e variação linear quase estática no segundo; coincidência não transforma trabalho em propriedade. |
| 467290 | `QL=400 kJ`; `η=0,60 > 1−300/600=0,50`; `Sger=400/300−1000/600=−1/3≈−0,333 kJ/K`. | Correto no modelo de ciclo e dois reservatórios; segunda lei violada. |
| 467663 | `QL=600 kJ`; `η=1/3≈33,3% < 1−300/500=40%`; `Sger=600/300−900/500=0,20 kJ/K`. | Compatível com as duas leis no modelo; não prova desempenho de um equipamento real. |
| 451880 | σ ≈ `5,67×10⁻⁸ W/(m²·K⁴)` corresponde ao arredondamento de [NIST CODATA 2022](https://physics.nist.gov/cgi-bin/cuu/Value?sigma), `5,670374419…×10⁻⁸`. | Valor e unidades corretos para a aproximação apresentada. |

A reprodução do script do Corretor também retornou `ok=true` e 12 blocos. A conferência independente identificou ainda os dois textos diretos por posição e hash do inventário: para esses parágrafos, os hashes são do **texto sem as tags `<p>`**, não do fragmento HTML completo. Eles conferem: posição 446974 `94d234e1021069ffc7729055e41629af8bc52aea7a202114c5e4e012bd8ec115` e 451880 `f703f6e1269936f0e9868d232c2103a4c2e1b7af26a4170f72bcb8a35243d4c0`. Em ambos os casos o parágrafo não contém nós filhos; não se generaliza esta extração a outros textos do inventário.

## Critérios e decisão

| Critério do recorte | Resultado |
|---|---|
| Identidade da fotografia, blocos e textos diretos | Atendido para as 14 ocorrências indicadas. |
| Valores, unidades e hipóteses das contas listadas | Atendido no contexto declarado, com dados nominais e arredondamento acima. |
| Fonte da constante física | Conferida com NIST CODATA 2022; demais exemplos usam dados didáticos da aula. |
| Teste computacional reproduzível | Atendido para aritmética transcrita e identidade; não é extração integral de todos os números. |
| Figuras, demais ocorrências e QA-09 completo | Não examinados; continuam pendentes. |
| Liberação do próximo ID | Não autorizada; depende de aceite integral de QA-09 e decisão do coordenador. |

Sem revisão humana, ensaio de navegador, estudo com alunos ou certificação externa nesta verificação. A aprovação localizada não é prova de nível avançado do curso nem garante validade em versões posteriores.
