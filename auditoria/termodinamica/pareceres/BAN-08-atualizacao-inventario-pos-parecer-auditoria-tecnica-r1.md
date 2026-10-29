# BAN-08 — auditoria técnica da sincronização pós-parecer, r1

Data 29/10/2026. Revisor: agente automatizado `/root/auditoria_av61_70`. **Resultado: delta JSON e vínculos corretos, com uma inconsistência de estado no resumo Markdown que requer ajuste editorial.** Parecer localizado; não aprova BAN-08 nem libera próximo ID. Não alterei produto, controle ou evidências do Corretor.

## Versão e confronto

O manifesto `auditoria/termodinamica/evidencias/BAN-08/atualizacao-inventario-pos-parecer-r1/manifesto-r1.json` tem SHA-256 `98e470352f1876aad25dccba5e06303186b1abe227b5db3d6509cdb76edb069a`. Confirmei os hashes antes/depois dos arquivos, o parecer e o HTML:

| Arquivo | SHA-256 anterior | SHA-256 atual |
| --- | --- | --- |
| Inventário JSON | `5e83ef8b27e4596e9d8d154aa19df1e8f836863a4ff76acac0ba5ea66e9af72c` | `adb2f7edd0bdfbf6d1f0ec0bc8aefd46b22d6728a0aa59fc3981281aac93fbcd` |
| Resumo Markdown | `1eba9f02611dcb1b1a58690a876a0541d9fe5eb57714496415306f95d5564e29` | `f0fb7899fbf628515de624873ad3ef253ae08f0a3c1ec8f1154c941b11d573e4` |

HTML permanece `9ec10053e40640feeb977baea742da3cbe4d546659f772f0256c6b3cb0720a55`. Comparei o JSON completo: os 197 IDs e sua ordem e todos os campos globais permanecem; 194 registros são iguais. Somente `revisao.gabarito` muda de `pendente` para `verificado` e `revisao.evidencia_gabarito` é acrescentado em AV42, AV45 e AV52; todos os demais campos desses registros são idênticos.

Os três vínculos apontam ao mesmo `auditoria/termodinamica/pareceres/BAN-07-revalidacao-av42-av45-av52-r1-independente.md`, SHA-256 `86e9edc229e31fa2c798ad5ae1b89d595ddf74b080652f9a435c515517380c08`, de `/root/auditor_ban08_novo`, independente do Corretor. O parecer aprova expressamente a revalidação BAN-07 dos três artigos aplicados com hashes 81c755…/4999be…/f920b2…, e mantém BAN-08 fora do escopo. Verifiquei a concordância dos três hashes na versão aplicada, as condições e a associação dos links; `verificado` reflete o parecer localizado, sem inferir que BAN-08 tenha sido aprovada. O vínculo anterior de AV45 continua identificado como histórico no resumo e não é aplicado à versão atual.

## Validação e contagem de links

O validador canônico foi inspecionado e reexecutado sem escrita de evidências. Resultado: 197 registros e artigos, 29 recursos, 1263 links locais, zero erros e avisos, conforme `validacao-r1.json` do Corretor. A verificação é estrutural e documental, não valida mérito científico ou aprendizado. O crescimento de 1260 para 1263 é explicado pelos três novos campos de evidência: com uma cópia do JSON alterada **apenas em memória** para retirar os três links e restaurar `pendente`, `validateInventory` retornou 1260; no JSON corrente, 1263. Não gravei a cópia nem reatribuí resultados a versões anteriores.

## Achado: estado contraditório no resumo

O diff de `INVENTARIO_QUESTOES.md` apenas acrescenta o parágrafo que relata a revalidação e os três vínculos. Porém o parágrafo imediatamente anterior, mantido sem qualificação temporal, ainda diz no presente: “O JSON registra ... a revisão do gabarito da versão efetiva como pendente” e “Revisão independente da versão aplicada e testes de persistência são necessários”. Na versão atual, o JSON registra os três gabaritos como verificados e o parecer citado documenta revalidação e testes controlados; o parágrafo novo afirma a verificação. A leitura do resumo, portanto, apresenta estados atuais contraditórios. O validador automático não detecta essa coerência temporal.

**Ajuste recomendado:** marcar expressamente esse trecho como situação no instante da entrega parcial, ou reformulá-lo para refletir o estado atual preservando links aos registros históricos. Reexaminar o delta e hash do Markdown após a reapresentação. Não modificar o parecer histórico do Auditor, nem confundir essa retificação com aceite global BAN-08.

## Alcance e limites

A sincronização dos metadados JSON e dos links é compatível com BAN-02 no recorte afetado; o resumo precisa corrigir a contradição antes de declarar a sincronização documental integralmente coerente. Não houve teste com estudantes, navegador real ou reauditoria integral dos 197 itens. O veredito BAN-07 é atribuído ao Auditor que o emitiu; o presente trabalho não o substitui nem altera o controle.
