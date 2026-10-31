# QA-09 — candidata isolada para `base-isentropica`, r13

Data: 30/10/2026. Corretor automatizado `/root/next_theory`. Candidata não aplicada, aguardando Auditor distinto. Responde ao [parecer independente da teoria de segunda lei](../../../pareceres/QA-09-teoria-segunda-lei-entropia-r13-auditoria-independente-20261030.md), sem encerrar QA-09 nem liberar outro ID.

## Escopo e alterações

O bloco existente apresenta diferenças de entalpia como razões de trabalho e afirma que irreversibilidade altera o trabalho de turbina e compressor sem explicitar o modelo de balanço que sustenta ambas. A candidata acrescenta, antes das equações, condições suficientes: regime permanente, uma entrada/saída, adiabático, apenas trabalho de eixo, ΔEc/ΔEp desprezíveis, referência adiabática internamente reversível com mesmo estado de entrada e pressão de saída e diferenças de entalpia positivas adequadas às funções de ambos os equipamentos. Não se diz que todos os equipamentos são adiabáticos. As duas notas de irreversibilidade passam a ser expressamente ligadas à comparação adiabática e ao trabalho específico. Nenhum MathML, legenda, link ou símbolo é alterado.

Essas condições permitem que o balanço estacionário reduza o trabalho específico de eixo à queda de h na turbina e ao aumento de h no compressor; para igual estado de entrada e pressão de saída, a referência adiabática reversível e o real adiabático são comparáveis no modelo. O [MIT, §6.9](https://web.mit.edu/16.unified/OldFiles/www/SPRING/thermodynamics/notes/node51.html) apresenta eficiências adiabáticas com mesma razão de pressão; [Purdue ME200](https://engineering.purdue.edu/ME200/files/homework/HW36/ME200-Spring2020-HW36-web.html) usa regime permanente, adiabaticidade e mudanças cinéticas/potenciais desprezíveis. As fontes são conceituais, não fontes dos números fictícios.

O contramodelo do parecer continua útil: gás ideal com cp=1 e R=0,287 kJ/(kg·K), T₁=1000 K, T₂s=700 K e T₂=800 K na mesma p₂, recebe q=200 kJ/kg a 2000 K; wreal=400 e ws=300 kJ/kg, mas a razão das quedas de h é 2/3. A geração de entropia calculada é ≈0,03353 kJ/(kg·K)>0. É teste de balanços, não projeto de turbina. A nova condição adiabática exclui esse caso do domínio da redução.

## Fotografia e simulação

Fonte preservada r13 `evidencias/QA-09/aplicacao-energyplus-fichas-r13-r1/resultado/depois-aula.html` SHA-256 `f19000a7ddb1f3552b9633b0efec266fb3f6c5e5065808505a2f65b2005aefbc`; inventário r13 SHA `0df99b79bcc2350581fcdded72435d30d07858de237a549e6228ca73682f8d9b`. O bloco original, UTF-16 331818–337684, tem SHA `c8a1b942f070d194b11f44fc8f8d190cba5571cf668cba384de6864816558d7b`; o candidato `2c95d8e5d8d90d01fe365ee214ec4664ccd4dc08cd2e108a66931011a777c17f`. Os arquivos de fragmentos adicionam uma quebra final, excluída dos hashes. Manifesto `manifesto.json` enumera as três substituições únicas no bloco; texto fora do bloco permanece igual na simulação.

`node auditoria/termodinamica/evidencias/QA-09/candidata-teoria-isentropica-r13-20261030/verificar.mjs` é somente leitura e passou: a simulação preserva 197 artigos, 734 MathML e atributos identificadores, links e ARIA, e gera HTML hipotético SHA `926c6b3e346763d9cac262d2b17174e5538f2acaafc14f0dede2f62665b0523a`. Também reconfirma a aritmética do contramodelo; isso não é teste de navegador ou avaliação independente.

Antes de aplicação, Auditor distinto deve conferir modelo, notas, fontes e delta. Uma futura aplicação exige fotografia/mapa novos, reconciliação de nós e recursos, verificação dos artigos e reavaliação localizada dos aceites relacionados; a versão aplicada requer outra auditoria. Não houve teste em navegador real, leitor de tela, estudantes ou revisão humana.
