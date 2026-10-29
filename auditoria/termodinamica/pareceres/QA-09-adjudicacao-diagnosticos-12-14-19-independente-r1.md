# QA-09 — adjudicação independente dos diagnósticos 12, 14 e 19, r1

Data: 29/10/2026. Revisor: agente automatizado `/root/adjudicacao_qa09`, independente da implementação. **Decisão localizada: ajustes de suficiência necessários nos três diagnósticos**, para a fotografia indicada. Não há erro aritmético nos modelos ensinados. Este parecer não altera produto ou controle, não aprova QA-09 e não libera outro ID; a avaliação e integração cabem ao Auditor e ao Corretor responsáveis.

## Escopo, critério e identificação

A revisão confrontou comando, solução, bases acessíveis antes da tentativa e contramodelos para as ressalvas de D12, D14 e D19. QA-09 exige conferência de cada ocorrência, de suas hipóteses, fontes e resultados; o preflight não autoriza fechamento por amostragem. O protocolo exige coerência entre enunciado, solução e hipóteses. Os diagnósticos estão na seção 8.2, posterior às bases didáticas, e orientam o estudante a registrar e justificar o modelo e suas condições; os links “Retomar as aulas” estão dentro da solução recolhida. As bases anteriores estão disponíveis antes da tentativa e foram consideradas, mesmo sem supor que o leitor abre o comentário. Resultados são exatos na aritmética dos dados nominais; não se apresenta tolerância instrumental inexistente.

| Material consultado | SHA-256 |
|---|---|
| `modulos/e1-termodinamica.html` | `7541e7c4c8314922992e99e8b62b40342c2d938e6edeac67ef9f74b69f86c17c` |
| `auditoria/termodinamica/PROTOCOLO_AAA.md` | `18f1f299556e8e60c926a1921987f6d2c10cc939aa4aef4487117dc66c344afc` |
| `auditoria/termodinamica/CONTROLE_AAA.json` | `04131e0b345f0437fb7fe3d9491ca9bca8ff091e68f6d0c96455b20461266934` |
| `auditoria/termodinamica/pareceres/QA-09-preflight-independente-r1.md` | `dca3ed8905619c455ed2f843e7983389fb4b94d4524d2b9d6269c825905683b6` |
| `auditoria/termodinamica/pareceres/QA-09-diagnosticos-11-15-apoio-independente-r1.md` | `2c69b7ce19f67cc4e31af0059dddbc348431d527fa34a293b32817e10544d423` |
| `auditoria/termodinamica/pareceres/QA-09-diagnosticos-16-20-apoio-independente-r1.md` | `2dd4f595f7fa3a73eeac4b8bd973df434ee1879ac876b4c98e0b892d0818a922` |
| `auditoria/termodinamica/pareceres/BAN-08-adjudicacao-av52-r1-independente.md` | `82e211ebb30e0e7e58460167429c47730137db9b8e332f1e1ac7d42aeae258fb` |
| `auditoria/termodinamica/pareceres/BAN-07-revalidacao-av42-av45-av52-r1-independente.md` | `86e9edc229e31fa2c798ad5ae1b89d595ddf74b080652f9a435c515517380c08` |

O controle consultado aponta QA-09 `em_correcao`, rodada 1; esse estado é informativo, não uma decisão de aceite. Os fragmentos abaixo são bytes UTF-8 do `div.exemplo` completo, sem acrescentar nova linha. A fotografia dos diagnósticos 12 e 14 no apoio anterior tinha outro hash de HTML; os hashes dos fragmentos permanecem idênticos na fotografia aqui examinada. Não se infere identidade de todas as demais partes.

## D12 — rendimento e consumo auxiliar

Fragmento `618ac9f908af2cd203e8c44ff47708b488aa0e80c61111b4a1e5e082c4e35ca7`. O comando fornece turbina 140 kW, compressor 50 kW e calor recebido 300 kW e solicita rendimento do conjunto. `#base-brayton-real`, anterior ao diagnóstico, ensina explicitamente turbina menos compressor **desprezando outros consumos**. Nesse modelo, com 300 kW como calor total, a conta `Ẇlíq = 140 − 50 = 90 kW`, `η = 90/300 = 30%` está correta. As duas válvulas fechadas na compressão antes de abertura da descarga correspondem ao alternativo convencional ensinado. A admissão de 6 L em deslocamento de 8 L dá 75% na mesma referência de sucção ensinada em `#base-eficiencia-volumetrica`; repetir a referência e a mesma base de ciclo é esclarecimento útil, não a pendência que determina este juízo.

O comando não diz que esses são os únicos consumos nem fixa expressamente o calor como entrada total do conjunto. Um auxiliar de 10 kW, mantendo 300 kW como entrada total e os demais dados, produz líquido de `140 − 50 − 10 = 80 kW` e rendimento de `80/300 = 26,666…%`. Por exemplo, com fontes de 600 K e 300 K, 220 kW rejeitados fecham o balanço e `220/300 − 300/600 = 7/30 kW/K > 0`; a segunda lei não descarta esse contramodelo. O auxiliar e as temperaturas são construção de teste, não dados do produto.

