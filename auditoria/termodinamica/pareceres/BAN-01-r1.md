# Parecer BAN-01 — rodada 1

**Data:** 27/10/2026, America/Sao_Paulo.  
**Revisor:** agente automatizado Auditor AAA (`/root/auditor_aaa`).  
**Versão examinada:** entrega BAN-01-r1.  
**Veredito:** **AJUSTES_OBRIGATORIOS**.  
**Liberação do próximo ID:** **NÃO LIBERADO**.

## Critério e escopo

O critério original determina reorganizar as alternativas das 30 questões iniciais, atualizar conjuntamente gabarito, comentário e referências às letras, eliminar a sequência ABCDE repetida, manter resposta única correta e verificar cada item sem criar outra sequência sistemática.

Examinados integralmente os 30 artigos `q-e1-01` a `q-e1-30`, suas 150 alternativas, todos os comentários, as 140 justificativas por alternativa, as seis justificativas por proposição de Q13/Q18 e o mapa E1 em `assets/registro.js`. Não foi feita validação integral dos bancos CR/AV nem aceite de BAN-07/BAN-08/UX-11 ou do curso inteiro.

A permutação e a atualização técnica estão corretas. A leitura independente identificou duas insuficiências preexistentes nos enunciados afetados que impedem afirmar integralmente o critério de resposta única sem hipóteses reveladas apenas na solução. A correção mecânica não introduziu esses problemas; preservá-los, contudo, não os converte em evidência de resposta inequívoca para o aceite exigido.

## Arquivos e versões

| Arquivo | SHA-256 examinado |
|---|---|
| `modulos/e1-termodinamica.html` | `d375695006edf96cbb709b7e85e7ebb84e94474333505768a3cccec0e94119a4` |
| `assets/registro.js` | `234cb179c3a7c81043d9d66ee65116b2f07503999aac6a45c433dccd51545055` |
| `assets/curso.js` — comportamento lido, sem alteração | `81728c9fd1e96b738410e6b51cf4ab3ed785fb17753e68a988c1dcf236d8f899` |

As cópias anteriores entregues pelo Corretor coincidem integralmente com os arquivos lidos e preservados independentemente pelo Auditor antes das alterações: HTML `10c3d92ef94136069dc94ee102fc0ff6e30b94cda82a66edf62de7d5346c015f`; registro `d55c275daf98a485574c40661155b02d25d1636d90ec2cb856d635df0b4f95fc`.

## Verificações independentes e resultados

