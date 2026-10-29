# BAN-08 — diagnóstico inicial e plano de auditoria numérica integral

Data: 29/10/2026. Corretor: agente automatizado `/root/inspect_repo`. Estado: **diagnóstico e plano, sem aprovação e sem alteração do produto**. BAN-08 foi liberado pelo coordenador; BAN-07 r3 foi aprovado no alcance de sua versão e não substitui o recálculo de BAN-08.

## Critério e alcance

O critério BAN-08 determina recalcular as **190 resoluções atuais e todas as futuras** com precisão compatível e apresentar registro por ID com solução, resultado, tolerância, fonte e revisor. Uma amostra não fecha o item. A regra comum de §3.2 exige responsabilidade, revisão, data, arquivos, evidências e pendências; conforme o Protocolo AAA, exigências de criação de unidade curricular não se aplicam artificialmente a esta conferência de banco existente. O Auditor independente examinará a versão entregue; o Corretor não aprova sua própria entrega nem libera outro ID.

O [inventário de partida](inventario-numerico-197-r1.json) mapeia os **197 artigos** da versão vigente: 30 Q, 80 CR, 80 AV e sete problemas abertos FUN-01/02. Os sete abertos são incluídos na execução e cobertura como extensão explícita aos 190 previstos no critério, sem fingir que a redação original de BAN-08 diz 197. Os nove estudos críticos CR04/09/24/34/35/39/62/79/80 permanecem sem pontuação e requerem análise das contas e modelos condicionais, não imposição de uma chave física universal.

O artigo de referência é `modulos/e1-termodinamica.html`, SHA-256 `80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0`; inventário JSON SHA-256 `486c53c5aa6c432831599c4eca170e4620d089b4eb15b480dbfb2cbfaf54c9ce`. Os demais hashes de critério, protocolo, parecer e dados FUN estão no inventário. Cada registro inclui hash do artigo, comando, hashes de blocos de solução, hipóteses, recursos e vínculos extraídos, além dos campos de recálculo inicialmente pendentes.

A extração dos [197 registros](inventariar-r1.mjs) usa `parseHtml` e `sha256` canônicos e confere cada hash contra o inventário. Há 155 artigos com algum indicador numérico automático; **isso não é uma contagem de questões numéricas**: rótulos e símbolos podem ser falsos positivos, enquanto números de figuras, fontes, tabelas e MathML podem ser omitidos. Todo ID permanece `NAO_RECALCULADO` até leitura integral. Sem aceitar um item apenas porque seu hash coincide com BAN-07.

## Amostra inicial: teste do método, não aceite

A [amostra inicial](amostra-inicial-r1.json) cobre seis IDs de naturezas diferentes, calculados ou classificados pelo Corretor e ainda sem revisão independente. O [código reprodutível](recalcular-amostra-r1.py) usa `Decimal` com precisão 40, sem invocar calculadores do produto.

| ID | Alcance da amostra | Resultado e limite |
|---|---|---|
| Q01 | Conceitual sem resultado numérico | C: fronteira vedada impede massa, mas permite energia; tolerância não aplicável. |
| Q06 | Equação de gás ideal | p=100 kPa, D; decimais dados fornecem valor exato, com unidades conferidas. |
| CR26 | Balanço com suplemento editorial | ΔU≈1.304,4 kcal, E sob modelo fechado; admite ±0,05 kcal para a casa exibida. |
| CR39 | Conversão em estudo crítico | 350×4,2=1.470 J exatos; C é chave documental, e Kelvin–Planck exige o modelo restrito. |
| AV31 | Conceitual sem resultado numérico | E no modelo de PCS/PCI; tolerância não aplicável e não se presume diferença positiva sem água. |
| FUN01 saturação | **Somente subparte numérica** | x≈0,507494454, h≈1.621,94904 kJ/kg, afastamento≈175,05096 kJ/kg; propriedades da linha local a 0,20 MPa e tolerâncias editoriais preservadas. Demais subpartes continuam pendentes. |

O JSON local de propriedades declara a origem NIST; a amostra não reabriu a publicação original e não converte a tolerância didática de ±1 kJ/kg em incerteza certificada. As fontes externas, páginas e convenções devem ser confrontadas na análise integral dos itens dependentes.

## Execução por lote

