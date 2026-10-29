# BAN-07 r2 — revisão independente preliminar das candidatas CR06, CR26 e CR45

Data: 29/10/2026. Revisora: `/root/auditoria_av61_70`, agente automatizado independente do Corretor. **CR06 e CR26 aprovadas como propostas isoladas; CR45 requer ajuste proposto antes de aprovação isolada.** A decisão é local, sujeita à adjudicação do Auditor principal. Não significa aplicação das propostas, aprovação da entrega r2 ou BAN-07 nem liberação do próximo ID.

## Critério, identidade e método

A adjudicação [CR06/25/26/45 r1](BAN-07-auditor-decisoes-cr06-cr25-cr26-cr45-r1.md), SHA-256 `5a4fbc9454a651239d71fc0e0eacd676afcb1536c551440401797efc8b5b68f9`, exige em CR06 linearidade das duas escalas, em CR26 sistema fechado e trocas totais delimitadas e em CR45 ciclo com duas fontes e sem outras trocas relevantes, antes da marcação; alternativamente cada um pode ser tratado como estudo crítico sem nota. Texto, figura e chave oficiais devem ser preservados. FON-02 exige distinguir e justificar suplementos em relação ao original; BAN-10 exige separar documento e interpretação e excluir da nota quando a ambiguidade impedir medida válida. Não reabro esses aceites globais.

Confrontei os três fragmentos e seus JSONs com o HTML congelado `modulos/e1-termodinamica.html`, SHA-256 `de614a44d796ca04268915f89f502060db2772835c072036a990802eff912b80`, e a adjudicação. A prova e figura CR06 e prova/chave CR45 foram previamente vistas por esta revisora, documentadas nos pareceres r1 pertinentes; a prova de CR26 e sua conferência documental são herdadas de FON-01, não afirmo nova inspeção visual nesta peça. O arquivo de texto original, figura, campos e chaves nos três artigos são idênticos a r1: inspeção própria da inserção editorial e reprodução do verificador do Corretor, após leitura do código para conferir que é somente de leitura; ao remover o parágrafo `cr-suplemento` de cada candidata, reconstrói-se exatamente o artigo r1. O parágrafo fica dentro do enunciado e antes do fieldset, marcado como hipótese editorial não integrante da prova.

| Proposta | SHA-256 HTML isolado | SHA-256 JSON | Artigo r1 SHA-256 |
|---|---|---|---|
| CR06 | `873e51481bc440721e17c233292535fdf7367670ba819c954987b7c263d8420b` | `2fa0c64fc2c34b9b144efe6a91ba52c7469c54cdb0563d3422352bfe68434206` | `69c0e38652f6be60ce26064942c5df1ef936193d8f6c3b79bd6530c28e29f31e` |
| CR26 | `7c0ed44062bd50045076b2379e2449d24ef23da635ffe8a4d751ae37fb85303f` | `e4d168b3c018caf97f4b4f57b0db4478136a2f852544653244480bb3c0951907` | `4799e28ca9e9aa74d19aa5bac1560323e7d4d71e74a98e63561068afb3b802c8` |
| CR45 | `49a25699d2703ffec80252139d7278dc806665feae3ad2bb30f33d0058286eec` | `d1848d054ccf447bdf57933855dc267696a8fd1d02a7d50f31ff12b844b81eae` | `382306e2bd0381e3614cfefd799d12a1b90a06b3b78e1f2171bc5c9c67c4ba4d` |

## CR06 — aprovada como proposta isolada

A nova hipótese, separada e anterior à resposta, faz X e Y lineares na altura h da coluna, com leituras que variam com h. Escrevendo TX=αX+βXh e TY=αY+βYh, βY≠0, elimina-se h e resulta TX=(αX−βXαY/βY)+(βX/βY)TY=a+bTY. Assim a afirmativa é correta e **C** é única marcação no modelo; E a nega. O suplemento exclui o contramodelo de escala quadrática identificado na adjudicação. Figura, enunciado e chave oficiais seguem separados e sem alteração; exemplo Celsius–Fahrenheit da resolução continua identificado como exemplo autoral, não leitura numérica da figura. Ausência de números na figura não afeta a prova geral. Sem arredondamento relevante.

## CR26 — aprovada como proposta isolada

A hipótese prévia exige sistema fechado, sem fluxo de massa, energias cinética e potencial desprezíveis, apenas as transferências indicadas e conversão explícita 1 kcal=4,184 kJ. Com calor saindo Q=−400/4,184≈−95,60 kcal e trabalho realizado pelo agitador sobre o sistema Win=1.400 kcal, ΔU=Q+Win≈1.304,40 kcal. A afirmação “superior a 5.500 kcal” é falsa; **E** é a única marcação correta e C a contradiz. A margem é muito maior que qualquer arredondamento apresentado. O suplemento remove a indefinição sobre escoamento e trocas extras e distingue a convenção adicionada do original; a explicação após a tentativa continua coerente. A figura ilustrativa não é usada para demonstrar ausência de fluxo.

