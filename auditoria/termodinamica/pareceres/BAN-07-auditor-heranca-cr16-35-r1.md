# BAN-07 — revisão independente de herança CR16–CR35, r1

Data: 29/10/2026. Revisora: agente automatizado independente `/root/auditoria_av71_80`. **Resultado parcial: AJUSTE OBRIGATÓRIO proposto para CR26** por suficiência de hipóteses antes da tentativa, sujeito à integração pelo Auditor/coordenador. Outros 17 itens sem novo ajuste obrigatório identificado no alcance abaixo; três deles são estudos críticos sem pontuação. CR17 e CR27 foram decididos em peça anterior e não integram os 18 deste parecer. Não aprova BAN-07 global nem libera próximo ID.

## Escopo e método

Foi lido o protocolo AAA e a preparação de BAN-07; a fonte anterior de ciência e suas limitações é [BAN-07-leitura-base.json](BAN-07-leitura-base.json), SHA-256 `d71452ed79437c69f454706c7645b47b5e3b7f2a41e228f0ea37ac078a2a9913`, autoria `/root/auditor_aaa`. Ela relata leitura anterior dos CR para FON-02 e não alegou cegamento total nem aceite da entrega. Este parecer confronta enunciado, comentário, chave, limitações e, quando cabível, cinco opções ou roteiro crítico na r1; os argumentos e referências à preparação anterior são atribuídos, não se atribui sua execução a esta revisora. Não houve cegamento nesta revisão. Plausibilidade de erros é juízo teórico, sem piloto. As resoluções das questões originais são autorais e hipóteses suplementares não são atribuídas à banca.

HTML atual SHA-256 `de614a44d796ca04268915f89f502060db2772835c072036a990802eff912b80`, igual ao pacote r1. Os 18 artigos foram confrontados diretamente com a base anterior, e são idênticos aos hashes da leitura-base, sobre bytes UTF-8 do trecho `<article>…</article>`. Isso autoriza confronto da leitura mas, isoladamente, não decide suficiência. Foram lidas as bases ligadas de umidade, gás ideal, balanço fechado, trabalho e expansão livre relevantes aos pontos abaixo, disponíveis antes da resposta; não se afirma exame integral de todas as bases ou de todas as fontes originais. Critérios: comando, dados, modelo anterior à tentativa, unidades, interpretação técnica, chave documental, alternativas e suas justificativas, dentro do formato de cada item.

## Decisões individuais

**CR16 — E, sem ajuste.** À mesma T e pressão total, com a aproximação de mistura ideal apresentada antes da tentativa em `#base-umidade`, pᵥ₂/pᵥ₁=0,40/0,50=0,8. A alegação 1,25 inverte a razão. A hipótese de intensificação desprezada é expressa na base e depois na resolução; não se generaliza esta igualdade à mistura real em condições não especificadas. E julga a proposição falsa; C aceitaria a razão inversa.

**CR18 — E, sem ajuste.** n fixo e T₂/T₁=1.200/300=4 implicam p₂V₂/(p₁V₁)=4. Triplicar ambos daria 9; não é necessário determinar p₂ ou V₂ isoladamente. C aceitaria o par contraditório; E o refuta. Comentário calcula corretamente 2.700 K para fator 9.

**CR19 — C, sem ajuste.** p=3×0,082×330/85,4=0,950585… atm >0,94 atm. R em atm·L/(mol·K) é fornecido; arredondamento 0,9506 preserva a comparação. E negaria desigualdade obtida pelos dados nominais; nenhuma incerteza experimental foi fornecida.

**CR20 — E, sem ajuste.** O universal é refutado por pressão constante positiva no limite formal do gás ideal: V=nRT/p→0, não infinito. Extrapolação não prediz volume real a 0 K e mudança de fase pode ocorrer antes. C aceitaria o comportamento alegado; E distingue limite matemático e validade física, como a resolução.

**CR21 — C, sem ajuste.** p, V e T são variáveis macroscópicas de uso comum na descrição; não se afirma que sejam independentes ou que bastem sem especificar quantidade e composição. A resolução delimita pV=nRT para gás ideal de quantidade/composição fixas. E negaria a descrição comum.