1. **Comparação exaustiva:** 30/30 artigos identificados; 150/150 conteúdos de alternativas preservados; cada permutação derivada pelo Auditor a partir do conteúdo, sem depender do mapeamento proposto. Todas as alternativas mantêm rótulos A–E na ordem de apresentação, sem duplicatas.
2. **Gabaritos e comentários:** 30/30 respostas pretendidas preservadas semanticamente e gabaritos visíveis/atributos concordantes. As 140 justificativas acompanharam corretamente seus conteúdos. Q13/Q18 mantêm I/II/III intactos. Enunciados, soluções, figuras, fórmulas e demais elementos de cada artigo permanecem idênticos fora das permutações e letras autorizadas.
3. **Escopo:** bytes externos aos 30 artigos idênticos; bytes de `registro.js` externos ao mapa `modulos.e1.questoes` idênticos. O comportamento compartilhado `curso.js` permanece idêntico à base.
4. **Digitais reais:** o Auditor construiu árvores dos fragmentos e executou as funções originais `textoDaDigital`, `normalizarDigital` e `fnv1a` de `curso.js`. Reproduzidas as 30 digitais anteriores e as 30 novas. Registro E1 sincronizado, 30 digitais únicas e nenhuma colisão com as anteriores.
5. **Correção funcional isolada:** executada a função original `mostrarCorrecao` para cada uma das cinco escolhas em cada questão: **150 casos**, com 30 acertos e 120 erros esperados. Letra correta, destaque, seleção, feedback e disponibilidade de refazer conferidos em adaptadores mínimos de elementos. Isso não é ensaio de navegador.
6. **Progresso:** executadas as funções originais `lerEstadoModulo` e `progressoDoModulo` com estados anteriores, novos e mistos. Respostas antigas não foram indevidamente atribuídas às letras novas; estados novos tiveram 30 respostas e 30 acertos no módulo/portal. Estado misto mantém somente as digitais vigentes.
7. **Sequência:** `CBECCDEABEDCCEAADDAAECCCEBAECB`; A=6, B=4, C=9, D=4, E=7. Ausentes períodos globais de 1 a 15 e repetição dos seis blocos de cinco; inspeção não encontrou rotação fixa ou alternância sistemática substituta. Não se exige frequência perfeitamente uniforme; tampouco se afirma comprovação psicométrica de aleatoriedade.
8. **Reprodução:** o verificador do Corretor foi lido e executado, com 30 itens verificados. Além dele, foi escrito e executado `BAN-01-r1-verificacao.mjs`, independente do mapeamento proposto. O resultado está em `BAN-01-r1-evidencias.json`, ambos nesta pasta de pareceres.
9. **Leitura de resposta única:** os 30 comandos e alternativas foram lidos. Foram refeitos os cálculos elementares: Q02=300 kPa; Q04=0,25; Q06=100 kPa; Q07=300 kJ; Q08=40 kJ; Q09=200 kJ produzidos; Q11=800 kW; Q12=magnitude 0,5 kJ/kg; Q15=35%; Q16=50%; Q17=COP 3 e 1.200 kJ; Q19=80%; Q23=COP 3; Q26=2.860 kJ/kg; Q27=4 bar absolutos; Q28=80%; Q29=0,10 kW/K. Nos conceituais, as classificações e sequências pretendidas permaneceram coerentes; as insuficiências de Q10/Q12 estão explicitadas abaixo.

Não houve execução em navegador, avaliação com estudantes, leitor de tela ou certificação externa. Os testes isolados não comprovam renderização ou acessibilidade. A ausência desses ensaios não é a causa da rejeição desta rodada: as modificações são de dados, houve comparação integral da estrutura preservada e execução das funções afetadas em todos os casos de escolha. As causas são os dois enunciados abaixo.

## Quadro de critérios

| Critério aplicável | Estado | Evidência ou justificativa |
|---|---|---|
| Reorganizar as 30 questões | Atendido | 30 permutações não triviais comprovadas |
| Eliminar ABCDE repetido e outra sequência sistemática | Atendido | Sequência e verificações documentadas |
| Atualizar gabarito visível e atributo | Atendido | 30/30 concordantes |
| Atualizar comentários e referências às letras conjuntamente | Atendido | 140 associações preservadas; proposições I/II/III intactas; letras de estados da figura Q09 preservadas |
| Manter conteúdo das alternativas e resposta pretendida | Atendido | 150 conteúdos idênticos e alternativas corretas semanticamente preservadas |
| Demonstrar resposta única com condições disponíveis antes da resolução | **Não atendido integralmente** | Q10 omite regime usado na dedução; Q12 não distingue magnitude de trabalho e valor com sinal |
| Verificar cada item depois da alteração | Atendido | Leitura 30/30, comparação integral, 150 casos de correção isolada |
| Concordância científica entre enunciado e solução | **Não atendido integralmente** | Q10/Q12 revelam condições relevantes apenas na resolução |
| Registro de progresso coerente com o novo banco | Atendido no escopo BAN-01 | Digitais reproduzidas e filtragem existente executada; continuidade histórica tratada abaixo |
| Preservar outros módulos e comportamento compartilhado | Atendido | Comparação exata das partes externas ao mapa E1 e dos arquivos-base |
| Versão, evidências, revisor e limitações reais | Atendido | Hashes e verificadores disponíveis; ausência de navegador explicitada |
| Novas aulas, rubricas e projetos para item curricular | Não aplicável | BAN-01 é correção do banco existente, não autoria de nova unidade curricular |
| Classificação global de nível avançado | Não aplicável a esta entrega | Depende dos demais itens e das portas ACE |

