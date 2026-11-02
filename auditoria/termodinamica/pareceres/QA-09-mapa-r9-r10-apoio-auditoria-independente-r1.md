# QA-09 — apoio independente ao mapa r9→r10

Data: 30/10/2026. Revisor: agente automatizado `/root/next_graphics`, distinto do Corretor da aplicação. **APROVADO no escopo documental do mapa e da preservação aqui examinados.** Esta avaliação apoia o Auditor principal; não substitui o exame científico das cinco alterações, não aprova QA-09 integral e não libera outro ID.

## Versão e escopo

Aula r9: `2d6b8fb2f9c99e04d22c19d7b32bbc3eb20577459d9132e506f9c0acef3f2fc2`; aula r10: `a8bed8a91a36a1c1f41cd75e3c1858fecb4e14a506e582ad1fdb186d275805e3`. Formulário r9: `cda652563a79c49a6c3d527ad1400c7f7597d33c9b8523ed8a26047b25c69feb`; r10: `01d5d79639cd17dfcaea38479019cf719e2601f5b35d446ab562e50d381fa5c9`.

Inventários r9 e r10: `023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d` e `3497cbf9ffcbe0a1e2eb84eeb9e34c0cfb6e0ed63a2747795bf75832454e2f6c`; mapa `mapa-correspondencia-inventario-r9-r10-r1.json`: `d882301bb56ec469da5bb9b6f0b42f02e908c7dfcbdacaa048d6d0caff552a62`. As fotografias anteriores e posteriores estão em `evidencias/QA-09/aplicacao-pressao-fichas-r10-r1/`; os arquivos posteriores conferem byte a byte com as duas páginas efetivas.

## Reconstrução e preservação

O script independente `evidencias/QA-09/auditoria-mapa-r9-r10-independente-r1/reconstruir.mjs`, SHA-256 `84fcbbb4d97f30cb4d04a971f89719144f94d4ba601950653188478a456dd495`, reconstruiu cada página a partir da fotografia r9 com as cinco substituições literais únicas, pela ordem inversa de posição. Conferiu os hashes dos fragmentos originais e candidatos, posição e unicidade; as reconstruções coincidem byte a byte com r10. O HTML teve três deltas: `combustao`, `vaporizacao` e `diagnostico02`; o formulário teve `ficha-40` e `ficha-67`.

Na reconstrução os 197 artigos da aula permanecem idênticos, com mesmos IDs e ordem. O inventário oficial mantém os 197 registros individuais; somente a chave de topo `fonte` mudou. Das 100 fichas, somente `formula-reacao` e `formula-calor-reversivel` mudaram; as demais 98 são idênticas. Os 734 MathML da aula e 191 do formulário são idênticos como fragmentos. Trata-se de confronto estrutural, não de teste visual, de leitor de tela ou de correção científica integral de FOR-01.

## Pares, referências e recursos

O script independente `evidencias/QA-09/auditoria-mapa-r9-r10-independente-r1/mapa.py`, SHA-256 `2fd557a374cb02c915b3b0538230a75b222f1d36584c43e4d9dca89e7a059ec3`, leu ambos os inventários, o mapa e os deltas sem gravá-los. Verificou unicidade, cobertura, documento, tipo, tag, seção, âncora, hashes e deslocamento externo; nos trechos internos confrontou intervalo, contexto e ordem. Todos os 11.397 registros são pareados sem duplicação: 11.308 externos (11.303 hashes iguais e cinco alterados por seções ancestrais que contêm edições), 89 internos (79 hashes iguais e dez diferentes). Correspondências internas por sequência/contexto não demonstram por si só identidade semântica ou validade científica; o Auditor principal deve examinar os deltas. Os hashes iguais não transferem prova para dependências não examinadas.

As 815 referências foram confrontadas na mesma ordem: uma mudou de `../modulos/e1-termodinamica.html#substancias` para `../modulos/e1-termodinamica.html#base-entropia` dentro da ficha 67; o alvo novo existe na aula. As demais mantêm valor e texto, com deslocamentos consistentes quando externos às edições. Dos 138 registros de recursos, um reflete essa mudança de referência; hashes para os dois HTMLs são atualizados coerentemente e os demais recursos mantêm seus hashes. Os seis ativos específicos e os 197 artigos excluídos no inventário estrutural permanecem iguais. Referência resolvida e hash preservado não comprovam mérito científico do destino nem comportamento em navegador.

| Critério deste apoio | Resultado |
|---|---|
| Fotografias e reconstrução dos cinco deltas | Atendido, byte a byte na versão indicada. |
| Artigos, registros, fichas e MathML | Atendido no alcance descrito; duas fichas intencionalmente alteradas. |
| Mapa de 11.397 pares e contagens | Atendido estruturalmente, com 89 pares internos sujeitos ao exame semântico. |
| Referências, recursos e ativos | Atendido no recorte de identidade e destino, com uma alteração explicitada. |
| Revalidação científica de conteúdo e QA-09 global | Fora deste apoio; pendente do Auditor principal e do trabalho integral. |

Um ledger r9 e pareceres anteriores não são automaticamente válidos em r10: requerem reconciliação, avaliação de contexto e dependências e registro de alcance; em especial, quaisquer alegações sobre as duas fichas e teoria afetadas exigem revalidação localizada de FOR-01 e demais pareceres pertinentes. Não houve revisão humana, estudo com alunos, certificação externa ou navegador real nesta análise.
