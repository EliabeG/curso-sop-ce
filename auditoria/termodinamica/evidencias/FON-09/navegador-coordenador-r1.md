# FON-09 r1 — verificação de navegador pelo coordenador

Data local: 2026-10-27. Revisor automatizado: /root. Evidência complementar, não é parecer independente.

Verificação funcional realizada no HTML SHA-256 bd356310c226ba5ab12ff0f51a9b13746fcd05396f9aa64414582ac8281f1372. Após isso, apenas a redação da nota foi esclarecida para nomear explicitamente a unidade incorreta e a tabela histórica. O HTML final, SHA-256 6ed5c74f03b2ce449f88e79d143c904442c524166a83afce8f12441d391a6625, foi recarregado no navegador: a nota atualizada apareceu e ambos os blocos iniciaram recolhidos. A conferência textual final não é apresentada como repetição integral dos testes funcionais anteriores. Prévia local em http://127.0.0.1:54945/modulos/e1-termodinamica.html#cr-e1-68. Navegador integrado, capturas observadas1265×712, sem alteração de viewport.

- A afirmação original85 permanece visível para julgamento; a nota distingue correção editorial de errata oficial, indica a origem documental e remete ao conjunto corrigido.
- Os dois details iniciam recolhidos e têm rótulos distintos. O conjunto físico corrigido abriu e sua tabela foi inspecionada visualmente com todas5linhas, unidades, valores e origem legíveis.
- No primeiro rascunho, a pressão101,325 quebrava em duas linhas. O Corretor aplicou a classe existente sem-quebra às pressões. Após recarga do HTML então testado, o número permaneceu inteiro e a tabela coube na coluna sem sobreposição observada.
- Na versão funcional testada, a transcrição histórica rotulada como inválida abriu pela ação Expand, mostrou a tabela histórica e fechou por Return.
- A resolução existente abriu na versão funcional testada e mostrou Gabarito definitivo:C—Certo, com a explicação condicionada às mesmas temperaturas/geometria.
- Nenhuma alternativa foi marcada; o banco continuou com0respostas no navegador. Não foi simulada migração de histórico real. Os seletores de identidade foram lidos no curso.js: digitalDoBanco percorre texto do .cr-enunciado e seus elementos, opções e gabarito, e não depende de visibilidade; essa leitura de código não é chamada de teste com tentativas históricas.
- Logs consultados por erros/avisos retornaram lista vazia.

A prévia do PDF local no navegador integrado ficou vazia e não foi contada como leitura documental. Os PDFs foram efetivamente renderizados por Windows.Data.Pdf e suas imagens inspecionadas em evidência separada. Isso não é teste de download/visualizador PDF em todos os navegadores. Não houve auditoria completa de acessibilidade, leitor de tela, dispositivo móvel real, todos os pontos de quebra, aplicação com estudantes ou publicação externa. As capturas da interface foram inspecionadas nos resultados da ferramenta, sem arquivo de screenshot persistido.
