# QA-09 — reconciliação de cartões com teoria e resumo, r26

30/10/2026. Corretor `/root/next_theory`. Este é um exame integrado de três cartões e seus contextos de modelo na r26, não uma reivindicação de cartões ou blocos sem revisão anterior. Os cartões foram auditados na fotografia r8 e alguns corrigidos posteriormente; o resumo e glossário foram alterados na r23 e a teoria isentrópica antes disso. Suas mudanças não transferem automaticamente hipóteses aos cartões, que são visualizados individualmente. A revisão lê os sete fragmentos abaixo e não cobre todos os 21 cartões ou a aula inteira. Sem alterar produto; solicita Auditor independente.

Fotografia `aplicacao-fun02-ficha59-ex010-r26-r1/resultado/depois-aula.html` SHA `afc7ff0aba80596aa8aa7a3eeb5b9a470948c7d866c6911911b9b00fb243bac2`, inventário SHA `d73d6b239822b288329a75fc1f976419ccae7047d1bc74ba161102a529038241`; posições UTF-16.

| Fragmento | Intervalo | SHA-256 |
|---|---|---|
| Cartão COP | 1270543–1270882 | d5fb4be0c7fa1fd59c1e33f62548d6699ae5ef10bd440c5c0f2960318039cafd |
| Cartão Carnot | 1273686–1275339 | 46685d5f37428e0aceeb8c6cb82ff09dffb2aa8cbd017917198b9cddfd8bec3d |
| Cartão compressor | 1276670–1279140 | 3683542f1df835e34f1cb3d19f8891beeec1ae83574fcfb7e2aa508ffc30aaeb |
| glossario | 1288693–1291733 | 40e448e1d3c7d1294f9332b1ff780f1f5fd7566da772210c06e4e8f1c93e429c |
| resumo | 1291734–1306530 | 86b19db1acabe79adfc53f4b1226f5ff1c0b2c14d9018bd9a4b29d94a71e0809 |
| base-isentropica | 336518–343264 | f73c2ca592fb347f95152429d99bb200a0512d66867cf444b7f513c55cc8e212 |
| base-limite-carnot | 312840–319413 | 510390ee33497cd22eeb65633460eba8de1f44a28cacce03100fa83c13e93509 |

## Achados para julgamento independente

1. **Cartão de compressor isentrópico.** A razão (h2,s−h1)/(h2,real−h1) é acompanhada de adiabaticidade, regime permanente, uma entrada/saída, ΔEc/ΔEp desprezíveis e referência com mesmo estado de entrada e pressão final. O cartão a chama razão de trabalhos de entrada e não explicita que são trabalhos líquidos totais não associados ao escoamento; caso se interpretem como trabalhos de eixo, outros trabalhos não-fluxo precisam ser desprezíveis. Tampouco declara mesma substância/composição fixa e ausência de reação/mistura na comparação, condições explicitadas na base isentrópica para a relação que compara irreversibilidades. Solicita-se julgamento sobre acrescentá-las ao cartão sem alterar MathML. Não se presume que o modelo de outro bloco esteja automaticamente visível ao estudante no cartão.

   Contraste sintético: gás ideal de composição fixa cp=1 e R=0,287 kJ/(kg K), T1=300 K; referência a 330 K, saída real a 340 K, mesmas pressões inicial/final, com p2/p1=(330/300)^(1/0,287)≈1,39388. Diferenças de entalpia de referência e real são 30 e 40 kJ/kg, razão 0,75. No caso real adiabático estacionário, considere entrada de trabalho de eixo 50 e saída de trabalho elétrico 10 kJ/kg: trabalho não-fluxo líquido recebido=40, coerente com Δh=40, mas relação usando trabalho de eixo seria 30/50=0,60 se a referência usasse apenas 30 de eixo. O aumento de entropia real é ln(340/330)≈0,02985 kJ/(kg K), não negativo. O balanço ilustra o efeito de uma interação adicional; não prova a construção de um equipamento real. [MIT, desvio de comportamento ideal](https://web.mit.edu/16.unified/OldFiles/www/SPRING/thermodynamics/notes/node51.html) e [MIT, balanço de escoamento](https://ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_6.htm).

2. **Cartão de Carnot.** A expressão ηC=1−TL/TH é seguida apenas por “sempre com temperaturas absolutas”, e a legenda chama ηC limite reversível entre fontes. O resumo r23 acrescenta operação motora reversível entre dois reservatórios e TH>TL>0. Temperatura absoluta, isoladamente, não estabelece essas condições nem exclui TH=0, que tornaria a razão indefinida. Para 600 e 300 K a fórmula dá 0,5; se 300 e 300 K, resulta zero, mas não representa motor produzindo trabalho positivo entre temperaturas diferentes. Solicita-se julgar se o cartão precisa reproduzir o domínio da base e do resumo. [MIT, texto de Carnot](https://ocw.mit.edu/courses/res-2-008-thermodynamics-and-climate-change-summer-2020/mitres-2-008su22_book.pdf) relaciona limite reversível e dois reservatórios.

3. **Cartão COP.** O cartão já restringe seu modelo a ciclo por compressão acionado somente por trabalho e distingue calor útil de refrigerador e bomba de calor, resolvendo o problema anterior de extrapolação a absorção. Usa, contudo, “trabalho de entrada” sem explicitar líquido total positivo e mesma fronteira/período, condições agora qualificadas no glossário e no resumo. Em Wlíq=0 a razão é indefinida; não se afirma existência de dispositivo real que atinja esse caso. Um ciclo com entrada e saída simultâneas de trabalho exigiria distinguir bruto e líquido; solicita-se ao Auditor julgar se a forma resumida é suficientemente clara no próprio cartão. [DOE, refrigeração por absorção](https://www.energy.gov/sites/default/files/2017/06/f35/CHP-Absorption%20Chiller-compliant.pdf) ilustra que outras máquinas exigem definir o acionamento; não se está atribuindo à fonte uma convenção universal de auxiliares.

## Reprodutibilidade e limites

Execute `node auditoria/termodinamica/evidencias/QA-09/reconciliacao-flashcards-r26-next-theory-20261030/verificar.mjs`: SHA `6da339e85fb775f96d782c8209c7fa804982b545c698bb26ce3ade1fb961b3e8`, saída `ok`. O script identifica fotografia e fragmentos e verifica o contraste energético e de entropia; não prova a realizabilidade do arranjo hipotético nem decide a suficiência pedagógica. Fontes consultadas via web em 30/10/2026; não houve teste com navegador, alunos, leitor de tela ou revisão humana. QA-09 permanece aberto.
