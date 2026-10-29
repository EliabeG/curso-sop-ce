# BAN-08 — apoio científico independente CR41–CR45

Data 29/10/2026. Autora das contas e revisora: agente automatizado `/root/auditor_ban08_novo`. Análise parcial sem cegamento, sem aprovação global BAN-08 nem liberação do próximo ID. Produto e controle não alterados. Enunciados históricos e modelos do curso: `modulos/e1-termodinamica.html`, SHA-256 `80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0`; os hashes individuais são dos trechos brutos UTF-8 `<article>...</article>`. Todos os cinco são C/E pontuáveis; CR45 somente sob suplemento editorial apresentado antes da tentativa. Provas e gabaritos oficiais estão vinculados nos artigos e no inventário; não foram reconferidos integralmente nesta análise. Chaves oficiais são evidência documental, não prova termodinâmica.

Fontes de modelo acessadas em 29/10/2026: MIT OCW, 3.00, aula 20, p. 137, https://ocw.mit.edu/courses/3-00-thermodynamics-of-materials-fall-2002/8791023a80525e69c7dfe17898cadaf5_lecture_20_oneside.PDF (potencial químico por espécie); OpenStax University Physics v.2 cap. 4 equações, https://openstax.org/books/university-physics-volume-2/pages/4-key-equations (balanço, rendimento e Carnot); OpenStax §4.6, https://openstax.org/books/university-physics-volume-2/pages/4-6-entropy (entropia); BIPM SI Brochure 9ª ed., versão 3.01, 2024, p. 133, índice https://www.bipm.org/en/publications/si-brochure/ (temperatura Celsius). Os dados numéricos do enunciado são tratados nominalmente, sem inferência de incerteza de medição.

## CR41 — C

Hash `f4c503ea9b326caa519bbdd2cd70ae85279d9d03996adcfe8de703f77fd18e64`; base `#base-equilibrio-fases`. Igualdade de potencial químico em equilíbrio de fases é entre a mesma espécie transportável nas fases coexistentes: μ_i^α=μ_i^β, além do equilíbrio térmico e mecânico. Não se exige μ_i=μ_j entre espécies distintas. O comentário desambigua o singular do texto histórico; em hipótese de restrições de permeabilidade, a igualdade refere-se às transferências permitidas. Não há valores numéricos ou aproximações a comparar; tolerância não aplicável ao critério simbólico. Chave C condiz com leitura de equilíbrio descrita, sem tratar mera igualdade como todas as condições suficientes de estabilidade.

## CR42 — C

Hash `a43aea2e5d81accad6559fadfeefb77adf5e5653628f674856c501e795ce48ea`; bases `#base-leitura-matematica`, `#base-eficiencia-cop`. Com 1.000 J como trabalho líquido e 3.000 J como calor total recebido na mesma base, η=1.000/3.000=1/3=33,333333...%; a apresentação 33,3% tem erro ≈0,033333 ponto percentual, inferior a 0,05 p.p. (meia unidade da casa decimal, arredondamento ao mais próximo, empates para cima). Antes de arredondar, 1/3<0,35 com diferença 1,666667 p.p.; C. Temperatura 750 K não entra nessa conta; não é possível calcular o limite de Carnot sem temperatura fria e as condições respectivas. A exibição não é incerteza dos dados.

## CR43 — C

Hash `1a934a1bd574e1b535a5a922cb0814a17d58079a7640b3f4d4c5c493af29c17b`; base `#base-entropia`. Congelamento da água pode reduzir ΔS_água, com calor rejeitado para a vizinhança; balanço global ΔS_total=ΔS_água+ΔS_vizinhança=Sger≥0. Na mudança reversível ideal, soma 0; na irreversível, positiva. O comentário não fornece massa, temperatura, calor ou entropias para avaliação numérica; igualdade zero e desigualdade são simbólicas, tolerância numérica não aplicável. C compatível sem presumir valor de entropia do entorno.

## CR44 — E

Hash `73982b41be7659f3a23f320d7ae6414c019750db4778f91c75674c20e0d53875`; bases `#base-carnot-prova`, `#base-trabalho-fronteira`. Uma etapa adiabática tem Q_etapa=0 e não garante 100% ao ciclo. No modelo explicitado de ciclo operando apenas entre fontes finitas de 0<Tf< Tq, η≤1−Tf/Tq<1. No ciclo inteiramente adiabático de massa fechada que retorna aos mesmos estados U, EC e EP, ΔE_ciclo=0, Q_líq=0 e W_líq=0; não há razão W/Qrecebido=0/0 que represente eficiência de 100%. A conclusão E coincide com a análise sob as hipóteses declaradas. Números 100%, zero e desigualdade são relações exatas do modelo; nenhuma tolerância numérica pertinente.

## CR45 — C sob suplemento

Hash `3b7e1013014ca169f810aba4973e03c1b98a8972c5648289a996b523d63ff448`; bases `#base-leitura-matematica`, `#base-carnot-prova`, `#base-limite-carnot`. O enunciado original fornece 900 kJ recebidos de fonte a 477 °C e 90 kJ rejeitados por ciclo a 27 °C. A versão atual, antes da resposta, acrescenta editorialmente ciclo fechado, exclusivamente duas fontes indicadas, trabalho líquido como único outro intercâmbio e quantidades de calor na mesma base de ciclo. Não atribuir essas condições ao documento da banca. O hash coincide com candidata r2b examinada por `/root/auditoria_av61_70` em `BAN-07-candidata-cr45-r2b-reconciliacao-cr06-independente.md`; não confundo esse parecer com meu novo cálculo.

Tq=477+273,15=750,15 K; Tf=27+273,15=300,15 K. Na primeira lei, W=900−90=810 kJ/ciclo e η=810/900=0,90=90%, ambos iguais ao texto. Carnot: η_max=1−300,15/750,15=0,5998800239952=59,9880024%, apresentado ≈60%; diferença 0,0119976 ponto percentual <0,5 p.p. (meia unidade da casa percentual inteira; arredondamento mais próximo, empate para cima). Antes de arredondar, 90% excede limite em 30,0119976 p.p.; logo a proposição de impossibilidade é verdadeira no modelo, C.

Verificação independente de segunda lei: Qf,min=900×300,15/750,15≈360,1079784 kJ/ciclo; os 90 kJ propostos ficam 270,1079784 kJ abaixo. ΔS_total=90/300,15−900/750,15≈−0,899909973 kJ/K por ciclo, incompatível com Sger≥0; balanço de energia isoladamente continua fechado. As temperaturas e calores são nominais; não se atribui precisão experimental. A exclusividade de fontes e base temporal comum sustentam esta conclusão, sem edição do original.

Nenhuma divergência numérica localizada. Não houve teste com estudantes nem certificação externa; este apoio não decide o banco completo.
