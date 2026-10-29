# FON-01 — portais oficiais e versões, apoio do coordenador

Data: 28/10/2026. Responsável: agente automatizado /root.

A API pública usada pelo próprio portal Cebraspe forneceu HTTP 200 para os oito concursos. As respostas completas, URLs e horários estão preservados nos arquivos JSON desta pasta. A rota foi identificada pela leitura do [script oficial](https://www.cebraspe.org.br/concursos/static/js/main.4bdb8f79.chunk.js), que foi arquivado, sem executá-lo. A regra de montagem dos links respeita o campo isGuid; nenhum nome de ato foi inventado.

O registro PORTAIS_COORDENADOR.json identifica o método, consultas, arquivos e limites; atos-selecionados.json relaciona as oito justificativas oficiais de alterações de gabarito, com datas e URLs do catálogo. Cada prova/chave legada está na listagem atual: 20 URLs coincidem exatamente após decodificação e duas CAESB diferem apenas na extensão .PDF/.pdf. Essa normalização está explícita e não equivale a certificar os bytes da variante publicada ou a última versão.

## Atualização CAESB

A [listagem oficial CAESB](https://apis.cebraspe.org.br/cebraspe/eventos/caesb_24) aponta uma [prova do cargo 9 atualizada](https://cdn.cebraspe.org.br/concursos/caesb_24/arquivos/905BAE8B8901D96A45D9CBF7F17341894AF8405A0E2D9122A552F640CAC8B9DB.pdf), publicada em 11/05/2026 às 12:39. O download tem 1.098.179 bytes e SHA-256 767b22affb2fe53295ccf8a4f66dd9e4a4cae55ba36d1a49b1dc980dc7efa9b5; difere do PDF legado de 651.707 bytes, SHA-256 84ae0602e23691a27529b1f96e7c58803ad82982550301724345cb0b5d690df5. A diferença não foi tratada como mudança automática de chave.

Windows.Data.Pdf abriu a versão atualizada com 16 páginas. Renderizei e vi somente as páginas físicas 1 e 5; os dois PNGs e o registro leitura-visual-coordenador.json estão arquivados. A página 5 contém a questão 38 completa, figura, alternativas e justificativa de D, 40 °C. A comparação integral e o efeito sobre os itens foram encaminhados ao Corretor e ao Auditor.

## Disponibilidade e limites

Atos CPNUJE atualizado, Petrobras NM, Petrobras NTJ e Itaipu foram baixados. TBG, TRF6, CAESB e Petrobras NS tiveram falhas de conexão em downloads locais; os registros de tentativas foram preservados. O leitor web acessa os PDFs oficiais dessas URLs. A leitura e conclusão por família continuam necessárias; este relatório não as substitui.

As tentativas CUA de carregar a página TBG expiraram; não foi alegada inspeção visual do portal. A consulta dos JSONs oficiais resolveu a obtenção da listagem. A pesquisa cobre os registros disponíveis nesses canais na data de consulta e não prova inexistência absoluta de outros atos. INPE/FGV permanece no lote do Corretor. Nenhum arquivo do aluno foi alterado neste apoio.
