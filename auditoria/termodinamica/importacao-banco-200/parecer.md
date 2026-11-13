# Parecer independente — importação documental 1–200, r1

**Data:** 13/11/2026. **Revisor:** agente automatizado independente `/root/auditoria_importacao`, distinto do implementador.

**Veredito: APROVADO exclusivamente para a importação documental e integração funcional descritas abaixo.** Não constitui aprovação científica dos cálculos, aprovação de QA-09/BAN-08, classificação avançada do curso ou certificação humana. Nenhum próximo ID AAA é liberado.

## Critério e alcance

O pedido atual é acrescentar as questões do ZIP ao curso. Foram examinados os dois cadernos, os dois gabaritos e a página complementar, seus recursos e sua ligação à aula E1. Aplicam-se preservação documental, rastreabilidade, integridade dos recursos, isolamento funcional e verificação da versão efetiva do protocolo. QA-09 permanece em correção: seu critério integral exige referência verificável e recálculo de cada ocorrência numérica, incluindo figuras e explicações; tal recálculo não é realizado nem aprovado neste parecer. As afirmações de revisão interna nos PDFs são do material recebido, não evidência produzida pelo revisor.

## Versão examinada

Branch `feat/termodinamica-200-questoes`, versão local após correção do tratamento dos diagramas em páginas com tabelas. A identificação dos 58 arquivos examinados (páginas, CSS, script compartilhado, gerador, inventários, quatro PDFs e 46 PNGs) está em [hashes-auditoria.json](hashes-auditoria.json). A validade deste parecer se restringe a esses bytes e ao alcance indicado.

## Verificações independentes

1. Os quatro PDFs do repositório foram comparados byte a byte com as entradas do ZIP anexado pelo usuário: iguais.
2. Conferência integral dos **200 enunciados**, **1.000 alternativas**, **200 letras de gabarito** e **200 comentários** contra os PDFs. A comparação dos enunciados verifica preservação de caracteres, normalizando espaços e a ordem de leitura de células/legendas; as alternativas têm comparação textual ordenada. Os comentários foram extraídos independentemente com `pdftotext -layout`, em vez dos filtros geométricos do gerador, e confrontados integralmente. Nenhuma perda textual encontrada na versão final. Reprodutor: [verificar-fidelidade.py](verificar-fidelidade.py), que requer PyMuPDF, lxml e pdftotext.
3. As **50 tabelas** HTML foram confrontadas célula a célula, linha e coluna, com as matrizes dos PDFs: iguais. Na primeira versão, a Q75 apresentava falso positivo de tabela sobre um diagrama, omitindo palavras e figura. O implementador corrigiu esse achado, filtrou a falsa tabela e preservou os diagramas em páginas que também contêm tabelas. A reconferência integral final passou. Os recortes Q39, Q42 e Q75 foram inspecionados visualmente e preservam setas e legendas; os **46 complementos visuais** da versão final possuem recursos locais e texto correspondente.
4. IDs da página são únicos; referências locais, imagens, PDFs e âncoras HTML foram resolvidos sem destino ausente. Os quatro links de download retornaram HTTP 200 no servidor local.
5. Teste independente em **Chromium real**, via Playwright: carregamento dos 200 artigos; filtro de volume; busca Q101; marcação/correção; abertura do comentário; refazer; persistência após recarga; tema; chave exclusiva `sopmec:avalia:v2:e1-banco-200`; leitura de comentários sem JavaScript; viewport de 390 × 844 sem overflow horizontal da página. Nenhum `pageerror`. Reprodutor: [verificar-navegador.py](verificar-navegador.py), com servidor local na porta 8000 ou variável `BANCO_URL`.
6. Os **197 artigos anteriores** da aula E1 são idênticos byte a byte à base `49d452e502bba1d6e1139c31fa0874879cebc851`. `assets/curso.js` não foi alterado. O inventário operacional conserva integralmente seus registros `itens`; apenas data, descrição da reconciliação, hash e snapshot da fonte são atualizados. O snapshot histórico anterior foi preservado e seu hash continua conferindo; o novo snapshot é idêntico à aula atual. Isso reconcilia os atalhos externos aos artigos e não transfere aceite aos novos 200 itens.
7. O validador canônico `node auditoria/termodinamica/inventario/validar-inventario.mjs` passou na versão final: `ok: true`, 197 artigos, 29 recursos, 1.263 links locais, sem erros ou avisos. Seu alcance é estrutural/documental.

## Quadro dos critérios aplicáveis

| Critério | Resultado | Evidência e limite |
|---|---|---|
| Preservar cadernos e gabaritos recebidos | Atendido | PDFs idênticos; comparação integral documental |
| Numeração, alternativas, comentários e chave coerentes com a fonte | Atendido | 200 itens, 1.000 alternativas e 200 comentários confrontados |
| Preservar tabelas, dados e complementos visuais | Atendido | 50 matrizes idênticas; 46 recursos e legendas; Q75 corrigida e reexaminada |
| Identificar autoria e metadados editoriais | Atendido | Material autoral e classificação editorial explicitados |
| Integridade de links, IDs e recursos | Atendido | Resolução local, HTTP 200 e validador canônico |
| Responder, conferir, refazer, filtrar e retomar | Atendido | Chromium real e contexto sem JS no alcance registrado |
| Isolar progresso e preservar artigos anteriores | Atendido | Chave exclusiva; 197 artigos idênticos; script comum intacto |
| Reconciliar hash sem regravar evidências históricas | Atendido | Registros de itens preservados, dois snapshots identificados |
| Recálculo científico integral de QA-09/BAN-08 | Não aplicável ao aceite documental | Não realizado; os IDs e aceites científicos não são encerrados nem ampliados |
| Piloto, revisão humana, acessibilidade integral e aprendizagem | Não aplicável | Não executados nem reivindicados |

**Ajustes obrigatórios pendentes no alcance documental/funcional: nenhum.** O achado da Q75 e o tratamento de diagramas com tabelas foram corrigidos e reconferidos antes deste veredito. A revisão científica integral dos novos cálculos continua fora deste aceite e não pode ser deduzida da importação fiel ou dos placares.

**Decisão de continuidade:** integração deste banco documental aprovada na versão identificada. QA-09 permanece aberto; não há liberação do próximo ID da fila AAA.
