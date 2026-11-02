# QA-09 — aplicação das hipóteses de pressão, fichas 40/67 e diagnóstico 2

Data: 30/10/2026. Corretor automatizado `/root/next_theory`. Estado: **aguardando auditoria independente da versão efetiva**. Esta aplicação é parte de QA-09, não encerra o ID nem autoriza o seguinte. As candidatas foram aprovadas isoladamente antes da aplicação; essa revisão não equivale a verificação da nova versão.

## Alterações

- Na explicação de combustão, a igualdade Q=ΔH para sistema fechado ficou condicionada a pressão termodinâmica constante, variações cinética/potencial desprezíveis e trabalho de fronteira `W=p(V₂−V₁)`, identificando a pressão que determina o trabalho com aquela usada em H. Na explicação de vaporização de massa fechada, a mesma hipótese de trabalho foi explicitada; o balanço do vaporizador em escoamento permanente foi preservado.
- A ficha 40 explicita o mesmo modelo para Qp=ΔH. A ficha 67 delimita o calor reversível por massa a um sistema fechado e conecta “Retomar na aula” à base de entropia, em vez de `#substancias`. Os MathML são preservados.
- O diagnóstico 2 passa a especificar que o tubo curvo está conectado ao fluido e se deforma pela pressão, evitando que a descrição genérica também identifique um termômetro de bulbo e capilar. A chave e resposta do diagnóstico foram preservadas.

As [candidatas de teoria](../teoria-pressao-entalpia-r9-20261030/entrega.md), [fichas](../candidatas-fichas-40-67-r9-20261030/analise.md) e [diagnóstico](../diagnostico02-candidata-r9-20261030/manifesto.json) foram examinadas em pareceres independentes sobre as propostas: [teoria](../../../pareceres/QA-09-teoria-pressao-entalpia-candidatas-auditoria-independente-20261030.md), [fichas](../../../pareceres/QA-09-candidatas-fichas-40-67-auditoria-independente-r9-20261030.md) e [diagnóstico](../../../pareceres/QA-09-diagnostico02-candidata-r9-auditoria-independente-20261030.md). A alteração de FUN-01 P3, que se situa em artigo, não foi incluída.

## Fotografia, teste e limites

Base r9: aula SHA-256 `2d6b8fb2f9c99e04d22c19d7b32bbc3eb20577459d9132e506f9c0acef3f2fc2`; formulário `cda652563a79c49a6c3d527ad1400c7f7597d33c9b8523ed8a26047b25c69feb`; inventário `023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d`. Versão r10 efetiva: aula `a8bed8a91a36a1c1f41cd75e3c1858fecb4e14a506e582ad1fdb186d275805e3`; formulário `01d5d79639cd17dfcaea38479019cf719e2601f5b35d446ab562e50d381fa5c9`; inventário r10 `3497cbf9ffcbe0a1e2eb84eeb9e34c0cfb6e0ed63a2747795bf75832454e2f6c`.

Os cinco originais foram localizados uma vez, sem sobreposição; seus arquivos isolados e candidatos foram confrontados com os hashes e substituídos literalmente. As fotografias anteriores e posteriores, configuração e edição estão nesta pasta. Após inspeção de saídas dos scripts, `verificar.mjs` (SHA-256 `563adb35ea39d72b2a706af734a3153530663699b9978ad10a85e8e9f1173392`) reconstruiu as duas páginas byte a byte e confirmou 197 artigos e registros individuais íntegros e em ordem, 100 fichas com somente 40/67 alteradas e 734 MathML na aula e 191 no formulário preservados. O inventário oficial foi atualizado somente na referência da fotografia da aula; o Markdown ganhou uma seção histórica.

O gerador r10 foi criado a partir do r9 com destino novo. O mapa r9→r10 SHA-256 `d882301bb56ec469da5bb9b6f0b42f02e908c7dfcbdacaa048d6d0caff552a62` registra 11.397 pares: 11.308 externos e **89 internos que exigem conferência individual**, incluindo a mudança controlada do link da ficha 67. Referências (815) e recursos (138 registros) foram confrontados separadamente; 197 artigos segregados permanecem idênticos. O mapa não transfere automaticamente aceites; reavaliar alcance de FUN-01/02, FOR-01, BAN e lotes QA-09 em função de mudanças de versão.

O validador canônico retornou `ok=true`, 197 itens, 29 recursos e 1.263 links, sem erro ou aviso. Isso é teste estrutural/documental, não certificação científica ou avaliação de aprendizagem. Não houve ensaio de navegador real nesta aplicação. O Auditor deve verificar independentemente os cinco deltas, os 89 pares internos, referências/recursos, o vínculo da ficha 67, os registros, testes e o impacto nas aprovações anteriores.

## Outros hashes

| Artefato | SHA-256 |
|---|---|
| `config.json` | `90847a0610086d77148227d454d1707d725406e2afa7eb5cc85693f830ad5735` |
| `edicoes-aplicadas.json` | `71d49118f80763221128adce6c15c17a6371362c56203a0131d230d587248d8a` |
| `resultado.json` | `50587f44aa518ce4d4c9a4c345f7ab812e1deed0be2fb460868fa82c01efa926` |
| Inventário oficial JSON | `2362fd386e0b7d1cb31b978a6c513114457e47bfccdda49f8017cba5cea87f88` |
| Inventário oficial Markdown | `3076d517ccf106ce414b708b04eaa74771da04256c03cfb45d39d34fd3177cc9` |

As aprovações de propostas e a execução do script não constituem parecer sobre a versão r10. Não foram produzidas revisão humana, aplicação com alunos ou certificação externa; QA-09 permanece em correção e o próximo ID bloqueado.
