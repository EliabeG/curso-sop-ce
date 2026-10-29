# BAN-07 r1 — análise independente da justificativa dos distratores em CR25

Data: 29/10/2026. Revisor: `/root/auditoria_av61_70`, agente automatizado independente do Corretor. **Decisão sugerida ao Auditor principal: não exigir ajuste obrigatório em CR25 por ausência de comentários individuais A–C no âmbito de BAN-07.** A justificativa publicada refuta matematicamente todas as alternativas incorretas; isso não é feedback individualizado de cada equívoco nem conclui DID-07. Não aprova BAN-07 global nem libera outro ID.

## Critério e alcance

O item BAN-07 determina conferir dados, consistência, comando, unidades, restrições, resposta única e distratores plausíveis. Seu aceite diz: “cada item tem demonstração do gabarito e justificativa dos distratores; detectar alternativas equivalentes após arredondamento”. O texto **não especifica local de publicação, formato, rótulo por letra nem que a explicação identifique uma causa para cada escolha**. “Cada item tem” requer, no mínimo, justificativa efetivamente vinculada a cada item e verificável; não autoriza presumir que a mera existência de uma letra oficial demonstre os distratores. A interpretação de que toda justificativa deva aparecer ao aluno em comentário separado não decorre expressamente desta redação.

Ao mesmo tempo, não é necessário resolver a localização em abstrato para aceitar este caso: o próprio produto contém uma demonstração que, aplicada a cada alternativa, a refuta. Os mecanismos teóricos enumerados em arquivos de auditoria são informação adicional, **não são apresentados como disponibilizados ao estudante** e não suprem por si só eventual lacuna pedagógica do material. Não se deve confundir este argumento comum com quatro explicações causais individualizadas.

A regra comum da seção 3.2 trata da conclusão de itens curriculares obrigatórios com objetivos, teoria, exercício, solução, rubrica e demais requisitos. O protocolo AAA, padrão de aprovação, afirma que requisitos gerais de conteúdo curricular novo não devem ser aplicados artificialmente a correção mecânica de alternativas, mantendo o aceite específico pertinente. DID-07 pede feedback sobre decisões e erros de modelagem, encaminhamento e nova situação; é ID distinto, ainda pendente, e sua satisfação não é inferida de BAN-07 ou deste caso. A resolução de CR25 permite descobrir a incompatibilidade numérica, mas não explica para cada alternativa qual equívoco geraria a escolha ou oferece nova situação personalizada.

## Produto, opções e demonstração

Artigo `cr-e1-25` do HTML r1 SHA-256 `ad3f5a9cb6c50e2cacacb42b7e8d3a14a6c8cb13320c1048aea23cc599d50ed6`; HTML SHA-256 `de614a44d796ca04268915f89f502060db2772835c072036a990802eff912b80`. O texto oficial contém gás ideal, quantidade fixa, p₂/p₁=2 e V₂/V₁=1,5. A resolução autoral pública informa T₂/T₁=2×1,5=3, usando kelvin, e aumento (3−1)×100%=200%; ainda distingue valor final de 300% do inicial de aumento de 200%. A chave oficial publicada é D.

A refutação individual que decorre desse argumento é:

| Opção publicada | Valor que exige para T₂/T₁ | Razão de não ser correta |
|---|---:|---|
| A, redução de 50% | 0,5 | Diverge de 3. |
| B, inalterada | 1 | Diverge de 3. |
| C, aumento de 50% | 1,5 | Diverge de 3. |
| D, aumento de 200% | 3 | Corresponde à demonstração. |
| E, aumento de 300% | 4 | Diverge de 3; 300% é valor final relativo, não aumento. |

Essa tabela é a explicitação **desta revisora**, não um componente publicado do produto. O aluno precisaria aplicar a conta do próprio artigo aos enunciados A–E; não há, no artigo, tabela de razões nem comentário nominal separado de A, B e C. A resolução explica diretamente E em contraposição a D. Não há alternativas equivalentes após arredondamento. Não confundir uma refutação lógica aplicável a todas as opções com prova empírica de plausibilidade ou evidência de que cada erro tenha sido diagnosticado pedagogicamente.

O registro preliminar [BAN-07-leitura-base.json](BAN-07-leitura-base.json), SHA-256 `d71452ed79437c69f454706c7645b47b5e3b7f2a41e228f0ea37ac078a2a9913`, pertence a `/root/auditor_aaa`; contém o cálculo e mecanismos teóricos propostos para A–E, com leitura prévia FON-02 e sem alegação de cegamento. Eles são documentação de auditoria. A leitura do Auditor principal em [BAN-07-auditor-heranca-cr16-35-r1.md](BAN-07-auditor-heranca-cr16-35-r1.md), SHA-256 `91955b0a8dd0a10c61027de8e9715e666f78fa279c65c83d1b4d1aae8e42ca03`, e a [adjudicação](BAN-07-auditor-decisoes-cr06-cr25-cr26-cr45-r1.md), SHA-256 `5a4fbc9454a651239d71fc0e0eacd676afcb1536c551440401797efc8b5b68f9`, distinguem refutação no produto dos mecanismos descritos no parecer e concluem sem ajuste em BAN-07. Esta revisão independente concorda com a fundamentação **para CR25**, não converte o precedente em isenção geral para todo item sem justificativa.

## Critérios e decisão

| Pergunta | Resultado |
|---|---|
| BAN-07 exige comentários individualmente identificados ao aluno? | Não há essa exigência textual explícita; não se afirma que documentação de bastidor sempre substitua justificativa adequada no produto. |
| CR25 apresenta argumento utilizável pelo estudante para refutar todas as opções? | Sim: razão final 3 e aumento de 200% contradizem os demais valores; E recebe explicação explícita adicional. |
| Produto explica individualmente as causas dos erros A–C? | Não. A enumeração e a tabela desta revisão são evidências do Auditor, não feedback apresentado no artigo. |
| Plausibilidade teórica e avaliação científica | Mecanismos foram registrados na preparação e na herança; a refutação lógica sozinha não demonstra sua frequência real. |
| DID-07 e nova situação | Não avaliados para aceite; continuam pendentes como requisito próprio. |

**Conclusão:** manter a decisão local sem ajuste BAN-07 para CR25, com a distinção acima. Se houver alteração posterior no texto ou hipótese de cálculo, reapreciar o argumento e a versão. Nenhuma alteração de produto, controle ou checklist foi realizada; não foram conduzidos testes com alunos ou navegadores nesta revisão.
