# BAN-07 r3 — resposta do Corretor ao ajuste R2-A

Data: 29/10/2026. Corretor: agente automatizado `/root/inspect_repo`. Versão aplicada mediante liberação do coordenador, **aguardando auditoria independente**. Não aprova BAN-07 nem libera o próximo ID.

O [parecer r2](../pareceres/BAN-07-r2.md) apontou que dois campos do inventário CR06 atribuíam a relação afim à dilatação, sem declarar a hipótese editorial sobre as escalas. No registro `cr-e1-06`, os campos `raciocinio.etapas[0]` e `vinculo_competencias.alcance` agora descrevem o reconhecimento da relação afim **quando ambas as escalas são lineares na altura da coluna, conforme hipótese editorial do curso**. A condição não é atribuída ao enunciado oficial.

A alteração afeta exclusivamente esses dois campos de `auditoria/termodinamica/inventario/inventario-questoes.json`: SHA-256 r2 `71ac07e042aa65675fc3d4b69d8d0ae11cb66df967d45e66b1a88f4f1350e074`; r3 `486c53c5aa6c432831599c4eca170e4620d089b4eb15b480dbfb2cbfaf54c9ce`. O restante do JSON, inclusive os outros 196 registros, foi comparado por reversão em memória e permanece idêntico. Categoria de reconhecimento, uma etapa, nível iniciante e vínculo C08 continuam coerentes com a tarefa. A linha Markdown já usa competências, nível, quantidade de etapas e justificativa sincronizados; não precisou mudar.

## Versão e verificações

O [manifesto r3](../evidencias/BAN-07/manifesto-r3.json) registra os hashes da versão e dos arquivos preservados. A [verificação r3](../evidencias/BAN-07/aplicacao-r3/verificacao-r3.json) contém os dois textos antes/depois, a comparação estrutural, a conferência semântica do resumo e o resultado do validador; o [backup do inventário r2](../evidencias/BAN-07/aplicacao-r3/inventario-r2-antes.json) permanece disponível. Entrega, manifesto, pareceres e demais evidências r2 foram preservados como registros da versão que examinaram.

O validador canônico do produto confirmou 197 registros e artigos, 29 recursos e 1.261 links locais, sem erros ou avisos. O módulo HTML e seu snapshot r2 permanecem byte a byte idênticos, assim como índice Markdown, JS, registro, suplementos e relatórios FON-01/02 e BAN-10; as digitais e o comportamento não foram modificados por esta edição. As provas funcionais r2 podem ser consideradas por identidade de HTML e JS, mas sua aplicabilidade cabe ao Auditor. Não foram executados novos testes de navegador, armazenamento pessoal, estudantes ou psicometria. O controle não foi alterado pelo Corretor.

A primeira execução encontrou uma falha ao registrar a verificação, após substituir o arquivo; o mecanismo de retorno restaurou automaticamente o inventário r2. Corrigido o registrador, uma segunda execução reconferiu os hashes e concluiu a aplicação e validação. O ajuste permanece sujeito a parecer independente sobre a versão efetiva.
