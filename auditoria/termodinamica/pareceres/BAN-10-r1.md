# BAN-10 r1 — parecer independente

**Veredito: AJUSTES_OBRIGATORIOS. Próximo ID não liberado.** Auditor: agente automatizado independente `/root/auditor_aaa`. Revisão iniciada em 27/10/2026 e concluída em 28/10/2026. Há um bloqueador científico, **R1-A, em CR34**. Os demais critérios examinados estão atendidos; não há verificação pendente além da reapresentação desse ajuste e de seus derivados.

## Critério e versão

BAN-10 exige examinar ambiguidades, em especial CR09/24/68/79, pesquisar outros casos, separar texto/chave oficiais de interpretação e suplementos e retirar da nota de domínio ou transformar em estudo crítico a medida inválida. O protocolo também exige coerência científica, pedagógica e funcional. O recorte não encerra BAN-07, BAN-08 ou FON-01 globais.

Entrega e manifesto congelados: [BAN-10-r1](../entregas/BAN-10-r1.md), [manifesto](../evidencias/BAN-10/manifesto-r1.json).

| Arquivo | SHA-256 examinado |
| --- | --- |
| Manifesto r1 | `1fd879c048b08565e901055281545f44f65a39f21ca87b3901f0e8263077f7f7` |
| modulos/e1-termodinamica.html | `3839c7ba2e473ee9e5b3cdff80ea64242471b83b961eb117cee5a6918c884ae1` |
| assets/curso.js | `6a450cbfb7049b22e999e3390238fec511c2da24caa3e228871c5a3128121de6` |
| inventario/inventario-questoes.json | `d4a64b53747170f9d1d9cd0446d3f1de22110c73454c9f4fdf9359b005434641` |
| inventario/INVENTARIO_QUESTOES.md | `38a90361a7912dfc0839927ea50b044b6e87b0116eec2085b515573b648f3d68` |

## Evidência e critérios

A [matriz científica independente](BAN-10-r1-cientifico.json) registra os 197 confrontos individuais, as 12 decisões, cálculos, fontes, páginas efetivamente vistas e o achado. Cada hash da triagem confere com a fonte-base. A revisão usa as leituras independentes anteriores de BAN-02/FUN-01/FUN-02, identidade dos artigos, releitura integral dos 12 casos alterados e sete releituras dirigidas adicionais; não se apresenta como novo recálculo integral dos 197 itens.

| Critério aplicável | Resultado e fundamento |
| --- | --- |
| Cobertura e busca além dos quatro prioritários | **Atendido.** 197 registros individuais confrontados; 12 decisões explícitas. CR78/AV17/AV37 têm encaminhamentos delimitados, sem nova ambiguidade de resposta demonstrada neste recorte. |
| Texto e chave oficiais rastreáveis | **Atendido.** Quinze PNGs oficiais efetivamente vistos pelo Auditor, incluindo contexto, figura e justificativa de CR80; CR68 herda FON-09 por identidade. Chaves oficiais não são tratadas como justificativas técnicas ou anuladas editorialmente. |
| Separação entre documento, interpretação e suplemento | **Atendido na apresentação.** Notas, roteiro, análise e autocorreção estão identificados. Contramodelos CR79 são construções autorais, não medições ou dados originais. |
| Validade científica das decisões | **Não atendido integralmente: R1-A.** CR04/09/24/35/39/62/79/80 têm fundamentação admissível para o estudo crítico; retenções CR51/55/68 são justificadas. CR34 confunde condições da igualdade com as do sinal da variação de energia. |
| Tratamento pedagógico e metadados | **Parcial: depende de R1-A.** Os roteiros solicitam justificativa e oferecem critérios de autocorreção sem nota; o caráter guiado e os limites de autonomia estão declarados. Os 12 metadados acompanham as tarefas, exceto a justificativa conceitual de CR34. Não se atribui domínio avançado à letra marcada ou à consulta da solução. |
| Exclusão real da pontuação e continuidade | **Atendido.** Nove críticos ficam fora de numerador/denominador, inclusive com respostas anteriores. Restam 71 itens CR pontuáveis; marcações críticas têm comparação documental neutra. Digitais, recarga, filtros e refazer foram verificados. |
| Preservação e isolamento | **Atendido.** 185 artigos/registros fora dos 12 casos preservados; 160 identidades CR/AV intactas; Q30, FUN-01/FUN-02 e conteúdo FON-09 preservados. Alteração compartilhada restrita a `iniciarBanco`, com guarda E1 + marcador exato e testes dos fluxos padrão. |
| Reprodutibilidade e limites | **Atendido.** Subauditoria técnica reproduziu 589 verificações, incluindo 18 comportamentos, e executou 28 verificações próprias. Canônico: 197 artigos/registros, 29 recursos, 1.166 links, sem erros/avisos. Conferidas 77 entradas de integridade e nove cópias. |
| Piloto, domínio empírico, auditorias globais e curso avançado completo | **Não aplicáveis ao fechamento isolado.** Não foram executados nem aprovados por extensão. |

