# Parecer FUN-02 — rodada 1

Data: 27/10/2026. **Veredito: APROVADO.** Revisor responsável: agente automatizado `/root/auditor_aaa`, independente da autoria. Apoio técnico: agente automatizado `/root/auditor_aaa/auditoria_tecnica_ban02`. Este parecer não representa certificação externa, revisão humana ou aplicação com estudantes.

## Critério e versão

FUN-02 exige diferenciais exatas e inexatas, integrais de processo e ciclo, derivadas parciais e condições mantidas. Seu aceite é explicar a dependência de calor/trabalho do caminho e construir dois processos entre os mesmos estados com balanços distintos. Foram examinados também todos os requisitos comuns do §3.2 da auditoria principal e as regras de preservação do protocolo.

Escopo: unidade 4.1 completa, preparação matemática, três problemas abertos, soluções e rubricas, dados/código/figura, três novos registros e resumo do inventário, seis atualizações parciais da matriz C01–C10 e navegação correspondente. Entrega: [FUN-02-r1](../entregas/FUN-02-r1.md); [manifesto congelado](../evidencias/FUN-02/manifesto-r1.json). Os seis hashes abaixo foram reconferidos no encerramento, sem mudança desde a entrega.

| Arquivo | SHA-256 |
|---|---|
| `modulos/e1-termodinamica.html` | `719a53ef86075dd3be9c7d9603faca620ec07416d1e97a5017740abb5b74c01a` |
| `assets/termodinamica/fun02-dados-v1.json` | `511aac986e9122e5498cdf69609274685791000a19f140a09d539fca01676319` |
| `assets/termodinamica/fun02-calculos-v1.mjs` | `2fdd0e498c41db2f7f8e90d5114dcd015f5377e00901e6274f25262e13c79a70` |
| `assets/termodinamica/fun02-caminhos-v1.svg` | `f324acce9060eb15eeab58958649392f4e5b667fbaf2ad9b63e3c68fbe3eae35` |
| `auditoria/termodinamica/inventario/inventario-questoes.json` | `c577058429375c11196eb99ae6bd01a9020f5258d3981d72c58896829ed900a2` |
| `auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md` | `c650d94556d527725595dfc86b1feaa055a32a2d9060e9b4680f1a152e11cca4` |

## Verificação científica independente

P1 e P3 foram resolvidos a partir dos enunciados congelados, antes da leitura das soluções ou dos resultados/código dos autores. A memória está em [cálculos independentes](FUN-02-r1-calculos-independentes.json). P2 foi resolvido anteriormente pelo enunciado isolado, sem consulta à solução; os dados, expressões, domínio e sete comandos foram reconferidos na versão integrada: [resolução preliminar](FUN-02-p2-preliminar.md) e [cálculos](FUN-02-p2-preliminar-calculos.json). Depois, houve leitura integral da teoria, dos três enunciados, soluções, rubricas e metadados novos. A aprovação não resulta apenas de executar os testes do Corretor.

**P1 — construção dos caminhos.** Obtive pA = 249.420 Pa e pB = 187.065 Pa. A rota isobárica–isocórica passa por 600 K e produz W = 2.494,200 J, ΔU = 1.870,650 J e Q = 4.364,850 J. A rota isotérmica a 300 K–isocórica produz W = 1.728,847698 J, a mesma ΔU e Q = 3.599,497698 J. Cada trecho fecha o balanço e permanece na janela. O percurso proposto a pB após a etapa isocórica passa por 225 K e deve ser recusado. O ciclo I com retorno por II invertido tem W = Q = 765,352302 J e ΔU = 0. Os sinais da solução estão corretos.

Também calculei as três outras ordenações admissíveis entre os controles fornecidos. A solução e a rubrica aceitam alternativas, exigem a verificação da faixa e não impõem o ciclo de referência a toda resposta. A inversão física é justificada pelas hipóteses mecânicas e térmicas explícitas. A afirmação sobre W = −ΔU em processo adiabático está corretamente condicionada à admissibilidade desse processo; não promete uma adiabat reversível entre os estados deste problema.

