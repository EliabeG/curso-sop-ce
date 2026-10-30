# QA-09 — revisão independente da candidata FUN-01 sobre v e ρ

Data: 30/10/2026. Revisor: agente automatizado `/root/qa_examples`. **Veredito localizado: APROVADO para a candidata isolada**, sujeito à verificação da versão efetivamente aplicada e das dependências. Não há aprovação integral de QA-09 nem liberação de outro ID. Este exame não comprova que a candidata tenha sido aplicada ao produto.

## Escopo e identidade

A candidata responde ao achado documentado no [parecer anterior](QA-09-fun01-textos-tabela-auditoria-independente-20261030.md): valores recíprocos de volume específico e densidade não identificam a procedência das leituras. Fonte examinada `modulos/e1-termodinamica.html`, SHA-256 `200f9b773050594d762cc596a5a89297024b245fc4f504081fc77baaed3db95f`; localização `fun01-parecer`, início UTF-16 114112 no inventário r7 `5090b9897a4698e0ad090f45182afba5880361aabc9fd3c3bdf848d971a85a1a`. O original ocorre uma vez no HTML e sua extração pela posição r7 coincide byte a byte com o fragmento isolado. O candidato não ocorre no HTML atual.

Li os dois parágrafos isolados e verifiquei que trocar uma única vez a frase indicada no manifesto produz a candidata integralmente, preservando o restante da estrutura. Hashes SHA-256 de fragmentos sem a quebra final dos arquivos: original `bdcd77b078906b6727248748ec8a21ff50fb891522a0aa61b62fc5cddd07294f`; candidato `7bc490923640adfe4d11c52c12ac26f4281bd51a46c348d1836e8807eed886d4`. Arquivos com quebra final: original `8e3356849c04119255f3a2d309e5fc59423a4b25c70d7528d655d4b97f40ea2e`; candidata `8f6646b348f707e126276ee8a7d9dcf66f8abede57ebb5cf688023b1c9b99e43`; análise do Corretor `896115b15e5d5badfaa068eaa53f0bbd27548241be284c6abcd5836460e9bd5f`; manifesto `dd715d6f108d56903b33623e43a19146971dd01cde7dac86a49eaff6e5a7a2e8`.

## Julgamento e contramodelo

Para a mesma amostra homogênea e instante, v=0,004 m³/kg e ρ=250 kg/m³ satisfazem ρv=1. Como propriedades de estado, as grandezas são mutuamente dependentes: ambas não fornecem dois graus de liberdade independentes. Dois equipamentos poderiam, no entanto, produzir leituras nominais compatíveis sem uma ter sido obtida da outra por inversão. Assim, a proposta elimina a afirmação não fundamentada quanto à origem das leituras e mantém a conclusão termodinâmica justificada. O contexto ainda diz que se deve escolher uma propriedade adicional independente, por exemplo T somente na região e modelo em que (T,v) sejam independentes. Os valores são nominais e não demonstram, sem incertezas, concordância metrológica certificada ou falha de sensor.

A candidata altera uma frase de um exemplo em FUN-01; não altera artigos pontuados, mas isso é conclusão da inspeção estática da candidata, não de uma aplicação que ainda não ocorreu. Em caso de aplicação, é necessário verificar toda a versão efetiva, reconciliar documento, contexto, posição e hash nas fotografias e inventários, conferir os 197 artigos e registros, e analisar o alcance dos aceites FUN-01 e demais dependências. Aceites anteriores não são automaticamente transferidos para novo hash.

| Critério localizado | Resultado |
|---|---|
| Identidade e delta da candidata | Atendido no arquivo e fotografia acima; substituição exata e única. |
| Aritmética e conclusão científica | Atendido para o modelo de mesma amostra; independência das leituras não é confundida com independência das propriedades. |
| Aplicação e revalidação em produto | Não examinadas porque a candidata não foi aplicada. |
| QA-09 integral e próximo ID | Continuam pendentes; não liberados. |

Não houve teste em navegador, revisão humana ou aplicação com estudantes. O veredito local não certifica o curso nem o lote FUN-01 completo.
