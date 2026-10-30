# QA-09 — reconciliação e recálculo dos diagnósticos 21–25, r13

Data: 30/10/2026. Corretor automatizado `/root/next_examples`. **Aguardando revisão independente da fotografia efetiva.** Lote de cinco diagnósticos de `#preparacao-questoes`, fora dos 197 artigos; não altera produto ou controle e não encerra QA-09.

## Versão e identidade

Aula r13 SHA-256 `f19000a7ddb1f3552b9633b0efec266fb3f6c5e5065808505a2f65b2005aefbc`; inventário r13 SHA-256 `0df99b79bcc2350581fcdded72435d30d07858de237a549e6228ca73682f8d9b`. A revisão localizada anterior de 21–25 examinou a foto r7 `200f9b773050594d762cc596a5a89297024b245fc4f504081fc77baaed3db95f`, com inventário `5090b9897a4698e0ad090f45182afba5880361aabc9fd3c3bdf848d971a85a1a`; seu parecer não é automaticamente transferido por hash igual.

O [verificador](verificar.py), executado sem escrita, confronta as fotografias e inventários, e reextrai os cinco diagnósticos por documento, seção, âncora, tag, número, intervalo UTF-16 e hash nas duas versões. Os blocos são byte a byte idênticos, embora suas posições mudem; a saída registra os dois intervalos. Além disso, li os enunciados e as bases r13 e refiz as contas abaixo. A passagem no script não avalia por si a suficiência do contexto nem representa parecer independente.

## Modelos, dados e contas

- **21 — enchimento:** tanque rígido inicialmente vazio, sem saída, calor ou trabalho, sem energia das paredes e com energias cinética/potencial desprezadas. Para gás ideal de composição fixa, referência comum de u e h e cₚ/cᵥ=1,25 constante conforme base `#base-balanco-transiente`, a massa final é a de entrada e `U₂=m_in h_in`, logo `u₂=h_in` e `T₂=1,25×320=400 K`. A massa se acumula; o processo não é permanente. Para gás ideal de composição fixa, a razão constante e cₚ−cᵥ=R constante justificam as capacidades constantes no modelo. Temperatura final é estado representativo de equilíbrio, não temperatura uniforme durante todo o enchimento.
- **22 — propriedade dependente de temperatura:** `Δh=∫₃₀₀⁴⁰⁰ (0,80+0,001T)dT=80+35=115 kJ/kg`. Coeficiente de T usa kJ/(kg·K²), T em K. Congelar cₚ(300)=1,10 kJ/(kg·K) daria 110 kJ/kg; não reproduz a integral. O valor no ponto médio é exato para esta função linear, não para qualquer cₚ(T). Base `#base-calor-variavel`.
- **23 — misturador:** em regime permanente com duas entradas e uma saída, sem trabalho e variações cinética/potencial desprezíveis, a massa de saída é 2+1=3 kg/s. Entalpias usam a mesma referência e modelos compatíveis conforme `#base-misturador-correntes`. Adiabático: `(2×100+1×400)/3=200 kJ/kg`; com +30 kW de calor: `(600+30)/3=210 kJ/kg`. O balanço obtém h de saída, não define por si temperatura ou fase.
- **24 — bocal:** `v₂²=v₁²+2×1000(h₁−h₂)=100²+2000×75=160.000 m²/s²`; a magnitude é `v₂=400 m/s`. Sem v₁² daria √150.000≈387,2983346 m/s, arredondado a 387,30 m/s com intervalo [387,295;387,305). Balanço de energia para regime estacionário, adiabático, sem trabalho e Δz desprezível não exige escoamento reversível. Base `#base-bocal-difusor`.
- **25 — estrangulamento e fase:** para modelo usual da base `#base-valvula-fase` (permanente, sem calor ou trabalho relevantes e ΔEc/ΔEp desprezíveis), `h₂≈h₁`. À pressão subcrítica de uma substância pura em equilíbrio, com entalpias da tabela didática na mesma referência, `(1000−500)/(2500−500)=0,25` dentro de [0,1]. Para 2700 kJ/kg o quociente algébrico 1,10 está fora do domínio: não é título, nem deve ser truncado para 1; consultar tabela superaquecida à pressão de saída.

Os valores são fornecidos como dados didáticos nominais, não propriedades medidas ou extraídas das fontes. Igualdades são exatas no modelo nominal; a única aproximação decimal exibida na comparação do bocal tem intervalo de arredondamento acima, que não é incerteza instrumental. As simplificações de estrangulamento e de entalpias compatíveis dependem das bases ligadas, não são universais para quaisquer válvulas e misturas.

## Referências e limites

- [MIT, aplicações da primeira lei: válvula e enchimento](https://web.mit.edu/16.unified/OldFiles/www/FALL/thermodynamics/notes/node17.html), seções 2.3.1–2.3.2, sustenta o balanço da válvula idealizada e o enchimento de tanque vazio de gás ideal; consultado em 30/10/2026.
- [NASA Glenn, conservação de energia](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/conservation-of-energy/), apoia entalpia e energia cinética na forma de escoamento; não fornece os dados fictícios aqui.
- [DOE, fundamentos, volume 1](https://www.energy.gov/sites/default/files/2026-04/DOE-HDBK-1012-92_VOL1.pdf), trata de entalpia, saturação e qualidade como fração mássica; não fornece as entalpias fictícias acima.

Solicita-se que outro Auditor confronte as bases r13, a identidade, aritmética, fontes e especialmente a suficiência das referências de estado/hipóteses dos diagnósticos 21, 23 e 25. Esta entrega não cobre integralmente todas as figuras, recursos, unidades ou ocorrências. Não houve teste em navegador, revisão humana, aluno ou certificação externa; QA-09 integral permanece pendente.
