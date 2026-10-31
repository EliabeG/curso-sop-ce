# QA-09 — apoio independente ao mapa r8→r9 e ao impacto de versão

Data: 30/10/2026. Revisor: agente automatizado `/root/audit_strategy`. **Resultado localizado: sem divergência estrutural identificada nos testes descritos.** Este apoio não substitui a revisão científica das candidatas ou da aplicação por outro Auditor; não aprova QA-09 integral nem libera outro ID.

## Fotografias, reconstrução e mapa

Aula r8: SHA-256 `57b13f0d6386764f1cc46ce543013b0eb75f7bfa97ffbd63ea331f38bfc5af8c`; aula r9 efetiva: `2d6b8fb2f9c99e04d22c19d7b32bbc3eb20577459d9132e506f9c0acef3f2fc2`. Formulário r8: `c27422b409a0a755448982c4074c6d6967fd3e91d7eae20274e218530f5c37b0`; formulário r9: `cda652563a79c49a6c3d527ad1400c7f7597d33c9b8523ed8a26047b25c69feb`. Inventário r8: `ae75a258398c385398567457d98ebd49b9838c0c9a4eedc69ea8d2d72981b687`; r9: `023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d`; mapa: `d210e8c7efd4520e0d2036c4ebd2ec90762f684ffe8378b5fd71fdbd43d15b90`.

Os oito pares de fragmentos são únicos em suas respectivas fotografias, os hashes e intervalos UTF-16 conferem e não se sobrepõem. A reconstrução independente das oito substituições reproduz as duas páginas efetivas **byte a byte**. O mapa cobre, sem duplicar nem omitir IDs, 11.396 ocorrências r8 e 11.397 r9: 11.200 pares externos, 196 pares internos aos trechos alterados e um texto adicionado no cartão do compressor. As classes são nós estruturais sobrepostos, não uma contagem de cálculos ou de progresso.

Para cada par externo conferi tipo, tag, documento, seção, âncora e início com os deslocamentos dos deltas. Para os 196 pares internos, conferi associação ao mesmo bloco e contexto; dos 181 com hash declarado igual, comparei também o **fragmento integral por bytes** e todos coincidem. Os 15 pares internos com hash diferente foram localizados e correspondem aos blocos e textos afetados; o texto adicionado foi localizado dentro do compressor. Os três pares externos com hash diferente são seções ancestrais das mudanças. A identidade estrutural dos pares não comprova a adequação científica dos novos textos e, em geral, igualdade de hash não transfere automaticamente aceites.

## Referências, recursos, artigos e fichas

As 815 referências preservam documento, tag, seção, âncora, atributo, destino e texto. Uma referência começa dentro de um dos blocos editados: a ligação da ficha 80 para `#base-brayton-real`; reextraí os dois elementos e seus bytes são idênticos. Nas outras 814 referências conferi também os deslocamentos do início. A comparação estrutural não acessa destinos externos nem comprova que a descrição ou o destino sejam cientificamente suficientes.

Dos 138 registros de recursos, três apontam ao formulário alterado e 105 à aula alterada, e seus hashes correspondem às fotografias r8 e r9; os 30 restantes conservam os hashes. Todos os caminhos de recursos no inventário r9 e os seis ativos específicos conferem com os respectivos arquivos. Os registros podem repetir um arquivo e não devem ser contados como recursos únicos. Não houve teste de renderização ou comportamento desses recursos.

Os 197 artigos do módulo foram comparados por bytes e ordem e coincidem com os hashes do inventário. No formulário, dos 100 artigos de fichas, **99 permanecem idênticos** e apenas a ficha 80 muda; os 191 elementos MathML do formulário estão idênticos por bytes. No JSON do inventário oficial das questões, apenas `fonte` mudou para o hash r9 do E1. O validador estrutural retornou `ok=true`, com 197 itens, 29 recursos e 1.263 links locais, sem erros ou avisos. Isso não equivale à validação científica de questões ou fichas.

## Efeito sobre pareceres e ledger

A ficha 80 afeta o alcance do aceite **FOR-01**: a preservação das demais fichas e da marcação MathML delimita o delta, mas não confirma por si só domínio de aplicação, texto de busca, explicação e referências da ficha modificada. O Auditor principal deve revisar e registrar a revalidação localizada de FOR-01 para r9. A mudança dos flashcards e do resumo afeta os respectivos pareceres de QA-09, inclusive o achado anterior sobre COP; só a auditoria da versão efetiva pode decidir se as pendências foram resolvidas. BAN-02/07/08 têm suporte estrutural na comparação dos artigos, registros e scripts não modificados, sem nova aprovação científica integral.

Ledger r7 mantém SHA-256 `1b0f3faaefb646103bc35b217494e1b46186012b56eaabc8c7f9e47f11dad463` e permanece fotografia histórica. Não foi atualizado para r8 ou r9; por desenho, seu verificador rejeita fontes cujos hashes diferem. Uma eventual fotografia r9 deve partir de pendência de integração e inserir cada evidência apenas após conciliar identidade, contexto e revalidação. Essa pendência no ledger não significa inexistência de revisão histórica. Nenhuma ponte automática decorre da semelhança de conteúdo ou de IDs.

## Reprodução e limitações

```sh
python3 auditoria/termodinamica/evidencias/QA-09/auditoria-mapa-r8-r9-independente-r1/verificar.py
```

O script independente, SHA-256 `88b8470ab96957992ee835670dc227862670670438b55c751e367cb02b663a4a`, lê dados e escreve somente em stdout. Foi executado com sucesso; não regrava inventários, mapa ou evidências anteriores. Faz a reconstrução e as comparações acima, não valida o mérito científico de cada novo texto ou a execução visual/dinâmica. Não houve teste em navegador, leitor de tela, estudantes, revisão humana ou certificação externa nesta análise. O Auditor principal mantém responsabilidade pela decisão da aplicação e pelo impacto científico; QA-09 continua em correção.
