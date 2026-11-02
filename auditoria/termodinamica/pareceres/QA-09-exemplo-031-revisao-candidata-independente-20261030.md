# QA-09 — revisão independente da candidata EX-031, 30/10/2026

Revisor: agente automatizado independente `/root/qa_fichas`. **Veredito: APROVADA a candidata isolada para aplicação localizada**, sem afirmar que a alteração já está no produto. O parecer anterior do lote EX-031–040 permanece com ajuste obrigatório até a aplicação e a revisão independente da versão efetiva. QA-09 permanece aberto e nenhum outro ID fica liberado.

## Escopo e identidade

A [entrega do Corretor](../evidencias/QA-09/exemplo-031-candidata-20261030/entrega.md) responde à ambiguidade identificada no [parecer EX-031–040](QA-09-exemplos-031-040-auditoria-independente-r1.md): a troca não excluía o trabalho não associado ao escoamento nos três equipamentos térmicos. Examino aqui somente a candidata do EX-031, sua identidade e o balanço no modelo declarado. A regra curricular comum de conclusão de um tópico não é atendida por esta correção localizada, nem se pretende encerrar o item curricular.

A fotografia `modulos/e1-termodinamica.html` tem SHA-256 `200f9b773050594d762cc596a5a89297024b245fc4f504081fc77baaed3db95f`; inventário r7 `5090b9897a4698e0ad090f45182afba5880361aabc9fd3c3bdf848d971a85a1a`. O original é uma `div.exemplo` única na seção `ciclos`, limites UTF-16 381086–381963. Reconfirmei a ocorrência literal única e hash do fragmento original, sem a quebra final do arquivo isolado, `fa0b22cc94dc24f3c4fc2493c719f30ab4a0484149f081b681497f81d73536e6`. A candidata, também sem quebra final, tem hash `fdbd8e2cc5d4212af40051f854dca99420ae4ef7b1c887a82c9540fdae2a3d6a`. A troca é exatamente uma inserção ao final das hipóteses iniciais; os dados, solução, marcação e demais palavras são preservados. O HTML efetivo ainda contém o original.

A inserção define entradas e saídas de calor líquidas na caldeira, no reaquecedor e no condensador e determina que esses três equipamentos não trocam trabalho além do trabalho de escoamento já incluído em h. Essa condição exclui explicitamente por abrangência outros trabalhos, inclusive elétrico e de eixo, sem contá-los duas vezes; bomba e turbinas seguem adiabáticas, equipamentos em regime permanente e variações cinética e potencial desprezíveis. O mesmo kg percorre a sequência sem extração.

## Recálculo e limitações

Sob as condições adicionadas, a primeira lei por unidade de massa dá `q−w=Δh`, com calor recebido e trabalho saindo positivos. Para os três equipamentos sem trabalho não associado ao escoamento: `qcaldeira=3100−210=2890`, `qreaquecedor=3200−2500=700` e calor rejeitado no condensador `2200−200=2000 kJ/kg`. A soma de entrada é `3590 kJ/kg`. Turbinas fornecem `600+1000=1600`; a bomba consome `10`; trabalho líquido `1590 kJ/kg`. A igualdade `3590−2000=1590` confere. `η=1590/3590=0,4428969…`, ou `44,29%` ao centésimo de ponto percentual.

O contramodelo com 100 kJ/kg elétricos recebidos na caldeira, detalhado no parecer anterior, fica excluído. Os números são entalpias didáticas; as contas não estabelecem temperaturas, pressões, fases ou validade integral pela segunda lei. A expressão “mesmo kg” mantém o mesmo fluxo em todos os equipamentos descritos e não valida um equipamento real.

Reproduzi o script do Corretor como leitura sem gravação, conferi independentemente a substituição única e recalculei com frações exatas. Entrega SHA-256 `553f1877e4d243b7f22ad0e150b7cc784a3e6fa13af4c3f566fb89b5a37a0651`; script `e764105f7ebf76e5192a2b79c3aca2f9c7f79c2617b8835276c972508a20638f`. Arquivos isolados, incluindo a quebra final: original `4ba5ca1d112ca575a5a4323690dc339672377a50a7061cb87e0e14a2206f59e4`; candidata `ef5b56119ac64659e702820301ca343b7f66ca2834042dd57ad9ea0edca71701`. A inspeção é estática; não houve navegador, teste com estudantes ou revisão humana.

## Critérios e decisão

| Critério da candidata | Resultado |
|---|---|
| Identidade, unicidade e delta | Atendido para fotografia e fragmentos examinados. |
| Exclusão do contramodelo e clareza de hipóteses | Atendido no modelo dos equipamentos especificados. |
| Cálculos, sinais, unidades e arredondamento | Atendido na extensão do exemplo. |
| Versão efetiva, inventário e aceites após aplicação | Ainda não examinados. Aplicar somente após comparar novamente a base; documentar mapa de posições, hashes, preservação dos 197 artigos/registros e revalidação de alcance, então solicitar novo parecer. |
| Fechamento de QA-09 e próximo ID | Não autorizado. |

A aprovação é restrita à candidata e não garante validade de uma versão posterior ou classificação avançada do curso.
