# BAN-02 — Parecer independente r1

Data: 27/10/2026. Auditor: agente automatizado independente `/root/auditor_aaa`.

**Decisão: AJUSTES_OBRIGATORIOS. BAN-02 r1 não está aprovado e nenhum próximo ID está liberado.** A reapresentação deve corrigir os quatro grupos abaixo dentro de BAN-02. A decisão e a matriz individual foram registradas antes deste Markdown em [BAN-02-r1-evidencias.json](BAN-02-r1-evidencias.json).

## Versão e critério

Este parecer refere-se exclusivamente ao [pacote r1 congelado](../evidencias/BAN-02/pacote-r1/inventario-questoes.json), cujo SHA-256 foi reconfirmado ao concluir o documento. Eventuais alterações correntes da r2 não pertencem à versão auditada.

BAN-02 exige registro individual de competência, pré-requisitos, origem, formato, nível, raciocínio requerido, número de etapas, hipóteses e exposição prévia dos 190 itens atuais, além de procedimento para cadastrar novos itens no mesmo registro. O nível deve refletir o raciocínio realmente exigido.

## Evidência e cobertura

O Auditor confrontou individualmente os **190 registros** com enunciados, alternativas, resoluções e notas da fonte: 30 Q, 80 CR e 80 AV. A [matriz independente](BAN-02-r1-evidencias.json) registra os campos examinados, observações por ID, hashes dos artigos/metadados e achados. As [notas preparatórias](BAN-02-preparacao-notas.json) foram produzidas a partir da fonte; as sete imagens PNG também foram inspecionadas localmente. Não houve execução de navegador pelo Auditor nesta rodada.

O [apoio técnico independente](BAN-02-r1-tecnico.md) comparou estrutura, origem e fontes dos 190 artigos e executou o validador real. Resultado: 190 registros para 190 artigos, sete recursos, 1.022 referências locais, zero erros e avisos. Formatos conferidos: 73 C/E e 117 de múltipla escolha. Os cinco arquivos do inventário coincidem byte a byte com o pacote r1. As URLs foram confrontadas com o HTML, sem conferir novamente os documentos oficiais externos.

**56 de 56 testes técnicos próprios passaram**, incluindo novos Q/CR/AV100, cadastro Q101, questões abertas/projetos, omissões, órfãos, duplicados, alterações de artigo/figura, estados condicionais e oito modos de declarar recursos. O script consolidado entregue concluiu seus **39 casos**, mas a importação no REPL falhou depois da impressão dos resultados, no epílogo `process.exitCode`, indisponível nesse runtime. Não se afirma execução integral limpa nem execução por CLI. Essa limitação não bloqueia o contrato: a via REPL documentada para o módulo do validador funcionou; o script de testes é documentado para Node CLI convencional. Resultados e limites constam das [evidências técnicas](BAN-02-r1-tecnico-evidencias.json) e do [script independente](BAN-02-r1-tecnico-verificacao.mjs).

## Critérios examinados

| Critério | Resultado da r1 |
|---|---|
| Cobertura individual e campos obrigatórios | Atendido estruturalmente em 190/190; não implica correção semântica. |
| IDs, origem, atribuição, formato e fontes presentes no HTML | Correspondência individual confirmada; conferência oficial externa permanece pendente. |
| Competências e alcance | Vínculos delimitados como apoio fundamental; ajustar o alcance derivado dos itens de R1-A/R1-B. Nenhuma competência avançada integral certificada. |
| Pré-requisitos pertinentes à tarefa atual | **Não atendido integralmente: R1-C.** |
| Nível pelo raciocínio realmente solicitado | **Não atendido integralmente: R1-B.** Estimativa sem piloto corretamente declarada. |
| Etapas intelectuais e número de etapas | Contagens coerentes com as listas em 190/190; **conteúdo de algumas etapas requer R1-A/R1-B**. |
| Hipóteses e limites fielmente registrados | **Não atendido integralmente: R1-A/R1-D.** Distinção entre hipóteses explícitas e implícitas está presente no conjunto. |
| Exposição prévia com evidência e limites | Relações específicas registradas, sem alegar novidade por ausência de duplicação; **corrigir unidades em R1-A**. |
| Cadastro de novos itens e manutenção | Protocolo reutilizável e testes atendidos, dentro dos limites declarados de descoberta e recursos. |
| Preservação do produto e aceites anteriores | HTML, registro, JS e CSS preservados; BAN-01 e GOV-01 não sofreram regressão de conteúdo nesta entrega. |

## Ajustes obrigatórios

### R1-A — Unidades de AV45 propagadas no inventário

**IDs: Q16, CR45 e AV45.** A fonte AV45 informa calor recebido de **1.000 kJ** e rejeição mínima de **500 kJ**. O inventário registra **1.000 J** e/ou **500 J** nas relações de exposição de Q16/CR45/AV45 e nos campos de raciocínio, hipóteses e alcance de AV45. O erro altera a grandeza por fator 1.000.

Corrigir todas as ocorrências derivadas de AV45 para kJ e regenerar os resumos afetados. Preservar os dados de outros itens que usam J corretamente, como CR42. A evidência da r2 deve identificar os campos alterados e mostrar concordância literal com AV45.

**Retificação de observação preliminar do Auditor:** AV30 realmente usa 300 kJ e está correto no inventário r1. A anotação própria que dizia 300 J foi corrigida após reconferência literal; AV30 não integra este achado.

### R1-B — Leitura crítica complementar contada como tarefa avaliada

