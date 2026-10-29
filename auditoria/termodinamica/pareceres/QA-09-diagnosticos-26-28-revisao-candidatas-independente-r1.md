# QA-09 — revisão independente das candidatas dos diagnósticos 26–28, r1

Data: 29/10/2026. Apoio automatizado independente, sem alterar produto ou controle e sem aprovação global QA-09. Decisão localizada: **as três candidatas são tecnicamente adequadas aos pontos adjudicados**, sujeitas à verificação da aplicação e dos artefatos dependentes.

## Fotografia e método

Documento `modulos/e1-termodinamica.html` SHA-256 `7541e7c4c8314922992e99e8b62b40342c2d938e6edeac67ef9f74b69f86c17c`; inventário QA-09 `auditoria/termodinamica/evidencias/QA-09/inventario-r4.json` SHA-256 `44d19642bcf39109edf620e7304580b7a8a686e7c42cfa7101fa3d118a79d054`; adjudicação `auditoria/termodinamica/pareceres/QA-09-adjudicacao-diagnosticos-26-28-independente-r1.md` SHA-256 `68869eb1cf952661bcc8d36c4e9f3ba2d96948d5b94337299f99e6a87ef5b3cb`. As três informações de fonte, inventário e adjudicação em cada manifesto conferem com os bytes. Cada fragmento original ocorre uma só vez no documento; em cada caso o texto `antes` ocorre uma vez e sua substituição exata por `depois` produz byte a byte a candidata, sem outros deltas. Arquivos isolados têm nova linha final; os hashes de fragmento abaixo referem-se ao conteúdo sem ela.

## Diagnóstico 26 — ciclo com dois fornecimentos

A candidata explicita que os trabalhos listados e os dois fornecimentos são todos os trabalhos e todo calor externo recebido, referidos à mesma massa; a rejeição é a única outra transferência térmica para o exterior. Ela exclui os termos adicionais dos contramodelos e mantém a solução. `w_líq=600+900−20=1480 kJ/kg`; `q_in=2400+800=3200 kJ/kg`; `η=1480/3200=0,4625=46,25%`; `q_out=3200−1480=1720 kJ/kg`. A solução mantém as mesmas unidades e valores. O fechamento energético não comprova por si a existência física de um ciclo com estados e limites de segunda lei que não foram fornecidos. Igualdades exatas para dados nominais, sem tolerância experimental declarada.

## Diagnóstico 27 — extração e potência do estágio

A candidata identifica o estágio posterior como turbina estacionária e adiabática, com variações cinética e potencial desprezíveis, e identifica a queda como entalpia. O aquecedor aberto continua referido às hipóteses da base. `y=(700−300)/(2300−300)=400/2000=0,20`; de 10 kg/s, extração `2 kg/s`, restante `8 kg/s`; `Ẇ=8×250=2000 kW`. Usar indevidamente a vazão total daria `10×250=2500 kW`. O modelo do estágio exclui o calor perdido do contramodelo e não pressupõe reversibilidade. Valores exatos para dados nominais, sem tolerância experimental declarada; solução e elos com as bases permanecem.

## Diagnóstico 28 — CO₂ transiente

A candidata declara que além de G não há outras fontes, reações, remoções ou trocas com outras zonas e que volumes são referidos às mesmas condições, dentro do modelo de mistura e vazões da base. Conversões `Ci=600 ppm=0,0006`, `Ce=400 ppm=0,0004`. `V dCi/dt=0,20+500(0,0004−0,0006)=0,10 m³/h`; dividindo por 200 m³, `dCi/dt=0,0005 h⁻¹=500 ppm/h` no instante inicial. Para condições mantidas, `Ce+G/V̇=400+0,20/500×10⁶=800 ppm`, alcançado assintoticamente no modelo; não pode ser imposto instantaneamente nem se conserva a taxa inicial. O sumidouro do contramodelo fica excluído. Igualdades exatas no modelo para dados nominais, sem tolerância de medição declarada. Não são limites normativos de ventilação.

## Identidade e progresso

Os três são `div.exemplo` da seção `#preparacao-questoes`, fora dos 197 artigos BAN-08 e sem alternativas ou gabarito próprio em placar. O código `assets/curso.js` SHA-256 `a20f4d19158073a9a1c48aabdfba8fa863b02063e16061c00b16448a6ccc2e13` seleciona `article.questao` e `.concurso-item, .avalia-item` para bancos pontuáveis. Os deltas preservam estrutura e elos, e pela inspeção estática não indicam alteração de digitais ou respostas salvas desses bancos. Não houve teste de navegador nem de armazenamento. A aplicação muda o hash integral e requer verificação do resultado aplicado, integridade dos artigos/código e vínculos, progresso e atualização dos inventários e revalidação localizada dos aceites dependentes. Esta revisão da candidata isolada não comprova aplicação.

## Hashes de evidências

| Evidência SHA-256 | D26 | D27 | D28 |
|---|---|---|---|
| Fragmento original | `5782e55fa0b6b01146e8f1aecc6a39d659b53ff3d23b99ea0f236757801fce1b` | `94f05fbcee63dd51420d6fd57eb3023417cfd3b5b31148b9544fb7dd4ce57267` | `7f2c843eab47d23fa30790386dfbb200c22fa06f1307c56483fee9ac2eab61f0` |
| Fragmento candidato | `a82e00538d8a780dddb23b2699f75fb915b546c308c12fd5d44f6d62a74f1e1a` | `f464a072c29b5744c8fff6663d902628d84e5f8a28f51c68306f3a8a8e242962` | `d19ea80ff8c3ea479fc09548943bb1bed8c40d129ae265f24aec7f04cba162ed` |
| Arquivo original | `4b0d7fbf8f7f18c6287bbed5f1235eea08dc865488ef3112e35a94f039014460` | `fc6573b3ab11591cebe4f7c9a5861010db1a8acb1d26183ce2b577c5fcaca72c` | `8a46ed3c93fbce80dc1ad30c08a501649e7bcc8f85f5f7cbc1457c11421c314f` |
| Arquivo candidato | `cf7c549f37b623338d5155a19eeba01e89575a8e5a49f45cbbc56982ffe15f1b` | `ad1453bc4d440a752197f3294d53b0148002ce00fdbded58c4013af62f6015a1` | `11b15f66c44187f84bb13e77c2cd8a3be3302e9eec9d7005072316c25f1dd7b9` |
| Manifesto JSON | `651d4587ce869dc9fbf3a3cd580cdbd500c763c8babd08bd08cb5035d0d6dc5a` | `915bae559064bfd6063e4727e2bd5910e80bc1994c50c07c54ba0612240ce009` | `01288f9170a79c8a0f6c68166e6a455cf957c914eca19e690d91e5b9700e492d` |

Os arquivos de evidência ficam em `auditoria/termodinamica/evidencias/QA-09/`, com prefixos `diagnostico26-`, `diagnostico27-` e `diagnostico28-`. O parecer não cobre os demais diagnósticos nem o aceite global.
