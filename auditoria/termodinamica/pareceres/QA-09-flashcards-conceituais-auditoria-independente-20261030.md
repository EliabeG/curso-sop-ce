# QA-09 — auditoria independente de 12 flashcards conceituais

Data: 30/10/2026. Revisor automatizado independente `/root/qa_examples`. **Veredito: AJUSTES_OBRIGATÓRIOS** no lote localizado devido ao cartão genérico de COP. Os outros 11 cartões não apresentaram erro identificado no alcance e ressalvas abaixo. QA-09 integral segue em correção e o próximo ID não está liberado.

## Critério, fotografia e método

QA-09 exige inventariar e conferir conteúdo numérico e suas explicações fora dos 197 artigos. Este lote contém 12 cartões com conceitos e não números de medição; ausência de algarismos não foi usada para dispensar exame de significado. Fonte `modulos/e1-termodinamica.html` SHA-256 `57b13f0d6386764f1cc46ce543013b0eb75f7bfa97ffbd63ea331f38bfc5af8c`; inventário r8 SHA-256 `ae75a258398c385398567457d98ebd49b9838c0c9a4eedc69ea8d2d72981b687`; entrega do Corretor `flashcards-conceituais-20261030/entrega.md` SHA-256 `dd85fdbbc3cd10cc84f263063e1cb21d976c78103b11a935e4acc49ed16807e4`; verificador do Corretor SHA-256 `c5f7d0ac597e3dd8829a668d01ba63a165ecc974790682fd641ac13e1cc578d5`.

Extraí os 12 elementos `details.flashcard` diretamente do HTML usando as posições UTF-16 do r8 e li frente e resposta; comparei o SHA-256 do fragmento bruto com o inventário, posição e o quadro da entrega. Reexecutei o verificador somente de leitura, que confirmou os 12 hashes; o script de identidade não decide mérito técnico. Os locadores e hashes individuais estão na entrega examinada. O contexto E1 de refrigeração por compressão foi considerado, mas o cartão de título genérico não declara que sua resposta se limita a esse modelo.

## Julgamento por cartão

- **Sistema fechado (1258382):** massa fixa, sem massa atravessando a fronteira; energia pode atravessá-la. Não equivale a isolamento.
- **Volume de controle (1258554):** região definida para balanço de massa e energia. O volume de controle pode apresentar nenhuma vazão em um caso específico; definição resumida não obriga escoamento.
- **Intensiva (1258726) e extensiva (1258891):** definição de comparação sob mesma composição e estado e condições usuais, sem efeitos de superfície relevantes. Intensividade não significa que a propriedade seja constante quando o estado muda. Extensividade implica aditividade/proporcionalidade nos limites do modelo.
- **Título (1259055):** fração mássica de vapor em equilíbrio líquido–vapor da substância pura; não é automaticamente fração molar de uma mistura multicomponente.
- **Entropia (1260863):** propriedade de estado presente em balanços de entropia e irreversibilidade; o cartão não substitui o balanço completo, nem confunde entropia transferida com geração.
- **Adiabático (1261026):** ausência de transferência de calor pela fronteira, sem garantir ausência de trabalho, entalpia transportada por massa, ou temperatura constante.
- **Isentrópico (1261181):** entropia específica constante; massa variável de um volume de controle impede identificar isso automaticamente com entropia total constante.
- **COP (1261323):** o cartão diz “Calor útil transportado dividido pelo trabalho consumido” sem restringir a tecnologias movidas por trabalho. Essa expressão serve ao refrigerador ou bomba de calor de compressão quando a fronteira de trabalho e efeito útil estão definidos, mas não é definição universal de qualquer COP; ajuste abaixo.
- **Estrangulamento (1261480):** queda dissipativa de pressão, usualmente modelada aproximadamente com entalpia constante quando escoamento é estacionário e Q, trabalho não associado ao escoamento e variações cinética/potencial são desprezíveis. A forma resumida não deve ser usada como definição suficiente para qualquer queda irreversível de pressão. Este parecer não transfere nem substitui a análise separada do cartão específico de válvula.
- **Regeneração (1261653):** recuperação de calor para pré-aquecer alimentação descreve os modelos Rankine/Brayton ensinados; arranjo e fontes de energia devem ser reconhecidos no ciclo específico, não inferidos como universais.
- **Refrigeração por compressão (1269356):** compressor→condensador→expansão→evaporador corresponde à sequência cíclica simples. Não afirma que todas as máquinas de refrigeração adotem esse arranjo.

## Ajuste obrigatório no COP

O [DOE, *Absorption Chillers for CHP Systems*](https://www.energy.gov/sites/default/files/2017/06/f35/CHP-Absorption%20Chiller-compliant.pdf) define o COP do chiller por absorção como carga frigorífica útil dividida pela entrada de calor. Por exemplo, em um balanço hipotético de taxas, carga frigorífica 70 kW, calor de acionamento 100 kW e trabalho auxiliar de bomba 1 kW dão COP térmico usual 70/100=0,70, não 70/1=70. Se considerada a fronteira global, também se deve declarar como os auxiliares entram no indicador. Valores são apenas contramodelo de definição e balanço, não projeto ou prova de viabilidade de estados.

Como a aula existente ensina explicitamente refrigeração por compressão, uma correção possível é limitar o cartão a esse modelo e indicar qual calor útil é usado para refrigeração ou aquecimento, com trabalho consumido como denominador. Alternativamente, poderia descrever COP como efeito útil dividido pela energia de acionamento claramente especificada e reservar fórmulas ao dispositivo apropriado. O Corretor deve preparar candidata isolada, preservar a finalidade pedagógica e submeter o texto à revisão; a correção da versão efetiva exige reconciliação por documento, contexto, posição e hash, preservação dos 197 artigos e revalidação localizada dos aceites afetados. Não atribuir ao DOE uma definição única que inclua automaticamente todos os consumos auxiliares.

## Quadro de critérios

| Critério do lote | Resultado |
|---|---|
| Identidade dos 12 cartões na fotografia r8 | Atendida por posição, contexto e hash; verificação estrutural não cobre sentido. |
| Conteúdo de 11 cartões e ressalvas | Sem erro identificado no contexto descrito; não aprovam todas as formulações ou conteúdos de apoio. |
| COP genérico e seu domínio | **Não atendido**: enunciado excessivamente geral face ao contraexemplo térmico de absorção. |
| Candidata e versão corrigida | Ainda não examinadas nesta rodada. |
| QA-09 integral e próximo ID | Continuam pendentes. |

DOE consultado em 30/10/2026; não houve captura com hash local. Não foram realizados ensaios em navegador, com estudantes, revisão humana ou certificação externa.
