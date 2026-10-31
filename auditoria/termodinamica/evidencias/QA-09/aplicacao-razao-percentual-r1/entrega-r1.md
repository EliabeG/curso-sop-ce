# QA-09 — aplicação combinada de quatro correções, r1

Data: 30/10/2026. Corretor automatizado `/root/qa_teoria`; aplicação local após sinal da coordenação e revisão das candidatas na fotografia r7. **Aguardando auditoria independente da versão efetiva.** Esta entrega não encerra QA-09, não libera o próximo ID e não declara o curso avançado.

## O que mudou

Quatro fragmentos completos de `modulos/e1-termodinamica.html` foram substituídos exclusivamente pelas candidatas identificadas em `quatro-candidatas-config.json` e `edicoes-aplicadas.json`. Antes da aplicação, cada original foi encontrado uma única vez, cada candidata estava ausente, os blocos não se sobrepunham e seus hashes correspondiam aos manifestos e, no caso EX-031, à entrega e ao verificador da candidata.

1. **Razão percentual:** para falar de aumento de 40% na razão 1,4, explicita-se X₁ > 0; a redução também requer X₁ > 0 e X₂ < X₁.
2. **FUN-01, frações:** a conversão entre fração molar de vapor e título mássico passa a usar as massas molares médias de cada fase e identifica condições de igualdade, inclusive os limites.
3. **FUN-01, independência v/ρ:** elimina a alegação não documentada de origem de uma medida e mantém a conclusão de que ρ=1/v torna os valores redundantes para a mesma amostra.
4. **EX-031, reaquecimento:** caldeira, reaquecedor e condensador têm calor líquido externo especificado e não recebem nem fornecem trabalho não associado ao escoamento. Os valores e a solução permanecem. A conta sob o modelo é qₕ=3.590 kJ/kg, trabalho líquido=1.590 kJ/kg e rendimento≈44,29%.

O HTML anterior e o efetivo estão congelados como `antes.html` e `depois.html`; a aplicação combinada reproduz o resultado byte a byte. O inventário oficial JSON teve apenas a fotografia de fonte atualizada; 197 registros individuais e os 197 artigos preservam conteúdo e ordem. O Markdown oficial recebeu uma seção histórica nova. Aceites anteriores referem-se a suas versões, e o efeito de cada mudança requer revalidação independente no alcance pertinente, incluindo FUN-01 e BAN-02/07/08.

## Verificações

Antes de aplicar, o mecanismo foi ensaiado em cópia descartável com os mesmos quatro pares; a fotografia resultante coincide em SHA-256 com a efetiva. Também foi ensaiado em cópia com três pares, dois deles sintéticos, para testar o mecanismo; os arquivos sintéticos não foram aplicados ao curso. Comandos de reprodução estão em `INSTRUCOES.md`, e os pares reais em `quatro-candidatas-config.json`. `aplicar-r1.mjs` escreve arquivos e não é transacional: nunca o execute sobre evidências existentes; use uma cópia limpa e leia a instrução antes.

O r8 e o mapa r7→r8 têm **11.396 pares**, 7.186 IDs deslocados, oito hashes de trecho alterados ou ancestrais e 18 ocorrências com início dentro dos blocos modificados. Essas 18 são associadas por ordem e contexto; a correspondência exata deve ser inspecionada pelo Auditor. Os 815 registros de referências foram comparados por campos e início fora dos blocos, e os 138 registros de recursos por identidade e hash, admitida a atualização do próprio HTML E1. Nada disso transfere automaticamente aceites de r7 nem confirma conteúdo visual ou links externos.

`node auditoria/termodinamica/evidencias/QA-09/aplicacao-razao-percentual-r1/verificar-r1.mjs` reconstruiu o HTML, verificou identidade dos fragmentos, confirmou 197 artigos e registros, fotografias e totais do mapa. O `node auditoria/termodinamica/inventario/validar-inventario.mjs` retornou `ok=true`: 197 itens/artigos, 29 recursos e 1.263 links locais, sem erro ou aviso. O teste de persistência `auditoria/termodinamica/evidencias/BAN-08/aplicacao-av42-av45-av52-r1/testar-persistencia.mjs` passou nos seis cenários; utiliza funções reais com DOM e armazenamento simulados e não é ensaio em navegador. Não houve teste com estudantes, revisão humana ou certificação externa.

## SHA-256 das fotografias e evidências

| Arquivo | SHA-256 |
|---|---|
| HTML anterior / `antes.html` | `200f9b773050594d762cc596a5a89297024b245fc4f504081fc77baaed3db95f` |
| HTML efetivo / `depois.html` | `57b13f0d6386764f1cc46ce543013b0eb75f7bfa97ffbd63ea331f38bfc5af8c` |
| Inventário oficial JSON antes | `c240148429da2f2a295e6a97bce2f466a255fdc5f5fef1858aaed2fc2a687e89` |
| Inventário oficial JSON atual | `554608968c6fa031fd13a008215dba4c825377422d68bfc5a74db33667756b2c` |
| Inventário oficial Markdown atual | `67f48c9dc02a3e329f75ee356aa521c6288b37f5ca096fc30fae7a67ba916620` |
| Inventário r8 | `ae75a258398c385398567457d98ebd49b9838c0c9a4eedc69ea8d2d72981b687` |
| Mapa r7→r8 | `37d48a92165de1e29573b3ed5af992bd16df9a5da71b8372576fd84f0e6657fc` |
| `edicoes-aplicadas.json` | `3ef30f28ce1abf92a4b55bdcee9567663944f47f691b7a3c8c2ee0c5d4d099cf` |
| `quatro-candidatas-config.json` | `0fb5e3ffa56cf3e467adf2b7f8c09e6eb3e8f8683aff31eb0609b8191a4eef2e` |
| `resultado-r1.json` | `7d806f39edcca04dfb485637b457a5d4c30b0d074d58209d933be450080d6594` |
| `verificar-r1.mjs` | `197ee694195f9677f00f83855a95cdd0a621f857b0259b24fc545f256f15099c` |
| `aplicar-r1.mjs` | `4d00bc62c94fd3bfe823cb1b28d03e7d50ea6e4ac088dec8eca2b83c72f1aabf` |
| `mapear-r7-r8.mjs` | `2b2e2a0ae4dce592a95396151cfe8a2afff64a4f815d4ec6327b921e537d4ef9` |
| `inventariar-r8.mjs` | `5ad3e57f245ec8dce7034b851245ac5c667bae6eb4f18f64978aa08952055c67` |
