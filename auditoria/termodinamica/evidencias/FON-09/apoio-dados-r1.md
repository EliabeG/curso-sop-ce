# FON-09 — dados de referência para a correção de CR68

**Natureza:** apoio de pesquisa ao Corretor, sem parecer de auditoria independente. **Consulta:** 27/10/2026. **Escopo:** água pura, propriedades de saturação em cinco pressões absolutas e referência de densidade do líquido a 25 °C. Esta nota não altera o curso, o inventário, o controle nem o gabarito.

## 1. Conjunto corrigido recomendado

`vf` representa o volume específico do líquido saturado; `vg`, o do vapor saturado. Ambos são volumes por massa, em m³/kg. A temperatura é a de saturação correspondente à pressão absoluta de cada linha.

| Pressão absoluta (kPa) | Temperatura de saturação (°C) | vf (m³/kg) | vg (m³/kg) | Proveniência da linha |
| ---: | ---: | ---: | ---: | --- |
| 101,325 | 99,974296 | 0,0010434411 | 1,6732012 | NIST Chemistry WebBook SRD 69, consulta de saturação por pressão, resposta bruta preservada; §3 |
| 150 | 111,349 | 0,00105273 | 1,1593 | NISTIR 5078, Table 2, página impressa 12; §2 |
| 200 | 120,210 | 0,00106052 | 0,88568 | NISTIR 5078, Table 2, página impressa 12; §2 |
| 250 | 127,411 | 0,00106722 | 0,71866 | NISTIR 5078, Table 2, página impressa 12; §2 |
| 300 | 133,522 | 0,00107317 | 0,60576 | NISTIR 5078, Table 2, página impressa 12; §2 |

Esta tabela preserva os dígitos recebidos de cada fonte para permitir conferência. Não implica que as propriedades físicas tenham a mesma incerteza ou precisão em todas as linhas. Se o curso preferir uma apresentação menos extensa, a primeira linha pode ser exibida como **99,974 °C; 0,00104344 m³/kg; 1,67320 m³/kg**, mantendo os valores brutos nesta evidência e declarando o arredondamento.

As quatro últimas linhas são transcrições numéricas com conversão de unidades; a primeira é resultado calculado pelo serviço primário NIST. **Não atribuir a primeira linha à tabela impressa e não rotular o conjunto inteiro como transcrição literal de uma única tabela.** Não foi feita interpolação.

## 2. Fonte impressa, localização e conversões

