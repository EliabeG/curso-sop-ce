# QA-09 — apoio independente aos diagnósticos 1–5 da preparação

Data: 29/10/2026. Revisor: agente automatizado `/root/auditoria_av61_70`. Escopo parcial; não aprova QA-09, não libera próximo ID e não altera produto ou controle. Os cinco diagnósticos estão em `modulos/e1-termodinamica.html#preparacao-questoes`, SHA-256 `9ec10053e40640feeb977baea742da3cbe4d546659f772f0256c6b3cb0720a55`. Identifico cada trecho pelo bloco bruto desde seu `<h3>` até imediatamente antes do `<h3>` seguinte, recodificado em UTF-8; inclui o fechamento da caixa e abertura da caixa seguinte, portanto não é hash isolado do `div`.

## Diagnóstico 1 — 7b54fa032ce8fcc93223b08117df60c9e5476fc7a4503ca82b77edd3e09a21c4

**Ocorrência de fração — ajuste proposto:** o enunciado divide amostra homogênea em quatro partes nas mesmas condições, mas não requer massas ou volumes iguais. A afirmação da resposta “cada parte tem um quarto” não decorre dessa hipótese. Contramodelo com frações `0,1`, `0,2`, `0,3`, `0,4`: somam 1, dão quatro porções não vazias e de massas/volumes diferentes, com densidade e temperatura iguais no mesmo estado. `1/4=0,25=25%` por parcela seria exato se a divisão fosse em quatro partes iguais. Sugestão ao Auditor: explicitar essa condição antes da tentativa; não editei o item e não presumo intenção do autor.

**Densidade e unidade:** para cada parcela homogênea com massa e volume na mesma fração `f_i`, `(f_i m)/(f_i V)=m/V`; temperatura permanece no estado indicado. Unidade de base da temperatura termodinâmica é kelvin, símbolo K. Não há valores medidos ou tolerância de medição. Base `#base-medidas`; [BIPM, unidades de base](https://www.bipm.org/en/measurement-units/si-base-units).

## Diagnóstico 2 — c15f8c1904182169be4bdf593b49b1f0bf16879163d59bb3463502b89f6e73d3

**Ocorrência de faixa:** `span=L_sup−L_inf`; `L_sup=(−20 °C)+(150 °C de intervalo)=130 °C`. Conversão de verificação: `−20 °C=253,15 K`, acrescentando intervalo de 150 K obtém-se `403,15 K=130 °C`. Valores do exercício são nominais, aritmética exata; não há incerteza instrumental ou arredondamento informado. **Instrumento:** tubo curvo metálico em manômetro Bourdon indica pressão, não temperatura diretamente. Base `#base-instrumentos`; [NIST, conversão de temperaturas e intervalos](https://www.nist.gov/pml/owm/si-units-temperature).

## Diagnóstico 3 — 8ddc041e836d3dec15482bee1264558069ad35db70e5fb1567418f16f073d387

**Ocorrência de temperaturas:** `20 °C=293,15 K`, `80 °C=353,15 K`, pela soma de 273,15. Massa, composição e volume constantes de gás ideal implicam `p_f/p_i=T_f/T_i=353,15/293,15=1,2046733754…`, não 4. Apresentar `1,205` tem erro `0,000326625…<0,0005`; aumento relativo é `20,4673375…%`, que arredonda para `20,5%` com erro `0,032663` ponto percentual `<0,05`. `80/20=4` é razão dos valores Celsius e não de temperaturas absolutas; não demonstra quadruplicação. Tolerância citada é de exibição, não incerteza experimental. Base `#base-gas-modelo`; [NIST temperatura](https://www.nist.gov/pml/owm/si-units-temperature).

## Diagnóstico 4 — a25be1b0a2beeea1bca3b6a85f429f6d6b5eb96231cd260aa3f49a9d327f4133

**N/A numérico fundamentado:** enunciado e resposta são qualitativos: sólidos vibram e líquidos se movem; alta pressão não garante idealidade, que costuma ser favorecida por baixa densidade e afastamento da condensação. Não há grandeza medida, dado de estado, número ou resultado numérico nessa explicação; o “4” é número de identificação, não grandeza física. Sem tolerância de cálculo aplicável. Bases `#base-molecular`, `#base-gas-modelo`.

## Diagnóstico 5 — 15fa7adaf50a839dda0a0463ac7122fc62e296b790c6f65e787e789e405c0e8e

**Ocorrência de umidade — ressalva a adjudicar:** `75%=0,75`, `30%=0,30`, e `0,30/0,75=0,40`, aritmética nominal exata; isso não equivale a fração mássica da água no ar. A razão de pressões parciais é 0,40 na aproximação `φ=p_v/p_sat(T)` de mistura ideal com fator de intensificação desprezado, explicitada em `#base-umidade`, ou quando a pressão de saturação de referência for a mesma em ambos os estados. Na formulação real de ar úmido, a correção de saturação pode depender da pressão total: a igualdade de temperatura sozinha não a fixa em geral. O enunciado informa apenas mesma T e o comentário não explicita o modelo; a base ligada após a resposta declara a aproximação. Recomendo adjudicar se a hipótese deve ser expressa na própria tentativa. Não há dados para calcular desvio real ou incerteza instrumental. [ASHRAE, psicrometria, capítulo 1](https://handbook.ashrae.org/Handbooks/F21/SI/F21_Ch01/F21_Ch01_si.aspx).

## Limites e atribuição

Não há `img` ou SVG dentro dos cinco trechos identificados. As bases vinculadas foram consultadas para os modelos e condições usados acima; outros números e exemplos dessas seções são ocorrências próprias de QA-09 ainda não cobertas por este registro. Consulta às fontes externas em 29/10/2026. Os cinco exames não constituem cobertura dos demais 23 diagnósticos nem das demais classes. Não foram executados teste com estudantes, certificação externa ou validação empírica de instrumentos. Decisões e eventuais alterações competem ao Auditor principal e Corretor.

Hashes dos trechos das bases, do `<h3>` respectivo até o próximo `<h3>` ou fim da seção, recodificados em UTF-8: `#base-medidas` `960921c8c51256131d11b7cf38722aaa7f8f9f3c0d843d82a193d50489b459d6`; `#base-instrumentos` `ee5616391d9dc3c2849d700712c4f7afaf533b1bdc695ee5b65f2d1e1cb51d98`; `#base-gas-modelo` `c3dc17e696fa8f8710243bea95621797936ca08a1b17f55895e6e05f065ab89f`; `#base-molecular` `502fe86168f4739d37b906c36b63075989b153b6215dd6ae5476a92739f357df`; `#base-umidade` `7287f3e2bac49eb098650532e5193b57893da0aba5f758682c8ca9160911f8f5`. Identidade não equivale a revisão integral das bases.