A base mostra um modelo possível e sua condição, mas a exclusão de equipamentos ou transferências em uma instalação particular depende do caso. Essa é a mesma distinção do precedente AV52: ele exigiu que a exclusão do auxiliar e a totalidade do calor fossem comunicadas antes da escolha, embora a mesma base estivesse disponível; a revalidação de BAN-07 conferiu a versão que passou a explicitá-las. **Decisão: ajuste necessário**. Por exemplo, declarar antes da tentativa que os demais consumos são desprezíveis e que 300 kW é a entrada térmica total; manter ou explicitar a definição de potência líquida e conferir a resolução na versão aplicada.

## D14 — face exposta e outras transferências

Fragmento `d31dc8c7929c0d00feccdf2f5baca49b3d957a5cb81c7ce36fd26a68330df849`. O comando informa bloco de `2 × 1 × 1 m`, geração `60 W/m³`, apenas face `2 × 1 m` exposta, `h = 6 W/(m²·K)`, ambiente `18 °C`, regime permanente e ausência de radiação. A solução fala em faces isoladas. A base anterior `#base-geracao-face` apresenta especificamente uma face convectiva, demais faces isoladas, nenhuma outra perda e temperatura superficial uniforme, ou média com h uniforme; também alerta que contato condutor exige mudar o balanço.

Dentro desse modelo, `V = 2 m³`, `A = 2 m²`, geração `120 W`, `ΔT = 120/(6×2) = 10 K` e `T = 28 °C`; o valor é de superfície uniforme ou média na condição indicada, não de todo o bloco. “Apenas a face está exposta” e exclusão da radiação não determinam, por si, a ausência de contato condutivo nas faces restantes. Com `60 W` conduzidos a um suporte e `60 W` pela face exposta, em regime permanente, a mesma geração fecha o balanço e `T̄s = 18 + 60/(6×2) = 23 °C` para h uniforme. O suporte e a transferência são hipotéticos, não fatos da questão.

Aqui a aula identifica o modelo que torna a conta viável, mas também ensina a possibilidade da transferência adicional e o comando não estabelece seu isolamento; essa diferença altera diretamente o resultado, tal como a exclusão de consumo em AV52. **Decisão: ajuste necessário**. Estabelecer no comando que as demais faces são isoladas e que não há outras saídas de calor; especificar temperatura uniforme da face ou pedir a média com h uniforme, ou formulação equivalente coerente com a base e solução. Não se exige bloco isotérmico nem detalhar modos já excluídos pelo modelo.

## D19 — fontes, sumidouros e ar exterior

Fragmento `345887a5a233fa75a098ddabe3540edd95857c6fc0feea4c11b99fb64f44ea71`. O comando dá 20 pessoas a `300 mL/min` cada, excesso permitido de `500 ppm`, regime estacionário e mistura perfeita, e pede a vazão exterior necessária. A base anterior `#base-balanco-co2` explicita mistura, volume/densidade aproximadamente constantes, base volumétrica comum e balanço com fonte interna conhecida **sem outras fontes, reações, remoção ou troca com outras zonas**. No modelo nela apresentado: `G = 6000 mL/min = 0,36 m³/h`; excesso `500×10⁻⁶ = 0,0005`; `V̇ = 0,36/0,0005 = 720 m³/h`. Esse é o mínimo para atender ao limite no modelo, pois a igualdade corresponde ao excesso máximo; vazão maior reduz o excesso.

Uma remoção adicional de `0,18 m³/h`, nas mesmas condições volumétricas, deixa `0,18 m³/h` para a ventilação remover e leva a `0,18/0,0005 = 360 m³/h` no mesmo regime e excesso. Uma fonte adicional produziria resultado maior. Esses termos são contramodelos, não instalações descritas no produto; mistura perfeita e regime permanente, isoladamente, não os excluem. Os valores da base e o diagnóstico usam geração por pessoa, mas o comando não declara que são a geração total nem que não há remoção adicional ou outra zona.

**Decisão: ajuste necessário**, com a mesma lógica de exclusividade de termos do balanço aplicada em AV52 e ao diagnóstico 6; declarar que pessoas são a única geração, sem outras remoções/reações ou trocas com outras zonas, e usar as vazões nas mesmas condições volumétricas. Referir explicitamente o modelo simplificado da base anterior antes da tentativa é alternativa aceitável se identifica sem ambiguidade essas condições para este caso. Não é necessário exigir comportamento universal de um ambiente real ou transformar o exercício em projeto normativo de ventilação.

## Alcance da decisão

A distinção não é exigir que todo diagnóstico repita toda a aula: hipóteses constitutivas de um modelo expressamente ensinado, como idealização de mistura, podem ser herdadas pelo contexto quando não há conflito; já transferências ou fontes adicionais fisicamente viáveis mudam a resposta e não são automaticamente excluídas de um caso particular. As três pendências são de suficiência localizada e não invalidam as contas sob as hipóteses apresentadas. Outra redação que feche os respectivos balanços é admissível mediante confronto independente. Depois da aplicação, conferir texto anterior à tentativa, resolução, hashes da versão efetiva e repercussões nos registros. Não se alegam ensaios com alunos, teste de navegador ou verificação de QA-09 integral; não se libera o próximo ID.
