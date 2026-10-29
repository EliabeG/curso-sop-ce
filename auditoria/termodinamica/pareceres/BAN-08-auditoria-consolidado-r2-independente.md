# BAN-08 — auditoria independente do consolidado r2 na entrega r3

Data 29/10/2026. Auditor: agente automatizado `/root/auditor_ban08_novo`, independente do Corretor `/root/inspect_repo`. **Resultado localizado: correção FUN02 atendida e nenhuma outra divergência identificada no cotejo dos 197 registros com os apoios e a versão examinada.** Este parecer técnico não aprova BAN-08 globalmente nem libera próximo ID; a decisão integral cabe ao Auditor principal e à coordenação. Produto, controle e versões históricas não foram alterados nesta revisão.

## Versão e alcance

Examinei [entrega r3](../entregas/BAN-08-entrega-197-corretor-r3.md), SHA-256 `e2263923cdc7244ae032443c5c39a1d1d04e0a3ac9c3f4910e0a7548c50e15a6`, e `manifesto-entrega-197-corretor-r3.json`, SHA-256 `e9ecb32268fff2c8a61dc2e42b5e7eaf3be6c22abbcf24c7757b35fb3c1715`. Conferi os 11 caminhos/hashes nele identificados, incluindo os campos especiais de validação e validador: todos coincidem. O consolidado r2 `auditoria/termodinamica/evidencias/BAN-08/consolidado-197-corretor-r2.json` tem SHA-256 `796201da8c67b0aacef166ab511ac4494e951ca9270b8413c3a10ef24a3ec677`; sua validação r2 `5f9a25fcd4adc8d3cab7a7e6a98c12351cbb67480d5dc9aeb7de31f4866cdbdf`. HTML atual `9ec10053e40640feeb977baea742da3cbe4d546659f772f0256c6b3cb0720a55`, inventário JSON `adb2f7edd0bdfbf6d1f0ec0bc8aefd46b22d6728a0aa59fc3981281aac93fbcd`, resumo Markdown `7824dcd17e20d14b54db2c339310e6100cebaf8e7df59051d636844c7dc3be7d`.

O [cotejo individual dos 197 IDs](BAN-08-auditoria-consolidado-197-r2-independente.json), SHA-256 `0df4f095a8d61c8a463b25dec71e6cd14f8d0e385703a7c555f3c078f4d3b54e`, identifica para cada um o artigo, chave quando há, campos do consolidado, origem com hash, apoios com autoria/hash, recursos inventariados e resultado do confronto. Li os conteúdos por ID e comparei campos de dados, solução, resultado, comparação, tolerância e limites com o registro de origem; conferi artigos e chaves contra o HTML, e recursos com inventário. Para os três AV modificados, comparei a estrutura do recálculo aplicado, que usa campos com nomes próprios. **Essa execução não repete nem reivindica a autoria de cada cálculo feito por outros revisores**; a ciência dos itens é apoiada nas revisões individuais indicadas na matriz, com alcance e autores originais.

## Cobertura, fontes e revisão atribuída

Há 197 registros únicos, sem ausentes ou extras: 30 Q, 80 CR, 80 AV e sete abertos. Os hashes de todos os artigos coincidem com HTML e inventário; as 190 chaves do consolidado coincidem com os atributos dos artigos, e todos os 29 recursos distintos inventariados coincidem com seu hash atual. Os registros fornecem dados, solução, resultado, comparação, tolerância, limite e fonte ou não aplicabilidade fundamentada; os zeros e relações simbólicas não foram transformados em tolerâncias de medição. Registros com uma letra de resposta apenas em `resultado` têm a conclusão e fundamento nos campos de solução/comparação; a letra isolada não é tomada como cálculo.

Cotejei arquivos de origem e apoios por caminho e SHA-256, autores declarados e versão. Também conferi 347 âncoras internas e 125 caminhos locais listados nas fontes dos registros; não realizei nova pesquisa integral das páginas externas. Para cada um dos 194 artigos não alterados desde a base `80eff701...`, o artigo e os recursos inventariados são idênticos; o parecer de integração e a revalidação BAN-07 demonstraram em separado a identidade do HTML fora de AV42/45/52. As fontes históricas citadas nos registros não são apresentadas como nova execução. Em CR11–19 o hash individual consta da tabela final do parecer de apoio, em vez de cada seção; nos três AV, o parecer técnico da aplicação identifica a versão do HTML e a revalidação BAN-07 associada identifica os hashes individuais.

Os nove estudos críticos CR04/09/24/34/35/39/62/79/80 permanecem no universo e são descritos como **sem nota**, separando chave documental, hipóteses e contramodelos. Em CR68, os dados oficiais históricos defeituosos e o conjunto FON-09 corrigido permanecem separados; a evidência anterior e suas consultas têm autoria atribuída. Não realizei nova consulta dinâmica de toda tabela de propriedades nem reexame visual integral dos originais. Os sete problemas abertos foram cotejados com os apoios específicos: incluem condições gerais, rubricas e tolerâncias, em vez de declarar que uma única trajetória ou exemplo esgota as respostas admissíveis.

