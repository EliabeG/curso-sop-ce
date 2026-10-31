# QA-09 — candidatas isoladas das fichas 88 e 99

Data: 30/10/2026. Corretor: agente automatizado `/root/next_formulas`. **Candidatas não aplicadas; aguardam auditoria independente.** Respondem ao [parecer das fichas de aplicações r12](../../../pareceres/QA-09-fichas-aplicacoes-r12-auditoria-independente-20261030.md), que identificou condições faltantes no uso isolado. QA-09 permanece em correção e outro ID não é liberado.

## Ficha 88 — pressão intermediária

A proposta acrescenta que os dois estágios de compressão adiabáticos operam **em regime permanente**, preservando o mesmo gás ideal, cp e cv constantes, eficiências isentrópicas iguais e constantes, intercooler até T₁ sem perda de pressão, mesma vazão, ausência de mudança de fase, ΔEc/ΔEp desprezíveis e pressões absolutas p₃>p₁>0 fixas. A hipótese é adicionada no texto visível e no campo de busca; fórmulas e restante do conteúdo permanecem iguais.

Com `a=(k−1)/k>0`, `r₁=pi/p₁`, `r₂=p₃/pi`, razão global r₁r₂ fixa e demais hipóteses do modelo, o trabalho total específico é proporcional a `r₁ᵃ+r₂ᵃ−2`; mínimo em r₁=r₂ e pi=√(p₁p₃). Para pressões fictícias p₁=1 bar e p₃=16 bar, pi=4 bar. Igualdade de vazões por si só pode anular a acumulação de massa sem anular variação da energia armazenada num estágio. Se houver transiente com armazenamento, o balanço contém dEVC/dt; por isso o trabalho não é automaticamente obtido apenas a partir da diferença de entalpias de regime permanente. Não se afirma que todo transiente tenha outro ótimo: os termos adicionais exigem modelagem própria.

## Ficha 99 — geração térmica e fronteira

A candidata mantém regime permanente, `q‴` uniforme ou médio, temperatura da face e do fluido uniformes, h médio, demais faces isoladas, ausência de radiação/outras perdas e h,A>0. Acrescenta que `q‴` é a **geração térmica total considerada** e que não há outros aportes energéticos independentes não incluídos em q‴. Determina não contar duas vezes uma conversão que já esteja incluída na geração. Essa é a contabilidade suficiente para `q‴V=hA(Ts−T∞)` na fronteira e modelo da ficha; não afirma que todo bloco real satisfaça essas hipóteses.

Contraste fictício: q‴V=1000 W e hA=20 W/K fornecem ΔT=50 K quando não há outro aporte independente. Se houver adicionalmente trabalho mecânico de 200 W dissipado internamente e explicitamente **não incluído** na geração de 1000 W, o balanço térmico tem saída de 1200 W e ΔT=60 K. Se a dissipação já estivesse contabilizada na geração total, somar os 200 W outra vez seria erro. O contraste serve para distinguir a fronteira de contabilização, não afirma que o problema original tenha esse eixo.

## Identidade e simulação

Formulário r12 SHA-256 `6857fd83e0b2e49c804903cff1dea4128a665ab22eb27bac4ab15d6c557ff756`; inventário r12 SHA-256 `457a56300aab8f612ebb7f136c7c2f62520abb49c005c209a238925179248d0e`. O manifesto registra posições UTF-16, âncoras e hashes. Cada original ocorre uma vez na fotografia e cada condição aparece duas vezes no bloco para manter texto visível e `data-busca` sincronizados. Arquivos isolados incluem quebra de linha final, excluída dos hashes de fragmento.

| Ficha | Âncora | UTF-16 | SHA original | SHA candidata |
|---|---|---|---|---|
| 88 | `formula-intermediaria` | 209667–212234 | `bd19218dd4ad251d9debfc2b70b19102da7fb7996c82ea98ab2e61582ce7008d` | `ac1e873b4de6822bd57453234a46c8fcea1271d017367aeb97f4330cff7e11e9` |
| 99 | `formula-geracao` | 235945–238888 | `e4b32d03b87cfde282b239623549998f6852a206208271b5c1147773f97fd6db` | `5262a7c0d1bb26b99a8c185827a28f547cf819fa6f3b1455b374a67f29bf17bd` |

`node auditoria/termodinamica/evidencias/QA-09/candidatas-fichas-88-99-r12-20261030/verificar.mjs` confirma fotografia, substituições literais e hashes, simula as mudanças **em memória** e verifica 100 fichas, 98 não alvo byte a byte idênticas e 191 elementos MathML preservados. Também executa os testes fictícios acima e compara razões 2, 3, 4, 5 e 8 para o modelo da ficha 88; a prova geral do mínimo decorre da derivação e não apenas dessa amostra. A execução retornou `ok=true` sem alterar produto; isso não é teste de navegador ou aprovação de FOR-01.

## Encaminhamento

Solicita-se revisão independente das hipóteses, da fronteira energética e dos contrastes, incluindo se a redação de q‴ evita dupla contagem. Se aprovadas e aplicadas, gerar fotografia/mapa novos sem regravar históricos, reconciliar registros e referências, verificar a integridade das outras fichas e o comportamento de busca/revelação, reavaliar o alcance de FOR-01 e auditar a versão efetiva. Não houve revisão humana, teste com alunos ou certificação externa.
