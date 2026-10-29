# FON-09 r1 — conferência da origem e substituição dos dados de CR68

27/10/2026. Corretor automatizado: /root/corretor_aaa. Relatório de execução, sujeito ao parecer independente. Escopo: densidade, cinco linhas da tabela e preservação da afirmação/gabarito do item 85.

## Cadeia documental

| Documento | Localização conferida | Resultado |
|---|---|---|
| Prova oficial Cebraspe/Petrobras 2023.2, ênfase 8, aplicação 24/03/2024, código 950_PETROBRAS_23_008_01 | Página 3 de 4 do PDF; texto web e imagem prova-oficial-p3-r1.png efetivamente inspecionada | Já contém 1.000kg/cm³ e as cinco linhas integralmente iguais ao HTML/caderno. Não são erros atribuíveis apenas à transcrição do curso. |
| Caderno fornecido | Página 14 de 31; caderno-p14-r1.png efetivamente inspecionada | Reproduz unidade e todos os números; identifica questões redigitadas e figuras recriadas. Não é fac-símile integral da prova. |
| HTML anterior | Artigo cr-e1-68, bloco cr-e1-68-enunciado; cópia cr68-antes.html | Os cinco conjuntos T/vf/vg e a densidade coincidem com os documentos. O bloco foi preservado literalmente, mas recolhido como transcrição histórica inválida para cálculos. |
| Gabarito oficial definitivo | Página 1; gabarito-oficial-p1-r1.png efetivamente inspecionada | Coluna do item 85 contém C. Nenhuma consequência sobre outros itens, inclusive os que usam dados defeituosos, foi inferida. |

As cópias oficiais obtidas em 27/10/2026 são idênticas por SHA-256 às cópias já existentes em downloads/termodinamica. Os hashes e tamanhos estão em documentos-hashes-r1.json. A renderização das páginas foi feita pelo coordenador com Windows.Data.Pdf, sem alterar PDFs; o Corretor inspecionou as três imagens retornadas. Não há documento de errata oficial identificado nesta entrega. A correção publicada é editorial e não supõe a intenção tipográfica do autor.

## Densidade e comparação integral da tabela

A unidade literal implica 1000/(10^-6)=10^9 kg/m³. O modelo didático alternativo ρ≈1000 kg/m³ deve ser declarado aproximação incompressível; não é valor exato. A consulta NIST WebBook em 25 °C e 101,325 kPa retorna 997,04764 kg/m³ (líquido); desvio relativo da aproximação≈0,29611%. Essa referência não fixa a pressão real dos pontos 1/2 nem usa densidade saturada de 100 °C como se fosse líquido de 25 °C.

As cinco pressões são condições prescritas, convertidas consistentemente para as consultas/tabela. Cada célula física foi comparada à meia unidade da última casa impressa, como teste de compatibilidade de arredondamento, não como estimativa de incerteza experimental.

| p kPa | Grandeza | Original | Referência corrigida | Classificação |
|---:|---|---:|---:|---|
| 101.325 | T_C | 100 | 99.974296 | Compatível com arredondamento |
| 101.325 | vf_m3kg | 0.00104 | 0.0010434411 | Compatível com arredondamento |
| 101.325 | vg_m3kg | 1.695 | 1.6732012 | Incompatível com precisão impressa |
| 150 | T_C | 114 | 111.349 | Incompatível com precisão impressa |
| 150 | vf_m3kg | 0.00108 | 0.00105273 | Incompatível com precisão impressa |
| 150 | vg_m3kg | 0.354 | 1.1593 | Incompatível com precisão impressa |
| 200 | T_C | 128 | 120.21 | Incompatível com precisão impressa |
| 200 | vf_m3kg | 0.00110 | 0.00106052 | Incompatível com precisão impressa |
| 200 | vg_m3kg | 0.206 | 0.88568 | Incompatível com precisão impressa |
| 250 | T_C | 138 | 127.411 | Incompatível com precisão impressa |
| 250 | vf_m3kg | 0.0012 | 0.00106722 | Incompatível com precisão impressa |
| 250 | vg_m3kg | 0.138 | 0.71866 | Incompatível com precisão impressa |
| 300 | T_C | 147 | 133.522 | Incompatível com precisão impressa |
| 300 | vf_m3kg | 0.00114 | 0.00107317 | Incompatível com precisão impressa |
| 300 | vg_m3kg | 0.100 | 0.60576 | Incompatível com precisão impressa |

