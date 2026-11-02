# QA-09 — preparo protegido de pressão r27 → r28

30/10/2026. Responsável `/root/next_examples`. **NÃO APLICADO; aguardando decisão sobre as fichas 43/44 e sinal da coordenação.** A configuração atual cobre somente a candidata de pressão. Se as fichas forem aprovadas e incluídas, será necessário integrar seus manifestos e pareceres, validar possíveis sobreposições por documento, calcular e conferir os novos hashes combinados, reensaiar as guardas e gerar o mapa em cópia antes de qualquer aplicação. Este preparo não certifica uma futura combinação.

## Insumos e guardas

Aula r27 `9af8e2c9ffe509e40594d086a9ef4ad75127fb4ca873efb305d3144e08f3fc49`, formulário `16329b7369c4ba927f5f7da30551f86934aad1f6a6e55627443dea5cb9fe0c02`, inventário QA-09 `a58d7f0b0a5f097eef83ad83026ef49e801457b87f7cf2b2345c3dd915597c7c`; inventário oficial JSON `bc41bab109174695acd787c183dca7f8e58dd227c8389e48d83bc2b7a4e7e27e`, Markdown `abb09d0926d24a111a7963cc8c0726d7eeeaffaa703468fb602977d71a55cfb4`. Auditoria r27 SHA `fb60390d209f81bb4bcca7fddfb62756b399d7da5ec93bf42220550fb95eb501`, parecer da candidata SHA `84b0529c245994c4ed1fdac1bd246c11303ec1137dfe5dcdb9434c7efecbd83f`, manifesto aprovado SHA `70a4aa3e86d7604ee1281d493d702db8678b6517d88e8fbc9f61b7acde61e718`.

`aplicar.mjs` SHA `5031f48301c66dda38957a1cf51fb603d6c15500820d35a03309e3a7dadb8687` exige os hashes das fotos, documentos, pareceres e manifesto, trecho r27 correto e único, substituição exata, destino ausente, preservação dos 197 artigos, de 734 MathML e dos atributos ID/links/ARIA testados. O resultado hipotético da aula é `3486b562ad7e8ec563fbf191775642628617f0436fe831b5e3a91e4f503bf49c`; exclusivamente pressão, não representa futura combinação. A versão atual contém bloqueio explícito no modo `--apply`; removê-lo exige prévia decisão e sinal da coordenação. O código do modo bloqueado prevê snapshots, atualização do inventário oficial, geração e mapa, mas **não foi executado nem verificado ponta a ponta neste preparo** e é não transacional. Falha depois de escritas exigiria reconciliação antes de repetir.

Gerador `inventariar-r28.mjs` SHA `4bce09265481b96861791ed40839a49591dd0a88f2195dcc1c45b2708844da13` e mapeador `mapear.py` SHA `e7ea43dc15c8fd02d4fbef289767ef4ee80d77f508b22b09de95aaf4125edaa1` são adaptações para r27→r28 e ainda não foram executados. Não existe fotografia ou mapa r28 produzidos por este preparo.

## Ensaios realizados

`node auditoria/termodinamica/evidencias/QA-09/aplicacao-pressao-r28/aplicar.mjs --ensaio` executa cálculo em memória e não grava produto nem gera mapa/inventário; sua saída `verificacao-ensaio.json` SHA `2319a16eedd1e90b6682f5bb18c99d3cad252c12b99a787d1356b7e7bf96b7d2`. Simulação produz o SHA previsto e preserva formulário, 197 artigos e MathML inspecionado.

`testar-guardas.py` SHA `e61f590dc1cb985aa26ed0fedeaa055900066a974ba95914de58138c3758cd00` cria apenas fixture mínima descartável, executa a simulação válida, confirma bloqueio de `--apply` e adultera em separado aula, manifesto, candidata e parecer: todos são rejeitados antes de escrita. Saída `teste-guardas.txt` SHA `2bab7883ef6d8ccc2c3cebec73989f321a5261b9a1c686f6ce9c511a0e524339`. O ensaio não foi um navegador, teste de aprendizagem ou auditoria de ciência.

Os hashes da aula e do formulário efetivos permanecem os da r27. Aguardam-se pareceres das eventuais candidatas e decisão sobre sua inclusão. O teste de aplicação completa em cópia deve ocorrer sobre o executor final, seguido de revisão independente da versão efetiva.
