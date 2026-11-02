# QA-09 — auditoria da teoria de segunda lei e entropia, r13

Data: 30/10/2026. Auditor: agente automatizado independente `/root/next_graphics`, distinto do Corretor `/root/next_theory`. **Veredito: AJUSTES OBRIGATÓRIOS para o bloco `base-isentropica`**, por ausência de hipóteses na interpretação das diferenças de entalpia como trabalhos e nas afirmações sobre irreversibilidade. As demais relações examinadas não apresentaram divergência no alcance abaixo. QA-09 integral continua aberto e não se libera outro ID.

## Identidade e escopo

Aula `modulos/e1-termodinamica.html` e sua fotografia efetiva SHA-256 `f19000a7ddb1f3552b9633b0efec266fb3f6c5e5065808505a2f65b2005aefbc`; inventário r13 `0df99b79bcc2350581fcdded72435d30d07858de237a549e6228ca73682f8d9b`. A entrega do Corretor `evidencias/QA-09/teoria-segunda-lei-entropia-r13-20261030/entrega.md` tem SHA-256 `487bf6c0d305e192c4429d4560fcea7cbd0368f3f1a7a1db6413eb9e4c48ba7f`. Examinei os sete contêineres por âncora, posições e hashes na entrega, incluindo texto e fórmulas em MathML. `evidencias/QA-09/auditoria-teoria-segunda-lei-r13-20261030/verificar.mjs`, SHA-256 `410df370dfa0e87e538dee19b87bdef4c5d031601461a1ebd1edffa88274c66c`, é somente leitura e passou na identificação e nas contas do contramodelo e dos demais exemplos. Os sete contêineres incluem nós sobrepostos; este parecer não confere automaticamente todo registro subordinado, todos os recursos ou todo o curso.

## Ajuste obrigatório — interpretação da eficiência

O bloco `base-isentropica` apresenta `(h₁−h₂,real)/(h₁−h₂,s)` como “trabalho real sobre ideal” de turbina e `(h₂,s−h₁)/(h₂,real−h₁)` como “trabalho ideal sobre real” de compressor. Especifica a mesma pressão de saída de referência, mas não explicita, no próprio bloco, regime permanente, uma entrada e uma saída, mesmo estado de entrada, calor e mudanças de energia cinética/potencial desprezíveis e denominadores definidos. Sem as hipóteses do balanço que reduzem trabalho de eixo às diferenças de entalpia, essas expressões não determinam necessariamente as razões de trabalhos. As frases “a irreversibilidade reduz o trabalho produzido” e “a irreversibilidade aumenta o trabalho consumido” também necessitam ser vinculadas à comparação adiabática correspondente, em vez de enunciadas para equipamento arbitrário com calor ou variações de energia cinética.

Confrontei independentemente o contraste fictício de turbina: gás ideal com cp=1 e R=0,287 kJ/(kg·K), T₁=1000 K, referência isentrópica T₂s=700 K e saída real T₂=800 K, ambas na razão de pressão `p₂/p₁=0,7^(1/0,287)=0,288583779`. Com q=200 kJ/kg recebido e ΔEc=ΔEp=0, `w_real=q+h₁−h₂=400 kJ/kg`, enquanto referência adiabática `w_s=h₁−h₂s=300 kJ/kg`; as quedas de entalpia dão 200/300=2/3, e a razão de trabalhos é 400/300=4/3. Independente da prova de construção de uma turbina, os balanços são coerentes: `Δs=cp ln(0,8)−R ln(0,288583779)=0,133531393 kJ/(kg·K)` e, para fronteira térmica a 2000 K, `s_ger=Δs−q/Tb=0,033531393 kJ/(kg·K)>0`. O exemplo mostra que calor não nulo afeta a interpretação das razões e da comparação de trabalho.

A [MIT, Thermodynamics §6.9](https://web.mit.edu/16.unified/OldFiles/www/SPRING/thermodynamics/notes/node51.html), apresenta eficiências adiabáticas e mesma razão de pressão, desprezando energia cinética em seu modelo; a [Purdue ME200](https://engineering.purdue.edu/ME200/files/homework/HW36/ME200-Spring2020-HW36-web.html) usa equipamento adiabático em exemplo aplicado. São apoios de modelos, não fontes dos números fictícios acima. Não se deve apresentar adiabaticidade como propriedade de todas as turbinas ou compressores.

**Ajuste exigido:** delimitar o modelo em que entalpias representam trabalhos específicos — ao menos regime permanente, uma entrada/saída, mesmo estado de entrada e pressão de saída para a referência, calor e variações cinética/potencial desprezíveis, sem outros trabalhos e denominadores apropriados — e associar as duas afirmações sobre irreversibilidade à comparação nesse modelo. Preservar índices, sinais e fórmulas; os valores de entrada/saída devem ser fisicamente coerentes com o papel de turbina ou compressor.

## Demais blocos examinados

Os enunciados de Kelvin–Planck e Clausius qualificam o único efeito; o balanço do sistema fechado usa temperatura de fronteira apropriada e geração não negativa. A equivalência das formas de Δs para gás ideal com capacidades constantes segue de `cp−cv=R` e da equação de estado; os logaritmos usam razões de temperaturas e pressões absolutas. O bloco anterior enquadra explicitamente o balanço como de sistema fechado; a conclusão sobre adiabático internamente reversível deve ser entendida nesse contexto. Em volume de controle, as condições de entrada/saída e regime exigem identificação própria.

Recalculei Carnot para 800/400 K: η=0,5, para QH=600 kJ Wmáx=300 e QL,mín=300 kJ; rejeição de 120 leva a W=480 e η=0,8, acima do limite para dois reservatórios. Com ambiente de referência a 290 K e Sger=0,10 kJ/K, exergia destruída=29 kJ. Em `dh=Tds+vdp`, composição fixa e modelo simples compressível, para variação isentrópica e v aproximadamente 0,001 m³/kg, Δp=800 kPa resulta Δh≈0,8 kJ/kg. Os valores são fictícios e nominais; exergia destruída não é energia que desaparece, e a identidade de Gibbs não transforma calor real irreversível em Tds. A [MIT OCW, segunda lei](https://ocw.mit.edu/courses/16-050-thermal-energy-fall-2002/0d600615983322e758cd9d75fa3b6758_04_part1b.pdf) e a [MIT OCW, relações de Gibbs](https://www.ocw.mit.edu/courses/2-611-marine-power-and-propulsion-fall-2006/4c32b0845d40ee00555da443f8a0f58b_06second_law.pdf) foram abertas em 30/10/2026 para apoio conceitual, não como fontes dos números.

| Critério | Resultado |
|---|---|
| Identidade dos sete contêineres na fotografia | Atendido no recorte indicado. |
| Eficiência de turbina/compressor e comparação de trabalho | Não atendido: hipóteses de balanço ausentes no bloco. |
| Demais relações e valores examinados | Sem divergência nas condições descritas. |
| QA-09 integral e próximo ID | Não atendidos; permanecem bloqueados. |

Após candidata isolada e revisão por agente distinto, aplicar somente com nova fotografia e mapa e verificar os efeitos em fichas, exemplos, referências e aceites anteriores. Nenhum ensaio em navegador, leitor de tela, estudante, revisão humana ou certificação externa foi realizado nesta auditoria.
