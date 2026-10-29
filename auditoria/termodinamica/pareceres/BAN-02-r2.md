# BAN-02 — Parecer independente r2

Data: 27/10/2026. Auditor: agente automatizado independente `/root/auditor_aaa`.

**Decisão: AJUSTES_OBRIGATORIOS. Falta somente R2-A, em AV20. BAN-02 não está aprovado e nenhum próximo ID está liberado.** Os ajustes anteriores estão atendidos, mas a revisão das listas introduziu uma omissão pontual que precisa ser corrigida antes do aceite.

## Versão e verificações

Foi auditado o [pacote r2 congelado](../evidencias/BAN-02/pacote-r2/inventario-questoes.json), com canônico SHA-256 `d17e2fcf73f2dbbe72005fb70ee6b36d1cad60ef90a1618abaf080d8bfd79507`. A [evidência independente r2](BAN-02-r2-evidencias.json) contém os deltas e o resultado individual da leitura das 80 listas AV. A [matriz dos 190 itens da r1](BAN-02-r1-evidencias.json) permanece aplicável aos artigos e campos preservados.

O confronto independente confirmou **112 diferenças de campos**: 83 listas de pré-requisitos — 80 AV e três CR — e 29 outros campos. Todos os deltas foram examinados; nenhuma alteração de produto foi identificada. As 80 listas AV foram lidas individualmente contra a tarefa existente e as anotações independentes anteriores. Não foram repetidas análises dos campos intactos sem nova razão.

O [apoio técnico independente](BAN-02-r2-tecnico.md) reproduziu as **18 verificações dirigidas**, todas satisfeitas, e conferiu que a saída coincide com a evidência entregue. A validação atual retornou 190 registros para 190 artigos, sete recursos, 1.022 referências locais, zero erros e avisos. Confirmou ainda os 112 deltas, as 22 evidências r1 preservadas, as 15 entradas do manifesto r2 e a igualdade dos cinco arquivos com o pacote congelado. Schema, validador, guia e os quatro arquivos do produto permanecem nos hashes anteriores; não se repetiram os testes de infraestrutura intacta. Resultados em [BAN-02-r2-tecnico-evidencias.json](BAN-02-r2-tecnico-evidencias.json).

Não houve teste de navegador nesta rodada. Validação estrutural não detecta, por si, a ausência de um conhecimento necessário para distinguir duas alternativas.

## Critérios e ajustes anteriores

| Critério | Resultado da r2 |
|---|---|
| Registro individual dos 190 itens e campos obrigatórios | Atendido; cobertura preservada e revalidada. |
| IDs, origem, atribuição e formato | Preservados da conferência individual r1; fontes oficiais externas não foram novamente auditadas. |
| Competências e alcance | Atendido no escopo de apoio fundamental; removida a atribuição de crítica avaliada em CR24/79. Nenhuma competência integral avançada certificada. |
| Pré-requisitos necessários à tarefa | **Pendente apenas R2-A, AV20.** As outras 79 listas AV revistas estão atendidas. |
| Nível pelo raciocínio solicitado | Atendido. CR09/24/79 são iniciantes sob leitura condicionada, sem crédito por crítica fornecida nas notas. Estimativa sem piloto preservada. |
| Raciocínio e número de etapas | Atendido; três CR agora têm uma etapa correspondente ao comando. As demais contagens e descrições foram preservadas. |
| Hipóteses explícitas, implícitas e limites | Atendido no inventário. AV57 registra Brayton ideal e calores específicos constantes; as ressalvas dos CR ambíguos foram preservadas. |
| Exposição prévia específica e limites de inferência | Atendido. Unidades de AV45 corrigidas nos seis campos derivados; relações e ressalvas de ineditismo preservadas. |
| Entrada de novos itens e detecção de omissão/desatualização | Atendido pelas verificações anteriores do contrato intacto e validação atual. Limites de descoberta documentados permanecem aplicáveis. |
| Preservação de produto e versões anteriores | Atendida; BAN-01/GOV-01 e pacote r1 preservados. |

