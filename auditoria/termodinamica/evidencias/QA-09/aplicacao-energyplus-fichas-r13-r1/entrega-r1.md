# QA-09 — aplicação de referência EnergyPlus e fichas 88/99, r13

Data: 30/10/2026. Corretor automatizado `/root/next_examples`. **Aplicação na cópia de trabalho concluída; aguardando auditoria independente da versão efetiva.** Não encerra QA-09 nem libera outro ID.

## Alterações e fotografia

A candidata de fonte foi [aprovada isoladamente](../../../pareceres/QA-09-candidata-fonte-energyplus-r12-auditoria-independente-20261030.md), SHA-256 `43b2515ab3d9a0ec1974b0339bdcddba68dcba5d60f977563b8e1d9e0637cfd0`, e as fichas [88/99 foram aprovadas isoladamente](../../../pareceres/QA-09-candidatas-fichas-88-99-r12-auditoria-independente-20261030.md), SHA-256 `31c7ff0b55c26953e7caf3c42eed464520e51a8085bda5b26d78c4745c747c74`. Em E1, trocou-se exclusivamente o `href` do PDF EnergyPlus 24.1 que respondeu HTTP 404 pela página HTML da seção de balanço de CO₂ da mesma versão; o texto visível e atributos do link não mudaram. A equivalência integral com o PDF não foi demonstrada. O mesmo endereço em outro módulo segue fora do escopo E1.

A ficha 88 passa a declarar **regime permanente** no modelo do ótimo de compressão em dois estágios. A 99 explicita que a geração térmica é a total considerada, que não existem aportes independentes omitidos e que contribuições não devem ser contadas duas vezes. Nas duas, o ajuste foi aplicado à condição visível e à busca; os elementos matemáticos e links não mudaram.

HTML anterior SHA-256 `f76c39a3e1d8c349ebf0df72cc20a3ab21c68960c8451799bad90a9dcc4bd8c7`; HTML efetivo `f19000a7ddb1f3552b9633b0efec266fb3f6c5e5065808505a2f65b2005aefbc`. Formulário anterior `6857fd83e0b2e49c804903cff1dea4128a665ab22eb27bac4ab15d6c557ff756`; efetivo `5f3f31a4801f96a2b78b40c75d37392f6b16d264901ac313ac00458901970285`. Inventário oficial JSON atual `272d7a8fb277b45b60c9253475abe33de2accd061a3e9fe158b9207011bc874e`; Markdown atual `0f9e94ea3714ea868b50c76086093ba7b5b3ceb53d387cd24fd4eacbc97ff2e9`. Os 197 registros individuais são idênticos aos anteriores; somente a chave de fonte foi atualizada e o Markdown recebeu seção histórica. Fotografias e resultados estão em [resultado](resultado/).

## Verificações

- Ensaio em cópia e execução real com pareceres e hashes fixados: 197 artigos da aula e seus registros, 98 fichas não alvo, os 191 MathML do formulário e os MathML da aula são idênticos; dois cartões alterados e um único link da aula alterado. Um primeiro ensaio isolado encontrou erro em nome de variável após gravação na cópia; foi corrigido e o novo ensaio passou antes da aplicação.
- [verificar.mjs](verificar.mjs), SHA-256 `b1bf8a9fa5029dec2a6bdbf8de50a6b65642ce69125d3ab220cfeaeb8705d362`, executado sobre a versão efetiva: reconstrói ambas as páginas a partir das candidatas, confronta artigos, fichas, MathML, links, fonte do inventário e mapa; passou. É verificação estrutural do Corretor, não parecer independente.
- Inventário r13 SHA-256 `0df99b79bcc2350581fcdded72435d30d07858de237a549e6228ca73682f8d9b`; mapa r12→r13 `3f198c327e0bbb5d28c116fa5b1d655224e6ad9e24505556397d6c3586169671`. O mapa reconcilia 11.397 pares, 77 internos a inspecionar, 815 referências e 138 recursos; registra uma mudança de URL. Contagens sobrepostas não medem cálculos concluídos e hash igual não transfere aceite.
- Validador canônico retornou `ok=true`: 197 artigos/itens, 29 recursos, 1.263 links locais, sem erros ou avisos. Não testa a disponibilidade de referências externas nem certifica mérito científico. A candidata e o parecer registram a leitura externa do novo destino; a página HTML não foi demonstrada idêntica integralmente ao PDF original.

## Encaminhamento

Solicita-se auditoria independente da versão efetiva: correspondência dos três deltas, contexto científico das duas fichas, 77 pares internos, referência externa e metadados, 197 artigos, outras fichas, MathML e efeitos localizados sobre FOR-01 e BAN. Não há navegador real, leitor de tela, revisão humana, teste com estudantes ou certificação externa nesta entrega; a referência externa não comprova norma nem segurança de projeto.
