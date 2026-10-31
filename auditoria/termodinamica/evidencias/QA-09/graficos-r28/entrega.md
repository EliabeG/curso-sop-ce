# QA-09 — triagem de três gráficos de treino na fotografia r27

30/10/2026. Corretor automatizado `/root/next_graphics`; **aguarda Auditor independente**. Este lote visual pontual revisa três gráficos raster compartilhados com questões de origem e seus respectivos exercícios autorais. Não altera artigos, ativos ou controles; não substitui o tratamento independente dos 197 artigos e de suas fontes oficiais. As imagens foram abertas visualmente como arquivos locais, não no navegador; coordenadas abaixo são estimativas de leitura de pixel e não ensaio metrológico.

Aula r27 de `aplicacao-carnot-flashcards-r27-r1/resultado/depois-aula.html` SHA-256 `9af8e2c9ffe509e40594d086a9ef4ad75127fb4ca873efb305d3144e08f3fc49`.

| Recorte | SHA-256 do artigo | Recurso PNG e SHA-256 |
|---|---|---|
| AV-06, UTF-16 [990447,994499) | `89dc4205deb6e31424ecf39c1abc0a270339b7200d33d281f528f7c28762e87d` | `figura-922604ee21ac.png`, `922604ee21ac25fec713806a3102c7b775b9cd16ba2c77054cb45d976226b17e` |
| AV-30, UTF-16 [1076355,1080938) | `b15d6dd6aa44531627bb9a953e5d572a383804b557bb38df3869b581420c3b01` | `figura-de4ee7b16ed4.png`, `de4ee7b16ed42d37537a23bbcf6cf7aee66cb447e11bb950b3c783e3a859aa1b` |
| AV-37, UTF-16 [1103560,1107932) | `b741f7c26e317df09eaf7984e2065f881464ffc7367202fa2968b4ce30efe928` | `figura-222735fab01e.png`, `222735fab01e54a81e34f3bb54cfd7097a8cbc1391ebe6420d60df8b2513a9cb` |

## Achado a examinar: ambiguidade de AV-06

A imagem compartilhada com CR-06 é uma representação de duas escalas e três níveis identificados simbolicamente: pontos de gelo, vapor e nível intermediário T_X/T_Y. AV-06 fornece os pares X=0/Y=20 e X=100/Y=70 e pede X para Y=45; a resposta matemática X=50 está correta pela interpolação linear. O enunciado não diz que os dois pares correspondem aos pontos de gelo/vapor, nem que o traço intermediário representa Y=45. Assim, não é demonstrado que a resposta esteja errada ou que a figura seja uma escala quantitativa para esse problema.

Ainda assim, o comando chama o esquema de ilustrativo e a orientação didática diz “combinar o desenho com os dados”, criando possível leitura quantitativa que não foi delimitada. Se um leitor assumir os pares nos traços de gelo/vapor e Y=45 no traço intermediário, os pixels aproximados no arquivo 1290×870 têm alturas 599, 219 e 468: a fração geométrica é (599−468)/(599−219)≈0,345, em vez da metade exigida pelos valores do enunciado. Essa discrepância **depende dessa atribuição não declarada** e não demonstra defeito da figura original ou da alternativa. Recomenda-se revisão editorial independente sobre declarar que o desenho é esquemático e que os pontos fornecidos são dados do enunciado, ou empregar figura autoral compatível, preservando a figura de origem e o gabarito oficial. Qualquer mudança do artigo AV-06 exige tratamento próprio do banco e auditor independente.

## Outros dois recortes

- **AV-30:** o gráfico local exibe expansão A→B, V crescente, e o enunciado fornece gás ideal isotérmico, única modalidade de trabalho de fronteira e Q=300 kJ; ΔU=0 e W=300 kJ, alternativa D. O diagrama é qualitativo; não extraí valores de seus eixos nem autentiquei a imagem em relação à fonte oficial.
- **AV-37:** o gráfico exibe disponibilidade/irreversibilidade em função do ângulo da manivela. O enunciado qualifica expressamente a conta como independente dos valores das curvas. T₀=300 K e S_ger=0,20 kJ/K fornecem 60 kJ, alternativa C. O arquivo não fornece escala vertical para medir esse número, nem foi tratado como dado numérico.

## Reprodução e limites

`python3 auditoria/termodinamica/evidencias/QA-09/graficos-r28/verificar.py` SHA `99c92e8f5a47ba51f2e720c116fe98e44f3b06751df319e8dd64480887915a09` passou, conferindo hashes, vínculos, dimensões PNG e três contas. A associação da posição geométrica de AV-06 é um teste condicional interpretativo, não uma inferência automática feita pelo script. Não comparei as imagens com as provas oficiais nesta rodada; não há conclusão sobre fidedignidade ou acessibilidade, nem aprovação independente, ensaio em navegador ou teste com estudantes.
