# QA-09 — apoio independente ao mapa r11→r12

Data: 30/10/2026. Auditor de apoio: agente automatizado `/root/next_graphics`, distinto do Corretor da aplicação. **APROVADO no alcance estrutural e de identidade abaixo.** O Auditor principal deve examinar a suficiência científica das cinco alterações e a revalidação delimitada; esta análise não encerra QA-09 nem libera outro ID.

## Fotografias e reconstrução

Aula r11/r12 idêntica, SHA-256 `f76c39a3e1d8c349ebf0df72cc20a3ab21c68960c8451799bad90a9dcc4bd8c7`; formulário r11 `01d5d79639cd17dfcaea38479019cf719e2601f5b35d446ab562e50d381fa5c9`, r12 `6857fd83e0b2e49c804903cff1dea4128a665ab22eb27bac4ab15d6c557ff756`. Inventários r11 `720f2b9ace69ab8f07be685d5205040569cc72814f67d51d44786872469c07d7` e r12 `457a56300aab8f612ebb7f136c7c2f62520abb49c005c209a238925179248d0e`; mapa `1c67bdda8f5996c6a230e4556277dbbfac270e64ec5b2ac0cabccdee4b3680ef`.

`evidencias/QA-09/auditoria-mapa-r11-r12-independente-r1/reconstruir.mjs`, SHA-256 `29ea3f598afc639625c61006fcf8ca953d15eaf9601100e7f3584817a7006bbc`, reconstrói r12 em memória a partir da fotografia anterior e dos cinco fragmentos reais, conferindo unicidade, hashes, deslocamentos e as fotografias posteriores. O resultado reproduz o formulário efetivo byte a byte; a aula anterior, atual e fotografia posterior são idênticas. Os 197 artigos e sua ordem permanecem na aula. Das 100 fichas, 95 permanecem idênticas; as cinco alteradas são `formula-equilibrio-mistura`, `formula-recipiente-mistura`, `formula-fase-calorimetria`, `formula-co2-acumulacao` e `formula-co2-vazao`. Os 191 fragmentos MathML do formulário são idênticos. O inventário oficial JSON SHA-256 `f2605176763a61832417506517373a16736717d5cc23de7494e901322c394856` corresponde ao registrado na entrega r11; o Markdown `1e5251583294cc3a497bba6693671e6f996f624012c218121c66e5866380bef9` também. O validador canônico retornou `ok=true`, 197 artigos/registros, 29 recursos e 1.263 links, sem erros nem avisos. Esses testes não comprovam mérito científico ou renderização.

## Mapa e dependências

`evidencias/QA-09/auditoria-mapa-r11-r12-independente-r1/mapa.py`, SHA-256 `3afbe287b4928c8b02903f4aed457af8c31a28b4c6d6177113b32972658ca591`, confrontou sem gravação as duas fotografias e todos os 11.397 pares: documento, tipo, tag, seção, âncora, hashes e deslocamentos externos, além de ordem e contexto dos nós internos. Há 11.238 pares externos (11.236 hashes iguais; dois alterados, seções ancestrais `calorimetria` e `escoamento`) e 159 internos (144 hashes iguais, 15 alterados: ficha, atributos e parágrafo em cada uma das cinco fichas). As correspondências internas são estruturais; o Auditor principal deve verificar o significado dos textos e não herdar aceites por igualdade isolada.

As 815 referências mantêm os mesmos valores e textos, e os fragmentos HTML dos links são idênticos entre versões, inclusive dentro das fichas. Dos 138 registros de recursos, três que apontam ao formulário têm hash atualizado; os demais permanecem iguais. Os seis ativos específicos e os 197 registros de artigos excluídos no inventário estrutural permanecem iguais. Os vínculos e a identidade de hashes não demonstram, por si, que o destino é didaticamente suficiente nem que a página renderiza corretamente.

| Critério de apoio | Resultado |
|---|---|
| Fotografias e cinco substituições | Atendido: reconstrução byte a byte. |
| 197 artigos, 95 fichas e 191 MathML | Atendido no escopo estrutural; cinco fichas intencionalmente alteradas. |
| 11.397 pares, inclusive 159 internos | Atendido para identidade/contexto e ordem; exame semântico segue com Auditor principal. |
| 815 referências, 138 recursos e seis ativos | Atendido na extensão descrita; sem revisão integral do conteúdo dos destinos. |
| Ciência, FOR-01 integral e QA-09 | Não decididos por este apoio; requerem parecer principal e demais etapas. |

Ao revalidar FOR-01 ou outros pareceres, examinar explicitamente conteúdo e dependências efetivamente afetados; correspondência de posição ou hash não transfere aceites automaticamente. Não houve navegador real, leitor de tela, teste com estudantes, revisão humana ou certificação externa nesta análise.