Os valores E/E/D e hipóteses aplicadas de AV42/45/52 têm recálculo próprio do Corretor e revisões independentes identificadas; a [revalidação BAN-07 localizada](BAN-07-revalidacao-av42-av45-av52-r1-independente.md), SHA `86e9edc229e31fa2c798ad5ae1b89d595ddf74b080652f9a435c515517380c08`, não aprova BAN-08. Os 197 campos `revisor_independente` continuam como `PENDENTE*`: eles não alegam que o Corretor tenha emitido decisão independente. Os campos `apoios` identificam os autores efetivos das análises anteriores; a decisão global do Auditor permanece distinta desses rótulos.

## Retificação de FUN02 integrabilidade

O [parecer preliminar](BAN-08-auditoria-consolidado-preliminar-r1-independente.md) apontou a igualdade incorreta “20 ln 2 = 271,807098 J/mol” no registro r1. Comparei recursivamente as versões: no registro de origem r2, apenas o campo `resultado` desse ID foi corrigido, além de um objeto de histórico; no consolidado r2, somente esse registro muda no resultado e no vínculo/hash de origem, acompanhados de metadados de versão/histórico. Os demais 196 registros são iguais; as versões r1 permanecem preservadas.

Recálculo próprio: 20 ln 2=13,862943611… J/mol; 100(3 ln 2+1/2)=257,944154168… J/mol; soma=271,807097779… J/mol. A r2 distingue incremento `13,862944` e total `271,807098`, ambos corretamente arredondados à sexta casa, e preserva a diferença orientada `−13,862944`. O artigo já continha o cálculo correto; não houve alteração de produto. Reexecutei o validador r2 do Corretor após leitura de seu código sem escrita; o teste passou e reproduziu os números, a identidade de 197 artigos/origens/apoios e o delta localizado. A correção do meu achado está atendida.

## Sincronização do inventário e resumo

Li o [parecer técnico de atualização do inventário](BAN-08-atualizacao-inventario-pos-parecer-auditoria-tecnica-r1.md), SHA `ca04865e63322ae3e341c06a47b9612e3e4a73c3178b3ad18b6991640d8a8e4f`, e o [parecer de correção do resumo](BAN-08-resumo-historico-auditoria-tecnica-r1.md), SHA `bfec219bcd010c7d5d4dadc33a78ad5786a4a1f581926be7bae97c66bd027043`, ambos de `/root/auditoria_av61_70`. Eles atribuem corretamente ao meu parecer BAN-07 a revalidação dos três AV e distinguem estado da entrega inicial do posterior. O primeiro relatou a contradição temporal do resumo; o segundo verificou sua correção, com duas alterações editoriais e reconstituição do texto em memória. O segundo também verificou 232 destinos e 209 fragmentos locais do resumo; não apresento essa execução como minha.

Executei pessoalmente o validador canônico sobre a versão atual: **197 artigos/registros, 29 recursos, 1.263 links locais, zero erros e avisos**. É verificação estrutural/documental, não certificação científica ou empírica. O apoio técnico de inventário atribui a variação 1260→1263 aos três vínculos da revalidação BAN-07, reproduzida por teste em memória daquela revisora. As condições e pendências históricas dos três AV estão reconciliadas sem reescrever os pareceres antigos.

## Decisão localizada e limites

| Critério neste exame | Resultado |
|---|---|
| Universo e identidade dos 197 | Atendidos nos hashes e referências atuais; matriz por ID disponível. |
| Solução, resultado, tolerância, fonte e autoria | Campos cotejados por ID com origem e apoios atribuídos; sem nova divergência identificada após correção FUN02. Leitura do consolidado não transforma cálculos alheios em execução própria. |
| Estudos críticos e abertos | Nove sem nota preservados e sete abertos incluídos com hipóteses e família de soluções; CR68 distingue dados históricos e corretivos. |
| AV42/45/52 e BAN-07 afetado | Versão aplicada e revalidação localizada identificadas; não significam aprovação automática de BAN-08. |
| Correção FUN02 r2 | Atendida, com aritmética e delta verificados; r1 preservada. |
| Inventário e resumo | Pareceres técnicos atribuídos; validador atual reproduzido. |
| Decisão global e fila | Pendente do Auditor principal e coordenação. Este apoio não altera controle nem aprova BAN-08. |

Nenhuma pendência adicional de conteúdo do consolidado foi identificada neste escopo após a retificação. Isso não prova aplicação com estudantes, dificuldade empírica, navegadores reais, todos os históricos pessoais, acessibilidade ou certificação externa. Os testes controlados de digitais e armazenamento foram descritos na revalidação BAN-07, com seus limites; não são repetidos como teste de aprendizagem aqui.
