# QA-09 — reconciliação das fichas 31–41 de sistemas fechados r20

30/10/2026. Corretor `/root/next_formulas`. **Aguardando Auditor independente.** As fichas já foram examinadas na r9 e a 40 foi corrigida e auditada na r10; esta rodada reconcilia e reexamina relações na r20, sem transformar revisão antiga em aceite automático. Produto não alterado e QA-09 aberto.

## Identidade e alcance

Formulário r20 SHA `694ee3d26e8f5679d565986cfb0ad8c10aa98667fc8ffb62a569a87679847a58`, aula r20 SHA `b05a68731a6975755c0030c524e7915d7833aacb176f680b3890fe82efc803e7` e inventário r20 `e548f61cde56f676dd0c670924bd58e7012a2f80229231de6560cbb55831adf4`. Preservados formulários r9 `cda652563a79c49a6c3d527ad1400c7f7597d33c9b8523ed8a26047b25c69feb` e r10 `01d5d79639cd17dfcaea38479019cf719e2601f5b35d446ab562e50d381fa5c9`. Os 11 artigos são idênticos aos da r10; dez também são idênticos aos da r9, com a 40 corrigida em r10. Parecer de fichas r9 SHA `15d4bb62a3f856d89f4262e148ed2b6455a4ede9018acc018b25fc99f382d0cd`; auditoria da aplicação r10 SHA `26a166c526f7b2be922ba90bb13870c90e2b4a6066213fabfbf39affd7c60ffc`.

`identidades.json` SHA `429cc00638df43bd13e7fb649901bba5b20daf25432623ecf0722a40e2319d1f` registra 11 IDs, hashes e intervalos UTF-16 em cada foto; `verificar.mjs` SHA `efad98dc3383557a714d05c2e3572f3eacdeb3786e2c78fef8dc1f27ec00420f` é somente leitura e confirmou identidades, 12 destinos de links existentes e cálculos. Executado como `node auditoria/termodinamica/evidencias/QA-09/fichas-fechados-reconciliacao-r20-20261030/verificar.mjs`, retornou `ok=true`. Sua checagem de links não testa navegação ou significado do destino. Reabri os contextos de primeira lei, trabalho, expansão livre e termoquímica: são pertinentes no alcance examinado; o link da ficha 41 vai à seção geral de energia, não a uma âncora especificamente da definição. Nenhuma conclusão abrange integralmente os destinos.

## Relações e hipóteses

Valores seguintes são sintéticos e nominais, não medições ou dados das fontes.

| Fichas | Revisão |
|---|---|
| 31–33 | Sistema fechado com Q recebido e W produzido positivos: ΔU+ΔEc+ΔEp=Q−W; Q=100, W=30, ΔEc=10, ΔEp=−5 kJ dão ΔU=65 kJ. Com ΔEc/ΔEp desprezíveis, U₁=200, Q=100, W=30 dão U₂=270 kJ; em modelo adiabático, W=−250 implica ΔU=+250 kJ. Adiabático não exige trabalho nulo. |
| 34–35 | Trabalho de fronteira em processo quase estático com p representando pressão da fronteira: Wb=∫p dV; p constante dá Wb=pΔV. p=100 kPa e volumes 0,5→0,2 m³ dão −30 kJ; não equivale a trabalho elétrico ou de eixo. Não aplicar pressão interna de equilíbrio a expansão livre irreversível. |
| 36 | Gás ideal de massa/composição fixas, isotérmico e reversível, somente trabalho de fronteira e ΔEc/ΔEp desprezíveis: ΔU=0, W=mRT ln(V₂/V₁)=Q. Para m=1 kg, R=0,287 kJ/(kg K), T=300 K e V₂/V₁=2, W≈59,679972 kJ; argumento positivo e adimensional. |
| 37 | Gás ideal de massa/composição fixa, capacidades constantes e só trabalho de fronteira: com ΔEc/ΔEp desprezíveis, isocórico dá Q=mcᵥΔT; isobárico quase estático dá Q=mcₚΔT. m=1 kg, cv=0,718, cp=1,005 kJ/(kg K), ΔT=100 K dão 71,8 e 100,5 kJ. A condição quase estática vincula pressão termodinâmica à fronteira no processo isobárico. |
| 38 | Retorno ao mesmo estado implica ΔU=0; sem variações líquidas de Ec/Ep, Qlíq=Wlíq, somas algébricas numa mesma fronteira por ciclo. Entrada 500 e saída 300 kJ dão Qlíq=Wlíq=200 kJ, sem exigir cada transferência nula. |
| 39 | Recipiente externo fechado, rígido e isolado, gás ideal e vácuo, sem outros trabalhos, estados de equilíbrio e ΔEc/ΔEp desprezíveis: Q=W=ΔU=0, T₂=T₁. Para m=1 kg, R=0,287 e V₂/V₁=2, ΔS=Sger≈0,198933 kJ/K. Avaliação via caminho reversível auxiliar não torna reversível a expansão real. |
| 40 | Sistema fechado, pressão termodinâmica p constante, Wb=p(V₂−V₁) à mesma pressão, nenhum outro trabalho e ΔEc/ΔEp desprezíveis: Qp=ΔH. Reação inversa entre mesmos estados troca sinal; ΔHdireta=−250 kJ dá Qp=−250 e ΔHinversa=+250 kJ. A ficha atual explicita a condição da fronteira corrigida na r10. |
| 41 | Definição de propriedade específica h=u+pv: u=500 kJ/kg, p=200 kPa e v=0,5 m³/kg dão h=600 kJ/kg. pv tem interpretação de trabalho de escoamento em volume de controle; a definição de h também vale para estados de sistema fechado. |

## Fontes e pedido de revisão

Consultei [MIT, calor e trabalho](https://ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_3.htm), [MIT, primeira lei](https://ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_4.htm), [MIT, entropia e expansão livre](https://ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_7.htm), e [MIT, entalpia e Q=ΔH no processo a pressão constante](https://web.mit.edu/16.unified/OldFiles/www/FALL/thermodynamics/notes/node17.html). Fontes sustentam modelos e conceitos, não os dados sintéticos. Não identifiquei divergência no alcance apresentado; solicito Auditor distinto para texto, MathML, hipóteses e fontes, especialmente 37 e 40. Não houve navegador real, leitor de tela, alunos, revisão humana ou certificação externa.
