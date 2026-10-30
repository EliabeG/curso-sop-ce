# QA-09 — referências de energia e FUN-02, r12→r13

Data: 30/10/2026. Corretor automatizado `/root/reference_triage`. **Entrega localizada aguardando auditoria independente; QA-09 integral continua aberto.** O lote abrange os índices 141–160, base zero, da coleção `referencias` do inventário r12, com reconciliação explícita para a fotografia r13 em que a aula foi alterada depois do início da triagem.

## Fotografia, identidade e classificação

A fotografia r12 da aula (`modulos/e1-termodinamica.html`, SHA-256 `f76c39a3e1d8c349ebf0df72cc20a3ab21c68960c8451799bad90a9dcc4bd8c7`) foi preservada em `auditoria/termodinamica/evidencias/QA-09/aplicacao-energyplus-fichas-r13-r1/resultado/antes-aula.html`; o inventário r12 tem SHA `457a56300aab8f612ebb7f136c7c2f62520abb49c005c209a238925179248d0e`. A aula r13 atual tem SHA `f19000a7ddb1f3552b9633b0efec266fb3f6c5e5065808505a2f65b2005aefbc`, inventário r13 `0df99b79bcc2350581fcdded72435d30d07858de237a549e6228ca73682f8d9b`.

As 20 referências foram confrontadas nas duas fotografias: seus metadados de documento, seção, âncora, rótulo, URI e posições UTF-16 são iguais, e o SHA do elemento `<a>` também coincide. [identidades.json](identidades.json) registra cada identidade individual; sua igualdade não comprova todas as dependências e não transfere aprovação de cálculos. O [verificador](verificar.mjs) é somente leitura: compara índices e metadados, reextrai cada link nas duas páginas e confirma que os 11 destinos internos existem uma vez. Não avalia rede, apresentação em navegador real, licenças, nem correção científica das páginas.

| Índices r12/r13 | Categoria e função | Verificação |
|---|---|---|
| 143–144 | Navegação interna para `#base-mistura-termica` e `#energia` | Destinos existem uma vez; não são fontes externas. |
| 145–152 | Navegação interna da unidade FUN-02 e bases anteriores | Destinos existem uma vez; não se contam como oito cálculos. |
| 158 | Navegação para `#fun02-exatidao` | Destino existe uma vez; não é fonte externa. |
| 141–142, 153–157, 159–160 | Nove vínculos externos para sete URLs distintas | Consultas e limites por ocorrência abaixo; URL repetida não elimina o contexto distinto. |

## Referências externas — consulta temática limitada

Páginas acessadas em 30/10/2026 por ferramenta de pesquisa web. São materiais didáticos disponibilizados por seus autores/editoras; servem para fundamentação, não são medições de propriedades. A consulta textual não garante renderização visual de imagens, disponibilidade futura nem direitos de reprodução.

| Índices | Fonte | Conteúdo conferido e limites |
|---|---|---|
| 141 | [OpenStax, University Physics 1, §7.2](https://openstax.org/books/university-physics-volume-1/pages/7-2-kinetic-energy) | Página acessível; cobre energia cinética e dependência do referencial. Apoia a fórmula de translação não relativística do curso, não todas as aproximações de balanços de escoamento. |
| 142 | [OpenStax, University Physics 1, §8.1](https://openstax.org/books/university-physics-volume-1/pages/8-1-potential-energy-of-a-system) | Página acessível; discute energia potencial gravitacional e escolha de referência perto da superfície terrestre. O uso `mgΔz` do curso requer g aproximadamente uniforme. |
| 153, 159 | [University of Washington, CHEM452, apêndice 4.1](https://faculty.washington.edu/jcv2/CHEM452_WI2023/html/appendix_differentials.html) | Página acessível; apresenta diferencial total e variáveis mantidas constantes nas derivadas parciais. 153 fundamenta notação da aula; 159 é outro uso em variáveis normalizadas, cujo fator de conversão deve ser verificado no exercício. |
| 154, 160 | [OpenStax, Calculus 3, §6.3](https://openstax.org/books/calculus-volume-3/pages/6-3-conservative-vector-fields) | Página acessível; trata domínio aberto simplesmente conexo, teste de parciais e independência de caminho em campos conservativos. As condições de continuidade e domínio da aula devem ser aplicadas ao modelo específico; igualdade de parciais apenas em um ponto não prova exatidão global. |
| 155 | [MIT, primeira lei, §2.1](https://web.mit.edu/16.unified/www/SPRING/thermodynamics/notes/node14.html) | Página acessível; discute energia, calor, trabalho e primeira lei. Para os sinais adota-se a convenção explicitada pelo E1; algumas expressões são imagens e não foram visualmente conferidas nesta triagem. |
| 156 | [OpenStax, University Physics 2, §3.4](https://openstax.org/books/university-physics-volume-2/pages/3-4-thermodynamic-processes) | Página acessível; aborda processos adiabáticos e cíclicos. **Ressalva:** a seção afirma em termos gerais que uma expansão adiabática realiza trabalho e diminui temperatura. Isso não cobre expansão livre adiabática de gás ideal em recipiente rígido isolado, que pode ter `Q=W=ΔU=0` e mesma temperatura. A aula E1 distingue a exceção; não adotar a frase geral da fonte como regra universal. O Auditor deve avaliar a adequação desse vínculo e se requer contextualização ou fonte adicional. |
| 157 | [OpenStax, University Physics 2, §4.6](https://openstax.org/books/university-physics-volume-2/pages/4-6-entropy) | Página acessível; a relação integral apresentada usa percurso reversível. Não basta, isoladamente, validar todos os detalhes de irreversibilidade interna e externa do texto E1. |

Na ressalva do índice 156, o contramodelo é um gás ideal em um compartimento de recipiente externo rígido e adiabático, expandindo livremente para vácuo após abertura de uma membrana: não há calor através da fronteira nem trabalho externo; desprezando ΔEc/ΔEp do conjunto, `ΔU=0`; para gás ideal de composição fixa, temperatura final em equilíbrio é a inicial. A construção é um teste conceitual com hipóteses declaradas, não uma afirmação de que toda expansão adiabática seja livre.

## Limites e pendências

Não foram modificados HTML, fórmulas, inventários ou evidências históricas. O lote identifica 20 **referências**, não 20 cálculos ou percentual da revisão. É necessária auditoria independente das identidades, consultas e ressalva do índice 156. A investigação de direitos de reprodução, testes em navegador e o restante das referências e cálculos continuam pendentes; o próximo ID não foi liberado.
