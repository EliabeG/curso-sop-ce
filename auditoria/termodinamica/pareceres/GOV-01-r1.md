# Parecer GOV-01 — rodada 1

**Data:** 27/10/2026, America/Sao_Paulo.  
**Revisor:** agente automatizado Auditor AAA (`/root/auditor_aaa`).  
**Versão examinada:** entrega GOV-01-r1, congelada pelo Corretor e confirmada pelo coordenador.  
**Veredito:** **APROVADO**.  
**Liberação do próximo ID:** **SIM, após registro do aceite e autorização concreta do coordenador.**

## Critério original e escopo examinado

GOV-01 determina publicar os resultados C01–C10, distinguir preparação para concurso de formação avançada aplicada, ligar cada promessa a conteúdos e instrumentos que efetivamente a avaliam e evitar promessa de cobertura universal de provas ou de todos os ramos da Termodinâmica.

Examinados a descrição da página, o lead, toda a introdução alterada, as dez linhas C01–C10, os 14 pares aula–atividade anunciados como disponíveis e a integridade das partes preservadas. A entrega é de delimitação e comunicação curricular: os resultados avançados são publicados como alvos em desenvolvimento; as capacidades anunciadas como atuais têm alcance menor, explícito e verificável. O aceite de GOV-01 não significa que as dez competências avançadas tenham sido implementadas ou avaliadas integralmente.

## Arquivos e hashes examinados

| Arquivo | SHA-256 |
|---|---|
| `modulos/e1-termodinamica.html` — versão aprovada nesta rodada | `b4e2d672c6feecb4289ad73bb9c16000ff5156720698f10153ff93fa0b788a8e` |
| `assets/registro.js` — inalterado | `444a13658e0b869760296826be30267215293b18c3074f283b2a1ea252e828a2` |
| `assets/curso.js` — inalterado | `81728c9fd1e96b738410e6b51cf4ab3ed785fb17753e68a988c1dcf236d8f899` |
| `assets/curso.css` — inalterado | `b8ded6abc4548f378daab2e299a8a55ba81e8841c41049133a84d93848ee3eaa` |

A cópia anterior de GOV-01 é idêntica ao conteúdo capturado independentemente pelo Auditor antes do trabalho, SHA-256 `a69846fbe1dd1bb8ef3ce3a685ffc2a308d6595a8f95a8637da523e77e231d1d`, aprovado em BAN-01-r2.

## Verificação semântica independente das promessas atuais

Foram lidos os comandos, as alternativas, as soluções e os trechos didáticos correspondentes. A conferência não se limitou à existência dos links nem à narrativa do Corretor.

| Resultado-alvo | Capacidade efetivamente anunciada como atual e evidência examinada | Decisão |
|---|---|---|
| C01 — modelagem | `base-fronteira` distingue os tipos de sistema; Q01 solicita classificar o recipiente vedado com condições dadas. O quadro limita a promessa ao reconhecimento, sem alegar escolha autônoma de fronteira. | Pertinente |
| C02 — propriedades | `substancias` ensina título e relação de mistura; Q04 fornece região e entalpias e exige calcular `x=0,25`. A promessa não inclui consulta independente a tabelas. | Pertinente |
| C03 — massa e energia | `base-primeira-lei` e `base-turbina-potencia` ensinam os balanços usados em Q07 (`ΔU=300 kJ`) e Q11 (`800 kW`). O alcance atual é aplicação orientada de energia; transientes e integração com massa permanecem explicitamente pendentes. | Pertinente |
| C04 — segunda lei | `base-entropia` sustenta as afirmações de Q18; `base-entropia-escoamento` sustenta Q29 (`0,10 kW/K`). O quadro informa que Q29 retoma os dados do exemplo e serve para fixação. | Pertinente |
| C05 — exergia | `base-exergia` explica a relação de destruição de exergia; AV-37 fornece a relação e os dados para `300×0,20=60 kJ`. O quadro descreve exatamente essa aplicação direta e exclui alegação de balanço completo. | Pertinente |
| C06 — ciclos | `base-rankine` e Q20 tratam da sequência de equipamentos; `base-refrigeracao` e Q23 calculam COP=3 com entalpias dadas. A determinação autônoma dos estados, as perdas e a comparação completa permanecem pendentes. | Pertinente |
| C07 — misturas e processos reativos | `base-umidade` e AV-16 permitem a razão `45/60=0,75` sob temperatura constante; `base-gas-modelo` e AV-22 fornecem `Z=180/200=0,90`; `base-termoquimica` e AV-31 distinguem PCS/PCI. São anunciados como introduções, sem extrapolar para misturas reativas ou modelos reais completos. | Pertinente |
| C08 — métodos e incerteza | `base-interpolacao` ensina o procedimento de Q26 (`2.860 kJ/kg`). A tabela é declarada didática e a repetição de dados é identificada como fixação. Não se promete ferramenta validada nem análise de incerteza atual. | Pertinente |
| C09 — julgamento | `base-segunda-lei` ensina Kelvin–Planck; AV-39 propõe converter integralmente calor de uma única fonte em trabalho como único efeito cíclico. A capacidade atual anunciada é identificar essa impossibilidade específica, sem alegar julgamento geral de dados incompletos. | Pertinente |
| C10 — comunicação técnica | A linha informa ausência de sequência didática e instrumento próprio para relatório/defesa. Não usa orientações genéricas de estudo como se fossem ensino e avaliação dessa competência. O resultado permanece um alvo publicado, sem promessa atual de entrega. | Delimitação honesta; competência não implementada |

