# QA-09 — Revisão independente das candidatas dos diagnósticos 12, 14 e 19, r1

Data: 29/10/2026. Revisão localizada por apoio automatizado independente, à luz de `QA-09-adjudicacao-diagnosticos-12-14-19-independente-r1.md` SHA-256 `6d8fe05bbf2eab9697d0d331b8b19fa04b964e12d2de0fd07f194a197362d869`. **As três candidatas são tecnicamente adequadas** para sanar as insuficiências adjudicadas. Parecer sobre fragmentos isolados, sem aplicação, alteração de produto/controle ou aprovação global QA-09.

## Fotografia e método

O documento atual `modulos/e1-termodinamica.html` tem SHA-256 `7541e7c4c8314922992e99e8b62b40342c2d938e6edeac67ef9f74b69f86c17c`; o inventário QA-09 `auditoria/termodinamica/evidencias/QA-09/inventario-r4.json` tem `44d19642bcf39109edf620e7304580b7a8a686e7c42cfa7101fa3d118a79d054`. Para cada número li original, candidata e manifesto, conferi os hashes e constatei que o fragmento original ocorre exatamente uma vez no HTML. A substituição dos bytes declarados no manifesto pelo texto candidato produz exatamente cada novo fragmento; não há outra diferença literal. As candidatas mantêm solução, perguntas fora do trecho especificado, estrutura e ligações. Arquivos de fragmento incluem uma nova linha final; hashes de fragmento abaixo excluem essa linha.

## 12 — ciclos e compressor

A candidata explicita que não há outros consumos de potência e que 300 kW é o calor total recebido. Isso exclui o consumo auxiliar do contramodelo adjudicado e fixa o denominador, preservando o arranjo turbina/compressor da base. `Ẇlíq=140−50=90 kW`, `η=90/300=0,30=30%`; na compressão anterior à descarga, as duas válvulas ficam fechadas no modelo convencional. Os `6/8=0,75=75%` referem-se, segundo a base `#base-eficiencia-volumetrica`, a volumes nas condições de sucção e mesma base de ciclo. A adjudicação considerou repetição dessa referência no comando esclarecimento útil, não pendência obrigatória. Igualdades para dados nominais, sem tolerância instrumental declarada.

## 14 — geração e superfície

A candidata explicita que as demais faces são termicamente isoladas e solicita a temperatura **média** da face exposta. Em regime permanente, sem radiação nem outras saídas de calor e com h uniforme como o valor dado, `V=2 m³`, `A=2 m²`, `Q̇=60×2=120 W`, `T̄s=18+120/(6×2)=28 °C`. A diferença de 10 K equivale a 10 °C de intervalo. Não há necessidade de supor o interior isotérmico; a temperatura média é coerente com a base `#base-geracao-face`. As condições excluem o contato condutivo hipotético antes apontado. A solução publicada permanece correta; igualdades para dados nominais, sem tolerância instrumental declarada.

## 19 — balanço de CO₂

A candidata explicita ausência de outras fontes, remoção por outros mecanismos e troca com outras zonas e requer volumes referidos às mesmas condições. Com regime estacionário bem misturado e o modelo da base `#base-balanco-co2`, `G=20×300 mL/min=0,36 m³/h`; excesso permitido `500 ppm=0,0005`; `V̇=0,36/0,0005=720 m³/h`. O valor é o mínimo para atender ao excesso máximo nesse modelo; não se trata de determinação normativa de ventilação. O novo texto exclui o sumidouro do contramodelo adjudicado. Igualdade para dados nominais, sem tolerância de medição declarada.

## Identidade, progresso e aplicação

Os três são `div.exemplo` da seção `#preparacao-questoes`, fora dos 197 artigos BAN-08 e sem alternativas ou registro próprio de gabarito pontuável. `assets/curso.js` SHA-256 `a20f4d19158073a9a1c48aabdfba8fa863b02063e16061c00b16448a6ccc2e13` usa seletores `article.questao` e `.concurso-item, .avalia-item` para os bancos, não esses blocos. Sob a inspeção estática e os deltas literais, não se identificou alteração de digitais ou respostas salvas dos bancos. Não houve teste em navegador nem verificação de extensão externa. Aplicação futura altera o hash do documento: é necessário conferir a versão realmente aplicada, seus deltas, artigos/código, vínculos, progresso e fotografias e aceites dependentes, sem presumir sua transferência automática.

## Hashes de evidência SHA-256

| Evidência | D12 | D14 | D19 |
|---|---|---|---|
| Fragmento original | `618ac9f908af2cd203e8c44ff47708b488aa0e80c61111b4a1e5e082c4e35ca7` | `d31dc8c7929c0d00feccdf2f5baca49b3d957a5cb81c7ce36fd26a68330df849` | `345887a5a233fa75a098ddabe3540edd95857c6fc0feea4c11b99fb64f44ea71` |
| Fragmento candidato | `2a5914ed4fd1abd6a5e0c92af1254bb7cb353eda23e4ba232d1f39ac04187d09` | `ac518b30e57fcbc1e99b461aeedf936b6ac549be41cda580c12b8182f6234e67` | `9bb600fe48c6e15ed78eb6c2cff4091af810e917a668f15834fa565203de488a` |
| Arquivo original | `40f7dac84a26a64eace5e48268d110dd811b73f8c81d933ce7468a6277d2428b` | `8d52f26e4898c51564fbe98c853416a861e00a211c8ab56514f55c2b88b2700e` | `e7621d4de7c959d1221118ff39a1d31ea78da22394875c8ee626016b1e0f0940` |
| Arquivo candidato | `c409e88c1b930961bd88567c212d280d36284dfcb845d3579fff2d8321cd3a4a` | `970ac86ce8d9e207f83271a2554ec92189ddb76d08be8fbd8d62e792fc9c919c` | `5256dc8b5a3ebccc904b4f36edf41482424f713c5acb765563f11389ce23c89b` |
| Manifesto JSON | `13bc2d60888322b7da8ea5f3f0b1569b3da3941abfd5cb3fa7058c3c43501084` | `ac9c916cdafc28efb6f71ba4f736ac41cbeed998e2051c3ba8680adbebd8fa4e` | `f881c349baac447b31d893729484d52cce85c4b2e32a73e92406d2293996a943` |

Os arquivos estão em `auditoria/termodinamica/evidencias/QA-09/`, com prefixos `diagnostico12-`, `diagnostico14-` e `diagnostico19-`. Os estados nos manifestos ainda descrevem preparação prévia e não constituem decisão nem aplicação; a adjudicação acima é identificada separadamente.
