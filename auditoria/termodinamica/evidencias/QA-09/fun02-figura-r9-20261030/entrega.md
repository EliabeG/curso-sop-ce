# QA-09 — FUN-02: figura quantitativa e dados de apoio na fotografia r9

Data: 30/10/2026. Corretor: agente automatizado `/root/next_graphics`. Estado: **aguardando auditoria independente**. Alcance: dados do problema P1 de FUN-02, figura p–V, cálculo dos caminhos I e II, identificação dos ativos e vínculos na fotografia efetiva. Não se presume validação integral de QA-09 nem transferência automática de um parecer antigo.

## Identificação e fronteira

- Aula `modulos/e1-termodinamica.html` SHA-256 `2d6b8fb2f9c99e04d22c19d7b32bbc3eb20577459d9132e506f9c0acef3f2fc2`; inventário r9 SHA-256 `023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d`.
- `assets/termodinamica/fun02-dados-v1.json` v1.0, SHA-256 `511aac986e9122e5498cdf69609274685791000a19f140a09d539fca01676319`; `fun02-calculos-v1.mjs` SHA-256 `2fdd0e498c41db2f7f8e90d5114dcd015f5377e00901e6274f25262e13c79a70`; `fun02-caminhos-v1.svg` SHA-256 `f324acce9060eb15eeab58958649392f4e5b667fbaf2ad9b63e3c68fbe3eae35`.
- Os links fora dos artigos estão em `#fun02-dados`, posições r9 UTF-16 252246 e 252344, e apontam ao JSON e ao script. O SVG é referenciado uma vez, no artigo `fun02-e1-caminhos` (início UTF-16 253755, fim 263251), dentro dos 197 artigos; o inventário QA-09 exclui seus elementos internos. A figura foi examinada aqui por ser ativo relevante, sem contá-la como figura adicional fora dos artigos.
- O parecer anterior [FUN-02-r1](../../../pareceres/FUN-02-r1.md) avaliou os mesmos três hashes de ativos, mas outra versão do HTML. Aqui se confrontam o uso e o contexto r9; isso não reconvalida automaticamente todas as decisões daquele parecer.

## Modelo, balanços e resultados

Dados autorais didáticos, não medições: gás ideal de composição fixa, 1 mol; `R = 8,314 J/(mol·K)` é valor arredondado deliberado do pacote, não o valor exato contemporâneo da constante. `Cᵥ = 1,5 nR = 12,471 J/K`; A: 300 K e 0,010 m³; B: 450 K e 0,020 m³. Fronteira mecanicamente quase estática, sem atrito, sem mudanças cinética/potencial, só trabalho de fronteira; os trechos são idealmente reversíveis, permitindo o retorno. Convenção: Q recebido e W feito pelo sistema positivos; `ΔU=Q−W`. Faixa 250–650 K.

| Estado | Volume | Temperatura | Pressão calculada |
|---|---:|---:|---:|
| A | 10 L | 300 K | 249,420 kPa |
| C | 20 L | 600 K | 249,420 kPa |
| B | 20 L | 450 K | 187,065 kPa |
| D | 20 L | 300 K | 124,710 kPa |

A→C isobárico e C→B isocórico dão `W_I = p_A(V_B−V_A) = 2494,20 J`. A→D isotérmico e D→B isocórico dão `W_II = nRT_A ln(V_B/V_A) = 1728,84769775 J`. Ambos têm `ΔU = n cᵥ (450−300) = 1870,65 J`; portanto `Q_I = 4364,85 J`, `Q_II = 3599,49769775 J`. Percorrendo I e voltando por II invertido, `W_ciclo = Q_ciclo = 765,35230225 J`, `ΔU_ciclo=0`. A temperatura máxima C de 600 K está na faixa; D também. A conversão `1 kPa·L = 1 J` confere dimensionalmente.

A figura imprime 2494,20 J, 1728,85 J e 765,35 J. Para arredondamento ao centésimo, cada resultado está no intervalo de ±0,005 J em torno do valor mostrado. Isso é tolerância de representação, não incerteza de medição. As pressões calculadas concordam com a descrição SVG; estados/legendas A, B, C e D e as duas setas de cada trajetória foram inspecionados na imagem renderizada. A região sombreada está entre a isobárica de ida e a isoterma de retorno; os trechos isocóricos não contribuem para ∫p dV. Não se estimou trabalho medindo pixels.

O SVG possui 161 vértices na isoterma A–D, seguidos de um ponto adicional B no trecho vertical. As coordenadas foram reconvertidas pelo sistema de eixos (8–22 L e 0–280 kPa), comparando cada pressão com `p = 2494,2/V(L)`. Desvio máximo `0,000515944 kPa`, compatível com a quantização de três casas das coordenadas SVG; os quatro marcadores de estados batem com as coordenadas analíticas. A geometria foi vista em [renderização isolada](fun02-renderizacao.png), SHA-256 `793a36268721258d3dfa9a990b7bfa9b758dfcd9c8f0eb36fb954257b65887f6`, produzida por Inkscape a partir do SVG sem editar o ativo. Isso não é teste do site em navegador.

## Reprodução e fontes

`python3 auditoria/termodinamica/evidencias/QA-09/fun02-figura-r9-20261030/verificar.py` lê arquivos sem gravá-los, confere os hashes, os dois links externos aos artigos, o vínculo único do SVG, as coordenadas de estados e os 161 pontos e recalcula os resultados; SHA-256 do script `ccb7c143d6b25e551415607fbaef936a730e9861246763680d0e9d98b3834560`. A execução passou na data indicada. O teste numérico do código publicado `calcularFun02` também foi executado em Node apenas por importação/função; foram 49 verificações internas e as saídas I, II e ciclo coincidiram. O script independente acima não reproduz todos os demais caminhos nem P2/P3, e sua inspeção não é auditoria independente.

Referências primárias consultadas em 30/10/2026: [MIT, First Law §2.1](https://web.mit.edu/16.unified/www/SPRING/thermodynamics/notes/node14.html), convenção de sinais e primeira lei; [OpenStax, University Physics 2 §3.4](https://openstax.org/books/university-physics-volume-2/pages/3-4-thermodynamic-processes), processos quase estáticos e relação isotérmica. São fontes dos modelos, não dos dados didáticos autorais.

Não houve ensaio em navegador, leitor de tela, aluno, revisão humana ou certificação externa. O teste não demonstra a correção de todos os ativos, figuras, referências ou registros do curso. Exige parecer de Auditor distinto na versão identificada; QA-09 continua em correção e o próximo ID permanece bloqueado.
