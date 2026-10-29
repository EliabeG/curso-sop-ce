# BAN-10 r1 — verificação de navegador pelo coordenador

Revisor automatizado: /root. Data local: 27/10/2026. Evidência complementar; não é o parecer independente.

Prévia local em http://127.0.0.1:54945/modulos/e1-termodinamica.html. Navegador integrado em segundo plano, viewport observado de 1265 × 712, sem ajuste de dimensões.

## Versões e alcance

O teste funcional inicial de CR09 começou no HTML 8033be33ff10db32244fcbc1d4be2c0ed25a6d270992fcd77e96b3d01677e345 e curso.js a6201b87bb6b35440206e85eb65e86fa50d3780f6bbe9443a1d5d7385138bdc1. O HTML 913d68e615e5a79d3f7c370c403df6b4de0a078a8b9cf14cdefaec63ff36af24 foi recarregado em seguida, preservando a marcação documental; nele foram feitos os testes conjuntos, filtro e teclado. Depois, o único ajuste funcional de JS foi pluralização textual, e o HTML teve uma etiqueta redundante removida do bloco histórico de CR68 para preservá-lo literalmente.

A versão final testada na conferência de singular, limpeza, leitura de CR79 e carregamento E2 foi: HTML 3839c7ba2e473ee9e5b3cdff80ea64242471b83b961eb117cee5a6918c884ae1; curso.js 6a450cbfb7049b22e999e3390238fec511c2da24caa3e228871c5a3128121de6. O teste conjunto completo não é apresentado como integralmente repetido após esses dois deltas restritos.

## Ações e resultados observados

- Estado inicial: 80/80 questões exibidas; treino com 0/71 respondidas, 0 acertos/erros; estudos críticos com 0/9 marcações.
- CR09 recebeu C, diferente da chave E. A ação Comparar com a chave oficial mostrou explicitamente estudo crítico sem pontuação e não coincidência documental. O treino permaneceu0/71, sem acerto ou erro; apenas estudos críticos passou a 1/9. A resolução abriu com chave oficial e interpretação autoral separadas.
- Após recarga, a marcação C de CR09 reapareceu, manteve o feedback sem pontuação e o contador separado. Em seguida CR68 recebeu C: o treino passou a 1/71, com 1 acerto e0 erros, e a marcação crítica permaneceu1/9. Nova recarga preservou essa separação.
- O filtro Somente não respondidas reduziu a exibição a 78/80, reconhecendo as duas marcações, e conservou os contadores globais separados. Ao desativá-lo, 80/80 foram exibidas.
- Refazer questão em CR68 removeu apenas a resposta de treino; CR09 permaneceu1/9. Refazer CR09 restaurou0/71 e 0/9. Somente as duas respostas criadas para este teste foram removidas. A linha de base observada era vazia; não foi apagado histórico preexistente.
- A análise de CR09 abriu por Expand e fechou por Return. O roteiro, interpretação, critério de autocorreção sem nota e fonte BIPM apareceram como elementos distintos do texto oficial.
- Na versão final, CR68 foi respondida novamente para conferir o texto 1 correta. O contador mostrou 1/71, 1 correta, 0 incorretas e 0/9 críticas. Refazer removeu essa resposta de teste e restaurou os dois contadores vazios.
- CR79 foi aberto sem marcar alternativa. A análise autoral mostra dois contramodelos com 45,73 W radiativos e condução de 2,23 W ou 111,43 W, rotulados como construções autorais. Foram inspecionadas capturas do roteiro, comparação e análise, sem sobreposição ou corte de conteúdo observado nessa largura.
- O E2 foi carregado somente para regressão de leitura do JavaScript compartilhado:40/40 questões, 0 respondidas, contador anterior preservado e sem separação crítica do E1. Nenhuma resposta ou arquivo de E2 foi alterado. Não é auditoria científica do E2.
- Consultas aos logs de erros/avisos do E1 e E2 retornaram listas vazias.

## Limites

Os testes de marcação e recarga usaram respostas novas de teste na prévia local; não comprovam migração de histórico real de estudante. Os cenários dinâmicos automatizados do Corretor e a futura revisão independente têm evidências próprias. Não houve aplicação com alunos, auditoria completa de acessibilidade, leitor de tela, testes de todos os nove itens na interface, dispositivos móveis ou todos os pontos de quebra. As capturas foram vistas nos resultados da ferramenta, sem arquivo de screenshot persistido. A documentação PDF foi inspecionada separadamente em PNGs reais.

