# QA-09 — recálculo de exemplos de texto e tabela FUN-01, r1

Data: 30/10/2026. Corretor automatizado `/root/qa_oficina`. Estado: **aguardando auditoria independente**, sem alteração do conteúdo. A aprovação deste lote não conclui QA-09. A amostra é constituída pelas ocorrências abaixo, fora dos artigos pontuados segregados no inventário; as outras fórmulas, recursos, exemplos, atributos, explicações e atividades permanecem por revisar. `FUN-01` é usado como localização, não como transferência automática de aceite anterior.

## Identidade

Fonte `modulos/e1-termodinamica.html`, SHA-256 `200f9b773050594d762cc596a5a89297024b245fc4f504081fc77baaed3db95f`; inventário QA-09 r7 `5090b9897a4698e0ad090f45182afba5880361aabc9fd3c3bdf848d971a85a1a`. Nas referências abaixo, as posições são UTF-16, do documento e da fotografia indicados. O script verifica nove nós de texto direto e a tabela nas posições registradas, recompondo o hash de texto direto com os filhos omitidos conforme o inventário. Seu mapa contém os hashes individuais. As unidades e os dados didáticos foram lidos do texto efetivo; cálculos digitados no script não são extração automática e devem ser conferidos pelo auditor.

## Conferência

| Posição r7 | Ocorrência | Resultado e hipótese |
|---|---|---|
| 91881 | Recuperação de volume, base molar e conversão | `0,012/4=0,003 m³/kg`; `3/(3+2)=0,60 mol/mol`; `1 cm³/g=(10⁻⁶ m³)/(10⁻³ kg)=0,001 m³/kg`. A fração molar não é necessariamente mássica. |
| 92203 | Limite determinístico `12±3` | Extremos `9` e `15`; valor maior que 10 não é garantido. Não há distribuição probabilística declarada. |
| 96357 | Reação fictícia `A ⇌ 2B`, `μA=6` e `μB=3 kJ/mol` | `ΔrG=2μB−μA=0 kJ/mol` é estacionariedade da reação permitida, não prova de mínimo estável. |
| 102086 | Água saturada, p=0,10 MPa, x=0,20 | `vf+x(vg−vf)=0,00104315+0,2(1,6939−0,00104315)=0,33961452 m³/kg`; `hf+x(hg−hf)=417,5+0,2(2674,9−417,5)=868,98 kJ/kg`. Dados arredondados na fonte; equivalência termodinâmica de mistura sob equilíbrio e título mássico. Resultados nominais. |
| 105052 | Modelo ideal de componentes fictícios | `pb=xA pAsat+(1−xA)pBsat`; para `pAsat=400`, `pBsat=100 kPa`, xA=0,25 dá 175 kPa e xA=0,75 dá 325 kPa. Os parâmetros são didáticos, não propriedades de uma mistura real. |
| 105534 | Água: constantes críticas | `Tc=647,096 K`, `pc=22,064 MPa` concordam com IAPWS R7-97(2012), §3. A unidade define supercrítico por `T>Tc` e `p>pc`; a igualdade de um limite não atende essa definição estrita. |
| 108659 | Dois reservatórios de mistura ideal | `pAγ=80×0,25=20 kPa`; `pAδ=160×0,125=20 kPa`; `RT ln(20/20)=0`. Com B complementar, `pBγ=60 kPa`, `pBδ=140 kPa`. Igualdade de potencial A não demonstra equilíbrio por B; modelo usa temperaturas iguais e gás ideal. |
| 111716 | Tabela de água saturada | As três linhas conferem com NISTIR 5078 (1998), tabela 2, pp. impressas 11–12; `cm³/g × 0,001 = m³/kg`. Células da aula e vetor `agua_saturacao` do JSON trazem as mesmas propriedades reproduzidas abaixo. |
| 114112 | Parecer sobre `v=0,004 m³/kg` e `ρ=250 kg/m³` | `1/0,004=250`; `ρv=1`. São reciprocais, portanto redundantes para mesma amostra e instante; identificar independência de outro par exige modelo e região. |
| 251734 | `R=8,314 J/(mol·K)` | Aproximação adequada a 0,001 de `8,314462618…`, CODATA 2022; dados FUN-02 são autorais. Não foi auditado aqui o módulo de cálculo FUN-02 inteiro. |

Tabela reproduzida em unidades de aula: `(p MPa, T °C, vf m³/kg, vg m³/kg, hf kJ/kg, hg kJ/kg)` = `(0,10; 99,606; 0,00104315; 1,6939; 417,50; 2674,9)`, `(0,15; 111,349; 0,00105273; 1,1593; 467,13; 2693,1)`, `(0,20; 120,210; 0,00106052; 0,88568; 504,70; 2706,2)`. No PDF NIST os volumes são, respectivamente, `(1,04315; 1693,9)`, `(1,05273; 1159,3)` e `(1,06052; 885,68)` cm³/g. O confronto foi feito com a [tabela NIST](https://www.nist.gov/document/nistir5078-tab2pdf), consultada em 30/10/2026, linhas 0,10 MPa (p. impressa 11) e 0,15/0,20 MPa (p. impressa 12). Os valores críticos foram confrontados com [IAPWS, R7-97(2012), §3](https://iapws.org/technical-guidance/release/IF97-Rev.download), p. 5, e R com [CODATA 2022/NIST](https://physics.nist.gov/cuu/pdf/wallet_2022.pdf). As fontes externas são referências dos dados, não validação de aprendizagem nem prova de precisão dos instrumentos hipotéticos.

## Reprodução e limitações

`node auditoria/termodinamica/evidencias/QA-09/fun01-textos-tabela-20261030/verificar.mjs` retornou `ok=true`, nove hashes de texto direto, um da tabela e checagens de aritmética. Não grava saída; importa o parser do projeto. Ele compara o vetor JSON da tabela com os valores esperados registrados e a fotografia do HTML com a tabela auditada; a correspondência entre a tabela HTML e o PDF depende da leitura independente. O hash do script é `19f908ce17b9d6646905347514e2d515bad93f9da8aa0c58b8d59ed7a4b0ecc8`. JSON FUN-01: `a73b4d6140219cbd6b005216bb7a44db0a68b05f21ca51b7ac4b1ca782dd1448`; script FUN-01: `a0fbdc4e6e7291a563db2362d26f4107ad67f56843e741d96eef8eea5a8d2a88`; JSON FUN-02: `511aac986e9122e5498cdf69609274685791000a19f140a09d539fca01676319`. O script FUN-01 e a totalidade dos JSON não foram recalculados aqui; incluídos como dados de identidade para avaliação posterior. Não houve erro identificado neste recorte, sujeito à conferência independente, nem teste de navegador ou avaliação humana.
