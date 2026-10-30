# QA-09 — preparo de aplicação EnergyPlus e fichas 88/99, r12→r13

Data: 30/10/2026. Corretor automatizado `/root/next_examples`. **Preparo e ensaio somente em cópia; nada aplicado ao produto.** A candidata do vínculo EnergyPlus tem parecer localizado favorável; as candidatas das fichas 88/99 na fotografia ensaiada ainda aguardam revisão independente. QA-09 permanece aberto.

## Escopo e condições

O mecanismo preparado aceita exatamente três substituições: vínculo EnergyPlus em E1 e cartões 88/99 de sua fotografia r12. Ele exige hashes fixos dos dois manifestos, da candidata e da revisão EnergyPlus e das bases. Para `--apply`, exige adicionalmente caminho e SHA-256 do parecer das fichas 88/99; o próprio parecer deve declarar veredito aprovado e identificar pelo hash o manifesto exato ensaiado `02a4abfebd9edef1e62439894097288e9a8bc3ad0670f6d3e5e26420bad7200f`. A execução exige também liberação da coordenação. Se candidatas forem alteradas em nova rodada, não usar este executor como se a revisão se transferisse: adaptar os hashes, examinar os novos deltas e ensaiar novamente.

Aula base `f76c39a3e1d8c349ebf0df72cc20a3ab21c68960c8451799bad90a9dcc4bd8c7`; formulário `6857fd83e0b2e49c804903cff1dea4128a665ab22eb27bac4ab15d6c557ff756`; inventário r12 `457a56300aab8f612ebb7f136c7c2f62520abb49c005c209a238925179248d0e`; JSON do inventário oficial `f2605176763a61832417506517373a16736717d5cc23de7494e901322c394856`; Markdown oficial `1e5251583294cc3a497bba6693671e6f996f624012c218121c66e5866380bef9`. Se a base mudar, não executar; reconciliar e revisar o impacto.

A mudança no HTML da aula troca somente o link para a seção HTML EnergyPlus 24.1 e preserva seus 197 artigos, sem alterar o mesmo URL em outro módulo fora do escopo E1. O inventário oficial atualiza apenas `fonte` e mantém os 197 registros idênticos; seu Markdown recebe seção histórica. No formulário, duas fichas alvo mudam condições e busca, os outros 98 cartões, MathML e links permanecem idênticos. O gerador r13 é cópia do r12 com destino novo protegido; o mapa compara posições, contexto, 815 referências, 138 recursos e artigos segregados, registrando especificamente a troca do URL. Pares internos de cada alteração exigem revisão individual; nenhum aceite é transferido automaticamente.

## Ensaio em cópia e execução futura

Em cópia `/tmp`, `node .../aplicar.mjs --ensaio` passou: aula simulada `f19000a7ddb1f3552b9633b0efec266fb3f6c5e5065808505a2f65b2005aefbc`; formulário simulado `5f3f31a4801f96a2b78b40c75d37392f6b16d264901ac313ac00458901970285`; inventário simulado r13 `0df99b79bcc2350581fcdded72435d30d07858de237a549e6228ca73682f8d9b`; mapa `3f198c327e0bbb5d28c116fa5b1d655224e6ad9e24505556397d6c3586169671`. Há 11.397 pares, dos quais 77 internos; 197 artigos e registros preservados; 98 fichas não alvo e 191 MathML preservados; validador canônico sem erro (1.263 links e 29 recursos). Ver [resultado-ensaio.json](resultado-ensaio.json). O primeiro ensaio revelou um erro de nome de variável após gravação na cópia; foi corrigido e a versão atual passou em cópia nova. Isso reforça a limitação não transacional.

Modo de ensaio é recusado fora de `/tmp`. O executor recusa `--apply` sem dois argumentos de parecer e recusa parecer inexistente antes de gravar; esses bloqueios foram testados. Após parecer favorável das duas fichas, inspeção e sinal da coordenação, a forma é:

```sh
node auditoria/termodinamica/evidencias/QA-09/aplicacao-energyplus-fichas-r13-r1/aplicar.mjs --apply CAMINHO_DO_PARECER SHA256_DO_PARECER
```

**Limite operacional:** a escrita do produto e do inventário oficial ocorre antes de gerar mapa e validar. Em caso de falha ou interrupção, a operação pode ficar parcial; preserve snapshots em `resultado/`, compare hashes e reconcilie, sem apagar históricos ou declarar conclusão. Após eventual aplicação é necessário um novo parecer independente sobre a versão efetiva, conteúdo técnico, 77 pares internos, vínculos e alcance de FOR-01/BAN, além de controle de versões. Não houve teste em navegador, leitor de tela, estudantes ou revisão humana.

Hashes: `aplicar.mjs` `959332178434ba9692039169b035ae5c7a02bfd2ced2062da9f823e2cc3e4bfa`; `mapear.py` `b04205ca890a0a91f9e3dd387609f2accb4233e2270df2e533e661155eb5ae23`; `inventariar-r13.mjs` `4b793a721d283e7d35b41ca68dc717501959b4ce0a971eb532613fb94c7ac59d`; `resultado-ensaio.json` `20c116f57ea3cea6f07f98831436f37e3822c7feca6d51bd2f539808faf13091`.


## Aditamento após revisão das fichas

As fichas 88/99 receberam [parecer localizado favorável](../../../pareceres/QA-09-candidatas-fichas-88-99-r12-auditoria-independente-20261030.md), SHA-256 `31c7ff0b55c26953e7caf3c42eed464520e51a8085bda5b26d78c4745c747c74`. A verificação de parecer do executor foi ajustada para reconhecer a redação literal do veredito e um novo ensaio da versão exata com `--apply` e o parecer verdadeiro passou em cópia isolada; os resultados de HTML e inventário coincidem com o ensaio anterior. A aplicação real permanece sujeita à liberação da coordenação e revisão da versão efetiva.
