# QA-09 — auditoria independente dos exemplos EX-031 a EX-040, r1

Data: 30/10/2026. Revisor: agente automatizado independente `/root/qa_fichas`. **Veredito do lote: AJUSTES_OBRIGATÓRIOS**, devido ao enunciado EX-031. Os demais cálculos, EX-032 a EX-040, conferem no alcance das hipóteses abaixo. QA-09 permanece em correção e outro ID não está liberado.

## Critério e fotografia

QA-09 exige inventariar e recalcular o conteúdo numérico fora dos 197 artigos, inclusive exemplos, explicações, oficinas e figuras, com referência verificável e resultados conferidos. O presente parecer examina apenas 10 exemplos descritos em [relatório do Corretor](../evidencias/QA-09/exemplos-031-040-corretor-r1/relatorio.md); não encerra QA-09. A regra curricular comum refere-se à conclusão de unidades curriculares, o que esta verificação parcial não pretende fazer.

A aula examinada é `modulos/e1-termodinamica.html`, SHA-256 `200f9b773050594d762cc596a5a89297024b245fc4f504081fc77baaed3db95f`; inventário r7 `5090b9897a4698e0ad090f45182afba5880361aabc9fd3c3bdf848d971a85a1a`; relatório do Corretor `7bc18d61bcfb7e8da7e71d7fb52a61ff6a4bb05fb093be8623b88667b81e7984`; seu resultado `54abde8ec4ca1e5c7268c0b40208fdf14566333f04f61eb30f183b96b9ab0a0d`. As dez identidades e hashes dos blocos foram confrontados com o HTML e o inventário usando documento, seção, posição UTF-16, tipo e conteúdo. O auditor leu diretamente os trechos e seu contexto. As posições referem-se exclusivamente à fotografia citada.

## Bloqueio: EX-031