## CR45 — ajuste proposto para a base de tempo das energias

O novo suplemento explicita antes da resposta máquina fechada que completa cada ciclo, dois reservatórios mantidos nas temperaturas dadas, calor somente entre eles e trabalho líquido como única outra troca energética. Isso corrige a exclusividade ausente em r1. Porém, não afirma expressamente que os **900 kJ recebidos** se referem a **cada mesmo ciclo** em que são rejeitados 90 kJ. O texto oficial diz “recebendo 900 kJ de calor de uma fonte ... rejeite 90 kJ de calor por ciclo”; a solução subtrai diretamente 900−90 e, portanto, toma ambos por ciclo. Essa leitura é comum e pode ser a pretendida; a pontuação rigorosa deve deixar explícita a mesma base, pois a frase também admite leitura dos 900 kJ ao longo de vários ciclos.

Contramodelo sob essa leitura alternativa, ainda obedecendo ao suplemento atual: um motor cíclico entre 750,15 K e 300,15 K recebe **180 kJ por ciclo**, rejeita **90 kJ por ciclo** e fornece 90 kJ de trabalho por ciclo. Em cinco ciclos recebe 900 kJ da fonte e rejeita 90 kJ em cada ciclo ao dissipador; 50% de eficiência é menor que o limite de Carnot de aproximadamente 59,988%, e a variação de entropia dos reservatórios é 90/300,15−180/750,15≈0,05990 kJ/K por ciclo, positiva. Logo o ciclo é possível. Ele não atribui à prova a intenção de descrever cinco ciclos; mostra a condição temporal que a solução precisa para concluir C de forma inequívoca.

**Ajuste concreto:** acrescentar à hipótese editorial, sem alterar o texto oficial, que os **900 kJ recebidos e os 90 kJ rejeitados são quantidades por um mesmo ciclo**; manter duas fontes, ciclo completo e demais condições. Com isso, W=810 kJ/ciclo, η=0,90 e ηCarnot≈0,59988; C é correta e E falsa. Reapresentar fragmento, JSON e hashes atualizados e recalcular a digital da candidata. Essa especificação adicional esclarece a base temporal adotada na resolução; não muda ou atribui dados à banca.

## Digitais, limites e reapresentação

A reprodução do `verificar-CR06-26-45-candidatas.mjs` do Corretor, SHA-256 `5cfcbe14a24a7c1f18a046a32f616776e72ac87f820100ce3bc2ebe57ad7b6ed`, foi executada após inspeção de que não grava arquivos. As digitais de conteúdo mudam respectivamente `01aa3697→d63393e4`, `988714ce→1c9fcf05` e `c084d78c→107f0566`. Não há colisões entre essas três ou com as 80 digitais CR atuais, segundo aquele verificador; não foram examinadas todas as digitais de históricos desconhecidos. Para uma nova versão de CR45, a digital acima deixa de descrever a candidata final. O verificador também conferiu os cinco hashes do produto congelado r1.

| Critério | Resultado |
|---|---|
| Texto oficial, imagem, chave e distinção editorial | Atendido nos três fragmentos; os suplementos são identificados antes da escolha e removê-los reproduz o artigo r1. |
| Suficiência para chave única | CR06 e CR26 atendem; CR45 ainda precisa delimitar por ciclo ambas as quantidades energéticas, conforme contramodelo. |
| Separação FON-02/BAN-10 | Estrutural e textual na proposta isolada; inventário e rastreio de suplementos deverão ser atualizados no produto futuro, sem apresentar hipóteses como originais. |
| Identidade e regressão | Digitais isoladas calculadas e colisões atuais verificadas; não se verificou histórico real, comportamento de placar, aviso, persistência, recarga ou navegador. |
| Ciência e opções | Julgamentos C/E demonstrados nos modelos indicados; sem arredondamento capaz de inverter respostas. Nenhum teste com estudantes ou certificação externa. |

**Decisão:** CR06 e CR26 aprovadas apenas como candidatas isoladas; CR45 **AJUSTES OBRIGATÓRIOS propostos** para tornar comum a base por ciclo. Uma reapresentação aplicada exige atualização de inventário e rastreabilidade, hashes, nova verificação de digitais/colisões, manutenção de tentativas antigas sem migração, teste proporcional de placar/aviso/recarga e análise integral do Auditor. Não se aplica esta decisão automaticamente a outras propostas ou IDs; produto, controle e checklist permanecem sem alteração por esta revisão.
