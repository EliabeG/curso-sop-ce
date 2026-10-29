# BAN-07 — parecer independente da rodada 2

Data: 29/10/2026. Auditor: agente automatizado `/root/auditoria_av71_80`, independente do Corretor `/root/inspect_repo`. **Veredito: AJUSTES_OBRIGATORIOS.** Os seis artigos aplicados atendem às correções científicas examinadas, mas dois campos do inventário de CR06 não refletem a hipótese editorial que sustenta seu raciocínio. BAN-07 r2 e a revalidação integral de BAN-02 para esta versão não estão aprovados. **O próximo ID não está liberado.**

## Critério e versão examinada

BAN-07 exige dados suficientes, consistência física, comando, unidades, restrições e resposta única, demonstração do gabarito, justificativa dos distratores e detecção de equivalências após arredondamento. Em estudo crítico sem pontuação, o exame distingue a afirmação oficial, sua chave documental e a interpretação técnica, sem forçar unicidade. O Protocolo AAA requer versão identificável, revisão independente, coerência dos registros afetados e reexame até que todos os critérios aplicáveis estejam atendidos. O trabalho aqui não fecha BAN-08, DID-07, UX-04, BAN-09 ou o curso inteiro.

[Entrega r2](../entregas/BAN-07-r2.md), SHA-256 `c9b19afcf3c3ddb0f8033b6fd13090d31750d60e31c68751804159e5c9b44bee`; [manifesto r2](../evidencias/BAN-07/manifesto-r2.json), SHA-256 `471b222e81c17a257a008a38671eb617498720f0add1f1baf7343baa0b0b413d`.

| Arquivo aplicado ou evidência | SHA-256 |
|---|---|
| `modulos/e1-termodinamica.html` | `80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0` |
| `auditoria/termodinamica/inventario/inventario-questoes.json` | `71ac07e042aa65675fc3d4b69d8d0ae11cb66df967d45e66b1a88f4f1350e074` |
| `auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md` | `35df191e2f7964adfb7b975668491e8ba39d983a5df93640a35d3d96ae142df8` |
| `evidencias/BAN-07/e1-termodinamica.r2.html` | `80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0` |
| `evidencias/BAN-07/revisao-fon02-complementar-r2.json` | `42ce5afe33e0481562c7673daaf25b359b8580b30276d9df75a1965adaa68399` |
| `evidencias/BAN-07/triagem-ban10-complementar-r2.json` | `cc03d1fdf3a2401c93ea193ce99ed44d79c5a937d908e202ca03ee914b9d819d` |
| `evidencias/BAN-07/confronto-fon01-cr-r2.json` | `d7fb0464f2c33701da8396a400c489dcde5096fc66de8c7d3e4d143ee7def9e4` |

O [exame científico próprio dos seis artigos e complementos](BAN-07-r2-cientifico-independente.md), SHA-256 `a803a1a25575bba920eea8960186e73cc4cdc4878a23cfac0cc199f0ef592abf`, registra as 15 opções AV, as seis marcações CR, contas, fontes e limites. Chaves e propostas já eram conhecidas; não se reivindica cegamento ou evidência psicométrica.

## Resultado das correções científicas

| Item | Decisão sobre o artigo r2 | Fundamento no alcance examinado |
|---|---|---|
| AV04 | Atendido; D única | Incompressibilidade aproxima v como constante; E agora confunde isotermia com aquela condição, e comentário refuta a equivalência. A/B/C também são falsas. |
| AV31 | Atendido; E única | A diferença PCS/PCI é a condição de fase da água na mesma referência; B agora confunde essa diferença com calor sensível por referência térmica distinta. A/C/D são falsas. |
| AV62 | Atendido; D única | Na admissão normal, pressão da linha de sucção supera a da câmara; B agora inverte essa diferença, com comentário coerente. A/C/E são falsas. |
| CR06 | Atendido no artigo; C sob suplemento | Escalas X e Y lineares e variáveis na altura fornecem relação afim. A condição prévia é rotulada editorial; E nega o resultado. O inventário tem a pendência abaixo. |
| CR26 | Atendido; E sob suplemento | Sistema fechado, trocas definidas e kcal termoquímica dão ΔU≈1.304,4 kcal, inferior a 5.500. A hipótese é editorial, distinta do texto oficial. |
| CR45 | Atendido; C sob suplemento | Duas fontes e 900/90 kJ no mesmo ciclo dão η=90%, superior ao limite de Carnot ≈59,99%; E nega a impossibilidade nesse modelo. |

