# QA-09 — fichas de ciclos, compressão e radiação r15

Data: 30/10/2026. Corretor automatizado `/root/next_formulas`. **Aguardando Auditor independente.** Este recorte amplia a verificação antiga de constantes/expoentes para as relações inteiras das fichas 70, 81–83, 89–90 e 96; o lote não aprova QA-09, não altera produto nem controla outros objetos.

## Identidade e método

Formulário `formulas/termodinamica.html` SHA-256 `3ea110fda92c74253b69d89f5a6e62b288aa3bd99db6a51b54a6c67c8af82fce`; inventário r15 SHA `c8c9c3a3e141eba47a16e9f85c69f97c6e8b8a55aab689c6120ef1a0070c9d9c`. Recortes HTML completos por IDs, offsets UTF-16 e SHA em `identidades.json` SHA `948f213048343dc1c83bd584ecdceba6539b4d89b1a6aa2d94065ec3d28322a2`. Examinados texto, hipóteses e MathML; o script `verificar.mjs` SHA `faf13e97e610f29bfcfb995327240e550da870cd5a6005c8e158e84310d921b4` executa `node auditoria/termodinamica/evidencias/QA-09/fichas-ciclos-compressao-radiacao-r15-20261030/verificar.mjs`, confere hashes/identidades e recálculos, e retornou `ok=true`. Não interpreta fórmulas extraídas automaticamente nem escreve produto. Os casos a seguir são artificiais, não dados experimentais ou das fontes.

## Relações e verificações

| Ficha | Exame científico e numérico |
|---|---|
| 70 | Gás ideal de composição fixa, k=cp/cv constante: ds=cp dT/T−R dp/p=0 e R/cp=(k−1)/k fornecem T₂/T₁=(p₂/p₁)^((k−1)/k); p v^k constante e T₂/T₁=(v₁/v₂)^(k−1). Com T₁=300 K, p₂/p₁=4, k=1,4: T₂=445,7983 K. Pressões absolutas e temperaturas em K, mesmo gás; isentropia entre estados não garante processo real adiabático reversível. |
| 81 | Brayton simples ideal com dois processos isentrópicos e dois isobáricos, gás ideal com calores constantes e ciclo motor: η=1−rp^(-(k−1)/k). Para rp=8 e k=1,4, η=0,447955. Calor de entrada tem de ser positivo; perdas de pressão, regeneração e variação de cp exigem modelo diferente. |
| 82 | Otto ar-padrão ideal com calores constantes: compressão e expansão isentrópicas e trocas de calor isocóricas dão η=1−1/r^(k−1). Para r=8 e k=1,4, η=0,564725. Rendimento é térmico do ciclo ideal, não previsão automática de motor real. |
| 83 | Diesel ar-padrão ideal com compressão/expansão isentrópicas, adição isobárica e rejeição isocórica: η=1−r^(1−k)(rc^k−1)/(k(rc−1)), com r>1, 1<rc<r e k>1. Para r=18, rc=2, k=1,4, η=0,631578. A ficha define V₃/V₂ e as faixas; em rc=1 a forma direta é indeterminada, ainda que exista limite Otto. |
| 89 | Em escoamento permanente internamente reversível, desprezadas energias cinética/potencial, trabalho recebido = ∫ₚ₁ᵖ₂ v dp. Para gás ideal e pv^n constante, n>0 e n≠1, integra-se para n/(n−1) RT₁[(p₂/p₁)^((n−1)/n)−1]; a razão n/(n−1) pertence ao trabalho de eixo em escoamento, não ao trabalho de fronteira fechado. R=0,287 kJ/(kg K), T₁=300 K, p₂/p₁=4, n=1,3 dão 140,662 kJ/kg. Não confundir reversibilidade interna com isolamento adiabático; calor pode ser necessário para manter n. |
| 90 | Mesmas condições de escoamento internamente reversível, agora isotérmico: v=RT/p, ∫v dp=RT ln(p₂/p₁). Para o exemplo anterior, n→1, T=300 K e razão 4, dá 119,360 kJ/kg. Pressões absolutas positivas; compressão supõe p₂>p₁. O trabalho não se generaliza a compressor irreversível apenas por T constante. |
| 96 | Superfície cinza uniforme pequena vendo um entorno grande aproximadamente negro/isotérmico em meio não participante: Q̇=εσA(Ts⁴−Tamb⁴), positivo para saída. Com ε=0,8, A=2 m², Ts=500 K, Tamb=300 K e σ=5,67×10⁻⁸ W/(m² K⁴), dá 4935,168 W. Ts=Tamb resulta zero; Ts<Tamb inverte o sinal. Refletividade ou fatores de forma de um conjunto arbitrário de superfícies não estão abrangidos. |

## Fontes consultadas e limites

- [NASA Glenn, compressão isentrópica](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/isentrophic-compression/): derivação de relações para gás ideal e calores específicos constantes, ficha 70.
- [MIT OCW, Thermodynamics and Climate Change](https://ocw.mit.edu/courses/res-2-008-thermodynamics-and-climate-change-summer-2020/mitres-2-008su22_book.pdf): equações 5.35–5.36 (Otto e Diesel, pp. 143–144 impressas) e 5.122 (Brayton, p. 163), fichas 81–83. Os números hipotéticos acima não são retirados da fonte.
- [Purdue, ME 200, capítulo 6](https://www.purdue.edu/freeform/me200/wp-content/uploads/sites/29/2023/03/ME-200-Chapter-6.pdf): pp. 68–70 impressas, trabalho de escoamento reversível politrópico e isotérmico e hipóteses, fichas 89–90.
- [NIST/NBS, estudo de sistemas criogênicos, seção A3](https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nbsir74-366.pdf): fluxo radiativo com quarto expoente e fator de emissividade de superfície para entorno distante; ficha 96. A aplicação da ficha especifica entorno negro e meio não participante; não transfere a fórmula a geometrias gerais.

Não houve navegador real, leitor de tela, revisão humana ou ensaio com alunos. A verificação numérica não valida unidades ou hipóteses por si só. Solicito ao Auditor independente confrontar identidade, MathML, domínio das equações, fonte e contas, em particular se a referência ao modelo ar-padrão ideal na ficha 82 é suficientemente explícita e se os limites das fichas 89/90 são suficientes.