Fonte primária: Allan H. Harvey, *Thermodynamic Properties of Water: Tabulation from the IAPWS Formulation 1995 for the Thermodynamic Properties of Ordinary Water Substance for General and Scientific Use*, NISTIR 5078, outubro de 1998. A [página institucional do relatório](https://www.nist.gov/srd/nistir-5078) descreve a tabulação baseada na formulação IAPWS-95. A data de atualização da página institucional não altera a edição de 1998 do relatório.

A [Table 2 — Saturation (Pressure)](https://www.nist.gov/document/nistir5078-tab2pdf) tem cinco páginas de PDF, correspondentes às páginas impressas 11 a 15. As linhas abaixo estão na **página impressa 12, segunda página do PDF, índice 1 quando contado a partir de zero**. [Arquivo PDF direto](https://www.nist.gov/system/files/documents/srd/NISTIR5078-Tab2.pdf#page=2).

| p original (MPa) | t original (°C) | vL original (cm³/g) | vV original (cm³/g) |
| ---: | ---: | ---: | ---: |
| 0,15 | 111,349 | 1,05273 | 1159,3 |
| 0,20 | 120,210 | 1,06052 | 885,68 |
| 0,25 | 127,411 | 1,06722 | 718,66 |
| 0,30 | 133,522 | 1,07317 | 605,76 |

O cabeçalho original do volume é **cm³/g**, enquanto o da densidade é **kg/m³**. Não confundir essas duas colunas. Os espaços de agrupamento de dígitos do PDF, como em `1.052 73`, foram removidos sem mudar os números.

Conversões exatas usadas:

\[
1\,\mathrm{MPa}=1000\,\mathrm{kPa},\qquad
1\,\mathrm{cm^3/g}=\frac{10^{-6}\,\mathrm{m^3}}{10^{-3}\,\mathrm{kg}}
=10^{-3}\,\mathrm{m^3/kg}.
\]

Exemplo reproduzível: a 150 kPa, `vf = 1,05273 × 10⁻³ = 0,00105273 m³/kg` e `vg = 1159,3 × 10⁻³ = 1,1593 m³/kg`. Foi usada diretamente a coluna de volumes; não se calculou o recíproco das densidades arredondadas da tabela para produzir dígitos adicionais.

O fator de conversão é exato, mas os valores de entrada são tabulados e arredondados. Uma temperatura impressa com três casas decimais não é, por esse motivo, uma medição com incerteza de 0,001 °C.

## 3. Ponto de 101,325 kPa: cálculo primário do WebBook

A Table 2 impressa **não contém 0,101325 MPa**. Na página impressa 11, primeira página do PDF, aparecem os pontos vizinhos 0,10 MPa, a 99,606 °C, e 0,11 MPa, a 102,292 °C. Substituir a linha procurada pela de 100 kPa mudaria o estado; uma interpolação exigiria declaração explícita e avaliação de sua aproximação. A consulta direta abaixo elimina essa necessidade.

Fonte primária: [NIST Chemistry WebBook — Thermophysical Properties of Fluid Systems](https://webbook.nist.gov/chemistry/fluid/), água, identificador `C7732185`. [Consulta reproduzível de saturação a 0,101325 MPa](https://webbook.nist.gov/cgi/fluid.cgi?Action=Load&ID=C7732185&Type=SatT&Digits=8&PLow=0.101325&PHigh=0.101325&PInc=0.001&RefState=DEF&TUnit=C&PUnit=MPa&DUnit=kg%2Fm3&HUnit=kJ%2Fkg&WUnit=m%2Fs&VisUnit=uPa%2As&STUnit=N%2Fm).

Parâmetros que definem o estado: `Type=SatT`, `PLow=0.101325`, `PHigh=0.101325`, `PUnit=MPa`, `TUnit=C`; `Digits=8` controla a apresentação. **Nesta interface, `SatT` produz saturação por incrementos de pressão**: o título da resposta é “Saturation Properties for Water — Pressure Increments”. Não inferir o significado da consulta apenas pelo nome abreviado do parâmetro.

| Fase indicada na resposta | T (°C) | p (MPa) | ρ (kg/m³) | v (m³/kg) |
| --- | ---: | ---: | ---: | ---: |
| liquid | 99,974296 | 0,10132500 | 958,36750 | 0,0010434411 |
| vapor | 99,974296 | 0,10132500 | 0,59765677 | 1,6732012 |

O serviço apresentou uma mensagem automática sobre ajuste do incremento para limitar o número de pontos. A resposta efetiva contém **um par líquido/vapor à pressão solicitada**, 0,10132500 MPa; os resultados acima foram lidos nessas linhas, sem assumir que o incremento solicitado tivesse sido mantido. A consulta foi obtida por HTTP e salva integralmente, incluindo cabeçalhos das tabelas, fases, referências e notas do serviço.

A resposta identifica como base termodinâmica a formulação IAPWS-95, com referência a Wagner e Pruß (2002), [DOI 10.1063/1.1461829](https://doi.org/10.1063/1.1461829), e à revisão de 2016 da liberação IAPWS. Isso é resultado de um modelo de propriedades disponibilizado pelo NIST, não uma nova medição feita nesta revisão. Os oito dígitos solicitados ao serviço não demonstram oito dígitos de exatidão física.

## 4. Densidade a 25 °C: estado real de referência e aproximação didática

Foi realizada uma segunda [consulta primária ao WebBook, isotérmica a 25 °C e 0,101325 MPa](https://webbook.nist.gov/cgi/fluid.cgi?Action=Load&ID=C7732185&Type=IsoTherm&Digits=8&T=25&PLow=0.101325&PHigh=0.101325&PInc=0.001&RefState=DEF&TUnit=C&PUnit=MPa&DUnit=kg%2Fm3&HUnit=kJ%2Fkg&WUnit=m%2Fs&VisUnit=uPa%2As&STUnit=N%2Fm). Parâmetros relevantes: `Type=IsoTherm`, `T=25`, `TUnit=C`, `PLow=PHigh=0.101325`, `PUnit=MPa`. A resposta identifica a fase como líquido.

| T (°C) | Pressão absoluta (kPa) | Densidade retornada (kg/m³) | Volume específico retornado (m³/kg) |
| ---: | ---: | ---: | ---: |
| 25,000000 | 101,325 | 997,04764 | 0,0010029611 |

Para texto didático, **ρ ≈ 997,05 kg/m³ a 25 °C e 101,325 kPa absolutos** é uma referência adequada deste modelo. O valor **1000 kg/m³** pode ser adotado como aproximação explícita de líquido incompressível para os cálculos do exercício. Não o apresentar como valor exato da água a 25 °C.

O desvio relativo da aproximação em relação ao valor de referência é reproduzível:

\[
100\frac{1000-997{,}04764}{997{,}04764}=0{,}29611022398\ldots\%.
\]

Essa diferença é pequena para alguns modelos didáticos; sua aceitabilidade depende da tolerância e do propósito do cálculo. Já a unidade literal `1000 kg/cm³` corresponderia a **10⁹ kg/m³**, um milhão de vezes `1000 kg/m³`. Corrigir a unidade e declarar a aproximação são duas operações diferentes.

O valor de referência acima vale no estado explicitamente consultado. Não é a densidade saturada da primeira linha do §1, cujo líquido está próximo de 100 °C, nem estabelece automaticamente a densidade exata em ambos os lados da bomba de CR68, onde a pressão muda. Para conservar `1000 kg/m³` em vários estados, o curso deve dizer que adotou a aproximação incompressível do problema.

## 5. Aplicação a CR68 e limites desta evidência

Na leitura do artigo `cr-e1-68`, a tabela incorporada ao curso continha os seguintes pares `T; vf; vg`, nas unidades °C e m³/kg: `100; 0,00104; 1,695` a 101,325 kPa; `114; 0,00108; 0,354` a 150 kPa; `128; 0,00110; 0,206` a 200 kPa; `138; 0,0012; 0,138` a 250 kPa; `147; 0,00114; 0,100` a 300 kPa. Esses são os dados observados no HTML do curso, não dados recomendados para reutilização.

A comparação com o §1 confirma que a tabela do artigo requer correção ou separação inequívoca como transcrição histórica com erros. A referência a 101,325 kPa não deve tratar 100 °C como igualdade exata, embora esse arredondamento possa ser explicitamente adotado em um exercício. Os valores de vapor das linhas seguintes têm discrepâncias muito superiores a simples diferenças de arredondamento.

Esta pesquisa não realizou a comparação documental entre o caderno fornecido, a prova oficial e a transcrição do HTML. Portanto, **não atribui a origem de cada erro à banca, ao caderno ou à transcrição**. Essa atribuição exige a evidência documental específica preparada pelos responsáveis por essa comparação. A presente nota fornece o conjunto substituto e a rastreabilidade científica, uma parte do critério FON-09.

O item de CR68 julga uma afirmação sobre emissividade e perda de calor por radiação. Corrigir a densidade ou a tabela de saturação não altera, por si só, o julgamento desse item; qualquer explicação ou manutenção do gabarito deve se apoiar no enunciado e na física da radiação correspondentes. Esta nota não valida integralmente CR68, nem encerra o critério FON-09.

## 6. Evidências locais e reprodução

Respostas brutas preservadas nesta mesma pasta, obtidas do domínio oficial `webbook.nist.gov` em 27/10/2026:

| Arquivo | Conteúdo | SHA-256 |
| --- | --- | --- |
| `apoio-webbook-saturacao-101325.html` | Resposta completa de saturação por pressão | `ccbfe0998477db30e1acd2c81acb035df65e5aea580dd8147accb5b6f4d88b34` |
| `apoio-webbook-densidade-25c-101325.html` | Resposta completa da isotérmica a 25 °C | `7bc6b02309d877723dd721a9eab8f9f2ee817d8fa2008c7b4c7de12373f5a01e` |

Os hashes identificam os arquivos de evidência salvos em UTF-8. A representação HTML de uma futura consulta pode mudar sem que os valores físicos mudem; a comparação de reprodução deve conferir os parâmetros, unidades, fases e números, além de preservar a nova resposta.

Para reproduzir: abrir as duas consultas parametrizadas dos §§3–4; confirmar as unidades escolhidas e as linhas de estado devolvidas; comparar os números com as respostas salvas. Para as outras quatro pressões, conferir a página 12 da Table 2 e multiplicar os volumes em cm³/g por 10⁻³. Nenhum PDF existente foi alterado por este apoio.

**Conferências executadas:** leitura dos cabeçalhos e linhas da fonte primária; verificação da localização das quatro pressões na tabela impressa; ausência do ponto exato de 101,325 kPa nessa tabela; extração das linhas numéricas dos dois HTMLs primários salvos; conversão dimensional exata; cálculo do desvio de densidade; identificação das fases e separação entre saturação e líquido a 25 °C. A leitura da tabela impressa usou o texto do PDF disponibilizado pelo NIST; as respostas WebBook foram verificadas em seu HTML retornado.
