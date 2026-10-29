# BAN-07 — parecer independente parcial AV71–AV80, rodada 1

Data: 29/10/2026. Revisor: agente automatizado independente `/root/auditoria_av71_80`. **Veredito local: sem ajustes obrigatórios encontrados neste bloco**. Este parecer não aprova BAN-07 inteiro, não libera outro ID e não certifica curso, aprendizagem ou projeto de equipamento.

## Escopo, versão e método

BAN-07 exige dados suficientes, consistência física, comando, unidades, restrições, resposta única, demonstração da chave e justificativa de distratores plausíveis por erros reais; examinam-se equivalências após arredondamento. O Protocolo AAA e a preparação independente foram lidos. Foram inspecionados os dez enunciados, todas as 50 alternativas e seus comentários, os cálculos necessários, a figura de AV80 e os deltas diretos dos dez artigos. Os juízos de plausibilidade abaixo são mecanismos teóricos concretos, não resultados de aplicação a alunos. As chaves e comentários estavam visíveis na extração: não se alega exame cego ou solução anterior ao confronto. A análise é própria e não depende exclusivamente do diagnóstico do Corretor.

A versão examinada é `modulos/e1-termodinamica.html`, SHA-256 **de614a44d796ca04268915f89f502060db2772835c072036a990802eff912b80**, igual ao arquivo congelado `evidencias/BAN-07/pacote-r1/modulos/e1-termodinamica.html`. A base anterior `evidencias/BAN-07/antes/modulos/e1-termodinamica.html` tem SHA-256 **0fc12a96fd30d366770a56c366fb61bc6a9fa7bd761e81fb40242a30f6dd78c7**. `PROTOCOLO_AAA.md` SHA-256 **18f1f299556e8e60c926a1921987f6d2c10cc939aa4aef4487117dc66c344afc**. `corretor/delta-artigos-r1.json` SHA-256 **9654b4c2a62d95776ec084b1d6c777d8551a0b81c5aea43fe1e71eb57126a6e4**; `diagnostico-pos-correcao-197-r1.json` SHA-256 **c71c4f88b795eda573a1621ff6879c1c0a1d1a9cbf858594f105d983219f1f34**. Os hashes dos artigos abaixo correspondem aos bytes UTF-8 de cada trecho `<article>…</article>` extraído diretamente, inclusive marcação; apenas AV73 difere da base anterior.

## Juízos individuais

**AV71 — C.** Ventilador e bomba impõem escoamento, caracterizando convecção forçada; a existência de empuxo adicional não transforma a classificação em exclusivamente natural. A: tomar o contato com a serpentina como condução exclusiva em sólido; B: confundir troca térmica com radiação exclusiva; C: correta; D: confundir todo escoamento por gradiente de temperatura com natural, ignorando acionamento; E: confundir movimento com isolamento térmico. Comando conceitual suficiente; comentários consistentes. A exclusividade em A, B e D e a necessidade em E tornam cada alternativa falsa, sem segunda resposta equivalente.

**AV72 — B.** Em tubos concêntricos, co-corrente entra na mesma extremidade; contracorrente, nas extremidades opostas. A inverte nomes; B é correta; C confunde os sentidos com uma variável irrelevante para perfis de temperatura; D atribui à co-corrente as entradas opostas; E atribui à contracorrente entradas comuns. A inversão e a generalização explicam os erros. Comentários corretos; definição de configuração é suficiente; somente B satisfaz ambas as partes.

**AV73 — A.** A razão área de troca/volume elevada caracteriza compactação; a capacidade também depende de coeficientes, temperaturas e geometria, sem promessa de desempenho ilimitado. A correta; B confunde volume pequeno com área térmica pequena; C troca a propriedade de transferência por capacidade de armazenamento; D toma uma parede mais espessa como melhora de condução, embora R=L/(kA) aumente com L para mesmo k e A; E confunde papel estrutural com função de extensão de área da aleta. Somente A satisfaz o comando; os comentários refletem essas distinções. Não se infere que qualquer aleta tenha eficiência unitária.

