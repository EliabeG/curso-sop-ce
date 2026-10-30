# QA-09 — aplicação combinada de flashcards, resumo e ficha 80

Data: 30/10/2026. Corretor automatizado `/root/qa_teoria`. As oito candidatas foram aplicadas após revisão da r2 dos flashcards e ensaio auditado da ficha. **Aguardando auditoria independente da versão efetiva e revalidação do alcance de FOR-01.** Esta entrega não encerra QA-09 nem libera o próximo ID.

## Fotografia e conteúdo

A aplicação parte da aula r8 SHA-256 `57b13f0d6386764f1cc46ce543013b0eb75f7bfa97ffbd63ea331f38bfc5af8c`, formulário `c27422b409a0a755448982c4074c6d6967fd3e91d7eae20274e218530f5c37b0` e inventário r8 `ae75a258398c385398567457d98ebd49b9838c0c9a4eedc69ea8d2d72981b687`. Os sete pares da aula são os de `candidatas-flashcards-resumo-20261030-r2` e o par do formulário é o de `ficha-080-candidata-20261030`. Hashes e posições efetivas constam em `config-r2.json` e `edicoes-aplicadas.json`; originais ocorreram uma vez cada, candidatos estavam ausentes e não havia blocos sobrepostos.

O COP distingue calor útil frio e quente no ciclo de compressão movido por trabalho; o flashcard da válvula especifica regime permanente e trabalhos; o do compressor esclarece a referência isentrópica; o do trocador explicita regime e vazões. Dois cartões de pressão intermediária delimitam as hipóteses da otimização. O resumo distingue a entropia do sistema fechado e as entropias específicas de entrada e saída de um volume de controle. Na ficha 80, o rendimento de motor exige calor externo positivo e trabalho líquido positivo. Detalhes e contramodelos estão nas análises das candidatas e respectivos pareceres; a aplicação não altera os números de exercícios.

As fotografias `antes-aula.html`, `depois-aula.html`, `antes-formulario.html` e `depois-formulario.html` congelam as versões, e os oito fragmentos reconstroem exatamente os dois resultados. A fonte do inventário oficial foi atualizada, mantendo os 197 registros; seu Markdown acrescenta nota histórica. Os arquivos de código e estilo não foram modificados. O impacto de dependências e aceites anteriores, inclusive FOR-01, exige exame independente específico; não se presume transferência automática.

## Verificações e limites

- Antes da aplicação, foi ensaiada uma cópia integral descartável com as mesmas oito candidatas r2. Os hashes dos dois arquivos efetivos coincidem com os da simulação. O mecanismo não é transacional, escreve snapshots e inventários e **não deve ser reexecutado sobre os arquivos produzidos**; para reproduzir, use cópia da base r8 e destino novo.
- `node auditoria/termodinamica/evidencias/QA-09/aplicacao-flashcards-ficha80-r1/verificar.mjs` reconstrói os dois arquivos, confirma unicidade e hashes dos oito fragmentos, 197 artigos e 197 registros, 99 fichas não alvo e as 100 identidades; os 734 MathML da aula e 191 do formulário são byte a byte idênticos aos da base. Isso não cobre todo o comportamento visual ou acessibilidade.
- O validador canônico passou: 197 artigos/itens, 29 recursos e 1.263 links locais, sem erros ou avisos. Os 103 links das fichas à aula apontam a 50 destinos distintos existentes; existência não comprova qualidade didática dos destinos.
- O mapa r8→r9 reconcilia 11.396 para 11.397 ocorrências: 11.200 pares externos por posição/contexto, 196 pares internos por sequência/tipo/contexto que precisam de exame individual e uma ocorrência adicionada ou reestruturada. Os 815 registros de referências e 138 de recursos foram comparados; nos dois documentos modificados, os hashes dos recursos refletem as novas fotografias. Hash igual não transfere aceite nem demonstra validade de dependências.
- O teste BAN-08 de persistência passou nos seis cenários com funções reais de `curso.js` em DOM e armazenamento simulados. Não é navegador real, nem verifica o filtro ou a interação dos cartões no formulário. Nenhum teste com alunos ou certificação externa foi realizado.

## Arquivos e SHA-256

| Arquivo | SHA-256 |
|---|---|
| Aula efetiva / `depois-aula.html` | `2d6b8fb2f9c99e04d22c19d7b32bbc3eb20577459d9132e506f9c0acef3f2fc2` |
| Formulário efetivo / `depois-formulario.html` | `cda652563a79c49a6c3d527ad1400c7f7597d33c9b8523ed8a26047b25c69feb` |
| Inventário oficial JSON | `d37e07a9f5ba5f85025f7090f22f3eeac7322e4ae2099439742762f8913a1204` |
| Inventário oficial Markdown | `4df557ab3cf309686f0107f801bf27c63d1e79854c2d13c473134c5ebc6673a9` |
| Inventário r9 | `023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d` |
| Mapa r8→r9 | `d210e8c7efd4520e0d2036c4ebd2ec90762f684ffe8378b5fd71fdbd43d15b90` |
| `config-r2.json` | `017b14761832e5b371ffc24fa6cccb807f1bb6b2a41b9d160a46d636be1c067a` |
| `edicoes-aplicadas.json` | `5f75701d8a19898a6068a942d5af2680a9d0a8ea4165f6452ba86a23eba91eaa` |
| `resultado.json` | `552bb11885f90d7830d088bf65bc46b5cf8f3580e47777484454d9fac3e5acc0` |
| `preparar-config.py` | `50910d171179e9a33ef86c521bd3121d1aa3b8bca60c33c9cb5754a2e528fc4e` |
| `aplicar.mjs` | `f48bb23e70ec539043da749da7350b29545e128e40348f96ccd7bacf93f1c767` |
| `mapear.py` | `404810aa5c99f9ef729c921206967520c1ac3a2f6b0996923b08359752aab579` |
| `verificar.mjs` | `e4b88753d85bbe37c3cc324c57c7c277d0292436ed45a8a9f67043bbbcb411bf` |
| `inventariar-r9.mjs` | `441ab0ab9b3c0ef2e3de8baff403fa7b2e949a665047c18ead4744e710855ae3` |
