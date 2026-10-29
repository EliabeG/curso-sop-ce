# QA-09 — auditoria independente do mapa r2 → r3

Data: 29/10/2026. Responsável: apoio auditor independente `/root/auditoria_av61_70`. Escopo: correspondência estrutural de ocorrências dos inventários QA-09 r2 e r3 e reprodutibilidade do gerador. Não altera produto ou controle nem aprova QA-09.

## Decisão

O mapa é adequado como reconciliação estrutural destas duas fotografias específicas. Os 11.396 pares foram confrontados independentemente em ordem com os dois inventários, conferindo arquivo, tipo, tag, seção, âncora, identificadores, posições, hashes e classificação. Nenhuma divergência foi encontrada. As duas listas possuem 11.396 registros e o mapa não omite nem repete par. Os IDs de cada inventário são únicos; também não há colisão da combinação documento, tipo, tag, seção, âncora e início em cada versão.

A fotografia anterior possui uma única ocorrência da frase corrigida e a substituição exata reproduz o HTML posterior. O ponto da inserção é 519302 unidades UTF-16 e o acréscimo tem 17 unidades. Cada posição inicial posterior no documento E1 muda exatamente conforme essa regra; em outros documentos não muda. Os 1.052 IDs distintos entre as versões decorrem dessa regra. No documento das fichas, o hash informado nos dois inventários coincide com o arquivo de hash `c27422b409a0a755448982c4074c6d6967fd3e91d7eae20274e218530f5c37b0`.

O mapa relata 11.393 pares com hashes iguais e três divergentes: a seção `preparacao-questoes` (`...:467689:secao`), o diagnóstico 1 (`...:519198:exemplo_ou_diagnostico`) e seu parágrafo (`...:519254:texto`). Confrontei os intervalos UTF-16 dos três com as fotografias: todos contêm a frase alterada e o intervalo r3 é exatamente o r2 com a substituição aprovada. Para seção e diagnóstico, também recalculei os hashes dos fragmentos com êxito. O hash de texto direto usa no gerador o conteúdo textual direto do nó, excluindo filhos, e não o fragmento integral; sua desigualdade foi conferida contra ambos os inventários e sua abrangência, contra o intervalo. Os hashes de fragmento dos diagnósticos 02–28 permanecem iguais, conforme auditoria anterior da aplicação.

## Reprodutibilidade, colisões e limites

O gerador original sobrescreve o mapa histórico. Para não gravá-lo, executei uma cópia temporária que só substituiu o caminho relativo de importação pelo mesmo módulo absoluto e redirecionou a saída para um arquivo temporário. Retornou sucesso e gerou saída byte a byte idêntica ao mapa preservado, SHA-256 `fc78b2b1bb7cecba974dda14ba50edfb7872a4a3b41074b5354dbe0cebe3423c`.

O gerador pareia por índice, valida documento, tipo, tag, seção, âncora e início ajustado e classifica a igualdade de hashes. Ele não faz teste explícito de unicidade nem pesquisa alternativa em caso de reordenação; esses limites foram supridos pela checagem independente acima para os dados presentes, não eliminados para execuções futuras. Há muitos hashes de conteúdo repetidos — 7.397 registros excedentes em grupos com mesmo hash r2 —, de modo que um hash isolado não distingue ocorrências; preservar documento, contexto, posição transformada e ordem é necessário. IDs e deslocamento são específicos destas fotografias, não identidades permanentes. O mapa contém ocorrências, não faz reconciliação individual das listas separadas `referencias` ou `recursos`.

Igualdade de hash e pareamento demonstram identidade estrutural do trecho segundo o modo de extração de cada classe, não correção científica ou cobertura da revisão. Em particular, o hash de texto direto pode excluir filhos e dependências; uma prova herdada continua exigindo correspondência de escopo e verificação das figuras, fórmulas, fontes e contexto pertinentes. Nos três pares de hash diferente, não se deve herdar automaticamente uma conclusão anterior sem reavaliar o efeito da edição; o diagnóstico 1 foi reavaliado no parecer próprio da aplicação. O mapa não prova que o levantamento identificou toda ocorrência numérica nem substitui auditoria QA-09 por ocorrência.

## Referências de integridade

- Mapa `auditoria/termodinamica/evidencias/QA-09/mapa-correspondencia-inventario-r2-r3-r1.json`: `fc78b2b1bb7cecba974dda14ba50edfb7872a4a3b41074b5354dbe0cebe3423c`.
- Gerador `mapear-r2-r3-r1.mjs`: `e8093b260b8890529323849125d7225338024e0d2f3dfce39c5a47baf4caa756`.
- Inventário r2 `8f37801a8dfdc073c3ee37357b36126a5235b8bb1fc4ad1f09215236bd5753f4`; inventário r3 `3074ab8fdf511d68dce73ec97bacca9dd9d5b0bbc3fe07a7d4ce329669b8b446`.
- HTML anterior `9ec10053e40640feeb977baea742da3cbe4d546659f772f0256c6b3cb0720a55`; posterior `0de7342b99b9ebef8c1526f0b8eefb3544f000a4546d7b500558550d178285eb`.
- Parecer da aplicação `QA-09-aplicacao-diagnostico01-auditoria-independente-r1.md`: `6d44812dd299e65d28682fe0c0917d1d2166d6433b46afd7e7a5bc7f6f73b52a`.
