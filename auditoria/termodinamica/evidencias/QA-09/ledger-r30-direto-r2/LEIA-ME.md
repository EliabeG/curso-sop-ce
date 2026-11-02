# QA-09 — ponte direta do ledger r28 para r30, revisão 2

30/10/2026. Integrador `/root/planning`. **Reavaliação individual concluída pelo integrador; aguarda Auditor independente da ponte.** A origem é o ledger r28 r2 SHA `518e6b952254773be5d95ba31e06607ba0a34562d6d90162f9b95d36f6fba000`, com parecer independente `auditoria-ledger-r28-r2-graficos/parecer.md` SHA `b71c1480f31ffa456ae0c5b0c20ce4ccd01320dab3a251f39d75628dd37068bd`. A r29 é apenas passagem estrutural: sua triagem r1 foi preservada e não recebeu aceite. A triagem r30 r1 também permanece intacta.

Aula r30 SHA `c719adae3464fb56ed2b0ad7014e0721c0aab2da444fb484ec0b40c5c0c8fbd4`, formulário `949c44fc5b96703929770b2881383d449af890616d34b9ab10b998ca96c75749` e inventário `1ce69fc1ab71850abc3ab8dc3df82b04e78788b9e62a55919c609a708a7979b4`. Os mapas r28→r29 e r29→r30 têm SHAs `a05800b66c6d56aa791cb16a251007ee26c6d4fef50c2fe7b42a2a104e8b21ba` e `7aca7066c5b3da141549566be2b6539643ebadcd44acc2473bccdcce4a986d17`. A aplicação r30 foi aprovada no recorte por `auditoria-aplicacao-r30/parecer.md`, SHA `1917231655ba500425b0fb5254c3900cb621c9ab29a68d642921985c2cc995df`; o parecer da aplicação não substitui o da ponte.

A [reconciliação dos 78 objetos](reconciliacao.md), SHA `7b27306d0f616a6d5321ec388ddc84d7b4f3a5df0cb0ebababd837bec7b59e24`, registra resultado e efeito dos deltas individualmente, incluindo EX034, D11, D12 e D27. Não houve alteração dos 78 recortes, 43 contextos rastreados ou quatro contêineres de figura. A r30 esclarece que coincidência entre trabalho total e eixo é exata com saldo nulo dos demais trabalhos e aproximada se desprezível; os objetos listados mantêm seus limites de modelo. O juízo anterior r28 permanece em cada registro e os juízos desta ponte em `juizos.json` SHA `73bbacacca6ab4b671838743194c42fd127f960a0ae7713b380b8b611a948e67`. Igualdade de hash não transfere automaticamente aceite.

A coleção de 11.409 ocorrências, 816 referências, 138 relações de recursos e seis ativos tem estado padrão `pendente_de_integracao`. A revalidação localizada não promove pais, filhos, bases, fontes, recursos, figuras adicionais ou as fichas 84/85. Os conjuntos se sobrepõem; não formam percentual de conclusão. QA-09 continua aberto.

## Verificação somente leitura

`node auditoria/termodinamica/evidencias/QA-09/ledger-r30-direto-r2/ledger.mjs --verificar auditoria/termodinamica/evidencias/QA-09/ledger-r30-direto-r2/ledger.json`

O verificador fixa hashes das páginas ativas e das três fotografias, inventários, mapas, pareceres e ledgers anteriores; reextrai os 78 fragmentos e contextos, confere três PNGs, 18 pares compostos do inventário e os IDs/hashes de 11.409 pares em cada mapa, refazendo seleção de contas. O exame científico não é inferido pelo programa. Exige a foto ativa r30; após outra aplicação, use snapshots em árvore isolada ou faça uma nova ponte, sem remover guardas.

Sete mutações no ledger em cópias temporárias — hash, posição, remoção, estado padrão, contexto, par e juízo — foram rejeitadas. São testes de confronto com o ledger reconstruído, não testes de alteração integral do mapa. `negativos.py` SHA `4c19a8cf4be15cecbc7d34bf51cab8f069a1850752cc438ef344e75dc291165f`, resultado SHA `d7802335f5cde96f90ff23ee9f43ba5f3f1a532618bc622e7d08991128de94d8`.

- `ledger.mjs` SHA `493fef8025d3b4ddb30f03fed567679b118654a5fc696b7861dd209124250eab`.
- `ledger.json` SHA `58d31ac8b26366c543cc439b3b4dc0c7c9428d191949c8ac49d801b4a459dc12`.

O incidente da aplicação r29 antes do ensaio, por erro de diretório, permanece registrado na entrega e no parecer de r29; o ensaio posterior é retrospectivo. Meu vínculo anterior como integrador e auditor de lotes é declarado; a presente ponte requer outro Auditor e não reaprova automaticamente minha própria ciência. Não houve navegador, leitor de tela, alunos ou revisão humana.
