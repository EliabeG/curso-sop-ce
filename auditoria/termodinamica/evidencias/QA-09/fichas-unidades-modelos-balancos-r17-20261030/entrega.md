# QA-09 — unidades, modelos e balanços do formulário r17

Data: 30/10/2026. Corretor `/root/next_formulas`. **Aguardando Auditor independente; hipótese de denominador e fronteira da ficha 60 para julgamento.** Recorte de 11 fichas cujas constantes/fatores haviam sido examinados anteriormente sem implicar revisão integral das relações. Não altera produto nem aprova QA-09.

## Base e método

Formulário `formulas/termodinamica.html` SHA `dea4923117d09fa77cabacb0b65816cbf6d57b724d88285003804a1f1440389d`; inventário r17 SHA `b8eae39cc72cf807d7b84aad7e7a38423168b809231bc3b7f08c439d6d25163b`. As identidades por ID, intervalo UTF-16 e hash de artigo completo estão em `identidades.json` SHA `539d5def09204a105832cd2eddfa2e3e7ca759a1a0704c1d689e81d4f391416f`. Li textos, símbolos e MathML. `verificar.mjs` SHA `101f37b2fa4c0c7ade6058f955fbdf57924346c44f178cd73cd86a760880a2d7` verifica identidade, hashes e as contas a seguir, somente leitura; executado da raiz com `node auditoria/termodinamica/evidencias/QA-09/fichas-unidades-modelos-balancos-r17-20261030/verificar.mjs` retornou `ok=true`. Não interpreta automaticamente a física ou o MathML. Números a seguir são artificiais, não medições nem dados das fontes.

## Relações, domínios e testes

| Ficha | Verificação |
|---|---|
| 03 | k=1000 e W=J/s; kPa·m³=1000 Pa·m³=1000 J=1 kJ. L=10⁻³ m³; mm=10⁻³ m; cm³=10⁻⁶ m³; kPa=10³ Pa. Na convenção **termoquímica** indicada, cal=4,184 J e kcal=4,184 kJ; não generaliza outras convenções de caloria. |
| 04 | T/K=t/°C+273,15; ao subtrair estados, ΔT/K=Δt/°C. Exemplo 27 °C=300,15 K. Temperatura absoluta é exigida em razões, não basta diferença em Celsius. |
| 10 | X₁ positivo e mesma grandeza de referência: aumento=(X₂/X₁−1)100%, redução=(1−X₂/X₁)100%. X₁=80 e X₂=100 resultam +25% e −25%, respectivamente; não são dois aumentos independentes. |
| 11 | Fração volumétrica C=Cppm×10⁻⁶; 1000 ppm_v=0,001. Dez pessoas com geração por pessoa 0,02 m³/h têm G=0,2 m³/h, usando mesmas condições de referência para taxas volumétricas. `N×taxa por pessoa` exige taxa individual igual ou média apropriada e fontes adicionais somadas. Não confundir ppm em massa e em volume. |
| 12 | n=m/M e R=Ru/M; unidades de M devem coincidir com o mol de Ru. Com m=0,028 kg e M=0,028 kg/mol, n=1 mol e R≈296,929 J/(kg K) usando Ru=8,314 J/(mol K). Constantes mostradas são arredondadas; entidades do mol precisam ser especificadas no uso. |
| 19 | Gás ideal clássico, média por molécula da energia cinética **translacional** em três dimensões: 3kBT/2. Com kB=1,380649×10⁻²³ J/K e T=300 K, 6,2129205×10⁻²¹ J. Não equivale à energia interna inteira de gás molecular com modos adicionais. |
| 25 | Ar úmido aproximado ideal sem intensificação, referindo a mesma fase de saturação: φ=pv/psat(T). Se psat=3 kPa e pv=1,2 kPa, φ=0,4. A T fixa e denominador φ₁≠0, φ₂=0,6 e φ₁=0,4 dão pv₂/pv₁=1,5. Não usar aproximação como modelo exato em qualquer pressão ou saturação. |
| 30 | Para massa fixa, velocidade translacional e g constante, ΔEC=m(v₂²−v₁²)/2 e ΔEP=mg(z₂−z₁), em J. Com m=2 kg, v₁=3 e v₂=5 m/s, ΔEC=16 J; g=10 m/s² e Δz=3 m dão ΔEP=60 J. Não se trata de energia interna. |
| 42 | Volume de controle fixo, permanente, uma entrada e uma saída representativas: q−w=Δh+Δ(vel²)/2000+gΔz/1000 em kJ/kg, w exclui trabalho de escoamento. Para Δh=100 kJ/kg, v₁=100, v₂=200 m/s, g=9,81 e Δz=20 m, q−w=115,1962 kJ/kg. Vazões devem ser não nulas para dividir por massa; média deve representar os fluxos de energia. |
| 57 | Redução da 42 com regime permanente, q=w=0 e ΔEP desprezível: h₁−h₂=(vel₂²−vel₁²)/2000, sem requerer reversibilidade. v₁=50 m/s e Δh=40 kJ/kg dão v₂≈287,228 m/s; raiz é magnitude e exige argumento não negativo. Uma entrada/saída representativas e vazão não nula são inerentes à equação. |
| 60 | Para mesmo ciclo, período/fronteira, duas transferências térmicas QH e QL e **trabalho líquido recebido Win>0**, conservação dá QH=QL+Win, COPBC=QH/Win=COPR+1; 400/100=300/100+1=4. **Ponto a julgar:** o cartão declara mesmo ciclo e fronteira e ausência de outras trocas relevantes, mas não explicita Win>0 ou que Win é total líquido do ciclo; se Win=0, os quocientes não existem. Avaliar se essa condição deve constar no cartão isolado ou se o contexto da aula basta. Não confundir COPBC com a razão de energia útil por combustível de sistema que recebe calor adicional. |

## Fontes primárias e limitações

- [NIST SP 811, fatores de conversão](https://www.nist.gov/pml/special-publication-811/nist-guide-si-appendix-b-conversion-factors/nist-guide-si-appendix-b9), [temperatura e prefixos](https://www.nist.gov/pml/special-publication-811/nist-guide-si-chapter-4-two-classes-si-units-and-si-prefixes) e [definições SI](https://www.nist.gov/si-redefinition/definitions-si-base-units), fichas 03–04 e 12.
- [NIST, geração de CO₂ por ocupantes](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=920870) e [NIST, propriedades de ar úmido e fator de intensificação](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=921756), fichas 11 e 25; a primeira discute diferenças individuais, sem imputar valores fictícios à fonte.
- [MIT OCW, equipartição translacional](https://ocw.mit.edu/courses/5-60-thermodynamics-kinetics-spring-2008/a48f66f75209c904d98e034be688ebe2_BTNsoSNR5B0.pdf), ficha 19; [MIT, balanço de escoamento](https://ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_6.htm), fichas 42/57; [DOE, definição de COP](https://www.energy.gov/cmei/femp/incorporate-minimum-efficiency-requirements-heating-and-cooling-products-federal), ficha 60. Fichas 10 e 30 foram verificadas por álgebra e definições mecânicas.

Solicita-se ao Auditor distinto confrontar fórmulas, MathML, dados de teste, fontes e sobretudo o domínio da ficha 60. Não houve navegador real, leitor de tela, aluno, revisão humana ou certificação externa; este recorte não transfere aprovação a outras fichas ou versões.
