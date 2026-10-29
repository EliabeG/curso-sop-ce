# Parecer FUN-01 — rodada 1

**Veredito: AJUSTES_OBRIGATORIOS.** Data: 27/10/2026. Revisor responsável: agente automatizado `/root/auditor_aaa`; apoio técnico independente: `/root/auditor_aaa/auditoria_tecnica_ban02`.

A aula, os quatro problemas, as soluções e as rubricas atendem ao conteúdo científico e pedagógico examinado de FUN-01. A única pendência obrigatória desta rodada é documental: dois títulos antigos permanecem no inventário e no resumo. A reapresentação deve corrigir essa identificação, preservando o conteúdo já verificado. **O próximo ID permanece bloqueado até o parecer da nova versão.**

## Critério e versão

Foram aplicados FUN-01, a regra comum da seção 3.2 da auditoria principal e o protocolo Corretor–Auditor. O aceite exige desenvolver equilíbrio térmico, mecânico, químico e de fases, postulado de estado, composição e independência; ensinar e avaliar classificação de dados suficientes, redundantes ou incompatíveis, incluindo saturação, misturas e região supercrítica. Também exige objetivos, pré-requisitos, teoria/hipóteses, exemplo com decisões, prática independente, solução/rubrica, fontes, revisão científica/numérica e vínculo C01–C10.

Examinados integralmente: a unidade 3.1 e sua preparação, os quatro enunciados/soluções/rubricas, os quatro registros novos, os dados e as seis linhas alteradas da matriz. Os cinco arquivos atuais coincidem em bytes com o pacote congelado r1 e com estes hashes:

| Arquivo | SHA-256 examinado |
|---|---|
| `modulos/e1-termodinamica.html` | `cacda8c7742eead77aa1e92021b01c085c1b7340201d5cca0ada8ff743a8b04f` |
| `assets/termodinamica/fun01-dados-v1.json` | `a73b4d6140219cbd6b005216bb7a44db0a68b05f21ca51b7ac4b1ca782dd1448` |
| `assets/termodinamica/fun01-calculos-v1.mjs` | `a0fbdc4e6e7291a563db2362d26f4107ad67f56843e741d96eef8eea5a8d2a88` |
| `inventario/inventario-questoes.json` | `4b18b397b68b9a46aae4db4c526d7bc2e4712df0e65b33359ba414fc6112e4df` |
| `inventario/INVENTARIO_QUESTOES.md` | `5242d53447dc9441109586d448793c324596745e2017546a19cb39ff5b854725` |

Os dois últimos caminhos são relativos a `auditoria/termodinamica`. A entrega e as cópias históricas r1 não devem ser sobrescritas.

## Verificações independentes

Resolvi os quatro enunciados com os dados fornecidos **antes de ler suas soluções ou depender do programa de cálculo**. A memória está em [cálculos independentes](FUN-01-r1-calculos-independentes.json); a comparação científica e documental está em [evidências consolidadas](FUN-01-r1-evidencias.json).

| Caso | Resultado independente e decisão conferida |
|---|---|
| Tanque | `v=0,45 m³/kg`, `x=0,507494454`, vapor `1,014988908 kg`, `h=1621,949040 kJ/kg`; intervalos separados por pelo menos `175,050960 kJ/kg`. Há conflito condicionado às hipóteses, sem prova isolada de defeito de um sensor. |
| Mistura | I líquido; II bifásico, `xA=0,30`, `yA=0,5625`, `β=0,380952381`, `nl=6,190476190 mol`, `nv=3,809523810 mol`; III vapor. As tentativas bifásicas de I/III dão frações inviáveis. IV admite uma família condicionada à composição/fases, não uma conclusão automática de coexistência. |
| Supercrítico | A não garantido; B/C seguramente fora da definição simultânea adotada; D supercrítico com título indefinido. Só a melhoria conjunta garante A. Limites estritos: erro de T menor que `2,904 K` e de p menor que `0,036 MPa`. |
| Bancada | H-1 falha térmica e mecanicamente; H-2 requer `29,620 kPa` no fundo, diferença intrínseca de μ de `+0,3924 J/mol` compensada pela gravidade. Em D, diferença inicial de μA de `3457,695396 J/mol`; transferência de `0,120279047 mol`; pressões finais `70/130 kPa`. Conservação por espécie e curvatura positiva de F confirmadas na coordenada permitida. |

