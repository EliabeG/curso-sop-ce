# FUN-02 r1 — auditoria técnica auxiliar

Data: 27/10/2026. Autor: `/root/auditor_aaa/auditoria_tecnica_ban02`, apoio independente do Auditor responsável.

**Não foi identificada divergência técnica na versão congelada examinada. Este documento não emite o parecer científico/pedagógico geral nem libera outro ID.**

## Reprodução efetivamente executada

O verificador documental e o módulo de cálculo foram lidos antes da importação. O primeiro lê arquivos locais; o segundo calcula em memória a partir do JSON. Não executam comandos externos nem avaliam expressões textuais do pacote. As funções exportadas foram executadas no Node REPL, com término normal:

- `verificarFun02()`: **240 verificações documentais** satisfeitas.
- `validateInventory({rootDir})`, chamado diretamente: **197 registros/197 artigos**, 11 recursos, 1.062 referências locais, zero erros e zero avisos.
- `calcularFun02(dados)`, chamado diretamente: **49 verificações numéricas** efetivamente executadas; cada condição falha lançaria erro.

As três saídas são integralmente idênticas aos JSON entregues. A comparação não se limitou ao resumo do Corretor. O módulo de cálculo integra numericamente as trajetórias declaradas e consome os ciclos/observação de P2 do pacote; esta execução confirma sua reprodução para os dados fornecidos, sem substituir a derivação científica independente.

Reprodução documental:

```js
var modulo = await import('file:///C:/Users/User/Downloads/SOP-CE/auditoria/termodinamica/evidencias/FUN-02/verificar-fun02-r1.mjs');
nodeRepl.write(await modulo.verificarFun02());
```

## Conferência independente de integridade e escopo

Os **seis arquivos publicados e suas seis cópias** conferem com o manifesto em SHA-256 e tamanho. As **26 evidências** enumeradas também conferem em hash e tamanho. Os snapshots anteriores de HTML, inventário e resumo são idênticos aos respectivos arquivos do pacote FUN-01 r2.

Uma extração independente dos artigos, separada do parser do validador, confirmou **194 artigos anteriores idênticos**. Os **194 objetos de inventário** permanecem idênticos e na mesma ordem. Cada uma das **194 linhas individuais anteriores do resumo** aparece exatamente uma vez, sem alteração, na versão atual. Essa última conferência foi realizada diretamente sobre as linhas; não depende da contagem de checks do script documental.

A retirada literal da unidade e de sua linha de menu, seguida da reversão dos seis deltas registrados para **C01/C02/C03/C08/C09/C10**, recompõe integralmente o HTML anterior. Não há alteração adicional no HTML além desses deltas. O inventário atualizou o hash/snapshot da fonte e acrescentou a descrição de FUN-02 ao método; seus limites e demais metadados de topo foram preservados.

Os **oito arquivos compartilhados/de infraestrutura e FUN-01** conferem com hashes anteriormente auditados: `registro.js`, `curso.js`, `curso.css`, schema, validador, guia e os dois arquivos de dados/cálculo FUN-01. Não foram repetidos os 56 testes BAN-02, pois essa infraestrutura permanece intacta.

## Três registros novos

Os novos IDs são `fun02-e1-caminhos`, `fun02-e1-integrabilidade` e `fun02-e1-calor-caminho`. Seus títulos coincidem com os `h3`; a comparação abrangeu também os demais itens, totalizando **197 títulos sem divergência**.

Cada artigo possui as marcas de inventário E1, banco aberto e resposta aberta; cada registro identifica seu artigo/fragmento e hash corretos, zero alternativas, recursos rastreados e contagem de etapas coerente. Todas as relações apontam para âncoras únicas existentes. Os vínculos de competência declaram avaliação parcial, e a revisão permanece pendente. O extrato `novos-registros-r1.json` coincide integralmente com os três objetos acrescentados.

O resumo inclui as três linhas novas e a distribuição correspondente ao JSON: **197 itens, 171 iniciantes, 22 intermediários e quatro avançados estimados**. Esta conferência valida a consistência da contagem, não o mérito da classificação. O SVG examinado referencia apenas seus marcadores internos, sem recurso externo carregado identificado.

## Identificação da versão

| Artefato | SHA-256 |
|---|---|
| HTML | `719a53ef86075dd3be9c7d9603faca620ec07416d1e97a5017740abb5b74c01a` |
| Inventário | `c577058429375c11196eb99ae6bd01a9020f5258d3981d72c58896829ed900a2` |
| Dados | `511aac986e9122e5498cdf69609274685791000a19f140a09d539fca01676319` |
| Código de cálculo | `2fdd0e498c41db2f7f8e90d5114dcd015f5377e00901e6274f25262e13c79a70` |
| SVG | `f324acce9060eb15eeab58958649392f4e5b667fbaf2ad9b63e3c68fbe3eae35` |
| Resumo | `c650d94556d527725595dfc86b1feaa055a32a2d9060e9b4680f1a152e11cca4` |
| Verificador documental | `ff9d21e594fa545d88af2f2a1964d1fc514e921974de388f058f5e3226ad8354` |

Os resultados por arquivo, artigo, registro e linha, bem como as saídas completas reexecutadas, estão em [FUN-02-r1-tecnico.json](FUN-02-r1-tecnico.json).

## Limites

Não foram executados Node CLI, navegador, teste móvel, leitor de tela ou piloto nesta subauditoria. A evidência de navegador do coordenador teve sua integridade conferida, mas sua execução não foi repetida por este apoio. Não houve nova conferência bibliográfica nem julgamento científico das soluções, níveis ou rubricas. Nenhum produto, controle ou arquivo do Corretor foi editado. Somente este relatório e sua evidência independente foram gravados.
