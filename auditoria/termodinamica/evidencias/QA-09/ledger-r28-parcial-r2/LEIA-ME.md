# QA-09 — ponte parcial do ledger expandido r27 para r28, revisão 2

30/10/2026. Integrador `/root/planning`. **Revalidação individual concluída pelo integrador; aguarda auditor independente da ponte.** A r1 de triagem foi preservada com todos os 78 objetos pendentes. Esta r2 registra 18 objetos-base e 60 recortes adicionais em escopo localizado, sem promover os pais, filhos, bases, referências, recursos ou ativos. A coleção de 11.409 ocorrências, 816 referências, 138 relações e seis ativos tem estado padrão `pendente_de_integracao`; essas coleções se sobrepõem e não geram percentual de conclusão. QA-09 continua aberto.

Aula r28 SHA `d7294e8ed772cf4530788586d693a6cdfbf1ef6fa05c69afbc984efc46e353d8`, formulário `3157c9b114f3156e5517440d30b91ee8a4efdebcd95be8bd0c7a588f04dead46`, inventário `0a7a12fbf0cd2a0898bcebfdfa7ae98c850bdb0bf7d2b34eea06cc6a8d9afb44` e mapa `0e219e8d2863e3d7ced3af4857ce462ca5827bda38276da2a005e5f39e23eca2`. O parecer independente da aplicação efetiva é `auditoria-aplicacao-r28-next-theory-20261030/parecer.md` SHA `0b69b0e17287a80c188fb3f8dad462ac54819d893099be6af6ff1354bdcd1b18`. O parecer da aplicação não substitui a auditoria desta ponte.

A [reconciliação individual](reconciliacao.md) SHA `a0f53441b052372a3d7f2df12a3b9b02218a0fbf1ef7032f4c70cbf38b812af1` descreve o juízo e efeito dos nove deltas por objeto. Dos contextos registrados, 12 associações mudaram: nove com `base-leitura-matematica` e três com `substancias` (fichas 21/22 e D25). As seis fichas alteradas na aplicação não se tornam aceitas por esta ponte. Os dez contextos dos exemplos e quatro contêineres de figura foram comparados; os 23 contextos da base permanecem iguais. Revisei a dependência de D27 da turbina e de D20/EX037 de bomba, além do escopo de Rankine de D26/EX031; não são efeitos inferidos somente por hash. Os juízos estruturados estão em `juizos.json`, SHA `4e3a566c41cd21b057af57a194b596d7fa85e60f0ca6b7e9eae181fdc16cf908`.

## Verificação somente leitura

`node auditoria/termodinamica/evidencias/QA-09/ledger-r28-parcial-r2/ledger.mjs --verificar auditoria/termodinamica/evidencias/QA-09/ledger-r28-parcial-r2/ledger.json`

O script confere hashes das páginas ativas, snapshots r27/r28, inventários, mapa, pareceres e ledger r27; reextrai os 78 fragmentos, contextos, links e ativos dos três gráficos; confere os 18 pares individuais do inventário e os IDs e hashes de todos os pares do mapa; refaz uma seleção de contas. Os 78 fragmentos são idênticos, mas esse fato sozinho não transmite aprovação. As alterações de contexto são examinadas no relatório. Exige-se a foto correta: se o produto avançar, usar snapshots ou preparar nova ponte, não remover as guardas.

Sete mutações nos dados do ledger, executadas somente em cópias temporárias, foram rejeitadas: hash, posição, remoção, estado padrão, contexto, par do inventário e juízo. Isso testa confronto com o ledger reconstruído, não é teste de manipulação integral do mapa ou revisão de ciência. `negativos.py` SHA `99a4ade76339b7312ec184fd39eec6a412833d28e40bab9c4fab4a24f267f556`, resultado SHA `d7802335f5cde96f90ff23ee9f43ba5f3f1a532618bc622e7d08991128de94d8`.

- `ledger.mjs` SHA `a2692e9afa7ceedc969095cdab84f96f19c69c32380fca0175c48c94bc18a498`.
- `ledger.json` SHA `518e6b952254773be5d95ba31e06607ba0a34562d6d90162f9b95d36f6fba000`.

Meu vínculo anterior: fui auditor da candidata de substâncias/ciclos e autor do parecer correspondente; a presente ponte não torna independente minha própria revisão anterior. Sem navegador, leitor de tela, estudantes ou revisão humana.
