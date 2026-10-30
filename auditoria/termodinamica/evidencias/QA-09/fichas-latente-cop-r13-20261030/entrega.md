# QA-09 — fichas 23, 58 e 59: calor latente, rendimento e COP

Data: 30/10/2026. Corretor automatizado `/root/next_formulas`. **Revisão independente e adjudicação de três pontos de domínio pendentes.** Não foram alterados produtos nem históricos. QA-09 integral permanece aberto; não iniciar outro ID.

## Fotografia e reconciliação

Formulário r13 SHA-256 `5f3f31a4801f96a2b78b40c75d37392f6b16d264901ac313ac00458901970285`; inventário r13 SHA-256 `0df99b79bcc2350581fcdded72435d30d07858de237a549e6228ca73682f8d9b`. Durante a preparação, o formulário mudou da fotografia r12 (`6857fd83e0b2e49c804903cff1dea4128a665ab22eb27bac4ab15d6c557ff756`) para r13. Comparei os três artigos completos no inventário: seus deslocamentos UTF-16 e hashes coincidem, e reextraí e li os fragmentos sobre a **versão r13 efetiva**. Isso é reconciliação de identidade limitada; igualdade de hash isolada não transfere parecer de outra versão. O arquivo [identidades.json](identidades.json), SHA-256 `65896ac3f23f75811dfad16d9ced86492f77207482593564112ec9792d2fecf6`, registra documento, âncora, posições e hash de cada ficha.

[verificar.py](verificar.py), SHA-256 `d5a03c34f44ff95b64b0606a028cd06c57543ef1d197eb89c9578cffcb4edcce`, é somente leitura e passou, confirmando a fotografia, a unicidade e o hash de cada fragmento e contas fictícias. Ele não interpreta MathML nem decide o domínio. Os números são casos inventados, não medições ou valores obtidos das referências.

## 23 — calor latente de vaporização

A ficha escreve `hfg=hg−hf`, `Q=mhfg` para massa fechada e `ṁ=Q̇/hfg` para escoamento permanente. Os modelos devem diferenciar a massa fechada do volume de controle; p v já está incluído em entalpia de escoamento. Dados fictícios hf=500 e hg=2500 kJ/kg dão hfg=2000 kJ/kg; vaporizando m=2 kg, `m hfg=4000 kJ`; em escoamento com Q̇=6000 kW e sem trabalho não associado ao escoamento, `ṁ=3 kg/s`. A divisão exige hfg não nulo, substância pura e estados saturados distintos. As mesmas unidades e referência de h devem ser usadas.

**Ponto para Auditor:** para a identidade Q=m hfg da massa fechada, os estados devem ser líquido e vapor saturados na mesma pressão p e o trabalho de fronteira efetivo deve ser `Wb=p(V₂−V₁)`, sem outros trabalhos e com ΔEc/ΔEp desprezíveis. A ficha diz pressão fixa e só trabalho pV, mas não esclarece explicitamente qual pressão é usada no trabalho. A interpretação habitual pode implicar o mesmo p; os ajustes da ficha 29 e da base da aula foram mais explícitos. Solicito julgar se o cartão independente deve explicitar a identidade. A redução de escoamento tem condições separadas e não exige impor mecanismo quase estático do sistema fechado ao vaporizador.

## 58 — máquina térmica

Para ciclo de mesma fronteira com variação líquida de energia nula, calor total recebido QH>0, calor total rejeitado QL>0 e nenhum outro calor fora desses totais, `Wlíq=QH−QL` e `η=Wlíq/QH`. Exemplo fictício QH=500 e QL=300 kJ: Wlíq=200 kJ e η=0,4. Cada grandeza deve se referir ao mesmo ciclo, e trabalho líquido positivo caracteriza operação motora.

**Ponto para Auditor:** a ficha diz apenas “QH e QL são magnitudes positivas do mesmo ciclo”; se elas representarem só uma fonte quente e uma fria, outra entrada de 50 kJ também atravessando a fronteira não consta de `QH−QL`. Nesse exemplo o trabalho é 500+50−300=250 kJ e a razão ao calor total recebido é 250/550=5/11≈0,4545. Se QH significar **todo o calor recebido** e QL todo o rejeitado, a igualdade continua válida; se houver duas fontes quentes, QH deve ser o total para a razão global definida. Pedir ao Auditor verificar se símbolos e a aula garantem adequadamente essa interpretação ao consultar a ficha isolada. Não se pretende impor apenas dois reservatórios para o balanço geral.

## 59 — COP de refrigerador

Para ciclo **acionado somente por trabalho** sob fronteira e período comuns, com `Win>0` e QL≥0 de mesma unidade, a razão `COP_R=QL/Win` é adimensional. QL=600 kJ e Win=200 kJ dão COP=3. A fórmula pode servir para uma razão de refrigeração por trabalho com fronteira claramente definida; não é automaticamente a medida convencional do desempenho de todo refrigerador com outras entradas energéticas.

**Ponto para Auditor:** a ficha não explicita acionamento por trabalho como fonte energética relevante. Em ciclo por absorção, o COP térmico costuma ser carga frigorífica dividida pelo calor de acionamento. Caso hipotético QL=600 kJ, calor de acionamento=1000 kJ e trabalho elétrico=40 kJ: COP térmico=0,6, enquanto QL/Win=15 expressa apenas outra razão, não o mesmo indicador. Os números não são dados de equipamento comercial e a fronteira deve ser indicada. A referência do DOE abaixo usa a definição térmica para absorção; revisar se o cartão isolado deve limitar explicitamente seu domínio ao ciclo por trabalho.

## Referências e limites

- MIT, [derivação de Q=ΔH em processo isobárico reversível com trabalho pV](https://web.mit.edu/10.213/oldpages/f99/supp/readings/qdh/index.html), consultado em 30/10/2026: caso suficiente; Wb=pΔV e balanço são a condição mais geral usada no texto, sem afirmar reversibilidade necessária em qualquer processo.
- MIT OCW, [ciclo de Brayton e primeira lei cíclica, §A.3](https://ocw.mit.edu/courses/16-050-thermal-energy-fall-2002/7ad40d4087bf332cf6da225f14cfd565_03_part1a_to_CMS.pdf), p. 6–7 do PDF: exemplo de balanço e rendimento, não prova de que toda máquina possua apenas uma fonte ou sorvedouro.
- U.S. DOE, [Absorption Chillers for CHP Systems](https://www.energy.gov/sites/default/files/2017/06/f35/CHP-Absorption%20Chiller-compliant.pdf), definição do COP térmico da máquina por absorção. Os casos deste relatório são fictícios e não são dados dessas fontes.

Não há parecer próprio ou candidata nesta entrega. Outro agente deve examinar o MathML e condições efetivamente escritos, os vínculos das três fichas, os três possíveis ajustes e as referências. Fichas, nós filhos e versões não citadas não herdam revisão por similaridade. Não houve navegador real, validação com alunos, revisão humana nem certificação externa.
