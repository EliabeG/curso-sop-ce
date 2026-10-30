# QA-09 — exergia fora dos blocos teóricos r30, lote 2

30/10/2026. `/root/next_theory`. **Sem erro substantivo identificado neste recorte; aguarda auditoria independente.** Os exemplos já tinham revisões anteriores; esta é uma conferência localizada da fotografia r30, não criação de conteúdo nem alegação de primeira revisão. Sem edição de produto ou controles. Os dois artigos examinados integram os 197; não foram recontados como exercícios novos nem reabertos administrativamente.

## Identidade e histórico

Aula r30 SHA `c719adae3464fb56ed2b0ad7014e0721c0aab2da444fb484ec0b40c5c0c8fbd4`. O script `verificar.mjs` fixa os intervalos UTF-16 dos recortes, contas e hash da figura; leitura do texto e análise dos modelos foram realizadas separadamente.

| Recorte | Intervalo UTF-16 | SHA-256 | Revisão anterior |
|---|---|---|---|
| Diagnóstico D10, `preparacao-questoes` | 535679–536304 | `ceb10e781e7592d5dddbb9ad668aa88f976bb2693017bcbb63638a08a6c55d9c` | QA-09 `diagnosticos-r28-2`, recálculo r27; também revisão r9. |
| CR-37, `cr-e1-37` | 815954–819812 | `e3a49cb2403795ae867f5cd76694cc11c71f3ff7c24f31727407420bdcc5fe73` | Artigo integrante da auditoria histórica BAN-08; não se transfere sua aprovação a esta leitura. |
| AV-37, `av-e1-37` | 1105004–1109376 | `b741f7c26e317df09eaf7984e2065f881464ffc7367202fa2968b4ce30efe928` | Exatamente o hash do parecer científico `BAN-08-apoio-av36-40-r1-independente.md`; figura também revisada em `graficos-r28`. |

A figura referenciada pelos dois artigos tem SHA `222735fab01e54a81e34f3bb54cfd7097a8cbc1391ebe6420d60df8b2513a9cb`. Seu hash e vínculo foram conferidos, mas este lote não repete avaliação visual ou acessibilidade, já abordadas em outro recorte.

## Relações e conclusão

**D10:** com temperatura ambiente de referência 280 K constante e entropia gerada de 0,15 kJ/K, a destruição é T₀Sger=42 kJ. Para a segunda pergunta, a identidade de Gibbs dh=Tds+vdp, em estados de equilíbrio de substância simples compressível e composição fixa, dá Δh≈vΔp quando ds=0 e v≈0,001 m³/kg ao longo da variação; 0,001×600 kPa = 0,60 kJ/kg. As grandezas têm bases distintas: a primeira é total e a segunda específica. A identidade é de propriedades e não supõe que o trabalho de eixo de qualquer dispositivo seja necessariamente 0,60 kJ/kg. As condições adicionais constam na base vinculada `base-gibbs`.

**CR-37:** afirmar que mais irreversibilidade sempre significa mais trabalho realizado está incorreto. O comentário situa Gouy–Stodola na referência reversível apropriada, com condições e restrições comparáveis. Para T₀>0 e Sger crescente no mesmo contexto, T₀Sger é trabalho útil perdido; a comparação requer identificar sistemas e fluxos, e energia não desaparece. O gabarito E é compatível com essa contestação do enunciado universal. Não se inferem valores de trabalho da área ou das linhas da figura.

**AV-37:** 300 K×0,20 kJ/K=60 kJ, alternativa C. O distrator B resulta de 26,85×0,20=5,37, mas representa uso inválido de temperatura Celsius num produto cuja temperatura deve ser absoluta. Sger e destruição positivas não indicam aumento do trabalho útil máximo sob a comparação apropriada. O enunciado declara que a conta é independente dos valores das curvas; os números do eixo angular não são dados para cálculo de energia. A expressão final “combinar o desenho com os dados” descreve leitura contextual, não converte o gráfico em escala numérica para esta conta.

As referências históricas sobre os modelos incluem [MIT, Gouy–Stodola, §6.6](https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node49.html), citada no produto, e [MIT OCW, segunda lei e Gibbs](https://www.ocw.mit.edu/courses/2-611-marine-power-and-propulsion-fall-2006/4c32b0845d40ee00555da443f8a0f58b_06second_law.pdf), citado no parecer BAN-08. Nesta rodada, três tentativas de abertura/busca via serviço web retornaram erro sem conteúdo; não confirmo acessibilidade atual dessas páginas. As operações são cálculos próprios sobre dados didáticos, não medidas experimentais das fontes. A ausência de acesso atual limita o juízo sobre links, não invalida aritmeticamente as relações examinadas.

Sem teste de navegador, leitor de tela, estudantes, revisão humana ou certificação externa. Uma revisão localizada não demonstra cobertura integral de exergia ou nível avançado; QA-09 permanece aberto.
