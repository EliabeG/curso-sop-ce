# FOR-01 r2 — parecer independente

Data: 28/10/2026. Revisor: agente automatizado `/root/auditor_aaa`.

**Veredito: APROVADO. R1-A integralmente atendido.**

A reauditoria foi restrita às quatro fichas, aos três alvos da aula e aos documentos derivados de R1-A. Os critérios já atendidos no [parecer r1](FOR-01-r1.md) são herdados por identidade comprovada. O critério original continua sendo a revisão individual das 100 fichas — expressão, símbolos, unidades, hipóteses e ligação efetiva com a aula — sem universalizar balanços reduzidos.

## Versão aprovada

| Arquivo | SHA-256 |
|---|---|
| `formulas/termodinamica.html` | `c27422b409a0a755448982c4074c6d6967fd3e91d7eae20274e218530f5c37b0` |
| `modulos/e1-termodinamica.html` | `41984e9f1c3c55dde663e4c1d7271c59dd12fab9bcb499fae17c7ebcca680917` |
| `auditoria/termodinamica/inventario/inventario-questoes.json` | `de401cb3f8c56a52db7da18eab7134584cd5d39912fdc797f86b5cc053bdda04` |
| Manifesto r2 | `e45ac6743e82eccbb6fe30f33d64b6b23eec67574141f961cdabc77eafa72a04` |
| Entrega r2 | `06fd14cdcca2d83bf69ddab678f70bf75f25edee5c9cbbcf5fe34c51ad3f7024` |

Os três arquivos correntes foram reconferidos nesses hashes ao encerrar a revisão.

## Verificação científica e técnica

A [evidência científica r2](FOR-01-r2-cientifico.json), SHA `6a4e56f0544bf4b1911a72ad215685cbf0cc68f0a7ca0bab57e7de133c1d7efa`, registra a leitura independente das quatro condições, buscas, revisões individuais e três trechos da aula. As fichas **23/46/79/84** agora excluem todo trabalho não associado ao escoamento, recebido ou fornecido, inclusive elétrico, nos componentes em que se reduzem os balanços a diferenças de entalpia. O termo `pv` permanece incluído em `h`; os trabalhos de bomba, turbina e compressor não foram indevidamente eliminados.

O vaporizador com resistência dentro da fronteira recebe trabalho elétrico. Com `Q̇ = 0`, o balanço geral dá `Ẇnão-fluxo = −Ẇel,in` e `Ẇel,in = ṁhfg > 0`. Ele viola a nova hipótese de trabalho nulo e, portanto, fica corretamente fora da fórmula reduzida. A aula apresenta esse balanço com os sinais corretos. A demonstração é compatível com geração de entropia positiva; não depende de uma escolha arbitrária de trabalho. A tabela da válvula, já correta, e as fichas 55/89 foram preservadas.

O [subparecer técnico r2](FOR-01-r2-tecnico.md), SHA `fe016a8bfcae04890c591f1c538dad1ad31429e318c596fdc9f1a6f97478952e`, e seu [JSON](FOR-01-r2-tecnico.json), SHA `e0adddf7649f3681a0b2a9b19a99c7492db98214124b89df76600c8bfec00fbb`, confirmam **91/91 verificações restritas** reproduzidas em kernel novo. A validação canônica retornou **197 artigos/registros, 29 recursos e 1.166 links**, sem erros ou avisos. As 23 entradas do manifesto e nove cópias conferem. Não se repetiram os 913 testes intactos da r1.

| Critério aplicável | Resultado |
|---|---|
| Registro individual das 100 fichas | Atendido. Só os quatro registros afetados mudaram; os outros 96 permanecem idênticos. |
| Expressões, símbolos, unidades e sinais | Atendido por revisão r1 e preservação. As condições novas mantêm corretamente a distinção entre trabalho de fluxo e outros trabalhos. |
| Hipóteses suficientes; reduções não universais | Atendido. R1-A foi resolvido nas quatro fichas e o contramodelo elétrico está explicitamente fora da redução. |
| Ensino efetivo e coerência dos vínculos | Atendido. Calor latente, Rankine e refrigeração foram sincronizados; o destino da válvula já era correto. Demais vínculos herdados por identidade. |
| Fontes e validade científica | Atendido no recorte. O modelo geral e as fontes conferidas na r1 permanecem pertinentes; a demonstração nova foi examinada independentemente. |
| Representações e documentação | Atendido. Condições e `data-busca` coincidem; os 191 elementos MathML permanecem idênticos. A documentação nova informa corretamente **100 fichas / 191 elementos MathML**. |
| Preservação e escopo | Atendido. Quatro deltas de fichas e três da aula reconstroem integralmente os arquivos; 96 fichas, 197 artigos/registros, FUN-01/FUN-02, resumo e infraestrutura preservados. Inventário: somente hash/snapshot globais. Histórico r1 íntegro. |
| Interface pertinente | Atendido nos limites da [conferência do coordenador](../evidencias/FOR-01/navegador-coordenador-r2.md): busca das quatro fichas, legibilidade e três vínculos. Não é navegação executada pelo Auditor. |
| Piloto, impressão integral e nova cobertura avançada | Não aplicáveis a este aceite isolado; nenhuma execução desse tipo foi alegada. |

## Decisão

**Nenhum ajuste obrigatório permanece em FOR-01 r2.** O coordenador pode registrar este aceite e liberar o próximo ID da fila, após conferir a versão aprovada. O Auditor não iniciou nem concedeu aceite a outro item.

A aprovação cobre as 100 fichas existentes no escopo de FOR-01. Não certifica o curso inteiro como avançado, não encerra FOR-02/FOR-03/FOR-05/FOR-06 ou QA-09 e não representa aplicação com alunos, impressão em papel/PDF ou auditoria completa de acessibilidade.