**P2 — integrabilidade e diagnóstico.** Reconstruí Φ/E₀ = θ ln θ − θ + (θ − 1) ln ν + ν²/2 + 1/2. Suas duas parciais e a referência conferem. O defeito das cruzadas de B é 2E₀κ(θ − 2)/ν: κ = 0 é a condição de exatidão em todo o quadrante; a linha θ = 2 não fornece uma vizinhança aberta de exatidão para κ diferente de zero. O ciclo largo cancela para qualquer κ, enquanto o esquerdo identifica κ = 0,200 na família declarada.

As duas integrais de A são 257,944154 J/mol; B fornece 257,944154 e 271,807098 J/mol. Sua diferença é −13,862944 J/mol, com a orientação especificada. A parcial a volume molar constante vale 0,462098 J/(mol·K), enquanto a inclinação ao longo de ν = θ vale 1,295431 J/(mol·K). A solução distingue corretamente número, rótulo, condição mantida e conversão por Tref. Corrigir κ para zero altera os ensaios representados: não permite preservar silenciosamente a observação não nula. A interpretação matemática não é apresentada como demonstração de uma equação fundamental física.

**P3 — calor por kelvin e fator integrante.** Obtive T₂ = 600 K, W = −4.988,400 J, ΔU = 3.741,300 J e Q = −1.247,100 J. A capacidade do caminho é −4,157 J/K, enquanto CV = 12,471 J/K e Cp = 20,785 J/K; as bases total e molar são diferenciadas. A coincidência entre Q/ΔT e a razão diferencial decorre da constância demonstrada neste caso. O expoente 3/2 não implica adiabaticidade.

O teste de δQrev falha, e o de δQrev/T produz um potencial global no quadrante positivo. Pelas propriedades e pela integral ao longo do caminho, ΔS = −2,881412830 J/K, diferente de Q/T₁ = −4,157 J/K. A discussão final não rejeita automaticamente δQreal/Tgás = dS apenas por haver diferença finita de temperatura com a vizinhança: distingue reversibilidade interna, temperatura da fronteira e geração externa/interna. Não muda ΔS entre os mesmos estados. Os comandos e a rubrica preservam essa distinção.

**Teoria, dados e figura.** A aula desenvolve a regra da cadeia com variáveis mantidas, reconstrução do potencial, regularidade e domínio, suficiência global em região simplesmente conexa e a distinção entre uma curva e uma vizinhança aberta. Não transforma simples conexão em condição necessária para todo potencial. Distingue teste matemático de admissibilidade física. Os sinais Q recebido/W realizado são consistentes; p interno dV fica restrito às hipóteses apropriadas. As integrais resolvidas mostram decisões, não apenas substituições.

O JSON declara os modelos ideais, constantes, domínio, autoria e versão; não alega usar propriedades experimentais. O código é coerente com esses dados. O potencial interno usado pelo código difere por constante da referência escrita, mas é usado somente em diferenças, que conferem. A curva quantitativa do SVG contém 161 pontos da isoterma; sua conversão independente para os eixos resulta em desvio máximo de aproximadamente 0,000516 kPa, compatível com o arredondamento de coordenadas. Estados, sentido, unidades e área de 765,35 J concordam com os cálculos. Essa é uma conferência estática; a inspeção visual foi feita pelo coordenador.

## Quadro completo de aceite

