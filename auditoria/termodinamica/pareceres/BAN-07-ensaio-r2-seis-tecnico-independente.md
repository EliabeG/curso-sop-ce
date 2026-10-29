# BAN-07 r2 — auditoria independente preliminar do ensaio conjunto de seis itens

Data: 29/10/2026. Revisora: `/root/auditoria_av61_70`, agente automatizado independente do Corretor. **Resultado preliminar: ensaio estrutural e cenários reproduzidos sem falha; ajuste de consistência documental proposto para o inventário Markdown de CR06.** O stage é ensaio isolado, não produto entregue; este parecer não aprova produto futuro ou BAN-07, nem libera próximo ID.

## Versão e alcance

Ensaio do Corretor em `C:/Users/User/AppData/Local/Temp/ban07-r2-ensaio-1DJ4sQ`; resultado `auditoria/termodinamica/evidencias/BAN-07/ensaio-r2-seis/resultado-ensaio-r2-seis.json`, SHA-256 `973361cf97a72f8db4237f49dd8a4729909c8bbcae069fbfe82e876bd99f5534`. Script do Corretor `ensaiar-seis.mjs`, `81f34b36e92cfcbb047d5fcab1e7dd745ab02eb3c852327fa37822ae0b1e8880`. HTML do stage `80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0`; produto r1 base `de614a44d796ca04268915f89f502060db2772835c072036a990802eff912b80`.

As seis candidatas foram julgadas isoladamente nos pareceres `BAN-07-candidatas-av04-av31-av62-r2-independente.md` (`1059842bf92562ae98fe2fca6c15ab2fbee4b2975ad2578b97e5115bcb3af3b7`), `BAN-07-candidatas-cr06-cr26-cr45-r2-independente.md` (`1113b02ee2174f144b3720dcf3ae69d2e6e4f393e116c6727c6fb96287e2ca0d`) e `BAN-07-candidata-cr45-r2b-reconciliacao-cr06-independente.md` (`10070ab1d5d418717566794cdd010245541dd9116f1446f1a45ada447365ce3a`). O último substituiu para CR45 a variante inicialmente rejeitada e reconciliou a alteração do JSON de CR06. O resultado do ensaio menciona CR45-r2b ainda pendente de revisão como limite do momento da sua produção; a revisão posterior existe e está identificada aqui. Não se altera retrospectivamente a evidência histórica.

## Identidade, ciência herdada e reconstrução

Conferi diretamente os sete arquivos listados no resultado: cada arquivo no stage corresponde em SHA-256 ao valor registrado, e cada uma das sete cópias `ensaio-r2-seis/pacote-ensaio` corresponde ao mesmo valor. Arquivos externos à lista não ficam cobertos por essa conferência. Comparei o HTML do stage ao r1 usando extração própria dos artigos: **197 IDs e ordem preservados; somente os seis itens abaixo alterados; os 191 demais e o HTML fora de todos os artigos são idênticos**. Cada artigo alterado corresponde byte a byte à candidata isolada examinada:

| Artigo | SHA-256 da candidata e do artigo no stage |
|---|---|
| CR06 | `873e51481bc440721e17c233292535fdf7367670ba819c954987b7c263d8420b` |
| CR26 | `7c0ed44062bd50045076b2379e2449d24ef23da635ffe8a4d751ae37fb85303f` |
| CR45 r2b | `3b7e1013014ca169f810aba4973e03c1b98a8972c5648289a996b523d63ff448` |
| AV04 | `6ed8f664d46db759064d42ee073379bda2b8c1c7018ae3418d22774e14f72501` |
| AV31 | `2b2015e4ce0ec1bbea95c3da375ec316239d427f44454cfa43ca007c777fff7a` |
| AV62 | `795e127dad4361f30a6056f49479171b12c849388cdcdebde7fc09561be75ae7` |

Para os três CR, os suplementos são editoriais identificados antes da resposta; removê-los recupera integralmente os artigos r1, texto/figuras/chaves e comentários inclusos. O confronto FON-01 do ensaio corretamente se identifica como identidade, não nova conferência documental. As demonstrações científicas e suas condições vêm dos pareceres de candidatura acima, não são substituídas por igualdade de hashes.

## Inventário e complementos

Comparei JSON do inventário r1 e stage: **197 registros em ambos, exatamente seis registros alterados**, com hashes dos artigos correspondentes ao HTML. AV04/31/62 mudam apenas o hash do artigo em seus registros; CR06/26/45 também registram hipóteses editoriais e removem as respectivas hipóteses implícitas. Em CR06 atualiza-se a justificativa do nível para “A hipótese linear é explicitada em suplemento editorial do curso; basta reconhecer TX=a+bTY no modelo delimitado.” A fonte do inventário aponta para o snapshot do ensaio e o seu hash.

**Inconsistência a corrigir na reapresentação:** o `INVENTARIO_QUESTOES.md` do stage, linha 101, conserva a linha antiga de CR06: “A hipótese linear já é dada e basta reconhecer TX=a+bTY.” Embora a hipótese agora seja dada pelo suplemento no artigo, o resumo não reflete a justificativa revisada do JSON nem distingue sua autoria editorial; a seção adicionada no final diz que houve suplemento, mas a linha individual continua anterior. Sincronizar a linha CR06 com a justificativa atual do JSON (sem atribuir a hipótese à prova), regenerar os hashes afetados e reconferir a representação. O validador canônico não acusa essa divergência semântica.