**CR22 — C, sem ajuste.** Z=pV/(nRT); Z significativamente diferente de 1 evidencia desvio da relação volumétrica ideal. E negaria o desvio descrito. A recíproca não é afirmada: Z próximo de 1 não assegura idealidade de propriedades caloríficas ou ausência de interações. Comentário coerente nesse alcance.

**CR23 — E, sem ajuste.** Temperatura alta não garante aproximação ideal em presença simultânea de pressão alta; o caso convencional favorável é baixa densidade e temperatura suficientemente alta. A expressão não justifica universalmente que qualquer pressão elevada implique grande desvio: há competição entre condições reduzidas. C generalizaria a tendência do item; E rejeita garantia geral. A imagem comum não fornece dados necessários a essa afirmação.

**CR24 — estudo crítico sem nota, sem novo ajuste.** A leitura literal compara p_gás=nR(373,15 K)/V com p_água no ponto triplo; falta n/V. Só se ambos os valores forem pressões da mesma amostra gasosa a V e n constantes resulta 373,15/273,16≈1,366. Roteiro pede explicitar dado ausente e hipótese; autocorreção distingue leituras, chave oficial E e demonstração técnica condicionada, sem conferir pontuação. Não se declara razão única para o original.

**CR25 — D, sem ajuste científico.** Para n fixo, p₂/p₁=2 e V₂/V₁=1,5 dão T₂/T₁=3 em kelvin; variação é +200%, não 300%. A (−50%) ignora o efeito conjunto/inverte fatores; B supõe compensação inexistente; C usa aumento de V isoladamente; D é a única correta; E confunde valor final de 300% do inicial com aumento de 300%. Opções são distintas e comentário explica a distinção central de D/E; a análise individual dos demais distratores está explicitada neste parecer, não se afirma que exista comentário individual de A–C no produto.

**Adjudicação da justificativa em CR25.** BAN-07 exige justificar os distratores, mas não especifica um parágrafo etiquetado para cada letra. A resolução publicada determina diretamente T₂/T₁=3 e o aumento de 200%: A, B, C e E implicariam respectivamente 0,5, 1, 1,5 e 4 vezes a temperatura inicial, e todos contradizem o valor demonstrado. A resposta publicada distingue expressamente o erro particularmente provável de confundir aumento com valor final. Logo o próprio argumento oferecido ao estudante refuta as quatro opções, sem depender de consulta a este parecer; a enumeração acima explicita adicionalmente mecanismos teóricos plausíveis. Isso não equivale a feedback individualizado dos erros A–C ou à capacidade de refazer outra situação: DID-07 permanece aberto e não é aprovado aqui. Se um critério futuro exigir feedback individual para toda alternativa, a conclusão daquele ID dependerá dessa entrega, não desta refutação matemática. Não se aplica artificialmente toda a regra comum de criação de unidade curricular a este item já existente, conforme o protocolo.

