# Parecer independente — FON-09 r1

**Veredito: AJUSTES_OBRIGATORIOS.** Data: 2026-10-27. Auditor: agente automatizado Auditor AAA, distinto do Corretor. A proveniência e a correção científica dos dados de CR68 atendem ao recorte solicitado. A dependência técnica introduzida nesta rodada falha em dois casos negativos da mesma causa, registrados como **R1-A**. FON-09 permanece aberto e nenhum próximo ID está liberado por este parecer.

Não há outro bloqueador identificado nem verificação pendente nesta auditoria. A reapresentação pode ficar restrita ao parser do fragmento, aos testes pertinentes e aos documentos de entrega/integridade. O conteúdo científico aceito abaixo poderá ser herdado mediante comprovação de preservação.

## Versão examinada

Entrega congelada: [FON-09-r1.md](C:/Users/User/Downloads/SOP-CE/auditoria/termodinamica/entregas/FON-09-r1.md). Manifesto SHA-256: `d054c3eb9a8337c59959eed9e78c2028b9e2c68f36293e3ed8076a3c01fd2b4d`.

Os cinco arquivos correntes foram reconferidos ao fechar este parecer: hashes, tamanhos e cópias em `pacote-r1` coincidem integralmente. A subauditoria conferiu também as 26 evidências e os cinco snapshots anteriores.

| Arquivo | SHA-256 |
| --- | --- |
| `modulos/e1-termodinamica.html` | `6ed5c74f03b2ce449f88e79d143c904442c524166a83afce8f12441d391a6625` |
| `assets/termodinamica/fon09-cr68-dados-v1.json` | `828b967f1318924742e8b30aca8575549301afcccaad395f9ed5bcee2fc46456` |
| `auditoria/termodinamica/inventario/inventario-questoes.json` | `af30160109fa7e9e007e6de74eb1836896194ff90888aec75e0f8a4a86675618` |
| `auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md` | `1505e80c437fdd6dbbea40973155446ec859ba2fb363752217346876a8fb43db` |
| `auditoria/termodinamica/inventario/validar-inventario.mjs` | `114b1a063cb2a88e505c9ecffd2b22c75f29b709419b24e9e533331fa7283b22` |

## Critérios e evidência independente

O aceite original exige conferir a origem de cada erro associado a CR68, identificar a transcrição histórica, oferecer dados corrigidos rastreáveis e impedir o uso da tabela defeituosa como dado físico. O julgamento sobre emissividade deve continuar separado desses dados. A alteração autorizada do validador precisa preservar o contrato anterior e reconhecer integralmente somente o fragmento PDF permitido.

