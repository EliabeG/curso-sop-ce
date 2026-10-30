# QA-09 — teoria de processos, segunda lei e ciclos, lote r9

Data: 30/10/2026. Corretor automatizado `/root/next_theory`. Estado: **aguardando auditor independente**. Este lote não aprova QA-09, não revalida automaticamente parecer anterior e não permite iniciar outro ID. Não houve alteração da aula, dos inventários ou evidências históricas.

## Versão e escopo

Aula `modulos/e1-termodinamica.html`: SHA-256 `2d6b8fb2f9c99e04d22c19d7b32bbc3eb20577459d9132e506f9c0acef3f2fc2`. Fotografia `inventario-r9.json`: SHA-256 `023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d`. Esta revisão cobre dez campos `texto_direto` fora dos artigos BAN-08 e das caixas de exemplos: três sobre expansão livre, três sobre a segunda lei, dois sobre Brayton e dois sobre aquecedor aberto. Lemos as fórmulas e as hipóteses vizinhas para julgar cada texto; **isso não aprova automaticamente** essas fórmulas, outros nós, atividades, figuras ou a seção toda.

Cada posição é um deslocamento UTF-16 na fotografia. O SHA do campo é do texto bruto direto do nó, conforme a regra r9, e não necessariamente o hash de todo o elemento HTML. `verificar.mjs` (SHA-256 `8b114d2b364ace54a1f51bea45758cc565ad4f78a8942d52940a2dff3deff1a0`) relê a fonte e inventário, valida seus hashes, seções/posição/tag e o hash reconstituído de cada campo. Os testes numéricos ilustrativos não substituem inspeção científica. Execute, na raiz: `node auditoria/termodinamica/evidencias/QA-09/teoria-processos-ciclos-r9-20261030/verificar.mjs`. Foi executado com `ok: true` e não grava saída em arquivos.

## Conferência e hipóteses

| Posição · seção | Conteúdo e raciocínio | Resultado |
|---|---|---|
| 201257 · energia | O recipiente externo inteiro é rígido, isolado e fechado, com um lado em vácuo; Q=0 e W=0 no modelo, incluindo nenhum outro trabalho, com ΔEc e ΔEp desprezíveis. Portanto ΔU=0 para o sistema escolhido. | Compatível com a primeira lei; o limite do sistema e exclusão de outros trabalhos são essenciais. |
| 201657 · energia | Para gás ideal de composição e massa fixas, U depende de T; ΔU=0 dá T₂=T₁. A fórmula de estado `ΔS=mR ln(V₂/V₁)` segue da diferença entre estados de equilíbrio a temperaturas iguais, ainda que o processo real não seja reversível. Se V₂>V₁, m,R>0, ΔS>0. | Compatível: adiabaticidade não implica processo isentrópico; não interpreta a trajetória irreversível como quase estática. |
| 202564 · energia | Expansão livre do exemplo isolado tem Q=W=0. Para expansão isotérmica reversível de gás ideal com somente trabalho de fronteira, ΔU=0 e Q=W=mRT ln(V₂/V₁)>0 para V₂>V₁. | O contraste é correto nas hipóteses citadas; expansão volumétrica isoladamente não determina trabalho. |
| 338943 · segunda-lei | Em ciclo fechado, ΔU=0; se inteiramente adiabático, Qlíq=0. Para variações líquidas de Ec/Ep nulas, Wlíq=0. Não é rendimento 100%: `W/QH` tem QH=0 e é indefinido. | Compatível com primeira lei; refere-se ao ciclo completo, não a cada etapa. |
| 339353 · segunda-lei | Máquina cíclica entre duas fontes fixas com TH>TL>0 e QH>0: ΔSsistema=0 e Sger=QL/TL−QH/TH≥0. Da primeira lei W=QH−QL, segue η≤1−TL/TH. | Compatível para magnitudes positivas, sem outras interações energéticas/entrópicas além das consideradas. O exemplo anterior com 800/400 K e QH=600 kJ dá limite 0,5; QL=120 kJ daria η=0,8 e Sger=−0,45 kJ/K, inviável. |
| 343719 · segunda-lei | Para substância simples compressível com composição fixa e estados de equilíbrio, `dh=T ds+v dp`. Ao longo de uma sucessão isentrópica, ds=0 e Δh=∫v dp. Como v>0, aumento de p eleva h; para v aproximadamente constante Δh≈vΔp. | Compatível com a identidade de Gibbs e a unidade `kPa·m³/kg=kJ/kg`. Não transfere a identidade para trabalho de eixo sem balanço e hipóteses do equipamento. |
| 378541 · ciclos | Brayton ar-padrão ideal: compressão e expansão isentrópicas, entrada e rejeição de calor isobáricas; o fechamento ideal não torna estacionário um ciclo material de turbina a gás aberta real. | Sequência consistente no modelo; equipamento real exige perdas e troca de massa/energia. |
| 379246 · ciclos | Com k constante >1, a=(k−1)/k>0 e η=1−rₚ^(−a); `dη/drₚ=a rₚ^(−a−1)>0` para rₚ>1. A condição de máquina motora viável e limites térmicos devem ser mantidos. | Relação ideal correta em seu domínio. Teste artificial k=1,4: η(4)=0,32705 e η(8)=0,44796; é teste algébrico, não dado de instalação. |
| 382630 · ciclos | Para aquecedor aberto estacionário e adiabático, sem trabalho, com ΔEc/ΔEp desprezíveis e mesma referência de entalpia, uma unidade de massa principal se divide em y e 1−y; conservação dá `hₛ=y hₑ+(1−y)hₐ`. | Balanços consistentes no modelo de mistura, sem provar que qualquer conjunto arbitrário de entalpias é fisicamente realizável. |
| 384203 · ciclos | Isolando y, `y=(hₛ−hₐ)/(hₑ−hₐ)` com denominador não zero e y∈[0,1]. No dado didático vizinho (210, 2700, 500 kJ/kg), y=290/2490=0,11646586…; 11,65% é aproximação. | Identidade coerente com as hipóteses locais. Usar a fração arredondada 0,1165 não produz identidade exata: resulta em 500,085 kJ/kg. Os estados devem ser compatíveis com a pressão de mistura. |

