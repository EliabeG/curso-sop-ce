# QA-09 — auditoria independente das candidatas das fichas 88 e 99

Data: 30/10/2026. Auditor: agente automatizado `/root/next_graphics`, distinto do Corretor `/root/next_formulas`. **APROVADO somente para as duas propostas isoladas**, ainda não aplicadas. Não se aprova a versão posteriormente aplicada, FOR-01 global ou QA-09 integral; outro ID não está liberado.

## Escopo, versão e reconstrução

As candidatas respondem ao parecer `QA-09-fichas-aplicacoes-r12-auditoria-independente-20261030.md`, que solicitou explicitar regime permanente em 88 e contabilidade das fontes em 99. Formulário r12 SHA-256 `6857fd83e0b2e49c804903cff1dea4128a665ab22eb27bac4ab15d6c557ff756`; inventário r12 SHA-256 `457a56300aab8f612ebb7f136c7c2f62520abb49c005c209a238925179248d0e`. A análise da proposta tem SHA-256 `fa74d47ca721287582f2846437f753fe45901e179bc0ab0730b2c752ea25b0f9`; manifesto `02a4abfebd9edef1e62439894097288e9a8bc3ad0670f6d3e5e26420bad7200f`.

O script de leitura independente `evidencias/QA-09/auditoria-candidatas-fichas-88-99-r12-20261030/verificar.mjs`, SHA-256 `9ad4a7b03b1ea16a813400f09133c77e630043ded3f830446f782ecb126478d1`, confirmou hashes dos arquivos e fragmentos, intervalos UTF-16 e unicidade na fonte, e reconstituiu cada candidata por duas substituições idênticas: uma no texto visível e outra em `data-busca`. Simulando em memória as duas substituições, preservam-se a ordem e IDs das 100 fichas, os 98 blocos não alvo byte a byte, os 191 elementos MathML e os atributos dos dois artigos exceto `data-busca`. A simulação tem SHA-256 `5f3f31a4801f96a2b78b40c75d37392f6b16d264901ac313ac00458901970285`. Isso não prova renderização, filtro funcional nem aplicação real.

## Ficha 88

A proposta acrescenta “em regime permanente” aos dois estágios, preservando gás ideal, cp e cv constantes, mesma eficiência isentrópica constante, intercooling até T₁ sem perda de pressão, mesma vazão, sem mudança de fase e ΔEc/ΔEp desprezíveis; p₃>p₁>0 em valores absolutos. Sob esse modelo, a soma de trabalhos específicos dos estágios é proporcional a `r₁ᵃ+r₂ᵃ−2`, onde `a=(k−1)/k>0` e `r₁r₂=p₃/p₁` fixo; a desigualdade aritmético-geométrica atinge a igualdade quando `r₁=r₂`. Assim `p_i=√(p₁p₃)` e para 1 e 16 bar absolutos obtém-se 4 bar. Em regime não permanente, igualdade das vazões não elimina necessariamente acumulação de energia; o modelo estacionário precisa dessa condição. A alteração atende ao ajuste solicitado no alcance da ficha.

## Ficha 99

A proposta define `q‴` como geração térmica total considerada, uniforme ou média no volume, inclui as conversões contabilizadas e exclui aportes adicionais independentes não incluídos em `q‴`, preservando regime permanente, demais faces isoladas, ausência de radiação/outras perdas, temperaturas uniformes e h médio na face. Para `q‴V=1000 W` e `hA=20 W/K`, decorre ΔT=50 K. Se um aporte externo de 200 W estivesse fora dessa geração, o balanço passaria a 1200 W e ΔT=60 K; a proposta exclui tal aporte para a equação publicada. Se dissipação já compuser a geração total, não se somam novamente os 200 W. Esse contraste é apenas um cenário de contabilidade energética, não alegação de eixo ou equipamento real. A redação torna explícita a fronteira do modelo sem duplicação das fontes.

## Decisão e aplicação futura

| Critério | Resultado |
|---|---|
| Identidade, duas alterações por ficha e sincronização com busca | Atendido na fotografia r12 e simulação. |
| Hipóteses e dedução da ficha 88 | Atendido no modelo descrito. |
| Fronteira energética e não duplicação na ficha 99 | Atendido no modelo descrito. |
| Preservação estrutural do restante do formulário | Atendido na simulação; 98 fichas e 191 MathML idênticos. |
| Aplicação efetiva, FOR-01 e QA-09 integral | Não examinados/não atendidos por esta aprovação isolada. |

Se aplicadas, congelar a versão atual e gerar inventário e mapa novos; reconciliar as posições, referências e recursos; verificar as fichas não alvo, busca/revelação e dependências e solicitar auditor independente da versão efetiva. Reavaliar FOR-01 no alcance afetado, sem transferir o aceite anterior por simples hash ou por este parecer. Não houve navegador real, leitor de tela, teste com alunos, revisão humana ou certificação externa.
