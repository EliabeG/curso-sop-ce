# BAN-08 — apoio científico independente CR26–CR30

Data 29/10/2026; autora dos cálculos e revisora: agente automatizado `/root/auditor_ban08_novo`. Leitura sem cegamento; exame parcial sem aprovação global de BAN-08 nem liberação do próximo ID. Produto e controle não alterados. Fonte dos enunciados históricos, das hipóteses editoriais e comentários: `modulos/e1-termodinamica.html`, SHA-256 `80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0`; hashes abaixo correspondem ao trecho bruto UTF-8 `<article>...</article>`. Todos C/E, pontuáveis, inclusive CR26 sob suplemento antes da resposta. Os links a provas e gabaritos oficiais constam dos artigos e do inventário; não foram reexaminados integralmente nesta peça e não se atribuem à banca os suplementos. As chaves são evidência documental, não prova física.

Fontes: NIST SP 811, nota 9, https://www.nist.gov/pml/special-publication-811/nist-guide-si-footnotes, caloria termoquímica exatamente 4,184 J; OpenStax Physics §12.2, https://openstax.org/books/physics/pages/12-2-first-law-of-thermodynamics-thermal-energy-and-work, ΔU=Q−W e pressão-volume; OpenStax University Physics v.2 §3.3, https://openstax.org/books/university-physics-volume-2/pages/3-3-first-law-of-thermodynamics, energia interna e modelo de gás ideal. Acesso 29/10/2026. Os dados originais prevalecem sobre valores externos; operações nominais exatas não são alegações de precisão metrológica.

## CR26 — E, sob suplemento editorial

Hash `7c0ed44062bd50045076b2379e2449d24ef23da635ffe8a4d751ae37fb85303f`; bases `#base-leitura-matematica`, `#base-balanco-fechado`; figura `assets/questoes-reais-e1/figura-4c355dba6054.png` SHA-256 verificado `4c355dba6054f57fc26e5872ffdc1b83738a52345f31b8f994c26486651c2995`, foto de tanque e agitador sem valores quantitativos. Original: calor sai 400 kJ e misturador realiza 1.400 kcal; pede se ΔU>5.500 kcal. O curso acrescenta previamente sistema fechado, ΔEC≈ΔEP≈0, sem outras transferências e 1 kcal termoquímica=4,184 kJ; isso não é dado original.

Com Q>0 entrando e W>0 saindo, W=−1.400 kcal, Q=−400/4,184=−95,6022944551 kcal; ΔU=Q−W=+1.304,3977055449 kcal. Por rota em kJ: W=−5.857,6 kJ e ΔU=−400+5.857,6=+5.457,6 kJ; divisão por 4,184 confirma o resultado. Valores publicados −95,6 e 1.304,4 diferem do cálculo não arredondado em cerca de 0,0022945 kcal, menores que 0,05 kcal, meia unidade da casa decimal para arredondamento ao mais próximo, empate para cima. A distância ao limiar é 5.500−1.304,3977055=4.195,6022945 kcal; a desigualdade estrita proposta é falsa com ampla separação sob o modelo. Não se infere erro de medição dos dígitos impressos.

## CR27 — C no modelo declarado

Hash `1ff53155f6fc4ea80c3b4b9d15de2e28342db294570f3e745f659a18456164c0`; bases `#base-primeira-lei`, `#base-gas-energia`. Para massa fixa de gás ideal de composição fixa, ΔEC e ΔEP desprezíveis, trabalho líquido de compressão recebido é positivo em magnitude, Q=0 e ΔU=−W_sistema>0; como dU=n c_v(T)dT e c_v>0, T sobe. A relação e o zero são qualitativos exatos sob o modelo da resolução; nenhum trabalho, massa ou calor específico é fornecido para calcular ΔT; tolerância numérica não aplicável. O preâmbulo da prova estabelece 1 cal=4,2 J, mas este item não necessita de conversão. A hipótese de gás ideal e trabalho líquido deve ser mantida para não generalizar a qualquer fluido/processo.

## CR28 — E

Hash `3d6384bcf7120175aba311755ad0ad4f36ff896a0894161de88bc45cb8614365`; bases `#base-leitura-matematica`, `#base-balanco-fechado`, `#base-primeira-lei`. Usar dado original 1 cal=4,2 J: Q=+200×4,2=+840 J; W=+350 J, ΔU=840−350=490 J; Ui=100 J, Uf=100+490=590 J. As grandezas publicadas coincidem, diferenças zero. A proposição fornece 490 J como valor final, mas isso é a variação: E. Critério de igualdade aritmética nominal exata para dados e suposições editoriais de sistema fechado, outras transferências e variações macroscópicas desprezíveis. Não substituir 4,2 por 4,184, pois a prova fornece a convenção para este item.

## CR29 — E

Hash `f7ba62e87eedc71077825e5be83a5fd8f4dacb08ba29e658a51e99d5fe42fdac`; bases `#base-leitura-matematica`, `#base-trabalho-fronteira`, `#base-balanco-fechado`. O HTML usa sobrescritos no texto original: pressão 10³ N/m² e perda de calor 10³ J, não 103. Pressão de fronteira 1.000 Pa, ΔV=−0,1 m³, hipótese editorial de compressão quase estática e somente trabalho de fronteira: W=pΔV=−100 J; Q=−1.000 J; ΔU=Q−W=−1.000−(−100)=−900 J. Todos os valores do comentário coincidem nominalmente; −900 não é superior a +900 J, diferença de 1.800 J; E. Igualdade aritmética exata e comparação estrita sob hipóteses indicadas; sem medida de precisão adicional.

## CR30 — C

Hash `6abb421dab137437146a58fdaeb64d35ec7f9a6161d142f0bd29c9e91ac53f8b`; bases `#base-leitura-matematica`, `#base-trabalho-fronteira`, `#base-gas-energia`, `#base-balanco-fechado`. Figura `assets/questoes-reais-e1/figura-de4ee7b16ed4.png`, SHA-256 verificado `de4ee7b16ed42d37537a23bbcf6cf7aee66cb447e11bb950b3c783e3a859aa1b`: esquema identifica T1<T2<T3<T4<T5 e A→B na mesma isoterma com aumento de volume; nenhuma escala numérica a usar. A tabela do artigo qualifica A→B isotérmico, A→C adiabático e TA>TC, A→D isocórico e TA>TD, A→E isobárico e TA<TE, coerentes com esquema qualitativo.

Para gás ideal de massa/composição fixas, U=U(T), TA=TB implica ΔU=0 exatamente. Com ΔEC e ΔEP desprezíveis, Q=W para a transição, que expande; a afirmação é C sob modelo. O zero é igualdade simbólica e não dado medido; sem valores de calor e trabalho, tolerância numérica não aplicável. Trata-se de uma etapa, sem concluir que uma máquina cíclica converta todo o calor em trabalho.

Nenhuma divergência numérica localizada sob as hipóteses registradas. Nenhuma aplicação com estudantes, certificação externa ou aprovação global foi realizada.
