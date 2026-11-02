# QA-09 — auditoria independente do lote de exergia r30

30/10/2026. Auditor `/root/next_formulas`; autor `/root/next_theory`. **APROVADO NO RECORTE**, com limitação de fontes externas abaixo. Não aprova toda a exergia, o banco ou QA-09. Vínculos: auditei os diagnósticos D06–10 e D21–25 na r27 em `auditoria-diagnosticos-r28-2-next-formulas-20261030/parecer.md`, SHA-256 `1f297c78f140f228419db4a2fabdc16a2ef0753e29e0f34198139fa56b79e4eb`, e a rastreabilidade da ponte r30 que inclui AV-37. D10 foi relido nesta foto, mas não reivindico nova avaliação científica independente da minha revisão histórica dele.

## Identidade e verificação

Entrega `exergia-r30-lote2-next-theory/entrega.md` SHA `0bdc39c7d8d70da4da343a3fc380f07bbcb966e12f4ddf40e349eebe39fabbca`; `verificar.mjs` `8925cb1786a864a619480256684b94f8416e671ff3ba09eeaadb3cb25c7ce722`. Executei `node auditoria/termodinamica/evidencias/QA-09/exergia-r30-lote2-next-theory/verificar.mjs`: retornou `ok:true` com os três intervalos/hashes da entrega e figura `222735fab01e54a81e34f3bb54cfd7097a8cbc1391ebe6420d60df8b2513a9cb`. O hash da aula ativa corresponde à foto r30 `c719adae3464fb56ed2b0ad7014e0721c0aab2da444fb484ec0b40c5c0c8fbd4`. O SHA do recorte AV-37 `b741f7c26e317df09eaf7984e2065f881464ffc7367202fa2968b4ce30efe928` coincide com o parecer histórico `BAN-08-apoio-av36-40-r1-independente.md`, SHA `97979be4c4644c24ff0514f33c9334e2de98d2fe6d1768a6833f3d31e8d866ed`, e com a entrega `graficos-r28`; isso não transfere por si só aceite científico.

Li os três recortes, a base vinculada de exergia e a base Gibbs, e vi o PNG local. O gráfico apresenta disponibilidade versus ângulo de manivela, sem escala numérica vertical de energia; AV-37 explicitamente independe dos valores das curvas. O PNG está sem diferença local em relação ao commit `093eef7`, sem que isso prove origem oficial externa.

## Contas e condições

- **D10:** 280 K×0,15 kJ/K=42 kJ de exergia destruída; Δh≈vΔp=0,001 m³/kg×600 kPa=0,60 kJ/kg. A primeira grandeza é total, a segunda específica. A identidade dh=Tds+vdp exige propriedades de equilíbrio de substância simples compressível e composição fixa; aproximar a diferença finita por vΔp exige trajetória isentrópica entre estados de equilíbrio e v aproximadamente constante. A base `base-gibbs` fornece essas condições. A diferença de entalpia não determina, por si, trabalho de eixo de dispositivo arbitrário.
- **CR-37:** o enunciado universal de que mais irreversibilidade sempre produz mais trabalho é incorreto; o gabarito E é compatível. Para ambiente a T0 constante, W perdido=T0Sger mede destruição de exergia no contexto da referência reversível apropriada. A comparação de trabalho requer mesmas restrições e condições, incluindo tratamento de entradas e saídas; não se mede energia pelas áreas da figura angular.
- **AV-37:** 300 K×0,20 kJ/K=60 kJ, alternativa C. A operação com 26,85 °C gera 5,37 numericamente, porém é inadequada pois T0 do produto é absoluta; a conta usa dados do enunciado, não o eixo horizontal da figura. Sger positivo para T0 positivo implica perda de capacidade útil não negativa na comparação considerada.

## Fontes e limites

A entrega declara tentativas anteriores de acesso ao MIT sem conteúdo e não afirma acessibilidade atual; repeti tentativas de abertura de ambas as fontes citadas e o serviço retornou erro sem conteúdo. Não verifico, portanto, a disponibilidade atual dos links ou o conteúdo das páginas nessa rodada. Os pareceres históricos indicam consulta às fontes, mas não tomo esse registro como nova verificação externa. As imagens foram examinadas como arquivos locais, sem navegador, zoom em contexto, leitor de tela ou estudantes; não houve revisão humana ou certificação externa. Produto, banco e evidência examinada não foram alterados.
