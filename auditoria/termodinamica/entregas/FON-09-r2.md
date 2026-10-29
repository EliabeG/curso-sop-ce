# FON-09 r2 — fragmento completo (R1-A)

Entrega congelada do Corretor, 27/10/2026, em resposta ao [parecer r1](../pareceres/FON-09-r1.md).

O parser agora localiza o primeiro `#` e preserva todo o sufixo com `slice`, antes de decodificar e validar. A regra PDF permanece `page=N`, com inteiro positivo seguro. Assim, `#page=3#extra`, `#page=3#` e variantes `%23` são rejeitados. Em HTML, `#fundamentos#extra` procura o ID completo e não pode passar pela existência isolada de `fundamentos`.

[Delta integral](../evidencias/FON-09/delta-validador-r2.json): única mudança de produto em `validar-inventario.mjs`. SHA-256 anterior `114b1a063cb2a88e505c9ecffd2b22c75f29b709419b24e9e533331fa7283b22`; novo `0bd26bcf6288b3bd159ac7c167bfeb4a1a49bbebe784d26a3a93739fcb7790d5`.

- [20 casos PDF/HTML/outros recursos](../evidencias/FON-09/teste-pdf-r2.json): todos passaram, incluindo os dois contraexemplos, variantes codificadas, existência de arquivo, positivos e negativos.
- [39 casos do contrato existente](../evidencias/FON-09/contrato-existente-r2.json): todos passaram, executados novamente sem mudar fixtures ou expectativas.
- [Validação canônica](../evidencias/FON-09/validacao-inventario-r2.json): 197 artigos/registros, 15 recursos, 1.072 links locais, zero erros/avisos.
- [43 verificações de preservação](../evidencias/FON-09/preservacao-r2.json): HTML, dados, inventário e resumo idênticos à r1; pacote, 26 evidências, cinco snapshots anteriores e guia intactos.

[Manifesto e cópias r2](../evidencias/FON-09/manifesto-r2.json). O pacote r1 permanece imutável. Ciência e navegador são herdados por identidade dos arquivos; não foram refeitos. O limite permanece: validar sintaxe/existência de PDF não determina sua quantidade de páginas.

Corretor: implementação e testes. Apoio_fun01: leitura pontual do parser e casos puros em memória, sem alterar arquivos; não substitui o Auditor. Nenhum controle/checklist ou próximo ID foi alterado/iniciado. Aguardando reauditoria de FON-09 r2.
