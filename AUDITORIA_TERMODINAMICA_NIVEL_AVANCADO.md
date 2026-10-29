# Auditoria de Termodinâmica — requisitos para nível avançado real

**Projeto:** Curso SOP-CE — Engenharia Mecânica  
**Escopo:** exclusivamente o curso E1 de Termodinâmica e seus materiais de apoio.  
**Data de referência:** 27/10/2026, America/Sao_Paulo.  
**Versão deste documento:** 1.0.  
**Resultado atual:** intermediário, com fundamentos acessíveis e aprofundamentos pontuais.  
**Objetivo:** transformar a avaliação anterior em um plano verificável de desenvolvimento, revisão e demonstração de domínio avançado.

> Este documento registra trabalho pendente. Uma caixa vazia significa requisito ainda não aceito, inclusive quando parte do conteúdo já existe. A criação desta auditoria não implementa as correções nem certifica o curso. Os critérios quantitativos são metas internas propostas para este projeto, não exigências universais de universidades, bancas ou órgãos de acreditação.

**Dimensão do plano:** 169 itens verificáveis: 149 ações obrigatórias de conteúdo, avaliação e suporte (10 P0, 111 P1 e 28 P2), 10 extensões de especialização e 10 portas finais de aceite. O aceite de AVA-07 distingue preparação do protocolo de execução empírica, conforme explicado na seção 10.

### Guia de leitura

| Seções | Finalidade |
|---|---|
| 1–3 | Definição do nível, evidências atuais e regra de aceite |
| 4–5 | Percurso e conteúdo científico a desenvolver |
| 6–8 | Modelagem, didática e revisão do banco de questões |
| 9–10 | Projetos, avaliações, rubricas e demonstração de domínio |
| 11–14 | Formulário, fontes, experiência de estudo e qualidade |
| 15 | Extensões especializadas, separadas do núcleo obrigatório |
| 16–17 | Ordem de execução, acompanhamento e decisão final |
| 18–19 | Referências e conclusão operacional |

## 1. O que significa avançado neste projeto

O alvo é **Termodinâmica avançada de engenharia, no contexto de graduação e aplicações profissionais**, preservando a utilidade para concursos de Engenharia Mecânica. O aluno deve conseguir modelar situações novas, obter propriedades, resolver sistemas com várias etapas, confrontar primeira e segunda leis, avaliar aproximações e defender uma decisão técnica.

Não basta apresentar fórmulas mais difíceis, aumentar o número de páginas ou mencionar exergia, Gibbs e gases reais. Um assunto só conta como competência avançada quando há explicação suficiente, resolução demonstrada, prática independente e avaliação inédita compatível.

O núcleo obrigatório desta auditoria é deliberadamente exigente. As extensões da seção 15 ampliam a especialização, mas não são todas necessárias para sustentar o título delimitado acima. Termodinâmica estatística, quântica e de não equilíbrio em profundidade exigiriam outro escopo. Também não se deve anunciar equivalência a uma disciplina específica de pós-graduação com base neste plano.

### 1.1 Competências de saída

| Código | Competência demonstrável | Evidência exigida |
|---|---|---|
| C01 | Definir sistema, fronteira, regime, hipóteses e incógnitas | Modelo justificado antes da substituição numérica |
| C02 | Selecionar propriedades e modelos de substância | Estados completos, fontes, interpolação e limites de validade |
| C03 | Aplicar massa e energia em sistemas fechados e volumes de controle | Balanços gerais e simplificações justificadas, permanentes e transientes |
| C04 | Aplicar a segunda lei e calcular geração de entropia | Balanço do sistema e de suas interações, com viabilidade física |
| C05 | Quantificar exergia, destruição e eficiência de segunda lei | Balanço completo com ambiente de referência e finalidade declarados |
| C06 | Resolver e comparar ciclos ideais e reais | Estados determinados pelo aluno, perdas, restrições e comparação coerente |
| C07 | Tratar misturas, propriedades reais e processos reativos no escopo definido | Bases molares/mássicas consistentes e modelos químicos/termodinâmicos explícitos |
| C08 | Utilizar tabelas, cálculo manual e ferramentas numéricas criticamente | Reprodução de resultados, resíduos, limites, sensibilidade e incerteza |
| C09 | Julgar propostas, dados insuficientes e resultados impossíveis | Argumentação técnica, identificação de informações faltantes e análise de erro |
| C10 | Comunicar e defender uma solução de engenharia | Relatório rastreável, diagramas, memória de cálculo e discussão das limitações |

### 1.2 Limites de responsabilidade

Esta auditoria não determina alterações em E2, A1, A2, A3, A4, B ou nos demais módulos. Quando uma aplicação usa trocadores, ar úmido, refrigeração, bombas ou vapor, a entrega do E1 deve se concentrar nos estados, balanços e desempenho termodinâmico. Dimensionamento detalhado de transferência de calor, seleção normativa, projeto mecânico e segurança operacional permanecem nas disciplinas próprias.

Arquivos compartilhados, como `assets/curso.js` e `assets/curso.css`, podem ser lidos para compreender o E1. Uma futura mudança neles deve ser isolada por escopo e acompanhada de verificação de regressão; esta auditoria não os altera.

## 2. Base examinada e limites da evidência

### 2.1 Inventário confirmado

| Material | Local | Constatação |
|---|---|---|
| Aula principal | [modulos/e1-termodinamica.html](modulos/e1-termodinamica.html) | Fundamentos, propriedades, duas leis, ciclos, aplicações, laboratório, oficina, diagnóstico e bancos |
| Banco inicial | Aula, IDs `q-e1-01` a `q-e1-30` | 30 itens autorais |
| Questões reais | Aula, IDs `cr-e1-01` a `cr-e1-80` | 80 itens identificados como questões de concursos |
| Treino autoral | Aula, IDs `av-e1-01` a `av-e1-80` | 80 itens no estilo Avalia; não são questões oficiais da banca |
| Preparação | Aula, seção `preparacao-questoes` | 28 diagnósticos; oficina anterior contém quatro atividades com tentativa independente |
| Revisão | Aula, seção `flashcards` | 21 cartões, além de glossário e resumo |
| Formulário | [formulas/termodinamica.html](formulas/termodinamica.html) | 100 fichas distribuídas por 11 grupos |
| Documentos de origem | [downloads/termodinamica/LEIA-ME.md](downloads/termodinamica/LEIA-ME.md) e [fontes.json](downloads/termodinamica/fontes.json) | 12 cadernos e 12 arquivos de gabaritos listados |
| Comportamento | `assets/curso.js`, `assets/formulario-e1.js`, `assets/registro.js` | Componentes compartilhados, treino e armazenamento local |

O inventário é diferente de uma validação completa de conteúdo. A análise examinou a estrutura, os trechos teóricos, as 30 questões iniciais e amostras dos bancos adicionais; não conferiu individualmente os 190 gabaritos contra todos os PDFs. Não foram realizadas nesta etapa sessões de aprendizagem com alunos, testes de leitor de tela, ensaios completos de navegador nem reprodução computacional de todos os exemplos. Essas verificações aparecem como tarefas, não como aprovações presumidas.

As verificações estáticas complementares desta auditoria encontraram os 24 documentos locais com tamanho e SHA-256 correspondentes ao manifesto. Também não encontraram destinos locais/fragmentos ausentes na análise de links do E1 e do formulário: 1.204 IDs únicos no módulo e 431 no formulário. As 16 ocorrências de imagem do E1 possuem `alt`. São 734 elementos MathML no módulo e 191 no formulário. Esses resultados mostram estrutura e integridade local; não comprovam autenticidade independente dos PDFs, transcrição correta, qualidade de descrição, leitura assistiva ou execução no navegador.

### 2.2 Achados que já sustentam a classificação

| Evidência | Constatação | Consequência |
|---|---|---|
| Teoria: “Quando o calor específico varia” | Há integrais e exemplo com expressão linear de calor específico | Base útil, mas ainda exige aplicações autônomas em ciclos e transientes |
| Teoria: “Disponibilidade e exergia” | Conceitos e Gouy–Stodola estão presentes | É necessário avançar para balanços completos, referências e eficiências de segunda lei |
| Teoria: “Reaquecimento e extração” | Balanços explicados com entalpias já fornecidas | Faltam evidências de domínio de obtenção de todos os estados e análise integrada |
| `av-e1-37` | O próprio enunciado fornece a relação de trabalho perdido; o cálculo central é 300 × 0,20 | Nome de assunto avançado não equivale a complexidade avançada |
| `av-e1-57` | O fator exponencial do Brayton já é fornecido como 2 | Avalia uma substituição curta, não a solução do ciclo |
| `q-e1-26`, `q-e1-27`, `q-e1-29` | Reutilizam os dados dos exemplos de interpolação, dois estágios e entropia do trocador | Úteis para fixação; insuficientes como prova de transferência independente |
| `q-e1-01` a `q-e1-30` | Gabarito A, B, C, D, E repetido seis vezes | Padrão previsível fragiliza a avaliação |
| Correspondência entre bancos de 80 itens | Os tópicos dos itens reais e autorais se correspondem | Boa ligação com a base, mas quantidade não deve ser confundida com 160 desafios independentes |
| Entrada do banco real | O próprio material sinaliza ressalvas nos itens 09, 24, 68 e 79 | É obrigatório conferir origem, leitura técnica e tratamento avaliativo de cada ressalva |

### 2.3 Identificação da versão auditada

Os hashes permitem distinguir esta análise de futuras versões. Não substituem validação pedagógica ou científica.

| Arquivo | Bytes | SHA-256 |
|---|---:|---|
| `modulos/e1-termodinamica.html` | 1109588 | `10c3d92ef94136069dc94ee102fc0ff6e30b94cda82a66edf62de7d5346c015f` |
| `formulas/termodinamica.html` | 224180 | `07e4b579c437c2ae0feefc8e2260607da827e335ca6694b1d583181632851e96` |
| `downloads/termodinamica/fontes.json` | 13441 | `bd76d1b63a253a0c719a19591101e21a852e6fa0a2411efe3baebb5773c7af6b` |

## 3. Como executar e aceitar as tarefas

### 3.1 Prioridades e estado

- **P0 — correção/bloqueio:** compromete validade da avaliação, correção científica ou integridade dos dados. Resolver antes de usar o material afetado como comprovação de domínio.
- **P1 — núcleo avançado:** obrigatório para o nível-alvo definido neste documento.
- **P2 — suporte obrigatório:** necessário à entrega utilizável, verificável e sustentável; pode ser construído em paralelo ao conteúdo.
- **E — extensão:** aprofundamento especializado, com requisitos condicionados à promessa de cobertura.

Nos itens abaixo, **ampliar** significa que há base presente; **incluir** significa que o desenvolvimento requerido não foi localizado como unidade completa na leitura; **verificar** significa que não há evidência suficiente para aceitar nem para declarar defeito. “Não localizado” não deve ser convertido em afirmação de ausência absoluta sem inventário completo.

### 3.2 Regra de aceite comum

Para concluir qualquer item curricular obrigatório, entregar: objetivo observável; pré-requisitos; teoria e hipóteses; ao menos um exemplo resolvido que exponha decisões; exercício inédito independente; solução e rubrica; fonte e versão dos dados; revisão científica e numérica; ligação com a matriz C01–C10. Um tópico complexo pode exigir várias atividades. O mínimo de um exemplo não limita o trabalho necessário.