O enunciado fixa regime permanente, despreza variações cinética e potencial e torna a bomba e as turbinas adiabáticas. **Não exclui qualquer trabalho não associado ao escoamento na caldeira, no reaquecedor e no condensador**, nem o contexto imediato impõe essa exclusão. Logo, a passagem de diferença de entalpia a calor transferido e a identificação do trabalho líquido apenas com turbinas e bomba não estão determinadas por todos os dados. `p v` já está incluído em `h`; a lacuna diz respeito a outras formas de trabalho. O balanço geral consultado é apresentado por [Yan, conservação em volume de controle](https://eng.libretexts.org/Bookshelves/Mechanical_Engineering/Introduction_to_Engineering_Thermodynamics_%28Yan%29/05%3A_The_First_Law_of_Thermodynamics_for_a_Control_Volume/5.03%3A_Mass_and_energy_conservation_equations_in_a_control_volume), consultado em 30/10/2026.

Contramodelo de balanço, mantendo as mesmas entalpias e os demais dados: admita uma resistência dentro da fronteira da caldeira recebendo **100 kJ/kg de trabalho elétrico**, sem trabalho extra no reaquecedor e condensador. Com trabalho saindo positivo, `q − w = Δh`; logo `qcaldeira = 2890 − 100 = 2790 kJ/kg`. O reaquecedor recebe 700, de modo que o calor externo total é 3490 kJ/kg. A produção líquida, agora descontando também a entrada elétrica, é `1600 − 10 − 100 = 1490 kJ/kg`; a rejeição continua 2000, e `3490 − 2000 = 1490`. A razão seria `1490/3490 ≈ 42,69%`, diferente de 44,29%. Isto demonstra insuficiência nos balanços fornecidos, não a viabilidade completa de um ciclo físico com os estados didáticos; como já adverte a aula, entalpias isoladas não certificam pressões, fases ou segunda lei.

**Ajuste obrigatório:** declarar no exemplo que caldeira, reaquecedor e condensador não recebem nem fornecem qualquer trabalho não associado ao escoamento, inclusive elétrico; manter a hipótese sobre bomba e turbinas e a convenção local. O Corretor deve reavaliar a frase de trabalho líquido e energia à luz de fronteira e hipóteses, reapresentar a versão efetiva, seus hashes, o mapa de correspondência do inventário por contexto/posição/hash, preservação dos 197 artigos e alcance de aceites afetados. Depois, solicitar nova auditoria independente. Não substituir automaticamente o aceite nem fechar QA-09.

## Outros exemplos

| ID | Recálculo independente e alcance | Resultado |
|---|---|---|
| EX-032 | `y=290/2490=29/249≈0,11646586`; portanto `11,65%` e restante `88,35%` ao arredondar. `y×2700+(1−y)×210=500` com y exato. | Correto. Com `y=0,1165` arredondado, a conferência dá `500,085 kJ/kg`; a igualdade simbólica do texto é exata para y não arredondado. Esclarecer arredondamento pode ajudar, sem caracterizar erro no uso simbólico. |
| EX-033 | `3,5/5=0,70=70%`, volumes por ciclo referidos à sucção. | Correto. |
| EX-034 | `20 kJ/s ÷ 1000 kJ/kg=0,020 kg/s`. | Correto para efeito útil dado, não dados de propriedade da amônia. |
| EX-035 | `16×250=4000 mL/min=0,24 m³/h`; `400 ppm=0,0004`; `0,24/0,0004=600 m³/h`. | Correto no modelo estacionário e mesmas condições de referência; valores hipotéticos, não critério normativo. |
| EX-036 | `0,20/500=0,0004=400 ppm`; `450+400=850 ppm`. | Correto sob hipóteses do balanço em regime estacionário. |
| EX-037 | `54/3600=0,015 m³/s`; `1000×10×0,015×20=3000 W`; `3000/5000=60%`. | Correto para rendimento de eixo e altura manométrica dada. |
| EX-038 | `(230−200)/(300−200)=0,3`; `2800+0,3×200=2860 kJ/kg`. | Correto na interpolação linear local com dados de treino. |
| EX-039 | `1×(−0,20)+1×0,30=0,10 kW/K`. | Correto para conjunto estacionário adiabático ao exterior; não verifica estados e balanço de energia. |
| EX-040 | `√(1×16)=4 bar`; as duas razões são 4. Para o contexto, a soma dos dois termos de trabalho positivos com produto fixo é mínima quando iguais, pela desigualdade aritmético-geométrica. | Correto sob hipóteses do contexto: gás ideal, calores específicos constantes, mesma eficiência, resfriamento perfeito e ausência de perdas indicadas. |

A conferência automatizada independente, [auditoria-independente.py](../evidencias/QA-09/exemplos-031-040-corretor-r1/auditoria-independente.py), SHA-256 `2f8293bd34bff2361b8ea94c40f63a5bb9f6b1facab66a97072293b4be4351cb`, retornou `ok=true`, dez blocos e 11 checagens com frações exatas, inclusive o contramodelo. O `ok` significa que a aritmética e hashes transcritos conferiram, não que o lote foi aprovado. O script não extrai os dados numéricos automaticamente e não substitui leitura do enunciado ou análise das hipóteses. Não auditei figuras, outros conteúdos, navegador, desempenho de alunos ou validação externa.

## Quadro de critérios e decisão

| Critério para o recorte | Resultado |
|---|---|
| Identidade dos dez blocos na fotografia | Atendido. |
| Cálculos, unidades e arredondamento | Aritmética nominal correta; EX-032 usa y exato na igualdade. |
| Hipóteses suficientes para resultados mostrados | **Não atendido em EX-031:** falta excluir outros trabalhos nos equipamentos de troca térmica. |
| Rastreabilidade e reprodução de cálculos | Atendido no alcance dos dados de exercício e fontes citadas. |
| Critério integral de QA-09 | Não atendido: múltiplas ocorrências e classes ainda não examinadas. |
| Liberação do próximo ID | Não autorizada. |