**CR26 — E sob modelo restrito; AJUSTE OBRIGATÓRIO proposto.** No modelo fechado sem outras trocas, com ΔEc/ΔEp desprezíveis, Q=−400 kJ=−95,60 kcal e trabalho de agitador recebido=1.400 kcal dão ΔU≈1.304,4 kcal, abaixo de 5.500; E é coerente nesse modelo. Contudo o enunciado original diz apenas tanque e fluido como sistema e uma figura mostra conexões; não especifica operação sem entrada ou saída de massa. `#base-balanco-fechado` ensina um exemplo fechado, mas não declara que CR26 esteja fechado, nem que os termos citados esgotem suas trocas. Essas hipóteses aparecem explicitamente só depois da tentativa, na resolução. Num volume de controle em enchimento, a energia transportada pela massa é termo adicional: com entalpia líquida de entrada integrada de 5.000 kcal, sem saída nem outras parcelas, o balanço admite ΔU≈6.304,4 kcal na referência escolhida, preservando as duas transferências dadas e sendo superior ao limiar. O exemplo é contramodelo autoral, não fato da prova; uma escolha aberta ou fechada não se deduz da mera imagem. A referência [DOE Fundamentals Handbook, volume 1](https://www.energy.gov/sites/default/files/2026-04/DOE-HDBK-1012-92_VOL1.pdf), primeira lei para volume de controle, distingue termos de massa de calor e trabalho. **Ação:** preservar texto e chave oficiais; antes da tentativa, separar claramente uma hipótese editorial explícita de sistema fechado, variações macroscópicas desprezíveis e apenas as trocas indicadas, ou converter o item em estudo crítico sem pontuação que compare os modelos. Sincronizar solução, inventário e identidade quando aplicável; conferir novo alcance, histórico e a decisão em nova rodada. Não se declara a chave oficial inválida.

**CR28 — E, sem novo ajuste no modelo da base.** O gás absorve 200×4,2=840 J; o trabalho produzido informado é 350 J, e o modelo fechado com alterações macroscópicas desprezíveis é ensinado em `#base-balanco-fechado` antes da tentativa. ΔU=490 J, enquanto U₂=100+490=590 J. C confunde variação com valor final; E reconhece o erro. Interpreta-se trabalho informado como total da transformação, dentro do modelo convencional; não extrapolar a outros trabalhos adicionais ou a um sistema aberto.

**CR29 — E, sem novo ajuste.** O original tem expoentes em HTML: pressão 10³ N/m², calor perdido 10³ J. A resolução, no modelo de fronteira quase estática, usa W=1.000×(−0,1)=−100 J e Q=−1.000 J, levando ΔU=−900 J. Mais fortemente, mesmo sem usar o valor do trabalho de fronteira, um gás ideal de massa/composição fixas com p constante positiva e V menor tem T₂<T₁ e U₂<U₁ para cᵥ>0; portanto ΔU não é superior a +900 J. Esse argumento sustenta E independentemente de identificar p interna com pressão externa. O resultado numérico específico −900 requer as condições da resolução, que não são imputadas como dadas pela banca. C ignoraria a queda de temperatura/sinal; E refuta a desigualdade.

**CR30 — C, sem ajuste científico no modelo indicado.** A tabela declara A→B isotérmico e a figura fornece aumento de V; para massa fixa de gás ideal, ΔU=0. A figura B apresenta Q=ΔU+W, com Q entrando e W saindo; portanto Q=W para essa etapa. Não é um ciclo e não contraria Kelvin–Planck. C exprime a conclusão; E a negaria. A figura foi efetivamente vista: a descrição alternativa do artigo omite a isoterma A→B e a anotação Q=ΔU+W com ΔU=0; a tabela fornece isoterma, e a base instrucional fornece o balanço, mas há perda de equivalência da imagem a encaminhar a UX-04, sem decisão de aceite desse ID nem alegar teste assistivo.

**CR31 — E, sem ajuste.** Poder calorífico refere-se à energia liberada por combustão sob condições de referência, e não ao calor absorvido pelo combustível. C trocaria liberação por absorção; E é consistente. PCS/PCI diferem pelo estado da água de referência, não pelo sinal da combustão. Comentário coerente no alcance da definição.

**CR32 — C, sem ajuste.** Inverter a reação entre mesmos estados e condições reverte o sinal de ΔH; exotérmica libera e endotérmica absorve calor nas condições indicadas, como diz a resolução. E negaria a relação e as definições. A reversibilidade química não é prova de reversibilidade termodinâmica de uma realização real.

**CR33 — E, sem ajuste científico no modelo acessível.** Recipiente rígido, fechado e isolado; base prévia delimita vácuo no segundo compartimento, trabalho adicional desprezível e estados de equilíbrio. Então Q=W=0, ΔU=0 e, para gás ideal de composição fixa, T₂=T₁; a afirmação de queda é falsa. A expansão é irreversível e ΔS>0. Figura efetivamente vista: região externa à membrana está identificada como vácuo; alt do artigo apenas diz recipiente com gás e omite membrana/vácuo. A base acessível antes da tentativa descreve ambas as informações, porém a descrição da própria figura é incompleta e deve ser encaminhada a UX-04. Não houve teste de leitor de tela.

**CR34 — estudo crítico sem nota, sem novo ajuste.** A proposição original é ΔU>0, não ΔU=Q. Na massa fixa de gás ideal, mesmo volume, estados de equilíbrio, cᵥ>0 e calor exclusivamente entrando a temperaturas positivas de fronteira, ΔS>0 e ΔS=m∫(cᵥ/T)dT implicam T₂>T₁ e ΔU>0. Balanço total fornece ΔU=Q se e somente se W+ΔEc+ΔEp=0; anular cada termo é apenas suficiente. Roteiro e autocorreção ensinam a distinção; não se declara a chave C inválida por alegar trabalho arbitrário sem satisfazer segunda lei. Restrições e interpretação figuram expressamente na análise; marcação é documental e sem nota.

**CR35 — estudo crítico sem nota, sem novo ajuste.** Fechado e adiabático dão ΔU+ΔEc+ΔEp=−W, com W produzido positivo; ΔU=−W exige soma das variações macroscópicas nula. Uma elevação adiabática ideal pode armazenar energia em ΔEp sem aumentar U. Roteiro exige balanço total e condição de redução; chave C e hipótese usual são distinguidas da validade universal. Sem obrigar resposta unívoca à frase original nem pontuá-la.

## Identidade dos artigos

| ID | SHA-256 do artigo r1, igual à leitura preliminar |
|---|---|
| CR16 | `80a328824d46255663e720f5850480ab96df22ccdba54dc04db4c0e6f205ee32` |
| CR18 | `06b0dc953b5579ef19c44e8137895aaecd4e1d6245c44a6b49956cc7445fc6e1` |
| CR19 | `3871e235af09e1bdfedc606d42ae3922b3b02eea743895cd42cce446fc9a8a75` |
| CR20 | `2cb07dee73b66b77f5b0bb9b2e7cb494360a2fe28a500c14e2d3fbf709aa6a52` |
| CR21 | `5e112105b6213109cbaf04f2883ae27052a8c9027ed9d808a0fcd627a326784b` |
| CR22 | `a4cb5f18bafa792df4cdc4f632c585b8b49b63f20d7e719b36131dc44d34c944` |
| CR23 | `5be283e9eeaad31c39004231ee391654e3f476aaede45b5b81f74163628c3405` |
| CR24 | `7263887786f48bf00b02289fba4dcccfda7d655546d4c37da44e14a2d01ed438` |
| CR25 | `ad3f5a9cb6c50e2cacacb42b7e8d3a14a6c8cb13320c1048aea23cc599d50ed6` |
| CR26 | `4799e28ca9e9aa74d19aa5bac1560323e7d4d71e74a98e63561068afb3b802c8` |
| CR28 | `3d6384bcf7120175aba311755ad0ad4f36ff896a0894161de88bc45cb8614365` |
| CR29 | `f7ba62e87eedc71077825e5be83a5fd8f4dacb08ba29e658a51e99d5fe42fdac` |
| CR30 | `6abb421dab137437146a58fdaeb64d35ec7f9a6161d142f0bd29c9e91ac53f8b` |
| CR31 | `1195cc79755f79294771716075f277cae296343160770608c81367b2c7272bc3` |
| CR32 | `91cacfbdd2254fd2ad8c183e18f65d94da3156c40a211242599f800a554f73d9` |
| CR33 | `06e5d8361e1d50448ff26839517404fe07244c5ec74c1594371c11da6536997a` |
| CR34 | `ba60d9d912f78315cdfe332ad32107d522a0167da5efa18185add0caa81030c5` |
| CR35 | `62dea14902c59a5cfb2927125583531b5d1f6e5ccd43c796765d774171bfaafa` |

Imagens efetivamente vistas: CR23/33 `figura-9d164690a624.png`, SHA-256 `9d164690a6243cb31b9ea0f734b9a85ad4c6570398b9d5ef9278e4f44332bcc2`; CR26 `figura-4c355dba6054.png`, SHA-256 `4c355dba6054f57fc26e5872ffdc1b83738a52345f31b8f994c26486651c2995`; CR30 `figura-de4ee7b16ed4.png`, SHA-256 `de4ee7b16ed42d37537a23bbcf6cf7aee66cb447e11bb950b3c783e3a859aa1b`. A foto de CR26 ilustra instalação, não demonstra que há efetivamente escoamento no intervalo do item.

## Limites e decisão

As 18 análises conferem o alcance da herança científica preliminar e identificam uma insuficiência a corrigir em CR26; não se afirma que 17 itens sejam válidos para outros modelos não descritos ou que sua correção oficial tenha sido novamente conferida documentalmente. Chave oficial e fonte da banca são preservadas. Não foram executados testes de navegador ou pontuação, leitor de tela, estudantes, psicometria, certificação humana ou auditoria numérica BAN-08; não se pode concluir pela exclusão real da nota só com a leitura estática do artigo, além do mecanismo testado em BAN-10. A revisão não modifica produto, controle ou checklist e não libera o próximo ID.