Uma simples troca de números, um novo título ou a inclusão de uma fórmula não satisfazem o aceite. Registrar responsável, revisor, data, arquivos, evidência e pendências. Não marcar como concluído um requisito apoiado apenas em uma intenção.

## 4. Governança curricular e progressão

- [x] **GOV-01 — Delimitar a promessa do curso [P1; incluir].** Publicar os resultados de aprendizagem C01–C10 e distinguir preparação para concurso de formação avançada aplicada. **Aceite:** cada promessa aponta para conteúdos e instrumentos que efetivamente a avaliam; nenhuma promessa de cobertura universal de provas ou de todos os ramos da Termodinâmica. **Aceito em 27/10/2026:** [parecer GOV-01-r1](auditoria/termodinamica/pareceres/GOV-01-r1.md). As competências avançadas permanecem alvos em desenvolvimento; o aceite delimita a promessa e não encerra GOV-02.
- [ ] **GOV-02 — Construir matriz de rastreabilidade [P1; ampliar].** Mapear cada competência até aula, exemplo, diagnóstico, questão, problema aberto, projeto e avaliação final. **Aceite:** não existem competências obrigatórias sem ensino e avaliação, nem questões cuja base necessária esteja apenas presumida.
- [ ] **GOV-03 — Estabelecer pré-requisitos [P1; ampliar].** Diagnosticar álgebra, unidades, logaritmos, cálculo diferencial/integral, derivadas parciais, equações diferenciais simples e leitura de gráficos. Oferecer recuperação direcionada. **Aceite:** o aluno identifica o que precisa revisar antes de cada unidade e comprova essa base em exercícios próprios.
- [ ] **GOV-04 — Separar níveis de estudo [P1; incluir].** Organizar revisão fundamental, desenvolvimento intermediário e desafios avançados, com rotas de entrada e progressão. **Aceite:** um iniciante consegue progredir sem saltos ocultos e um aluno experiente consegue localizar o núcleo avançado sem refazer toda a introdução.
- [ ] **GOV-05 — Sequenciar dependências [P1; ampliar].** Propriedades antecedem ciclos; massa/energia antecedem entropia; entropia e ambiente antecedem exergia; modelos de substância antecedem otimização. **Aceite:** mapa de dependências sem referência circular obrigatória e percurso demonstrado até os projetos finais.
- [ ] **GOV-06 — Dimensionar o esforço de aprendizagem [P2; incluir].** Estimar leitura, prática, cálculos, projetos e revisões por unidade e depois calibrar com pilotos. **Aceite:** carga horária baseada em tarefas reais, distinguindo estudo ativo de tempo de leitura; não transformar extensão textual em estimativa automática de horas.

## 5. Auditoria científica e de conteúdo

### 5.1 Fundamentos, linguagem matemática e representação

Base atual: seções `fundamentos`, `substancias`, `energia` e explicações de símbolos. Preservar a clareza e ampliar a capacidade de derivar e escolher modelos.

- [x] **FUN-01 — Estado, equilíbrio e graus de liberdade [P1; ampliar].** Desenvolver equilíbrio térmico, mecânico, químico e de fases; postulado de estado de sistemas simples compressíveis; composição e independência de propriedades. **Aceite:** classificar pares de dados suficientes, redundantes ou incompatíveis, inclusive saturação, misturas e região supercrítica. **Aceito em 27/10/2026 após duas rodadas:** [parecer FUN-01-r2](auditoria/termodinamica/pareceres/FUN-01-r2.md). Unidade, quatro problemas abertos, soluções, rubricas e dados revisados; aprovação restrita ao item e à versão examinada.
- [x] **FUN-02 — Diferenciais, caminhos e propriedades [P1; ampliar].** Trabalhar diferenciais exatas e inexatas, integrais de processo e de ciclo, derivadas parciais e condições mantidas. **Aceite:** o aluno explica por que calor/trabalho dependem do caminho e constrói dois processos entre os mesmos estados com balanços distintos. **Aceito em 27/10/2026:** [parecer FUN-02-r1](auditoria/termodinamica/pareceres/FUN-02-r1.md). Teoria, três problemas abertos, soluções, rubricas, dados e figura revisados; alcance restrito à unidade e à versão aprovada.
- [ ] **FUN-03 — Quase equilíbrio e reversibilidade [P1; ampliar].** Separar processo quase estático, ausência de atrito, reversibilidade interna e externa. **Aceite:** resolver expansão contra pressão externa e comparar com caminho reversível, sem usar indiscriminadamente a pressão interna em trabalho de fronteira.
- [ ] **FUN-04 — Formas de trabalho e referências [P1; ampliar].** Distinguir trabalho de fronteira, eixo, elétrico, escoamento e trabalho útil contra o ambiente. **Aceite:** montar o balanço de um sistema com mais de uma forma de trabalho, sem duplicar `pv` e com convenção de sinais explícita.
- [ ] **FUN-05 — Diagramas quantitativos [P1; ampliar].** Construir e ler `p–v`, `T–s`, `h–s` e `p–h`, marcando regiões, estados, sentido, unidades e limites das interpretações por área. **Aceite:** produzir diagramas a partir de estados calculados e reconhecer quando uma figura é apenas esquemática.
- [ ] **FUN-06 — Valores de referência e bases [P1; ampliar].** Fixar convenções para propriedades específicas, molares, totais e taxas; referências de `u`, `h` e `s`; escalas e pressões absolutas. **Aceite:** combinar tabelas somente com referências compatíveis e demonstrar que uma mudança consistente de referência não altera o balanço de processo não reativo.

### 5.2 Propriedades de substâncias e relações termodinâmicas

Base atual: título, gás ideal, fator de compressibilidade, interpolação didática, calor específico variável e identidade de Gibbs. O trabalho é aprofundar obtenção e verificação de propriedades, não apenas acrescentar nomes de modelos.

- [ ] **PROP-01 — Tabelas reais completas [P1; ampliar].** Disponibilizar dados rastreáveis de água/vapor e de um refrigerante para líquido comprimido, saturação, superaquecido e supercrítico. **Aceite:** resolver estados a partir de diferentes pares, incluindo `(p,s)` e `(p,h)`, justificando região e método; não fornecer previamente todas as entalpias de cada problema.
- [ ] **PROP-02 — Interpolação e limites numéricos [P1; ampliar].** Ensinar interpolação simples e, quando necessária, em duas variáveis, avaliação de erro e limites perto do crítico e da mudança de fase. **Aceite:** comparar a aproximação com referência independente e recusar extrapolação ou interpolação entre regiões incompatíveis.
- [ ] **PROP-03 — Gás ideal com propriedades variáveis [P1; ampliar].** Usar `cp(T)`, `cv(T)`, integração e tabelas de funções de temperatura, incluindo entropia e processos isentrópicos. **Aceite:** comparar a hipótese de calor específico constante com a variável em um compressor e em um ciclo, quantificando diferença e faixa de uso.
- [ ] **PROP-04 — Modelos de gás real [P1; ampliar].** Sair do reconhecimento de `Z`: usar propriedades reduzidas e ao menos uma equação de estado real, com parâmetros e domínio conhecidos. **Aceite:** calcular um estado não ideal, identificar raízes fisicamente admissíveis e comparar ao gás ideal e a dados de referência; seleção de raiz não pode se apoiar apenas na convergência do solver.
- [ ] **PROP-05 — Propriedades energéticas de gás real [P1; incluir].** Explicar que corrigir `pv=RT` com `Z` não fornece automaticamente `h`, `u` e `s`; desenvolver relações de variação/residuais ou uma rota de tabelas consistente. **Aceite:** resolver transformação real com propriedades consistentes e demonstrar por que o método de energia de gás ideal pode falhar.
- [ ] **PROP-06 — Potenciais e relações de Maxwell [P1; ampliar].** Desenvolver `u`, `h`, Helmholtz e Gibbs, variáveis naturais, transformações pertinentes e relações de Maxwell de uso selecionado. **Aceite:** derivar ao menos uma relação a partir de um potencial e usá-la para obter uma propriedade ou dependência física, identificando hipóteses de composição e compressibilidade simples.
- [ ] **PROP-07 — Respostas termodinâmicas [P1; incluir].** Relacionar expansão térmica, compressibilidade isotérmica, calores específicos e a identidade geral que liga `cp−cv` a propriedades mensuráveis. **Aceite:** recuperar o caso de gás ideal e analisar um líquido sem pressupor universalmente `cp−cv=R`.
- [ ] **PROP-08 — Equilíbrio e transições de fase [P1; ampliar].** Desenvolver igualdade de potencial químico, estabilidade, graus de liberdade e Clapeyron/Clausius–Clapeyron com hipóteses explícitas. **Aceite:** estimar variação da pressão de saturação, confrontar uma tabela e explicar limites da aproximação, ponto crítico e estados metaestáveis.
- [ ] **PROP-09 — Estrangulamento e Joule–Thomson [P1; ampliar].** Quantificar a resposta térmica de um fluido real a entalpia constante e discutir sinal do coeficiente e região de inversão. **Aceite:** comparar gás ideal com um fluido real em uma válvula, sem concluir que toda redução de pressão necessariamente resfria.
- [ ] **PROP-10 — Consulta computacional rastreável [P1; incluir].** Ensinar consulta a biblioteca/documentação de propriedades, identificação de fase, unidades e referências. **Aceite:** reproduzir estados de controle por tabela e por ferramenta, com versão, modelo, par de entrada e tolerância; erros de fase devem gerar diagnóstico, não resultado silencioso.

### 5.3 Primeira lei, massa e regimes transientes

Base atual: convenção de sinais, sistema fechado, equipamentos estacionários, tanque enchendo, misturador, bocal e válvula.

- [ ] **ENE-01 — Sistemas fechados com etapas e restrições [P1; ampliar].** Incluir pistão com mola, batentes, carga externa e mudança de fase, quando fisicamente especificados. **Aceite:** determinar a sequência de eventos, estados intermediários, trabalho por trechos e energia total, sem assumir um único processo para toda a trajetória.
- [ ] **ENE-02 — Balanço geral de volume de controle [P1; ampliar].** Derivar e aplicar formas integral e diferencial de massa/energia com várias entradas e saídas, calor, eixo e acumulação. **Aceite:** construir o modelo geral antes de simplificá-lo e verificar quais termos desaparecem por hipótese, e quais apenas são pequenos.
- [ ] **ENE-03 — Enchimento e esvaziamento [P1; ampliar].** Ir além do tanque inicialmente evacuado: massa inicial não nula, saída, alimentação variável e esvaziamento. **Aceite:** resolver ao menos um enchimento e um esvaziamento com balanços integrados ou diferenciais e explicar por que `Tfinal=kTentrada` é um caso particular.
- [ ] **ENE-04 — Acoplamento fluido–parede e perdas [P1; incluir].** Incorporar capacidade térmica das paredes e uma lei de troca prescrita ao ambiente, mantendo o foco no balanço termodinâmico. **Aceite:** comparar solução adiabática com solução que inclui parede/perda e avaliar o limite em que cada simplificação é aceitável.
- [ ] **ENE-05 — Misturadores, separadores e redes de fluxos [P1; ampliar].** Combinar balanços em equipamentos conectados, recirculação, derivações e mudança de fase. **Aceite:** fechar massa e energia globalmente e por componente sem usar média de temperaturas quando o balanço exige entalpias.
- [ ] **ENE-06 — Energia cinética e estados de estagnação [P1; ampliar].** Relacionar entalpia estática e de estagnação, bocais/difusores e condições necessárias para determinar saída e vazão. **Aceite:** resolver um caso em que desprezar velocidade altera materialmente o resultado e reconhecer quando o balanço de energia, sozinho, não fecha o problema.
- [ ] **ENE-07 — Fenômenos acoplados e ordem de grandeza [P1; ampliar].** Decidir quando manter energias potencial/cinética, trabalho e perdas com estimativas, em vez de regras memorizadas por equipamento. **Aceite:** justificar descarte ou retenção de termos por comparação quantitativa com a precisão exigida.
- [ ] **ENE-08 — Medições e balanços inconsistentes [P1; incluir].** Usar dados medidos, arredondados e com incerteza para identificar resíduos e possíveis medições faltantes. **Aceite:** apresentar fechamento, limites de compatibilidade e diagnóstico sem “corrigir” arbitrariamente dados para forçar conservação.

