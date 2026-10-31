# QA-09 — auditoria independente de placar e tempo em VM r15

Data: 30/10/2026. Auditor `/root/next_formulas`; corretor `/root/next_graphics`. **Parecer: APROVADO NO RECORTE DE FUNÇÕES E CASOS ENSAIADOS**, sem inferir teste em navegador ou cobertura integral de QA-09.

## Identidade e execução

Confirmei SHA-256 da entrega `2e28ac398ab008d64627f12d7d79e1d5cf00cca9174f98ad7f354660051836ed`, do verificador `6241e84be0060a5d96e9a1e1f5281013469ffb12134a1595f1f2167cedd8ec7e`, de `assets/curso.js` `a20f4d19158073a9a1c48aabdfba8fa863b02063e16061c00b16448a6ccc2e13`, de `assets/registro.js` `46da94527d6639fe0265bd766286f1ef39623966105e00bda3b31f21ca2c247c`, da aula `f6c461f1d6039ea47dc7e97f9ad734bb0ea3fcb902f01ffdbf18d18d88e08d0e` e do inventário r15 `c8c9c3a3e141eba47a16e9f85c69f97c6e8b8a55aab689c6120ef1a0070c9d9c`. A aula e o inventário são entradas de identidade, não dados executados na simulação.

Inspecionei o verificador: somente leitura, verifica hashes, executa `registro.js` em VM e extrai por marcadores funções efetivas de `curso.js`; injeta objeto `window`, armazenamento, lista de letras, expressão regular, contexto de questões e relógio fictícios. A expressão regular e as letras injetadas coincidem com as constantes atuais do código real. O recorte contém as cinco funções declaradas; a execução não inicializa a aplicação nem seus eventos. Reproduzi `ok: true`, 30 questões no registro de E1.

## Observações

O teste das três respostas sintéticas confirma 3 respondidas e 2 acertos em resumo e progresso, sem contar chave obsoleta, e a apresentação de 67% das respondidas. A ausência de resposta não exibe percentual. O formatador ensaiado trunca milissegundos para segundos inteiros e limita tempo negativo a zero: 59.999 ms → 00:00:59; 3.661.000 ms → 01:01:01; 360.000.000 ms → 100:00:00. No ramo genérico de simulado com relógio injetado, confirma 4 minutos decorridos frente a 3, mensagem de esgotamento e, após correção simulada, resultado e tempo final de 1 minuto. Esse último teste não prova que E1 chama esse ramo nem testa o fluxo de um simulado.

Repeti a busca por executáveis nomeados no PATH, sem encontrá-los; isso não demonstra ausência em todo o sistema e não valida os demais locais ou uma sessão de usuário. Os ensaios usam dados artificiais e não testam DOM, CSS, renderização, teclado, acessibilidade, armazenamento real, múltiplas abas, carregamento completo, demais estados de simulado, bancos complementares ou correção científica dos gabaritos. Não houve teste em navegador, estudante ou revisão humana, e produto não foi alterado.
