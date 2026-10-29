# Parecer FUN-01 — rodada 2

**Veredito: APROVADO.** Data: 27/10/2026. Revisor: agente automatizado `/root/auditor_aaa`.

R1-A foi integralmente atendido: os títulos dos problemas de mistura e região supercrítica agora correspondem aos artigos publicados. A comparação integral confirmou que apenas esses dois campos e suas duas ocorrências no resumo mudaram. Os demais critérios científicos, pedagógicos e de preservação examinados no [parecer r1](FUN-01-r1.md) permanecem válidos.

## Escopo e verificações

Esta reauditoria aplica FUN-01, a regra comum da seção 3.2 e o protocolo, mediante revisão exclusiva do ajuste R1-A e da preservação dos critérios já examinados. A leitura e resolução independente dos quatro problemas não foram repetidas: HTML, dados e código de cálculo estão idênticos à versão integralmente auditada.

Foram executadas comparações próprias, sem depender da declaração de delta do Corretor:

- O inventário atual é exatamente o texto da cópia r1 com as duas substituições de título. A comparação dos objetos identificou somente `/itens/191/titulo` e `/itens/192/titulo`; os demais 192 registros e todos os outros campos foram preservados.
- O resumo atual é exatamente a cópia r1 com as mesmas duas substituições. O extrato r2 corresponde integralmente aos quatro registros novos vigentes.
- Os quatro títulos novos coincidem com seus `h3`; as duas divergências anteriores foram eliminadas.
- Os cinco arquivos coincidem com manifesto e cópias r2. As cinco cópias históricas do pacote r1 mantêm seus hashes. HTML, dados, cálculo e os seis arquivos compartilhados mantêm os hashes anteriormente conferidos.
- Reexecutei o validador canônico: **194 registros/194 artigos, oito recursos, 1.042 referências locais, zero erros e zero avisos**.

Os resultados detalhados e o delta estão nas [evidências independentes r2](FUN-01-r2-evidencias.json).

## Versão aprovada

| Arquivo | SHA-256 |
|---|---|
| `modulos/e1-termodinamica.html` | `cacda8c7742eead77aa1e92021b01c085c1b7340201d5cca0ada8ff743a8b04f` |
| `assets/termodinamica/fun01-dados-v1.json` | `a73b4d6140219cbd6b005216bb7a44db0a68b05f21ca51b7ac4b1ca782dd1448` |
| `assets/termodinamica/fun01-calculos-v1.mjs` | `a0fbdc4e6e7291a563db2362d26f4107ad67f56843e741d96eef8eea5a8d2a88` |
| `auditoria/termodinamica/inventario/inventario-questoes.json` | `4ead2e63ba59077cd89691dfef83e24a58fa58b5c8a4cde1c5420f9e3aad4def` |
| `auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md` | `b0223cb896015240284f1027a487308836252942a9503ce3a6eb9d084db0a15c` |

## Aceite completo e decisão

| Grupo de critérios | Resultado |
|---|---|
| R1-A: títulos, resumo e representações atuais coerentes | Atendido nesta rodada, por comparação integral. |
| Estado, equilíbrios, independência, composição e graus de liberdade; classificação em saturação, mistura e região supercrítica | Atendido na r1 e preservado sem alteração. |
| Objetivos, pré-requisitos, teoria/hipóteses, exemplos, prática independente, soluções e rubricas | Atendido na r1 e preservado sem alteração. |
| Fontes/versionamento, revisão científica/numérica e matriz C01–C10 parcial | Atendido na r1 e preservado sem alteração. |
| Manutenção do inventário, escopo, regressões, autoria e evidências | Atendido; correção documental aplicada e validação reproduzida. |

Não há ajuste obrigatório remanescente de FUN-01. A evidência de navegador do coordenador, vinculada ao mesmo HTML, permanece aplicável; não houve novo teste de navegador pelo Auditor nem aplicação com estudantes.

**FUN-01 está aprovado para a versão acima e libera a seleção do próximo ID pelo coordenador.** O Auditor não inicia a próxima correção. A orientação de dependências da r1 permanece: FUN-02 pode seguir com material próprio, mantendo os itens legados P0 fora da comprovação; eventual reutilização de material afetado exige resolver o bloqueio correspondente antes. Esta aprovação não encerra GOV-02, BAN-10/FON-09 ou demais IDs e não classifica o curso inteiro como avançado.