Resultado: 2 células compatíveis (T e vf da primeira linha), 13 incompatíveis. A tabela histórica não é recomendada parcialmente para novas contas. A tabela corrigida completa fica separada e rastreada. Não se chama erro ao arredondamento legítimo 100 °C ou 0,00104 m³/kg.

## Referência, versão e reprodução

O conjunto assets/termodinamica/fon09-cr68-dados-v1.json conserva originais, valores corrigidos/brutos, exibição, conversões, comparação por célula, fontes/páginas/consultas e hashes. Versão 1.0. Água pura em equilíbrio líquido–vapor; não gás ideal.

- 150/200/250/300 kPa: NISTIR 5078 (1998), Table 2, p. impressa 12 / p. PDF 2, colunas de volume em cm³/g multiplicadas exatamente por 0,001; pressões MPa × 1000. A coluna de volumes foi usada diretamente, sem fabricar dígitos pelo recíproco de densidades arredondadas.
- 101,325 kPa: linha exata ausente da Table 2; consulta direta NIST WebBook com pressão 0,101325 MPa, Type=SatT na API, duas fases. Modelo IAPWS-95 citado pelo serviço. Nenhuma interpolação editorial.
- Densidade: consulta distinta Type=IsoTherm a 25 °C e 0,101325 MPa. Não confundir com o líquido saturado da primeira linha.

Os dois HTMLs primários foram lidos pelo Corretor, com cabeçalhos, valores, fases e referência do modelo. O apoio_fun01 verificou as fontes e documentou consultas em apoio-dados-r1.md. A primeira linha exibida foi arredondada a 0,001 °C, 10^-8 m³/kg para líquido e 10^-4 m³/kg para vapor; demais linhas conservam casas da tabela após conversão. Digits=8 controla apresentação, não prova exatidão física. A mensagem automática do WebBook sobre incremento não mudou a pressão retornada.

## Preservação e alcance

Afirmação 85, alternativas C/E, gabarito C e resolução de emissividade preservados. A afirmação é exibida para julgamento; o contexto documental permanece em details identificado com advertência. O conjunto corrigido não é exigido para responder à afirmação. O bloco cr-enunciado original, imagens, alternativas e gabarito que determinam digitalDoBanco estão intactos: o registro.js das 30 questões iniciais não requer alteração, e a digital do banco será comparada pelo verificador.

FON-09 não conclui FON-01, BAN-10 ou BAN-08 gerais. O inventário registra conferência documental específica de CR68 com esta evidência, mantendo nível, competência, demanda e campo histórico de revisão de gabarito. A ciência e os dados substitutos ainda dependem do parecer do Auditor.

## Dependência técnica autorizada: páginas de PDF

O validador anterior tratava fragmentos de PDF como IDs HTML e rejeitou os links locais #page=14/#page=3/#page=1, embora as páginas existam. O coordenador autorizou corrigir somente esse caso: arquivo com extensão .pdf, fragmento page=N com inteiro positivo seguro e existência do arquivo. Âncoras HTML e outros recursos continuam sendo verificadas normalmente; fragmentos arbitrários de PDF são rejeitados. A quantidade real de páginas não é determinada por essa validação sintática: os três documentos desta entrega foram conferidos visualmente e por contagem na renderização.

O ajuste não modifica o schema ou o contrato dos registros. O contrato existente foi reexecutado em 39 casos (sem alterações de expectativas); 8 casos adicionais verificam PDF válido, página zero/não numérica, fragmento arbitrário, arquivo ausente, âncora HTML válida/ausente e outro tipo de recurso. Resultados em contrato-existente-r1.json e teste-pdf-r1.json. A cópia reexecutar-contrato-r1.mjs só troca a saída CLI por exportação de resultado para o runtime disponível; os fixtures permanecem iguais ao arquivo histórico BAN-02. Não encerra QA-04 nem reabre/encerra BAN-02 por extensão.
