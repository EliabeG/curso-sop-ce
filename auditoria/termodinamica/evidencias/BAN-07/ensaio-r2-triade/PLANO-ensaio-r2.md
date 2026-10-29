# BAN-07 — plano de aplicação r2, ensaio isolado da tríade

**Estado:** ensaio técnico do Corretor, não aplicado e não aprovado. Escopo restrito a AV04-E, AV31-B e AV62-B. AV69 não está incluída. A adjudicação e o parecer integral sobre r1 ainda estão em curso; CR06, CR26 e CR45 podem acrescentar obrigações e exigir reconstrução do pacote. Este plano não libera a aplicação nem o próximo ID.

## Proposta examinável

- AV04: E confunde incompressibilidade com isotermia; D permanece a chave. [Prova das cinco opções e contramodelo](../propostas-r2/AV04-candidata.json), SHA-256 `973c4c2b82c8ae97ed4f8a784399df44d9cf3f75d80e303943844f368777b05f`.
- AV31: B confunde o efeito da fase da água com calor sensível devido a temperaturas distintas de referência; E permanece a chave. [Prova das cinco opções](../propostas-r2/AV31-candidata.json), SHA-256 `51dcf6eeba809fdf5294ddc0b86e5d048424697041930b1fe37b5c6a706e96c1`.
- AV62: B inverte o diferencial de pressão de abertura da válvula de admissão no modelo usual; D permanece a chave. [Prova das cinco opções](../propostas-r2/AV62-candidata.json), SHA-256 `4c8604d81bf884e5459d26f006c051451357d31a6085b96c8d80724345e0f0bc`.

Cada proposta substitui somente texto do distrator e comentário correspondente, sem alterar enunciado, chave ou demais alternativas. São explicações teóricas dos erros; não houve avaliação de estudantes. As redações literais continuam sujeitas a exame independente na versão final.

## Executar o ensaio

Na raiz do projeto, execute `node auditoria/termodinamica/evidencias/BAN-07/ensaio-r2-triade/ensaiar-triade.mjs`. A ferramenta confere os cinco hashes r1 e os hashes dos três artigos de base e candidatos, cria uma cópia integral sob a pasta temporária do sistema, troca nela os três artigos e atualiza inventário, índice Markdown e snapshot **dessa cópia**. Rejeita divergência de versão ou de escopo. O produto, registro e controle originais não são escritos. A cada execução cria outro diretório temporário, cujo caminho consta do resultado; a ferramenta não o remove.

O [resultado gravado](resultado-ensaio-r2-triade.json) identifica a cópia completa usada para a validação e seus hashes. O [pacote reduzido](pacote-ensaio/) contém cópias dos quatro arquivos atingidos, preservadas para inspeção; ele não é uma cópia autocontida de todos os recursos ou um pacote autorizado para implantação. Para reproduzir a validação completa, use a cópia temporária identificada no resultado ou execute novamente a ferramenta. O nome do snapshot e os textos de metadados dizem expressamente “ensaio”; **não copiar esse inventário como versão final**.

## Verificações e limites da execução de 29/10/2026

- Parser canônico: exatamente três artigos mudaram, IDs/chaves/ordem e todo o conteúdo fora dos artigos permanecem iguais. Os 194 demais artigos, inclusive AV69 e todos os CR, permanecem idênticos. Produto r1 e controle conferidos ao final.
- Validador do inventário na cópia completa: 197 registros e artigos, 29 recursos, 1.261 links locais, zero erros e zero avisos. Somente três registros de item mudaram; fonte global, snapshot e a explicação do método foram sincronizados. A revisão anterior dos registros não foi promovida a aprovação.
- Funções reais de digital de `curso.js`, com adaptador do parser canônico: AV04 `8eaed3f8` → `cccc3a46`, AV31 `4538caee` → `9230a05d`, AV62 `ed91f6ac` → `e0ab3037`. Cada nova digital é única entre os 80 AV atuais e não consta das 80 digitais AV r1. Isso não prova ausência de colisão com históricos desconhecidos de versões antigas.
- Funções reais do banco AV executadas em Node/VM com DOM e `localStorage` simulados: tentativas antigas permanecem, não preenchem a versão nova, item não alterado mantém resposta, aviso aparece e respostas novas persistem na recarga de um contexto simulado. Não houve navegador real, teste de placar, falha de gravação ou acesso ao armazenamento pessoal.
- SHA-256 do módulo no ensaio: `90615b1f43956425d39be2784e5b652bdd74888a12bd2826751e6ff3003e6c52`. O arquivo completo de resultado e os quatro arquivos provisórios têm hashes no próprio resultado; a ferramenta tem SHA-256 `a5e066278109b7ea9b2fa4aa17858f32d2860630650dc376ec805437a080c7eb`.

## Antes de qualquer aplicação posterior

1. Concluir parecer integral de r1 e adjudicar CR06, CR26 e CR45, incluindo o tratamento decidido para transcrição e gabarito oficial. Incorporar ao escopo quaisquer ajustes adicionais determinados e refazer a versão e o ensaio; esta tríade não presume que o escopo final esteja fechado.
2. Receber decisão do coordenador para aplicação ao produto e confirmar com o Auditor quais redações literais e condições se aplicam. Nenhum aceite é inferido deste ensaio.
3. Revalidar os hashes reais de produto e propostas, reconciliar o pacote com quaisquer deltas autorizados e gerar versão final, snapshot e inventário com nomes e descrições definitivos, preservando as evidências r1. Conferir somente mudanças esperadas e manter as chaves/documentos oficiais pertinentes.
4. Reexecutar validação canônica, prova das opções e das mudanças, comparação de todas as digitais relevantes e teste de histórico de versões conhecidas. Em cópia de armazenamento de teste, verificar aviso, ausência de migração, placar, nova resposta e persistência após recarga em navegador. Registrar limites de colisão em históricos desconhecidos e os hashes finais.
5. Entregar a versão efetivamente aplicada, manifesto e evidências ao Auditor independente. Aguardar parecer explícito antes de qualquer avanço no controle; o Corretor não aprova sua própria entrega.