**AV74 — B.** Nas condições mantidas, Q̇=UAΔTₘ: 500×10×20=100.000 W=100 kW e 250×10×20=50 kW. A: fator dez por erro aritmético/conversão; B correta; C: inverte o efeito e duplica a taxa; D: ignora a alteração de U; E: trata números de U como kW sem os fatores dimensionais. As hipóteses explícitas de área e diferença média fixas são cruciais; não se afirma que tais grandezas permaneçam fixas em toda instalação real. Opções quantitativamente distintas mesmo arredondadas; comentários coerentes.

**AV75 — B.** q″ₓ=−10(−20)=+200 W/m²; o sinal indica fluxo no sentido positivo. A: confunde densidade de fluxo com potência total sem área; B correta; C: ignora gradiente não nulo; D: esquece sinal negativo de Fourier; E: divide 20 por 10. Dados e unidades bastam, comentários coerentes e apenas B tem magnitude, sinal e unidade corretos; +200 W não equivale a +200 W/m².

**AV76 — C.** I é verdadeira (advecção pelo movimento global); II é verdadeira (convecção na acepção do texto combina transporte pelo escoamento e difusão); III é falsa: k positivo permite condução e Fourier determina o sentido. A V–F–V erra II e III; B F–V–V erra I e III; C V–V–F correta; D F–F–V inverte as três; E V–V–V aceita III. Cada sequência difere, sem equivalência. Os comentários descrevem corretamente os erros e os qualificadores; a terminologia é compatível com a base vinculada.

**AV77 — C.** Para o sistema completo em regime permanente com as outras trocas desprezadas, energia rejeitada é 12+3=15 kW. A: conta só a potência recebida; B: subtrai em vez de adicionar; C correta; D: omite potência recebida; E: 12/3=4 é COP adimensional, não calor em kW. Comentários e sinais estão coerentes com os valores positivos de entrada e saída pedidos. Opções distintas; somente C fecha o balanço.

**AV78 — A.** Na vaporização, Q≈m h_fg sob condições adequadas e sem outras parcelas relevantes: alto h_fg favorece calor expressivo por massa evaporada. A correta; B confunde propriedade específica com garantia universal de eficiência; C extrapola vantagem térmica para descarte indevido; D inverte o sinal do processo endotérmico; E confunde desempenho com segurança de vazamentos. A usa “pode favorecer” e não promete vantagem global em qualquer ciclo ou condições; os comentários são consistentes. Sem comparação numérica, temperatura de saturação específica não é necessária para a escolha.

**AV79 — E.** Gás residual desprezível reduz sua contribuição, mas não elimina propagação radiativa nem condução por cabos e suportes. A supõe convecção intensa apesar da hipótese; B confunde vácuo com isolamento absoluto; C supõe que vácuo interrompe condução nos sólidos; D supõe que radiação exige fluido; E correta. Os mecanismos devem ser considerados, mesmo que um deles possa resultar pequeno em condições específicas: não se declara predominância ou taxa. Comentários e enunciado são consistentes; somente E contempla ambos.

**AV80 — E.** V=2×2×1=4 m³; geração 150×4=600 W. Em regime permanente, com cinco faces isoladas e radiação desprezada, 600=10×4×(Tₛ−25), donde ΔT=15 K e Tₛ=40 °C. A: supõe ausência de diferença apesar de geração; B: usa indevidamente 1 m², dando 25+600/(10×1)=85 °C; C: usa indevidamente toda a área 16 m², dando 28,75 °C; D: toma o acréscimo de 15 K como temperatura absoluta em °C; E correta. As cinco respostas são distintas após arredondamento; enunciado contém dados, unidades e restrições suficientes. Comentários coerentes. O PNG `assets/questoes-reais-e1/figura-9d73adf962aa.png`, SHA-256 **9d73adf962aaabecba761c823d3faca4bb4dd463a7009033e7267242bce84cb2**, foi efetivamente visto: ABCD tem AD=2 m e DC=2 m, DH=1 m; coincide com o texto e alternativa textual da imagem. A figura é redundante para este cálculo, pois o enunciado explicita a geometria; não se afirma aferição de leitura de figura ou acessibilidade assistiva.

## Identidade dos dez artigos e deltas

