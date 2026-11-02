# QA-09 — auditoria independente da aplicação de quatro candidatas

Data: 30/10/2026. Revisor: agente automatizado independente `/root/qa_diagnosticos`. **Veredito: APROVADO para a aplicação localizada das quatro alterações na versão examinada**, sem pendência obrigatória identificada nesse alcance. QA-09 não está concluído; o próximo ID não é liberado.

## Critério, versão e alcance

QA-09 exige inventário e recálculo de todo o conteúdo numérico fora dos 197 artigos de BAN-08, incluindo exemplos, oficinas, diagnósticos, fichas, figuras e explicações. Este parecer examina somente a aplicação das candidatas previamente revisadas, seus quatro trechos efetivos, as fotografias, o mapa e o impacto localizado sobre os aceites afetados. Não é aceite integral de QA-09 ou de uma nova unidade curricular.

A entrega do Corretor `auditoria/termodinamica/evidencias/QA-09/aplicacao-razao-percentual-r1/entrega-r1.md` tem SHA-256 `e1d4fca90cd8af4e9b81187952c4322795a649b58fbd415dbd75d030a6841b5c`. HTML anterior `200f9b773050594d762cc596a5a89297024b245fc4f504081fc77baaed3db95f`; HTML efetivo `57b13f0d6386764f1cc46ce543013b0eb75f7bfa97ffbd63ea331f38bfc5af8c`; inventário r7 `5090b9897a4698e0ad090f45182afba5880361aabc9fd3c3bdf848d971a85a1a`, r8 `ae75a258398c385398567457d98ebd49b9838c0c9a4eedc69ea8d2d72981b687`, e mapa `37d48a92165de1e29573b3ed5af992bd16df9a5da71b8372576fd84f0e6657fc`. Inventário oficial JSON efetivo `554608968c6fa031fd13a008215dba4c825377422d68bfc5a74db33667756b2c` e Markdown `67f48c9dc02a3e329f75ee356aa521c6288b37f5ca096fc30fae7a67ba916620`.

## Reconstrução e recálculo

Fiz leitura separada dos quatro pares de fragmentos e de suas manifestações anteriores, sem executar o aplicador que grava arquivos. Cada original ocorre uma única vez na fotografia anterior; cada candidata ocorre uma vez no HTML atual e o original correspondente não aparece. Os hashes dos fragmentos sem a quebra final conferem com a configuração e os pareceres. Substituindo os quatro pares na fotografia anterior, a reconstrução coincide **byte a byte** com o HTML efetivo e a fotografia `depois.html`; não há outras alterações nesse HTML no delta examinado.

1. **Razão percentual:** a versão efetiva exige X₁>0 para chamar X₂/X₁=1,4 de aumento de 40% e X₁>0, X₂<X₁ para a fórmula de redução. Em 100→140, (140−100)/100=40%; em 100→70, (100−70)/100=30%. O contramodelo anterior −10→−14 está fora do domínio declarado e a divisão por zero fica excluída.
2. **Fração molar e mássica de vapor:** com β=nᵥ/(nₗ+nᵥ), mᵥ=nᵥM̄ᵥ e mₗ=nₗM̄ₗ, a expressão aplicada é `x=βM̄ᵥ/[(1−β)M̄ₗ+βM̄ᵥ]`. Para duas fases presentes e massas molares médias positivas, `x−β=β(1−β)(M̄ᵥ−M̄ₗ)/[(1−β)M̄ₗ+βM̄ᵥ]`, de modo que a igualdade depende da igualdade das médias; nos limites β=0/1, x=0/1. Com β=0,4 e médias 20/40 g/mol, x=8/(8+24)=0,25. O texto não confunde x_A com título.
3. **v e ρ:** 1/(0,004 m³/kg)=250 kg/m³ e ρv=1. Para a mesma amostra, as propriedades são reciprocamente dependentes; a versão efetiva não afirma que uma medição foi calculada a partir da outra, fato que os dados não demonstram. Não se infere precisão de sensores ou região de fase dos valores centrais.
4. **EX-031:** para cada equipamento, no modelo estacionário e com energias cinética/potencial desprezíveis, q−w=Δh. As hipóteses aplicadas excluem trabalho adicional nos três equipamentos térmicos, ao passo que bomba e turbinas são adiabáticas. Assim q_caldeira=3.100−210=2.890, q_reaquecedor=3.200−2.500=700, rejeição=2.200−200=2.000 kJ/kg; turbinas=1.600 e bomba=10 kJ/kg; trabalho líquido=1.590, entrada=3.590 kJ/kg, fechamento 3.590−2.000=1.590 e eficiência=1.590/3.590≈44,29%. Valores didáticos não garantem estados ou viabilidade real do ciclo.

