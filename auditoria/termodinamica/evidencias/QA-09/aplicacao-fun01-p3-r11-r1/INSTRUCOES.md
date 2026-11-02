# QA-09 — preparo de aplicação FUN-01 P3 r10→r11

Data: 30/10/2026. Corretor automatizado `/root/next_examples`. **Preparação e ensaio em cópia; não foi executada no produto.** A candidata foi aprovada em `QA-09-fun01-p3-procedencia-candidata-auditoria-independente-20261030.md`, SHA-256 `e9ea9c3c8e1ec8b9d6fc5a7d6e19c4a8d541601d01ef1ba3c0d279160c9db511`, com reconciliação expressa r9→r10.

## Operação proposta

Um único parágrafo na solução de `fun01-e1-supercritico`, um dos 197 artigos, muda de “uma é calculada da outra” para “uma pode ser calculada a partir da outra, sem que isso determine como as medições foram obtidas”. A reconstrução literal exige 196 outros artigos byte a byte iguais e o artigo alvo igual exceto esse parágrafo; preserva enunciado, dados, solução remanescente e rubrica. No inventário oficial, a execução altera apenas `fonte.sha256`, `fonte.snapshot` e o campo `localizacao.sha256_artigo` do único item `fun01-e1-supercritico`; os outros 196 registros e todos os demais campos do alvo são idênticos. O Markdown do inventário recebe uma seção histórica de escopo localizado. O formulário não muda.

A base r10 exigida é aula SHA-256 `a8bed8a91a36a1c1f41cd75e3c1858fecb4e14a506e582ad1fdb186d275805e3`, formulário `01d5d79639cd17dfcaea38479019cf719e2601f5b35d446ab562e50d381fa5c9`, inventário QA-09 `3497cbf9ffcbe0a1e2eb84eeb9e34c0cfb6e0ed63a2747795bf75832454e2f6c`, inventário oficial JSON `2362fd386e0b7d1cb31b978a6c513114457e47bfccdda49f8017cba5cea87f88` e Markdown `3076d517ccf106ce414b708b04eaa74771da04256c03cfb45d39d34fd3177cc9`. Se qualquer base mudar, interromper e reconciliar; não reaplicar por semelhança. O executor também fixa os hashes da candidata, do parecer, do mapa e do gerador.

O gerador `inventariar-r11.mjs` é cópia do r10 com destino e proteção contra sobrescrita novos; não executa o gerador antigo. O mapa r10→r11 exige identidade de documentos, tipo, contexto e deslocamentos UTF-16; identifica explicitamente um ancestral com hash alterado, assegura unicidade de pares, compara 815 referências, 138 recursos, seis ativos e os 197 registros segregados, com alteração apenas do P3. A igualdade de hash não transfere automaticamente qualquer aceite anterior; o alcance de FUN-01 e BAN-02/07/08 precisa ser revalidado pelo Auditor.

## Ensaio e limites

Em uma cópia descartável desta árvore r10, o executor completou; produziu HTML hipotético SHA-256 `f76c39a3e1d8c349ebf0df72cc20a3ab21c68960c8451799bad90a9dcc4bd8c7`, artigo P3 `ab2d00867b0f11bc75810b84c74f8347e308fbf26b07f62de8fc11e0eb378c4d`, inventário r11 `720f2b9ace69ab8f07be685d5205040569cc72814f67d51d44786872469c07d7` e mapa `3c50f64d7f5a318edfc7544c2f2c628ca8789d45efdef8dcb08c88eac027cc3a`. O mapa teve 11.397 pares, 11.396 externos e um ancestral para conferência. Validador canônico: 197 artigos/itens, 29 recursos, 1.263 links, nenhum erro ou aviso. Em cópias separadas: execução sem `--apply`, destino já existente e fonte adulterada foram rejeitados; na última o HTML adulterado não foi sobrescrito. Detalhes em [resultado-ensaio.json](resultado-ensaio.json).

Após liberação da coordenação, executar somente na raiz e apenas se as bases e destinos ainda forem aqueles registrados:

```sh
node auditoria/termodinamica/evidencias/QA-09/aplicacao-fun01-p3-r11-r1/aplicar.mjs --apply
```

Antes da operação, o executor preserva a aula e os inventários oficiais anteriores e a nova aula em `resultado/`, e registra delta e verificações. **A operação não é transacional:** o produto e o inventário oficial são escritos antes da geração do mapa e da verificação final. Em falha ou interrupção após essas escritas, o estado pode ficar parcial; preservar snapshots, examinar hashes e reconciliar sem apagar provas. Nunca inferir que uma execução interrompida foi aprovada. O teste não é ensaio de navegador nem prova de aprendizagem. Solicita-se auditoria da versão efetiva, de todos os critérios afetados e, em particular, da revalidação FUN-01/BAN, antes de afirmar aceite localizado. QA-09 integral continua em correção.

## Hashes dos mecanismos

- `aplicar.mjs`: `847d752504cc9ce231acf7841ba282bb3bce3c7ec16ec257a212c551ea5f68de`.
- `mapear.py`: `d39bf28d456dc7402ec920ed9dd02b8c3c76e05007fa65ceefa0f7423d0a0133`.
- `../inventariar-r11.mjs`: `888779c0723d7f4340434ac9b120fa57211840eca7db1202bbca9e9929dc7f37`.
