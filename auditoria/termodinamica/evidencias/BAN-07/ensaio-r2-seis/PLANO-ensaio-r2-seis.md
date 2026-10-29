# BAN-07 r2 — ensaio conjunto e plano para reapresentação

**Estado:** pacote de ensaio isolado de seis candidatas; não aplicado ao produto e não aprovado como entrega. As aprovações citadas referem-se a fragmentos isolados e não aprovam o pacote integrado. Somente o coordenador pode autorizar a aplicação após a revisão deste pacote.

## Escopo e versões

O ensaio usa os seis fragmentos e respectivos JSONs com os hashes examinados nos pareceres independentes:

| Artigo | SHA-256 do fragmento candidato | Decisão e limite |
|---|---|---|
| AV04 | `6ed8f664d46db759064d42ee073379bda2b8c1c7018ae3418d22774e14f72501` | AV04-E, chave D; aprovação isolada no parecer AV04/31/62. |
| AV31 | `2b2015e4ce0ec1bbea95c3da375ec316239d427f44454cfa43ca007c777fff7a` | AV31-B, chave E; aprovação isolada no mesmo parecer. |
| AV62 | `795e127dad4361f30a6056f49479171b12c849388cdcdebde7fc09561be75ae7` | AV62-B, chave D; aprovação isolada no mesmo parecer. |
| CR06 | `873e51481bc440721e17c233292535fdf7367670ba819c954987b7c263d8420b` | Suplemento editorial antes da tentativa, chave oficial C; JSON reconciliado e aprovação isolada no complemento CR45/CR06. |
| CR26 | `7c0ed44062bd50045076b2379e2449d24ef23da635ffe8a4d751ae37fb85303f` | Suplemento editorial antes da tentativa, chave oficial E; aprovação isolada no parecer CR06/26/45. |
| CR45 r2b | `3b7e1013014ca169f810aba4973e03c1b98a8972c5648289a996b523d63ff448` | Suplemento editorial com valores no mesmo ciclo, chave oficial C; aprovação isolada no complemento CR45/CR06. |

As decisões são [AV04/31/62](../../../pareceres/BAN-07-candidatas-av04-av31-av62-r2-independente.md), [CR06/26/45](../../../pareceres/BAN-07-candidatas-cr06-cr26-cr45-r2-independente.md), [adjudicação CR45](../../../pareceres/BAN-07-decisao-candidata-cr45-r2.md) e [CR45 r2b e reconciliação CR06](../../../pareceres/BAN-07-candidata-cr45-r2b-reconciliacao-cr06-independente.md). O [resultado](resultado-ensaio-r2-seis.json) registra também os seis hashes dos JSONs; a ferramenta recusa qualquer divergência. AV69 não integra o escopo. Se uma redação, decisão ou hipótese mudar, regenerar e reapresentar o conjunto: os hashes não se transferem automaticamente.

## Artefatos do ensaio

A [ferramenta](ensaiar-seis.mjs) verifica hashes do r1 e das seis candidatas, cria cópia completa isolada na pasta temporária do sistema, substitui apenas esses artigos e produz ali inventário, snapshot e relatórios complementares. Na raiz do projeto: `node auditoria/termodinamica/evidencias/BAN-07/ensaio-r2-seis/ensaiar-seis.mjs`. Cada execução cria uma cópia temporária nova e registra seu caminho no resultado; não remove as cópias anteriores. Ela não escreve produto nem controle reais. SHA-256 da ferramenta: `81f34b36e92cfcbb047d5fcab1e7dd745ab02eb3c852327fa37822ae0b1e8880`.

O [pacote reduzido](pacote-ensaio/) contém os sete arquivos gerados para inspeção. A cópia completa usada na execução está identificada no resultado; o pacote reduzido não inclui todas as dependências dos links e não é autocontido. Os documentos levam “ensaio” no caminho e no texto, logo precisam ser reconstruídos para a versão final e **não devem ser promovidos diretamente**.

| Arquivo relativo à raiz da cópia | SHA-256 |
|---|---|
| `modulos/e1-termodinamica.html` | `80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0` |
| `auditoria/termodinamica/inventario/inventario-questoes.json` | `5e9c2baae9429accd786b3ceabc3210d6e0404c22e4e07f0f3c68ddeff3f4348` |
| `auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md` | `9de922270b663df28a085b2d9ad1515ae93d500b903cd2f7c4d9abf388943ba7` |
| `auditoria/termodinamica/evidencias/BAN-07/e1-termodinamica.r2-seis-ensaio.html` | `80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0` |
| `auditoria/termodinamica/evidencias/BAN-07/revisao-fon02-complementar-r2-ensaio.json` | `e9537a95c63dad3402c51f6af3128c5b9d79781fa90cbd82a7a7f506117cacf0` |
| `auditoria/termodinamica/evidencias/BAN-07/triagem-ban10-complementar-r2-ensaio.json` | `760b47051f87534963079900ac8c51effab09527c451dce3a90be78f77768487` |
| `auditoria/termodinamica/evidencias/BAN-07/confronto-fon01-cr-r2-ensaio.json` | `d7fb0464f2c33701da8396a400c489dcde5096fc66de8c7d3e4d143ee7def9e4` |

