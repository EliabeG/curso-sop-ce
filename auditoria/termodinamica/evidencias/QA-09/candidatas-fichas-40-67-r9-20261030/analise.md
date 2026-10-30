# QA-09 — candidatas isoladas para as fichas 40 e 67

Data: 30/10/2026. Corretor: agente automatizado `/root/next_formulas`. **Não aplicadas**; aguardam revisão de agente independente. Formulário base SHA-256 `cda652563a79c49a6c3d527ad1400c7f7597d33c9b8523ed8a26047b25c69feb`; inventário r9 SHA-256 `023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d`. O manifesto registra âncoras, intervalos UTF-16 e hashes dos fragmentos originais e propostos; arquivos isolados incluem uma quebra de linha final que os hashes dos fragmentos excluem.

## Ficha 40 — pressão e trabalho de fronteira

O [parecer do lote de sistemas fechados](../../../pareceres/QA-09-fichas-fechados-31-41-auditoria-independente-r9-20261030.md) pede explicitar a relação entre a pressão na fronteira e a pressão termodinâmica. A candidata diz que p termodinâmica é constante e que o único trabalho é `Wb=p(V₂−V₁)`, sem outros trabalhos; requer que a pressão de fronteira coincida com p e cita o processo quase estático como exemplo. A condição é repetida em `data-busca` e no texto visível, sem modificar fórmulas MathML, sinal ou explicação de inversão dos mesmos estados.

Motivação: pressão externa constante isoladamente não identifica ΔH como calor. Num contramodelo fictício de gás ideal fechado, pext=100 kPa durante deslocamento, p₁=200 kPa, V₁=1 m³ e p₂=100 kPa, V₂=2 m³: p₁V₁=p₂V₂=200 kJ, então T e U inicial/final coincidem. Sob Wb=pextΔV=100 kJ e sem outros trabalhos, ΔU=0 implica Q=100 kJ, mas ΔH=ΔU+(p₂V₂−p₁V₁)=0. É trajetória irreversível com pressão do gás mudando; **não** é contramodelo ao novo enunciado. Demonstra que uma pressão externa constante sozinha não atende às hipóteses da identidade. Em contrapartida, se a pressão de estado p é constante e a pressão de fronteira usada no trabalho é a mesma, `Q=ΔU+pΔV=ΔH`, com ΔEc/ΔEp desprezíveis.

## Ficha 67 — massa de referência e local do calor

O [parecer do lote de entropia](../../../pareceres/QA-09-fichas-entropia-r9-auditoria-independente-20261030.md) identificou que a relação específica `δqrev=Tds` não deve ficar apresentada sem referência de massa no cartão isolado. A candidata especifica **sistema fechado de massa fixa**, trajetória reversível de referência e T como temperatura absoluta da fronteira onde há calor, igual à do sistema no caminho reversível. A fórmula e suas unidades por massa permanecem iguais; a condição é sincronizada com `data-busca`. O vínculo de retomada é alterado de `#substancias` para `#base-entropia`, que trata expressamente de transferência e geração de entropia.

Um volume de controle permanente não satisfaz automaticamente `ΔSconteúdo=Q/T`: por exemplo, no modelo reversível de uma entrada e saída com ṁ=1 kg/s, calor de 60 kW atravessando a fronteira a 300 K e s₂−s₁=0,2 kJ/(kg·K), a geração é zero, a entropia do conteúdo é constante e Q̇/T=0,2 kW/K é equilibrado pelo transporte líquido de entropia pelas correntes. O contramodelo ilustra por que a massa de referência e a fronteira devem ser identificadas; não invalida uma relação de escoamento deduzida com suas próprias hipóteses.

## Identidade, simulação e limitações

Cada original ocorre exatamente uma vez no formulário base, nos intervalos e hashes do manifesto; as candidatas correspondem a alterações de texto visível/busca e, na ficha 67, ao destino do link. `node auditoria/termodinamica/evidencias/QA-09/candidatas-fichas-40-67-r9-20261030/verificar.mjs` simulou as duas substituições em memória: 100 fichas, 98 fichas não alvo byte a byte iguais, MathML das duas preservado, condições contidas no texto de busca e alvo `#base-entropia` existente; parser sem erros. Não ocorreu teste em navegador nem mudança do produto.

Submeter as candidatas ao Auditor independente, incluindo hipóteses e contramodelos. Se aprovadas e aplicadas, congelar versão, gerar inventário/mapa novos para as posições alteradas, validar 197 artigos, fórmulas/links/persistência, reexaminar alcance de FOR-01 e pedir auditoria da versão efetiva. Nenhuma destas simulações conclui QA-09 nem transfere automaticamente aceites anteriores.