**R1-A:** corrigido em Q16, CR45 e AV45; as descrições agora usam 1.000 kJ/500 kJ. CR42 continua em J e AV30 continua corretamente em 300 kJ.

**R1-B:** corrigido em CR09/24/79. Método, justificativas, etapas, alcance e resumo distinguem o comando respondido da leitura crítica já fornecida. As ambiguidades continuam abertas e não tiveram o gabarito certificado.

**R1-C:** os dez IDs originalmente apontados foram corrigidos, e as 80 listas AV foram revistas. Essa revisão gerou somente a omissão nova de AV20, descrita abaixo.

**R1-D:** corrigido em AV57, mantendo a tarefa como substituição simples com fator fornecido.

A distribuição atual confere: **171 iniciantes, 19 intermediários e nenhum avançado**. Ela descreve os itens e não constitui classificação final do curso.

## R2-A — Repor a distinção entre extrapolação matemática e validade física em AV20

**Campo:** `av-e1-20.pre_requisitos`.

A r2 mantém apenas leitura de `V=nRT/p` com quantidade e pressão constantes e limite da proporcionalidade quando T tende a zero. Retirou o conhecimento sobre o limite físico do modelo que constava da r1.

Na fonte, as alternativas **D e E chegam ambas a volume zero**. A alternativa D acrescenta que isso provaria que todo gás real permanece gasoso a 0 K; E recusa a validade dessa extrapolação para gás real até 0 K. Logo, calcular o limite não basta para selecionar a resposta: o estudante precisa distinguir o resultado matemático do modelo ideal de seu domínio físico, incluindo possível mudança de fase/desvio da idealidade. Esse conhecimento é efetivamente solicitado pelas alternativas, e não apenas enriquecimento posterior da resolução.

**Ajuste necessário:** acrescentar à lista de pré-requisitos essa distinção entre extrapolação matemática e validade física do gás ideal. Preservar os dois requisitos matemáticos pertinentes. Não alterar enunciado, alternativas, nível ou etapas, nem reabrir as outras 79 listas já satisfeitas.

**Evidência exigida para r3:** delta restrito ao campo de AV20 e à atualização coerente dos artefatos derivados/evidências; pacote r2 preservado; novos hashes e validação final. A nova auditoria verificará esse delta e a preservação das conclusões anteriores. Nenhum trabalho de outro ID está autorizado por este parecer.

## Hashes da versão r2 auditada

| Arquivo | SHA-256 |
|---|---|
| `inventario-questoes.json` | `d17e2fcf73f2dbbe72005fb70ee6b36d1cad60ef90a1618abaf080d8bfd79507` |
| `INVENTARIO_QUESTOES.md` | `2d82fbde8502a1f5096373f10cf0c57d2c23e7730f3a134dc2d0d7755e4b7590` |
| `inventario.schema.json` | `c71033464d54e71e61d4dcbae56847a88720e5ff937c1e1f7179005ab22d149b` |
| `validar-inventario.mjs` | `ddc8a6831422a868fb5a8b15b2f6653325f6644acf4f5c64dbf35bb0d2369fdd` |
| `LEIA-ME.md` | `cdcd7e965bdc4a998b6e2fa784a53f84f295abcf9ade2d06ce62fff71d072449` |
| `modulos/e1-termodinamica.html` | `b4e2d672c6feecb4289ad73bb9c16000ff5156720698f10153ff93fa0b788a8e` |
| `assets/registro.js` | `444a13658e0b869760296826be30267215293b18c3074f283b2a1ea252e828a2` |
| `assets/curso.js` | `81728c9fd1e96b738410e6b51cf4ab3ed785fb17753e68a988c1dcf236d8f899` |
| `assets/curso.css` | `b8ded6abc4548f378daab2e299a8a55ba81e8841c41049133a84d93848ee3eaa` |

**FUN-01 continua bloqueado por este gate.** Este parecer não aprova outros IDs, gabaritos integrais, fontes oficiais, independência das avaliações ou o nível avançado do curso.
