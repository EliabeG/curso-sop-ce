# Parecer BAN-01 — rodada 2

**Data:** 27/10/2026, America/Sao_Paulo.  
**Revisor:** agente automatizado Auditor AAA (`/root/auditor_aaa`).  
**Versão examinada:** entrega BAN-01-r2.  
**Veredito:** **APROVADO**.  
**Liberação do próximo ID:** **SIM, pelo coordenador, após registrar este aceite.**

## Critério original e escopo

BAN-01 exige reorganizar as alternativas das 30 questões iniciais, atualizar conjuntamente gabarito, comentários e referências às letras, eliminar ABCDE repetido, manter resposta única correta e verificar cada item sem criar outra sequência sistemática.

Foram examinados integralmente os 30 artigos `q-e1-01` a `q-e1-30` e o mapa de questões E1 em `assets/registro.js`. Esta rodada reexamina os dois ajustes obrigatórios do [parecer anterior](BAN-01-r1.md), a literalidade dos deltas, todas as verificações estruturais e o comportamento de correção/progresso pertinente. Não concede aceite aos outros IDs nem classifica o curso inteiro como avançado.

## Versão efetivamente aprovada

| Arquivo | SHA-256 |
|---|---|
| `modulos/e1-termodinamica.html` | `a69846fbe1dd1bb8ef3ce3a685ffc2a308d6595a8f95a8637da523e77e231d1d` |
| `assets/registro.js` | `444a13658e0b869760296826be30267215293b18c3074f283b2a1ea252e828a2` |
| `assets/curso.js` — lido e executado parcialmente, sem alteração | `81728c9fd1e96b738410e6b51cf4ab3ed785fb17753e68a988c1dcf236d8f899` |

As cópias r1 conferem com os hashes do parecer anterior e com os conteúdos preservados independentemente em memória pelo Auditor: HTML `d375695006edf96cbb709b7e85e7ebb84e94474333505768a3cccec0e94119a4`; registro `234cb179c3a7c81043d9d66ee65116b2f07503999aac6a45c433dccd51545055`. As cópias originais também permanecem iguais à linha de base verificada.

## Reavaliação dos ajustes obrigatórios

| Exigência | Resultado independente | Estado |
|---|---|---|
| R1-A — Q10: regime permanente disponível antes da resolução | O enunciado passou a informar que a válvula opera **em regime permanente**, adiabaticamente, sem trabalho e com pequenas mudanças de velocidade/altura. Assim, a eliminação da acumulação na solução corresponde às hipóteses fornecidas. A única relação geral adequada entre as alternativas permanece `h₁ ≈ h₂`, letra E. | **Atendido integralmente** |
| R1-B — Q12: distinguir magnitude e valor algébrico do trabalho | O comando passou a pedir a **magnitude aproximada do trabalho específico de entrada (consumido), adotada como positiva**. O resultado é `0,001 × 500 = 0,5 kJ/kg`, letra C. A alternativa negativa não responde à magnitude positiva pedida. A definição de `w_in` e sua justificativa permanecem coerentes. | **Atendido integralmente** |
| Alterar apenas os dois enunciados e as digitais necessárias | Comparação de arquivos inteiros admite somente os dois textos exatos acima e as substituições de digitais `1877b147 → ab29d979` e `0e39d656 → 83f286e2`, com gabaritos E/C preservados. | **Atendido integralmente** |
| Preservar evidências e não enfraquecer a comparação de enunciados | Evidências r1 preservadas. Verificador do Corretor exige literalmente os enunciados completos esperados; o independente confronta toda a r2 com a r1 mais as duas únicas substituições autorizadas. | **Atendido integralmente** |

Os fundamentos dos dois ajustes e suas referências científicas estão registrados no parecer r1. Não foram detectadas outras pendências de resposta única dentro do escopo examinado.

## Verificações independentes da versão r2

Foi criado e executado [BAN-01-r2-verificacao.mjs](BAN-01-r2-verificacao.mjs), com resultado em [BAN-01-r2-evidencias.json](BAN-01-r2-evidencias.json). Também foi lido e reproduzido o verificador r2 do Corretor. Ambos concluíram sem falhas.

