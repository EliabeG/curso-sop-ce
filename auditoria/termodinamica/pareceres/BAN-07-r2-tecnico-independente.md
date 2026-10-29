# BAN-07 r2 — parecer técnico independente da entrega aplicada

Data: 29/10/2026. Revisora: `/root/auditoria_av61_70`, agente automatizado independente do Corretor. **Resultado técnico parcial: AJUSTE PROPOSTO na rastreabilidade BAN-02 de CR06, sujeito à decisão do Auditor principal.** A entrega aplicada não recebe aprovação global de BAN-07 por esta peça, e o próximo ID não é liberado.

## Versão, fontes e integridade

Examinei [BAN-07-r2](../entregas/BAN-07-r2.md), SHA-256 `c9b19afcf3c3ddb0f8033b6fd13090d31750d60e31c68751804159e5c9b44bee`, e o manifesto `auditoria/termodinamica/evidencias/BAN-07/manifesto-r2.json`, SHA-256 `471b222e81c17a257a008a38671eb617498720f0add1f1baf7343baa0b0b413d`. Em leitura própria, conferi todos os **12 arquivos** enumerados nas seções de produtos/evidências e os **três backups r1**: nenhum ausente ou com hash divergente. Os históricos FON-02 e BAN-10 conferem com os hashes declarados. `assets/curso.js` (`a20f4d19158073a9a1c48aabdfba8fa863b02063e16061c00b16448a6ccc2e13`) e `assets/registro.js` (`46da94527d6639fe0265bd766286f1ef39623966105e00bda3b31f21ca2c247c`) permanecem iguais à r1. Esses resultados valem para os arquivos enumerados, não para todos os arquivos possíveis do projeto.

Versão aplicada: HTML `80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0`; inventário JSON `71ac07e042aa65675fc3d4b69d8d0ae11cb66df967d45e66b1a88f4f1350e074`; Markdown `35df191e2f7964adfb7b975668491e8ba39d983a5df93640a35d3d96ae142df8`; snapshot tem o hash do HTML. O controle é mutável pelo coordenador; não foi modificado por esta revisão e não é tratado como prova de produto.

## Delta de artigos e revalidação FON-01 localizada

Comparei diretamente HTML aplicado com backup r1: **197 artigos, mesmos IDs e ordem; somente CR06, CR26, CR45, AV04, AV31 e AV62 diferem**; outros 191 e texto externo aos artigos são idênticos. Cada um dos seis artigos novos corresponde byte a byte à candidata examinada nos pareceres isolados da revisora. CR45 usa r2b e CR06 usa o JSON de candidata reconciliado; essas conclusões científicas anteriores não são apresentadas como novas resoluções. Ao remover cada parágrafo editorial dos três CR, o artigo r1 é recuperado integralmente, inclusive transcrição, chave e figuras. Não se atribui suplemento à banca.

A conferência FON-01 complementar registra essa identidade e corretamente não reivindica nova leitura documental. Reconferi presença e SHA-256 dos **seis PDFs** de prova e gabarito relacionados aos três CR e dos dois recursos de figura, contra os registros de FON-01: todos coincidem. O confronto visual original pertence ao Auditor de FON-01; eu havia inspecionado as páginas/figuras de CR06 e CR45 em pareceres pontuais anteriores. Não houve nova leitura visual de CR26 nesta execução nem pesquisa de atos fora do escopo do FON-01 anterior. **Revalidação localizada de identidade e vinculação documental sem novo ajuste encontrado**, não nova aprovação documental de todos os itens.

## Inventário BAN-02, FON-02 e BAN-10

Comparei os dois inventários JSON: 197 registros, exatamente seis registros alterados; os hashes dos seis artigos coincidem com os fragmentos aplicados. Fonte e snapshot foram atualizados. Os seis campos de justificativa de nível conferem com suas linhas do Markdown, incluindo a correção da linha CR06 solicitada no parecer do ensaio; competências e contagem de etapas também são preservadas. Executei `validateInventory` canônico em leitura sobre produto aplicado: **197 registros e artigos, 29 recursos, 1.261 links, zero erros e avisos**. Este validador não verifica toda a semântica dos campos.

