# BAN-08 — apoio científico independente FUN02 calor de caminho

Data 29/10/2026. Revisora e autora dos cálculos: agente automatizado `/root/auditor_ban08_novo`. Apoio parcial sem cegamento, sem aprovação global de BAN-08 ou liberação de próximo ID; produto/controle preservados. Artigo bruto `fun02-e1-calor-caminho` SHA-256 `936a8ba00043cc49ad22d047338a78ae65b9c9e531dba634a5d943cfbd194a6c`; HTML `modulos/e1-termodinamica.html` SHA-256 `80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0`; dados `assets/termodinamica/fun02-dados-v1.json` v1.0 SHA-256 `511aac986e9122e5498cdf69609274685791000a19f140a09d539fca01676319`. Problema aberto com rubrica; recálculo feito diretamente das equações sem executar o script de produto. Dados e modelo de gás ideal são didáticos; cálculos nominais não são incertezas de equipamento.

Fontes de princípio, especificadas no pacote: MIT Unified §2.1 https://web.mit.edu/16.unified/www/SPRING/thermodynamics/notes/node14.html (primeira lei); OpenStax University Physics 2 §4.6 https://openstax.org/books/university-physics-volume-2/pages/4-6-entropy (entropia e integração reversível); Purdue ME200 Spring 2023 cap. 6 p. 2 https://www.purdue.edu/freeform/me200/wp-content/uploads/sites/29/2023/03/ME-200-Chapter-6.pdf (temperatura da fronteira e reversibilidade interna).

## Trajetória e balanço

Com n=1 mol, R=8,314 J/(mol K), cv,m=3R/2=12,471 J/(mol K), pV^(3/2)=K, e pV=nRT, obtém-se T√V=T1√V1; T(V)=300√(0,0200/V), T2=300√4=600 K. p1=8,314×300/0,0200=124710 Pa, p2=8,314×600/0,005=997680 Pa. Na trajetória K,n fixos, dT/dV=−T/(2V) e dV/dT=−2V/T; isto não é uma parcial de U a V fixo.

W=∫V1^V2 K V^(−3/2)dV=−2nR(T2−T1)=−4988,4 J, ΔU=n cv,mΔT=3741,3 J, Q=ΔU+W=−1247,1 J. Sinais significam 4988,4 J de trabalho recebidos e 1247,1 J rejeitados por calor; resíduo ΔU−Q+W=0. Comprimir pode aumentar T mesmo com calor saindo porque energia de trabalho supera a perda térmica. Números publicados são idênticos aos nominais, sem arredondamento relevante. Impor Q=0 sem alterar W e estados daria resíduo 3741,3−0−4988,4=−1247,1 J, violando primeira lei.

## Capacidades e integrabilidade

δQrev=n cv,m dT+nRT dV/V. Ao longo da restrição, δQ/dT=n(cv,m−2R)=−nR/2=−4,157 J/K. É constante nesta trajetória; por isso Q/ΔT=−1247,1/300=−4,157 J/K. Não se trata de CV: CV=n cv,m=12,471 J/K e Cp=n(cv,m+R)=20,785 J/K; cv,m=12,471 e cp,m=20,785 J/(mol K), valores iguais apenas numericamente porque n=1 mol. Capacidades de propriedade positivas não contradizem capacidade de caminho negativa.

Em (T,V) positivos, os coeficientes de δQrev têm derivadas cruzadas 0 e nR/V, logo δQrev não é diferencial exata. Para δQrev/T, coeficientes ncv,m/T e nR/V têm cruzadas zero em domínio aberto simplesmente conexo; a primitiva explícita é S=ncv,m ln T+nR ln V+constante para o modelo. Assim ΔS=ncv,m ln(600/300)+nR ln(0,005/0,020)=−(nR/2)ln2=−2,881412829588 J/K, coincidindo com a integral −(nR/2)∫300^600 dT/T ao longo do caminho; valor impresso −2,881412830 difere ≈0,000000000412 J/K (<0,5×10⁻⁹). Q/T1=−1247,1/300=−4,157 J/K, diferente de ΔS porque T varia no percurso, não se retira 1/T da integral.

## Irreversibilidades e rubrica

A transferência para reservatório mais frio com diferença finita de temperatura pode ser irreversível externamente sem impedir que o gás seja internamente reversível; com gás uniforme e somente trabalho p dV, Tgás dS=dU+p dV e primeira lei permitem δQreal/Tgás=dS. Para Q entrando no gás negativo, a contribuição conjunta δQ(1/Tgás−1/Treservatório)>0 quando Treservatório<Tgás. Não substituir a temperatura interna pela do reservatório; caso haja geração interna, exigir modelo e temperatura da fronteira e incluir dSger no balanço. Mantidos mesmos estados, ΔU e ΔS continuam fixos; mantidos adicionalmente p(V) e modos de trabalho, também W e Q. Não confundir irreversibilidade externa com prova automática de igualdade falsa para o gás.

A relação adiabática reversível de gás ideal com cv,m constante tem expoente γ=cp,m/cv,m=5/3, não o valor 3/2 do enunciado. Expoente constante por si não implica Q=0. Rubrica soma 2+2,5+2+2+1,5=10 pontos e sugere 0,1% nos resultados não nulos preservando sinal e base; isso é critério pedagógico, não tolerância de medição. Nenhuma divergência localizada. Não houve aplicação com estudantes ou certificação externa.
