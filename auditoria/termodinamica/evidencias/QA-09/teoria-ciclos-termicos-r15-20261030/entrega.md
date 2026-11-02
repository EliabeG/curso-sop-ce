# QA-09 — teoria de ciclos térmicos, fotografia r15

Data: 30/10/2026. Corretor automatizado `/root/next_theory`. Recalculei seis blocos de teoria de ciclos e COP, em parte com exemplos previamente verificados isoladamente. **Dois pontos de domínio requerem adjudicação independente:** comparação de componentes em `base-brayton-real` e restrição energética do COP em `base-eficiencia-cop`. O balanço nominal e demais relações descritos abaixo conferem em seus modelos. Não houve alteração de produto ou controle; QA-09 não foi encerrado. O bloco de exergia foi examinado no lote de segunda lei r13, evitando contar o mesmo exame como novo lote.

## Fotografia e identidade

Cópia preservada `evidencias/QA-09/aplicacao-wika-r15-r1/resultado/depois-aula.html` SHA-256 `f6c461f1d6039ea47dc7e97f9ad734bb0ea3fcb902f01ffdbf18d18d88e08d0e`; inventário r15 SHA `c8c9c3a3e141eba47a16e9f85c69f97c6e8b8a55aab689c6120ef1a0070c9d9c`. Script somente leitura `verificar.mjs`, SHA `f3f9f3e90061c513fee44e53fca484ab3c7fbab11bdaaa378cff58b529aa6f45`, verifica âncoras, hashes, intervalos e as contas e retornou `ok=true`. Hashes abaixo cobrem contêineres inteiros, não o texto direto das âncoras no inventário.

| Âncora | Início–fim UTF-16 | SHA-256 do bloco |
|---|---|---|
| base-eficiencia-cop | 299262–308797 | `d69c923666e5cbc712349c4dfe9e6a18f3ffdd7b5f6fe271dc745b29238c44f9` |
| base-limite-carnot | 308797–315231 | `382a2daf360ad0a04bfb9245f0746d547d8f5fa2d28e6b5b93d53621cb96bcfd` |
| base-refrigeracao | 365081–377906 | `2221e77dbbfa11591bcfac47c254e42941ab8074da717ac90975118425277955` |
| base-brayton-real | 377906–381233 | `ff66d7377eff5357668aae739c6390e23a38ad954acdd1b6af92447575e944a0` |
| base-comparar-ciclos | 381233–382466 | `adfa898e638f94b9eedc18ad7da9881f8bdb8c601bf51a30b8d61422f389f2bd` |
| base-ciclos-variantes | 382466–387076 | `7628014cf26268ba5dd27b7647ac9f89210ea977eba53e556e7c4efd8cd28198` |

## Ponto para adjudicação — Brayton e comparação de irreversibilidades

