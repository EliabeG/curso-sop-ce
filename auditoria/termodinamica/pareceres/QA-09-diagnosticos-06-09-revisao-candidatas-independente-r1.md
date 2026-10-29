# QA-09 — Revisão independente das candidatas isoladas dos diagnósticos 6 e 9, r1

Data: 29/10/2026. Responsável: apoio independente automatizado. Escopo pontual, sem editar produto/controle nem aprovar QA-09. Ambas são **tecnicamente adequadas à correção dos pontos adjudicados**, sujeitas à aplicação controlada e à revisão da versão efetivamente aplicada.

## Versão e delta

A fonte examinada é `modulos/e1-termodinamica.html`, SHA-256 `0de7342b99b9ebef8c1526f0b8eefb3544f000a4546d7b500558550d178285eb`; o inventário de QA-09 é `auditoria/termodinamica/evidencias/QA-09/inventario-r3.json`, SHA-256 confirmado `3074ab8fdf511d68dce73ec97bacca9dd9d5b0bbc3fe07a7d4ce329669b8b446`. Cada fragmento original ocorre exatamente uma vez no HTML atual. Independente comparação de bytes confirma, para cada candidata, a igualdade entre seu fragmento e o original com a única substituição literal declarada em seu manifesto. Arquivos isolados incluem nova linha final e por isso possuem hash distinto do fragmento exato.

Diagnóstico 6: inseriu “Essas são as únicas transferências de energia pela fronteira.” Isso exclui o trabalho elétrico adicional do contramodelo do parecer `QA-09-adjudicacao-diagnosticos-06-08-independente-r1.md` SHA-256 `c3274ddb3173fcefc01df73991022bc57b08534f6cc43d3505117e9c16f7d7bc`. Preservou dados, perguntas, resposta, link, marcação e indicação de outras variações inexistentes. Com a convenção da aula e a ausência de variação cinética e potencial aí ensinada, Q=−30 kJ, W=−180 kJ, ΔU=Q−W=150 kJ e U₂=500+150=650 kJ; igualdade para dados nominais, sem arredondamento. A candidata não precisa alterar a resolução.

Diagnóstico 9: o enunciado passa a dizer que a máquina térmica opera em ciclos com trocas de calor apenas com duas fontes a 900 K e 300 K, recebendo ao todo 900 kJ da quente e rejeitando ao todo 100 kJ à fria no mesmo ciclo. Mantém as duas perguntas, resposta, links e marcação. Cumpre as condições da adjudicação `QA-09-adjudicacao-diagnosticos-07-09-independente-r1.md` SHA-256 `9fc1f260835e3b520256994b5aea937fbd3fa9d1e6ee23464ebc6246da327324`. A máquina cíclica retorna a seu estado inicial, ΔS_máquina=0, e ΔS_fontes=−900/900+100/300=−2/3 kJ/K; contraria a segunda lei. Na leitura alternativa da solução, ηC=1−300/900=2/3 e Qfrio,mín=900×300/900=300 kJ, superior aos 100 propostos. A água pode perder entropia ao congelar desde que o conjunto obedeça à segunda lei. Exato para dados nominais; sem arredondamento. A candidata exclui acúmulo líquido por ciclo do contramodelo não cíclico e corrige sua ambiguidade.

## Identidade e aplicação

Ambos são `div.exemplo` em `#preparacao-questoes`, fora dos 197 artigos BAN-08 e sem alternativas ou gabarito pontuável. A inspeção de `assets/curso.js` SHA-256 `a20f4d19158073a9a1c48aabdfba8fa863b02063e16061c00b16448a6ccc2e13` mostra seletores de pontuação `article.questao` e `.concurso-item, .avalia-item`, que não incluem esses blocos. Conclusão estática: os deltas propostos não alteram digitais de perguntas pontuadas nem suas respostas, na implementação examinada. Não houve teste de navegador ou do estado salvo. As âncoras `#preparacao-questoes`, `#base-balanco-fechado`, `#base-carnot-prova` e `#base-entropia` ocorrem uma vez na fonte; os vínculos nos fragmentos foram preservados.

Após aplicação, conferir os dois deltas efetivos, preservação dos artigos e código, vínculos, identidade/progresso e fotografia dos inventários e aceites dependentes. Esta revisão isolada não prova aplicação, testes de regressão ou aceitação global. Referências anteriores a qualquer mudança continuam associadas à versão e ao alcance que examinaram.

## Hashes da evidência SHA-256

| Evidência | Diagnóstico 6 | Diagnóstico 9 |
|---|---|---|
| Fragmento original | `d6834093a3d7ebc5c8058689cf3e6c9c9721d66da12b929051a411ef495e246f` | `72a42e3735925949b6977964389d48aa363720f9cfadb69ecdebcad19f92bdc4` |
| Fragmento candidato | `c81bcd183b4118a4e1821542d5b71325f1bb44509c081143d3f89b9eb17e425c` | `ea5b9c8b4c01bbc1846f6364b463f204c68a7c6d6ea799714b19a54100860d53` |
| Arquivo original | `470266ea5dd47ee9674f9bd1c4db8c3e6036f0b1e79db69579219110408f255a` | `29dfa5aba6389f9d0b1b57b02344fb83ad9628a939e104a8aaaf2a601a9dfc8c` |
| Arquivo candidato | `7e4642e6323e1c01e799b535e1672bf4ec557f287e7d2d7022b594dc1b28654e` | `01dc8874860961ea2d8ee239fa00da8ab31a41f5b0e7e8587114bfa325e7d8e8` |
| Manifesto candidato JSON | `c52eb1378607fdee0fc1d76b0ae5688aa491b5bad9e3ccef1744b5555f734fc7` | `75ddabf5fabd1e9afec00f838c29954be614eb9ddacf993f79d14ee92f8fdbfc` |
| Análise candidata do Corretor | `ad21d05a04cde1543ff0f99fcb803328978d41c2bde2038822219b45ca43aa7a` | `9d1b4e364eedda5aaf2613472d2e66a8fffb5f32613a04ba6e03132919a91e41` |

Os arquivos se encontram em `auditoria/termodinamica/evidencias/QA-09/` com nomes `diagnostico06-*` e `diagnostico09-*`. Os hashes anunciados nos manifestos correspondem aos bytes conferidos.