FON-02 complementar: conferi 80 IDs, os 77 registros não atingidos são idênticos à fonte histórica; nos três atingidos o registro anterior permanece e cada suplemento está em campo novo identificado como editorial, com HTML, chave e hash do artigo do stage. A cópia da fonte FON-02 histórica é idêntica à original, com hash `4401889a58d96cad02ed12c703e180a645bf47b428fe4959d2decba5d8e2d9d1`; o complemento distingue `fonte_entregue` histórica e `fonte_reexaminada_BAN07` atual, sem declarar novo aceite FON-02. Cabe atualizar o índice/inventário efetivo de suplementos e submeter as dependências na entrega real; esse ensaio não transfere aceites anteriores automaticamente.

BAN-10 complementar: **197 registros, 194 não atingidos idênticos** à triagem histórica; CR06/26/45 são reavaliados sob modelos editoriais, com situação e motivo anteriores preservados no campo histórico e uso pontuável proposto sujeito à auditoria. Contagem soma 197. A fonte histórica é preservada por hash `b7e64034b3d1c6b31897948369c901a4a05648e53f30f91c6d553a7eb6d29147`. A exclusão dos nove estudos críticos não se presume apenas pelo JSON; o teste controlado abaixo inclui um deles.

Executei por chamada direta, somente leitura, o `validateInventory` canônico sobre o stage: **197 registros/197 artigos, 29 recursos, 1.261 links locais, zero erros/avisos**. Ele verifica estrutura e rastreabilidade, não coerência completa do Markdown, nem ciência ou aprendizagem.

## Digitais e progresso

Após inspecionar o script que escreve stage e resultado, **não o executei diretamente**. Em cópia temporária no mesmo diretório, adaptei a criação do stage para apontar ao stage existente, li baseline no produto r1, substituí a escrita do HTML por comparação com o stage e encerrei antes de qualquer escrita do inventário, complementos ou resultado. Reproduzi assim as verificações estruturais, digitais e testes controlados do Corretor sem gravar no stage ou evidências prévias; a cópia temporária foi removida. A reprodução passou e produziu:

| Artigo | Digital r1 → ensaio | Chave |
|---|---|---|
| AV04 | `8eaed3f8` → `cccc3a46` | D |
| AV31 | `4538caee` → `9230a05d` | E |
| AV62 | `ed91f6ac` → `e0ab3037` | D |
| CR06 | `01aa3697` → `d63393e4` | C |
| CR26 | `988714ce` → `1c9fcf05` | E |
| CR45 | `c084d78c` → `9475e2f5` | C |

No conjunto comparado, novas digitais não colidem com as 80 digitais r1 de cada banco nem com outra digital atual do mesmo banco. Históricos desconhecidos e versões futuras não foram integralmente enumerados.

A reprodução executou trechos reais de leitura, atualização, salvamento, avisos e filtro/placar em Node/VM com armazenamento e DOM mínimos simulados: em cada banco, três respostas antigas revisadas, um controle não revisado e, no CR, um estudo crítico. Verificou que antigas não preenchem novas, controle permanece, aviso surge, respostas novas são armazenadas com antigas, contexto recriado lê as novas, e um estudo crítico não entra no denominador simulado. O teste usa subconjunto de itens e substitui `mostrarResposta` por stub; **não é teste completo de interação DOM ou navegador, nem teste de localStorage pessoal, concorrência real ou falha de gravação**. A descrição do resultado do Corretor é evidência desses cenários, não comprova todos os comportamentos em produção.

## Critérios e decisão

| Critério | Resultado localizado |
|---|---|
| Seis candidatas, outras unidades e hashes | Correspondem aos fragmentos e à base r1; sete arquivos do stage e suas cópias conferidos. |
| Ciência e fontes oficiais | Análises herdadas dos pareceres isolados com identidade confirmada; FON-01 complementar é confronto de identidade, sem reabrir documentalmente os PDFs. |
| Inventário e representações | JSON e hashes dos seis coerentes; **linha Markdown CR06 a sincronizar** para refletir a justificativa e autoria editoriais do JSON. |
| Suplementos e triagem | Complementos provisórios preservam histórico e separam os três suplementos; revisão de dependências no produto real continua necessária. |
| Digitais e progresso | Reprodução controlada passou para os cenários descritos; teste real após aplicação segue necessário. |
| Produto futuro e próximo ID | Não examinados nem liberados; resultado é somente deste snapshot de ensaio. |

Reapresentar após sincronizar a linha de CR06 e atualizar hashes/evidência do stage ou da entrega efetiva; conferir também inventário, suplementos, identidade, histórico e navegador proporcionalmente à versão realmente aplicada. Este parecer não afirma piloto com estudantes, psicometria, auditoria integral de acessibilidade ou certificação externa. Não alterei stage, produto ou controle.