| Critério | Resultado e fundamento |
| --- | --- |
| Origem exata da densidade e das cinco linhas históricas | **Atendido.** Inspeção visual efetiva das imagens da prova oficial, página 3, e do caderno, página 14. A unidade `kg/cm³` e as 15 células já estão na prova; caderno e HTML mantêm esses valores. A origem documental está estabelecida, sem inferir a intenção do autor nem inventar errata oficial. |
| Identidade da questão e gabarito | **Atendido.** A imagem do gabarito definitivo confirma item 85 = C, código `950_PETROBRAS_23_008_01`, prova de 24/03/2024, ênfase 8 — Operação. O caderno apresenta a questão com figura recriada; essa condição está identificada. |
| Transcrição, interpretação e correção distintas | **Atendido.** Enunciado histórico preservado literalmente em bloco identificado; dados inválidos não são apresentados como utilizáveis. Dados físicos corrigidos estão em seção separada, com condições e fontes próprias. O julgamento original sobre emissividade permanece visível. |
| Todas as 15 células confrontadas | **Atendido.** Comparação individual registrada no JSON científico. Duas células da primeira linha são compatíveis com a precisão impressa; as outras 13 são incompatíveis. Os limiares de arredondamento, diferenças e conclusões conferem. Não houve aprovação por amostragem. |
| Fontes e conversões das propriedades de saturação | **Atendido.** Primeira linha obtida diretamente do NIST WebBook a 0,101325 MPa; outras quatro linhas conferidas na Tabela 2 do NISTIR 5078. A primeira linha não é atribuída a uma linha inexistente da Tabela 2. Conversões de MPa para kPa e de cm³/g para m³/kg corretas. |
| Densidade corrigida e hipótese didática | **Atendido.** `1.000 kg/cm³` corresponde literalmente a `10⁹ kg/m³`. A referência independente do NIST a 25 °C e 0,101325 MPa fornece 997,04764 kg/m³. O uso didático de 1.000 kg/m³ é marcado como aproximação, cerca de 0,29611% acima dessa referência, sem atribuir pressão atmosférica aos pontos do dispositivo. |
| Não reutilização da tabela defeituosa | **Atendido no E1.** Busca e leitura dos usos relevantes encontraram os dados defeituosos somente no bloco histórico de CR68. AV68 usa a relação de emissividades e não reaproveita a tabela de água. Dados de saturação não são tratados como propriedades da água a 25 °C. |
| Preservação do item e continuidade | **Atendido.** Enunciado histórico, alternativas, resolução, gabarito e digital `f78a5342` preservados. O comentário de emissividade mantém suas hipóteses. Funções reais de leitura de respostas foram verificadas com armazenamento simulado; isso não equivale a teste com histórico de usuário em navegador. |
| Inventário e delimitação cognitiva | **Atendido.** Os metadados de CR68 distinguem conferência oficial, nota editorial, fontes corrigidas e limites. O comando continua de reconhecimento da emissividade; a ampliação do comentário não eleva artificialmente seu nível. Os 196 demais registros e artigos permanecem intactos. |
| Contrato anterior e nova regra PDF | **Parcial; falha R1-A.** O contrato anterior e os positivos passam. O parser descarta parte do fragmento antes de aplicar a nova regra e aceita dois valores inválidos. |
| Escopo e integridade | **Atendido.** Repor somente o artigo anterior de CR68 reconstrói literalmente o HTML anterior. Infraestrutura compartilhada, schema e demais conteúdos preservados. Não há mudança curricular fora de FON-09 nem aceite de outro ID. |

As referências físicas verificadas para as cinco pressões são:

| Pressão (kPa) | Temperatura (°C) | v líquido (m³/kg) | v vapor (m³/kg) | Fonte |
| ---: | ---: | ---: | ---: | --- |
| 101,325 | 99,974296 | 0,0010434411 | 1,6732012 | NIST WebBook, consulta direta |
| 150 | 111,349 | 0,00105273 | 1,1593 | NISTIR 5078, Tabela 2 |
| 200 | 120,210 | 0,00106052 | 0,88568 | NISTIR 5078, Tabela 2 |
| 250 | 127,411 | 0,00106722 | 0,71866 | NISTIR 5078, Tabela 2 |
| 300 | 133,522 | 0,00107317 | 0,60576 | NISTIR 5078, Tabela 2 |

