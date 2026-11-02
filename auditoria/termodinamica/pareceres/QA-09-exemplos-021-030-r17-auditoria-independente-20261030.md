# QA-09 — auditoria independente EX-021–030 na r17

30/10/2026. Auditor `/root/planning`, distinto do Corretor `/root/next_examples`. **Veredito: AJUSTE OBRIGATÓRIO no lote, por insuficiência do enunciado EX-027.** As demais nove verificações não apontaram divergência no alcance e nas hipóteses abaixo. Nenhum objeto foi integrado ao ledger por este parecer; QA-09 permanece em correção.

## EX-027: enunciado e contramodelo

A aula diz que a máquina “recebe 1.000 kJ por ciclo e rejeita 600 kJ”, e conclui W=400 kJ e η=40%. Esses números são corretos quando 1.000 kJ é o **calor total recebido**, 600 kJ é a **única rejeição de calor**, ambos na mesma fronteira e período, e W é trabalho líquido de um ciclo completo. A frase não explicita que não há outra entrada ou rejeição de energia. A base próxima `#base-refrigeracao` exclui trocas adicionais para um ciclo reverso de compressão de vapor; o EX-027 é uma máquina térmica, portanto essa condição de outro dispositivo não elimina a ambiguidade. A base anterior `#base-eficiencia-cop` apresenta o balanço do modelo de máquina, mas não identifica explicitamente os totais específicos do EX-027; o enunciado pode ser tornado suficiente de forma direta.

Contramodelo físico nominal: um ciclo recebe 1000 kJ a 800 K e mais 200 kJ a 600 K, rejeita 600 kJ a 300 K e entrega W=600 kJ. Energia: 1000+200−600=600. Entropia gerada para reservatórios ideais: 600/300−1000/800−200/600=5/12 kJ/K>0. Ele satisfaz as duas quantidades citadas sem tomá-las como totais, e dá outro trabalho por ciclo e outra eficiência. É construção de contraste, não dado do curso ou de produto real.

Solicito candidata isolada que explicite que os 1.000 kJ são todo o calor recebido, que 600 kJ são todo o calor rejeitado, que são as únicas trocas de calor e que o trabalho é líquido na mesma fronteira e por ciclo. Preservar o objetivo de 400 kJ e 40%, reconstruir a versão aplicada e exigir revisão independente. O defeito é de suficiência das hipóteses, não de aritmética quando elas valem.

## Outras nove verificações

- **021:** no misturador permanente adiabático sem trabalho e com variações cinética/potencial desprezíveis, entalpias compatíveis, (1×100+3×300)/4=250 kJ/kg e 4×250=1000 kW; fase não é determinada.
- **022:** bocal permanente adiabático e sem trabalho: v₂=√(50²+2×40.000)=287,2281… m/s, arredondado a 287,23. A entalpia deve ser convertida de kJ/kg a J/kg e a raiz é magnitude.
- **023:** estrangulamento com h₂≈h₁ e dados de saturação à pressão de saída: (950−400)/(2600−400)=0,25 em massa, sob equilíbrio bifásico e referências compatíveis; a tabela é didática.
- **024:** duas fontes a 800 e 400 K, QH=600 kJ: ηC=0,5, Wmáx=300 e rejeição mínima 300 kJ. Proposta rejeitando 120 produz W=480 kJ, mas Sger=120/400−600/800=−0,45 kJ/K e viola segunda lei no modelo de duas fontes.
- **025:** 290×0,10=29 kJ de exergia destruída, ambiente uniforme e comparação compatível; não é destruição de energia nem Sger equivalente à variação de entropia do sistema.
- **026:** para substância simples compressível de composição fixa, estados de equilíbrio, ds=0 e v≈0,001 m³/kg, Δh≈vΔp=0,80 kJ/kg; não conclui automaticamente trabalho de bomba real.
- **028:** ciclo simples de refrigeração da base, sem trocas adicionais declaradas: COPR=600/200=3, QH=600+200=800 kJ e COPBC=4. Sem temperaturas, não se avalia viabilidade por segunda lei.
- **029:** no modelo do contêiner, sem consumos adicionais, potência líquida 90−30=60 kW e η=40%; com compressor a 45 kW e demais valores mantidos, 45 kW e 30%. A comparação é hipotética.
- **030:** mantendo 120 kJ de trabalho líquido por ciclo, redução de calor externo (400−300)/400=25%, η=30%→40%, aumento de 10 pontos percentuais. Não demonstra desempenho de regenerador real específico.

Os valores são nominais e não indicam incerteza experimental. Examinei diretamente as bases e a alteração de `base-brayton-real` r16: os exemplos 029/030 continuam no contexto de potência líquida, hipóteses e regeneração indicadas; o intercooling em outra base r17 não altera suas contas.

## Identidade e fontes

Aula r17 SHA `6b0df1096d0b6de6995ffc51bf8489cb45ab954a7aabdeb3f48d068c9777c57c`, inventário `b8eae39cc72cf807d7b84aad7e7a38423168b809231bc3b7f08c439d6d25163b`, entrega SHA `75e44ad28204c1dc4ab1639cc50a779e4a0438a809d29225679bef062f0caed3`. O verificador do Corretor foi executado em leitura; meu verificador `auditoria/termodinamica/evidencias/QA-09/auditoria-exemplos-021-030-r17-independente-r1/verificar.py` SHA `eaff47c7adf78e6288dd57d03887619e9fc050064d799c8b9389b7a1073a9c2a` confronta os dez recortes e contêineres com inventário, hashes e foto r17, refaz contas e contramodelo. O parecer r7 histórico foi considerado no alcance; igualdade de hash não transfere aceites.

Consultei independentemente [MIT, estrangulamento e primeira lei](https://web.mit.edu/16.unified/OldFiles/www/FALL/thermodynamics/notes/node17.html), [MIT, refrigeradores](https://web.mit.edu/16.unified/OldFiles/www/FALL/thermodynamics/notes/node25.html), [OpenStax, ciclo de Carnot](https://openstax.org/books/university-physics-volume-2/pages/4-5-the-carnot-cycle) e [MIT, relações entre propriedades](https://live.ocw.mit.edu/courses/16-050-thermal-energy-fall-2002/0d600615983322e758cd9d75fa3b6758_04_part1b.pdf). Apoiam os modelos físicos, não os números fictícios dos exercícios. Fontes e nós contextuais não são integralmente aprovados por este parecer. Sem teste de navegador, leitor de tela, estudantes, revisão humana ou certificação externa.
