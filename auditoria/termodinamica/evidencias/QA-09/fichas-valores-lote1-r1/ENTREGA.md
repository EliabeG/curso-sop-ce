# QA-09 — recálculo localizado de valores do formulário, lote 1

Data: 30/10/2026. Autor: agente automatizado `/root/qa_fichas`. Estado: **aguardando auditoria independente**. Fotografia: `formulas/termodinamica.html` SHA-256 `c27422b409a0a755448982c4074c6d6967fd3e91d7eae20274e218530f5c37b0`. As 12 fichas abaixo são identificadas em `resultado.json` por ID estável, número, deslocamento em bytes, tamanho, hash SHA-256 do artigo HTML e conteúdo MathML extraído. A posição refere-se somente a esta fotografia; não confundir com posições UTF-16 de outros inventários QA-09.

Este lote confere valores, fatores e coeficientes indicados abaixo; **não** representa uma triagem exaustiva de todos os números, índices, condições ou fórmulas das 100 fichas. A revisão de expressão e hipóteses em FOR-01 não substitui QA-09, e este lote não encerra QA-09 nem altera o conteúdo. Não houve revisão humana, ensaio de navegador nem aplicação com alunos. Comparações aproximadas assumem arredondamento decimal usual à última casa apresentada, não incerteza de medição.

## Resultados e memória de cálculo

| Ficha | Ocorrências analisadas e verificação independente | Resultado e limites |
|---|---|---|
| 03 `formula-conversoes` | Prefixo k = 10³; 1 W = 1 J/s. 1 kPa·m³ = 10³ N/m²·m³ = 10³ N·m = 1 kJ. 1 L = 1 dm³ = 10⁻³ m³; 1 mm = 10⁻³ m; 1 cm³ = (10⁻² m)³ = 10⁻⁶ m³; 1 kPa = 10³ Pa. | Corretos por definição de unidade. |
| 03 `formula-conversoes` | Para a **caloria termoquímica**, 1 cal = 4,184 J; 1 kcal = 1000 cal = 4184 J = 4,184 kJ. | Correto para a convenção termoquímica indicada; não universaliza outros tipos de caloria. |
| 04 `formula-temperatura` | T/K = t/°C + 273,15. Subtrair dois estados cancela o deslocamento, logo ΔT/K = Δt/°C. | Correto, exato por definição; temperatura absoluta e variação não são a mesma grandeza. |
| 10 `formula-percentual` | 100% corresponde à unidade; (X₂−X₁)/X₁ × 100 = (X₂/X₁−1) × 100; redução tem o sinal oposto. | Correto para X₁ > 0 como indicado; 100 converte fração em porcentagem. |
| 11 `formula-ppm-geracao` | 1 ppm = 1/1.000.000 = 10⁻⁶ de uma fração na mesma base. | Correto para a fração volumétrica definida na ficha; não converter automaticamente ppm em massa para volume. |
| 12 `formula-mols` | CODATA 2022 dá R = 8,314462618… J/(mol·K); para um arredondamento de 0,001, 8,314 está dentro de ±0,0005. Como 1 atm·L = 101325 Pa × 10⁻³ m³ = 101,325 J, R = 0,08205736608… atm·L/(mol·K); a aproximação 0,082 está dentro de ±0,0005. | Correto nas unidades explicitadas; os dois valores têm aproximações distintas. A conversão de mol para kmol exige fator 1000 adicional. |
| 12 `formula-mols` | O SI fixa 1 mol = 6,02214076 × 10²³ entidades elementares especificadas. | Exato por definição; especificar as entidades é necessário. |
| 19 `formula-cinetica-molecular` | Na teoria cinética ideal, ⟨mv²/2⟩ = 3kBT/2. As três direções translacionais contribuem com kBT/2 cada, no domínio clássico. | Coeficiente 3/2 correto para a média **translacional** por molécula; não generalizar para toda a energia interna molecular. |
| 25 `formula-umidade` | O exemplo 50% = 50/100 = 0,50. | Correto; φ é fração adimensional. |
| 30 `formula-energia-mecanica` | A energia cinética translacional é m·vel²/2; a subtração dos estados preserva o fator 1/2. | Correto para o modelo indicado; (kg)(m/s)² = J. |
| 42 `formula-balanco-escoamento` | ΔeC = (vel₂²−vel₁²)/2 em J/kg. Divisão por 1000 converte em kJ/kg, dando denominador 2000. Para potencial, gΔz em J/kg dividido por 1000 dá kJ/kg. | Coeficientes 2000 e 1000 corretos para velocidade em m/s, g em m/s², altura em m e entalpia em kJ/kg. |
| 57 `formula-bocal-difusor` | A equação da ficha 42 sem calor, trabalho ou variação potencial dá h₁−h₂ = (vel₂²−vel₁²)/2000; isolando, vel₂² = vel₁²+2000(h₁−h₂). | 2000 correto em kJ/kg; usar 2 se h for J/kg. Raiz real exige argumento não negativo. |
| 60 `formula-cop-bomba-calor` | No mesmo ciclo e fronteira, QH = QL + Win. Dividir por Win > 0 fornece COPBC = COPR + 1. | Correto sob a hipótese declarada de ausência de outras trocas relevantes. |
| 96 `formula-radiacao` | CODATA 2022: σ = 5,670374419… × 10⁻⁸ W/(m²·K⁴); o valor 5,67 × 10⁻⁸ difere em cerca de 0,000374419 × 10⁻⁸ e está dentro de ±0,005 × 10⁻⁸. | Aproximação correta; o modelo de troca líquida na ficha requer superfície cinza pequena diante de grande entorno negro isotérmico e meio não participante. |

