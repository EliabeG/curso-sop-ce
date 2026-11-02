# QA-09 — 12 flashcards conceituais restantes, r1

Data: 30/10/2026. Corretor automatizado `/root/qa_diagnosticos`. Estado: **aguardando auditoria independente**. Esta triagem complementa os nove cartões matemáticos de `flashcards-resumo-lote-20261030`; não aprova QA-09 nem outros materiais. Não altera o HTML ou inventários.

## Fotografia e método

`modulos/e1-termodinamica.html`, SHA-256 `57b13f0d6386764f1cc46ce543013b0eb75f7bfa97ffbd63ea331f38bfc5af8c`; inventário r8 `ae75a258398c385398567457d98ebd49b9838c0c9a4eedc69ea8d2d72981b687`. Li os 12 elementos `details.flashcard` completos na seção `flashcards`, fora dos 197 artigos. As posições UTF-16 e os hashes abaixo identificam os blocos integrais; `verificar.py` confirma sua extração e hashes, sem alterar arquivos. Conteúdo é qualitativo e não apresenta medição ou resultado numérico; as verificações abaixo não são um descarte por falta de algarismos. Novas versões exigem reconciliação por posição, contexto e hash.

## Conferência individual

| Posição | Cartão e interpretação conferida | Limite |
|---:|---|---|
| 1258382 | Sistema fechado: massa fixa delimitada por fronteira, que pode trocar energia. | Para o modelo convencional, não cruza massa; energia pode cruzar como calor ou trabalho. Sistema fechado não é necessariamente isolado. |
| 1258554 | Volume de controle: região escolhida para analisar fluxos de massa e energia. | A escolha da fronteira define as interações; um volume pode, num caso limite, não ter vazão de massa. |
| 1258726 | Intensiva: independente da quantidade de matéria. | Entender a comparação de subsistemas de mesmo estado, composição e regime, com efeitos de superfície não dominantes; pressão ou temperatura podem mudar por alterações de estado. |
| 1258891 | Extensiva: proporcional à quantidade de matéria. | Sob duplicação de sistema homogêneo no mesmo estado, massa, volume e energia total dobram, ignorando efeitos de superfície/interação; valores numéricos de exemplo são sintéticos. |
| 1259055 | Título: fração mássica de vapor em mistura saturada. | Aplicável à coexistência líquido–vapor em equilíbrio da substância pura; não confundir com fração molar de vapor de mistura multicomponente. |
| 1260863 | Entropia: propriedade usada no balanço de reversibilidade e geração. | É propriedade de estado; geração interna é não negativa e a transferência externa não se confunde com geração. O cartão é uma síntese, não enuncia balanço completo. |
| 1261026 | Adiabático: sem transferência de calor pela fronteira. | Não exclui trabalho ou transporte de energia por massa, nem implica automaticamente reversibilidade ou temperatura constante. |
| 1261181 | Isentrópico: entropia específica constante. | É propriedade específica; não confundir com entropia total constante de um volume de controle de massa variável. |
| 1261323 | COP: calor útil dividido pelo trabalho consumido. | Para refrigerador de compressão, calor útil retirado da região fria; para bomba de calor, calor útil entregue à região quente. A fronteira e o trabalho considerados devem ser definidos; não se afirma um COP para qualquer instalação. |
| 1261480 | Estrangulamento: redução de pressão irreversível, frequentemente isoentálpica. | A aproximação h₁≈h₂ exige o modelo usual estacionário, uma entrada e uma saída, sem calor/trabalho de eixo relevantes ou variações cinética/potencial relevantes. A irreversibilidade não decorre de mera diferença de pressão em todo dispositivo. A resposta do cartão específico de válvula tem lacuna já examinada em outro lote. |
| 1261653 | Regeneração: recuperação de calor para elevar temperatura de alimentação. | Em ciclo regenerativo simples, uma corrente mais quente aquece a corrente de alimentação; não determina uma eficiência ou um arranjo universal. |
| 1269356 | Refrigeração por compressão: compressor → condensador → dispositivo de expansão → evaporador. | Sequência de um ciclo simples, a partir do compressor e repetida ciclicamente; não descreve todos os arranjos de refrigeração. |

Não foi localizado erro que exija alteração nesses 12 cartões sob os limites indicados. Alguns são definições intencionalmente curtas e não substituem as bases ligadas à aula. A suficiência da forma condensada para estudo independente e a abrangência dos termos COP, regeneração e estrangulamento devem ser examinadas pelo Auditor; não se reivindica validação de todas as variantes de cada dispositivo.

## Identidade dos blocos

| Posição | SHA-256 |
|---:|---|
| 1258382 | `cf5fb7687a07c99036e13234cc4b99e1030e6bf2bde757df5ea04520655554d4` |
| 1258554 | `d3fe2c3c31bba63bda8b65e83b9d27f25e062fddc890936d61b8efcc4b80ae39` |
| 1258726 | `8d9d0c48590c9372c630a0dbc643ce04e220c5b5df3a19c9bf49ee0aaead0b23` |
| 1258891 | `6c49dd258ce6bc214d3501ac95dc22629db31a8f125fd71d431b3ffa5cbaef30` |
| 1259055 | `189b01d298d2324d5c0af5bc1a673e54c2714c063b843a0850703011ae2192b2` |
| 1260863 | `f12e3ef7ee71dea50ed9b9b6d807349f6349bf2640fdb6da41755b23aa1e414a` |
| 1261026 | `74f706ce9e47544c3966c61fc71f8e77950fa3199f262784e2334e088684f2ca` |
| 1261181 | `982634ea00f719a7c9ac29703a5608395c2cbeb7f84e7808161994717e8ee668` |
| 1261323 | `3a59761411a2e8121725915610184bfa700ef7209c46dd2d5ac7a63de47fdebc` |
| 1261480 | `55c2d6751a474f8dfa5ffe0af121d84a42a35cfb5e95c1b25ecd1f91387828bd` |
| 1261653 | `fffdf7d335dcd544c6e951a3d14483765ad82417828ad51709db6adee7601d64` |
| 1269356 | `ec475195b04ae6839573d972b522b12a2d2a52c69b4816100aa324ab53af579c` |

## Referências e limites

Modelos e definições de referência na própria aula E1 e no [DOE Fundamentals Handbook, volume 1](https://www.energy.gov/sites/default/files/2026-04/DOE-HDBK-1012-92_VOL1.pdf), seções sobre sistemas, propriedades e processos. Distinção entre COP de aquecimento e refrigeração no [DOE, Industrial Heat Pumps for Steam and Fuel Savings](https://www1.eere.energy.gov/manufacturing/tech_assistance/pdfs/heatpump.pdf). Fontes consultadas em 30/10/2026; nenhuma apresenta medições deste projeto. Não houve teste com alunos, navegador real, leitor de tela, revisão humana ou certificação externa. O Auditor deve ler os blocos efetivos, conferir as hipóteses e emitir juízo independente.
