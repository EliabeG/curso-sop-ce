# QA-09 — auditoria independente das candidatas de CO₂, fichas 52/53, r11

Data: 30/10/2026. Revisor automatizado independente `/root/next_theory`, distinto do Corretor `/root/next_formulas`. **Veredito: APROVADO para as candidatas isoladas no alcance abaixo.** Elas ainda não foram aplicadas: é necessária nova fotografia, teste e auditoria da versão efetiva. QA-09 integral não está aprovado nem o próximo ID liberado.

## Critério, versão e identidade

QA-09 exige conferir todo o conteúdo numérico além dos 197 artigos com referências e resultados verificáveis. Esta proposta responde somente à [ressalva das fichas 52/53](QA-09-fichas-escoamento-r10-auditoria-independente-20261030.md): a geração volumétrica G precisava de referência explícita à mesma T,p do ambiente e da ventilação. O critério curricular comum não se completa com essa correção isolada.

Formulário examinado SHA-256 `01d5d79639cd17dfcaea38479019cf719e2601f5b35d446ab562e50d381fa5c9`; inventário r11 `720f2b9ace69ab8f07be685d5205040569cc72814f67d51d44786872469c07d7`. Apesar da mudança do HTML da aula desde r10, o formulário permanece byte a byte igual; conferi as posições e hashes no inventário r11 em vez de transferir aceite automaticamente. [Análise](../evidencias/QA-09/candidatas-co2-52-53-r11-20261030/analise.md) SHA-256 `060b2e857e880fc7302caa61f25b2cce0261477f54892a0da2540f302a3b6bdc`, [manifesto](../evidencias/QA-09/candidatas-co2-52-53-r11-20261030/manifesto.json) `43430cb2d539ad51ebd21e157b04f56b11247f6e1641600c360f87d8f37a04d1`.

Cada fragmento original aparece uma única vez no formulário e confere com seção, âncora, intervalos UTF-16 e hashes r11. A substituição da condição original pela nova ocorre duas vezes em cada cartão, no texto visível e no atributo `data-busca`; reproduzi os quatro deltas literalmente e comparei com os candidatos. As fórmulas, títulos, links e demais atributos relevantes permanecem iguais.

## Ciência e testes

As candidatas preservam o modelo de zona única bem misturada, CO₂ diluído, volume/densidade constantes, balanço de entrada/saída e demais hipóteses, e explicitam G e vazões volumétricas na mesma temperatura e pressão do ambiente. Dados em outra base devem ser convertidos. Para gás ideal e pressão comum, um fluxo de 0,010 m³/h de CO₂ referido a 600 K equivale a 0,005 m³/h a 300 K. Com V=300 m³, V̇=30 m³/h e Ce−Ci=−0,0002, o balanço dá `(0,005−0,006)/300×10⁶ = −3,333… ppm/h`. Empregar a vazão volumétrica sem convertê-la daria incorretamente +13,333… ppm/h. Com Ci−Ce=0,001, a vazão estacionária usando G convertido é 5 m³/h. São valores artificiais; se pressões diferirem, a conversão também as deve considerar. A base da aula já indica referências comuns das vazões; as candidatas tornam G explícito no cartão isolado.

O [teste independente read-only](../evidencias/QA-09/auditoria-candidatas-co2-52-53-r11-20261030/verificar.mjs), SHA-256 `2ca55a4a6f05a33b5e4fa84d7c5d56a15fd7f7bd92d3078a459c7eb21ecdb72b`, passou: confirmou hashes, duas ocorrências alteradas por ficha, 100 cartões, 98 não alvo idênticos, 191 MathML preservados e atributos de identidade, links e ARIA selecionados iguais na simulação. Também executei o verificador read-only do Corretor, com resultado compatível. Não foi alterado o formulário real e a simulação não testa a apresentação ou filtros em navegador.

As relações foram confrontadas com [NISTIR 6729, equação 4](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=860846), para o balanço em zona única, e [NASA, equação do gás ideal](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/equation-of-state-ideal-gas-2/), para conversão de estados de referência. Fontes consultadas em 30/10/2026, sem atribuir os dados artificiais a elas.

| Critério localizado | Resultado |
|---|---|
| Identidade de originais/candidatas e versão | Atendido em r11, com hashes e reconstrução literal. |
| Domínio e cálculo com bases volumétricas | Atendido nos modelos e limites expressos. |
| Texto visível, busca, estrutura e MathML na simulação | Atendido por inspeção estática; navegador ainda não testado. |
| Aplicação real, FOR-01 e QA-09 integral | Não atendidos por esta proposta; exigem nova revisão da versão aplicada e reconciliação. |
| Liberação do próximo ID | **Não liberado.** |

Após eventual aplicação, verificar fotografia, mapa, links e busca/revelação pertinentes, revisar o alcance de FOR-01 e solicitar novo parecer independente. Não houve revisão humana, teste com alunos ou certificação externa.
