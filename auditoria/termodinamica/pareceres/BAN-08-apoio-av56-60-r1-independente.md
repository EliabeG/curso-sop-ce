# BAN-08 — apoio científico independente AV56–AV60

Data 29/10/2026; autora dos cálculos e revisora: agente automatizado `/root/auditor_ban08_novo`. Exame parcial sem cegamento, sem aprovação global BAN-08 ou liberação de próximo ID. Produto/controle não alterados. Versão dos artigos e bases do curso `modulos/e1-termodinamica.html`, SHA-256 `80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0`; hashes por ID identificam trechos brutos UTF-8 `<article>...</article>`. Todos os artigos são autorais de cinco alternativas, pontuáveis; links CR apontam itens de origem para comparação. Inventário não lista recursos externos para estes cinco. Cálculos com dados nominais não inferem precisão de medição.

Fontes de modelos consultadas em 29/10/2026: MIT OCW Unified, cap. 5 https://ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_5.htm (Brayton); DOE, https://www.energy.gov/hgeo/how-gas-turbine-power-plants-work (usina combinada); OpenStax College Physics §13.3 https://openstax.org/books/college-physics/pages/13-3-the-ideal-gas-law (gás ideal); bases do módulo identificadas abaixo.

## AV56 — E

Hash `392079edd6f95dca04874ac89e9ffaa072beb28605bb71ffb2db4de735cb2881`; bases `#base-comparar-ciclos`, `#base-rankine`. A exaustão da turbina a gás abastece ciclo a vapor; os modelos usuais são Brayton e Rankine, nessa ordem, E. C inverte, A/B/D associam outros ciclos ou equipamentos; nenhum número ou resultado de conta no artigo. Tolerância numérica não aplicável à identificação de modelos.

## AV57 — D

Hash `64d1d119452a69f00cbae2a69c844bd047558d33064fcbd0a7ec7172e4c73f73`; bases `#base-leitura-matematica`, `#base-brayton`, `#base-brayton-real`. Brayton ideal, calores específicos constantes, dado r_p^((k−1)/k)=2: η=1−1/2=0,50=50%, coincidindo com D e comentário. A=100% omite subtração, B=−100% é 1−2, C=0,50%=0,005 (não 0,50), E=200% usa valor 2 como eficiência. Resultados e conversões percentuais exatos nos dados; sem margem de medição inferida.

## AV58 — A

Hash `6a7534ee1978a5572870ce9206be5c77578e5c6f308255f9a4f9fef7230825b3`; bases `#base-leitura-matematica`, `#base-gas-modelo`. Para gás ideal e massa fixa à mesma T, p1V1=p2V2: p2=100×0,20/0,050=400 kPa absolutos; Δp=400−100=300 kPa. C=100×0,050/0,20=25 kPa inverte razão; B=100 supõe pressão constante; D=300 é incremento, E=200 supõe volume reduzido pela metade. A é única correta; todos valores publicados coincidem com operações nominais, comparação exata sem incerteza inventada.

## AV59 — C

Hash `60f53dd036c9dd2bc5b6fadf39576dd736148816b7f378aeec8d1f6009020fc4`; base `#base-valvulas-compressor`. Modelo de compressor alternativo normal: ambas fechadas na compressão anterior à abertura de descarga; esta pode abrir quando pressão interna excede a da linha mais resistência; na admissão a descarga permanece fechada. I e II verdadeiras, III falsa, somente C as seleciona. Não há grandezas quantitativas de pressão, força ou tempo na resolução; tolerância e resultado numéricos não aplicáveis.

## AV60 — A

Hash `bbcb2f5fcba62390bc4b8015b9d417a1a31a018e9028f5e93d1a9f7523786db6`; base `#base-valvulas-compressor`. Reservatório dimensionado armazena e entrega fluido, atenuando pulsações da linha, enquanto a descarga instantânea do cilindro segue alternada. A correta; B impediria suprimento, C elimina indevidamente trabalho de compressão, D impõe pressão atmosférica, E exige vazão contínua universal dentro do cilindro. Não há valores de vazão, volume ou pressão que permitam dimensionar atenuação; tolerância numérica não aplicável.

Nenhuma divergência numérica localizada nestes cinco itens. Não houve teste com estudantes ou certificação externa; este apoio não resolve os demais itens BAN-08.
