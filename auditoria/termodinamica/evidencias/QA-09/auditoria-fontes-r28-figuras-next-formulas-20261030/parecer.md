# QA-09 — parecer independente sobre fontes e quatro figuras da fotografia r27

Data: 30/10/2026. Auditor: `/root/next_formulas`. **Resultado: APROVADO NO RECORTE**, com as limitações abaixo. Trata-se de auditoria da entrega `fontes-r28-figuras-r27-20261030`, e não de uma versão r28 do produto, nem de aceitação global da aula.

## Identidade e procedimento

Conferi diretamente os quatro fragmentos, seus textos acessíveis, legendas e desenhos, o manifesto e o verificador da entrega. Na fotografia examinada, `modulos/e1-termodinamica.html` tinha SHA-256 `9af8e2c9ffe509e40594d086a9ef4ad75127fb4ca873efb305d3144e08f3fc49`; a entrega tinha SHA `d7455f7c84dfb1bac5a5d45da8053632fa70034d00479cc8d9c8c3653211cc5e`, o manifesto `identidades.json` SHA `db7a58ccca64bdada986ee53c1db6ac6e2ad65b1ef160af67fb18529975efd1c` e `verificar.py` SHA `09c2b9c2b245a233eb46cca3df4c7705efa2573ca6aaf6687e259bb2110c1101`. Executei o verificador na raiz: retornou `ok: identidades, rótulos ARIA, legendas e contas; não testa leitor de tela ou renderização`. Sua guarda verifica também o inventário identificado na entrega. Os intervalos UTF-16 e hashes dos fragmentos constam do manifesto e foram confrontados com os quatro elementos.

Para examinar geometria e sentido das setas, exportei separadamente os SVGs a imagens temporárias: acrescentei namespace e CSS sintético e normalizei a capitalização de `viewBox` para o renderizador independente. O resultado confirma as relações geométricas descritas abaixo apenas nessa reconstrução; não equivale à renderização da página com seu CSS em navegador. Abri as três fontes primárias citadas e conferi o contexto indicado.

## Exame científico e correspondência

| Figura e intervalo UTF-16 | Verificação independente |
|---|---|
| Ciclo p–V, 172570–173632 | O percurso A→B→C→D→A é horário. Na interpretação quase estática, expansão a 200 kPa e compressão a 100 kPa por 2 m³ geram trabalho líquido de fronteira de +200 kJ, convenção positivo produzido. Título acessível e legenda descrevem o mesmo circuito; o SVG não tem `desc`, o que a entrega declara. |
| Dois caminhos p–V, 200305–201775 | A→C→B fornece 600 kJ e A→D→B 200 kJ de trabalho de fronteira quase estático; segmentos verticais não contribuem. Em ambos os extremos pV=300 kPa·m³, implicando mesma temperatura somente para o mesmo gás ideal e massa fixa. Texto acessível e caminhos da reconstrução concordam. |
| Mistura, 211566–212886 | Com mesmo líquido, capacidade térmica constante, sistema isolado, recipiente desprezível e sem contribuição adicional relevante de trabalho ou energia de mistura, `(1×20+3×60)/4=50 °C`; massa final 4 kg. Valores e setas da reconstrução conferem. A descrição isolada não contém todas as hipóteses, e o relatório corretamente aponta sua presença no bloco contextual. |
| Compressor alternativo, 408674–410028 | 1→2 é compressão com válvulas fechadas; 2→3 descarga com volume decrescente; 3→4 reexpansão; 4→1 admissão. A reconstrução concorda com legenda e descrição. As linhas horizontais representam pressões aproximadamente constantes e são esquema qualitativo, não curva medida. |

[Purdue, ME 200, p. 8 do PDF](https://engineering.purdue.edu/CFDLAB/class/me200/filesFall2008/me200_notes_f08_week2.pdf) sustenta dependência do trabalho do caminho e sinal positivo do ciclo horário; não fornece os valores didáticos destas figuras. [MIT OCW, Solution Theory, p. 8 do PDF](https://ocw.mit.edu/courses/3-20-materials-at-equilibrium-sma-5111-fall-2003/764ba46faf34fb6f2439c6b52eb37fb9_mixtures.pdf) aborda entalpia de mistura, apoiando a ressalva geral de que sua contribuição pode ser relevante; não prova o valor numérico do exemplo de um mesmo líquido. [DOE-HDBK-1018/2-93, p. ME-05 3, p. 85 do PDF](https://www.energy.gov/documents/doe-hdbk-1018-93vol2) descreve a reexpansão e os eventos de válvula no compressor; não atribui os dados ou curvas exatos à figura.

## Alcance

Os quatro SVGs possuem título referenciado e legenda; três possuem também `desc`. Verificação de existência e unicidade de rótulos, conferência textual e reconstrução visual parcial sustentam as afirmações localizadas da entrega. Não testei página renderizada em navegador, contraste, ampliação, ordem de leitura, leitores de tela ou experiências de usuários. Não infiro conformidade de acessibilidade, validade de outras figuras, cobertura integral das fontes ou aprovação global do curso. Não alterei HTML, controles ou a evidência examinada.
