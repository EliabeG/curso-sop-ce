# QA-09 — auditoria independente dos diagnósticos D06–D10 e D21–D25

30/10/2026. Auditor `/root/next_formulas`. **APROVADO NO RECORTE** da fotografia r27, sem aprovação global do curso. `diagnosticos-r28-2` nomeia o lote de evidência, não uma fotografia de produto r28. Li os dez enunciados, respostas e trechos pertinentes das bases de retomada; o exame científico considera também as condições expostas nessas bases.

## Identidades e reprodução

Entrega `diagnosticos-r28-2/entrega.md` SHA-256 `66bdf05a8ec3373253094065aee002b05e039de12f2af93df89c1f4ab71e851b`; manifesto `identidades.json` SHA `7e0c1603e26dde8c95a26c0866717e9b4c7f6bd44158628a356627a1e48e4f68`; verificador `verificar.py` SHA `9ce71584f4f6528ddc5ffe1c85d0f03e5271f50b22ba9cdb61ddc8a71ae6a6e8`. Fotografia `aplicacao-carnot-flashcards-r27-r1/resultado/depois-aula.html` e aula corrente no momento da verificação tinham SHA `9af8e2c9ffe509e40594d086a9ef4ad75127fb4ca873efb305d3144e08f3fc49`; inventário r27 SHA `a58d7f0b0a5f097eef83ad83026ef49e801457b87f7cf2b2345c3dd915597c7c`.

Executei `python3 auditoria/termodinamica/evidencias/QA-09/diagnosticos-r28-2/verificar.py` e comparei sua saída integral com `identidades.json` por `diff`: saída idêntica, código 0. O script extrai os dez intervalos UTF-16 da foto e confere hash, numeração e unicidade dos destinos, além de contas selecionadas. Li diretamente os fragmentos e os contextos de retomada; existência de âncora por si só não prova a correção do texto.

## Reavaliação dos modelos e contas

| Diagnóstico | Verificação |
|---|---|
| D06 | Convenção Q positivo ao entrar e W positivo ao sair: ΔU=−30−(−180)=150 kJ; U₂=650 kJ. Variações cinética e potencial desprezíveis e demais transferências excluídas. |
| D07 | Para gás ideal de massa fixa, recipiente externo rígido isolado, vácuo e sem outros trabalhos, Q=W=ΔU=0; T final de equilíbrio é igual à inicial. S aumenta por expansão para volume maior; não se supõe trajetória reversível real. |
| D08 | Inverter reação entre os mesmos estados troca o sinal de ΔH para +30 kJ; a relação entre ΔH e calor pressupõe as condições da base, inclusive trabalho de fronteira pΔV compatível e pressão constante. PCS conta a recuperação da condensação segundo a referência dos produtos. |
| D09 | η máxima = 1−300/900=2/3, Q frio mínimo = 900×300/900=300 kJ; rejeição de 100 kJ viola a segunda lei. Entropia da água pode cair se a variação da vizinhança compensar. |
| D10 | T₀Sger=280×0,15=42 kJ. Para substância simples compressível em estados de equilíbrio, composição fixa, ds=0 e v aproximadamente constante, Δh≈0,001×600=0,60 kJ/kg; 1 kPa·m³ = 1 kJ. |
| D21 | Balanço transiente com tanque inicialmente vazio dá m₂u₂=mᵢₙhᵢₙ. Para gás ideal de composição fixa com capacidades constantes e referência de entalpia/energia compatível, T₂=(cp/cv)Tᵢₙ=1,25×320=400 K; existe acumulação. |
| D22 | Integração de cp(T): 0,80×100+0,001×(400²−300²)/2 = 115 kJ/kg; cp(300)×100=110 kJ/kg. Coeficiente angular em kJ/(kg·K²); média do ponto central é exata aqui pela linearidade. |
| D23 | Vazão de saída 3 kg/s; (2×100+1×400)/3=200 kJ/kg; com entrada de calor de 30 kW, (600+30)/3=210 kJ/kg. Exige regime permanente, sem trabalho, variações cinética/potencial desprezíveis e referências de entalpia compatíveis. Estado térmico não decorre apenas de h. |
| D24 | Conservação energética dá v₂²=100²+2×1000×75=160.000 m²/s², portanto v₂=400 m/s; desprezar v₁ daria 387,30 m/s. Balanço estacionário adiabático sem trabalho ou variação de cota não exige reversibilidade. |
| D25 | No modelo de estrangulamento, h₂≈h₁; (1000−500)/(2500−500)=0,25. Para 2700 kJ/kg o resultado algébrico é 1,10, fora do domínio de título; identificar região apropriada à pressão de saída, sem truncar. |

## Fontes e limites

Abri [MIT, aplicações da primeira lei](https://web.mit.edu/16.unified/OldFiles/www/FALL/thermodynamics/notes/node17.html), cujas seções 2.3.1 e 2.3.3 tratam, respectivamente, do estrangulamento adiabático e enchimento transiente; [MIT, equação de energia em escoamento](https://ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_6.htm), que apresenta o balanço para volume de controle, e [MIT, entropia e trabalho perdido](https://web.mit.edu/16.unified/www/SPRING/thermodynamics/notes/node48.html), que desenvolve a relação com a temperatura ambiente. São apoio aos modelos nos contextos indicados, não origem dos valores didáticos. A validação dos demais enunciados apoia-se nos balanços e hipóteses explicitados acima, não na alegação de que essas três páginas sejam fontes específicas de cada fórmula.

Este parecer não testa navegador, tecnologia assistiva, aprendizagem, demais diagnósticos ou versões posteriores, nem atribui certificação externa. Não modifiquei produto, controles ou a entrega examinada.