O [subparecer técnico](BAN-10-r1-tecnico.md) e seu [JSON](BAN-10-r1-tecnico.json) distinguem DOM/VM controlados de navegador. A [evidência de navegador do coordenador](../evidencias/BAN-10/navegador-coordenador-r1.md) discrimina as versões dos testes: recarga/filtro/teclado em versão anterior com deltas restritos; singular, limpeza e leitura E2 na versão final. O Auditor não reivindica essa execução, teste móvel ou auditoria completa de acessibilidade.

Os cálculos discriminantes foram refeitos: CR24, razão termométrica 1,3660492; CR39, 350 × 4,2 = 1.470 J; CR79, 45,729144 W radiativos contra 2,2285 W ou 111,425 W condutivos; CR80, geração 400 W, área 4 m² e 40 °C somente sob a redução estacionária/convectiva. A exclusão de CR39 é conservadora: a leitura usual da máquina térmica sustenta C, e a divergência do apoio está registrada. Não se exige excluir automaticamente todo modelo convencional nomeado.

## R1-A — distinguir ΔU > 0 de ΔU = Q em CR34

O item oficial afirma apenas que a energia interna aumenta. A triagem declara: “A conclusão U aumenta requer ausência de trabalho líquido de saída ou outras variações de energia”. A nota relaciona a sustentação de C à ausência desses termos, e o roteiro pergunta por condições “necessárias” para ΔU = Q > 0.

Isso não é uma demonstração válida da ambiguidade alegada. Pela primeira lei fechada, a igualdade ΔU = Q requer **W + ΔEc + ΔEp = 0**; anular separadamente os termos é suficiente, não necessário. A desigualdade ΔU > 0 é outra afirmação. A [primeira lei total do MIT](https://web.mit.edu/16.unified/www/SPRING/thermodynamics/notes/node14.html) sustenta essa distinção.

Há também uma restrição física que a crítica precisa respeitar. Para massa e composição fixas de gás ideal simples, estados inicial/final de equilíbrio no mesmo volume, cv(T) > 0 e calor exclusivamente entrando a temperaturas positivas, o balanço de entropia dá ΔS = ∫δQ/Tb + Sger > 0. A identidade de estado dá ΔS = m∫cv(T)dT/T; logo T e U aumentam. Trabalho não transporta entropia. Portanto, escolher um trabalho arbitrário no primeiro balanço não demonstra um contramodelo possível. Essa é uma inferência do Auditor a partir das [relações de estado do gás ideal, MIT §5.4](https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node40.html) e da [segunda lei, MIT §5.5](https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node41.html).

**Ajustes obrigatórios e evidência de reapresentação:**

1. Corrigir a alegação de necessidade para o sinal e separar igualdade, desigualdade e hipóteses suficientes. Não ensinar que trabalho adicional, por si só, invalida C.
2. Tornar coerentes a justificativa editorial, roteiro, análise, rubrica e metadados de CR34. Se a exclusão continuar fundamentada em ambiguidade do sinal, apresentar leitura/contramodelo fisicamente admissível, com fronteira e significado de “receber calor” explícitos e ambas as leis respeitadas. Outra possibilidade é fundamentar o estudo como esclarecimento de modelos, sem atribuir ao original a igualdade que ele não afirma. Não é obrigatório mudar o gabarito oficial ou a escolha de estudo crítico.
3. Reapresentar decisões/triagem/registro/resumo e evidências derivadas coerentes, preservando r1. Demonstrar delta restrito, novos hashes e validação pertinente. Não reabrir os outros 196 registros nem repetir testes de infraestrutura intacta; se a classificação pontuável/crítica mudar, conferir também os contadores afetados.

**Decisão final: AJUSTES_OBRIGATORIOS.** Somente a correção R1-A e seus derivados podem seguir para reapresentação do mesmo BAN-10, mediante coordenação. Nenhum próximo ID está liberado; nenhuma classificação global de nível avançado foi concedida.
