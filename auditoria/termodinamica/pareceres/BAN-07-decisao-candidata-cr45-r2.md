# BAN-07 — decisão preliminar da candidata isolada CR45 r2

Data: 29/10/2026. Revisor: agente automatizado `/root/auditoria_av71_80`. **Ajuste confirmado antes de aceitar esta candidata isolada:** explicitar que 900 kJ recebidos e 90 kJ rejeitados são quantidades de um mesmo ciclo. Isso não constitui aplicação, aprovação da r2, aceite global BAN-07 ou liberação do próximo ID.

## Objeto e identidade

Examinei o texto oficial reproduzido, o novo suplemento anterior ao campo de resposta e o comentário da candidata [CR45-candidata.html](../evidencias/BAN-07/propostas-r2/CR45-candidata.html), SHA-256 `49a25699d2703ffec80252139d7278dc806665feae3ad2bb30f33d0058286eec`, e o registro JSON da candidata, SHA-256 `d1848d054ccf447bdf57933855dc267696a8fd1d02a7d50f31ff12b844b81eae`. A r1 segue `de614a44d796ca04268915f89f502060db2772835c072036a990802eff912b80`. Li o [parecer independente de candidatas](BAN-07-candidatas-cr06-cr26-cr45-r2-independente.md), SHA-256 `1113b02ee2174f144b3720dcf3ae69d2e6e4f393e116c6727c6fb96287e2ca0d`, de `/root/auditoria_av61_70`; sua análise e reprodução de verificador pertencem àquela revisora, e não foram reexecutadas por mim. Esta decisão trata apenas da base por ciclo de CR45, sem examinar ou aprovar as outras candidatas.

## Adjudicação

O novo suplemento estabelece corretamente máquina cíclica, dois reservatórios, somente duas trocas de calor e trabalho líquido como única outra troca, corrigindo a objeção da r1 sobre a terceira fonte. O original diz que a máquina recebe 900 kJ da fonte e rejeita 90 kJ **por ciclo**, mas não explicita que o calor recebido de 900 kJ é por esse mesmo ciclo. Pode ser lido convencionalmente dessa forma; a frase não afasta com clareza a leitura dos 900 kJ acumulados ao longo de vários ciclos. O suplemento atual tampouco fixa essa base. O cálculo publicado W=900−90 e a comparação dos rendimentos exigem que as duas quantidades se refiram ao mesmo ciclo.

Como demonstrado pelo apoio, um motor entre 750,15 K e 300,15 K que receba 180 kJ e rejeite 90 kJ em cada ciclo produz 90 kJ de trabalho, com eficiência de 50%, inferior ao máximo de Carnot ≈59,99%. Em cinco ciclos recebe 900 kJ no total e rejeita 90 kJ por ciclo ao dissipador. A variação de entropia dos reservatórios é 90/300,15−180/750,15≈0,0599 kJ/K por ciclo, positiva. O caso é fisicamente admissível na leitura alternativa, sem terceira fonte ou alteração dos dados atribuídos à banca. Não se afirma que a banca pretendesse cinco ciclos; o exemplo mostra por que a base temporal da condição editorial deve ser inequívoca.

**Reapresentação necessária:** acrescentar ao suplemento editorial separado do texto oficial que os 900 kJ recebidos e os 90 kJ rejeitados correspondem ao mesmo ciclo, mantendo as duas fontes, a condição cíclica e trabalho líquido como única outra troca. Conferir que C é única no modelo: W=810 kJ/ciclo e η=90% > ηCarnot≈59,99%; E nega essa impossibilidade condicionada. Preservar original e chave documental, sincronizar os metadados, recomputar hash e digital e verificar colisões e histórico na integração r2. A nova redação, quando existir, requer nova revisão; nenhuma sugestão textual é automaticamente aprovada.

Nenhum produto, controle ou checklist foi modificado. Não executei testes de navegador, armazenamento, aprendizagem ou certificação externa. O produto r1 permanece congelado.
