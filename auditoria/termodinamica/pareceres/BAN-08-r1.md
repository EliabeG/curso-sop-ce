# BAN-08 — parecer independente r1

Data: 29/10/2026. Auditor principal: `/root/auditor_ban08_final`, agente automatizado independente do Corretor `/root/inspect_repo`. **Veredito: APROVADO**, restrito à entrega e aos arquivos identificados neste parecer. Não constitui aprovação do curso como avançado, nem execução de QA-09, nem liberação de outro ID.

## Critério e escopo

BAN-08 exige recalcular as 190 resoluções existentes e todas as futuras, com precisão compatível, mantendo registro por ID de solução, resultado, tolerância, fonte e revisor, sem aceite por amostragem. O universo entregue compreende 197 IDs: 30 Q, 80 CR, 80 AV e sete problemas abertos de FUN-01/FUN-02; inclui os nove estudos críticos sem nota. A avaliação cobre os valores e afirmações quantitativas das resoluções, recursos e dados necessários, e as relações simbólicas e condições dos abertos. QA-09 abrange ainda outros conteúdos numéricos fora desses 197 e não é encerrado aqui.

A regra comum da seção 3.2 é aplicada conforme seu alcance: este trabalho é revisão numérica do banco existente e correção de três enunciados existentes; não exige fabricar uma unidade curricular nova. A verificação científica e numérica, hipóteses, fonte, versão, responsabilidade e evidências pertinentes são exigidas. O protocolo exige parecer independente sobre a versão efetiva e nenhuma pendência obrigatória escondida em amostragem.

## Versão examinada

| Arquivo | SHA-256 |
|---|---|
| `auditoria/termodinamica/entregas/BAN-08-entrega-197-corretor-r3.md` | `e2263923cdc7244ae032443c5c39a1d1d04e0a3ac9c3f4910e0a7548c50e15a6` |
| `auditoria/termodinamica/evidencias/BAN-08/manifesto-entrega-197-corretor-r3.json` | `e9ecb32268fff2c8a61dc2e42b5e7eaf3be6c22abbcf24c7757b35fb3c1715` |
| `modulos/e1-termodinamica.html` | `9ec10053e40640feeb977baea742da3cbe4d546659f772f0256c6b3cb0720a55` |
| `auditoria/termodinamica/inventario/inventario-questoes.json` | `adb2f7edd0bdfbf6d1f0ec0bc8aefd46b22d6728a0aa59fc3981281aac93fbcd` |
| `auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md` | `7824dcd17e20d14b54db2c339310e6100cebaf8e7df59051d636844c7dc3be7d` |
| `auditoria/termodinamica/evidencias/BAN-08/consolidado-197-corretor-r2.json` | `796201da8c67b0aacef166ab511ac4494e951ca9270b8413c3a10ef24a3ec677` |
| `auditoria/termodinamica/pareceres/BAN-08-auditoria-consolidado-r2-independente.md` | `ae313f7e9180bfa151d354436ec0c8bd4faef55696c6e4c32015656f91e149c8` |
| `auditoria/termodinamica/pareceres/BAN-08-auditoria-consolidado-197-r2-independente.json` | `0df4f095a8d61c8a463b25dec71e6cd14f8d0e385703a7c555f3c078f4d3b54e` |
| `auditoria/termodinamica/pareceres/BAN-07-revalidacao-av42-av45-av52-r1-independente.md` | `86e9edc229e31fa2c798ad5ae1b89d595ddf74b080652f9a435c515517380c08` |
| `auditoria/termodinamica/pareceres/BAN-08-resumo-historico-auditoria-tecnica-r1.md` | `bfec219bcd010c7d5d4dadc33a78ad5786a4a1f581926be7bae97c66bd027043` |

Li o protocolo `PROTOCOLO_AAA.md` SHA `18f1f299556e8e60c926a1921987f6d2c10cc939aa4aef4487117dc66c344afc`, a seção BAN-08 e a seção 3.2 da auditoria original, a preparação independente e o estado do controle: BAN-08 está aguardando auditoria, com entrega r3. Não alterei o controle, o checklist ou o produto. Confirmei pessoalmente os 11 pares caminho/hash do manifesto r3, inclusive validador e validação, todos coincidentes.

## Confronto e resultados

Comparei por código os conjuntos do inventário, consolidado e matriz independente: 197 IDs únicos em cada um, sem ausentes ou extras; os hashes de artigo coincidem entre os três registros em todos os IDs. Confirmei os 79 pares distintos de caminho/hash de origens e apoios indicados na matriz; todos existem e coincidem. Cada linha da matriz atribui pelo menos uma revisão a agente automatizado distinto do Corretor. A reexecução própria, após leitura, de `validar-consolidado-197-r2.py` não gravou arquivos e confirmou os 197 artigos e campos, origens, apoios e o delta localizado; é verificação estrutural do script do Corretor, não revisão científica independente por si só.