## Estrutura, mapeamento e revalidação localizada

Além da reconstrução, um segundo parser (`lxml`) encontrou os 197 artigos com IDs e conteúdo serializado iguais e na mesma ordem. Os 197 registros individuais do inventário oficial são idênticos aos da fotografia anterior; apenas a chave `fonte` do JSON mudou. O teste canônico de inventário retornou `ok=true`, com 197 itens/artigos, 29 recursos e 1.263 links locais; o verificador da entrega também retornou `ok=true`. O teste de persistência, inspecionado antes da execução, passou nos seis cenários de BAN-08, usando funções reais com DOM e armazenamento simulados; não é navegador real.

Comparei os 11.396 pares r7/r8, seus IDs, hashes, documento, tipo, tag, seção, âncora e deslocamentos esperados fora das quatro regiões alteradas: 7.186 IDs mudaram e oito hashes mudaram. Destes oito, três são seções ancestrais, três são os textos de percentual e FUN-01, e dois são o bloco EX-031 e seu parágrafo inicial. Examinei os 18 nós com início dentro dos blocos: todos têm a mesma ordem, tipo e contexto; cinco hashes diferem nos trechos efetivamente editados e os demais correspondem a conteúdo preservado. Isso é associação localizada, não aceite automático dos demais nós.

Os 815 registros de referências preservam metadados de conteúdo e suas posições iniciais acompanham os deslocamentos esperados; os 138 registros de recursos preservam campos e hashes exceto as referências ao próprio HTML atualizado. As listas de 197 artigos segregados e os seis ativos específicos do r7/r8 coincidem. Igualdade de hash e contagem não prova qualidade de fontes ou conteúdo visual. O ledger esparso r7 permanece válido somente para sua fotografia anterior e não deve ser apresentado como ledger atual sem reconciliação.

A preservação dos artigos e registros, dos arquivos de script e dos ativos FUN-01, somada à inspeção dos quatro deltas, não revelou impacto localizado sobre questões, gabaritos ou os blocos de FUN-01 já aceitos além das duas explicações corrigidas. Os efeitos examinados são compatíveis com os objetivos de independência de propriedades e distinção de bases da unidade. Isso sustenta uma **revalidação localizada**, e não transfere automaticamente todos os aceites de BAN-02/07/08 e FUN-01 para o hash novo nem reavalia integralmente seus critérios. Dependências e demais apresentações permanecem sujeitas a QA-09.

| Critério localizado | Resultado |
|---|---|
| Candidatas e versão efetiva | Atendido: reconstrução fiel das quatro substituições e hashes. |
| Cálculos, interpretação e hipóteses | Atendido nas quatro alterações e modelos descritos. |
| Artigos, inventário, referências e recursos afetados | Atendido no alcance estrutural descrito; persistência apenas simulada. |
| Mapa e consequências sobre aceites | Conferência localizada realizada, com ressalvas de conteúdo, dependências e versões. |
| Critério integral QA-09 e liberação de outro ID | Não atendido; permanecem bloqueados. |

Não houve ensaio em navegador real, teste com alunos, revisão humana ou certificação externa. A aprovação localizada não demonstra que o curso como um todo tenha alcançado o nível avançado.