### 5.4 Segunda lei e entropia

Base atual: enunciados, Carnot, balanços de entropia, gás ideal, expansão livre e eficiência isentrópica.

- [ ] **ENT-01 — Construção da segunda lei [P1; ampliar].** Desenvolver equivalência dos enunciados, teorema de Carnot e desigualdade de Clausius em uma sequência compreensível. **Aceite:** justificar as restrições usadas e distinguir definição de propriedade, desigualdade e igualdade de processo reversível.
- [ ] **ENT-02 — Entropia por diferentes rotas [P1; ampliar].** Calcular variações por tabelas reais, gás ideal com propriedades variáveis, sólidos/líquidos e mudanças de fase. **Aceite:** obter a mesma variação entre estados por rotas de referência compatíveis e não igualar a variação de entropia ao calor real dividido por uma temperatura arbitrária.
- [ ] **ENT-03 — Fronteiras térmicas e reservatórios finitos [P1; ampliar].** Tratar várias transferências, temperaturas de fronteira variáveis e fontes que esfriam/aquecem. **Aceite:** calcular geração de entropia do conjunto e comparar com a aproximação de reservatório a temperatura constante.
- [ ] **ENT-04 — Entropia em processos transientes [P1; incluir].** Aplicar acumulação e transporte de entropia em enchimento/esvaziamento e sistemas conectados. **Aceite:** apresentar balanços de massa, energia e entropia compatíveis no mesmo caso e identificar as irreversibilidades.
- [ ] **ENT-05 — Mistura e transferência com diferenças finitas [P1; ampliar].** Quantificar geração por mistura, troca térmica e quedas de pressão, deixando clara a fronteira de cada cálculo. **Aceite:** distribuir a geração por componentes sem dupla contagem e explicar diminuição de entropia de uma corrente com geração positiva no conjunto.
- [ ] **ENT-06 — Reversibilidade e eficiência isentrópica [P1; ampliar].** Determinar a saída isentrópica a partir da entrada e pressão final, em vez de receber todas as entalpias. **Aceite:** calcular estados real e de referência de turbina/compressor e verificar direção física das perdas e convenção de eficiência.
- [ ] **ENT-07 — Testes de impossibilidade [P1; ampliar].** Criar casos que conservam energia e violam a segunda lei, casos possíveis e casos com informação insuficiente. **Aceite:** o aluno classifica cada situação e explica qual dado adicional é necessário; não usa `eficiência<100%` como prova suficiente de viabilidade.

### 5.5 Exergia e avaliação de desempenho

Base atual: conceito, ambiente e Gouy–Stodola. É uma das principais frentes de aprofundamento.

- [ ] **EXE-01 — Ambiente e estado morto [P1; ampliar].** Especificar `T0`, `p0`, composição quando relevante, equilíbrio restrito/completo e fronteira do trabalho útil. **Aceite:** justificar a referência e mostrar como ela afeta exergia sem alterar a energia conservada.
- [ ] **EXE-02 — Exergia física de sistema fechado e de fluxo [P1; incluir].** Desenvolver expressões pertinentes com energia interna/entalpia, entropia, volume e parcelas cinética/potencial. **Aceite:** calcular ambas e explicar por que não são intercambiáveis; separar trabalho contra o ambiente de trabalho útil.
- [ ] **EXE-03 — Exergia de calor e fontes finitas [P1; incluir].** Calcular transferência de exergia por calor em temperatura constante ou variável e por trabalho. **Aceite:** integrar um resfriamento/aquecimento finito e mostrar por que não basta usar um fator de Carnot com uma temperatura escolhida sem justificativa.
- [ ] **EXE-04 — Balanços completos [P1; incluir].** Desenvolver exergia para sistemas fechados, volumes de controle permanentes e um transiente. **Aceite:** discriminar entrada, saída, acumulação, destruição e perda para o exterior, com fechamento e compatibilidade com `T0*Sger`.
- [ ] **EXE-05 — Eficiência de segunda lei [P1; incluir].** Definir produto e recurso para turbina, compressor, aquecedor, refrigerador e sistema integrado. **Aceite:** calcular indicadores coerentes com a finalidade e explicar por que fórmulas de eficiência não podem ser transportadas indiscriminadamente entre equipamentos.
- [ ] **EXE-06 — Diagnóstico por componente [P1; incluir].** Aplicar energia e exergia a uma instalação, localizar irreversibilidades e distinguir grande rejeição de energia de grande destruição de exergia. **Aceite:** apresentar balanço agregado e por componente, diagrama de fluxos e prioridades de melhoria sustentadas pelos números.
- [ ] **EXE-07 — Viabilidade de melhorias [P1; incluir].** Avaliar se reduzir irreversibilidade é tecnicamente alcançável sob restrições reais de temperatura, pressão e serviço. **Aceite:** comparar cenário-base e duas alternativas com a mesma função e fronteiras, evitando tratar toda exergia destruída como trabalho recuperável na prática.

### 5.6 Ciclos de potência, refrigeração e compressão

Base atual: ciclos ideais, eficiência, reaquecimento/extração com entalpias dadas e compressão em estágios. O nível avançado exige resolver estados, acoplar equipamentos e comparar decisões.

- [ ] **CIC-01 — Rankine completo com propriedades reais [P1; ampliar].** Resolver bomba, caldeira, turbina e condensador a partir de pressões, temperaturas e eficiências. **Aceite:** tabela completa de estados, vazão para uma potência requerida, calor, trabalho, rendimento, título final quando definido e balanços de energia/entropia.
- [ ] **CIC-02 — Rankine com reaquecimento e regeneração [P1; ampliar].** Incluir extração, aquecedor aberto e fechado, bombas e drenos, com vazões diferentes. **Aceite:** comparar casos coerentes, determinar frações de extração e verificar massa/energia de cada ramo, sem copiar um único conjunto de entalpias fornecidas.
- [ ] **CIC-03 — Restrições e sensibilidade do ciclo a vapor [P1; incluir].** Analisar pressão de condensação, pressão de caldeira, superaquecimento, umidade e eficiência dos equipamentos. **Aceite:** produzir curvas de desempenho com restrições, identificar região inviável e justificar uma escolha; ganho de rendimento não pode ocultar piora de outra exigência.
- [ ] **CIC-04 — Brayton ideal e real [P1; ampliar].** Determinar temperaturas e trabalhos com eficiências não ideais, perdas de pressão e calor específico variável. **Aceite:** comparar ciclos sob as mesmas condições de contorno e separar trabalho líquido, consumo do compressor, rendimento e potência para uma vazão especificada.
- [ ] **CIC-05 — Brayton modificado e otimização [P1; ampliar].** Quantificar regeneração com efetividade finita, resfriamento intermediário e reaquecimento. **Aceite:** calcular o ponto em que a regeneração deixa de ser útil e distinguir razão de pressões que maximiza trabalho da que otimiza outro objetivo, sob restrições declaradas.
- [ ] **CIC-06 — Otto, Diesel e ciclo misto [P1; ampliar].** Desenvolver estados, trabalho, calor, pressão média efetiva e efeitos de taxa de compressão/corte; contrastar hipóteses ar-padrão e processo real. **Aceite:** comparar ciclos com as mesmas restrições relevantes e demonstrar por que eficiência ideal isolada não permite ordenar motores reais.
- [ ] **CIC-07 — Ciclo combinado e cogeração [P1; ampliar].** Resolver a ligação energética entre turbina a gás, recuperação e ciclo a vapor; incluir demanda de calor útil e referências do desempenho. **Aceite:** fechar o conjunto, distinguir eletricidade de calor de processo e avaliar energia e exergia sem somar eficiências de subsistemas.
- [ ] **CIC-08 — Refrigeração real e bomba de calor [P1; ampliar].** Usar refrigerante com propriedades reais, eficiência do compressor, superaquecimento, sub-resfriamento e quedas de pressão. **Aceite:** determinar carga, vazão, potência, rejeição, COP e geração/destruição por componente, com comparação ao limite apropriado.
- [ ] **CIC-09 — Refrigeração em estágios [P1; incluir].** Desenvolver pelo menos um arranjo de dois estágios, com separador/inter-resfriamento ou cascata. **Aceite:** calcular estados e vazões de cada circuito, explicar o benefício e o custo termodinâmico e comparar com o ciclo simples sob serviço equivalente.
- [ ] **CIC-10 — Compressão politrópica e multietapas [P1; ampliar].** Derivar trabalho de escoamento, diferenciar expoente politrópico e eficiência politrópica, tratar resfriamento imperfeito e perdas. **Aceite:** demonstrar a média geométrica no caso ideal e resolver um caso em que ela deixa de ser ótima, documentando a busca do mínimo.
- [ ] **CIC-11 — Compressor alternativo e capacidade [P1; ampliar].** Relacionar volume morto, reexpansão, razão de pressões e eficiência volumétrica sob modelo definido; distinguir vazões reais e referidas. **Aceite:** calcular capacidade e potência sem confundir deslocamento, volume admitido e condições normalizadas.
- [ ] **CIC-12 — Vapor em instalações [P1; ampliar].** Integrar caldeira, separação, estrangulamento, vapor flash, retorno de condensado, purga e demanda térmica. **Aceite:** resolver uma rede simplificada com consumos e perdas especificados e avaliar recuperação de energia/exergia sem transformar o E1 em curso de projeto normativo de caldeiras.

### 5.7 Misturas e termodinâmica química

Base atual: quantidade de matéria, ar úmido, potencial químico, calorimetria e PCS/PCI. O desenvolvimento deve permitir aplicação consistente, sem supor que reconhecer uma definição resolve misturas reais ou combustão.