O relatório de FON-02 é uma extensão em arquivo novo de 80 registros: somente três registros recebem suplemento editorial adicional; preserva origem e atribuição anteriores. A triagem BAN-10 é uma extensão nova em que apenas CR06/26/45 passam a modelo editorial com pontuação sujeita a auditoria; as outras 194 classificações permanecem históricas, não foram reauditadas. O registro FON-01 prova por comparação que remover cada parágrafo editorial recupera todo o artigo r1, mas não substitui nova leitura documental de PDFs. Os arquivos históricos originais de FON-02 e BAN-10 permanecem sem alteração. A fonte editorial deve ser distinguida da prova oficial, com hipóteses atualizadas no inventário.

## Verificações realizadas e seus limites

- Apenas seis dos 197 artigos mudaram; ordem, IDs, chaves e todo o conteúdo fora dos artigos foram preservados. Em cada CR, remover o parágrafo editorial reproduz o artigo r1 byte a byte, inclusive transcrição, figura, alternativas, chave e solução.
- O validador canônico verificou 197 registros e artigos, 29 recursos e 1.261 links locais, sem erro nem aviso. Seis hashes de artigo, fonte, snapshot e hipóteses editoriais dos três CR foram atualizados na cópia; demais registros permanecem idênticos. A classificação de CR06 foi redigida para atribuir explicitamente a condição ao suplemento.
- Digitais calculadas pelas funções reais em VM: AV04 `8eaed3f8` → `cccc3a46`; AV31 `4538caee` → `9230a05d`; AV62 `ed91f6ac` → `e0ab3037`; CR06 `01aa3697` → `d63393e4`; CR26 `988714ce` → `1c9fcf05`; CR45 `c084d78c` → `9475e2f5`. Cada digital nova é única entre os 80 itens atuais do próprio banco e não coincide com as 80 digitais r1 desse banco. Históricos desconhecidos não foram examinados.
- Funções reais de armazenamento e placar dos dois bancos, executadas em Node/VM com DOM e `localStorage` simulados: versões antigas são preservadas e não contam como respostas novas, item estável permanece, aviso é exibido, respostas novas sobrevivem à recarga do contexto e uma marcação de estudo crítico fica fora da nota. Não é teste em navegador real, com armazenamento pessoal, com estudantes, nem teste de falha de gravação.
- Os cinco arquivos de produto r1 e o controle foram conferidos ao final; os relatórios históricos FON-02 e BAN-10 também não foram modificados. O resultado SHA-256 é `973361cf97a72f8db4237f49dd8a4729909c8bbcae069fbfe82e876bd99f5534`.

## Procedimento proposto após revisão e liberação

1. O Auditor examina os sete arquivos de ensaio, as seis versões literais, o resultado e os efeitos FON-01/02, BAN-02/10 e BAN-07. Resolve eventuais ajustes e verifica se o tratamento pontuável sob suplementos editoriais é aceitável. Não se presume que qualquer aceite anterior se aplique a um novo hash.
2. Após decisão e liberação do coordenador, conferir novamente controle, hashes de r1, candidatos, decisões e dependências. Em caso de divergência ou rejeição, interromper a promoção, corrigir a candidata em versão separada e regenerar todo o ensaio e a auditoria afetada.
3. Construir em nova cópia o pacote definitivo: manter os seis fragmentos aceitos; criar snapshot r2 com nome definitivo, registrar seus hashes e substituir nomes/declarações de ensaio no inventário, índice e novos relatórios. Preservar todos os pareceres, triagens e evidências r1/FON-02/BAN-10 históricos; registrar a origem e a distinção editorial de cada hipótese. Revalidar os sete artefatos e obter novo manifesto de hashes; esse pacote final precisa ser examinado antes da aplicação.
4. Com autorização para aplicação do pacote específico, preservar cópia dos arquivos atuais, aplicar os arquivos finais de maneira verificável e conferir hashes, deltas e rollback. Não trocar JS ou registro se o conjunto validado não exigir isso. O coordenador controla o arquivo de controle.
5. No produto efetivamente aplicado, repetir validador, inspeção de fontes, chaves e suplementos, colisões e testes em navegador com armazenamento de teste: histórico antigo preservado sem migração, aviso, placar, estudos críticos, nova resposta e recarga. Encaminhar produto e evidências efetivos ao Auditor independente. A aprovação isolada de cada fragmento não substitui o parecer integrado e não libera o próximo ID.
