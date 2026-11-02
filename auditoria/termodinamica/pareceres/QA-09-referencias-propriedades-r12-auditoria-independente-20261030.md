# QA-09 — auditoria independente das referências de propriedades e aplicações, r12

Data: 30/10/2026. Auditor automatizado `/root/next_theory`; Corretor `/root/reference_triage`. **Veredito localizado: sete referências com identidade e pertinência temática confirmadas nos limites abaixo; a referência 685 permanece com acesso direto bloqueado por 404 nesta consulta.** Há candidata separada aprovada para o vínculo 685, ainda não aplicada nesta fotografia. Este parecer não aprova QA-09 integral, nem transfere aceite automaticamente para outras versões.

## Fotografia e método

HTML SHA-256 `f76c39a3e1d8c349ebf0df72cc20a3ab21c68960c8451799bad90a9dcc4bd8c7`; inventário r12 `457a56300aab8f612ebb7f136c7c2f62520abb49c005c209a238925179248d0e`. Entrega do Corretor SHA-256 `d28ce5ce8e825812a06c8f13752207bc9df9d25efcbe17628c487fd2f451b92d`, identidades `e61d7d6a5d46c42982b00c4c58c065f0302150806329c71abab489a42af0af18`. Meu script somente leitura `evidencias/QA-09/auditoria-referencias-propriedades-r12-20261030/verificar.mjs`, SHA-256 `06a3e3e64463c31bd5939f118bd1f34b0e3128cef9c53f3839e3bfd1202d358d`, verificou os oito elementos, links, seções, intervalos e hashes perante HTML e inventário; passou. O script do Corretor também passou. A verificação de mérito usa consulta de fontes separada, não o script.

## Fontes verificadas

| Índice | Observação independente |
|---|---|
| 671 | [NISTIR 5078](https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir5078.pdf), 1998, tabela baseada em IAPWS-95, PDF aberto e página física do PDF 17 inspecionada. A linha de 0,10 MPa registra 99,606 °C, hL=417,50 e hV=2674,9 kJ/kg. Os valores não equivalem a uma validação automática da questão original 68. |
| 678 | [DOE/AFDC](https://afdc.energy.gov/glossary): definições de poder calorífico superior com água condensada e inferior com água em vapor, sem valores específicos para os combustíveis do curso. |
| 679 | [NIST Chemistry WebBook, amônia](https://webbook.nist.gov/cgi/cbook.cgi?ID=C7664417&Mask=887): CAS 7664-41-7 e massa molar 17,0305 g/mol; tabela de entalpias de vaporização em kJ/mol com temperatura e autores de origem. Converter unidades e respeitar temperatura e contexto; exemplo hipotético do curso não é dado NIST. |
| 683 | [NASA Glenn](https://www.grc.nasa.gov/www/BGH/realspec.html): calor específico dependente de temperatura e modelo de ar a altas temperaturas. É material didático para o fenômeno; não valida coeficientes quantitativos genéricos para quaisquer fluidos. |
| 684 | [MIT, primeira lei](https://web.mit.edu/16.unified/OldFiles/www/FALL/thermodynamics/notes/node17.html), §2.3.3: enchimento transiente de tanque, com hipóteses próprias que devem ser verificadas na aplicação. |
| 685 | A [URL PDF EnergyPlus 24.1](https://energyplus.net/assets/nrel_custom/pdfs/pdfs_v24.1.0/EngineeringReference.pdf) retornou HTTP 404 na abertura direta pela ferramenta web; resultado limitado a esta consulta. A busca indexada expõe §2.5, não equivale a ler o PDF integral. A [página alternativa da mesma edição](https://bigladdersoftware.com/epx/docs/24-1/engineering-reference/carbon-dioxide-predictor-corrector.html) abriu e trata do balanço de CO₂. A candidata de substituição foi objeto de parecer independente próprio `QA-09-candidata-fonte-energyplus-r12-auditoria-independente-20261030.md`; ainda não integra r12. |
| 686 | [MIT, capítulo 6](https://live.ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_6.htm): equação de energia de volume de controle em regime permanente e identificação textual de c²/2 como energia cinética por massa. Várias fórmulas são imagens e não foram totalmente verificadas visualmente. |
| 687 | [MIT, aula 16](https://ocw.mit.edu/courses/2-60j-fundamentals-of-advanced-energy-conversion-spring-2020/1437d5925093b270c871160ec861fd12_MIT2_60s20_lec16.pdf): conferi as páginas 8 e 10 do PDF, que apresentam reaquecimento e aquecedor aberto com balanço de entalpias. Material didático com conteúdo de terceiros em outras páginas e restrições próprias; não pressupor licença para reprodução. |

## Constantes críticas: não misturar origens

A página 2 do PDF MIT 687 registra 22,088 MPa para a pressão crítica da água, enquanto a [IAPWS IF97 revisada](https://iapws.org/technical-guidance/release/IF97-Rev.download), §3, registra 22,064 MPa e 647,096 K. A diferença é 0,024 MPa, portanto não são o mesmo número nem arredondamentos equivalentes às casas mostradas. O documento IAPWS informa revisão de 2007 e clarificação de 2012; a referência MIT é adequada para os ciclos nas páginas citadas, mas não deve ser atribuída como origem do valor crítico IAPWS. A origem ou natureza exata da divergência do MIT não foi estabelecida.

As observações de rede são localizadas na data e ferramenta, não garantem disponibilidade duradoura. Não houve navegador real, validação de todo o PDF NIST, validação do item 68, revisão humana, licença de reprodução ou inspeção das referências restantes. O vínculo 685 requer aplicação e auditoria do resultado efetivo, e a ocorrência em A4 permanece fora deste escopo.
