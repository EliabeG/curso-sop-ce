# QA-09 — auditoria independente localizada de textos e tabela FUN-01

Data: 30/10/2026. Revisor: agente automatizado independente `/root/qa_examples`. **Veredito: AJUSTES_OBRIGATÓRIOS** para esta entrega localizada, pela afirmação de procedência não sustentada no texto da posição 114112. O restante do recálculo abaixo está coerente dentro das hipóteses descritas; não se aprova o lote completo nem QA-09 integral ou outro ID.

## Critério e versão examinada

QA-09 requer inventário e recálculo de todo o conteúdo numérico fora dos 197 artigos. Este parecer restringe-se aos nove textos diretos e tabela identificados em `auditoria/termodinamica/evidencias/QA-09/fun01-textos-tabela-20261030/entrega.md`, SHA-256 `74dbf2700da43d65c1041acd096e8601eeeae5c3c9e057ec2b0b555c5efb19ac`. A fonte efetiva `modulos/e1-termodinamica.html` tem SHA-256 `200f9b773050594d762cc596a5a89297024b245fc4f504081fc77baaed3db95f`; inventário r7 `5090b9897a4698e0ad090f45182afba5880361aabc9fd3c3bdf848d971a85a1a`; dados FUN-01 `a73b4d6140219cbd6b005216bb7a44db0a68b05f21ca51b7ac4b1ca782dd1448`; programa de verificação do Corretor `19f908ce17b9d6646905347514e2d515bad93f9da8aa0c58b8d59ed7a4b0ecc8`.

Independente da narrativa do Corretor, li diretamente o HTML nas posições UTF-16 r7 91881, 92203, 96357, 102086, 105052, 105534, 108659, 114112 e 251734, e recalculei seus hashes de texto direto usando o parser do projeto e a mesma regra de omissão de filhos do inventário. A tabela na posição 111716 foi extraída como HTML bruto e tem SHA-256 `f690a51e46e062591aed6c23d6c01527fe02ca30407caa2118acc964ce42d0dc`. As dez identidades e seus contextos coincidem com o r7; o script do Corretor retornou `ok=true`, mas não é a única base desta análise. Posições dependem da versão e o parser é compartilhado com o projeto; uma edição requer reconciliação.

## Verificações independentes

- Posição 91881: 0,012/4 = 0,003 m³/kg; 3/(3+2) = 0,60 em base molar; 1 cm³/g = 10⁻⁶/10⁻³ = 0,001 m³/kg.
- 92203: 12±3, como limite determinístico, compreende [9,15], que contém valores não maiores que 10. A notação não determina probabilidade.
- 96357: para A⇌2B, reação permitida a T e p fixos, 2×3−6=0 kJ/mol. Condição de estacionariedade sem comprovação de mínimo estável ou cinética; o próprio texto admite a limitação.
- 102086: na mistura saturada a 0,10 MPa, x=0,20 dá v=0,00104315+0,20(1,6939−0,00104315)=0,33961452 m³/kg e h=417,50+0,20(2674,9−417,50)=868,98 kJ/kg, conforme os valores arredondados fornecidos.
- 105052: no modelo de solução ideal da base, pbolha=xA pAsat+(1−xA)pBsat; composições 0,25 e 0,75 dão **175 e 325 kPa**. Valores fictícios não constituem dados reais de mistura.
- 105534: `Tc=647,096 K` e `pc=22,064 MPa` coincidem com [IAPWS R7-97(2012), §3, p. 5](https://iapws.org/technical-guidance/release/IF97-Rev.download). A definição estrita T>Tc e p>pc é a adotada pela unidade.
- 108659: para mistura ideal na mesma T e mesmo padrão de referência, pA=80×0,25=20 kPa e 160×0,125=20 kPa; RT ln(1)=0. Complementares pB=60 e 140 kPa, sem se inferir equilíbrio de B apenas do valor de A.
- 111716: comparei as células do HTML à [tabela 2 do NIST](https://www.nist.gov/document/nistir5078-tab2pdf), pp. impressas 11 e 12. Para pressões 0,10/0,15/0,20 MPa, temperaturas 99,606/111,349/120,210 °C e entalpias hf 417,50/467,13/504,70 e hg 2674,9/2693,1/2706,2 kJ/kg coincidem; os volumes NIST 1,04315/1,05273/1,06052 e 1693,9/1159,3/885,68 cm³/g coincidem após multiplicar por 0,001 m³/kg por cm³/g. O vetor `agua_saturacao` FUN-01 corresponde às células da tabela. Não há alegação de precisão superior à da fonte.
- 114112: **1/0,004 = 250 kg/m³ e ρv=1**; para a mesma amostra, os valores não fornecem duas propriedades termodinâmicas independentes. Porém a frase que afirma que uma medida “foi obtida por inversão da outra” não decorre de tais números. Ver contramodelo abaixo.
- 251734: **8,314 J/(mol·K)** é arredondamento a três casas decimais de 8,314462618… em [CODATA 2022/NIST](https://physics.nist.gov/cuu/pdf/wallet_2022.pdf); erro cerca de 0,000463 J/(mol·K), inferior a 0,0005. Esta observação não revisa o pacote FUN-02 inteiro.

Fontes externas consultadas em 30/10/2026; as páginas/PDFs não foram preservados com hash local neste lote. As contas usam dados nominais; não se alegam tolerâncias experimentais.

## Ajuste obrigatório e contramodelo

Na posição 114112, o enunciado só diz que um relatório apresenta `v=0,004 m³/kg` e `ρ=250 kg/m³`; não declara como os valores foram obtidos. Dois instrumentos poderiam medir independentemente, por exemplo com resultados nominais coincidentes após arredondamento, e ainda assim produzir exatamente os mesmos valores. O produto ρv=1 continua verdadeiro e as propriedades continuam reciprocamente dependentes para a mesma amostra e instante, embora não se possa concluir que uma leitura foi calculada por inversão da outra. A procedência dos valores é uma questão diferente de independência termodinâmica.

Corrigir a frase em candidato isolado de modo que explicite a dependência matemática sem afirmar como a medida foi obtida; preservar o exemplo, a conclusão de que o par não determina o estado e a exigência de propriedade independente. O Corretor deve identificar o fragmento e a versão, apresentar o delta exato e confrontar suas dependências e aceites existentes; a versão aplicada deve ser examinada independentemente. Este ajuste não implica defeito no cálculo 1/v nem permite assumir erro ou acerto de sensores.

| Critério | Resultado |
|---|---|
| Identidade e fonte dos nove textos e tabela | Atendido na fotografia descrita; limites de versões e fontes externos explícitos. |
| Dados da tabela e contas nominais | Conferidos, inclusive conversão de unidades; propriedades fictícias preservadas como tais. |
| Interpretação do texto 114112 | **Não atendido:** origem da medição foi afirmada sem dado. |
| Alteração do produto e revisão da versão corrigida | Não realizadas; necessárias para nova apreciação localizada. |
| QA-09 completo e próximo ID | Não atendido neste lote; seguem pendentes. |

Nenhum teste com alunos, revisão humana ou ensaio de navegador foi executado. O parecer não invalida automaticamente FUN-01 inteiro nem aprova a versão corrigida ainda inexistente; deve-se examinar o impacto localizado no aceite anterior após aplicação.
