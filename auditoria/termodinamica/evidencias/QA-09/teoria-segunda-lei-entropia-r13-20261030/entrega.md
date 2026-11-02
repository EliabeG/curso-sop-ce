# QA-09 — teoria da segunda lei e entropia, fotografia r13

Data: 30/10/2026. Corretor automatizado `/root/next_theory`. Escopo de sete blocos de teoria; **possível ajuste de domínio em `#base-isentropica` requer adjudicação independente**. Os demais blocos não apresentaram divergência no alcance lido. Sem edição de produto ou controle; não se conclui QA-09 integral nem se inicia outro ID.

## Fotografia e método

Fonte preservada `evidencias/QA-09/aplicacao-energyplus-fichas-r13-r1/resultado/depois-aula.html`, SHA-256 `f19000a7ddb1f3552b9633b0efec266fb3f6c5e5065808505a2f65b2005aefbc`; inventário r13 SHA `0df99b79bcc2350581fcdded72435d30d07858de237a549e6228ca73682f8d9b`. O verificador somente leitura `verificar.mjs`, SHA `68096a618fd4369e38bdeeefd3ae86267679092b5eefc0446fe8c4ac3effb55b`, confirma âncoras, intervalos e hashes e recalcula as contas; `ok=true`. Os hashes são dos contêineres inteiros, não dos títulos registrados no inventário. Leitura de contexto e consulta de fontes não são substituídas por script.

| Âncora | Início–fim UTF-16 | SHA-256 do contêiner |
|---|---|---|
| base-segunda-lei | 298129–298744 | `0ebd5bd15efd674139b4406ad0738be67c7d9cbd88f52f0496f623a73d49f617` |
| base-entropia | 314713–320119 | `3a42d1f246191f62e01f4563f3883ae4d317022492621258fa00cec5657061d3` |
| base-entropia-gas | 320119–331818 | `1f92506c9418009d1ec8bba9cbd51e328946ec89cecae58219936973f02a9df3` |
| base-isentropica | 331818–337684 | `c8a1b942f070d194b11f44fc8f8d190cba5571cf668cba384de6864816558d7b` |
| base-carnot-prova | 337684–340314 | `21d73236cb2cb1e129daa15c48bdd780bdc79171782bb3f3ee3c4d45cef795c6` |
| base-exergia | 340314–343244 | `23ce04f24f08f852e88524c64f08f9f3ddc11a41a01ffedefacbead5e9d02a1d` |
| base-gibbs | 343244–345574 | `15d6533d14b70ecda54f9472aec8a20b85b6872f38b2f6f6e99087f2a653b232` |

## Segunda lei, entropia e gás ideal