- [ ] **MIX-01 — Misturas de gases ideais [P1; ampliar].** Desenvolver frações molares/mássicas, massa molar, constantes da mistura, pressões parciais e propriedades energéticas. **Aceite:** converter bases e fechar massa/energia de mistura com composição explicitada e propriedades dependentes da temperatura.
- [ ] **MIX-02 — Entropia de mistura e separação [P1; incluir].** Quantificar mistura ideal, papel das pressões parciais e limite reversível de separação. **Aceite:** comparar mistura de espécies distintas com reunião de porções da mesma substância e explicar as hipóteses sem atribuir geração fictícia a rótulos diferentes do mesmo gás.
- [ ] **MIX-03 — Ar úmido como aplicação termodinâmica [P1; ampliar].** Trabalhar razão de umidade, ponto de orvalho, entalpia, mistura e condensação em balanços. **Aceite:** resolver um processo com remoção/adição de água e calor, com base em massa de ar seco e ligação ao A1 sem exigir alterações naquele módulo.
- [ ] **QUI-01 — Estequiometria e excesso de ar [P1; incluir].** Balancear reação, composição do combustível, ar teórico/real e produtos em bases seca/úmida. **Aceite:** conservar cada elemento, distinguir frações molares e mássicas e resolver ao menos um problema inverso a partir de composição dos gases.
- [ ] **QUI-02 — Entalpias de formação e balanço reativo [P1; ampliar].** Usar referências químicas, entalpia sensível, formação, estados físicos e PCS/PCI. **Aceite:** calcular calor/trabalho ou consumo de combustível com reação balanceada e não aplicar mudança arbitrária de referência de espécies sem contabilizar energia de reação.
- [ ] **QUI-03 — Temperatura adiabática de chama [P1; incluir].** Resolver um caso com composição de produtos prescrita, propriedades variáveis e método iterativo. **Aceite:** fechar energia, examinar excesso de ar/preaquecimento e declarar que o resultado sem dissociação é limitado pela hipótese de composição congelada.
- [ ] **QUI-04 — Equilíbrio químico básico [P1; ampliar].** Relacionar Gibbs, potencial químico, avanço e direção de reação; resolver ao menos uma reação simples com constante de equilíbrio adimensional e atividade/fugacidade aproximada explicitada. **Aceite:** determinar composição de equilíbrio com balanço de elementos e analisar efeito de temperatura/pressão; redes extensas e modelos não ideais ficam nas extensões.
- [ ] **QUI-05 — Exergia de combustíveis e perdas [P1; incluir].** Distinguir poder calorífico, exergia química e física, com ambiente e fonte dos valores de referência. **Aceite:** integrar uma análise de combustor/caldeira e explicar por que a qualidade da energia não é medida apenas pelo calor liberado.

## 6. Modelagem, cálculo e validação dos resultados

O objetivo de “contas sem calculadora” pode ser preservado na trilha de concurso, mas não deve impedir atividades avançadas com tabelas, planilhas e programação. A ferramenta precisa apoiar o raciocínio e tornar o cálculo reproduzível.

- [ ] **MOD-01 — Fechamento do modelo [P1; ampliar].** Ensinar contagem de incógnitas, equações independentes, dados de contorno e restrições físicas. **Aceite:** resolver um problema fechado e diagnosticar um subdeterminado e um superespecificado, sem inventar dados silenciosamente.
- [ ] **MOD-02 — Resolver sistemas e processos iterativos [P1; incluir].** Trabalhar raízes, sistemas não lineares e equações diferenciais necessários aos problemas selecionados. **Aceite:** justificar método, estimativa inicial, domínio, critério de parada e interpretação de falhas; convergência numérica não equivale a validade física.
- [ ] **MOD-03 — Ferramentas reproduzíveis [P1; incluir].** Fornecer planilhas ou scripts com entradas, unidades, fórmulas, documentação e versões de dependências. **Aceite:** uma pessoa consegue reproduzir os resultados de uma instalação limpa ou por instruções completas, sem caminhos particulares ou arquivos não entregues.
- [ ] **MOD-04 — Verificação independente [P1; incluir].** Comparar resultados por balanços globais, cálculo manual em caso reduzido, tabela ou segunda implementação adequada. **Aceite:** os casos de referência detectam erro de unidade, sinal, fase e troca de propriedades; não usar a própria fórmula defeituosa como único oráculo do teste.
- [ ] **MOD-05 — Tolerâncias e arredondamento [P1; incluir].** Definir precisão dos dados, arredondamento intermediário e tolerância de comparação. **Aceite:** cada solução informa o que vem de aproximação física, interpolação, arredondamento ou solver; resíduos são avaliados com escala definida, inclusive perto de zero.
- [ ] **MOD-06 — Sensibilidade e otimização [P1; incluir].** Variar parâmetros relevantes, escolher objetivo e impor restrições, distinguindo máximo local e domínio viável. **Aceite:** apresentar curvas e justificar a solução escolhida, conferir extremos/limites e documentar o custo de uma melhoria em outra métrica.
- [ ] **MOD-07 — Incerteza de dados [P1; incluir].** Separar incerteza de medição, variabilidade operacional, aproximação do modelo e erro numérico. **Aceite:** propagar incertezas por método adequado ao caso e avaliar se a diferença entre duas propostas é significativa frente à incerteza dos dados.
- [ ] **MOD-08 — Estudo com dados de operação [P1; incluir].** Incorporar um conjunto de dados experimentais públicos ou fornecidos e rastreáveis; dados sintéticos devem ser identificados. **Aceite:** estimar desempenho, apresentar resíduos e limitações e confrontar o modelo com os dados; um caso sintético não comprova validação experimental.
- [ ] **MOD-09 — Uso crítico de software e assistência automática [P2; incluir].** Exigir registro de ferramenta, hipótese e verificações quando houver solver, biblioteca ou assistência automática. **Aceite:** o aluno explica a solução e corrige uma perturbação do problema; a evidência de domínio não se reduz à saída de uma ferramenta.

## 7. Arquitetura didática e aprendizagem independente

O módulo já possui explicações de símbolos, exemplos, mapas “Estudar a base”, oficina e diagnósticos. O desenvolvimento deve transformar esse apoio em progressão mensurável de autonomia.

- [ ] **DID-01 — Objetivos por unidade [P1; ampliar].** Substituir objetivos genéricos por ações observáveis: derivar, determinar estado, modelar, comparar, validar e justificar. **Aceite:** cada objetivo é ensinado e cobrado em nível cognitivo compatível; “conhecer exergia” não encerra o requisito.
- [ ] **DID-02 — Retirada gradual de ajuda [P1; ampliar].** Organizar exemplo completo, exercício com pistas, solução parcialmente preenchida e problema independente. **Aceite:** os últimos problemas não fornecem automaticamente a equação decisiva, o modelo de substância ou todas as propriedades intermediárias.
- [ ] **DID-03 — Transferência entre contextos [P1; ampliar].** Variar fronteira, regime, pergunta, hipótese, tipo de dado e configuração, além de números. **Aceite:** uma família de treino contém situações em que a relação habitual deixa de ser aplicável e o aluno precisa escolher outra abordagem.
- [ ] **DID-04 — Concepções equivocadas [P1; ampliar].** Mapear erros de conceito: calor armazenado, adiabático igual a isentrópico, entropia sempre crescente em qualquer parte, COP como eficiência de conversão, título fora da região bifásica e estado igual a caminho. **Aceite:** cada erro possui diagnóstico, explicação causal, contraexemplo e nova tentativa independente.
- [ ] **DID-05 — Diagnósticos com decisão de estudo [P1; ampliar].** Preservar os 28 existentes e acrescentar os necessários às novas competências, com rubrica e encaminhamento específico. **Aceite:** o aluno sabe qual evidência precisa produzir para seguir, e uma resposta vista na resolução não é registrada como domínio autônomo.
- [ ] **DID-06 — Retenção e prática cumulativa [P1; incluir].** Distribuir revisões ao longo do percurso e misturar assuntos sem indicar previamente a fórmula. **Aceite:** incluir uma tarefa retardada após intervalo de estudo, com variante inédita, para diferenciar retenção de repetição imediata.
- [ ] **DID-07 — Feedback de raciocínio [P1; ampliar].** Explicar decisões, erros de modelagem, unidades e consistência, não apenas a alternativa correta. **Aceite:** um erro relevante encaminha para a lacuna correspondente e permite refazer por nova situação, sem induzir mera memorização da letra.
- [ ] **DID-08 — Carga cognitiva e navegação [P2; ampliar].** Organizar o conteúdo extenso em unidades localizáveis, com resumo, pré-requisitos e ponto de continuidade. **Aceite:** o aluno encontra a trilha avançada, retoma o estudo e distingue conteúdo obrigatório de apoio sem percorrer uma página inteira à procura do tópico.
- [ ] **DID-09 — Problemas abertos e dados insuficientes [P1; incluir].** Incluir julgamento de propostas, escolha de medições e identificação de ambiguidade legítima. **Aceite:** rubricas aceitam hipóteses alternativas justificadas e não punem a identificação correta de que os dados não determinam uma resposta única.
- [ ] **DID-10 — Solução como comunicação técnica [P1; incluir].** Exigir fronteira desenhada, hipóteses, fonte das propriedades, equações, cálculo e interpretação. **Aceite:** uma terceira pessoa pode reconstruir a solução; números sem unidade ou resultado sem modelo não recebem crédito integral.

## 8. Banco de questões: correção, cobertura e dificuldade

**Dados confirmados por inspeção estática:** 190 itens fechados. No banco real, 73 são Certo/Errado e 7 têm cinco alternativas; somando os bancos, há 117 questões de cinco alternativas. Os dois bancos de 80 itens compartilham distribuição temática: 12 fundamentos, 13 gases, 11 energia, 10 segunda lei, 19 ciclos e 15 aplicações. Essa classificação do material não equivale a uma classificação de dificuldade.

