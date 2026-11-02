# QA-09 — aplicação das fichas 27–29 e 52–53 na fotografia r12

Data: 30/10/2026. Corretor automatizado `/root/next_examples`. **Aplicação concluída na cópia de trabalho; aguardando auditoria independente da versão efetiva.** QA-09 integral permanece em correção; o próximo ID continua bloqueado.

## Escopo e identidade

As três candidatas de calorimetria r3 e duas de CO₂ foram aprovadas isoladamente em [parecer de calorimetria](../../../pareceres/QA-09-candidatas-calorimetria-27-29-r3-auditoria-independente-20261030.md), SHA-256 `c51b2c1244928d06954a01c74d98883e3597e6e2b8f8e6aef609a96e17c6aa4b`, e [parecer de CO₂](../../../pareceres/QA-09-candidatas-co2-52-53-r11-auditoria-independente-20261030.md), SHA-256 `8b848c80ecc4b5ff4bf5b6316472986f0d1cfc92d8474c8c901e29297e3c0656`, ambos sobre a fotografia r11. O executor fixou esses pareceres e os manifestos aprovados; as quatro ocorrências de condições de CO₂ e as seis de calorimetria foram substituídas no texto visível e na busca dos cinco cartões, sem modificar fórmulas.

As fichas 27 e 28 explicitam o modelo aproximado de energia interna de sólidos/líquidos, os efeitos desprezados e a inclusão do recipiente e trabalho externo. A 29 delimita substância pura, temperatura e pressão constantes durante a mudança de fase, ausência de outros trabalhos e o significado de ℓ. Nas fichas 52/53, geração e vazões volumétricas devem ser referidas à temperatura e pressão do ambiente, convertendo bases diferentes. Os limites e contramodelos estão nas candidatas e nos pareceres, e precisam ser confrontados novamente na versão efetiva.

Aula r11/r12 inalterada SHA-256 `f76c39a3e1d8c349ebf0df72cc20a3ab21c68960c8451799bad90a9dcc4bd8c7`; formulário anterior `01d5d79639cd17dfcaea38479019cf719e2601f5b35d446ab562e50d381fa5c9`; formulário atual `6857fd83e0b2e49c804903cff1dea4128a665ab22eb27bac4ab15d6c557ff756`. Inventário oficial JSON `f2605176763a61832417506517373a16736717d5cc23de7494e901322c394856` e Markdown `1e5251583294cc3a497bba6693671e6f996f624012c218121c66e5866380bef9` não mudaram: eles identificam a aula, que permaneceu idêntica. Snapshots anteriores e posteriores estão em [resultado](resultado/).

## Verificação

- Ensaio em cópia descartável antes da aplicação confirmou mesma saída, 100 fichas na mesma ordem, as 95 não alvo byte a byte iguais, 191 elementos MathML e links preservados; HTML da aula e os 197 artigos e registros permaneceram íntegros. Execuções em cópias sem `--apply`, com destino existente ou com formulário adulterado foram rejeitadas; a última não gravou o produto.
- [verificar.mjs](verificar.mjs), SHA-256 `1402bf51003b3de8a6fd86e02a973404eda0ef1a9c8767f6392f218f0f855bb3`, executado após aplicação, reconstituiu o formulário efetivo byte a byte a partir das cinco candidatas e confirmou os mesmos limites estruturais; não constitui auditoria independente.
- Inventário r12 SHA-256 `457a56300aab8f612ebb7f136c7c2f62520abb49c005c209a238925179248d0e`; mapa r11→r12 `1c67bdda8f5996c6a230e4556277dbbfac270e64ec5b2ac0cabccdee4b3680ef`. O mapa contém 11.397 pares, 11.238 externos e 159 internos associados por ordem/contexto que exigem exame individual. Registra 815 referências, 138 recursos e os 197 artigos segregados. Uma correspondência ou hash igual não transfere aceites automaticamente.
- Validador canônico passou: 197 artigos e registros, 29 recursos e 1.263 links locais, sem erros ou avisos. Os resultados e hashes estão em [verificacoes.json](resultado/verificacoes.json). O mapa e o validador são estruturais, não provam mérito científico ou aprendizagem.

## Encaminhamento

O Auditor independente deve confrontar os cinco textos atuais e hipóteses, os 159 pares internos, originais/candidatas, MathML, busca, referências e recursos e a preservação das demais fichas e dos 197 artigos, além da revalidação localizada de FOR-01 e demais aceites afetados. A execução não foi transacional e deve ser tratada como fotografia efetiva, nunca como prova de uma execução futura. Não houve teste em navegador real, leitor de tela, revisão humana, teste com alunos ou certificação externa nesta entrega. Os aceites anteriores não são automaticamente transferidos à r12.