Os enunciados de Kelvin–Planck e Clausius qualificam o **único efeito**, de modo que o trabalho de um refrigerador não é ignorado. Na formulação de sistema fechado, ΔS=∫δQ/Tb+Sger, com temperatura de fronteira local e soma por contatos; Sger≥0. A fronteira e a diferença de temperatura são tratadas explicitamente. Um sistema fechado adiabático e internamente reversível tem ΔS=0, mas adiabático irreversível pode ter ΔS>0. A fórmula para gás ideal com capacidades constantes, Δs=cp ln(T₂/T₁)−R ln(p₂/p₁)=cv ln(T₂/T₁)+R ln(v₂/v₁), usa pressão e temperatura absolutas e razões adimensionais. A equivalência segue de cp−cv=R e p₂/p₁=(T₂/T₁)(v₁/v₂). As relações isentrópicas listadas exigem o mesmo modelo e k constante; não demonstram reversibilidade de um processo real arbitrário. A [MIT OCW, segunda lei e gás ideal](https://ocw.mit.edu/courses/16-050-thermal-energy-fall-2002/0d600615983322e758cd9d75fa3b6758_04_part1b.pdf) fornece a base conceitual.

## Ponto de domínio — eficiência isentrópica

O bloco `#base-isentropica` apresenta as razões de diferenças de entalpia como “trabalho real sobre ideal” e “trabalho ideal sobre real” e afirma sem ressalva que irreversibilidade reduz trabalho da turbina e aumenta consumo do compressor. Para interpretar diferenças de entalpia estática como trabalhos específicos de eixo, é preciso ao menos regime permanente, uma entrada e saída, condições reais e de referência com mesmo estado de entrada e pressão de saída, calor e variações de energia cinética e potencial desprezíveis, além de denominadores adequados. A pressão de saída comum aparece no símbolo h₂,s, mas as condições restantes não estão no bloco. [MIT, eficiência adiabática de turbina e compressor](https://web.mit.edu/16.unified/OldFiles/www/SPRING/thermodynamics/notes/node51.html) explicita o modelo adiabático e despreza energia cinética; [Purdue, análise de equipamento](https://engineering.purdue.edu/ME200/files/homework/HW36/ME200-Spring2020-HW36-web.html) explicita regime permanente, adiabaticidade e energia cinética/potencial desprezível. Solicito Auditor adjudicar e, se confirmado, preparar redação que delimite as duas expressões e as afirmações de trabalho, sem prescrever adiabaticidade para todos os equipamentos.

Contraste numérico fictício para uma turbina estacionária com 1 entrada/1 saída, ΔEc=ΔEp=0 e gás ideal com cp=1 e R=0,287 kJ/(kg·K): T₁=1000 K, saída isentrópica de referência T₂s=700 K e saída real T₂=800 K, no mesmo p₂/p₁=(0,7)^(1/0,287)≈0,28858. Calor recebido q=200 kJ/kg de fronteira a 2000 K. `wreal=q+h₁−h₂=400 kJ/kg`; na referência adiabática `ws=h₁−h₂s=300 kJ/kg`; a razão das quedas de entalpia é 200/300=2/3, não a razão dos trabalhos 400/300. `Δs=ln(0,8)−0,287 ln(0,28858)≈0,13353`, enquanto q/Tb=0,10000 kJ/(kg·K), resultando Sger≈0,03353 kJ/(kg·K)>0. Este é um teste de consistência por primeira e segunda leis, não projeto ou demonstração de construção de turbina. Mostra por que as conclusões precisam ser vinculadas ao modelo adiabático comparado.

## Carnot, exergia e Gibbs

Para 800 e 400 K, ηC=0,5 e para QH=600 kJ os limites são Wmáx=300 kJ e QL,mín=300 kJ. Com rejeição de 120 kJ, a primeira lei dá W=480 kJ e η=0,8, acima do limite para dois reservatórios; não é dispositivo permitido. Um ciclo completamente adiabático com ΔE=0 apresenta Wlíq=0 e rendimento por QH indefinido, conforme texto. Para T₀=290 K e Sger=0,10 kJ/K, destruição de exergia=29 kJ, na comparação com ambiente de referência constante e mesmas restrições; exergia transportada é contabilizada separadamente. Na relação `dh=Tds+vdp`, substância simples compressível e composição fixa, ao longo de variação isentrópica com v≈0,001 m³/kg, Δp=800 kPa dá Δh≈0,80 kJ/kg. A identidade de propriedades não confunde calor real irreversível com Tds; [MIT, relações de Gibbs](https://www.ocw.mit.edu/courses/2-611-marine-power-and-propulsion-fall-2006/4c32b0845d40ee00555da443f8a0f58b_06second_law.pdf).

Dados numéricos fictícios e nominais, não dados de laboratório. Foram examinados texto, fórmulas e hipóteses dos blocos citados, não todos os recursos, imagens ou links de toda a aula. Não houve teste em navegador, leitores de tela, ensaio com estudantes ou revisão humana. A fonte efetiva pode mudar; a reconciliação de versão é necessária para qualquer aplicação ou aceite.