Conferi ainda os exemplos resolvidos, sinais, bases molar/mássica, dimensionalidade, limites dos modelos e a distinção entre incompatibilidade com a hipótese bifásica e impossibilidade de qualquer estado. A derivação hidrostática, a comparação de potenciais e o teste de estabilidade não são usados como provas de fenômenos excluídos pelo modelo.

As três linhas da [tabela NIST](https://www.nist.gov/document/nistir5078-tab2pdf) e as constantes da [IAPWS, §3](https://iapws.org/technical-guidance/release/IF97-Rev.download) conferem, inclusive a conversão de volume. A regra das fases foi confrontada com [MIT 2.43, aula 09](https://ocw.mit.edu/courses/2-43-advanced-thermodynamics-spring-2024/mit2_43_s24_lec09.pdf); Raoult com [University of Washington, §5.1](https://faculty.washington.edu/jcv2/CHEM452_WI2023/html/ideal_solutions_and_colligative_properties.html); potenciais e restrições com [MIT 3.020, aula 13](https://ocw.mit.edu/courses/3-020-thermodynamics-of-materials-spring-2021/mit3_020s21_l13.pdf), [Tong, §4.4](https://www.damtp.cam.ac.uk/user/tong/statphys/statmechhtml/S4.html#S4.SS4) e as demais fontes indicadas na evidência. O link MIT `SPRING/node10` está correto para sua edição; a numeração diferente de `FALL/node11` não é um erro. A abertura direta de duas páginas IUPAC retornou 403 nesta ferramenta; os conteúdos oficiais foram recuperados na busca e corroborados pelas notas MIT. Isso não foi confundido com defeito do produto.

O [apoio técnico](FUN-01-r1-tecnico.md), examinado e incorporado a este parecer, reexecutou os **239 checks documentais, 28 numéricos e o validador canônico**: 194 artigos/194 registros, oito recursos, 1.042 referências locais, zero erros/avisos. Confirmou independentemente os 190 artigos e registros anteriores intactos, os seis arquivos compartilhados preservados, as cinco cópias do manifesto e os pacotes BAN-02. Esses testes comprovam reprodução e preservação; não substituem a leitura semântica acima.

## Quadro de critérios

| Critério | Resultado e fundamento |
|---|---|
| Objetivos observáveis e pré-requisitos | Atendido. Entrada e recuperação cobrem bases, unidades e intervalos; a preparação ensina o logaritmo e a derivada necessários. |
| Equilíbrio térmico e mecânico | Atendido. Restrições, condução, balanço de forças, gravidade e suporte são ensinados e aplicados; não se reduz equilíbrio à ausência de movimento. |
| Equilíbrio químico e de fases | Atendido no escopo. Distingue transferência da mesma espécie de reação estequiométrica; inclui estacionariedade e estabilidade. Coexistência local não é confundida com equilíbrio global. Reações reais quantitativas não são anunciadas como avaliadas. |
| Postulado de estado e independência | Atendido. Composição, coordenadas de trabalho, escala extensiva, identidades, existência/unicidade e teste local são delimitados. |
| Composição e graus de liberdade | Atendido. Derivação de F, composição global versus de fase, quantidades e bases molar/mássica desenvolvidas e cobradas. |
| Saturação, mistura, supercrítico; dados suficientes/redundantes/incompatíveis | Atendido. Os casos exigem classificação fundamentada e informações complementares, com limites de validade claros. |
| Exemplos resolvidos com decisões | Atendido. Há rejeição de conclusões inadequadas, justificativa do modelo e interpretação; não apenas fórmulas. |
| Prática independente inédita local | Atendido. Os casos integrados exigem inversão/diagnóstico, seleção de fases, construção de família de estados, melhoria de medidas e redistribuição finita com estabilidade. Não são simples trocas de números dos exemplos. Retomadas de fixação são explicitadas. |
| Soluções, rubricas e progressão | Atendido. Quatro rubricas de 10 pontos, justificativas observáveis, erros críticos e limites de pontuação; a bancada ainda exige mínimos nos três eixos centrais. |
| Fontes, versões e dados | Atendido. Dados reais rastreáveis e modelos fictícios identificados; tolerâncias editoriais não são apresentadas como incerteza NIST. |
| Revisão científica e numérica | Atendido no conteúdo examinado. Resolução própria concorda com as soluções e a reprodução computacional. |
| Matriz e nível cognitivo | Atendido. As seis competências permanecem parciais. Dois itens intermediários e dois avançados estimados são defensáveis dentro do modelo delimitado; não há piloto ou domínio global alegado. |
| Cadastro dos novos itens e metadados | **Não integralmente atendido: R1-A.** Campos cognitivos e vínculos pertinentes; duas identificações de título estão desatualizadas. |
| Escopo e regressões | Atendido nas verificações descritas. Conteúdo anterior e infraestrutura preservados; nenhum conteúdo de outro módulo alterado pelo pacote. |
| Responsáveis, versão e limitações | Atendido. Autoria e revisões identificadas como automatizadas; arquivos, hashes e limites declarados. |

A verificação local de originalidade combinou leitura semântica dos casos/exemplos e comparação com o banco anteriormente auditado. A busca auxiliar não encontrou sequências de 12 palavras dos novos enunciados nos 190 artigos antigos; essa ausência não foi tratada como prova suficiente de novidade universal.

## R1-A — sincronizar os dois títulos documentais

| ID | Título antigo no inventário/resumo | Título publicado a usar |
|---|---|---|
| `fun01-e1-mistura` | Problema 2 — A mesma temperatura não determina o lote | Problema 2 — Quatro lotes e uma hipótese bifásica |
| `fun01-e1-supercritico` | Problema 3 — Quando a leitura garante condição supercrítica? | Problema 3 — O rótulo “supercrítico” é sustentado pelos dados? |

Os outros 192 títulos correspondem aos artigos. IDs, links e hashes estão corretos; não há encaminhamento para problema errado. O schema exige texto não vazio e não exige igualdade literal ao `h3`, portanto **não se atribui ao validador uma falha de contrato que ele não promete detectar**. O problema é a identificação documental desatualizada da versão entregue, também reproduzida nas linhas 277–278 do resumo e no extrato dos novos registros.

Reapresentar somente a sincronização dos dois campos `titulo` no canônico, das duas linhas do resumo e de suas representações derivadas da **nova rodada**, com novos hashes e delta completo. Preservar a r1 histórica, os demais campos/192 registros e os arquivos de aula, dados e cálculo. A validação canônica deve continuar passando. Não se exige mudar schema, ampliar testes gerais ou refazer a investigação científica preservada.

## Limites e decisão

Este Auditor e seu apoio não executaram navegador. Li o [registro do coordenador](../evidencias/FUN-01/navegador-coordenador-r1.md), vinculado ao mesmo hash: navegação, abertura das quatro soluções, alternância por teclado do problema 3 e recarga do acréscimo final foram confirmadas. As capturas observadas, ausência de erros nos logs e tentativas inconclusivas estão delimitadas. Não converti essa evidência em execução minha nem em teste amplo de acessibilidade. Não houve piloto com estudantes, certificação externa ou aceitação de todos os IDs do curso.

**FUN-01 r1 requer apenas R1-A e não libera o próximo ID.** Uma reapresentação restrita poderá ser auditada pelo delta e pela preservação dos critérios aceitos acima. BAN-10/FON-09, GOV-02, demais FUN/PROP/MIX e a classificação global avançada continuam fora deste aceite.

### Orientação de dependências, sem liberação

Após o fechamento efetivo de FUN-01, FUN-02 pode ser desenvolvido como unidade própria: as relações entre propriedades, calor/trabalho, caminhos e ciclos podem ser ensinadas e avaliadas com fontes, modelos e problemas próprios. Não foi identificada dependência científica ou técnica que obrigue utilizar os itens legados pendentes de BAN-10/FON-09. Os casos CR09/CR24/CR68/CR79 continuam excluídos de comprovação de domínio e não devem fornecer dados defeituosos ou hipóteses implícitas às novas atividades.

Essa viabilidade exige explicitar a base matemática pertinente, convenção de sinais, condições dos caminhos e fechamento dos balanços; não antecipa o aceite da futura unidade nem das demais competências. Se sua implantação passar a reutilizar qualquer material P0 afetado, o bloqueio correspondente deve ser resolvido antes desse uso. A fila permanece decisão do coordenador, e R1-A de FUN-01 ainda precisa ser encerrado primeiro.
