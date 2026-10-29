# BAN-08 — apoio científico independente AV36–AV40

Data 29/10/2026. Autora dos cálculos e revisora: agente automatizado `/root/auditor_ban08_novo`. Exame parcial sem cegamento, sem aprovação global de BAN-08 nem liberação do próximo ID. Produto e controle não alterados. Enunciados, comentários e bases locais em `modulos/e1-termodinamica.html`, SHA-256 `80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0`; hashes individuais dos trechos brutos UTF-8 `<article>...</article>`. Os cinco itens são autorais de cinco alternativas e pontuáveis; referências CR são origem de comparação, não fonte dos dados novos. Igualdade de operações com dados didáticos não infere incerteza experimental.

Fontes de modelo consultadas em 29/10/2026: OpenStax Physics §12.2, https://openstax.org/books/physics/pages/12-2-first-law-of-thermodynamics-thermal-energy-and-work (primeira lei); OpenStax University Physics v.2 cap. 4, https://openstax.org/books/university-physics-volume-2/pages/4-key-equations (Carnot e entropia); MIT OCW 2.611, segunda lei p. 3, https://www.ocw.mit.edu/courses/2-611-marine-power-and-propulsion-fall-2006/4c32b0845d40ee00555da443f8a0f58b_06second_law.pdf (Gibbs); Simpson, tese Stanford, apêndice A.2–A.3 p. 109 https://web.stanford.edu/group/peec/cgi-bin/docs/systems/research/AdamPSimpson_PhDThesis_Final_Draft.pdf (destruição de exergia T0Sger).

## AV36 — E

Hash `6b740a5a219f82f11f8e03899fb670df2cc54663545c07731f48643f1edb7285`; bases `#base-trabalho-fronteira`, `#base-entropia`, `#base-balanco-fechado`. Expansão reversível adiabática de gás ideal fechado, apenas trabalho de fronteira e ΔEC/ΔEP desprezíveis: Q=0; se W>0, ΔU=−W<0, então ΔT<0 para cv>0; reversibilidade e adiabaticidade implicam ΔS=0. A–D são verdadeiras nas condições; E impõe W=0 por Q=0 e é incorreta. Não há valores para Q/W/temperatura além das identidades e desigualdades do modelo; tolerância numérica não aplicável.

## AV37 — C

Hash `b741f7c26e317df09eaf7984e2065f881464ffc7367202fa2968b4ce30efe928`; bases `#base-leitura-matematica`, `#base-exergia`. Figura `assets/questoes-reais-e1/figura-222735fab01e.png` SHA-256 verificado `222735fab01e54a81e34f3bb54cfd7097a8cbc1391ebe6420d60df8b2513a9cb`: gráfico de disponibilidade contra graus da manivela, rótulos e curvas ilustram perdas, sem escala vertical de energia; números do eixo angular não entram na conta expressamente independente dos valores das curvas. Pelo enunciado, T0=300 K e Sger=0,20 kJ/K; W_perdido=T0Sger=300×0,20=60 kJ, valor publicado e diferença nominal 0. A=0,20 confunde entropia com energia; B usa indevidamente 300−273,15=26,85 °C e 26,85×0,20=5,37 (não é produto dimensional termodinâmico adequado); D troca sinal; E usa temperatura como energia. Comparação exata das operações didáticas; 300 K é temperatura ambiente absoluta e não taxa de temperatura; sem margem experimental inventada.

## AV38 — E

Hash `bde32c401ca98314f5217325508776fef07fca3eddb42b7a689a588fe973dfd4`; bases `#base-leitura-matematica`, `#base-limite-carnot`. Motor cíclico entre reservatórios a Tq=500 K e Tf=300 K: ηmax=1−300/500=0,40=40%, diferença 0 ante publicação. A=300/500=60%, B=100% viola limite com Tf>0; C=(500−300)/300=2/3≈66,7%, erro ≈0,033333 ponto percentual, menor que 0,05 p.p. para uma casa decimal ao mais próximo, empates para cima; D=(500−300)/(500+300)=25%; E=40%. Distintos. A tolerância em C é de exibição, não de medição.

## AV39 — A

Hash `42ffe7852ec1c612a414d4403674cecde23d4f79aea495c7e0feb68d7dd7cf6b`; bases `#base-segunda-lei`, `#base-balanco-fechado`. Para um ciclo, ΔE=0, Q=+1.000 kJ e W=+1.000 kJ satisfazem Q−W=0 e produziria η=1=100%; o único efeito seria retirar calor de uma única fonte e convertê-lo inteiramente em trabalho, vedado por Kelvin–Planck. A, não D; unidade igual em B, etapa adiabática em C ou lei zero em E não alteram essa conclusão. Igualdades são exatas para os números nominais; sem tolerância física derivável.

## AV40 — B

Hash `b0eea6e50cfc5d5c03befe2871587f01f350784667829c280e90723526ed7ef8`; bases `#base-leitura-matematica`, `#base-gibbs`. Substância simples compressível, ds=0 e v≈0,002 m³/kg constante: dh=Tds+vdp → Δh≈vΔp=0,002×500=+1 kPa·m³/kg=+1 kJ/kg; resultado nominal corresponde ao comentário. A usa 500/0,002=250.000, operação de dimensão incompatível; C inverte sinal; D apresenta energia total kJ em vez de entalpia específica kJ/kg, E ignora efeito da pressão. Igualdade aritmética exata nos valores fornecidos, mas a resposta continua aproximada porque v é aproximadamente constante; não há dados para quantificar erro desse modelo. As alternativas B e D possuem o mesmo número, mas unidades diferentes.

Nenhuma divergência numérica localizada. Estes registros não constituem teste com estudantes, certificação externa ou decisão global de BAN-08.
