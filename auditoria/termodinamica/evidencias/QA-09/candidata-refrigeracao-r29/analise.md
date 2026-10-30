# QA-09 — candidata isolada: refrigeração e fichas 84/85, base r28

30/10/2026. Corretor automatizado `/root/next_graphics`. **NÃO APLICADA; aguarda Auditor independente `/root/reference_triage`.** Responde ao parecer `auditoria-formulas-r28-lote5/parecer.md` SHA-256 `5693d5a9fafb2cf9029bf5892db781e2e26734a90a69bc9ced2060b61e4a29c4`. O nome r29 indica a próxima possível aplicação; as candidatas usam a fotografia r28. Não altera produto ou controles e não encerra QA-09.

## Propostas

- **Base `base-refrigeracao`:** identifica w_c como trabalho líquido total não associado ao escoamento recebido pelo compressor, por unidade de massa e positivo; coincide com o trabalho de eixo recebido somente se outras modalidades de trabalho não associado ao escoamento forem desprezíveis. O COP usa trabalho líquido total positivo na mesma fronteira e período. As três legendas específicas de W no contêiner passam a declarar entradas menos saídas de trabalho. Os outros usos da legenda idêntica fora deste contêiner não são alterados.
- **Ficha 84:** a descrição de w_c passa a identificar o trabalho líquido total não associado ao escoamento recebido pelo compressor, positivo e em kJ/kg. A condição indica quando coincide com o trabalho de eixo. As mesmas frases são atualizadas na busca `data-busca` e no conteúdo visível.
- **Ficha 85:** Ẇ_in passa a ser potência líquida total recebida, entradas menos saídas, positiva, em kW; a condição nomeia Q̇_L, Q̇_H e Ẇ_in na mesma fronteira e período, sem outras interações energéticas relevantes. As cópias de busca e conteúdo visível são atualizadas juntas.

As fórmulas e os dados numéricos permanecem idênticos. Não se afirma que potência de eixo seja potência elétrica total do equipamento real. Na base, o trabalho de escoamento continua incluído em h e não é somado novamente. Contraste contábil sintético: compressor recebe 35 kJ/kg no eixo e 5 kJ/kg elétricos, portanto h₂−h₁=40 kJ/kg nas hipóteses dadas; com q_L=150 kJ/kg, COP=3,75 e q_H=190 kJ/kg. Usar apenas 35 daria ≈4,286 e confundiria o trabalho de eixo com o total.

[MIT, balanço em escoamento](https://ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_6.htm) distingue trabalho de escoamento de trabalho externo; [DOE/FEMP](https://www.energy.gov/cmei/femp/incorporate-minimum-efficiency-requirements-heating-and-cooling-products-federal), nota f da tabela, define COP como efeito útil por trabalho líquido de entrada na mesma unidade. Fontes abertas em 30/10/2026 não fornecem os números sintéticos.

## Identidade e reprodução

Aula r28 SHA `d7294e8ed772cf4530788586d693a6cdfbf1ef6fa05c69afbc984efc46e353d8`; formulário r28 `3157c9b114f3156e5517440d30b91ee8a4efdebcd95be8bd0c7a588f04dead46`; inventário r28 `0a7a12fbf0cd2a0898bcebfdfa7ae98c850bdb0bf7d2b34eea06cc6a8d9afb44`. `manifesto.json` SHA `d79bf0daa4d58783e927c6af58bc7d0b03f8a394c9e2739573ad3284b0addae3` contém intervalos, hashes de recortes e substituições literais com quantidades. Fragmentos isolados têm quebra terminal não incluída no hash.

`python3 auditoria/termodinamica/evidencias/QA-09/candidata-refrigeracao-r29/verificar.py` SHA `5a422d0924a0ca8e268896f013699653cbb632c5e6e965c2aeb30e7a640df9dd` passou somente em memória: preserva os 197 artigos da aula, as 98 fichas não alvo, os 734 MathML da aula e 191 do formulário, e os atributos ID/href/src/ARIA comparados. Aula hipotética SHA `2acc29d13f92da2e4ba351f1bc3a6ddd7af2ac075578d29a5c38722baa456aee`; formulário hipotético `5ea4a845a48c175febd103847cbf1acd4e0b8f29112ac455f39c77f32906c8d2`.

A candidata da base cobre o mesmo contêiner de uma proposta separada para EX-028; se ambas forem aplicadas, é necessário compor suas substituições sobre o mesmo original, conferir compatibilidade e calcular novos hashes conjuntos antes da aplicação, sem sobrescrever uma pela outra. A inspeção e o SHA acima não aprovam essa combinação. Avaliação científica, mapa e revalidação localizada da versão efetiva são pendentes. Sem navegador real, leitor de tela, estudantes, revisão humana ou certificação externa.