Os testes usam igualdade exata para identidades algébricas; para valores aproximados, os números foram mantidos com precisão de guarda e o arredondamento indicado. Nenhuma precisão experimental foi fornecida. Nos exemplos acima, 800/400 K e entalpias são dados didáticos do próprio curso, não valores medidos nem atribuídos às fontes externas; o par de testes de Brayton é artificial.

## Identidades r9

| Posição UTF-16 | SHA-256 do campo |
|---:|---|
| 201257 | `c8826f1bd795aeec2bc232c6a2d7c34218c0c19c0abf59657cd774a7004e925c` |
| 201657 | `6dd784df30e50bdee84bae2d2cf202ffed7b763bb0317d5ef0ac84b4cfc6cb92` |
| 202564 | `14a9dba805ed9827873941e78874f7897605b750186f62368436fbf969b04fad` |
| 338943 | `af74b75157cecec1f2a7d2c1e29f7d327014c8ca4e0e063060e2aab91b79a7e0` |
| 339353 | `487b9cb7811cfa88a44fc3df77c2a0afabfdd6c65d3e420bf3ec8fcc09db6899` |
| 343719 | `017eb3e34d4468bac4f376ac3b6144fdee1f2e3dcff65ab3bf4a82931207b843` |
| 378541 | `94024dbdfe9dee78f0b30be179ff89ca39d59ba3404d8b735c957775349fac43` |
| 379246 | `48b416c28b719ab4e748fd6a93210c21e3610994287d6015424614c4b3208745` |
| 382630 | `168d4cc2b01849fb5badbbfbd9c533a3305984d3cc6ccfd5a7acaefc61718083` |
| 384203 | `5c81aff16a9b1a15df09f3f4ead6a60caab12ff0b4c9086b9a5181308ebe0382` |

## Referências e limites

Para confronto dos modelos: [MIT, expansão livre e isotérmica](https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node33.html), [MIT, entropia do gás ideal](https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node40.html), [MIT, equações de Gibbs](https://web.mit.edu/course/16/16.unified/www/SPRING/thermodynamics/notes/node38.html), [DOE, princípio de Carnot e duas fontes](https://www.energy.gov/sites/default/files/2026-04/DOE-HDBK-1012-92_VOL1.pdf), [NASA, sequência ideal de Brayton](https://www.grc.nasa.gov/www/k-12/airplane/brayton.html), [MIT, rendimento Brayton ideal, seção A.3 e equação A.3.3](https://ocw.mit.edu/courses/16-050-thermal-energy-fall-2002/7ad40d4087bf332cf6da225f14cfd565_03_part1a_to_CMS.pdf) e [MIT, regeneração Rankine](https://ocw.mit.edu/courses/2-611-marine-power-and-propulsion-fall-2006/resources/11rankine_regen/). Consultas em 30/10/2026; estas fontes sustentam modelos, não são origem dos números artificiais ou didáticos.

Não identifiquei erro nos dez trechos dentro das hipóteses descritas; cabe ao Auditor independente examinar diretamente a versão efetiva e as fontes e registrar eventual ajuste. Não houve ensaio de navegador, aplicação com estudantes, revisão humana ou certificação externa. Os outros registros de QA-09 continuam pendentes, inclusive a triagem de referências e recursos e a integração das revisões históricas.