- [x] **BAN-01 — Corrigir o padrão de gabarito [P0; corrigir].** Reorganizar as alternativas das 30 questões iniciais e atualizar gabarito, comentário e referências à letra conjuntamente. **Aceite:** eliminar a sequência ABCDE repetida, manter resposta única correta e verificar cada item após a alteração; não criar outra sequência sistemática como substituta. **Aceito em 27/10/2026 após duas rodadas:** [parecer BAN-01-r2](auditoria/termodinamica/pareceres/BAN-01-r2.md), com hashes e evidências independentes. As ambiguidades de Q10/Q12 identificadas na rodada 1 foram corrigidas antes do aceite. A aprovação é deste item e da versão examinada, não do curso inteiro.
- [x] **BAN-02 — Inventariar todos os itens [P1; ampliar].** Criar registro por ID com competência, pré-requisitos, origem, formato, nível, raciocínio requerido, número de etapas, hipóteses e exposição prévia. **Aceite:** os 190 itens atuais estão classificados individualmente e os novos entram no mesmo registro; nível não é inferido só pelo título do assunto. **Aceito em 27/10/2026:** [parecer BAN-02-r3](auditoria/termodinamica/pareceres/BAN-02-r3.md). Registro individual aprovado; não certifica gabaritos, fontes oficiais nem domínio avançado.
- [ ] **BAN-03 — Separar fixação de avaliação [P1; corrigir].** Manter repetições úteis no treino, mas excluí-las da evidência de domínio independente. Incluir `q-e1-26`, `q-e1-27`, `q-e1-29` e as correspondências entre bancos nessa revisão. **Aceite:** cada avaliação final usa famílias realmente inéditas, sem reutilizar o mesmo enunciado ou apenas trocar números de um exemplo imediatamente disponível.
- [ ] **BAN-04 — Auditar duplicação e quase duplicação [P1; verificar].** Comparar pares entre CR/AV e os exemplos: `av-e1-28` reutiliza dados de `cr-e1-28`, e `av-e1-25` repete a transformação do item correspondente. **Aceite:** marcar a relação pedagógica, distinguir reformulação de novo desafio e impedir que contagens duplicadas inflem a cobertura declarada.
- [ ] **BAN-05 — Classificar a complexidade real [P1; incluir].** Usar reconhecimento, aplicação direta, integração de etapas e modelagem/julgamento como categorias distintas. **Aceite:** avaliação por dois leitores ou revisão independente de casos limítrofes; não considerar uma questão avançada apenas porque cita Gibbs, entropia ou exergia.
- [ ] **BAN-06 — Corrigir lacunas de cobertura [P1; incluir].** Acrescentar problemas de propriedades reais, transientes completos, exergia, ciclos com estados desconhecidos, misturas, combustão e incerteza. **Aceite:** matriz C01–C10 coberta por problemas independentes e integrados; nenhuma dessas competências depende somente de uma pergunta conceitual fechada.
- [x] **BAN-07 — Enunciados e alternativas [P0; verificar].** Conferir dados suficientes, consistência física, comando, unidades, restrições e resposta única, incluindo distratores plausíveis baseados em erros reais. **Aceite:** cada item tem demonstração do gabarito e justificativa dos distratores; detectar alternativas equivalentes após arredondamento. **Aceito em 29/10/2026 na rodada 3:** [parecer BAN-07-r3](auditoria/termodinamica/pareceres/BAN-07-r3.md). Revisão de 197 itens e seis ajustes; aceite restrito à versão examinada, sem encerrar BAN-08 ou classificar o curso como avançado. **Revalidado em 29/10/2026:** após ajustes em AV42, AV45 e AV52, [parecer localizado](auditoria/termodinamica/pareceres/BAN-07-revalidacao-av42-av45-av52-r1-independente.md). BAN-08 permanece em andamento.
- [x] **BAN-08 — Auditoria numérica integral [P0; verificar].** Recalcular todas as 190 resoluções atuais e todas as futuras, com precisão compatível. **Aceite:** planilha/registro por ID com solução, resultado, tolerância, fonte e revisor; nenhuma aceitação por amostragem no fechamento final. **Aceito em 29/10/2026:** [parecer BAN-08-r1](auditoria/termodinamica/pareceres/BAN-08-r1.md), cobrindo 197 itens na versão examinada, com revisão atribuída por ID. Não encerra QA-09 nem classifica o curso inteiro.
- [ ] **BAN-09 — Uso avaliativo de figuras [P1; ampliar].** Verificar se a figura contém informação necessária ou é apenas ilustração; revisar escalas, dimensões, legenda e correspondência com a solução. **Aceite:** declarar o papel da figura e oferecer alternativa acessível equivalente; não contabilizar como interpretação gráfica um cálculo que independe do gráfico.
- [x] **BAN-10 — Ambiguidades e gabarito oficial [P0; verificar].** Rever em especial CR-09, CR-24, CR-68 e CR-79, que já possuem ressalvas, e pesquisar outros casos durante a conferência. **Aceite:** distinguir texto oficial, gabarito oficial, interpretação técnica e dado suplementar; retirar da nota de domínio ou reformular como estudo crítico quando a ambiguidade impedir medida válida. **Aceito em 28/10/2026 após duas rodadas:** [parecer BAN-10-r2](auditoria/termodinamica/pareceres/BAN-10-r2.md). Triagem de 197 itens, 12 decisões e nove estudos fora da pontuação; CR34 esclarece modelos sem invalidar a chave oficial. Aprovação restrita ao ID e à versão examinada.
- [ ] **BAN-11 — Problemas discursivos e rubricas [P1; incluir].** Acrescentar soluções abertas com crédito por modelagem, desenvolvimento, propriedades e interpretação, inclusive múltiplas rotas válidas. **Aceite:** rubrica distingue erro conceitual, erro numérico propagado e arredondamento; não desconta repetidamente o mesmo erro consequente sem justificativa.
- [ ] **BAN-12 — Metadados de tentativa [P2; incluir].** Distinguir primeira tentativa, tentativa com pista, consulta à resolução e repetição. **Aceite:** indicadores de aprendizagem não confundem a última resposta correta após consulta com acerto independente.
- [ ] **BAN-13 — Banco reservado de avaliação [P1; incluir].** Manter versões inéditas ou gerar variantes com validação física e dificuldade comparável. **Aceite:** não liberar a solução antes da entrega quando o instrumento for avaliativo; em site estático, declarar os limites de sigilo e usar correção/revisão externa quando se pretender comprovação formal.
- [ ] **BAN-14 — Análise após uso [P2; incluir].** Observar taxa de acerto, uso de distratores, tempo, omissões e relação com desempenho geral em amostra adequada. **Aceite:** registrar número/perfil de participantes e incerteza das conclusões; sem piloto, rotular dificuldade como estimada, nunca empiricamente validada.

## 9. Projetos integradores obrigatórios

Os projetos abaixo são requisitos deste plano interno. Não é necessário transformar cada projeto em um software ou instalação real. É necessário fornecer dados suficientes e rastreáveis, solução de referência, variantes de avaliação e rubrica. Nenhum projeto exige manipular equipamento pressurizado, combustível ou refrigerante: podem ser realizados com dados e modelos.

### 9.1 Padrão de entrega de todos os projetos

Cada projeto deve conter: enunciado e objetivo; diagrama e fronteira; dados e fontes; lista de incógnitas; hipóteses justificadas; tabela de estados; balanços e solução; verificação física; análise de sensibilidade; limitações; recomendação final; anexos reproduzíveis. Quando entropia ou exergia não forem pertinentes a uma parcela, justificar o recorte em vez de inventar métricas.

- [ ] **PRJ-01 — Central a vapor com extração [P1; incluir].** Comparar Rankine simples, reaquecido e regenerativo com demanda de potência e limite de umidade. **Aceite:** determinar estados reais, frações/vazões, consumo, energia e exergia por componente e explicar a escolha sob restrições; ao menos uma variante deve alterar uma condição essencial.
- [ ] **PRJ-02 — Instalação de ar comprimido [P1; incluir].** Comparar compressão em um/dois estágios, resfriamento, perdas de pressão e consumo para uma demanda equivalente. **Aceite:** tratar vazão de referência, pressão absoluta, trabalho, calor rejeitado, temperaturas e exergia; encontrar a pressão intermediária apropriada ao caso, sem impor sempre a média geométrica.
- [ ] **PRJ-03 — Refrigeração e bomba de calor [P1; incluir].** Atender uma carga especificada com refrigerante e limites operacionais, comparando dois arranjos. **Aceite:** determinar estados em `p–h`/`T–s`, vazão, COP, potências, irreversibilidades e sensibilidade às temperaturas; seleção normativa/comercial de equipamento não substitui a análise termodinâmica.
- [ ] **PRJ-04 — Sistema transiente [P1; incluir].** Resolver tanque com carga ou descarga, massa inicial, parede e troca térmica especificadas. **Aceite:** calcular evolução de massa/estado, eventos e tempo, confrontar caso-limite analítico e verificar massa, energia e entropia ao longo da simulação.
- [ ] **PRJ-05 — Caldeira/combustor e aproveitamento térmico [P1; incluir].** Combinar composição de combustível, excesso de ar, energia de reação e recuperação de calor. **Aceite:** conservar elementos e energia, declarar PCS/PCI, analisar gases de saída e exergia, quantificar efeito de uma melhoria e reconhecer limites do modelo de combustão.
- [ ] **PRJ-06 — Cogeração ou ciclo combinado [P1; incluir].** Comparar produção separada de eletricidade/calor com uma configuração integrada para as mesmas demandas. **Aceite:** declarar bases de comparação, resolver o acoplamento e não equiparar automaticamente calor de baixa temperatura a eletricidade.
- [ ] **PRJ-07 — Auditoria de uma proposta defeituosa [P1; incluir].** Fornecer relatório com erros selecionados de unidade, estado, hipótese e segunda lei. **Aceite:** localizar erros, demonstrar efeitos, reconstruir solução consistente e apontar dados que não podem ser recuperados; a rubrica não entrega previamente a localização dos defeitos.
- [ ] **PRJ-08 — Investigação com dados [P1; incluir].** Confrontar modelo de turbina, compressor, aquecimento ou refrigeração com dados experimentais rastreáveis. **Aceite:** ajustar apenas parâmetros identificáveis, apresentar incerteza, resíduos e validade externa; se só houver dados sintéticos, manter pendente a comprovação com observações reais.

## 10. Avaliação e comprovação de domínio avançado

### 10.1 Instrumentos necessários

- [ ] **AVA-01 — Diagnóstico de entrada [P1; ampliar].** Separar deficiências matemáticas de lacunas termodinâmicas e indicar recuperação. **Aceite:** instrumento e rubrica completos, sem usar uma nota global para esconder uma lacuna fundamental.
- [ ] **AVA-02 — Avaliações intermediárias [P1; incluir].** Aplicar tarefas sem roteiro após propriedades, leis, exergia e ciclos, misturando competências anteriores. **Aceite:** cada bloco demonstra retenção e transferência, com tentativa inédita após recuperação quando necessária.
- [ ] **AVA-03 — Prova final integrada [P1; incluir].** Criar avaliação com problemas abertos, dados de propriedades e julgamento de viabilidade. **Aceite:** ao menos 60% dos pontos exigem integração/modelagem/julgamento, ao menos 50% são atribuídos a desenvolvimento aberto e no máximo 20% a reconhecimento ou substituição direta; critérios internos, sujeitos a revisão justificada após piloto.
- [ ] **AVA-04 — Defesa de solução [P1; incluir].** Solicitar explicação oral ou escrita orientada por uma perturbação inédita de um projeto. **Aceite:** o aluno justifica hipóteses e prevê/recalcula o efeito de alterar uma condição; não basta apresentar um arquivo concluído.
- [ ] **AVA-05 — Recuperação e nova evidência [P1; incluir].** Vincular cada falha a estudo e prática específicos, com nova tarefa de dificuldade comparável. **Aceite:** domínio só muda após nova evidência independente; não exigir repetir o curso inteiro por uma única competência deficitária.
- [ ] **AVA-06 — Rubrica e decisão de aprovação [P1; incluir].** Publicar critérios de desempenho por competência e exemplos de respostas em diferentes níveis. **Aceite:** outro avaliador consegue aplicar a rubrica e divergências são discutidas/documentadas antes da classificação final.
- [ ] **AVA-07 — Piloto e calibração [P2; incluir].** Preparar aplicação com participantes compatíveis com o público para testar instruções, carga, ambiguidades e dificuldade. **Aceite:** em duas etapas registradas separadamente: (a) protocolo, instrumentos, perfil de participantes e plano de análise prontos e revisados; (b) aplicação real, resultados, alterações e limitações da amostra documentados. A etapa (a) é obrigatória para aceitar a estrutura do curso; a etapa (b) é obrigatória para alegar resultados de aprendizagem medidos. Sem participantes, manter a validação empírica pendente, sem inventar resultados nem impedir a avaliação científica da estrutura.

### 10.2 Rubrica proposta para tarefas integradoras

| Dimensão | Peso de referência | Evidência |
|---|---:|---|
| Fronteira, hipóteses e fechamento do modelo | 20% | Escolhas físicas explícitas e justificadas |
| Estados, propriedades e fontes | 15% | Região correta, unidades, referência e obtenção reproduzível |
| Balanços e desenvolvimento | 25% | Equações consistentes e solução das relações necessárias |
| Verificações e limites físicos | 20% | Massa/energia, segunda lei, resíduos e teste de plausibilidade |
| Sensibilidade, decisão e comunicação | 20% | Comparação coerente, limitações e argumento técnico |

