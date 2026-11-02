# QA-09 — candidatas isoladas: primeira lei e entropia em escoamento, r17

Data: 30/10/2026. Corretor `/root/next_graphics`, distinto do Auditor da ressalva `/root/reference_triage`. **Não aplicadas; aguardam Auditor independente.** Atendem às duas ressalvas do parecer `QA-09-primeira-lei-entropia-r17-auditoria-independente-20261030.md`, SHA `d7c62e53b22e4a59374e64705e2dd25701b204319384c47e972a03190d13638e`. Não alteram o produto, controle ou artigos e não encerram QA-09.

## Base e mudanças

Aula r17 SHA `6b0df1096d0b6de6995ffc51bf8489cb45ab954a7aabdeb3f48d068c9777c57c`; inventário r17 `b8eae39cc72cf807d7b84aad7e7a38423168b809231bc3b7f08c439d6d25163b`. Os fragmentos originais e candidatos, suas posições UTF-16, hashes e as cinco substituições literais estão no manifesto `69ebcc8cf1c091c20b040dc43c6bda0467124006b8802d28537b2ce3c1c84115`. O arquivo de cada amostra adiciona uma quebra terminal, excluída do hash de fragmento.

Em `base-primeira-lei`, a nota da forma simplificada passa a dizer que calor recebido contribui positivamente e trabalho realizado pelo sistema negativamente para o saldo da energia total, `Q−W`; a variação da energia interna coincide com a variação da energia total quando as variações cinética e potencial são desprezíveis. Preservam-se a convenção calor entrando/trabalho saindo positivos, a equação geral e a equação reduzida.

Em `base-entropia-escoamento`, as legendas de Q̇ⱼ, Tⱼ e j passam de “ponto” a **parcela de fronteira** com temperatura uniforme do lado do volume de controle, com calor entrando positivo. A nota instrui integrar a taxa local de calor dividida pela temperatura absoluta local na área de troca quando T variar, ou usar parcelas isotérmicas adequadas. A soma mostrada continua sendo a forma discreta sob as condições explicitadas; não se introduz média aritmética arbitrária nem se altera a fórmula MathML, seus símbolos, unidades ou sinais.

## Confronto físico

Para massa fixa, ΔE=Q−W e ΔE=ΔU+ΔEc+ΔEp. Um gás ideal com cv=0,718 kJ/(kg·K), inicialmente 400 K, perde 100 kJ como trabalho numa expansão adiabática e reversível, depois recebe 50 kJ a volume constante. Com energias cinética/potencial desprezíveis, ΔU=−50 kJ apesar de Q=+50 kJ. A contribuição de calor é positiva, mas não determina o saldo; dados hipotéticos, não ensaio.

Em volume de controle, 100 kW entrando a 300 K e 100 kW a 600 K transferem `100/300+100/600=0,5 kW/K`; tratar as duas parcelas como 200 kW à média aritmética 450 K daria `4/9≈0,444444 kW/K`. Se o fluxo de entropia de saída menos entrada for 0,6 kW/K, a produção é 0,1 kW/K pelo balanço correto, ante `7/45≈0,155556 kW/K` pelo uso inadequado da média. Os valores são contraste nominal de contabilidade, não especificação de equipamento.

O [MIT, primeira lei](https://ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_4.htm) apoia a convenção e a diferença entre energia total e interna; [Purdue, segunda lei em volume de controle](https://engineering.purdue.edu/~wassgren/teaching/ME20000/NotesAndReading/Lec28_Reading_Wassgren.pdf), p. 1 do PDF, apresenta integral de transferência de calor sobre a superfície. Fontes reabertas em 30/10/2026; não são origem dos valores fictícios.

## Preservação e reprodução

`python3 auditoria/termodinamica/evidencias/QA-09/candidatas-primeira-lei-entropia-r17-20261030/verificar.py`, SHA `752442e1f101b3f3f008aad64f45742553c69286a3d8b7f1f308de830ce70339`, passou em simulação de substituição em memória: aula hipotética SHA `c567e78dbd9fc0d20874650b74ba12eb6ab58aa87d80af517ff2765bffae332c`, 197 artigos preservados por fragmento, 734 MathML idênticos em ordem, IDs e destinos de links/recursos mantidos. O verificador também confere hashes, reconstrução dos cinco deltas e contramodelos; não grava o produto. O preparador isolado SHA `cf45c4a70f48be989705334ced70cb7c8088dd4587df2bf181a6d93e2c20e840` recusa sobrescrever os artefatos já existentes e não deve ser reexecutado sobre eles.

O programa não substitui interpretação científica, auditoria da candidata ou revalidação de eventual aplicação. Sem navegador real, leitor de tela, teste com estudantes ou revisão humana. Mudança posterior da base exige reconciliação por versão; solicita-se Auditor independente para o texto, hipóteses, legendas, contramodelos e preservação.
