# QA-09 — apoio independente aos diagnósticos 21–24, r1

Data: 29/10/2026. Parecer automatizado independente, sem editar produto ou controle e sem aprovação global. Versão `modulos/e1-termodinamica.html` SHA-256 `7541e7c4c8314922992e99e8b62b40342c2d938e6edeac67ef9f74b69f86c17c`; inventário `auditoria/termodinamica/evidencias/QA-09/inventario-r4.json` SHA-256 `44d19642bcf39109edf620e7304580b7a8a686e7c42cfa7101fa3d118a79d054`. Hashes de cada ocorrência são dos fragmentos HTML UTF-8 sem linha extra. Fonte externa consultada em 29/10/2026, sem captura ou hash local.

## 21 — Enchimento adiabático

Fragmento `08717431d6f258728f63490380fcf96a6de7363191a2c874c2c7b595ef7475f6`. Tanque inicialmente evacuado, uma entrada a 320 K, rígido e adiabático, sem saída ou trabalho, parede e energias cinética/potencial desprezíveis: massa final = massa admitida e `U₂=m_in h_in`, portanto `u₂=h_in`. Para mesmo gás ideal de composição fixa, `cp/cv=1,25` constante e propriedades/temperatura de entrada constantes, a base `#base-balanco-transiente` fornece `T₂=(cp/cv)T_in=1,25×320=400 K`. A razão constante do mesmo gás ideal de R constante implica cp e cv constantes, dentro do modelo; referência de u/h compatível. Há acumulação durante o enchimento e, portanto, não é regime permanente. Número exato sob dados nominais; não há tolerância experimental informada. Fonte: [DOE, fundamentos e balanços de energia](https://www.energy.gov/sites/default/files/2026-04/DOE-HDBK-1012-92_VOL1.pdf), além do balanço explicitado na base. Resultado conforme no modelo ensinado.

## 22 — Calor específico variável

Fragmento `3e5156b9614be86d149d3154889aada0abc3f9f2d7e20c597b09b781e02ea88e`. Gás ideal de composição fixa: `Δh=∫₃₀₀⁴⁰⁰(0,80+0,001T)dT = 80+0,0005(160000−90000)=115 kJ/kg`. Usar somente `cp(300)=1,10 kJ/(kg·K)` dá `110 kJ/kg`, erro de 5 kJ/kg, ou cerca de 4,35% do resultado correto; não conta a dependência em T. Sem arredondamento adicional para os dados declarados e sem tolerância instrumental; a base `#base-calor-variavel` estabelece a integral. Fonte: [NIST, entalpia de gás e calor específico](https://wtt-pro.nist.gov/wtt-pro/help/properties/enthalpy_gas.html). Resultado conforme.

## 23 — Misturador com calor recebido

Fragmento `e5e87b30397cc0394b10b1194461e7bf64fd0e831184d4b91eeae0d234cd5073`. Em regime permanente, duas entradas e uma saída, sem trabalho e alterações cinética/potencial: massa de saída `2+1=3 kg/s`, energia de entrada `2×100+1×400=600 kW`. Para Q̇=0, `h₃=600/3=200 kJ/kg`; com Q̇ líquido recebido de 30 kW, `h₃=(600+30)/3=210 kJ/kg`. Entalpias devem usar referência compatível, como ensina `#base-misturador-correntes`. Conservação não é média simples de temperaturas. Iguais exatamente para valores nominais, sem tolerância de medida informada. Fonte: [DOE, balanço de energia em escoamento](https://www.energy.gov/sites/default/files/2026-04/DOE-HDBK-1012-92_VOL1.pdf). Resultado conforme para a leitura de calor líquido informado.

## 24 — Bocal e velocidade de entrada

Fragmento `a86feea2983a3c008e11db251a908fce3402af0f7b5cc0d3a33a5aaee3033fbf`. Bocal estacionário adiabático, sem trabalho e mudança de altura: `v₂²=v₁²+2000(h₁−h₂)=10000+150000=160000 (m/s)²`, então `v₂=400 m/s`. É balanço de energia e não exige reversibilidade; entalpia em kJ/kg justifica fator 2000. Desprezar indevidamente v₁ daria `√150000=387,2983346… m/s`, que arredonda a `387,30 m/s` com erro <0,005 m/s, metade da unidade da última casa. O valor de 400 m/s é exato para os dados. A base `#base-bocal-difusor` ensina o modelo. Fonte: [DOE, balanço em escoamento](https://www.energy.gov/sites/default/files/2026-04/DOE-HDBK-1012-92_VOL1.pdf). Resultado conforme.

Esta revisão não cobre as demais ocorrências nem constitui aprovação QA-09.