O [cotejo independente integral](BAN-08-auditoria-consolidado-r2-independente.md), de `/root/auditor_ban08_novo`, documenta leitura individual dos campos e confronto com origem, chaves, artigos, recursos e apoios; sua matriz por ID identifica o alcance e a autoria efetiva. Relata 190 chaves coincidentes e 29 recursos distintos com hashes atuais. A ciência é sustentada pelos apoios individuais citados e atribuídos, incluindo análises de `/root/auditor_ban08_novo` e `/root/auditoria_av61_70`; li exemplos desses apoios e confrontei sua natureza com a matriz e a entrega. Não afirmo ter repetido pessoalmente todos os cálculos ou todas as consultas externas. A aprovação integra as revisões e heranças identificadas, não deriva apenas de número de linhas ou do script do Corretor.

Os campos `revisor_independente` do consolidado registram `PENDENTE` ou variantes de decisão pendente no momento de sua emissão. Eles não representam uma aprovação anterior. A matriz complementar, vinculada por ID e hash ao consolidado e aos apoios, fornece o revisor e a evidência atribuídos; este parecer é a decisão global posterior. O conjunto dos documentos satisfaz o registro de revisor sem reescrever o histórico ou atribuir ao Corretor uma revisão que ele não executou.

A ressalva da entrega r3 sobre FUN02 era temporal: a retificação recebeu depois exame independente. Recalculei: `20 ln 2 = 13,862943611… J/mol`; `100(3 ln 2 + 1/2) = 257,944154168… J/mol`; total `271,807097779… J/mol`. O registro r2 distingue corretamente incremento `13,862944` de total `271,807098` J/mol. A revisão independente documenta o delta e a preservação da versão anterior; o artigo publicado já apresentava a conta correta.

As ressalvas de suficiência dos antigos AV42, AV45 e AV52 foram resolvidas na versão aplicada. O parecer BAN-07 citado revalida expressamente apenas esse alcance: E/E/D, respectivamente; 25%, rejeição mínima 500 kJ por ciclo e 30%→25%, sob hipóteses explicitadas. Os demais 194 artigos e dependências são herdados nas condições de identidade ali documentadas. Essa é uma aprovação localizada de BAN-07, não uma suposta aprovação anterior de BAN-08. A auditoria técnica do resumo histórico distingue a situação inicial e a revalidação posterior; atribuo a seu autor a comparação editorial e a verificação de vínculos.

Os estudos críticos CR04/09/24/34/35/39/62/79/80 continuam fora da nota; chave documental, interpretações e contramodelos permanecem distintos. CR68 separa os dados históricos defeituosos dos dados corrigidos e sua fonte. Os sete abertos têm evidência de condições e famílias de soluções, sem reduzir escolha livre a um único exemplo. Onde não há resultado de medição, o registro distingue não aplicabilidade, igualdade simbólica ou comparação lógica de tolerância numérica. A evidência independente não declara nova pesquisa integral das fontes externas, teste com estudantes, certificação externa ou incerteza instrumental inferida dos dígitos.

## Quadro de critérios

| Critério | Decisão e fundamento |
|---|---|
| Universo integral, sem amostragem de fechamento | **Atendido**: conjuntos de 197 IDs coincidentes; matriz com decisão de cotejo e apoios por ID, incluindo críticos e abertos. |
| Solução, resultado e precisão/tolerância | **Atendido** pelo consolidado e cotejo individual atribuído; retificação FUN02 verificada. Exatidão, arredondamento, comparações e não aplicabilidade mantêm seus limites. |
| Fonte, versão, dados e revisor | **Atendido no conjunto dos documentos**: consolidação por ID, fontes, hashes e matriz de revisões atribuídas; os campos históricos pendentes não são apresentados como aceite anterior. |
| Ciência e coerência da versão efetiva | **Atendido no escopo BAN-08** com os apoios independentes e a revalidação localizada dos três artigos alterados; conclusões científicas e cálculos prévios permanecem atribuídos aos respectivos autores. |
| Integridade, delta e reprodutibilidade | **Atendido**: manifesto e vínculos conferidos; validador em leitura reproduzido; fontes históricas e limitações preservadas. |
| Regra comum curricular de conteúdo novo | **Não aplicável como obrigação de criar nova unidade** para esta revisão; hipóteses, dados, revisão e rastreabilidade aplicáveis foram examinados. |
| QA-09, navegador real, estudantes e certificação | **Fora do escopo / não demonstrados**; não são reivindicados por este parecer. |
| Ajustes obrigatórios BAN-08 | **Nenhum identificado** para os arquivos e escopo examinados. |

**Decisão sobre a fila:** BAN-08 está aprovado nesta versão; este Auditor não altera o controle nem libera o próximo ID. Somente a coordenação pode registrar a decisão e decidir a liberação conforme o protocolo. Alterações posteriores que afetem a evidência ou a versão examinada exigem reavaliação do alcance afetado.
