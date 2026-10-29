# QA-09 — adjudicação independente dos diagnósticos 26–28, r1

Data: 29/10/2026. Revisor: agente automatizado `/root/adjudicacao_qa09`, independente do Corretor. **Decisão localizada: ajustes de suficiência necessários em D26, D27 e D28**. Os resultados divulgados estão corretos nos modelos didáticos identificados abaixo. O parecer não altera produto ou controle, não aprova QA-09 e não libera outro ID.

## Alcance e fotografia

Examinei comandos e soluções e as bases anteriores à seção de diagnósticos, além do apoio e precedente D19. A seção 8.2 orienta justificar modelo e condições; links de retomada ficam nas respostas recolhidas, mas as bases já estão acessíveis antes da tentativa. O protocolo exige coerência entre enunciado, solução e hipóteses; o preflight QA-09 exige conferência por ocorrência. O controle consultado indica QA-09 em correção, rodada 1. Os cálculos abaixo usam dados nominais, com igualdade aritmética exata quando indicada; não há incerteza instrumental fornecida. Os contramodelos são construídos para testar suficiência, não dados ou alegações sobre instalações reais.

| Material | SHA-256 |
|---|---|
| `modulos/e1-termodinamica.html` | `7541e7c4c8314922992e99e8b62b40342c2d938e6edeac67ef9f74b69f86c17c` |
| `auditoria/termodinamica/pareceres/QA-09-diagnosticos-25-28-apoio-independente-r1.md` | `0ec6de51c727cf3c47d334600b2d83ff555b8317e17cc9e5c844846208d905cb` |
| `auditoria/termodinamica/pareceres/QA-09-adjudicacao-diagnosticos-12-14-19-independente-r1.md` | `6d8fe05bbf2eab9697d0d331b8b19fa04b964e12d2de0fd07f194a197362d869` |
| `auditoria/termodinamica/pareceres/QA-09-preflight-independente-r1.md` | `dca3ed8905619c455ed2f843e7983389fb4b94d4524d2b9d6269c825905683b6` |
| `auditoria/termodinamica/PROTOCOLO_AAA.md` | `18f1f299556e8e60c926a1921987f6d2c10cc939aa4aef4487117dc66c344afc` |
| `auditoria/termodinamica/CONTROLE_AAA.json` | `04131e0b345f0437fb7fe3d9491ca9bca8ff091e68f6d0c96455b20461266934` |
| `auditoria/termodinamica/pareceres/BAN-08-adjudicacao-av52-r1-independente.md` | `82e211ebb30e0e7e58460167429c47730137db9b8e332f1e1ac7d42aeae258fb` |

Hashes por diagnóstico são dos bytes UTF-8 do `div.exemplo` completo sem nova linha acrescentada. A base `#base-ciclos-variantes` instrui somar todos os trabalhos e o calor exterior e mostra um Rankine sem extração, além de alertar sobre potência auxiliar; ela identifica um aquecedor aberto com balanço de mistura nas condições declaradas. O exemplo `#base-turbina-potencia` usa turbina adiabática e variações de velocidade e altura desprezíveis. `#base-balanco-co2` define o modelo volumétrico bem misturado, vazões compatíveis e ausência de outras fontes, remoções, reações ou troca com outras zonas.

## D26 — totais do ciclo

Fragmento `5782e55fa0b6b01146e8f1aecc6a39d659b53ff3d23b99ea0f236757801fce1b`. O comando informa ciclo sem extrações, trabalhos produzidos `600` e `900 kJ/kg`, consumo de bomba `20 kJ/kg`, calor da caldeira `2400` e do reaquecedor `800 kJ/kg`. Se são todas as entradas e saídas relevantes na mesma base de massa, `w_líq = 600 + 900 − 20 = 1480 kJ/kg`, `q_in = 2400 + 800 = 3200 kJ/kg`, `η = 46,25%` e `q_rejeitado = 3200 − 1480 = 1720 kJ/kg`. É a resposta publicada.

Apesar de o exemplo anterior sugerir essa leitura convencional, ausência de extração não exclui, por si, consumo auxiliar ou fornecimento térmico externo adicional. Com auxiliar de `100 kJ/kg`, mantidos os valores dados e considerando-os o calor total, `w_líq = 1380 kJ/kg`, `η = 43,125%` e rejeição `1820 kJ/kg`. Com reservatórios hipotéticos de 900 K e 300 K, a geração de entropia dos reservatórios é `1820/300 − 3200/900 > 0 kJ/(kg·K)`: a segunda lei não elimina o exemplo. Uma fonte adicional também mudaria o denominador. O precedente AV52 tratou essa exclusividade como condição do caso, mesmo havendo base anterior.