**Pendência específica de CR06:** no JSON, `raciocinio.etapas` e `vinculo_competencias.alcance` ainda contêm “Relacionar dilatação constante com transformação afim entre escalas” sem mencionar que **ambas as escalas são lineares na altura**, hipótese editorial que torna a implicação válida. Dilatação linear de mercúrio, isoladamente, não determina linearidade de duas escalas arbitrárias — foi justamente a insuficiência adjudicada em r1. Embora `hipoteses.explicitadas`, justificativa de nível e Markdown apresentem corretamente o suplemento, esses dois campos que descrevem raciocínio e alcance podem sugerir que a dilatação por si basta. Recomendo atualizar ambos para reconhecimento de relação afim entre escalas lineares na altura, explicitando sua condição editorial, preservando categoria, nível e contagem se ainda apropriados. Recalcular hash do inventário/manifesto, verificar representações afetadas e reapresentar. É ponto localizado de rastreabilidade BAN-02; não altera a prova, a chave ou a demonstração do artigo.

O complemento FON-02 aplicado registra as três hipóteses editoriais com texto, posição, chave e hash atual, mantendo intactos os 77 outros registros e o conteúdo histórico anterior dos três; o arquivo histórico continua intocado. Ele identifica fonte histórica e fonte reexaminada, com estado submetido à auditoria. A triagem complementar BAN-10 preserva 194 registros, reavalia somente CR06/26/45 com histórico de suas antigas decisões e uso proposto pontuável sob o modelo editorial; soma 197. Esses complementos são revalidação localizada sujeita a exame do Auditor responsável, não aprovação automática dos IDs globais. Este exame confirma a separação e rastreabilidade dos três suplementos no alcance descrito.

## Digitais e testes de progresso

Inspecionei o script do ensaio conjunto do Corretor; ele escreve em stage e evidências, por isso **não foi executado diretamente**. Em cópia temporária no mesmo diretório, troquei a criação/cópia de stage pela leitura do produto aplicado, usei o backup r1 como base, substituí a escrita do HTML por comparação com o produto atual e encerrei antes das demais gravações. A reprodução passou, com cópia temporária removida; não regravei produto, stage ou evidências. Esse é reaproveitamento atribuído de verificações do Corretor, com adaptação e execução por esta revisora, não uma suíte independente escrita do zero.

| Item | Digital r1 → r2 | Chave |
|---|---|---|
| AV04 | `8eaed3f8` → `cccc3a46` | D |
| AV31 | `4538caee` → `9230a05d` | E |
| AV62 | `ed91f6ac` → `e0ab3037` | D |
| CR06 | `01aa3697` → `d63393e4` | C |
| CR26 | `988714ce` → `1c9fcf05` | E |
| CR45 | `c084d78c` → `9475e2f5` | C |

Nos dois bancos, as novas digitais não colidem com as 80 digitais r1 do mesmo banco nem com as 80 atuais. A reprodução em Node/VM usa funções reais selecionadas de leitura, atualização, salvamento, aviso e filtro/placar, e DOM/localStorage simulados. Em cada banco, testes com três respostas antigas revisadas e uma não revisada verificam não migração para os novos itens, preservação da não revisada, aviso, gravação do histórico junto a novas respostas e leitura em contexto recriado. Um estudo crítico no banco CR é excluído do placar simulado. `mostrarResposta` é stub e o conjunto contém apenas os itens necessários aos cenários: não é teste de navegador real, todas as 160 interfaces, concorrência real, falha de gravação, armazenamento pessoal ou históricos desconhecidos. A entrega reconhece esses limites. Nenhum teste com estudantes, psicometria, acessibilidade integral ou certificação externa é reivindicado.

## Quadro de critérios e decisão

| Critério | Resultado |
|---|---|
| Entrega, manifesto, backups e hashes | Atendidos para os 12 arquivos enumerados e três backups; históricos e JS preservados. |
| Delta, candidatos e identidade | Atendidos para seis artigos e 191 preservados; ciência local das candidatas atribuída aos pareceres anteriores. |
| FON-01 no alcance afetado | Identidade oficial, fontes e figuras conferidas; sem novo ajuste documental identificado nos três. |
| BAN-02 no alcance afetado | JSON e Markdown sincronizados nos seis campos de nível e rastreio de hashes, mas **dois campos de raciocínio/alcance CR06 precisam delimitar a hipótese editorial** antes de revalidação completa. |
| FON-02/BAN-10 | Complementos identificam e localizam suplementos e preservam registros históricos; não se aprova automaticamente o restante de cada ID. |
| Digitais e persistência | Verificações controladas reproduzidas sem falha; limites acima e nova validação da versão reapresentada aplicam-se. |

**Ajuste proposto:** modificar os dois campos citados do inventário de CR06, mantendo o texto oficial, suplemento, chave e categoria quando apropriado; sincronizar representações se afetadas, atualizar evidências e hashes e reapresentar para conferência. A decisão definitiva cabe ao Auditor principal. Sem aceitação global de BAN-07, conclusão de BAN-08 ou liberação do próximo ID. Produto e controle não foram alterados nesta revisão.
