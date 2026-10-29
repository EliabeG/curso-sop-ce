# FON-09 — preparação da auditoria independente

Data: 27/10/2026. Agente automatizado: `/root/auditor_aaa`. Estado: **preparação, sem parecer de aceite**. FON-09 é o único ID liberado. Nenhum produto, inventário ou controle foi editado pelo Auditor.

## Critério e recorte

O aceite exige conferir a origem exata dos erros nos dados associados ao CR68, manter transcrição identificada quando necessária e oferecer dados corrigidos rastreáveis, sem reutilizar a tabela defeituosa. O julgamento de emissividade é independente desses dados; corrigir o apoio não determina, por si, mudança de gabarito.

A tarefa pode ser tratada isoladamente. Não requer encerrar FON-01 ou BAN-10 para todo o banco. Os requisitos de um exercício curricular novo do §3.2 não devem ser impostos artificialmente a uma correção documental/física desses dados; identificação, coerência, fontes, reprodução e preservação continuam obrigatórias.

## Achados independentes antes da entrega

Li o conteúdo extraído da [prova oficial, página 3](https://cdn.cebraspe.org.br/concursos/petrobras_23_ntj/arquivos/950_PETROBRAS_23_008_01.PDF#page=3). Tanto a densidade em `kg/cm³` quanto as cinco linhas abaixo já estão nesse documento. O HTML CR68 reproduz esses números. Assim, não se pode atribuí-los exclusivamente à transcrição do curso ou do caderno fornecido. A evidência estabelece onde aparecem, não o processo de produção do erro nem a intenção do autor.

| Pressão / kPa abs | Temperatura / °C | v líquido / m³/kg | v gás / m³/kg |
|---:|---:|---:|---:|
| 101,325 | 100 | 0,00104 | 1,695 |
| 150 | 114 | 0,00108 | 0,354 |
| 200 | 128 | 0,00110 | 0,206 |
| 250 | 138 | 0,0012 | 0,138 |
| 300 | 147 | 0,00114 | 0,100 |

O [gabarito oficial definitivo](https://cdn.cebraspe.org.br/concursos/petrobras_23_ntj/arquivos/GAB_DEFINITIVO_950_PETROBRAS_23_008_01.PDF#page=1) identifica a aplicação de 24/03/2024, o código 950_PETROBRAS_23_008_01 e a ênfase Operação. A extração da linha 81–100 é compatível com 85 = C; a revisão final deve manter a correspondência da coluna, sem inferir anulação do item por erros em dados que ele não utiliza.

A nota atual é insuficiente para fechar FON-09: não identifica documentalmente a cadeia de transcrição nem oferece todas as colunas de todas as linhas corrigidas. A primeira linha e os volumes líquidos também precisam ser confrontados. Divergência deve ser julgada à precisão apresentada: arredondamento legítimo não é automaticamente erro material.

Li a [referência primária NISTIR 5078](https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir5078.pdf), tabela 2, páginas impressas 11–12 (PDF 17–18). As quatro linhas de comparação direta, convertidas de MPa e cm³/g, são:

| p / kPa | Tsat / °C | vf / m³/kg | vg / m³/kg |
|---:|---:|---:|---:|
| 150 | 111,349 | 0,00105273 | 1,1593 |
| 200 | 120,210 | 0,00106052 | 0,88568 |
| 250 | 127,411 | 0,00106722 | 0,71866 |
| 300 | 133,522 | 0,00107317 | 0,60576 |

Essa tabela tem linhas de 0,100 e 0,110 MPa, mas não uma linha literal de 0,101325 MPa. A correção nessa pressão deve identificar uma fonte ou cálculo específico, ou uma aproximação explicitamente demonstrada; não pode apresentar um resultado como transcrição literal inexistente. A tabela 3, página impressa 22 (PDF 28), dá aproximadamente 997,05 kg/m³ a 25 °C e 0,100 MPa, suficiente para distinguir a ordem física da aproximação didática de 1.000 kg/m³. Não se deve chamá-la de valor exato a qualquer pressão. O NIST explica que dígitos tabulados não são declaração de incerteza.

Conversões a conferir: MPa para kPa, fator 1.000; cm³/g para m³/kg, fator 0,001; a expressão literal 1.000 kg/cm³ equivale a 10⁹ kg/m³. A intenção de substituir `cm³` por `m³` é uma interpretação editorial plausível, não uma errata oficial sem documento comprobatório.

## Verificações exigidas na entrega congelada

| Critério | Evidência que será examinada |
|---|---|
| Origem exata | Prova/página/item e caderno/página, com documentos identificados e comparação completa da densidade, cabeçalhos e cinco linhas. Diferenciar coincidência documental de hipótese sobre como surgiu o erro. |
| Transcrição e correção separadas | Texto original claramente identificado; dados físicos corrigidos apresentados como correção editorial, sem alterar silenciosamente o documento oficial ou alegar errata da banca. |
| Densidade | Unidade e ordem de grandeza corretas, referência e condições de temperatura/pressão; aproximação didática identificada. |
| Saturação completa | Conferência de T, vf e vg para as cinco pressões, fase, pressão absoluta, bases e unidades; primeira linha também coberta. |
| Rastreabilidade numérica | Fonte, tabela/página ou versão/algoritmo, entradas, conversões e arredondamentos reproduzíveis. Não importar precisionamento inexistente nem chamar cálculo de transcrição. |
| Julgamento do item 85 | Preservar sua distinção dos dados de apoio e conferir código/coluna no gabarito definitivo; não reaproveitar tabela defeituosa na justificativa de emissividade. |
| Consistência interna | Nota, tabela de apoio, solução, links, recursos, metadados e inventário concordantes; eventuais dados derivados precisam da mesma referência. |
| Não reutilização indevida | A tabela original, se preservada, deve ser inequívoca como transcrição histórica imprópria para cálculo físico; examinar ocorrências/consumidores afetados no E1. |
| Preservação | Artigos e recursos não relacionados preservados; hashes e diferenças da entrega, atualização do registro individual afetado e validação do inventário. Não reexecutar infraestrutura intacta sem motivo. |
| Experiência e limites | Acesso à transcrição e ao apoio corrigido, legibilidade de unidades/cabeçalhos e links; separar inspeção estática, execução numérica e evidência de navegador. |

Não há autorização para mudar o gabarito apenas porque a tabela é ruim, nem para fechar a revisão científica de todo o banco por consequência. Se aparecer discrepância adicional necessária para corrigir os dados deste recorte, ela deverá ser explicitada e resolvida no mesmo gate.

## Identificação e pendências da preparação

HTML de base: `719a53ef86075dd3be9c7d9603faca620ec07416d1e97a5017740abb5b74c01a`.

| Documento local | SHA-256 |
|---|---|
| `assets/questoes-reais-e1/caderno-fornecido.pdf` | `bea6174ad3eee9a6880274597f444a7a20b05663dd4595d722d1a924532153b0` |
| Prova local Petrobras 2023.2 | `54ac87a4aa4f73687e45698a7ee065e4d2331b58862265bef1fa1002abf3f7a3` |
| Gabarito local Petrobras 2023.2 | `93d28c3a53eaf1b102081ba57971ed7b049920c1945bb71b3e14e45cb2ba6071` |

As cópias oficiais recém-obtidas em `evidencias/FON-09/` coincidem byte a byte, por hash e tamanho, com os documentos já disponíveis em `downloads/termodinamica/`. Isso confirma a preservação dos arquivos comparados, não substitui sua leitura.

A leitura acima é de extrações textuais primárias. As chamadas de screenshot web retornaram referências sem pixels; **não foram contadas como inspeção visual**. O runtime de PDF não está configurado e a tentativa de reativar apoio foi impedida pelo limite de threads. A comparação independente da página 14 do caderno continua para a rodada definitiva; o coordenador prepara evidência visual separada. A primeira linha corrigida será conferida conforme o método concreto entregue. Não há aprovação antecipada de nenhum dado ou implementação futura.

Preparação suficiente para aguardar a entrega congelada. O parecer definitivo dependerá dos arquivos efetivamente entregues e da conclusão dessas verificações específicas.