**IDs: CR09, CR24 e CR79.** Os três registros atribuem nível intermediário e etapas de exame das ambiguidades/insuficiências. CR09 e CR24 solicitam C/E; CR79 solicita uma alternativa. As notas e resoluções fornecem discussão crítica, mas o instrumento atual não pede nem avalia a formulação dessa crítica pelo estudante.

A ressalva global de que o nível intermediário se refere à leitura das notas é honesta, porém mistura a tarefa respondida com um enriquecimento fornecido pelo material. Isso contraria a classificação pela tarefa realmente exigida e pode inflar as etapas e a distribuição de níveis.

Reclassificar nível, justificativa, etapas e alcance pela resposta atualmente solicitada, explicitando a leitura condicionada esperada pela prova. Preservar as ambiguidades e a discussão crítica em revisão, hipóteses e limites, sem creditá-las como raciocínio produzido ou avaliado. Atualizar método e estatísticas do resumo. **Não criar um novo instrumento para solucionar este achado dentro de BAN-02.**

### R1-C — Pré-requisitos herdados que não correspondem à versão AV

O próprio guia exige que os pré-requisitos representem conhecimento necessário. Há listas parcialmente herdadas das CR de origem e omissões relevantes:

| ID | Correção necessária |
|---|---|
| AV11 | Retirar unidades de potência/energia como requisito da conversão Celsius–kelvin solicitada. |
| AV26 | Retirar conversão kcal/kJ: todos os dados estão em kJ e a própria justificativa declara ausência de conversão. |
| AV30 | Não exigir leitura p–V quando o texto já informa isotermia e todos os dados necessários; o inventário reconhece essa suficiência. |
| AV33 | Incluir entropia, irreversibilidade e a distinção entre temperatura constante e isentropia, necessárias ao julgamento das proposições. |
| AV39 | Retirar conversão cal/J: calor e trabalho estão ambos em kJ. |
| AV45 | Retirar conversão °C/K: ambas as temperaturas são fornecidas em K. |
| AV53 | Incluir redução relativa/porcentagem; regeneração de Brayton e recuperação de calor são contexto, não conhecimento necessário para a conta solicitada. |
| AV56 | Incluir identificação do ciclo Rankine, indispensável à associação pedida e ausente da lista. |
| AV61 | Retirar volume morto/reexpansão como requisito: a razão é definida no enunciado e o campo de limites afirma que esse modelo não é exigido. |
| AV77 | Incluir primeira lei/balanço energético do ciclo, necessário para somar calor retirado e potência recebida. |

Revisar as demais AV pelo mesmo critério, sem simplesmente copiar listas pelo vínculo de origem. Conhecimentos apenas contextuais podem ser descritos como tais fora do campo de requisitos necessários. A reapresentação deve discriminar alterações individuais e justificar eventuais casos mantidos.

### R1-D — Hipótese expressa de AV57 omitida

**ID: AV57, `hipoteses.explicitadas`.** O enunciado restringe a expressão ao **Brayton ideal com calores específicos constantes**. O registro menciona somente a fórmula e o fator de pressão fornecidos, sem registrar a restrição de calores constantes.

Adicionar o modelo ideal e os calores específicos constantes como hipóteses expressas, mantendo a classificação pela substituição simples realmente pedida. Não atribuir ao aluno a dedução da fórmula ou o cálculo da potência fracionária já fornecida.

## Condição da reapresentação

Preservar o pacote r1 e suas evidências. Entregar r2 com os quatro grupos resolvidos, resumo e estatísticas coerentes, hashes novos e mapa dos deltas. O HTML e os arquivos de execução do curso devem continuar preservados. Reexecutar a validação final; repetir testes de infraestrutura apenas se o contrato ou o validador forem alterados. O Auditor verificará os deltas e a preservação das conclusões anteriores.

Não existe aprovação de BAN-02 por completude numérica ou por testes estruturais: os quatro grupos semânticos precisam estar satisfeitos. **FUN-01, GOV-02 e qualquer próximo ID continuam sem liberação por este parecer.** A orientação de que uma futura FUN-01 independente pode usar fontes e problemas próprios sem depender dos CR problemáticos permanece apenas orientação; BAN-10/FON-09 seguem abertos.

## Hashes da r1 auditada

| Arquivo | SHA-256 |
|---|---|
| `inventario-questoes.json` | `740792085cfede3b91131187ebf40ce614b943e296991e05af5d601498ca287f` |
| `inventario.schema.json` | `c71033464d54e71e61d4dcbae56847a88720e5ff937c1e1f7179005ab22d149b` |
| `validar-inventario.mjs` | `ddc8a6831422a868fb5a8b15b2f6653325f6644acf4f5c64dbf35bb0d2369fdd` |
| `LEIA-ME.md` | `cdcd7e965bdc4a998b6e2fa784a53f84f295abcf9ade2d06ce62fff71d072449` |
| `INVENTARIO_QUESTOES.md` | `508d0d2f17d8220d9b69eee8bd60e71c6999bb56ffdd7ff9547dc26174a94c2d` |
| `modulos/e1-termodinamica.html` | `b4e2d672c6feecb4289ad73bb9c16000ff5156720698f10153ff93fa0b788a8e` |
| `assets/registro.js` | `444a13658e0b869760296826be30267215293b18c3074f283b2a1ea252e828a2` |
| `assets/curso.js` | `81728c9fd1e96b738410e6b51cf4ab3ed785fb17753e68a988c1dcf236d8f899` |
| `assets/curso.css` | `b8ded6abc4548f378daab2e299a8a55ba81e8841c41049133a84d93848ee3eaa` |

Este aceite não foi concedido. Nenhuma conclusão deste parecer certifica o curso como avançado, a dificuldade empírica dos itens, seus gabaritos integrais, a autenticidade das fontes ou os critérios de outros IDs.