Adaptar pesos ao objetivo de cada tarefa antes de aplicá-la. Não atribuir pontos a exergia, por exemplo, se o enunciado não oferece os dados para avaliá-la.

**Regra interna proposta:** alcançar pelo menos 80% no conjunto das evidências finais, pelo menos 70% em cada competência C01–C10 e aceitação das entregas integradoras obrigatórias. Atingir média não compensa erro conceitual crítico não corrigido. Erro crítico é aquele que invalida o modelo, como afirmar domínio usando temperatura Celsius em razão de Carnot, título fora da região bifásica, massa não conservada ou geração negativa de entropia aceita sem diagnóstico. Deve gerar recuperação e nova evidência na competência afetada, não uma punição ilimitada por um lapso de escrita isolado.

Para cada competência, exigir pelo menos duas evidências independentes de solução autônoma, uma delas de transferência para uma configuração nova. Evidências podem vir de provas, projetos ou defesa, sem criar duas atividades artificiais por tópico. A matriz deve mostrar onde cada demonstração ocorre. Permitir consulta quando ela fizer parte da tarefa; domínio avançado não exige memorizar todas as propriedades ou expressões.

O material pode ser considerado **estruturado para nível avançado** depois da revisão e dos critérios de entrega. Afirmar que **um aluno domina nível avançado** exige suas evidências de desempenho. Afirmar que **o curso comprovou resultados de aprendizagem** exige aplicação e análise de resultados; são três afirmações diferentes.

## 11. Formulário, diagramas e materiais de consulta

- [x] **FOR-01 — Auditoria das 100 fichas atuais [P0; verificar].** Conferir expressão, símbolos, unidades, hipóteses e ligação com a aula de cada ficha. **Aceite:** registro individual de revisão; fórmulas de balanço geral não podem ser apresentadas como simplificações universais. **Aceito em 28/10/2026 após duas rodadas:** [parecer FOR-01-r2](auditoria/termodinamica/pareceres/FOR-01-r2.md). Revisão individual das 100 fichas, hipóteses e 50 destinos conferidos; 191 elementos MathML preservados. R1-A sobre trabalho não associado ao escoamento foi corrigido e reauditado. Aceite restrito às fichas existentes; cobertura avançada adicional e QA-09 continuam abertos.
- [ ] **FOR-02 — Cobertura do núcleo avançado [P1; ampliar].** Acrescentar relações necessárias a propriedades reais, exergia, transientes, misturas e reações, somente após desenvolver a base. **Aceite:** toda fórmula nova aparece em explicação e uso validado, com limites e origem; quantidade de fichas não é meta de nível.
- [ ] **FOR-03 — Notação sem conflitos [P2; ampliar].** Harmonizar velocidade/volume, expoente politrópico/quantidade de matéria, título/fração extraída, razão de calores/condutividade e taxa/quantidade. **Aceite:** cada símbolo ambíguo é definido localmente e não muda silenciosamente dentro do mesmo problema.
- [ ] **FOR-04 — Diagramas e tabelas de apoio [P1; ampliar].** Entregar dados suficientes para resolução independente, com fonte, unidades, faixa e referência. **Aceite:** uma avaliação pode ser feita sem buscar propriedades não especificadas em uma fonte externa inacessível; esquema didático não é confundido com dado medido.
- [ ] **FOR-05 — Uso e derivação [P1; ampliar].** Ligar cada família de relações à sua derivação, forma geral, casos particulares e exemplo de uso indevido. **Aceite:** o aluno consegue selecionar uma expressão com base em condições físicas, sem depender somente de reconhecimento visual de fórmula.
- [ ] **FOR-06 — Sincronização entre materiais [P2; incluir].** Definir fonte de verdade para aula, formulário, resumo, flashcards, questões e dados auxiliares. **Aceite:** uma correção se propaga aos locais afetados e nenhum resumo conserva hipótese ou sinal já corrigido na aula.

## 12. Fontes, gabaritos e rastreabilidade científica

- [x] **FON-01 — Conferir cada questão oficial [P0; verificar].** Comparar enunciado, alternativas, figuras, cargo, tipo/cor, número, data e gabarito definitivo contra os arquivos de origem. **Aceite:** 80 registros com página e identificação inequívocas, inclusive eventuais anulações/retificações; existência do PDF não equivale à conferência do item. **Aceito em 28/10/2026 na rodada 1:** [parecer FON-01-r1](auditoria/termodinamica/pareceres/FON-01-r1.md).80 comparações individuais e fontes/atos pertinentes conferidos; referências CAESB atual e histórica diferenciadas. Aceite documental, sem encerrar FON-02, BAN-07/BAN-08 ou a classificação global.
- [x] **FON-02 — Rastrear dados suplementares [P0; verificar].** Identificar cada constante, propriedade ou hipótese acrescentada a um enunciado original. **Aceite:** suplemento separado e justificado, sem apresentar a versão enriquecida como transcrição literal da prova. **Aceito em 28/10/2026 após duas rodadas:** [parecer FON-02-r2](auditoria/termodinamica/pareceres/FON-02-r2.md). Suplementos dos 80 CR identificados e justificados; 21 esclarecimentos e 71 resumos de autoria, com transcrições/chaves preservadas. R1-A documental corrigido: 80 listas e 158 vínculos fiéis. Sem encerrar BAN-07/BAN-08, FON-03/FON-10 ou o aceite global.
- [ ] **FON-03 — Fontes de propriedades [P1; ampliar].** Registrar substância, composição, região, fonte, versão, referência energética e unidades de cada conjunto. **Aceite:** estados usados nos projetos podem ser reconstruídos por quem não participou da autoria.
- [ ] **FON-04 — Dados didáticos e dados físicos [P1; ampliar].** Preservar os exemplos simplificados identificados como didáticos, adicionando casos realistas consistentes. **Aceite:** não usar entalpias inventadas como prova de viabilidade física de um ciclo sem confirmar pressão, temperatura, fase e segunda lei.
- [ ] **FON-05 — Evidência junto à afirmação [P2; ampliar].** Associar conceitos sensíveis, fórmulas e dados à seção/página de referência apropriada. **Aceite:** bibliografia não funciona apenas como lista genérica ao final; cada afirmação que depende de fonte especializada é localizável.
- [ ] **FON-06 — Proveniência e permissão de uso [P2; verificar].** Manter autoria, origem, licença e condições de reprodução de textos, imagens, PDFs, tabelas e software. **Aceite:** material original, transcrito, adaptado e recriado identificado; não pressupor que acesso público concede qualquer forma de reutilização.
- [ ] **FON-07 — Versões, erratas e histórico [P2; incluir].** Registrar mudanças científicas, itens corrigidos, impactos em notas e versões dos dados. **Aceite:** um aluno consegue saber se estudou uma resolução substituída e encontrar a correção com o mesmo ID.
- [ ] **FON-08 — Revisão científica independente [P1; incluir].** Submeter as novas unidades e problemas a revisor tecnicamente qualificado, com escopo e parecer registrados. **Aceite:** resolver observações bloqueadoras, manter justificativa das decisões e não confundir uma segunda execução do mesmo gerador com revisão independente.
- [x] **FON-09 — Tratar os dados defeituosos associados ao CR-68 [P0; verificar/corrigir].** A nota atual já alerta sobre densidade escrita como `1.000 kg/cm³` e tabela de saturação inconsistente no material fornecido. **Aceite:** conferir a origem exata de cada erro, manter transcrição identificada quando necessário e oferecer dados corrigidos rastreáveis; não reutilizar a tabela defeituosa. O enunciado sobre emissividade não depende desses dados, portanto a correção não implica automaticamente mudar seu gabarito oficial. **Aceito em 27/10/2026 após duas rodadas:** [parecer FON-09-r2](auditoria/termodinamica/pareceres/FON-09-r2.md). Origem oficial e todas as 15 células conferidas; dados corrigidos rastreáveis publicados, transcrição histórica separada e gabarito preservado. A dependência técnica do validador foi corrigida e reauditada. O aceite não encerra FON-01, BAN-10, BAN-08 ou QA-04 globais.
- [ ] **FON-10 — Expor as cópias locais dos documentos [P2; ampliar].** Os links “Prova original”/“Gabarito definitivo” do E1 são externos; a leitura estática não localizou links do módulo para os 24 arquivos em `downloads/termodinamica/`. **Aceite:** oferecer catálogo e acesso local por questão, com página correta, mantendo também a fonte oficial; a conferência dos documentos deve funcionar offline.

## 13. Experiência de estudo, acessibilidade e persistência

Estas tarefas sustentam a utilização do curso. Não substituem profundidade científica. A inspeção estática atual não comprova funcionamento em navegador ou acessibilidade assistiva.

- [ ] **UX-01 — Navegação do E1 [P2; ampliar].** Dar acesso direto a unidades, projetos, propriedades, avaliações e progresso por competência, mantendo âncoras estáveis. **Aceite:** percursos funcionam por teclado e links diretos; não é obrigatório dividir a página se uma organização equivalente resolver o problema.
- [ ] **UX-02 — Matemática acessível [P2; verificar].** Validar leitura de MathML, frações, índices, integrais, somatórios e unidades, com alternativas textuais quando necessárias. **Aceite:** testar em combinações de navegador/leitor de tela documentadas; presença de marcação semântica sozinha não encerra a verificação.
- [ ] **UX-03 — Teclado, contraste e adaptação de tela [P2; verificar].** Examinar foco, ordem de navegação, controles de respostas, temas, zoom e tabelas extensas. **Aceite:** resolver atividades e consultar comentários sem mouse, sem perda de informação por cor e sem corte de conteúdo em telas pequenas ou ampliação.
- [ ] **UX-04 — Figuras, dados alternativos e impressão [P2; ampliar].** Disponibilizar descrições equivalentes e tabelas quando a leitura visual carrega dados do problema; preparar impressão/exportação útil. **Aceite:** a alternativa acessível preserva a tarefa intelectual sem revelar a resposta, e a versão impressa inclui as propriedades e hipóteses necessárias.
- [ ] **UX-05 — Separar andamento de domínio [P1; ampliar].** Diferenciar leitura/conclusão, acerto em treino, consulta de resolução e competência demonstrada. **Aceite:** concluir leitura de uma seção não concede automaticamente a classificação avançada nem oculta lacunas em entropia/exergia.
- [ ] **UX-06 — Backup completo de Termodinâmica [P2; ampliar].** Integrar ou oferecer exportação própria de todos os dados do E1, com identificação de versão e sem depender dos outros módulos. **Aceite:** ida e volta de exportação/importação preserva respostas, marcações e progresso do E1, inclusive bancos adicionais, e trata dados incompatíveis com mensagem clara.
- [ ] **UX-07 — Falhas de armazenamento e migração [P2; verificar].** Tratar indisponibilidade, dados corrompidos, limites e mudanças de esquema. **Aceite:** testes em cópia de dados demonstram recuperação ou aviso compreensível, sem zerar progresso silenciosamente nem sobrescrever dados válidos por uma importação inválida.
- [ ] **UX-08 — Uso offline e caminhos locais [P2; verificar].** Conferir aula, formulário, figuras, PDFs e dados de apoio no modo offline prometido pelo curso e também via servidor local. **Aceite:** recursos essenciais funcionam nos dois cenários declarados; dependências externas e limitações do armazenamento por origem são informadas de modo claro.
- [ ] **UX-09 — Estado de tentativa e feedback [P2; verificar].** Testar marcar, conferir, refazer, filtrar e voltar à página em todos os formatos usados no E1. **Aceite:** resultado exibido corresponde ao item e tentativa certos; mudanças de filtro/navegação não contam como resposta nem apagam dados sem ação explícita.
- [ ] **UX-10 — Desempenho e robustez [P2; verificar].** Avaliar carregamento e interação da aula extensa, fórmulas e bancos nos dispositivos-alvo, registrando medidas. **Aceite:** definir limites após medir a versão atual e corrigir travamentos/atrasos relevantes; não impor uma arquitetura nova sem demonstrar necessidade.
- [ ] **UX-11 — Correções e validade do progresso [P2; incluir].** Distinguir alteração editorial de mudança científica em enunciado, dado visual, hipótese, solução ou gabarito. **Aceite:** registrar versão e sinalizar/reavaliar as evidências afetadas; mudança de bytes da figura ou da resolução não pode passar despercebida só porque seu endereço e o texto do enunciado permaneceram iguais.
- [ ] **UX-12 — Conteúdo com JavaScript indisponível [P2; verificar].** Garantir acesso à teoria, dados, enunciados e soluções pela forma de uso declarada, mantendo explicação dos recursos interativos indisponíveis. **Aceite:** testar leitura e consulta sem JavaScript; a indisponibilidade de um placar não deve ocultar o conteúdo necessário ao estudo.