## Fontes utilizadas

Consulta em 30/10/2026. As páginas abaixo são referências externas para os valores e definições; nenhuma foi interpretada como prova de uso pedagógico ou aprendizagem.

- [NIST SP 811, fatores e temperatura Celsius](https://www.nist.gov/pml/special-publication-811/nist-guide-si-appendix-b-conversion-factors/nist-guide-si-appendix-b9): atmosfera, litro, caloria termoquímica e conversão K/°C.
- [NIST CODATA 2022, constante molar dos gases](https://physics.nist.gov/cgi-bin/cuu/Value?r): valor de R em SI.
- [NIST, unidade mol e constante de Avogadro](https://www.nist.gov/pml/owm/si-units-amount-substance): número exato de entidades por mol.
- [NIST CODATA 2022, constante de Stefan–Boltzmann](https://physics.nist.gov/cgi-bin/cuu/Value?sigma): valor de σ em SI.
- [OpenStax, teoria cinética e energia translacional](https://openstax.org/books/university-physics-volume-2/pages/2-2-pressure-temperature-and-rms-speed): fator 3/2 para gás ideal clássico.

## Reprodução e ressalvas

`python3 auditoria/termodinamica/evidencias/QA-09/fichas-valores-lote1-r1/verificar.py` requer `lxml`, lê somente o HTML atual e imprime JSON; não regrava evidências. Seu resultado reproduziu `resultado.json`. Ele verifica fotografia, unicidade de cada artigo, conteúdo textual das expressões MathML selecionadas, posições de alguns expoentes, frações e denominadores, e os cálculos aritméticos indicados. Texto linearizado não é representação matemática completa, nem o script é parser simbólico geral; a inspeção das estruturas MathML para as potências, frações e denominadores foi feita no HTML e deve ser reexaminada pelo Auditor. Valores citados em páginas externas foram verificados nesta sessão; script não acessa rede e não testa se as fontes mudaram.

SHA-256 `verificar.py`: `4d6fdc7e15ed1db2cbcdd899fc2f1944ad874697e22d66a5e18c9a181f8ca1f7`. SHA-256 `resultado.json`: `891b39f95223df1e8258a4e13dd9066c743b86e19f058171803a88aabb9108b3`. Solicita-se revisão independente sobre essa fotografia e estes achados; qualquer mudança no formulário exige reconciliar os artigos pelo contexto, posição e hash, sem transferir aceites automaticamente.