O conteúdo oficial e as chaves são preservados: ao retirar o único parágrafo editorial de cada CR aplicado, reconstruí seu artigo r1 integralmente. Essa prova de identidade não atribui as hipóteses à banca nem constitui nova pesquisa de atos oficiais. CR06/26/45 permanecem pontuáveis apenas como versões explicitamente suplementadas; as frases oficiais isoladas não recebem, por esta decisão, uma validade universal ou anulação.

## Herança r1, preservação e dependências

Comparei os 197 artigos r1 e r2 a partir dos IDs e hashes da cobertura r1: somente os seis listados mudaram; os outros 191 artigos e o HTML fora dos artigos são idênticos. Substituir os seis artigos novos pelos antigos reconstrói a r1 inteira. As decisões científicas dos 191 são herdadas **por identidade e alcance**, com autoria individual conforme o [adendo r1](BAN-07-r1-adendo-cobertura.md); não se atribuem suas soluções a esta execução. Os nove estudos críticos CR04/09/24/34/35/39/62/79/80 mantêm seus artigos e marcadores; sua análise é documental e sem nota, e não se impõe unicidade ao original.

**FON-01:** a reconstrução dos três artigos e a conferência de fontes/figuras do apoio técnico preservam o alcance documental anterior nas partes afetadas. A leitura visual dos documentos originais pertence às evidências e pareceres FON-01, salvo quando o apoio identifica exame próprio; esta revisão não realizou nova pesquisa integral ou reabertura geral dos 80 documentos.

**FON-02:** comparei os 80 registros complementares com a matriz histórica aprovada: os 77 demais são idênticos e, retirando somente o campo novo de cada um dos três atingidos, os três registros também reproduzem os históricos. Os campos novos identificam hipóteses editoriais, posição antes da marcação, chave e hash do artigo r2. A prova e a justificação científica de cada condição constam do exame dos seis. Considero **atendidos os critérios de identificação, origem e separação dos três suplementos neste alcance**, sem reescrever o aceite histórico ou declarar nova aprovação integral de FON-02.

**BAN-10:** a triagem complementar preserva 194 registros históricos e reavalia CR06/26/45 com motivação anterior, modelo editorial e uso proposto. Confrontei as três hipóteses e os juízos C/E no produto aplicado e considero **sustentada a pontuação dos três itens suplementados**; a redação oficial sozinha continua merecendo as ressalvas da r1. Os 194 campos restantes são históricos; sua cópia não é nova triagem integral nem identidade automática com o HTML atual. A herança das demais decisões repousa nos pareceres r1 e na preservação acima, não num hash antigo apresentado como atual. Com os três pontuáveis e os nove críticos preservados, o desenho estático corresponde a 71/9; comportamento dinâmico deve ser avaliado pelos testes explicitados abaixo.

**BAN-02:** seis registros do JSON mudaram e os 191 restantes foram preservados; as três hipóteses editoriais e hashes foram registrados, e o resumo Markdown de CR06 foi sincronizado com a justificativa do nível. Isso não resolve a inconsistência dos dois campos de raciocínio e competência descrita a seguir. Manter o aceite histórico não equivale a aprovar o inventário r2 incompleto.

## Ajuste obrigatório R2-A — inventário de CR06

Em `auditoria/termodinamica/inventario/inventario-questoes.json`, os campos `raciocinio.etapas` e `vinculo_competencias.alcance` de `cr-e1-06` ainda descrevem a tarefa como “Relacionar dilatação constante com transformação afim entre escalas”. Essa caracterização omite a condição editorial de que **ambas as escalas sejam lineares na altura da coluna**. A simples dilatação linear do mercúrio não determina a linearidade de duas escalas arbitrárias; essa era precisamente a insuficiência corrigida no artigo. O novo campo `hipoteses.explicitadas`, a justificativa do nível e a linha do resumo identificam corretamente a origem editorial, mas não eliminam a leitura incompleta desses dois outros campos.