**Constatação específica de armazenamento:** a leitura de `assets/curso.js` identifica prefixo geral `sopmec:v2:` e chaves separadas `sopmec:concursos:v2:e1` e `sopmec:avalia:v2:e1`. A exportação geral filtra o primeiro prefixo. O README já documenta essa separação; portanto, o backup completo é uma melhoria de continuidade, e não uma regressão oculta descoberta agora. A correção precisa ser verificada por restauração real de uma cópia de teste.

**Constatação sobre versionamento dos bancos:** `digitalDoBanco` considera texto, alternativas, gabarito e endereço/descrição de imagens. A leitura estática não encontrou inclusão dos bytes das imagens, de todas as notas de leitura ou da resolução nessa identificação. Isso exige uma política explícita de mudança científica (UX-11); não demonstra, por si só, perda de progresso reproduzida em navegador.

## 14. Garantia de qualidade e manutenção

- [ ] **QA-01 — Recuperar o processo de autoria [P2; verificar].** Identificar scripts e fontes usados para gerar registro, metadados e validações, ou documentar uma substituição reproduzível. **Aceite:** o E1 pode ser reconstruído e validado sem depender de ferramentas ausentes nesta entrega; o README declara que o repositório publicado exclui ferramentas internas, portanto essa ausência não prova defeito no pacote do aluno.
- [ ] **QA-02 — Revisão científica por unidade [P0; verificar].** Conferir definições, domínios, sinais, dimensionalidade, hipóteses e consistência entre exemplos e teoria. **Aceite:** todas as unidades do núcleo têm registro de revisão e nenhuma observação científica bloqueadora permanece aberta.
- [ ] **QA-03 — Casos numéricos de referência [P1; incluir].** Criar testes significativos para novos cálculos e bibliotecas: estados limite, saturação, gás ideal, processos reversíveis e balanços. **Aceite:** detectar erros que alteram o resultado de aprendizagem; evitar testes que apenas reproduzem a própria implementação ou validam texto decorativo.
- [ ] **QA-04 — Links e integridade de recursos [P2; verificar].** Verificar âncoras, IDs únicos, referências entre questão/aula/fórmula, arquivos e hashes dos documentos locais. **Aceite:** nenhum recurso essencial do E1 quebrado; falhas de fontes externas são registradas com alternativa rastreável, sem inventar conteúdo substituto.
- [ ] **QA-05 — Regressão funcional do E1 [P2; verificar].** Validar questões, placares, filtros, formulário, temas, retomada e backup após mudanças. **Aceite:** roteiro reproduzível cobre operações reais do aluno e estados de erro, com resultado registrado por versão.
- [ ] **QA-06 — Isolamento em arquivos compartilhados [P2; verificar].** Documentar alterações compartilhadas estritamente necessárias ao E1 e testar que não alteram dados/comportamento dos demais módulos. **Aceite:** nenhuma mudança curricular fora de Termodinâmica; ampliar testes somente quando o alcance técnico da alteração justificar.
- [ ] **QA-07 — Publicação e manifesto [P2; incluir].** Definir quais artefatos são do aluno e quais são internos; atualizar `PUBLICACAO.json` apenas na preparação de uma nova entrega coerente. **Aceite:** manifesto corresponde aos arquivos efetivamente publicados, com inventário e hash corretos; esta auditoria interna não é apresentada como aula por acidente.
- [ ] **QA-08 — Registro de pendências e revisão de classificação [P1; incluir].** Manter o estado dos IDs desta auditoria com evidências, dependências e bloqueios. **Aceite:** a decisão de elevar o nível resulta da matriz e das entregas aceitas; nenhum item é encerrado apenas porque aumentou o volume do curso.
- [ ] **QA-09 — Recalcular todo o conteúdo numérico [P0; verificar].** Além dos 190 itens de BAN-08, inventariar e recalcular exemplos resolvidos, oficinas, 28 diagnósticos, valores das fichas e novos projetos. **Aceite:** cada ocorrência possui referência verificável e resultado conferido, incluindo cálculos apresentados em figuras e explicações textuais; nenhuma classe de atividade fica fora por não ser chamada de “questão”.

## 15. Extensões de especialização e condições para incluí-las

Estes itens têm prioridade **E**. Sua ausência não bloqueia o título delimitado de graduação avançada adotado nesta auditoria. Se forem anunciados como parte do curso, passam a exigir o mesmo padrão de teoria, prática, avaliação e revisão. Não devem ser usados para substituir lacunas do núcleo.

- [ ] **ESP-01 — Misturas não ideais e equilíbrio multifásico [E; incluir se prometido].** Fugacidade, coeficientes de atividade, Raoult/Henry como limites, azeotropia, diagramas de equilíbrio e cálculo flash. **Aceite:** resolver caso multicomponente com balanços, critério de equilíbrio, seleção de fases e comparação com dados; declarar limites do modelo.
- [ ] **ESP-02 — Termodinâmica estatística [E; incluir se prometido].** Microestados, ensembles selecionados, funções de partição e conexão com propriedades macroscópicas. **Aceite:** derivar uma propriedade e confrontar o limite clássico; não tratar uma frase sobre desordem como desenvolvimento estatístico.
- [ ] **ESP-03 — Não equilíbrio e transporte acoplado [E; incluir se prometido].** Equilíbrio local, produção de entropia, forças/fluxos e relações de reciprocidade no domínio aplicável. **Aceite:** modelo com hipóteses explícitas e verificação de produção de entropia; cinética e leis de transporte não são deduzidas apenas da primeira lei.
- [ ] **ESP-04 — Combustão e química avançadas [E; incluir se prometido].** Equilíbrio com várias reações, dissociação, cinética, efeitos de residência e limites de formação de poluentes. **Aceite:** distinguir equilíbrio de taxa de reação, conservar elementos e validar modelo/dados antes de extrapolar resultados.
- [ ] **ESP-05 — Refrigeração por absorção, ejetores e criogenia [E; incluir se prometido].** Soluções, separação, liquefação e ciclos próprios, com composição e exergia. **Aceite:** estados e balanços completos por circuito, sem aplicar fórmulas de fluido puro a solução multicomponente sem justificativa.
- [ ] **ESP-06 — Ciclos especiais e armazenamento [E; incluir se prometido].** Rankine orgânico, CO₂ supercrítico, Stirling/Ericsson, armazenamento térmico e mecânico, conforme a aplicação escolhida. **Aceite:** justificar fluido/modelo e comparar desempenho sob a mesma função, com eficiência de ida e volta quando pertinente.
- [ ] **ESP-07 — Eletroquímica e conversão direta [E; incluir se prometido].** Potencial químico, trabalho elétrico, células a combustível, baterias e limites reversíveis. **Aceite:** distinguir energia, potência, capacidade e perdas, com balanço de espécies/carga adequado e referência dos dados.
- [ ] **ESP-08 — Escoamento compressível aprofundado [E; incluir se prometido].** Mach, estrangulamento sônico, bocais convergentes/divergentes, ondas de choque e modelos com atrito/calor. **Aceite:** integrar massa, energia e quantidade de movimento; não deduzir todos os estados por um único balanço energético.
- [ ] **ESP-09 — Exergoeconomia e decisão econômica [E; incluir se prometido].** Custos, disponibilidade operacional, ciclo de vida e alocação de custos exergéticos. **Aceite:** hipóteses econômicas, base temporal e incerteza explícitas, sem converter automaticamente ganho termodinâmico em viabilidade financeira.
- [ ] **ESP-10 — Interfaces, materiais e regiões críticas [E; incluir se prometido].** Efeitos de tensão superficial, sistemas não simples compressíveis, estabilidade avançada e fenômenos críticos conforme o recorte. **Aceite:** explicitar termos adicionais e o domínio do modelo; não generalizar identidades de composição fixa para sistemas que exigem variáveis adicionais.

## 16. Plano de execução por dependências

### 16.1 Ordem recomendada

| Etapa | Entrega concreta | IDs principais | Dependência e condição para avançar |
|---|---|---|---|
| 0 — Congelar a base e corrigir bloqueios | Inventário versionado, erratas e avaliação sem padrão de letras | GOV-01/02, BAN-01/02/07/08/10, FON-01/02/09, QA-02/09 | Registrar e corrigir erros encontrados; não usar itens ambíguos como comprovação independente |
| 1 — Organizar o percurso | Matriz, pré-requisitos e unidades com objetivos | GOV-03 a GOV-06, DID-01 a DID-05 | Definir onde cada competência é ensinada e avaliada |
| 2 — Construir base de propriedades e cálculo | Tabelas, relações, ferramentas e casos de referência | FUN, PROP, MOD-01 a MOD-05, FON-03/04 | Validar estados e referências antes de produzir ciclos completos |
| 3 — Aprofundar leis e exergia | Unidades e problemas de massa/energia/entropia/exergia | ENE, ENT, EXE | Balanços e verificação física aceitos antes de comparar instalações |
| 4 — Completar aplicações | Ciclos, misturas e reações com estados determinados | CIC, MIX, QUI | Propriedades e leis aceitas; integrar incerteza/sensibilidade |
| 5 — Construir prática e projetos | Problemas abertos, projetos e soluções de referência | MOD-06 a MOD-09, DID-06 a DID-10, BAN-03 a BAN-14, PRJ | Cada competência possui evidência independente e de transferência |
| 6 — Consolidar materiais e experiência | Formulário sincronizado, fontes, acessibilidade e backup | FOR, FON-05 a FON-10, UX, QA-01/03 a QA-07 | Conteúdo essencial reproduzível e utilizável; mudanças compartilhadas verificadas |
| 7 — Avaliar e decidir a classificação | Provas, rubricas, piloto, parecer e registro final | AVA, QA-08 e seção 17 | Sem bloqueios científicos e com evidências suficientes para a afirmação de nível |
| 8 — Especializar | Trilhas opcionais selecionadas | ESP | Só ampliar a promessa após aceitar o núcleo correspondente |

