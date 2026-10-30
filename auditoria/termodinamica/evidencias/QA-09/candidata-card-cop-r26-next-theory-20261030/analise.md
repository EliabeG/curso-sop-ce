# QA-09 — candidata isolada card-cop, r26

30/10/2026. Corretor `/root/next_theory`. **Não aplicada; aguarda Auditor independente.** Responde ao [parecer dos cartões](../../../pareceres/QA-09-reconciliacao-flashcards-r26-auditoria-next-examples-20261030.md).

O cartão define COP para ciclo por compressão acionado por trabalho, com calor útil e trabalho líquido total recebido positivo na mesma fronteira e ciclo. Distingue calor retirado da fonte fria para refrigeração e calor entregue à fonte quente para aquecimento. Por exemplo, 300 kJ de calor útil e 100 kJ de trabalho recebido com saída de 20 kJ dão W líquido recebido de 80 kJ e COP=3,75. Os valores são ilustrativos e não descrevem equipamento real.

Fontes: [MIT, balanço de escoamento](https://ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_6.htm), [MIT, limite de Carnot](https://ocw.mit.edu/courses/res-2-008-thermodynamics-and-climate-change-summer-2020/mitres-2-008su22_book.pdf), [DOE, outro acionamento de refrigeração](https://www.energy.gov/sites/default/files/2017/06/f35/CHP-Absorption%20Chiller-compliant.pdf). Os modelos sintéticos não são dados medidos dessas fontes.

Fotografia r26 SHA `afc7ff0aba80596aa8aa7a3eeb5b9a470948c7d866c6911911b9b00fb243bac2`; inventário SHA `d73d6b239822b288329a75fc1f976419ccae7047d1bc74ba161102a529038241`. Fragmento `COP` UTF-16 [1270543,1270882), original SHA `d5fb4be0c7fa1fd59c1e33f62548d6699ae5ef10bd440c5c0f2960318039cafd`, candidata `d98cae1270200a3ee7c29ba84b52d11658169eb3bf2e39fed4b1f03246a92fac`. Arquivos isolados têm quebra final excluída dos hashes; manifesto registra uma substituição literal.

`node auditoria/termodinamica/evidencias/QA-09/candidata-card-cop-r26-next-theory-20261030/verificar.mjs` passou: simulação em memória preserva 197 artigos, 734 MathML e atributos inspecionados de identidade, links e ARIA; SHA do HTML hipotético `19e855436502aefefd559b30b79bc81842fad703ac4ee5abb15324cba6e1cb40`. A revisão do sentido, a composição das candidatas e a auditoria da versão eventualmente aplicada são independentes deste teste. Sem ensaio de navegador, leitor de tela ou alunos.
