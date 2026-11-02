# QA-09 — auditoria independente de diagnósticos 01–10, r9

Data: 30/10/2026. Auditor automatizado `/root/planning`, distinto do Corretor `/root/next_examples`. **Veredito: AJUSTES OBRIGATÓRIOS no lote**, para o enunciado do diagnóstico 2. Não aprova QA-09 integral nem libera o próximo ID.

## Critério e identificação

QA-09 exige inventariar e recalcular as ocorrências numéricas além dos 197 artigos, inclusive diagnósticos e explicações, com referência verificável e resultado conferido. Esta revisão cobre somente os dez diagnósticos enumerados em `#preparacao-questoes`, as hipóteses e contas descritas abaixo. Não examina toda a aula, apresentação dinâmica ou aprendizagem.

Aula efetiva SHA-256 `2d6b8fb2f9c99e04d22c19d7b32bbc3eb20577459d9132e506f9c0acef3f2fc2`; inventário r9 SHA-256 `023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d`. A [entrega do Corretor](../evidencias/QA-09/diagnosticos01-10-r9-20261030/entrega.md) tem SHA-256 `f8ac088acb6dd9948f7abf574589879c871f598ee0e761f196ab9390513cec85`. O verificador independente [verificar.py](../evidencias/QA-09/auditoria-diagnosticos01-10-r9-20261030/verificar.py), SHA-256 `9a080a2f8849406a40c540986ba79062b3bb14aa541886a45b2625ec715a2b86`, confrontou cada diagnóstico por número, contexto, posição e hash de fragmento, e refez as contas selecionadas. Também reproduzi o verificador do Corretor após conferir que não grava evidência. A análise científica não decorre apenas dos scripts.

## Ajuste obrigatório — diagnóstico 2

A parte quantitativa é correta: para limite inferior de −20 °C e alcance de 150 °C, o limite superior é 130 °C; um intervalo de 150 °C tem magnitude 150 K. Porém, o enunciado pergunta qual instrumento e grandeza um “tubo metálico curvo acionando ponteiro” identifica, sem informar que o tubo está conectado diretamente a um fluido cuja **pressão de processo** é o mensurando. Essa descrição não determina uma única grandeza: termômetros de expansão a gás também podem empregar bulbo, capilar e tubo de Bourdon ligado a ponteiro, sendo a temperatura no bulbo o mensurando. Um manômetro de Bourdon ligado ao processo mede pressão. As duas configurações são descritas pela fabricante WIKA em [princípio do manômetro](https://www.wika.com/media/Technical-information/English/ds_in0001_en_co.pdf) e [termômetro acionado por gás, seção 2](https://www.wika.com/media/Operating-instructions/Operating-instructions/Temperature/Dial-thermometers/oi_tgt73_ex_en_de_fr_es.pdf), consultados em 30/10/2026.

A base `#base-instrumentos` apresenta o manômetro como exemplo e o link “Retomar as aulas” aparece após a resolução; essa associação não fixa o mensurando do dispositivo genérico no enunciado. **Ajuste solicitado:** explicitar que o tubo recebe diretamente a pressão do fluido de processo e se deforma com essa pressão, ou acrescentar condições equivalentes que identifiquem o manômetro. Preservar a pergunta sobre instrumento/grandeza e a conta do span. Preparar candidata isolada, confrontar identidade e impacto, e auditar independentemente a aplicação efetiva, inventário e referências afetados. Esta observação não afirma que todo tubo de Bourdon em um instrumento mede exclusivamente temperatura.

## Demais verificações no alcance da entrega

- **1:** partes de massas iguais da mesma amostra homogênea nas mesmas condições têm 1/4 da massa e do volume; densidade e temperatura são intensivas. A unidade SI é kelvin, K.
- **3:** gás ideal, massa fixa, volume constante e temperaturas absolutas: 353,15/293,15 = 1,2046733754…, arredondado a 1,205, aumento 20,4673…%, arredondado a 20,5%; pressão não quadruplica.
- **4:** partículas em sólidos e líquidos também têm movimento microscópico; baixa densidade e distância da condensação favorecem o modelo ideal. Não há dado numérico a recalcular nesta resposta qualitativa.
- **5:** sob o modelo ideal indicado em `#base-umidade` e à mesma T, a pressão de saturação é a mesma: 0,30/0,75 = 0,40. Umidade relativa não é fração de massa. Para mistura real, fator de intensificação pode depender da pressão total; a igualdade é delimitada ao modelo da base.
- **6:** sistema fechado com todas as transferências descritas e ΔEc/ΔEp desprezíveis: Q=−30, W=−180, ΔU=150 kJ e U₂=650 kJ, na convenção Q recebido/W saindo positivos.
- **7:** recipiente rígido isolado, sem outro trabalho, com estados inicial/final em equilíbrio e ΔEc/ΔEp desprezíveis conforme a base: Q=W=ΔU=0 e T₂=T₁ para gás ideal. Para expansão V₂>V₁, ΔS=mR ln(V₂/V₁)>0; não se supõe trajetória real reversível.
- **8:** reação inversa entre os mesmos estados e quantidades tem ΔH=+30 kJ; o PCS inclui a condensação da água dos produtos nas condições de referência. Não se atribui um valor fixo de PCS ao exemplo.
- **9:** no ciclo com apenas as duas fontes indicadas, ηC=1−300/900=2/3 e rejeição mínima =300 kJ. A proposta rejeitando 100 kJ dá ΔS das fontes = 100/300−900/900=−2/3 kJ/K e é inviável. A água pode perder entropia ao congelar se a geração total obedecer à segunda lei.
- **10:** para ambiente uniforme a 280 K e geração total 0,15 kJ/K, Xdestruída=42 kJ. Para substância simples compressível em estados de equilíbrio e composição fixa, ds=0 e v≈0,001 m³/kg ao longo de Δp=600 kPa levam a Δh≈0,60 kJ/kg. O segundo resultado é específico e aproximado.

Os valores são dados didáticos nominais; não há incerteza instrumental informada. Onde há arredondamento, foi comparado com o intervalo correspondente à última casa. Os demais nove diagnósticos não apresentaram divergência nos modelos e limites descritos; esta constatação não é aprovação global do lote nem transfere cobertura a outras ocorrências.

| Critério localizado | Resultado |
|---|---|
| Identidade dos dez blocos na fotografia | Atendida por posições, hashes e extração. |
| Aritmética e unidades | Conferidas nos modelos descritos; diagnóstico 4 é qualitativo. |
| Suficiência do enunciado do diagnóstico 2 | **Não atendida:** mensurando e conexão precisam ser explicitados. |
| Critério integral QA-09 | Não atendido; demais ocorrências e recursos continuam em revisão. |
| Liberação do próximo ID | **Não liberado.** |

Não houve ensaio em navegador real, revisão humana, teste com estudantes ou certificação externa. Qualquer alteração de versão requer mapa e reavaliação de alcance; um aceite parcial não demonstra que o curso seja avançado.