| Critério | Resultado e evidência |
|---|---|
| Diferenciais exatas/inexatas | Atendido. Desenvolvimento, potencial reconstruído, contraexemplos e P2/P3 verificados. |
| Domínio e alcance local/global | Atendido. Regularidade, simples conexão como garantia suficiente, região com furo e coincidência apenas em linha são diferenciadas. |
| Parciais e condições mantidas | Atendido. Aula com regra da cadeia; P2 exige corrigir a condição e a base de temperatura; P3 explicita K e n na trajetória. |
| Integrais de processo e de ciclo | Atendido. P1 integra trechos e fecha ciclo orientado; P2 constrói e interpreta cancelamento e ciclo não nulo. |
| Explicação de calor/trabalho dependentes do caminho | Atendido. Dois balanços entre os mesmos estados, variação de propriedade comum e transferências diferentes, com limites de generalizações. |
| Construção pelo aluno de dois processos | Atendido. P1 deixa a escolha dos controles ao aluno e exige admissibilidade, estados, integrais, balanços e condições de realização. |
| Objetivos observáveis e alcance | Atendido. Cinco resultados publicados e cobertura parcial das competências explicitada. |
| Pré-requisitos e preparação | Atendido para FUN-02. Bases indicadas, recuperação de cálculo/unidades, derivadas parciais ensinadas e preparação específica do P2. Não encerra o diagnóstico geral GOV-03. |
| Teoria e hipóteses | Atendido. Modelos, pressões absolutas, bases, composição, capacidade constante, trabalho e reversibilidade delimitados. |
| Exemplo resolvido com decisões | Atendido. Exemplos de parcial versus caminho, reconstrução de potencial, pressão linear e capacidade em isoterma expõem o motivo das escolhas. |
| Prática independente e novidade local | Atendido. P1 combina construção e restrição operacional; P2 combina defeito paramétrico, ciclos e condição mantida; não são simples trocas de números dos exemplos. P3 integra e interpreta um caminho novo, mas seus testes formais repetem ferramentas ensinadas: classificado como intermediário. |
| Soluções e rubricas | Atendido. Todas as partes respondidas, rubricas de 10 pontos, crédito parcial e erros críticos. Alternativas válidas são aceitas e erro aritmético propagado não é penalizado automaticamente várias vezes. |
| Fontes e versão dos dados | Atendido. Referências localizáveis, dados autorais E1-FUN02 v1.0 de 27/10/2026 e hipóteses explícitas; conferência bibliográfica descrita abaixo. |
| Revisão científica e numérica | Atendido. Resolução independente anterior à consulta, confronto integral das soluções e execução técnica complementar. |
| Vínculos C01–C10 | Atendido no alcance desta unidade. Atualizações C01/C02/C03/C08/C09/C10 correspondem a atividades reais e mantêm lacunas explícitas. Não encerra GOV-02 ou domínio integral das competências. |
| Registro de responsáveis e evidências | Atendido. Entrega/manifesto identificam autoria, revisão, data, arquivos, resultados e limites; este parecer registra a decisão independente. |
| Inventário e classificação cognitiva | Atendido. Três objetos individuais coerentes com enunciados, hipóteses, etapas e exposição prévia. P1/P2 avançados e P3 intermediário são estimativas justificadas pelo comando, sem piloto. |
| Preservação e escopo | Atendido. 194 artigos, registros e linhas anteriores intactos; alterações HTML limitadas à unidade, navegação e seis deltas da matriz. Infraestrutura compartilhada e FUN-01 preservados. |
| Interface na extensão alterada | Atendido com a evidência limitada do coordenador. Navegação, soluções, rubricas, teclado em P1 e figura observados na versão final; não equivale a auditoria integral UX. |
| Aplicação com estudantes ou certificação global | Não aplicável ao fechamento isolado de FUN-02; não executada nem alegada. O limiar pedagógico de 8/10 está declarado como não calibrado. |

O confronto de exposição inclui os exemplos da unidade e os itens Q09, AV30 e CR36 relacionados nos metadados. P1 exige construção e seleção que esses itens não exigem. P2 não se reduz à forma polinomial resolvida na aula. O teste do fator 1/T em P3 foi ensinado antes e não foi contado como descoberta inédita. A ausência de duplicação local não foi convertida em garantia de ineditismo universal ou desconhecimento prévio pelo estudante.

## Fontes consultadas e limites de acesso

