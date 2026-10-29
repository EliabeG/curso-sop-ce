# BAN-02 — Parecer independente r3

27/10/2026 · Auditor: agente automatizado independente `/root/auditor_aaa`.

**Decisão: APROVADO. O critério BAN-02 está integralmente satisfeito nesta versão. O gate está encerrado e o avanço ao próximo ID está liberado ao coordenador.** A ativação de FUN-01 permanece a cargo do coordenador; este parecer não aprova seu conteúdo futuro nem qualquer outro ID.

## Ajuste final e preservação

R2-A foi atendido: AV20 agora inclui como pré-requisito a distinção entre extrapolação matemática do gás ideal e domínio físico de um gás real, incluindo possível mudança de fase ou desvio da idealidade antes de 0 K. Isso cobre precisamente a diferença entre as alternativas D e E. Os dois requisitos matemáticos anteriores foram preservados.

A comparação integral independente entre os pacotes r2/r3 confirmou **um único campo alterado no canônico: `av-e1-20.pre_requisitos`**. Os 190 IDs, sua ordem e todos os demais campos permanecem iguais. O resumo recebeu apenas identificação da rodada, descrição do complemento e vínculo à nova entrega; mantém 171 itens iniciantes, 19 intermediários e nenhum avançado, como estimativa sem piloto.

O Auditor reexecutou o validador real: **190 registros para 190 artigos, sete recursos e 1.022 referências locais, zero erros e avisos**. Recalculou as seis entradas do manifesto r3 e os hashes das dez evidências r2, todos correspondentes. Produto, schema, guia e validador mantêm os hashes anteriores. Os testes de contrato intacto não foram repetidos; não houve teste de navegador nesta rodada.

## Aceite completo de BAN-02

| Critério | Conclusão |
|---|---|
| Competência, pré-requisitos, origem e formato por ID | Atendido nos 190 registros. Leitura independente r1/r2 preservada e omissão final de AV20 corrigida. |
| Nível, raciocínio e número de etapas | Atendido pela tarefa realmente solicitada, com estimativas justificadas e sem dificuldade empírica alegada. |
| Hipóteses e exposição prévia | Atendido no inventário, com pressupostos, ambiguidades, relações locais e limites declarados. Não se infere ineditismo da ausência de duplicação. |
| Todos os itens atuais classificados individualmente | Atendido: 30 Q, 80 CR e 80 AV; 73 C/E e 117 de múltipla escolha. |
| Novos itens no mesmo registro e detecção de omissões/desatualização | Atendido pelo contrato, guia e validador já exercitados, preservados nesta rodada. Seus limites documentados continuam aplicáveis. |
| Escopo, rastreabilidade e preservação dos aceites anteriores | Atendido; produto e pacotes anteriores preservados. BAN-01 e GOV-01 permanecem válidos. |

As conclusões usam a [matriz independente de 190 itens da r1](BAN-02-r1-evidencias.json), a [revisão dos 112 deltas e 80 listas da r2](BAN-02-r2-evidencias.json) e a [evidência final r3](BAN-02-r3-evidencias.json). Os quatro grupos de ajustes r1 foram satisfeitos na r2; a única pendência r2 foi satisfeita na r3. Não resta ajuste obrigatório de BAN-02 nesta versão.

## Hashes finais aprovados

| Arquivo | SHA-256 |
|---|---|
| `inventario/inventario-questoes.json` | `0b36157afab94ddb67ed3d0bec1a9984da8f7152f3fb246b5438fa0bc7ac7b58` |
| `inventario/INVENTARIO_QUESTOES.md` | `50bf39f3ae92590099c8aa139c5df822157413e3ee88377a3fbe2150d7ac1046` |
| `inventario/inventario.schema.json` | `c71033464d54e71e61d4dcbae56847a88720e5ff937c1e1f7179005ab22d149b` |
| `inventario/validar-inventario.mjs` | `ddc8a6831422a868fb5a8b15b2f6653325f6644acf4f5c64dbf35bb0d2369fdd` |
| `inventario/LEIA-ME.md` | `cdcd7e965bdc4a998b6e2fa784a53f84f295abcf9ade2d06ce62fff71d072449` |
| `modulos/e1-termodinamica.html` | `b4e2d672c6feecb4289ad73bb9c16000ff5156720698f10153ff93fa0b788a8e` |
| `assets/registro.js` | `444a13658e0b869760296826be30267215293b18c3074f283b2a1ea252e828a2` |
| `assets/curso.js` | `81728c9fd1e96b738410e6b51cf4ab3ed785fb17753e68a988c1dcf236d8f899` |
| `assets/curso.css` | `b8ded6abc4548f378daab2e299a8a55ba81e8841c41049133a84d93848ee3eaa` |

Este é aceite do **inventário BAN-02**, não certificação do curso como avançado. Permanecem abertos os trabalhos próprios de conteúdo, gabaritos, fontes, psicometria e independência das avaliações, incluindo os P0 já registrados. A próxima unidade deve cumprir seu próprio critério e usar as fontes e os problemas próprios previstos no preflight.
