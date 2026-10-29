# Parecer FON-02 — rodada 1

**AJUSTES_OBRIGATORIOS. Nenhum próximo ID liberado.** Auditor: agente automatizado independente /root/auditor_aaa. Data: 28/10/2026. O único impedimento é R1-A, na fidelidade da matriz de fontes. Não foi identificado outro ajuste necessário no conteúdo do curso neste recorte.

A revisão cobriu os 80 artigos completos, previamente lidos pelo Auditor e registrados em [notas independentes](FON-02-leitura-base.json), confrontados com os 80 diagnósticos finais e as 21 redações alteradas. As fontes oficiais previamente examinadas em FON-01 foram herdadas por identidade; não houve aceitação por amostragem. A [evidência científica](FON-02-r1-cientifico.json) contém as 80 conclusões individuais, 11 consultas primárias, sete alvos didáticos efetivamente lidos e os cálculos independentes. O [subparecer técnico](FON-02-r1-tecnico.md), de /root/auditor_aaa/tecnica_fon01, e seus [resultados detalhados](FON-02-r1-tecnico.json) foram examinados para esta decisão.

| Critério do recorte | Resultado |
|---|---|
| Identificação individual de constantes, propriedades, hipóteses e exemplos nos 80 CR | Atendido: distinção entre dados originais, derivações e escolhas autorais conferida. |
| Separação visível entre transcrição e comentário/suplemento | Atendido: 21 esclarecimentos e 71 resumos de autoria; nove estudos críticos preservados. |
| Justificação científica e procedência dos suplementos | Atendido no recorte: conversões, convenções, hipóteses de balanço e modelos delimitados; fontes pertinentes conferidas. |
| Fidelidade do índice documental de fontes por item | **Não atendido — R1-A.** |
| Preservação de enunciados, opções, chaves, figuras, identidade das respostas e pontuação | Atendido: componentes oficiais, 734 MathML, 71 itens pontuáveis e nove críticos preservados. |
| Integridade, reprodução e inventário | Atendido: 55 arquivos, nove cópias e dois vínculos FON-01 conferidos; 205 verificações reproduzidas; inventário 197/197, 29 recursos, 1.236 referências, sem erros/avisos. |
| Atribuição e limites da evidência de navegador | Atendido: relatório do coordenador identificado; este Auditor não o apresenta como teste próprio nem como auditoria ampla de acessibilidade. |

Os pontos sensíveis foram examinados: CR26 identifica caloria termoquímica, enquanto CR28 mantém a conversão dada na prova; CR24 distingue deslocamento Celsius–kelvin da atual definição do kelvin; CR36 delimita a relação adiabática e capacidades constantes; CR50 conserva a mesma entrada e pressão de saída, sem igualar entalpias finais; CR79 distingue valores escolhidos de medições e constante exata de aproximação decimal. As verificações de dados CR68 e estudos críticos anteriores são herdadas somente onde o conteúdo foi preservado. [NIST — calorias](https://www.nist.gov/pml/special-publication-811/nist-guide-si-footnotes), [MIT — calores específicos e processo adiabático](https://web.mit.edu/16.unified/www/SPRING/thermodynamics/notes/node17.html), [MIT — energia de escoamento](https://web.mit.edu/16.unified/OldFiles/www/SPRING/thermodynamics/notes/node18.html).

**R1-A — corrigir o índice de fontes da matriz.** Em revisao-suplementos-80-r1.json, o campo registros[].fontes.ensino_e_fundamentos_ja_vinculados contém apenas o primeiro alvo em cada um dos 80 itens. Os 80 rótulos incluem texto que ultrapassa a âncora. Das 158 ocorrências pertinentes existentes na base, foram omitidas 78 em 50 registros: 61 internas e 17 externas. Exemplos: CR01 perde #base-medidas; CR06 perde #base-instrumentos; CR10 perde #base-medidas e #base-propriedades. Sete ocorrências externas ausentes desse índice também não aparecem no catálogo global; as demais redundâncias não recuperam a associação individual correta.

Os vínculos continuam no HTML; não há regressão de navegação identificada. A falha está no artefato entregue para demonstrar o rastreamento: texto de enunciado, comentário e outras fontes fica associado à primeira âncora, enquanto destinos são descartados. O Markdown remete ao JSON e não reproduz esse campo, portanto não sana a omissão. As 205 verificações do autor não verificavam a exatidão desses rótulos ou sua cobertura.

Reapresentar somente a correção documental: reconstruir os 80 arrays pelas âncoras reais da base declarada, com destino e texto próprios, incluindo as 158 ocorrências pertinentes. Manter separado o conjunto de fontes já vinculadas das fontes acrescentadas na r1; não é necessário expandir o catálogo novo indiscriminadamente. Atualizar os derivados, a entrega e o manifesto necessários. Demonstrar, por comparação independente em todos os itens, href/texto/ordem, ausência de texto externo à âncora e cobertura integral. Preservar o restante da matriz, as fontes novas, os arquivos do curso/inventário/resumo e todo o pacote r1.

**Observação editorial O1:** dois hashes da tabela da entrega têm espaço interno, nos registros da matriz e do relatório de navegador. A remoção do espaço reproduz exatamente os hashes reais e do manifesto. Não constitui divergência binária nem bloqueador independente; imprimir os 64 caracteres contíguos na nova entrega.

Versões efetivamente auditadas, reconferidas pelo Auditor:

| Arquivo | SHA-256 |
|---|---|
| Entrega FON-02-r1.md | 9d5936596e2ada28e8e337bcf4c8084c2d361a2654cea92f886644f2268142de |
| Manifesto r1 | 25c420ff6f7650c982c402b3715c623ca7e68866f72e26bbbf0565fc6e065224 |
| modulos/e1-termodinamica.html | 0fc12a96fd30d366770a56c366fb61bc6a9fa7bd761e81fb40242a30f6dd78c7 |
| inventario-questoes.json | 0faacb0d84482e53afae1f8e481ce676f0e68e793376a9d4ad35a4aa6a93af8e |
| INVENTARIO_QUESTOES.md | 4c0b477b9479c6c546507535a194bb75805b2adf1bceaaa34337a20d02e3294e |
| revisao-suplementos-80-r1.json | ffeab0e9324624579772588dd010d2d70ad256e025290d06a0efb474fd5f9170 |

A [decisão estruturada](FON-02-r1-evidencias.json) reúne critérios, hashes e aceite exigido de R1-A. Os critérios já atendidos podem ser herdados na reauditoria mediante identidade comprovada; não é necessária nova leitura dos 80 artigos ou fontes intactas. A r1 permanece congelada. Este parecer não encerra BAN-07/BAN-08, FON-03/FON-10 nem certifica o curso como avançado. O próximo ID permanece bloqueado até APROVADO formal da reapresentação.