- **30/30 artigos:** presentes e na ordem esperada; todos os gabaritos visíveis correspondem aos atributos e à resposta pretendida.
- **150/150 alternativas:** conteúdo preservado e permutações coerentes. As associações foram derivadas independentemente por conteúdo, sem depender do mapeamento do Corretor.
- **140/140 justificativas por letra:** acompanham suas alternativas; **6/6 justificativas de proposições** em Q13/Q18 permanecem intactas.
- **Escopo:** demais bytes dos artigos preservados, exceto os dois enunciados explicitamente autorizados; todos os bytes externos aos 30 artigos idênticos à base. No registro, todos os bytes fora do mapa E1 permanecem idênticos. Os demais módulos não sofreram alteração nesses arquivos.
- **Digitais:** executadas as funções reais de `curso.js` sobre árvores dos fragmentos; 30 digitais atuais corretas, únicas e sincronizadas com o registro, sem colisões com as 30 anteriores à correção. Q10=`ab29d979`; Q12=`83f286e2`.
- **Correção:** repetidos **150 casos** da função real `mostrarCorrecao`, um para cada escolha em cada questão; 30 acertos e 120 erros conforme esperado, com letra correta, seleção, feedback e opção de refazer consistentes.
- **Estado e portal:** executadas as funções reais `lerEstadoModulo` e `progressoDoModulo` em estados antigos, novos e mistos. Nenhuma letra antiga foi atribuída a um novo conteúdo. Estado novo com todas as respostas corretas produz 30 respostas e 30 acertos.
- **Padrão de letras:** mantida a sequência `CBECCDEABEDCCEAADDAAECCCEBAECB`, com A=6, B=4, C=9, D=4, E=7; ausentes períodos globais de 1 a 15 e repetição dos seis blocos de cinco. A inspeção não encontrou rotação ou alternância sistemática substituta. Não se afirma validação psicométrica nem impossibilidade matemática de qualquer padrão concebível.
- **Ciência e conteúdo:** a leitura dos 30 itens realizada na r1 continua aplicável, porque os 28 itens restantes e todas as alternativas/soluções foram preservados integralmente. Os dois enunciados modificados foram relidos em conjunto com suas cinco alternativas e soluções, e satisfazem as exigências do parecer anterior.

## Quadro de todos os critérios aplicáveis

| Critério | Estado | Fundamentação |
|---|---|---|
| Reorganizar as 30 questões | Atendido | 30 permutações não triviais preservadas e verificadas |
| Eliminar ABCDE repetido e outra sequência sistemática substituta | Atendido | Análise documentada da sequência atual |
| Atualizar gabarito visível e atributo conjuntamente | Atendido | 30/30 concordantes |
| Manter comentário, justificativas e referências às letras coerentes | Atendido | Associações exaustivas preservadas; proposições e estados físicos da Q09 mantidos |
| Manter resposta única correta e hipóteses necessárias disponíveis | Atendido | 30 itens examinados; R1-A/R1-B integralmente resolvidos |
| Verificar cada item após alteração | Atendido | Comparação integral e 150 execuções de correção na r2 |
| Coerência entre enunciado, solução, unidades, figuras e comportamento afetado | Atendido | Deltas de hipótese/magnitude resolvidos; demais conteúdos idênticos à base conferida |
| Digitais e registro coerentes | Atendido | Funções originais reproduzidas e mapa E1 sincronizado |
| Preservar outros módulos | Atendido | Igualdade de todos os bytes externos ao escopo nos arquivos afetados |
| Evidências reproduzíveis, versão, responsável/revisor e limites reais | Atendido | Verificadores, resultados e hashes registrados, com ambientes distinguidos |
| Entregar novas aulas, pré-requisitos, rubricas e projetos curriculares | Não aplicável a BAN-01 | Correção pontual do banco existente; não é uma nova unidade curricular |
| Demonstrar eficácia com alunos ou aprovar todas as portas ACE | Não aplicável a BAN-01 | Requisitos globais continuam pendentes |

**Ajustes obrigatórios remanescentes de BAN-01: nenhum.**

## Limites e efeito sobre progresso

As verificações de código e as execuções de funções em isolamento são identificadas como tais. Não houve ensaio de navegador, leitor de tela ou teste com alunos. O uso de adaptadores mínimos para executar a correção não equivale a verificar renderização; nenhum resultado desse tipo é alegado.

As 30 digitais diferem da versão original. Tentativas anteriores à correção deixam de contar na versão vigente, e não foi implementada migração do histórico. Esse efeito foi declarado, reproduzido e considerado no parecer r1: a filtragem existente evita atribuir letras antigas aos novos conteúdos, e módulo/portal concordam. UX-11 e os requisitos globais de sinalização, versão e continuidade permanecem pendentes e não recebem aprovação implícita neste parecer. O efeito deve continuar explícito na comunicação ao usuário.

O aceite de BAN-01 se apoia nos critérios específicos inteiramente satisfeitos, não em promessas de resolver depois um defeito deste item. As tarefas distintas de evolução curricular, experiência e validação do curso permanecem no plano geral.

## Decisão de liberação

**APROVADO para os hashes registrados acima.** O coordenador pode registrar BAN-01 como aprovado e liberar **um próximo ID**, respeitando a ordem e as dependências do protocolo. O Corretor deve aguardar essa liberação concreta antes de começar outra correção.

Este aceite encerra a correção BAN-01 examinada. Não certifica qualidade global “AAA”, domínio de estudantes nem nível avançado do curso inteiro. Alteração posterior que invalide os critérios ou evidências exige reabertura do item.