| Artigo | SHA-256 final | Igual à base anterior? |
|---|---|---|
| AV71 | a6822e633557838619c8a4c9fa1790c583776ef03830b6ca475f28ad6b25e2ff | Sim |
| AV72 | 9b34292c52fddf0bbfff7573258e810e24f0d3ad6cc86dc0c1eaed9743754e7d | Sim |
| AV73 | 0726d64bef732bb8b75a4473a190e14e7b7359155533af25fd5fc6b6c5f0b34a | Não |
| AV74 | e1cbd2e738cff1e20744251bba5ae94651ec5502fd9dc5808c1627f19b37b032 | Sim |
| AV75 | cf84420539a50440af16625535da0e7513c3d3de6362be04a830790f9eb9029c | Sim |
| AV76 | 1c62973843285a448a379f2b090961af88e38192c7728fb8d628fe4f7a4b48cb | Sim |
| AV77 | ba4e9d281b7c90b87fa9f88e4d953020a002c8903045cd2fcc0e0e55430b2820 | Sim |
| AV78 | eb02ebe932d364e4cd46353e409c2c75a53ec06000a2f3d95929a1289b2af8e4 | Sim |
| AV79 | e1bcf99fdeeb7c91da73b8c89d96714294fd1c64234861d3ae7fb0b91cf78bcc | Sim |
| AV80 | 9586c1757d18d3ba88d59485b308d8e6c92a4dd5859ffe94ff3cd7e3e9ac9a71 | Sim |

AV73 anterior: **6112aaaabbba78b71fbc5b7d5c216ddc3b56a62fa2ebeab34bca6645567521d1**. Confronto direto linha a linha mostra substituição apenas das alternativas B–E e seus comentários; enunciado, A, chave e demais trechos do artigo mantidos. As novas alternativas representam erros diferentes dos antigos extremos de área zero/isolamento/coeficiente nulo. Em `assets/curso.js`, `digitalDoBanco` inclui enunciado, textos e valores das alternativas e chave: a alteração de AV73 muda a entrada da identidade; a preservação/efeito em tentativas foi inferida do código, sem teste de navegador nem comprovação de ausência de colisão. A coordenação deve considerar as evidências de regressão aplicáveis do pacote.

## Fontes técnicas e alcance

O [DOE Fundamentals Handbook, volume 2](https://www.energy.gov/sites/default/files/2026-04/DOE-HDBK-1012-92_VOL2.pdf), seção Convection Heat Transfer, fornece Q̇=hAΔT, usado em AV80; o [DOE technical support document](https://www.energy.gov/sites/default/files/2022-01/mref-pa-tsd.pdf), seção sobre área superficial e aletas, sustenta o papel da área em AV73. A [NASA, Thermal Control](https://www.nasa.gov/smallsat-institute/sst-soa/thermal-control/) distingue radiação e condução por contato no vácuo em AV79. Essas fontes apoiam conceitos; os cálculos, a seleção e os mecanismos de erro são próprios. Consulta em 29/10/2026.

## Quadro de critérios e decisão

| Critério | Resultado no bloco | Evidência/limite |
|---|---|---|
| Dados, comando, condições e consistência física | Atendido | Dez análises acima; hipóteses especiais assinaladas nos itens 74, 77, 79 e 80. |
| Chave demonstrada e única | Atendido | Dez provas e confronto das 50 opções; as cinco sequências em AV76 e resultados numéricos são distintos. |
| Justificativa dos distratores | Atendido teoricamente | Erros plausíveis especificados por alternativa; atratividade/discriminação empírica não foi medida. |
| Deltas e identidade | Atendido no alcance local | Comparação direta dos dez artigos; único delta AV73. Efeito da identidade em armazenamento não foi testado aqui. |
| Figuras e equivalência numérica | Atendido no alcance local | PNG efetivamente visto; texto explicita geometria, e resultados numéricos não se sobrepõem. |
| Aprovação integral e liberação do próximo ID | Não aplicável | Este parecer não cobre os 187 outros itens nem integra seus pareceres; decisão compete ao Auditor principal e à coordenação. |

Não há ajuste obrigatório identificado para AV71–80. Não foram realizados piloto, estudo psicométrico, revisão humana, teste de navegador, teste assistivo, conferência de fontes oficiais das questões originais ou auditoria numérica integral BAN-08. Não foram alterados produto, controle AAA nem checklist. Este registro parcial não libera o próximo ID.
