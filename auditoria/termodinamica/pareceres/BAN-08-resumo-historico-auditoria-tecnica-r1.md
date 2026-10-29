# BAN-08 — auditoria independente da correção do resumo histórico

Data 29/10/2026. Revisor: agente automatizado `/root/auditoria_av61_70`. **Conclusão localizada: o ajuste editorial atende à ressalva registrada no parecer técnico anterior; não identifiquei nova divergência no alcance examinado.** Não é aprovação global de BAN-08 nem liberação de próximo ID. Produto, controle e evidências anteriores não foram alterados por este revisor.

## Delta e reconciliação temporal

Manifesta-se a aplicação do Corretor `/root/inspect_repo` em `auditoria/termodinamica/evidencias/BAN-08/aplicacao-resumo-historico-r1/manifesto-r1.json`, SHA-256 `346bf0e84b339f61a321097476e4c3bf2e20c1ce0026c2aa94847694b4755992`. O parecer que pediu o ajuste `BAN-08-atualizacao-inventario-pos-parecer-auditoria-tecnica-r1.md` tem SHA-256 `ca04865e63322ae3e341c06a47b9612e3e4a73c3178b3ad18b6991640d8a8e4f`, conforme manifesto.

Resumo anterior `auditoria/termodinamica/evidencias/BAN-08/aplicacao-resumo-historico-r1/resumo-antes.md`: SHA-256 `f0fb7899fbf628515de624873ad3ef253ae08f0a3c1ec8f1154c941b11d573e4`. Resumo atual `auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md`: SHA-256 `7824dcd17e20d14b54db2c339310e6100cebaf8e7df59051d636844c7dc3be7d`. Comparei os textos integralmente: cada uma das duas substituições declaradas ocorre uma vez; aplicá-las em memória ao texto anterior reconstrói exatamente o resumo atual, sem outras alterações.

As duas afirmações antes apresentadas como pendências correntes foram qualificadas como estado **na entrega inicial**: o gabarito então estava pendente e a revalidação/testes controlados ainda eram necessários. O parágrafo seguinte informa a revalidação posterior e o estado atual. Ambas as frases foram corrigidas; não se confunde o relato histórico com gabaritos atualmente verificados, nem testes controlados com navegador real. O parecer BAN-07 localizado e o registro anterior de AV45 permanecem explicitamente distinguidos no resumo.

## Integridade, links e BAN-02

O HTML `modulos/e1-termodinamica.html` permanece com SHA-256 `9ec10053e40640feeb977baea742da3cbe4d546659f772f0256c6b3cb0720a55`; o JSON `auditoria/termodinamica/inventario/inventario-questoes.json` permanece com SHA-256 `adb2f7edd0bdfbf6d1f0ec0bc8aefd46b22d6728a0aa59fc3981281aac93fbcd`, iguais à versão sincronizada examinada no parecer anterior. Não houve novo delta nos registros JSON; AV42, AV45 e AV52 continuam com gabarito verificado e referência à revalidação BAN-07 da versão aplicada. Isso sustenta a continuidade de BAN-02 no alcance documental atingido, sem nova classificação científica dos 197 itens ou declaração de aceite global BAN-08.

O validador canônico foi reexecutado sem gravar evidências: 197 registros e artigos, 29 recursos, 1263 links locais, zero erros e avisos. O resultado coincide com `auditoria/termodinamica/evidencias/BAN-08/aplicacao-resumo-historico-r1/validacao-r1.json`, SHA-256 `c5c3ecfad7bf026bc6705be579d35aebe9ebb071a1d7bf44907e5bfb86a49e65`. Além da validação canônica do inventário e HTML, examinei 232 destinos de arquivos locais referenciados no resumo: todos existem. Dos vínculos com fragmento, os 209 apontam para IDs HTML existentes. Essa verificação de existência não certifica conteúdo científico de cada destino nem links externos.

## Limites

As verificações valem apenas para os hashes acima. O validador é estrutural/documental; não foram realizados teste com estudantes, revisão de acessibilidade ou certificação externa. A revalidação científica de AV42/45/52 é atribuída ao parecer BAN-07 do Auditor responsável, não repetida integralmente nesta revisão editorial.