A tabela publicada usa o arredondamento explicitado na entrega. A conferência externa usou a [Tabela 2 primária do NIST](https://www.nist.gov/document/nistir5078-tab2pdf), página 2 do arquivo separado, página impressa 12. As consultas do WebBook foram obtidas novamente pelo Auditor; as duas respostas HTML e seus hashes estão vinculados na evidência científica. Os valores coincidem com as capturas da autoria, sem pressupor identidade binária dos HTML dinâmicos.

## R1-A — validar o fragmento completo

Em [validar-inventario.mjs:201](C:/Users/User/Downloads/SOP-CE/auditoria/termodinamica/inventario/validar-inventario.mjs:201), a divisão `const [beforeHash, rawFragment] = reference.split('#')` descarta os componentes posteriores ao segundo delimitador. A expressão regular recebe apenas `page=3` nos dois casos abaixo:

```text
downloads/termodinamica/provas/2024-03-24_petrobras-tecnico-operacao-2023-2_prova.pdf#page=3#extra
downloads/termodinamica/provas/2024-03-24_petrobras-tecnico-operacao-2023-2_prova.pdf#page=3#
```

Reprodução: clonar o inventário em memória, acrescentar cada referência isoladamente em `origem.fontes` de CR68 e chamar `validateInventory` com a raiz do projeto. Ambos deveriam ser rejeitados, pois o fragmento completo não é `page=N`. Resultado observado: `ok: true`, `erros: []`. O Auditor principal reproduziu pessoalmente o primeiro caso; o apoio técnico reproduziu ambos. Nenhum inventário em disco foi alterado nesses testes.

**Ajuste obrigatório:** preservar e validar todo o conteúdo após o primeiro `#`, rejeitando os sufixos indevidos. A nova rodada deve incluir os dois negativos acima, a variante codificada, casos PDF positivos e inválidos pertinentes, existência do arquivo e preservação dos casos HTML/outros recursos e do contrato anterior. Não se exige verificar programaticamente a quantidade real de páginas do PDF: essa limitação é declarada e a paginação dos documentos usados foi conferida documentalmente.

O problema não invalida os dados físicos já examinados, mas impede o aceite integral da dependência técnica entregue. Acrescentar a regra ao guia pode ser tratado como melhoria posterior; não é um segundo bloqueador desta rodada.

## Verificações executadas e limites

O [subparecer técnico](C:/Users/User/Downloads/SOP-CE/auditoria/termodinamica/pareceres/FON-09-r1-tecnico.md) registra reprodução por Node REPL de 470/470 verificações entregues, 39/39 casos do contrato anterior e 8/8 casos PDF entregues. A validação corrente encontrou 197 artigos/registros, 15 recursos e 1.072 links locais, sem erros ou avisos. Nos 24 casos técnicos independentes, 22 resultados corresponderam às expectativas e dois expuseram R1-A. A contagem de testes positivos não elimina o contraexemplo.

A leitura visual do Auditor utilizou os três PNGs reais renderizados de PDFs por Windows.Data.Pdf, abertos com ferramenta de imagem. Não foi confundida com resultado textual de screenshot web, OCR ou navegação em PDF. A análise científica compreendeu as 15 células, condições, unidades, fases e a relação com o comando de CR68.

O relato de navegador do coordenador foi examinado como evidência separada: testes funcionais no hash `bd356310…`, seguidos de recarga e conferência da alteração textual final no hash `6ed5c74f…`. Não se afirma repetição integral dos testes funcionais nessa última versão. O relato é coerente com o delta informado. Esta auditoria não executou navegador nem certifica acessibilidade ampla, dispositivos móveis ou continuidade de histórico real de aluno.

Evidências detalhadas:

- [Ciência, fontes, 15 células, densidade e hashes finais](C:/Users/User/Downloads/SOP-CE/auditoria/termodinamica/pareceres/FON-09-r1-ciencia.json).
- [Execuções técnicas, preservação e 24 casos independentes](C:/Users/User/Downloads/SOP-CE/auditoria/termodinamica/pareceres/FON-09-r1-tecnico.json).
- [Relato de navegador do coordenador](C:/Users/User/Downloads/SOP-CE/auditoria/termodinamica/evidencias/FON-09/navegador-coordenador-r1.md).

## Condição da reapresentação e fila

O Corretor deve reapresentar somente FON-09, preservando o pacote r1 e discriminando o delta técnico. A r2 deverá comprovar a correção de R1-A e a identidade dos arquivos científicos e registros já examinados, além de atualizar os hashes e resultados dos testes afetados. Não há motivo identificado para repetir as consultas físicas ou a leitura de cada célula se esse conteúdo permanecer idêntico.

Após o aceite integral de FON-09, não foi identificada dependência que impeça iniciar BAN-10 como próximo recorte: CR09, CR24, CR68 e CR79 são prioridades, e o critério também exige procurar outras ambiguidades durante a conferência. BAN-10 precisará de sua própria conferência documental e decisão sobre uso na nota de domínio. FON-01 e BAN-08 globais permanecem abertos; não são encerrados por esta evidência localizada. Esta análise de dependência não inicia nem aprova BAN-10.

**Decisão final: AJUSTES_OBRIGATORIOS — R1-A. Nenhuma liberação de próximo ID e nenhuma declaração de curso avançado concluído.**