1. **Congelar entradas:** para cada lote confirmar hash global, hash de cada artigo, dados/figuras/scripts usados e posição das notas editoriais; registrar revisor de execução e data. Se houver mudança relevante, identificar os IDs atingidos e repetir as análises, sem estender automaticamente o resultado anterior.
2. **Ler o item inteiro:** enunciado, alternativas ou subitens, figuras legíveis e seus dados, solução, comentários, rubrica, base e fontes ligadas. Classificar individualmente como numérico, simbólico/condicional ou sem resultado numérico. A confirmação de não aplicabilidade exige inspecionar também explicações e distratores; código, números de identificação e rótulos não contam como cálculos.
3. **Recalcular:** transcrever dados e fontes, escolher modelo e hipóteses válidas antes da conta, declarar sinais, unidades e bases, calcular independentemente e confrontar cada resultado mostrado, não apenas a letra correta. Incluir resultados intermediários que sustentam a resposta, conversões, arredondamentos, tabelas e operações declaradas nos distratores. Investigar valores que dependam de recurso gráfico ou fonte externa; se não estiverem verificáveis, registrar bloqueio concreto em vez de inventar dados.
4. **Estabelecer tolerância:** usar limites expressos no problema e sua rubrica quando existirem; distinguir incerteza de dados de tolerância didática. Para valor arredondado, registrar precisão e regra de arredondamento, comparando com a meia unidade da última casa apenas quando apropriado; para igualdade simbólica, limites, sinal e alternativas conceituais, descrever critério lógico. Um valor limítrofe exige análise da propagação e não recebe tolerância genérica arbitrária. Verificar todas as alternativas que possam coincidir após arredondar.
5. **Registrar por ID:** conjunto de dados com unidades e fonte/versionamento; derivação ou justificativa de não aplicabilidade; resultado calculado e apresentado; diferença e tolerância; confirmação da chave/rubrica ou ressalva; revisor Corretor, data, método, status e hash; revisor independente e seu parecer quando efetuado. Para CR oficiais, separar transcrição/chave oficial de cálculo autoral ou hipótese editorial; para críticos, documentar cada leitura física relevante sem transformar letra documental em nota.
6. **Problemas abertos:** além de cada valor da solução exemplar, testar a família de respostas e as fronteiras da rubrica, margens de decisão e resíduos, verificando dados dos arquivos e precisão. Alternativas válidas não podem ser rejeitadas porque diferem do exemplo. Para caminhos, fases, equilíbrio ou integrais, reproduzir ao menos os casos e limites que sustentam as decisões, com fórmulas e unidades; não tratar execução do mesmo script autoral como revisão independente.
7. **Discrepância:** classificar se altera resultado, arredondamento, gabarito, comentário, fonte ou apenas apresentação; guardar cálculo oposto, alcance, hash e reprodução. Corrigir somente dentro de BAN-08 e reapresentar o produto efetivamente alterado, verificando impactos de BAN-07, FON e progresso quando pertinentes. Não alterar o produto antes de haver diagnóstico claro; não apagar a evidência da versão anterior.
8. **Controle de cobertura:** gerar relatório automático de unicidade e interseção com o inventário congelado, verificar 30 Q + 80 CR + 80 AV = 190 e sete abertos, sem duplicatas ou ausências. Nenhum campo `PENDENTE` pode contar como executado; contabilizar separadamente numéricos recalculados, simbólicos e não numéricos efetivamente justificados, nove estudos críticos e sete abertos. Rastrear cada resolução futura e reabrir casos cujas fontes ou versões mudem.

## Divisão e responsabilidade

- Lote Q: Q01–30 (30 IDs).
- Lotes CR: CR01–10, 11–20, 21–30, 31–40, 41–50, 51–60, 61–70, 71–80 (80 IDs), preservando as nove decisões de estudo crítico.
- Lotes AV: AV01–10, 11–20, 21–30, 31–40, 41–50, 51–60, 61–70, 71–80 (80 IDs).
- Lote FUN: quatro problemas FUN-01 e três FUN-02, com todos os subitens, famílias e rubricas (sete IDs).

Cada lote terá autor e revisor nomeados, evidência de cálculo reproduzível, fontes e limites; a distribuição concreta de agentes cabe ao coordenador e não é presumida neste planejamento. O Auditor não implementa as correções que está revisando. Um registro cuja análise só esteja herdada de outro trabalho deve identificar o autor anterior e a parcela realmente reconferida; herança sem recálculo não satisfaz o aceite de BAN-08.

A revisão final verifica os 197 registros, as 190 resoluções exigidas pelo critério, as sete abertas adicionadas, todas as discrepâncias e as pendências de fontes e tolerâncias. Exemplos resolvidos, oficinas, 28 diagnósticos e fichas fora dos artigos são escopo de QA-09 e não estão cobertos por este plano de BAN-08; não serão marcados como concluídos por este inventário.