`base-brayton-real` afirma que, para mesma entrada, razão de pressão e temperatura de entrada da turbina, irreversibilidades elevam trabalho do compressor e reduzem o da turbina. Mais adiante diz que “nas referências adiabáticas” entalpia fornece trabalho, mas não explicita adiabaticidade **dos equipamentos reais** nem desprezo de ΔEc/ΔEp em ambos. O caso padrão adiabático com mesma substância/composição, estados de entrada e pressão de saída, sem outros trabalhos além do eixo e energias cinética/potencial desprezíveis sustenta a comparação; sem esse domínio uma transferência de calor altera o trabalho real. A [MIT, §6.9](https://web.mit.edu/16.unified/OldFiles/www/SPRING/thermodynamics/notes/node51.html) usa eficiências adiabáticas e despreza velocidades em seu modelo. Solicito que o Auditor decida se o contexto da aula basta ou exige explicitação, sem tratar todos os equipamentos reais como adiabáticos.

Contraste fictício, já examinado na auditoria da teoria isentrópica: gás ideal cp=1 e R=0,287 kJ/(kg·K), T₁=1000 K, T₂s=700 K, T₂ real=800 K, mesma p₂/p₁≈0,288584. Com q=200 kJ/kg recebido, ΔEc=ΔEp=0, wreal=400 kJ/kg e ws=300 kJ/kg; a razão de quedas de h seria 2/3, mas a razão de trabalho 4/3. Para calor na fronteira a 2000 K, Δs≈0,133531 e sger≈0,033531 kJ/(kg·K)>0. São balanços consistentes, não prova de construção de turbina específica. Adiabaticidade excluiria esse contraste do modelo.

## Ponto para adjudicação — COP e fronteira

`base-eficiencia-cop` apresenta `COPR=QL/W`, `COPBC=QH/W` e `COPBC=COPR+1` com mesmo ciclo e fronteiras. Isso é correto no modelo com trabalho positivo como único acionamento e com QL e QH representando os dois calores totais considerados: QH=QL+W. A formulação da tabela não explicita ausência de calor adicional de acionamento. Um refrigerador por absorção que recebe 600 kJ da carga fria, 1000 kJ térmicos de acionamento e 40 kJ de trabalho tem rejeição de 1640 kJ; o COP térmico é 0,6 e 600/40=15 é outra razão. A [DOE, absorção](https://www.energy.gov/sites/default/files/2017/06/f35/CHP-Absorption%20Chiller-compliant.pdf) distingue o acionamento térmico. Solicito Auditor decidir se a frase introdutória e o contexto já limitam suficientemente a tabela, ou se é preciso explicitar o modelo; a existência do refrigerador por absorção não invalida a fórmula no modelo mecânico.

## Contas e demais relações

- **Carnot:** para duas fontes a temperaturas absolutas constantes TH>TL>0, eficiência reversível=1−TL/TH e COPs reversíveis TL/(TH−TL) e TH/(TH−TL). O teste artificial TH=800 K e TL=400 K dá 0,5, 1 e 2, respectivamente. As relações de Carnot exigem dois reservatórios e operações reversíveis; a denominação do bloco e suas duas fontes definem esse recorte.
- **Refrigeração por compressão:** no modelo específico da seção, compressor/válvula adiabáticos, demais componentes sem trabalho não fluxo, vazão única, ΔEc/ΔEp e trocas nas ligações desprezíveis, `wc=h₂−h₁`, `qL=h₁−h₄`, `qH=h₂−h₃`, `h₄≈h₃`, logo Q̇H=Q̇L+Ẇin. Para 600 kJ de carga e 200 kJ de trabalho, COPR=3, rejeição 800 kJ e COPBC=4, na mesma fronteira/período. Não estender a equipamentos com calor de acionamento adicional sem balanço apropriado.
- **Brayton com dados nominais:** (90−30)/150=40% e (90−45)/150=30%, dados os demais valores mantidos. Reduzir 400 para 300 kJ é redução de 25%; com trabalho de 120 kJ fixo, rendimento muda de 30% para 40%. A hipótese de trabalho fixo evita generalização universal sobre regeneração e eficiência.
- **Reconhecer ciclos:** as descrições Brayton, Rankine, Otto, Diesel, Stirling ideal e Carnot correspondem aos modelos indicados no texto; o ciclo combinado aproveita a exaustão de gás para gerar vapor. Sequências ideais não identificam integralmente um equipamento real.
- **Reaquecimento e extração:** turbinas (3100−2500)+(3200−2200)=1600 kJ/kg, bomba 10, calor recebido 3590 e rejeitado 2000 kJ/kg; trabalho líquido 1590 e eficiência 1590/3590≈44,29%. As entalpias são fictícias: fechamento da primeira lei não prova existência física ou segunda lei. Para aquecedor aberto, y=(500−210)/(2700−210)=290/2490≈0,11646586; fração arredondada 0,1165 é aproximada, não identidade exata quando substituída. O [MIT, aula Rankine](https://ocw.mit.edu/courses/2-60j-fundamentals-of-advanced-energy-conversion-spring-2020/1437d5925093b270c871160ec861fd12_MIT2_60s20_lec16.pdf), pp. 8 e 10, apresenta reaquecimento e aquecedor aberto; não é fonte dos números do exercício. Seu valor de pressão crítica na p. 2 diverge da IAPWS, como registrado em parecer de referências, e não é usado aqui.

Todos os dados numéricos são hipotéticos ou nominais; a aritmética do script não aprova automaticamente modelo ou interpretação. Fontes abertas pela ferramenta web em 30/10/2026. Sem teste em navegador, leitores de tela, alunos, revisão humana ou verificação integral dos recursos. Blocos sobrepostos não representam contagem de itens concluídos; qualquer decisão futura se vincula à versão e ao contexto revisados.