**Decisão: ajuste necessário.** Especificar que os dois trabalhos produzidos e o consumo da bomba são todos os trabalhos relevantes, os dois calores são todo o calor externo recebido, e a rejeição é a transferência líquida de calor restante; manter mesma base de massa para o ciclo. Uma formulação equivalente que feche o balanço é aceitável. Conferir a solução da versão aplicada.

## D27 — estágio após extração

Fragmento `94f05fbcee63dd51420d6fd57eb3023417cfd3b5b31148b9544fb7dd4ce57267`. A expressão “aquecedor aberto nas hipóteses ensinadas” remete ao modelo da aula: estacionário, adiabático, sem trabalho, mudanças cinética/potencial desprezíveis e mistura compatível com a pressão do aquecedor. `y = (700 − 300)/(2300 − 300) = 0,20`; a extração é `2 kg/s` e a vazão restante `8 kg/s`. Essa parte está suficientemente vinculada ao modelo explícito e correta.

O comando acrescenta que um estágio posterior recebe o restante e “tem queda de 250 kJ/kg”, solicitando a potência, mas não identifica explicitamente a grandeza dessa queda nem aplica ao estágio as hipóteses associadas ao aquecedor. Entendendo-a como queda de entalpia e usando o modelo anterior de turbina estacionária adiabática com mudanças cinética e potencial desprezíveis, obtém-se `8 × 250 = 2000 kW`, como na solução. Com a mesma queda de entalpia e vazão, mas perda de calor de `20 kJ/kg`, sem mudanças cinética/potencial, o balanço dá trabalho `250 − 20 = 230 kJ/kg` e potência `8 × 230 = 1840 kW`. Perda térmica não é contradita pelas hipóteses explicitamente vinculadas apenas ao aquecedor.

**Decisão: ajuste necessário para a potência do estágio**, sem alterar o resultado da fração. Identificar a queda como de entalpia e o estágio como turbina em regime permanente, adiabática, com variações cinética e potencial desprezíveis, ou remeter expressamente o estágio ao modelo correspondente da aula antes da tentativa. Não é necessário exigir reversibilidade.

## D28 — balanço transiente de CO₂

Fragmento `7f2c843eab47d23fa30790386dfbb200c22fa06f1307c56483fee9ac2eab61f0`. Com `V = 200 m³`, `V̇ = 500 m³/h`, `Ci = 600 ppm`, `Ce = 400 ppm` e geração `G = 0,20 m³/h`, o balanço simplificado anterior dá `V dCi/dt = 0,20 + 500(0,0004 − 0,0006) = 0,10 m³/h`, portanto `dCi/dt = 0,0005 h⁻¹ = 500 ppm/h`. Para condições mantidas, a concentração estacionária correspondente seria `400 + (0,20/500)×10⁶ = 800 ppm`; não pode ser imposta instantaneamente. Esses resultados estão corretos no modelo da base.

Um sumidouro adicional hipotético de `0,05 m³/h`, nas mesmas condições volumétricas e sem alteração dos dados do comando, dá `(0,20 − 0,10 − 0,05)/200 = 0,00025 h⁻¹ = 250 ppm/h` inicialmente; se mantido, o equilíbrio seria `700 ppm`. Ambiente bem misturado e G declarada não excluem por si essa remoção. A situação segue o precedente D19: a base fornece a condição sem sumidouros, mas o caso deve identificar que ela se aplica quando o termo muda o resultado.

**Decisão: ajuste necessário.** Declarar que, no balanço do ambiente, não há outras fontes, reações, remoções ou trocas com outras zonas e que as vazões são referidas às mesmas condições; alternativamente, remeter antes da tentativa ao modelo simplificado da base de modo que essas condições sejam impostas ao caso. Preservar “para condições mantidas” na interpretação do equilíbrio; não é preciso supor a taxa inicial constante no tempo nem impor um limite normativo de ventilação.

## Decisão e limites

Os três ajustes tratam de condições específicas que mudam o balanço, não da exigência de repetir toda a teoria ou enumerar cenários arbitrários. Após aplicação, verificar os comandos antes da resposta, coerência das soluções, hashes e registros afetados. Este parecer não revisa outros diagnósticos, não é teste de navegador ou de estudantes, e não substitui a verificação completa e a decisão final de QA-09.