## Ajustes obrigatórios para a rodada 2

### R1-A — Q10: declarar regime permanente no enunciado

O enunciado atual informa válvula adiabática, ausência de trabalho e pequenas mudanças de velocidade/altura. A solução elimina também a acumulação ao aplicar expressamente o balanço estacionário. Sem essa condição, o balanço geral admite acumulação de massa e energia, e a igualdade das entalpias não decorre apenas das condições enumeradas. A formulação de referência do MIT explicita escoamento permanente ao deduzir a relação de entalpia no estrangulamento. [MIT — Adiabatic throttling](https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node50.html).

**Correção exigida:** incluir a condição de regime permanente no enunciado, antes da tentativa, preservando a resposta pretendida e as demais hipóteses. Não é necessário transformar a questão em um problema transiente. Atualizar a digital correspondente e manter registro, gabarito e solução coerentes.

### R1-B — Q12: explicitar a grandeza e a convenção antes da tentativa

O comando atual pergunta apenas o trabalho específico aproximado. Entre as opções há `0,5 kJ/kg` e `−0,5 kJ/kg consumido`. A solução introduz depois a grandeza `w_in` como magnitude positiva. Sob a convenção de trabalho realizado pelo sistema positivo, também usada no próprio curso, trabalho de entrada tem valor negativo; portanto o aluno pode interpretar a segunda opção como valor algébrico do trabalho consumido. Esse conflito não se resolve dizendo apenas na resolução que se queria magnitude. A convenção que atribui sinal negativo ao trabalho recebido é explicitada na referência do MIT. [MIT — Primeira lei e sinais](https://ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_4.htm).

**Correção exigida:** pedir explicitamente a **magnitude do trabalho específico de entrada/consumido**, adotada positiva, no enunciado. Como alternativa equivalente, declarar outra grandeza/convenção inequívoca e rever coerentemente os itens afetados, mantendo o objetivo didático. Conservar a justificativa do sinal coerente com o comando e atualizar a digital correspondente.

### Evidência de reapresentação

- Entrega `BAN-01-r2.md` com resposta objetiva a R1-A e R1-B e novos hashes.
- Registrar os dois ajustes semânticos autorizados, sem afirmar preservação byte a byte desses enunciados em relação à base original.
- Preservar a permutação e todo o restante já conferido, exceto alterações estritamente necessárias às duas correções e às suas digitais.
- Atualizar o verificador para conferir explicitamente os dois enunciados novos e manter verificação exaustiva dos 30 itens. Não remover genericamente a verificação dos enunciados.
- Sincronizar o mapa E1, manter intactos os demais módulos e repetir as verificações pertinentes.

## Decisão sobre continuidade do progresso

A mudança de digitais faz com que tentativas anteriores deixem de contar na versão atual; o histórico não é migrado. Isso é uma limitação concreta de continuidade, declarada na entrega e reproduzida pelo Auditor. O código existente foi desenhado para filtrar respostas de questões modificadas, e a atualização de `registro.js` impede divergência entre módulo e portal. Não há associação silenciosa de uma letra antiga a uma alternativa nova.

Não imponho uma nova infraestrutura de migração como condição de BAN-01: o item exige corrigir o banco e a avaliação continua semanticamente coerente sob a invalidação existente. O aceite global ainda dependerá de UX-11 e das obrigações de versão, sinalização e continuidade; esta revisão não aprova esses requisitos. O efeito sobre o progresso deve permanecer explícito ao comunicar a mudança ao usuário. A rejeição desta rodada decorre de R1-A/R1-B, não de um defeito inventado na filtragem existente.

## Decisão final

**AJUSTES_OBRIGATORIOS. O próximo ID permanece bloqueado.** O Corretor deve corrigir R1-A/R1-B e reapresentar BAN-01 para nova auditoria. Somente um parecer posterior `APROVADO` poderá liberar o coordenador a selecionar a próxima correção. Este parecer não certifica o curso como avançado.
