# QA-09 — candidatas de referência volumétrica de CO₂, fichas 52 e 53

Data: 30/10/2026. Corretor: agente automatizado `/root/next_formulas`. **Candidatas isoladas não aplicadas; aguardam auditor independente.** Respondem ao [parecer das fichas de escoamento](../../../pareceres/QA-09-fichas-escoamento-r10-auditoria-independente-20261030.md), que exigiu explicitar a referência de temperatura e pressão da geração volumétrica G. O presente trabalho não encerra QA-09 nem altera o produto.

## Proposta e pressupostos

As condições das fichas 52 e 53 já indicavam vazões de entrada/saída iguais e referidas à mesma T,p, mas não explicitavam G na mesma base. As propostas mantêm os demais pressupostos de zona bem misturada, CO₂ diluído, volume/densidade constantes, demais termos e hipóteses originais. Passam a dizer, no texto visível e no `data-busca`, que **G e vazões volumétricas são referidas à mesma temperatura e pressão do ambiente**, com orientação para converter dados fornecidos em outra base. A aula vinculada já menciona bases comuns: a proposta torna explícito G no uso do cartão isolado, sem declarar ausência da condição na aula.

Teste artificial a pressão comum e gás ideal: G=0,010 m³/h referido a 600 K equivale a G=0,005 m³/h referido a 300 K. Com V=300 m³, V̇=30 m³/h, Ce=0,0004 e Ci=0,0006, `V dCi/dt=0,005+30(0,0004−0,0006)=−0,001 m³/h`, logo `dCi/dt=−3,333… ppm/h`; inserir 0,010 sem converter levaria indevidamente a +13,333… ppm/h. Em regime estacionário com Ci−Ce=0,001, a mesma geração convertida conduz a V̇=5 m³/h; sem conversão seriam 10 m³/h. Esses valores e os estados de referência são fictícios, não medições. A conversão volumétrica apresentada depende do modelo de gás ideal e de mesma pressão; condições reais e eventuais mudanças de pressão exigem tratamento apropriado.

## Fotografia, alterações e testes

Formulário efetivo SHA-256 `01d5d79639cd17dfcaea38479019cf719e2601f5b35d446ab562e50d381fa5c9`; inventário r11 SHA-256 `720f2b9ace69ab8f07be685d5205040569cc72814f67d51d44786872469c07d7`. A foto r10 usada no parecer anterior possui o mesmo hash do formulário, mas este relatório usa r11 e suas posições, que devem ser verificadas novamente se a base mudar. Os fragmentos completos do manifesto não incluem a quebra final presente nos arquivos isolados.

| Ficha | Âncora | UTF-16 r11 | SHA do original | SHA da candidata |
|---|---|---|---|---|
| 52 | `formula-co2-acumulacao` | 121580–123793 | `8ce00d9f1adb37ebc9b4a2783948e38e34a17fad813efe8127c922c97308fa6b` | `3e7f4a7e5f4c49d0914f8881a2ffc62a4e1ea895ceaf77c2fbdae5ee68281d1d` |
| 53 | `formula-co2-vazao` | 123793–126178 | `a05f1641032fd9994aa0074665cb6f1a0a2c86559f48c09f232ca5008ec1f4cc` | `be2df2385b16a3759823685d69f4740f82e657439185fc796de952e9cf3306bb` |

`verificar.mjs` lê as fotografias e fragmentos, verifica a troca literal de duas ocorrências de condição em cada bloco, compara a simulação com o arquivo efetivo e confirma 100 fichas na mesma ordem, 98 não alvo idênticas e os 191 MathML preservados. Recalcula o exemplo artificial acima. O script produz resultado apenas em memória/saída padrão; executado na raiz com `node auditoria/termodinamica/evidencias/QA-09/candidatas-co2-52-53-r11-20261030/verificar.mjs`, retornou `ok=true`. Essas verificações estáticas não são ensaio em navegador, revalidação integral de FOR-01 nem julgamento independente do mérito.

## Encaminhamento

Auditor independente deve confrontar modelos, conversão, identidade, extensão e compatibilidade da condição com a base da aula. Se aprovadas e aplicadas, produzir nova fotografia e mapa sem regravar históricos, conferir os vínculos, 100 fichas, 191 MathML, comportamento de busca/revelação pertinente e efeito nos aceites FOR-01, e auditar a versão realmente aplicada. Não declarar QA-09 integral aprovado a partir desta parcela.
