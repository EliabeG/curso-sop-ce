# QA-09 — auditoria independente da candidata do diagnóstico 2

Data: 30/10/2026. Auditor automatizado `/root/planning`, independente do Corretor da candidata. **Veredito localizado: APROVADA para aplicação como proposta isolada.** A alteração ainda não foi aplicada ou auditada na versão efetiva. QA-09 integral continua em correção; o próximo ID não está liberado.

## Critério e escopo

QA-09 exige a conferência do conteúdo numérico, entre outros, nos 28 diagnósticos. O parecer dos diagnósticos 1–10 identificou ambiguidade no instrumento do item 2; esta revisão examina apenas a candidata e sua identidade, sem aprovar o item 2 na versão aplicada nem o ID integral. A base examinada é a aula SHA-256 `2d6b8fb2f9c99e04d22c19d7b32bbc3eb20577459d9132e506f9c0acef3f2fc2`, inventário r9 SHA-256 `023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d` e parecer do achado SHA-256 `ec141bf0549af65e6fccbabca00810ff91493d8d80935a84753ef1edf97b0e0a`.

Análise do Corretor: `auditoria/termodinamica/evidencias/QA-09/diagnostico02-candidata-r9-20261030/analise.md`, SHA-256 `ea8a1a9db0e65b59a44f32ed453818d3b0b68997482c27c1215ca9afb0bf6188`; manifesto na mesma pasta, SHA-256 `869ee0dcc540b1d7d53b4ac764494d5748a471bbea9ffc6dd4963246c4a8f056`.

## Revisão científica e literal

Na versão atual, a descrição apenas de um tubo metálico curvo que aciona ponteiro não determina o mensurando. Um manômetro de Bourdon conectado diretamente ao processo responde à pressão do fluido; um termômetro de gás pode utilizar tubo de Bourdon, bulbo e capilar em sistema fechado cujo mensurando é a temperatura do bulbo. A [WIKA descreve o manômetro](https://www.wika.com/media/Technical-information/English/ds_in0001_en_co.pdf) e o [termômetro de gás, seção 2](https://www.wika.com/media/Operating-instructions/Operating-instructions/Temperature/Dial-thermometers/oi_tgt73_ex_en_de_fr_es.pdf). São exemplos de configurações, não fonte dos valores didáticos.

A candidata especifica conexão direta ao fluido de processo e deformação por sua pressão, o que distingue o instrumento pretendido do contramodelo de termômetro. Mantém a pergunta por instrumento e grandeza e a resposta de manômetro de Bourdon e pressão; não fornece previamente o nome do instrumento. A primeira parte e a solução são preservadas. Com limite inferior −20 °C e span de 150 °C, o limite superior é −20+150=130 °C; a magnitude do intervalo também é 150 K. O enunciado não determina incerteza ou pressão absoluta/manométrica e a solução não reivindica isso.

Conferi o trecho original único na posição r9 UTF-16 520730–521217 e o seu contexto, título e hash `4670ee317c14cbcb66974953d954f942f3d50e59e0b46b9c4c9f9553111eb786`; a candidata tem hash do fragmento `5b08c714ad542c5600f719f98de0a8503f1cf50ce691fdb2f0c58ec64da167f9`, ambos sem a quebra final dos arquivos isolados. A troca literal da única frase antiga pela nova reconstrói a candidata, preservando o restante byte a byte. O verificador independente `auditoria/termodinamica/evidencias/QA-09/auditoria-diagnostico02-candidata-r9-20261030/verificar.mjs`, SHA-256 `b1723cfc77e4fb4c0df170d6c8dde6f88392e7cf64e1a974ef9413fa0a16ca57`, passou na simulação em memória: parser sem erros, 197 artigos idênticos e mesma ordem e conta de span correta. Uma simulação não comprova aplicação real nem comportamento em navegador.

| Critério localizado | Resultado |
|---|---|
| Identidade da base, original e delta | Atendido na fotografia r9, por posição, contexto, unicidade e hash. |
| Eliminar o contramodelo e preservar objetivo | Atendido para a conexão ao processo e pressão como mensurando; instrumento e grandeza seguem sendo perguntados. |
| Resultado numérico e unidades | Atendido para dados nominais; nenhuma precisão experimental reivindicada. |
| Versão efetiva, mapa e regressão após aplicação | Ainda não examinados; obrigatórios após aplicação. |
| QA-09 integral e liberação do próximo ID | Não atendidos; continuam bloqueados. |

O Corretor pode apresentar a aplicação na versão efetiva após reconferir a base; esta revisão não é autorização para alterar outros IDs. Depois, gerar nova fotografia e mapa sem sobrescrever históricos, verificar os 197 artigos e inventário, as referências e o impacto dos aceites anteriores; solicitar novo parecer independente para a versão aplicada. Não houve teste com alunos, revisão humana, navegador real ou certificação externa.