As dez formulações avançadas preservam o sentido das competências C01–C10 da auditoria. Os limites de cada uma estão visíveis no mesmo quadro, e a abertura afirma expressamente que o alvo ainda não está integralmente ensinado e avaliado. Isso impede interpretar a existência do quadro como conclusão das competências.

## Verificações estruturais e de integridade

Foi criado e executado [GOV-01-r1-verificacao.mjs](GOV-01-r1-verificacao.mjs), independente do verificador do Corretor, com resultado em [GOV-01-r1-evidencias.json](GOV-01-r1-evidencias.json). O verificador entregue pelo Corretor também foi lido e reproduzido sem falhas.

- A comparação integral permite somente as duas ocorrências do lead — meta description e texto visível — e a introdução delimitada pelo título de objetivos e pela guia de notação. Os demais bytes são idênticos à base.
- Os **190 artigos** dos três bancos são idênticos byte a byte, incluindo as **30 questões aprovadas em BAN-01-r2**. Registro, código e estilos compartilhados permanecem idênticos.
- Os **1.204 IDs anteriores** permanecem; foram acrescentados **14 IDs**, totalizando **1.218**, sem duplicatas.
- Os **43 links internos introduzidos** têm destino único já existente na base. Foram conferidos os 14 pares pedagógicos de C01–C09; C10 não contém um vínculo inventado.
- As dez linhas têm cabeçalhos de linha, quatro células rotuladas e status de desenvolvimento explícito. A introdução usa elementos visíveis e classes já existentes, sem lógica nova de comportamento.
- O lead anterior que dizia “Domine...” foi substituído por uma descrição compatível com o nível intermediário atual e o percurso avançado em desenvolvimento. A promessa ampla anterior de conclusão também foi substituída.

Não foi necessário repetir as 150 execuções de correção de BAN-01: os 190 artigos, `registro.js` e `curso.js` estão integralmente preservados, e nenhuma mudança afeta alternativas, resposta, digital ou correção. Essa conclusão usa a comparação completa, não amostragem.

## Quadro de critérios de aceite

| Critério aplicável | Estado | Fundamentação |
|---|---|---|
| Publicar C01–C10 | Atendido | Dez resultados completos, identificados e visíveis |
| Distinguir concurso de formação avançada aplicada | Atendido | Finalidades e exigências descritas separadamente, com alcance atual e alvo em desenvolvimento |
| Cada promessa atual apontar a ensino e instrumento pertinente | Atendido | 14 pares examinados semanticamente; capacidades limitadas ao que as atividades efetivamente solicitam |
| Não tratar objetivos planejados como conteúdos implementados | Atendido | Todas as lacunas avançadas explícitas; C10 declara ausência de ensino/instrumento próprios |
| Não prometer cobertura universal de provas ou ramos | Atendido | Limites explícitos para editais e para estatística, quântica e não equilíbrio em profundidade |
| Escopo exclusivo de Termodinâmica | Atendido | Apenas abertura do E1 alterada; interface com E2 delimitada sem transferir a competência avançada do E1 para outro módulo |
| Coerência entre discurso e instrumentos | Atendido | Q26/Q29 identificados como fixação; relação fornecida de AV-37 não apresentada como balanço avançado |
| Preservar correção anterior BAN-01 | Atendido | Igualdade integral dos 30 artigos e do registro; sem invalidação do aceite anterior |
| Links e estrutura pertinentes à alteração | Atendido | 43 destinos existentes, 14 IDs únicos e cabeçalhos/células estruturados |
| Versão, responsável/revisor, evidências e limites reais | Atendido | Hashes, leitura semântica e verificadores registrados; ausência de ensaio de navegador declarada |
| Criar nova teoria, exemplos, exercícios inéditos e rubricas científicos | Não aplicável a GOV-01 | Entrega de governança; não houve nova unidade científica nem competência curricular declarada completa |
| Encerrar matriz completa GOV-02, inventário BAN-02 ou portas ACE | Não aplicável a este parecer | São itens distintos, com critérios próprios ainda não aceitos |

**Ajustes obrigatórios remanescentes de GOV-01: nenhum.**

## Limites e dependências

Esta auditoria realizou leitura editorial/científica pertinente aos vínculos, comparação estática e execução de verificadores. Não houve ensaio de navegador, leitor de tela, teste com estudantes nem demonstração empírica de aprendizagem. A estrutura da tabela foi conferida no HTML, sem alegar teste visual ou de acessibilidade completa.

A ausência de implementação integral de C01–C10 não é ocultada nem aprovada por ressalva: a tarefa GOV-01 é tornar a promessa proporcional à oferta real e publicar o alvo. A entrega cumpre esse objetivo ao limitar as promessas atuais e declarar as ausências. **Isso não satisfaz o aceite de GOV-02**, que exige ensino e avaliação efetivos para as competências obrigatórias. Um futuro mapa de lacunas será evidência de planejamento, sem encerramento automático de GOV-02.

O hash global do HTML mudou, mas o conteúdo protegido por BAN-01 continua íntegro. Este parecer registra a manutenção desse aceite na nova versão, sem reabrir uma correção que não foi afetada. A limitação já declarada de invalidação de tentativas anteriores a BAN-01 continua existente; GOV-01 não altera esse comportamento nem encerra UX-11.

## Decisão de liberação

**APROVADO para a versão e os hashes registrados.** O coordenador pode registrar GOV-01 como aprovado e liberar um próximo ID, preservando o bloqueio sequencial. BAN-02 é um próximo candidato adequado para inventariar a base; GOV-02 deve conservar o aceite final dependente da cobertura efetiva, conforme o preflight comunicado.

O Corretor deve aguardar autorização concreta do coordenador. Este parecer não aprova BAN-02, GOV-02, C01–C10 como competências implementadas nem o nível avançado global do curso.
