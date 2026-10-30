# QA-09 — candidata para domínio da razão percentual

Data: 30/10/2026. Proponente: agente automatizado `/root/qa_teoria` (Corretor). **Candidata não aplicada; necessita de revisão independente da proposta e, se aplicada, de auditoria da versão efetiva.**

## Problema e condição necessária

Na base identificada no manifesto, a aula afirma que X₂/X₁ = 1,4 implica aumento de 40%, sem especificar o sinal de X₁. A razão existe se X₁ ≠ 0, mas para interpretar o sinal da variação como aumento numérico é preciso X₁ > 0. Com X₁=−10 e X₂=−14, a razão é 1,4, porém ΔX=−4: houve diminuição no valor numérico. Com X₁=0, a razão não está definida.

A proposta introduz “Para X₁ > 0,” antes da interpretação, conservando os números e explicitando “Para X₁ > 0 e X₂ < X₁” antes da expressão de redução subsequente. Neste domínio, X₂=1,4 X₁ > X₁ e (X₂−X₁)/X₁=0,4, 40%. Sob X₁ > 0 e X₂ < X₁, a expressão de redução é positiva; sem essa desigualdade, seu sinal poderia indicar aumento e o texto não a chamaria de redução. São afirmações aritméticas gerais, não dados experimentais.

## Identidade e delta

O original completo (`original.html`) é um elemento `<li>` dentro do texto de fundamentos, fora dos artigos pontuados e das caixas de exemplo. O arquivo de trabalho tem SHA-256 `200f9b773050594d762cc596a5a89297024b245fc4f504081fc77baaed3db95f`. O original ocorre exatamente uma vez e a candidata ainda não ocorre. Inventário r7, posição UTF-16 36056–36216: `modulos/e1-termodinamica.html:36056:texto`, hash do campo de texto direto `722fd0a7f8460a76179598367038dd3f84024e4189f9617cb5bfd54f2aa2d0ed`; o SHA do fragmento HTML inteiro é outro e consta do manifesto. Os arquivos isolados terminam em quebra de linha; os hashes de fragmento no manifesto não incluem essa quebra. No HTML, `&gt;` e `&lt;` codificam os sinais `>` e `<` visíveis.

Revisão independente deve examinar a correção do domínio, contexto e hipótese da fórmula de redução. Se aplicada, exige uma reconstrução por substituição única, nova fotografia do HTML e inventário, reidentificação de posições, exame das dependências e 197 artigos, verificação de links e revisão independente. Uma equivalência de hash ou uma classificação parcial não transfere aceites automaticamente. A candidatura não representa correção aplicada ou encerramento de QA-09.
