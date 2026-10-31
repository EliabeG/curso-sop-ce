# QA-09 — apoio independente ao mapa r12→r13

Data: 30/10/2026. Auditor de apoio: agente automatizado `/root/next_graphics`, distinto do Corretor da aplicação. **APROVADO no alcance estrutural e de identidade abaixo.** Este agente revisou anteriormente as candidatas das fichas 88/99; o Auditor principal distinto deve julgar o conteúdo efetivamente aplicado e a revalidação dos aceites. Este apoio não encerra QA-09 nem libera outro ID.

## Fotografia e reconstrução

Aula r12 `f76c39a3e1d8c349ebf0df72cc20a3ab21c68960c8451799bad90a9dcc4bd8c7`, r13 `f19000a7ddb1f3552b9633b0efec266fb3f6c5e5065808505a2f65b2005aefbc`; formulário r12 `6857fd83e0b2e49c804903cff1dea4128a665ab22eb27bac4ab15d6c557ff756`, r13 `5f3f31a4801f96a2b78b40c75d37392f6b16d264901ac313ac00458901970285`. Inventário r12 `457a56300aab8f612ebb7f136c7c2f62520abb49c005c209a238925179248d0e`, r13 `0df99b79bcc2350581fcdded72435d30d07858de237a549e6228ca73682f8d9b`; mapa `3f198c327e0bbb5d28c116fa5b1d655224e6ad9e24505556397d6c3586169671`.

`evidencias/QA-09/auditoria-mapa-r12-r13-independente-r1/reconstruir.mjs`, SHA-256 `512039b77c59711b15daa4f522aa63fb662e63301fdc4c4822aa9a0fc8a27e92`, reconstrói as duas páginas em memória a partir das fotografias r12 e dos três fragmentos reais, conferindo unicidade, hashes e posições. O resultado e as fotografias posteriores são idênticos às fontes efetivas r13 byte a byte. Os 197 artigos da aula mantêm IDs, ordem e conteúdo; os 197 registros individuais do inventário oficial permanecem idênticos e somente a chave de topo `fonte` mudou. Das 100 fichas, 98 são idênticas; somente `formula-intermediaria` e `formula-geracao` mudaram. Os 734 MathML da aula e 191 do formulário são idênticos como fragmentos.

O validador canônico retornou `ok=true`, 197 artigos/registros, 29 recursos e 1.263 links locais, nenhum erro ou aviso. A verificação é estrutural, não é ensaio de navegador nem certificação científica.

## Mapa, referência externa e recursos

`evidencias/QA-09/auditoria-mapa-r12-r13-independente-r1/mapa.py`, SHA-256 `ef558bed3978d9c3280b34d1b6689e76ea197f2a5ba46b52b154e8a5049195e6`, verificou bijeção, hashes, documento/tipo/tag/seção/âncora, posições externas e ordem/contexto dos nós internos. Dos 11.397 pares, 11.320 são externos (11.317 hashes iguais, três seções ancestrais mudadas: `fontes`, `compressores`, `transferencia`); 77 são internos (71 hashes iguais, seis alterados: ficha, atributos e parágrafo em cada ficha alvo). A associação interna por sequência/contexto não é aprovação semântica automática.

Das 815 referências, uma mudou: o PDF antes indicado do EnergyPlus para `https://bigladdersoftware.com/epx/docs/24-1/engineering-reference/carbon-dioxide-predictor-corrector.html`. O endereço foi aberto em 30/10/2026 e apresenta a Engineering Reference EnergyPlus 24.1, tópico Carbon Dioxide Predictor-Corrector e balanço transiente; a verificação de acesso não substitui confronto científico integral nem verifica numeração do antigo PDF. As demais referências mantêm valor e texto na ordem documentada. Os 138 recursos mantêm caminho e referência; hashes de 105 registros apontados para a aula e três para o formulário são atualizados, demais hashes preservados. Os seis ativos específicos e os 197 artigos excluídos do inventário estrutural permanecem iguais.

| Critério deste apoio | Resultado |
|---|---|
| Reconstrução, artigos e inventário | Passou: três substituições, 197 artigos/registros preservados. |
| Fichas e MathML | Passou: 98 não alvo e 734+191 MathML idênticos. |
| 11.397 pares, 815 referências, 138 recursos e seis ativos | Passou para identidade e contexto estrutural, com um link externo explicitamente alterado. |
| Ciência dos textos, FOR-01 integral e QA-09 | Não decididos por este apoio; continuam sob revisão principal e pelas etapas restantes. |

Qualquer revalidação de FOR-01 ou de pareceres prévios deve verificar contexto e dependências, sem transportar aceite por hash isolado. Não houve teste em navegador, leitor de tela, aluno, revisão humana ou certificação externa nesta análise.
