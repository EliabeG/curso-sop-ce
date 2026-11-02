# QA-09 — apoio independente: mapa r7→r8 e repercussão de versão

Data: 30/10/2026. Revisor: agente automatizado `/root/audit_strategy`. **Resultado: sem divergências estruturais identificadas no escopo das verificações abaixo.** Este é um apoio à auditoria principal da aplicação, não substitui seu exame científico, nem aprova QA-09 integral ou libera outro ID.

## Fotografias e reconstrução

HTML anterior/fotografia `antes.html`: SHA-256 `200f9b773050594d762cc596a5a89297024b245fc4f504081fc77baaed3db95f`; HTML efetivo/fotografia `depois.html`: `57b13f0d6386764f1cc46ce543013b0eb75f7bfa97ffbd63ea331f38bfc5af8c`. Inventário r7: `5090b9897a4698e0ad090f45182afba5880361aabc9fd3c3bdf848d971a85a1a`; r8: `ae75a258398c385398567457d98ebd49b9838c0c9a4eedc69ea8d2d72981b687`; mapa r7→r8: `37d48a92165de1e29573b3ed5af992bd16df9a5da71b8372576fd84f0e6657fc`.

Examinei os quatro pares de fragmentos e seus hashes e posições UTF-16 no HTML r7, sua unicidade e a não sobreposição. A reconstrução independente pela substituição desses pares reproduz o HTML r8 **byte a byte**. Os quatro deltas têm, respectivamente, +45, +132, +27 e +207 unidades UTF-16. Isso prova a identidade do delta, não a suficiência científica das hipóteses.

## Mapa, referências, recursos e questões

Conferi os 11.396 pares pela posição na coleção, documento, tipo, tag, seção, âncora, IDs, hash declarado e deslocamento quando o início está fora dos blocos editados; foram encontrados 7.186 IDs deslocados e oito hashes diferentes. Dezoito registros começam dentro dos quatro blocos, para os quais o mapa não garante deslocamento pela fórmula geral e cuja identidade deve ser examinada individualmente. Os oito hashes diferentes correspondem às três seções ancestrais, aos três textos das primeiras candidatas, ao exemplo EX-031 e ao texto direto alterado dele. Para os 788 objetos categorizados do HTML fora de texto direto e atributos, recalculei os hashes dos fragmentos extraídos; também recalculei com parser independente os hashes dos **quatro textos diretos alterados**, antes e depois. Para os demais textos diretos e atributos comparei os hashes registrados, não os reextraí integralmente.

As 815 referências mantêm documento, seção, âncora, tag, atributo, valor e texto; nenhuma começa dentro dos blocos editados e os deslocamentos de início conferem. Dos 138 registros de recursos, 105 apontam ao próprio HTML E1 e passam a registrar o novo hash; todos os demais mantêm seus hashes. Os 138 caminhos atuais e seis ativos específicos conferem com seus hashes registrados; os ativos específicos não mudaram na comparação entre inventários. Não foram testados visualização, execução dinâmica, acesso externo ou a validade técnica de cada recurso. Registros repetidos apontando ao E1 não são 105 arquivos distintos.

Os **197 artigos** foram comparados byte a byte, na mesma ordem, usando extração independente das fotografias, e seus hashes coincidem com os registros do inventário r7 e r8. Os registros individuais do inventário oficial JSON não mudaram: apenas a chave `fonte` foi atualizada para o novo hash. O Markdown do inventário recebeu uma seção histórica. O validador `node auditoria/termodinamica/inventario/validar-inventario.mjs` retornou `ok=true`, 197 artigos, 29 recursos e 1.263 links locais, sem erros ou avisos. Essas provas estruturais dão suporte à avaliação localizada do impacto em BAN-02/07/08; não refazem integralmente as avaliações científicas ou o teste com usuário.

## Repercussão nos pareceres e ledger

O ledger r7 permanece conservado, com SHA-256 `1b0f3faaefb646103bc35b217494e1b46186012b56eaabc8c7f9e47f11dad463`. Seu verificador, executado sem escrita contra o HTML atual, **recusou a nova fotografia**, como previsto, por diferença do SHA-256. Os 12 blocos registrados no ledger — EX-011, EX-013 e EX-021–030 — conservam o hash de fragmento, mas todos têm nova posição/ID. Esse fato é um indício para análise localizada, não transfere seus aceites nem dispensa conferência de contexto e dependências. O ledger não está atualizado para r8 e não registra automaticamente outros pareceres anteriores ou recentes.

As alterações em `fun01-estado-equilibrio` recaem dentro do alcance curricular de FUN-01 e requerem a revisão científica localizada da versão r8; igualdade dos artigos FUN-01 não é por si só suficiente para avaliar a explicação em volta deles. A alteração de EX-031 afeta o parecer anterior do conjunto EX-031–040: esse exemplo precisa de reavaliação na versão efetiva, sem invalidar nem transferir automaticamente os outros nove. Os demais blocos e pareceres anteriores, incluindo os 12 do ledger, devem ser tratados por documento, contexto, posição, hash e dependências. Este apoio não concede ponte geral de aceites a r8.

Uma futura fotografia de ledger deve ter identidade e fonte r8, padrão pendente de integração, referências e recursos separados, e entradas explicitamente ligadas a pareceres e revalidações para a versão e o alcance correto; preservar o arquivo r7 como histórico. Pendência de integração não significa inexistência de revisão anterior. As coleções sobrepostas não são contagem de contas nem porcentagem de avanço.

## Reprodução e limites

Execute da raiz:

```sh
python3 auditoria/termodinamica/evidencias/QA-09/auditoria-mapa-r7-r8-independente-r1/verificar.py
```

O script independente, SHA-256 `4d5099e37a937fb24cb0d408be311c9fa877e5cedaee478ffc22b721c71c7ebb`, apenas lê arquivos e escreve em stdout. Sua execução passou. O script reconstrói os quatro deltas, confere os 11.396 pares e coleções separadas, reextrai os hashes no alcance acima e compara os artigos; não executa o mapeador histórico nem regrava evidências. O exame científico das quatro candidatas, as identidades internas aos blocos, testes de navegador e a revisão final permanecem sob responsabilidade da auditoria principal. Não houve revisão humana, teste com alunos nem certificação externa. QA-09 global permanece em correção e o próximo ID segue bloqueado.
