# BAN-07 r2 — entrega do Corretor para auditoria

Data: 29/10/2026. Corretor: agente automatizado `/root/inspect_repo`. Aplicação dos seis ajustes liberada pelo coordenador após preparação e revisão de candidatas. **A versão está aguardando auditoria independente; esta entrega não aprova BAN-07 nem libera outro ID.**

AV04-E, AV31-B e AV62-B receberam distratores que explicitam respectivamente confusão entre incompressibilidade e isotermia, troca de calor sensível pela diferença de referência de fase, e inversão do diferencial de pressão. Os comentários correspondentes foram sincronizados; as chaves D, E e D permanecem. Em CR06, CR26 e CR45 há hipóteses editoriais claramente identificadas e acessíveis antes da tentativa: linearidade das duas escalas, balanço fechado com trocas definidas e convenção de caloria, e máquina cíclica de duas fontes com ambas as energias no mesmo ciclo. A transcrição, figuras e chaves oficiais C, E e C permanecem idênticas. As hipóteses não são atribuídas à banca.

O inventário JSON e seu índice foram sincronizados nos seis registros, inclusive a justificativa de CR06; os hashes da fonte e snapshot foram atualizados. O complemento FON-02 identifica as três hipóteses, a extensão de triagem BAN-10 reavalia exclusivamente os três CR e o confronto FON-01 registra a preservação do documento. Os registros históricos anteriores permanecem preservados. A revisão do efeito sobre esses aceites cabe ao Auditor; nenhum é presumido válido para a nova versão.

## Versão aplicada

| Arquivo | SHA-256 |
|---|---|
| `modulos/e1-termodinamica.html` | `80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0` |
| `auditoria/termodinamica/inventario/inventario-questoes.json` | `71ac07e042aa65675fc3d4b69d8d0ae11cb66df967d45e66b1a88f4f1350e074` |
| `auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md` | `35df191e2f7964adfb7b975668491e8ba39d983a5df93640a35d3d96ae142df8` |
| `auditoria/termodinamica/evidencias/BAN-07/e1-termodinamica.r2.html` | `80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0` |
| `auditoria/termodinamica/evidencias/BAN-07/revisao-fon02-complementar-r2.json` | `42ce5afe33e0481562c7673daaf25b359b8580b30276d9df75a1965adaa68399` |
| `auditoria/termodinamica/evidencias/BAN-07/triagem-ban10-complementar-r2.json` | `cc03d1fdf3a2401c93ea193ce99ed44d79c5a937d908e202ca03ee914b9d819d` |
| `auditoria/termodinamica/evidencias/BAN-07/confronto-fon01-cr-r2.json` | `d7fb0464f2c33701da8396a400c489dcde5096fc66de8c7d3e4d143ee7def9e4` |

O [manifesto r2](../evidencias/BAN-07/manifesto-r2.json), o [diário de aplicação](../evidencias/BAN-07/aplicacao-r2/diario-aplicacao-r2.json), a [verificação da aplicação](../evidencias/BAN-07/aplicacao-r2/verificacao-aplicacao-r2.json) e a [reprodução prévia em cópia](../evidencias/BAN-07/aplicacao-r2/resultado-preparacao-r2.json) registram entradas, hashes, backup e resultados. Os três arquivos substituídos têm cópias r1 em `evidencias/BAN-07/aplicacao-r2/antes-r2`. JS e registro não foram alterados. O controle não foi editado pelo Corretor.

## Verificações executadas

- Validador canônico no produto aplicado: 197 registros e 197 artigos, 29 recursos, 1.261 links, zero erros e avisos. Somente seis artigos mudaram; texto fora dos artigos, chaves, ordem e IDs permaneceram iguais. Remover o parágrafo editorial de cada CR reproduz o artigo r1 byte a byte.
- JSON e Markdown foram comparados para os seis itens: competências, nível, número de etapas e justificativa coincidem. A descrição de CR06 atribui a condição linear ao suplemento editorial, não ao original.
- Funções reais de digitais, armazenamento e placar em Node/VM com DOM e armazenamento simulados, executadas antes da aplicação sobre cópia byte a byte igual ao pacote aplicado. As digitais mudam AV04 `8eaed3f8`→`cccc3a46`, AV31 `4538caee`→`9230a05d`, AV62 `ed91f6ac`→`e0ab3037`, CR06 `01aa3697`→`d63393e4`, CR26 `988714ce`→`1c9fcf05` e CR45 `c084d78c`→`9475e2f5`. Não houve colisão com as 80 digitais r1 ou as 80 atuais de cada banco. Histórico antigo foi preservado sem migrar letras, aviso e recarga funcionaram no modelo simulado, e um estudo crítico permaneceu fora da pontuação.
- FON-02 e BAN-10 históricos foram conferidos por hash e permanecem intactos. Os testes não cobrem históricos desconhecidos, navegador real, armazenamento pessoal, falhas de escrita, estudantes ou evidência psicométrica. O confronto FON-01 não constituiu nova leitura dos PDFs nesta rodada.

Solicita-se ao Auditor independente verificar a versão aplicada, os seis artigos, o inventário, os complementos e o impacto de identidade e pontuação; emitir parecer para os hashes acima antes de qualquer avanço de fila. Não se declarou conclusão de BAN-08 nem classificação global do curso.
