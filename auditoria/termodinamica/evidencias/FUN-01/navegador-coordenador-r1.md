# FUN-01 r1 — verificação de navegador pelo coordenador

Data: 2026-10-27. Escopo: nova unidade FUN-01 do curso E1. Esta evidência complementa o parecer independente; não concede aceite.

## Versão e ambiente

- HTML: modulos/e1-termodinamica.html.
- SHA-256: cacda8c7742eead77aa1e92021b01c085c1b7340201d5cca0ada8ff743a8b04f.
- Prévia local: http://127.0.0.1:54945/modulos/e1-termodinamica.html, servidor de leitura da pasta de trabalho, sem publicação externa.
- Navegador integrado do Codex, controles CUA e árvore de acessibilidade. Capturas observadas com 699 × 599 pixels; nenhum tamanho de tela foi forçado.

## Resultados observados

1. O link 3.1 do sumário levou a #fun01-estado-equilibrio; o roteiro da unidade levou a #fun01-problemas.
2. As soluções dos quatro problemas puderam ser abertas, expondo resolução e rubrica de 10 pontos. A versão final congelada foi recarregada e os quatro controles foram conferidos.
3. O controle do problema 3 foi fechado e reaberto pela tecla Return, com os dois estados confirmados na árvore de acessibilidade.
4. A abertura da unidade e as tabelas dos problemas 2, 3 e 4 foram inspecionadas em capturas. O conteúdo permaneceu legível no tamanho observado; as quebras de linha da tabela de seis colunas do problema 4 não produziram sobreposição visual.
5. Após a última revisão de texto, a recarga final confirmou o exemplo de reação A ⇌ 2 B, a expressão 2 μB − μA, o exemplo μA = 6 e μB = 3 e a distinção entre bloqueio cinético e equilíbrio.
6. As consultas de logs do navegador por erros e avisos retornaram listas vazias. Não foram selecionadas respostas nem alteradas tentativas nos bancos fechados.

## Limites e ocorrências da automação

O seletor Playwright do resumo não localizou o controle inicialmente e domSnapshot sofreu timeout. A verificação prosseguiu com os controles documentados da árvore de acessibilidade. Algumas tentativas de abrir controles fora da área visível não confirmaram a expansão; essas tentativas não foram contadas como sucesso. Com estados atualizados e rolagem, as soluções 2 e 4 abriram pela ação de acessibilidade Expand. O problema 3 foi colocado na área visível, aberto por clique e depois alternado por teclado, com confirmação de conteúdo e estado.

As capturas iniciais antecederam o último pequeno acréscimo sobre equilíbrio químico; a recarga e as verificações dos controles e desse acréscimo usaram o HTML congelado acima. As imagens foram inspecionadas nos resultados da ferramenta, sem arquivos de captura persistidos.

Não constitui auditoria completa de acessibilidade, teste em leitor de tela, múltiplos navegadores, dispositivo móvel real, todos os pontos de quebra, piloto com estudantes, gerenciador de downloads ou autenticidade dos PDFs externos. As tentativas inconclusivas de interação fora de tela não demonstram por si só defeito do curso.
