# QA-09 — auditoria independente do ledger parcial r9

Data: 30/10/2026. Auditor: agente automatizado independente `/root/next_graphics`. **APROVADO somente como registro parcial de identidade e alcance da fotografia r9.** Não encerra QA-09, não atribui completude aos blocos ou suas dependências, e não libera outro ID.

## Escopo e identificação

QA-09 requer inventário e recálculo de todo conteúdo numérico fora dos 197 artigos, com referências e resultados verificados. Este exame avalia a proposta de acompanhamento esparso e sua correspondência a oito deltas já examinados em parecer independente; não repete a revisão científica integral nem certifica cobertura total do inventário. Os 197 artigos permanecem segregados conforme o escopo da auditoria, sem inferir aceite de outros conteúdos.

- `ledger-r9-parcial-r1/ledger.json`: SHA-256 `50f529daca4b65876c54bff129b938d0fb0cad7e7194206fcfcc26428e021c59`.
- `ledger-r9-parcial-r1/ledger.py`: SHA-256 `abec471b35be0a7956611f9d5fd3b60135e721042bedb13bea770b73f245e7b1`.
- `ledger-r9-parcial-r1/LEIA-ME.md`: SHA-256 `2b11a9b0e8ae2445bfb939a23175d383821f3839039718c464e23f403409dd23`.
- Inventário r9: `023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d`; aula: `2d6b8fb2f9c99e04d22c19d7b32bbc3eb20577459d9132e506f9c0acef3f2fc2`; formulário: `cda652563a79c49a6c3d527ad1400c7f7597d33c9b8523ed8a26047b25c69feb`.
- Parecer da aplicação, SHA-256 `ad70d72cbe61ea89058406728517008aa379620dcfbb7b05f6cc13cda4e6852a`, aprova a aplicação localizada dos oito deltas e inclui os mesmos hashes de aula e formulário. Não aprova QA-09 como um todo.

## Verificações independentes

Examinei os oito registros e confrontei seus índices base zero, ID, arquivo, seção, âncora, tipo, tag, posições UTF-16 e hash com o inventário. Extraí cada fragmento dos documentos por UTF-16 e reconfirmei o hash do HTML; os IDs `ficha-080`, `cop`, `valvula`, `compressor`, `trocador`, `pressao-entrada-saida`, `pressao-1-3` e `resumo` são únicos. No resumo, a ocorrência do inventário representa texto direto, enquanto o fragmento HTML completo inclui a tag `li`: os hashes são diferentes por essa razão, não uma divergência omitida.

Confrontei o escopo das linhas com o parecer da aplicação. Cada estado afirma apenas a alteração localizada, e sua ressalva exclui aprovação automática de todos os enunciados, filhos, ancestrais, fontes ou dependências. O padrão das coleções permanece `pendente` **de integração no ledger**, e o texto esclarece que isso não apaga avaliações históricas já realizadas. Não se transfere automaticamente aceite de r7/r8 para r9. As coleções fixadas têm 11.397 ocorrências, 815 referências, 138 registros de recursos e seis ativos; são registros sobrepostos, não quantidade de cálculos nem percentual de conclusão.

O gerador foi inspecionado: lê fontes e produz JSON ou valida contra arquivo indicado, sem escrita de evidências. A execução do comando documentado retornou `ok=true`, oito linhas e contagens esperadas. Um script de auditoria independente, `auditoria/termodinamica/evidencias/QA-09/auditoria-ledger-r9-independente-r1/verificar.py`, SHA-256 `c0b8a6f15667f8a9737ef54a20a1e54228c46444493ddaa6ff59c62d21a30f66`, confirmou as oito identidades e, em cópias temporárias, testou separadamente adulterações no estado de uma linha, HTML, inventário, parecer e candidata: cada uma foi rejeitada. Os testes reproduzem detecção de alterações desses casos, não provam resistência a qualquer alteração coordenada do código e dos dados nem autenticidade de origem externa.

| Critério da proposta | Resultado |
|---|---|
| Fotografia, identidades e correspondência do parecer | Atendido para os oito deltas e hashes acima. |
| Padrão pendente, alcance localizado e segregação | Atendido; não implica que históricos não existam ou que nós sobrepostos sejam cobertos. |
| Reprodução e rejeição dos cinco testes em cópia | Atendido nos casos testados; não é proteção contra toda adulteração possível. |
| QA-09 integral e liberação de outro ID | Não atendido: há outras ocorrências e dependências a integrar, conferir e auditar. |

Não houve ensaio em navegador real, leitor de tela, estudo com alunos, revisão humana ou certificação externa. Uma mudança de fonte, inventário, parecer ou contexto deve interromper a correspondência desta fotografia e exigir reconciliação e reavaliação de alcance.
