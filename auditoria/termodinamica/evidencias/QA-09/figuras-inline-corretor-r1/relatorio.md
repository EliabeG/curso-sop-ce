# QA-09 — quatro figuras externas aos artigos, revisão do Corretor

Data: 30/10/2026. Autor: agente automatizado coordenador. Estado: **aguardando revisão independente**. Base `modulos/e1-termodinamica.html` SHA-256 `200f9b773050594d762cc596a5a89297024b245fc4f504081fc77baaed3db95f`; inventário r7 SHA-256 `5090b9897a4698e0ad090f45182afba5880361aabc9fd3c3bdf848d971a85a1a`. Os deslocamentos abaixo são UTF-16; cada `figure` contém um `svg`, portanto não são oito figuras diferentes. Os valores são dados didáticos das próprias figuras, não medições de equipamentos. Os cálculos são exatos para os valores nominais; não há precisão instrumental informada.

Foram inspecionados os SVGs, os rótulos, as setas, os títulos/descrições e o texto didático adjacente. Para inspeção visual, os quatro SVGs extraídos foram renderizados isoladamente com Inkscape, fundo branco e cores equivalentes introduzidas em uma cópia temporária (variáveis CSS substituídas); a montagem [figuras-renderizadas.png](figuras-renderizadas.png) tem SHA-256 `3d81c217303c950277b97857c174c24cff6357b69e4c6b589818ca7ab0907aca`. Isso não é teste do site em navegador nem auditoria completa de acessibilidade. A cópia não altera os SVGs do curso.

## Figura 1 — ciclo p–V, seção energia

`figure` em 170720, SHA-256 `382679b6d7c5a390a660ba6d004bd90e31a7b40c5199a0134f6f4c94df68d677`; `svg` em 170743, SHA-256 `a8211a295b3e3b075b4500a3bd85c9fc0c1fbe02e3a129f7f291856abcbfd314`. A (1 m³, 200 kPa), B (3 m³, 200 kPa), C (3 m³, 100 kPa), D (1 m³, 100 kPa); setas A→B→C→D→A, sentido horário, coerentes com o título e legenda. A área termodinâmica é `(200−100) kPa × (3−1) m³ = 200 kJ` de trabalho de fronteira líquido, usando 1 kPa·m³ = 1 kJ; os trechos verticais têm trabalho de fronteira zero. Para um ciclo fechado com ΔEc e ΔEp nulos e sem outros trabalhos, ΔU=0 e Q líquido = W líquido = +200 kJ. O desenho é declarado sem escala: não foi usado para medir a área geométrica. O texto afirma apenas a igualdade líquida, não que cada transferência seja zero.

## Figura 2 — dois caminhos entre estados A e B

`figure` em 197418, SHA-256 `eac47b40277fcad7474a4e766a905babeea45796f91031303cb36e32ed557703`; `svg` em 197441, SHA-256 `58457dad7dc1533e29ad859cf5e0d47cbb44729fe336947d3756ebfdfad2a3a1`. O caminho A→C→B expande de 1 a 3 m³ a 300 kPa e o vertical é isocórico: `W=300×2=600 kJ`. O caminho A→D→B desce isocoricamente e expande a 100 kPa: `W=100×2=200 kJ`. Os vértices, sentidos e valores batem com a descrição e com o exemplo adjacente. Para a mesma quantidade de gás ideal, `p_A V_A = p_B V_B = 300 kPa·m³`, logo as temperaturas extremas são iguais e `ΔU=0`; se apenas trabalho de fronteira e ΔEc/ΔEp desprezíveis, `Q=W` em cada caminho. As linhas verticais não são adiabáticas necessariamente; indicam volume constante.

## Figura 3 — mistura de parcelas do mesmo líquido

`figure` em 208328, SHA-256 `e9e3a1ac563e8c82462083d29ed4dbd7df725ef9ccc725c9f5d733af022ac282`; `svg` em 208351, SHA-256 `204d3cd9183e0db2843be6e51ee2bb2b954a4e488e24024ccc1f504bb54b2966`. Com 1 kg a 20 °C e 3 kg a 60 °C, mesmo líquido com calor específico constante, conjunto isolado, sem mudança de fase ou trabalho relevante e recipiente de capacidade desprezível, `T_f=(1×20+3×60)/(1+3)=50 °C`. A massa final é 4 kg e o calor perdido pela parte quente é `3c(60−50)=30c`, igual ao recebido pela fria `1c(50−20)=30c`, em unidades consistentes. Dados, título, descrição, desenho e explicação adjacente concordam; a figura não representa escoamento contínuo.

## Figura 4 — compressor alternativo com folga

`figure` em 401445, SHA-256 `ad673ba3750acb066643ddaeff915bf69e0cb23972b909f732b0dc51161290c7`; `svg` em 401468, SHA-256 `c6a119d5b2049302f76bd26426306a6c082afb8df8d1c353ed06313d18e0ca82`. O desenho esquemático mostra 1→2 compressão com redução de volume e aumento de pressão; 2→3 descarga aproximadamente isobárica; 3→4 reexpansão do gás residual; 4→1 admissão aproximadamente isobárica. O volume mínimo é positivo. Sentidos de setas, texto, legenda e sequência qualitativa concordam para o modelo idealizado com folga. Não há valores físicos numéricos para recalcular nessa figura; 1–4 são rótulos de estados, não medidas. As pressões de sucção e descarga dependem das hipóteses e das perdas descritas no texto.

## Limites e continuidade

Esta entrega não examina o SVG externo FUN-02, todos os recursos de figuras nos 197 artigos, comportamento dinâmico, fontes externas nem os demais registros de QA-09. A prova de identidade visual e os cálculos acima devem ser confrontados por Auditor independente na base efetiva; até então, não foram aceitos. Nenhum registro geral do inventário foi alterado e não há liberação do próximo ID.
