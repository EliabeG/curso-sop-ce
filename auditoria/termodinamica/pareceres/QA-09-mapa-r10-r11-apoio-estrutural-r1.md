# QA-09 — apoio estrutural ao mapa r10→r11

Data: 30/10/2026. Apoio: agente automatizado `/root/next_graphics`. **Resultado estrutural: verificações abaixo passaram.** Este agente criou a candidata P3, embora outro agente a tenha aplicado. Portanto, este documento é **apoio técnico de identidade e reconstrução, não uma auditoria independente da própria correção**; a decisão científica e a revalidação dos aceites anteriores pertencem ao Auditor principal distinto. Não encerra QA-09 nem libera outro ID.

## Fotografias

Aula r10 `a8bed8a91a36a1c1f41cd75e3c1858fecb4e14a506e582ad1fdb186d275805e3`; r11 `f76c39a3e1d8c349ebf0df72cc20a3ab21c68960c8451799bad90a9dcc4bd8c7`. Formulário preservado SHA-256 `01d5d79639cd17dfcaea38479019cf719e2601f5b35d446ab562e50d381fa5c9`. Inventários estruturais r10 `3497cbf9ffcbe0a1e2eb84eeb9e34c0cfb6e0ed63a2747795bf75832454e2f6c` e r11 `720f2b9ace69ab8f07be685d5205040569cc72814f67d51d44786872469c07d7`; mapa `3c50f64d7f5a318edfc7544c2f2c628ca8789d45efdef8dcb08c88eac027cc3a`.

## Reconstrução, 197 artigos e inventário oficial

`evidencias/QA-09/apoio-mapa-r10-r11-r1/reconstruir.mjs`, SHA-256 `0ba1d52a22840d365e426a91da8f1b858700e17d6a927a4ee09b22518274cc50`, lê as fotografias e reconstrói em memória a aula r11 por substituição única do parágrafo, confirmando identidade, posição e hashes. A reconstrução e a fotografia posterior são idênticas ao HTML efetivo byte a byte. O formulário permanece com o hash informado.

Os 197 artigos mantêm IDs e ordem; os 196 não alvo são idênticos. O alvo `fun01-e1-supercritico` mudou apenas pela substituição literal, incluindo preservação dos demais trechos do artigo, enunciado, solução restante e rubrica. Seu hash passou de `2fad0e042fb945eb44d0f2abe2c4e64322434195395fa4e5c084f17854f432a7` a `ab2d00867b0f11bc75810b84c74f8347e308fbf26b07f62de8fc11e0eb378c4d`. No inventário oficial, comparando os registros, apenas `localizacao.sha256_artigo` do P3 mudou; os outros 196 registros e os campos restantes do P3 são iguais. A chave de topo `fonte` atualiza a fotografia e o SHA. O validador canônico retornou `ok=true`: 197 artigos/registros, 29 recursos e 1.263 links, sem erros ou avisos. Isso confirma estrutura, não mérito científico nem experiência em navegador.

## Mapa, referências e recursos

`evidencias/QA-09/apoio-mapa-r10-r11-r1/mapa.py`, SHA-256 `7ca83cddbd9e3656faa35815f3d59afcef4b8932febfb42a52072e8681773f40`, verificou sem gravação os hashes dos dois inventários e do mapa, a bijeção e os campos documento/tipo/tag/seção/âncora, posições e deslocamentos de todos os 11.397 pares. Destes, 11.396 têm hashes iguais; o único hash divergente é a seção ancestral `fun01-estado-equilibrio`, cujo fragmento contém o artigo editado. O artigo próprio é segregado dos objetos QA-09 e sua mudança foi conferida separadamente acima.

Os 815 registros de referências mantêm valores e textos; suas posições seguem o deslocamento calculado. Os 138 recursos mantêm referência e caminho: 105 registros que apontam para o HTML modificado têm o hash atualizado, e os demais preservam seus hashes. Os seis ativos específicos permanecem idênticos. O inventário de artigos excluídos mantém 197 IDs e altera somente o hash do P3. A identidade de um recurso, posição ou hash não comprova automaticamente validade científica ou herança de aceite.

| Critério deste apoio estrutural | Resultado |
|---|---|
| Uma substituição e fotografias | Passou: reconstrução byte a byte. |
| Artigos, inventário e formulário | Passou para 196 artigos não alvo, delta único do P3, metadados do alvo e formulário. |
| Mapa, referências, recursos e ativos | Passou para as contagens e limites acima; ancestral explicitado. |
| Independência científica e aceites anteriores | Não objeto deste apoio: autoria prévia da candidata declarada; decisão cabe a Auditor distinto. |
| QA-09 integral e próximo ID | Não atendido; revisão completa continua pendente. |

A alteração do artigo exige revalidação delimitada FUN-01 e BAN-02/BAN-07/BAN-08 pelo Auditor principal; referências, históricos e ledger não transferem aceites automaticamente. Não houve navegador real, leitor de tela, aluno, revisão humana ou certificação externa neste apoio.