**Reapresentação necessária:**

1. Atualizar os dois campos para descrever a inferência de relação afim sob linearidade das duas escalas explicitada **no suplemento do curso**, sem atribuí-la ao original. Confrontar categoria, nível, número de etapas, vínculo C08 e resumo; preservá-los se continuarem corretos.
2. Entregar diff e novos hashes do inventário, manifesto e representações alteradas, além dos hashes dos arquivos preservados. Conservar texto oficial, figura, suplemento aplicado, chave e histórico documental; se o HTML permanecer byte a byte idêntico, sua cópia r2 pode continuar sendo o snapshot da fonte.
3. Reexecutar o validador canônico e conferir semanticamente os campos, o resumo e os vínculos; demonstrar preservação dos demais registros e evidências na extensão da alteração. O Auditor examinará a versão reapresentada e a aplicabilidade das evidências técnicas por identidade, sem presumir aceite automático.

O validador executado por mim na r2 retornou **197 registros e artigos, 29 recursos, 1.261 links locais, zero erros e avisos**. Ele não avalia a coerência semântica dos dois campos, razão pela qual seu resultado não afasta R2-A.

## Verificação técnica independente e limites

Li [BAN-07-r2-tecnico-independente.md](BAN-07-r2-tecnico-independente.md), SHA-256 `a3456a063df37be43b9a14394ed8822ee4c884ee64b53447cb3b06cf45ed68af`, e confirmei seu hash. A revisão pertence à agente automatizada independente `/root/auditoria_av61_70`, não ao Corretor nem a mim. Ela conferiu os 12 arquivos enumerados, três backups e fontes/documentos pertinentes aos três CR; reproduziu verificadores do Corretor em cópia temporária sem gravar os originais e o validador canônico. Também identificou R2-A, aqui confirmado.

Na reprodução técnica, as seis digitais mudaram e não colidiram com as 80 anteriores ou atuais no mesmo banco examinado. Em Node/VM com DOM e armazenamento controlados, cenários de histórico antigo, resposta não alterada, aviso, gravação, leitura em contexto recriado e um estudo crítico passaram; os testes usam subconjunto de itens e `mostrarResposta` como stub. São evidências limitadas, não teste de navegador real, todas as interfaces, histórico pessoal, falhas de gravação, leitores de tela, alunos ou psicometria. As execuções de navegador anteriores são atribuídas a seus autores e não cobrem automaticamente esta r2. A aplicação do produto e a reprodução técnica não provam aprendizagem ou validade de nota de domínio.

## Quadro de aceite e decisão

| Critério | Resultado r2 |
|---|---|
| Dados, modelos prévios, comando, unidades e consistência dos seis | Atendidos no alcance científico descrito; três hipóteses CR são editoriais, anteriores à escolha e separadas da banca. |
| Gabarito, unicidade, distratores e arredondamento | Atendidos nos seis modelos e opções examinados; plausibilidade teórica, sem piloto. |
| Cobertura remanescente | 191 artigos e conteúdo externo preservados; decisões r1 herdadas com autoria e limites, sem alegar nova resolução. |
| FON-01, FON-02 e BAN-10 afetados | Identidade documental e três suplementos/decisões revalidados no alcance localizado; não há aprovação global nova desses IDs. |
| BAN-02 e representações | **Não atendido integralmente:** R2-A exige sincronizar dois campos semânticos de CR06. |
| Versão, evidências e regressão | Identidade e cenários controlados sustentados por verificações atribuídas; validação final deve ser confrontada após o delta de R2-A. |
| Autoria e limites | Separados; não foram realizados por este Auditor testes de navegador, alunos, acessibilidade integral ou certificação externa. |

**Decisão:** `AJUSTES_OBRIGATORIOS` por R2-A. O Corretor deve reapresentar uma nova rodada de BAN-07; somente um parecer independente que satisfaça todos os critérios da versão efetivamente entregue pode permitir à coordenação selecionar outro ID. Produto, controle e checklist não foram alterados por este Auditor. O próximo ID permanece bloqueado.
