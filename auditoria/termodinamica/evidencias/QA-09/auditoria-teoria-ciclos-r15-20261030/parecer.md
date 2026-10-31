# QA-09 — parecer independente: ciclos térmicos r15

Data: 30/10/2026. Auditor automatizado: `/root/next_graphics`, distinto do Corretor `/root/next_theory`. **Parecer: ressalvas; três pontos de domínio requerem tratamento antes do aceite deste lote.** Os demais resultados pontuais referidos abaixo são consistentes no modelo declarado. Este parecer não altera produto ou controle, não aprova os 197 artigos nem encerra QA-09.

## Identidade e método

Examinei a cópia preservada `aplicacao-wika-r15-r1/resultado/depois-aula.html`, SHA-256 `f6c461f1d6039ea47dc7e97f9ad734bb0ea3fcb902f01ffdbf18d18d88e08d0e`, e o inventário r15 SHA-256 `c8c9c3a3e141eba47a16e9f85c69f97c6e8b8a55aab689c6120ef1a0070c9d9c`. A entrega examinada `teoria-ciclos-termicos-r15-20261030/entrega.md` tem SHA-256 `94441b841ee4edd30b79835eec0c161a0c92498a6abfbb557ea1c4e9f7e49dc8`. Li o conteúdo integral dos seis blocos identificados na entrega, incluindo texto, contas e expressões. O verificador independente confirma as seis âncoras, intervalos UTF-16 e hashes dos contêineres relatados pelo Corretor; os hashes cobrem o HTML integral dos blocos, não provam a física por si só. O script dele também passou na leitura da cópia r15.

## Ressalva 1 — Brayton real

Em `base-brayton-real`, os dois parágrafos afirmam que irreversibilidades aumentam o trabalho de compressão, reduzem trabalho de turbina e explicam a redução de trabalho líquido. A primeira afirmação enuncia condições de entrada, razão de pressões e temperatura de entrada de turbina; o segundo menciona “referências adiabáticas”, mas não torna clara a hipótese adiabática dos **componentes reais** na comparação. Mesmo fluido/composição, pressões de entrada/saída, regime permanente, mesmo estado de entrada de cada componente, apenas trabalho de eixo, variações cinética/potencial desprezíveis e operação adiabática real e de referência são um domínio suficiente usual. O texto sobre eficiência isentrópica em outro bloco não fixa suficientemente esta frase para leitura isolada.

Contramodelo: gás ideal de composição fixa com cₚ=1 e R=0,287 kJ/(kg·K), entrada 1000 K, pressão de saída/entrada `0,7^(1/0,287)≈0,288584`; T₂s=700 K e T₂=800 K. Com q=+200 kJ/kg para a turbina e ΔEc=ΔEp=0, `w=1000−800+200=400 kJ/kg`, ante 300 kJ/kg na referência adiabática reversível. A queda de entalpia real é menor, mas o trabalho real é maior. Para fronteira de calor a 2000 K, `Δs=ln(8/7)≈0,133531` e `sgen=Δs−200/2000≈0,033531 kJ/(kg·K)>0`. Não depende de projeto real construído. A condição adiabática dos componentes reais exclui o contraste.

