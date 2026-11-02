# QA-09 — auditoria independente de quatro figuras inline, r1

Data: 30/10/2026. Revisor: agente automatizado independente `/root/qa_diagnosticos`. Veredito: **APROVADO para a conferência localizada das quatro figuras descritas abaixo**, com os limites desta análise. Não é aprovação de QA-09 integral e **não libera o próximo ID**.

## Critério e escopo

QA-09 exige que todo conteúdo numérico além dos 197 artigos, inclusive valores em figuras e explicações, seja inventariado, referenciado e recalculado. Examinei apenas as quatro figuras inline fora desses artigos no módulo E1, suas marcações e os textos adjacentes; a regra comum de produção curricular não é declarada cumprida por esta conferência. A revisão não abrange figuras contidas nos 197 artigos, SVG externo FUN-02, demais ativos, conteúdo dinâmico, teste em navegador, acessibilidade integral, uso por estudantes ou todos os outros itens QA-09.

## Identidade e procedimento

`modulos/e1-termodinamica.html` SHA-256 `200f9b773050594d762cc596a5a89297024b245fc4f504081fc77baaed3db95f`; `inventario-r7.json` SHA-256 `5090b9897a4698e0ad090f45182afba5880361aabc9fd3c3bdf848d971a85a1a`. O relatório do Corretor `auditoria/termodinamica/evidencias/QA-09/figuras-inline-corretor-r1/relatorio.md` tem SHA-256 `2acbfd85c37dcf493445f8583d3e313ea43278e80ec5b61e8347875cc19c21db`.

Com extração independente do HTML por parser, encontrei quatro elementos `figure` sem ancestral `article`; os quatro `svg` são filhos dessas figuras, não outras quatro figuras. Recalculei os SHA-256 dos oito fragmentos originais usando os intervalos UTF-16 de r7, com concordância individual. Inspecionei os elementos SVG originais, rótulos, setas, `title`, `desc` quando existe, legenda e texto envolvente, e examinei a imagem produzida pelo Corretor `figuras-renderizadas.png` SHA-256 `3d81c217303c950277b97857c174c24cff6357b69e4c6b589818ca7ab0907aca`. A renderização auxiliar é compartilhada e não uma segunda renderização independente; a conferência de conteúdo e cálculos foi independente a partir do HTML efetivo. Não avaliei a apresentação real no navegador ou tecnologia assistiva.

## Recálculos e verificações

1. **Ciclo p–V**: figura 170720, SHA `382679b6d7c5a390a660ba6d004bd90e31a7b40c5199a0134f6f4c94df68d677`; SVG 170743, SHA `a8211a295b3e3b075b4500a3bd85c9fc0c1fbe02e3a129f7f291856abcbfd314`. Os vértices e setas correspondem a A(1 m³,200 kPa) → B(3,200) → C(3,100) → D(1,100) → A. Usando pressão na fronteira e trechos quase estáticos, W_AB=200×2=400 kJ; W_BC=W_DA=0; W_CD=100×(−2)=−200 kJ, então **W_líquido=+200 kJ**. O ciclo fecha propriedades; sob o balanço fechado com ΔEc=ΔEp=0 e sem outros trabalhos, Q_líquido=+200 kJ. A legenda informa unidades e desenho sem escala. Não inferi grandeza pela dimensão gráfica.
2. **Dois caminhos**: figura 197418, SHA `eac47b40277fcad7474a4e766a905babeea45796f91031303cb36e32ed557703`; SVG 197441, SHA `58457dad7dc1533e29ad859cf5e0d47cbb44729fe336947d3756ebfdfad2a3a1`. A(1,300)→C(3,300)→B(3,100): W=300×(3−1)=**600 kJ**; A→D(1,100)→B: W=100×(3−1)=**200 kJ**, com verticais sem trabalho de fronteira. Para a mesma massa de gás ideal, p_AV_A=p_BV_B=300 kPa·m³, logo T_A=T_B e ΔU=0. Com somente trabalho de fronteira e energias cinética/potencial desprezíveis, Q líquido em cada caminho é igual ao trabalho respectivo. A figura, descrição, setas e exemplo adjacente concordam; um trecho isocórico não é necessariamente adiabático.
3. **Mistura de líquidos**: figura 208328, SHA `e9e3a1ac563e8c82462083d29ed4dbd7df725ef9ccc725c9f5d733af022ac282`; SVG 208351, SHA `204d3cd9183e0db2843be6e51ee2bb2b954a4e488e24024ccc1f504bb54b2966`. Para mesmo líquido, c constante e recipiente desprezível, sem troca externa, reação, mudança de fase ou trabalho relevante, 1c(T_f−20)+3c(T_f−60)=0, resultando **T_f=50 °C** e massa final **4 kg**. O balanço dá 30c recebido pela parte fria e 30c cedido pela quente em unidades coerentes. Rótulos e descrição correspondem ao modelo e dados; o desenho mostra mistura fechada, não regime permanente.
4. **Compressor alternativo**: figura 401445, SHA `ad673ba3750acb066643ddaeff915bf69e0cb23972b909f732b0dc51161290c7`; SVG 401468, SHA `c6a119d5b2049302f76bd26426306a6c082afb8df8d1c353ed06313d18e0ca82`. O traçado e setas indicam 1→2 compressão com ambas as válvulas fechadas, 2→3 descarga aproximadamente à pressão de descarga, 3→4 reexpansão com válvulas fechadas e 4→1 admissão aproximadamente à pressão de sucção. Há volume mínimo positivo. Os números 1–4 são identificadores de estado, não medições. Concordam legenda, descrição e tabela adjacente, no modelo esquemático; não há grandeza física numérica a recalcular nessa figura.

As contas exatas acima usam valores nominais dos materiais didáticos; não foi declarada precisão instrumental. Os exemplos não dependem de alegar medição ou fonte de propriedades reais. A correspondência das figuras com um modelo idealizado não comprova comportamento real de equipamento.

## Critérios localizados

| Critério | Resultado |
|---|---|
| Identidade da versão, quatro figuras e seus quatro SVGs | Atendido para HTML e inventário r7; hashes e posições conferidos. |
| Valores, unidades, sentidos e cálculos | Atendido nas quatro figuras, sob as hipóteses explicitadas. |
| Título, descrição, legenda e contexto | Sem divergência identificada no alcance inspecionado; não equivale a auditoria completa de acessibilidade. |
| Recursos externos, browser, outros textos e figuras | Não examinados nesta entrega; permanecem na fila de QA-09. |
| Critério integral QA-09 e liberação do próximo ID | Não atendido; a aprovação é somente localizada. |

Nenhuma alteração corretiva obrigatória foi identificada nas quatro figuras examinadas. Uma nova alteração nas dependências ou na versão exige avaliar novamente o alcance; não se transfere aceitação automaticamente por um hash isolado.