As etapas podem se sobrepor: revisão de fontes, acessibilidade e construção de avaliações devem acompanhar a autoria. A ordem é de dependências intelectuais e de validação, não uma exigência de terminar toda a teoria antes de revisar a primeira aula.

### 16.2 Pacotes mínimos de trabalho

1. **Mapa curricular:** competências, dependências, estado atual, novas unidades e matriz de avaliação.
2. **Biblioteca de propriedades:** dados, fontes, referências, métodos de consulta e casos de verificação.
3. **Aulas avançadas:** desenvolvimento de FUN/PROP/ENE/ENT/EXE/CIC/MIX/QUI, ligado à prática.
4. **Caderno de problemas:** revisão dos atuais, novas famílias, soluções abertas e rubricas.
5. **Carteira de projetos:** oito projetos integradores com dados, variantes, soluções e critérios.
6. **Instrumentos de domínio:** diagnóstico, avaliações intermediárias/final, defesa, recuperação e portfólio.
7. **Material de consulta:** formulário, diagramas, tabelas, resumos e flashcards sincronizados.
8. **Pacote de qualidade:** revisão científica/numérica, fontes, acessibilidade, regressão e integridade da entrega.

Não fixar prazo ou esforço em horas sem decompor e revisar esses pacotes. As estimativas devem considerar pesquisa, derivação, autoria, cálculo, revisão independente, implementação e validação com estudantes, quando disponível. Reduzir um pacote exige revisar explicitamente a promessa e os critérios; não deve ocorrer por simples renomeação do curso.

### 16.3 Dependências críticas que não podem ser puladas

- Propriedades e referências consistentes → estados corretos → ciclos completos.
- Massa/energia e entropia → balanço de exergia → comparação de melhorias.
- Composição e estequiometria → propriedades dos produtos → balanço reativo → equilíbrio/temperatura de chama.
- Matriz de competência → problemas inéditos → rubrica → evidência de domínio.
- Revisão de enunciado/dados → solução verificada → gabarito → interface/placar.
- Política de versão → migração/backup → continuidade do estudo após correções.

### 16.4 Registro de execução por item

Usar uma linha por ID em planilha ou arquivo de acompanhamento. O formato abaixo permite iniciar o controle sem implantar uma plataforma nova.

| Campo | Conteúdo obrigatório |
|---|---|
| ID e prioridade | Identificador desta auditoria e P0/P1/P2/E |
| Estado | Não iniciado; em elaboração; em revisão; em validação; aceito; bloqueado; não aplicável com justificativa |
| Responsável e revisor | Pessoas/funções reais, sem preencher revisões inexistentes |
| Dependências | IDs, fonte, dados, ferramenta ou decisão necessária |
| Entregas | Caminhos/âncoras dos materiais produzidos |
| Evidência de aceite | Cálculo, teste, rubrica, parecer ou desempenho que encerra o item |
| Versão e data | Versão dos arquivos e data da revisão |
| Pendências | Problemas ainda abertos e seu efeito sobre a aceitação |

“Não aplicável” só cabe quando o escopo ou a solução equivalente está documentado. Não pode encerrar uma competência central sem mudar explicitamente a promessa do curso. Extensões podem permanecer não implementadas com exclusão clara da promessa.

## 17. Critérios finais para mudar a classificação

### 17.1 Matriz de evidências obrigatórias

| Competência | Ensino e prática | Evidências integradoras principais |
|---|---|---|
| C01 — Modelagem | GOV, FUN, MOD-01, DID | PRJ-04/07, prova inédita e defesa |
| C02 — Propriedades | PROP, FOR, FON-03/04 | PRJ-01/03, determinação independente de estados |
| C03 — Massa e energia | ENE, CIC, MIX, QUI | PRJ-01/04/05/06 |
| C04 — Segunda lei | ENT | PRJ-01/03/04/07 |
| C05 — Exergia | EXE, QUI-05 | PRJ-01/02/05/06 |
| C06 — Ciclos | CIC | PRJ-01/02/03/06 |
| C07 — Misturas e reações | MIX, QUI, PROP | PRJ-05 e avaliação específica inédita |
| C08 — Métodos e incerteza | MOD, PROP-10 | PRJ-04/08 e reprodução dos arquivos |
| C09 — Julgamento | ENT-07, MOD, DID-09 | PRJ-07, perturbação inédita na defesa |
| C10 — Comunicação | DID-10, AVA-04/06 | Relatórios e defesa dos projetos |

O mapeamento é uma base de planejamento. A versão final deve apontar o ID preciso de cada tarefa e o desempenho avaliado, não apenas o nome de um projeto.

### 17.2 Portas de aceite do curso

- [ ] **ACE-01 — Cobertura efetiva.** Todas as competências C01–C10 possuem conteúdo desenvolvido, prática e avaliação independente; itens P1/P2 obrigatórios estão aceitos ou têm solução equivalente documentada que preserve o escopo. Em AVA-07, a aceitação da estrutura exige a etapa (a); a etapa (b) permanece identificada separadamente e é exigida para afirmar resultados de aprendizagem medidos.
- [ ] **ACE-02 — Correção científica.** Não há pendência P0 conhecida em material usado como correto; as verificações pendentes foram concluídas e registradas, incluindo os itens problemáticos de origem.
- [ ] **ACE-03 — Autonomia real.** As avaliações exigem obtenção de propriedades, escolha de modelos, várias etapas, interpretação e julgamento; padrões de resposta, pistas e duplicações não sustentam a classificação.
- [ ] **ACE-04 — Cálculo reproduzível.** Propriedades, referências, unidades, tolerâncias e arquivos permitem refazer exemplos, problemas e projetos sem depender do autor.
- [ ] **ACE-05 — Integração das leis.** Projetos demonstram conservação, viabilidade pela segunda lei e desempenho exergético quando aplicável; fechar apenas a primeira lei não basta.
- [ ] **ACE-06 — Avaliação válida.** Banco inédito, rubricas, critérios, recuperação e defesa estão prontos e revisados; registros distinguem treino, consulta e demonstração autônoma.
- [ ] **ACE-07 — Entrega utilizável.** Navegação, acessibilidade, leitura offline prometida, imagens, fórmulas, dados e backup foram testados no ambiente declarado.
- [ ] **ACE-08 — Revisão independente e versão.** Pareceres, erratas, testes, fontes e versão de publicação estão registrados, com limitações remanescentes explícitas.
- [ ] **ACE-09 — Afirmação proporcional à evidência.** Distinguir curso preparado para nível avançado, aluno com domínio demonstrado e curso com resultados de aprendizagem medidos. Sem piloto, não atribuir eficácia comprovada nem estatísticas inventadas.
- [ ] **ACE-10 — Escopo preservado.** A evolução atende Termodinâmica; interfaces não transferem obrigações a outros módulos nem contam aprofundamento de outra disciplina como domínio do E1.

### 17.3 O que não autoriza declarar nível avançado

- Atingir uma quantidade de páginas, vídeos, fichas ou questões.
- Inserir termos especializados sem desenvolver sua utilização.
- Ter muitos acertos depois de consultar a resolução ou repetir o mesmo item.
- Realizar apenas operações de uma etapa com dados intermediários fornecidos.
- Resolver casos com todas as hipóteses indicadas, sem tarefas de escolha e crítica.
- Apresentar uma simulação sem fonte de propriedades, validação e análise física.
- Oferecer uma interface sofisticada sem aprofundamento e avaliação correspondentes.
- Usar a dificuldade de leitura, notação excessiva ou contas longas como substituto de complexidade intelectual.

## 18. Referências de comparação e suporte

As fontes abaixo foram consultadas em 27/10/2026. Servem como referência técnica e de organização curricular. A seleção dos requisitos, os percentuais da rubrica, os projetos e as portas de aceite são decisões propostas nesta auditoria; nenhuma instituição abaixo certificou o curso ou prescreveu esta lista.

1. **Graduação após uma primeira formação em Termodinâmica:** o programa de [MIT 16.050 — Thermal Energy](https://ocw.mit.edu/courses/16-050-thermal-energy-fall-2002/pages/syllabus/) descreve uma disciplina de graduação com formação anterior. É uma referência para distinguir revisão elementar de aprofundamento com exercícios e avaliações.
2. **Fundamentos e aplicações articulados:** as [notas de Thermodynamics and Propulsion do MIT](https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/index.html) incluem balanços, entropia, trabalho perdido, meios bifásicos, Clapeyron e ciclos. Servem de apoio à seleção de temas; sua presença em um índice não define, sozinha, a profundidade exigida aqui.
3. **Integração de sistemas de energia:** [MIT 2.60J — Fundamentals of Advanced Energy Conversion](https://ocw.mit.edu/courses/2-60j-fundamentals-of-advanced-energy-conversion-spring-2020/) apresenta conversão térmica, mecânica, química e eletroquímica, com materiais de problemas e projetos. Sustenta a escolha de avaliar integração; não obriga o E1 a cobrir toda essa diversidade.
4. **Fronteira com especialização/pós-graduação:** o [programa MIT 2.43 — Advanced Thermodynamics](https://www.mit.edu/~beretta/AdvancedThermodynamicsOutline.htm) estende-se a fundamentos rigorosos e modelagem de equilíbrio/não equilíbrio. É usado para evitar confundir o alvo de engenharia definido nesta auditoria com cobertura universal desse outro escopo.
5. **Água e vapor:** a [formulação industrial IAPWS-IF97](https://iapws.org/technical-guidance/release/IF97-Rev) documenta regiões e validade de um modelo de propriedades de água/vapor. É uma referência para PROP-01/02/10 e FON-03, sem obrigar o aluno a implementar todas as equações da formulação.
6. **Bibliotecas e estados de referência:** a [documentação oficial da interface de alto nível do CoolProp](https://coolprop.org/coolprop/HighLevelAPI.html) documenta consultas, identificação de fase e estados de referência. Serve de suporte ao controle de unidades, fases, modelos e referências em PROP-10/MOD; versão e fluido devem ser registrados no momento da implementação.
7. **Modelos de fluidos e misturas:** o [NIST — Reference Fluid Thermodynamic and Transport Properties Database](https://www.nist.gov/programs-projects/reference-fluid-thermodynamic-and-transport-properties-database-refprop) descreve modelos de propriedades para fluidos e misturas em diferentes regiões. É referência de validação possível; este plano não exige comprar licença nem adotar um fornecedor específico.

## 19. Conclusão operacional

O curso atual oferece uma base intermediária aproveitável: hipóteses explícitas, explicações de símbolos, exemplos, mapas de retomada, bancos e materiais locais. O principal trabalho é converter introduções e exercícios guiados em capacidade independente de modelar, obter propriedades, integrar leis, analisar sistemas reais e justificar decisões.

O resultado esperado desta auditoria é um conjunto de entregas e evidências verificáveis. A classificação só deve mudar quando as portas de aceite forem atendidas. Se a implementação ou a revisão revelar nova lacuna, adicioná-la ao registro com ID e efeito sobre o aceite; esta versão é uma linha de base abrangente para o escopo definido, não uma garantia de que a inspeção futura não encontrará novos problemas.