A [MIT §6.9](https://web.mit.edu/16.unified/OldFiles/www/SPRING/thermodynamics/notes/node51.html), consultada 30/10/2026, discute a comparação por eficiências adiabáticas e despreza energias cinéticas; não é fonte do contramodelo.

## Ressalva 2 — fronteira energética do COP

Em `base-eficiencia-cop`, os valores QL, QH e W são definidos como calor no evaporador, calor no condensador e trabalho consumido, mas a igualdade `COPBC=COPR+1` só informa mesmo ciclo e mesmas fronteiras. Para inferi-la a partir dessas definições é necessário `QH=QL+W`, incluindo apenas os dois calores indicados e o trabalho líquido positivo, sem outro aporte de energia ao ciclo. O cenário de compressão apresentado posteriormente em `base-refrigeracao` estabelece adequadamente as hipóteses, mas não fica explícito na fórmula geral anterior.

Exemplo de balanço, não especificação de um equipamento: refrigerador por absorção recebe 600 kJ da fonte fria e 1000 kJ térmicos de acionamento, mais 40 kJ de trabalho, e rejeita 1640 kJ. `600/1000=0,6` é uma definição de COP térmico e `600/40=15` é razão sobre o trabalho, não o mesmo indicador. Se as temperaturas dos reservatórios são respectivamente 270 K, 500 K e 300 K, `Sger=1640/300−600/270−1000/500=1,24444… kJ/K > 0`. Para preservar a nomenclatura do balanço, QH designa toda a rejeição externa nessa hipótese, sem atribuí-la a um condensador específico. A [DOE](https://www.energy.gov/sites/default/files/2017/06/f35/CHP-Absorption%20Chiller-compliant.pdf) confirma a existência de refrigeração por absorção acionada termicamente; os números e balanço acima são hipotéticos.

## Ressalva 3 — Carnot e variação do COP real

Em `base-limite-carnot`, o contexto e as três equações identificam o **limite reversível**; em seguida lê-se “Aproximar as temperaturas das fontes melhora o COP de refrigeração”, sem o qualificador limite/reversível. A leitura pode atribuir melhora garantida ao COP real, o que não decorre apenas da diferença de temperaturas. Recomendo explicitar que a conclusão é para o **COP de Carnot** ou impor hipóteses adicionais para o equipamento real.

Contramodelo cíclico com apenas duas fontes: TH=400 K, W=1 kJ por ciclo. Primeiro TL=200 K, QL=0,9 kJ, QH=1,9 kJ, COP real 0,9 e COP Carnot 1; depois TL=300 K, QL=0,6 kJ, QH=1,6 kJ, COP real 0,6 e COP Carnot 3. Em cada estado `QH=QL+W` e `Sger=QH/TH−QL/TL` vale respectivamente 0,00025 e 0,002 kJ/K, ambas positivas. Logo os limites reversíveis aumentam enquanto os dois COPs reais hipotéticos diminuem. É contraste termodinamicamente admissível, não previsão do comportamento de uma máquina específica.

## Contas e fontes

Conferi os exemplos de Brayton 40%→30% e regeneração 30%→40% com trabalho fixo; Carnot 800 K/400 K dá eficiência 0,5 e COPs 1 e 2; refrigeração de compressão 600/200 dá 3 e 4; reaquecimento dá 1590 kJ/kg de trabalho líquido, 3590 kJ/kg de entrada, 2000 kJ/kg de rejeição e 44,29%; extração aberta `290/2490≈0,1165`. Neste último, ao substituir o valor arredondado, o balanço vale aproximadamente, enquanto a fração exata o satisfaz exatamente. Estes exemplos não validam estados físicos além das hipóteses declaradas. Nomenclatura dos ciclos foi lida no contexto ideal expresso; os balanços de refrigerador por compressão contêm hipóteses explícitas na seção correspondente.

Consultei [MIT, Rankine, aula 16](https://ocw.mit.edu/courses/2-60j-fundamentals-of-advanced-energy-conversion-spring-2020/1437d5925093b270c871160ec861fd12_MIT2_60s20_lec16.pdf) e [MIT, refrigeradores](https://web.mit.edu/16.unified/OldFiles/www/FALL/thermodynamics/notes/node25.html), 30/10/2026, como fontes primárias para os modelos, não para os números didáticos. A divergência de pressão crítica naquela aula MIT já foi registrada no trabalho de referências; este parecer não a utiliza nem a valida.

## Reprodução e limites

`python3 auditoria/termodinamica/evidencias/QA-09/auditoria-teoria-ciclos-r15-20261030/verificar.py` retornou `ok: true`, seis blocos. SHA-256 do verificador `3464c0dba08b275da3e7c7361f31df44d48f8070e78b1a4f53cc291cc449d22d`; usa frações exatas e tolerância 10⁻¹² na identidade logarítmica do contraste. As contas são digitadas após leitura, não extraídas automaticamente do HTML. Não houve edição do produto, navegador, estudantes ou revisão humana. As ressalvas requerem candidata e revisão da versão aplicada; todos os demais conteúdos e recursos continuam sujeitos aos seus próprios lotes.