Foram abertas e conferidas fontes primárias: [University of Washington, CHEM452 Winter 2023, apêndice 4.1](https://faculty.washington.edu/jcv2/CHEM452_WI2023/html/appendix_differentials.html), para a notação das condições mantidas; [OpenStax Calculus 3, §6.3](https://openstax.org/books/calculus-volume-3/pages/6-3-conservative-vector-fields), para potenciais e hipóteses do teste global; [MIT SPRING, §2.1](https://web.mit.edu/16.unified/www/SPRING/thermodynamics/notes/node14.html), para a convenção e a distinção propriedade/transferência; [OpenStax University Physics 2, §3.4](https://openstax.org/books/university-physics-volume-2/pages/3-4-thermodynamic-processes) e [§4.6](https://openstax.org/books/university-physics-volume-2/pages/4-6-entropy), para processos e o percurso reversível na definição de entropia. Não importei simplificações dessas fontes que contrariassem as hipóteses mais explícitas do módulo.

O acesso web ao PDF Purdue ME200 Spring 2023, cap. 6, falhou por timeout em duas tentativas desta rodada. O coordenador posteriormente obteve a cópia primária local; não alego ter extraído sua página 2 nesta auditoria. A conferência independente da distinção relevante foi feita diretamente em [Purdue, Wassgren, §3.6.7](https://engineering.purdue.edu/~wassgren/teaching/ME20000/NotesAndReading/Lec24_Reading_Wassgren.pdf), equações 3.141–142 e 3.149–153: temperatura na fronteira, processo internamente reversível e geração no sistema. O insucesso do extrator local de PDF também não foi contado como leitura. A limitação de acesso não encobre uma divergência científica pendente.

## Reprodução, interface e preservação

O [relatório técnico independente](FUN-02-r1-tecnico.md) e seu [JSON](FUN-02-r1-tecnico.json) documentam a execução efetiva no Node REPL de 240 verificações documentais, 49 numéricas e do validador: 197 artigos/registros, 11 recursos, 1.062 referências locais, zero erros e avisos. As saídas conferem com a entrega. A conferência independente abrange os seis arquivos/cópias, 26 evidências, 194 artigos/registros/linhas preservados, todos os títulos e a recomposição literal do HTML anterior. Os testes de contrato BAN-02 não foram repetidos porque schema, validador e guia estão intactos.

O [registro de navegador do coordenador](../evidencias/FUN-02/navegador-coordenador-r1.md), vinculado ao mesmo hash, relata navegação, abertura das três soluções e rubricas, alternância por Return em P1 e inspeção visual do SVG. Eu não executei navegador, leitor de tela ou piloto. Não são alegados todos os tamanhos de tela, todos os navegadores ou uma auditoria completa de acessibilidade. A revisão científica acima é independente desse teste de interface.

## Decisão e próxima dependência

**Não há ajustes obrigatórios para FUN-02 r1. APROVADO para os seis hashes identificados. O gate de FUN-02 está liberado: o coordenador pode registrar o aceite e autorizar exclusivamente o próximo ID escolhido. O Corretor não deve iniciar outro ID sem essa autorização.** Qualquer alteração posterior relevante exige conferir a validade deste parecer para a nova versão.

A prioridade proposta de **FON-09** é adequada e não apresenta dependência impeditiva de fechamento prévio de BAN-10 ou FON-01 inteiros. A tarefa pode ser tratada no recorte dos dados associados a CR68: conferir documento/página e origem exata de cada erro, identificar a transcrição preservada, fornecer o conjunto corrigido com unidades, modelo, referência e precisão rastreáveis e impedir uso da tabela defeituosa como dado físico. A nota existente, por si só, não atende ao aceite. Uma consulta restrita à prova e ao gabarito do item para preservar sua interpretação não equivale a conferir todo o banco. Esta é somente análise de dependência; não houve implementação nem aceite de FON-09.

Permanecem abertos os demais P0 legados e os requisitos gerais de conteúdo, governança, avaliação, fontes e experiência. A aprovação de FUN-02 não declara o curso inteiro avançado nem aprova por consequência FUN-03, PROP-06, a segunda lei, GOV-02 ou qualquer outra tarefa.
