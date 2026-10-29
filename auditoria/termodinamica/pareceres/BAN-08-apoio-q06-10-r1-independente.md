# BAN-08 — apoio independente Q06–Q10

Data 29/10/2026. Revisor e autor dos cálculos: agente automatizado `/root/auditor_ban08_novo`. Apoio parcial, sem aprovação BAN-08 e sem liberação do próximo ID; chaves e comentários estavam visíveis. Dados, figuras e bases locais: `modulos/e1-termodinamica.html`, SHA-256 `80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0`; os hashes abaixo identificam o trecho bruto `<article>...</article>` em UTF-8. Todas as questões têm cinco alternativas e são pontuáveis. Números fornecidos são dados didáticos; operações nominais exatas não estimam incerteza de medição.

Fontes dos modelos, acessadas em 29/10/2026: OpenStax, Physics §12.2, https://openstax.org/books/physics/pages/12-2-first-law-of-thermodynamics-thermal-energy-and-work (gás ideal, primeira lei e trabalho pΔV); OpenStax, University Physics v.2, equações cap. 3, https://openstax.org/books/university-physics-volume-2/pages/3-key-equations (integral p dV); MIT OCW 2.60J, aula 2, p. 14, https://ocw.mit.edu/courses/2-60j-fundamentals-of-advanced-energy-conversion-spring-2020/54a791b898a31befeea178f796efcd9c_MIT2_60s20_lec2.pdf (balanço e estrangulamento). Os valores e constantes fornecidos pelo curso prevalecem no cálculo, sem validação externa de uma propriedade experimental.

## Q06 — D

- Hash `b5198addbf901253a2fa8f0bd10483417ee502426480ebd9db042379bd911892`; bases `#base-gas-modelo`, `#base-leitura-matematica`. Ar ideal com m=1 kg, R=0,287 kJ/(kg·K), T=300 K, V=0,861 m³, pressão absoluta. p=mRT/V=(1×0,287×300)/0,861=86,1/0,861=100 kJ/m³=100 kPa; intermediário 86,1 kJ e valor final publicado 100 kPa coincidem exatamente, diferenças 0. A=0,287 toma R como pressão; B=300 toma T como pressão; C=1 decorre de erro de fator 100; E=86,1 trata numerador energético como pressão. Nenhuma opção coincide com D. Tolerância: igualdade aritmética exata com os dados adotados; não se infere precisão experimental a partir dos zeros.

## Q07 — E

- Hash `d5f76870b3e0ce1e099b232f0f407f771a06182210946fabc70af3e7f878825a`; bases `#base-primeira-lei`, `#base-balanco-fechado`. Sistema fechado, variações de EC e EP desprezíveis, Q recebido positivo e W produzido positivo. ΔU=Q−W=500−200=+300 kJ, publicado 300 kJ, diferença 0. A=−300 inverte o sinal, B=700 soma indevidamente saídas, C=500 omite trabalho, D=200 copia trabalho; sinais e números separam alternativas. Tolerância: igualdade aritmética nominal exata, sem incerteza presumida.

## Q08 — A

- Hash `38c9be48585810f0334e07dd3869a1ea469dd7efdb9a869a406a8f42aa2bd4e7`; bases `#base-trabalho-fronteira`, `#base-leitura-matematica`. Expansão quase estática com p=200 kPa constante, V1=0,1 e V2=0,3 m³. Integral W=∫p dV=200(0,3−0,1)=40 kPa·m³=+40 kJ produzidos; publicado 40 kJ, diferença 0. B=60 usa 200×0,3; C=−40 inverte sinal; D=0 supõe ΔV=0; E=20 usa 200×0,1. Nenhuma equivale à correta. Igualdade aritmética nominal exata e convenção de trabalho produzido positivo; não se deriva tolerância física dos dados.

## Q09 — B

- Hash `16501a81d69977300456240e97fcc15906ca07738d3bb91c6eae68a7e8d3e657`; bases `#base-trabalho-fronteira`, `#base-balanco-fechado`. Figura SVG incorporada no próprio artigo e coberta pelo hash acima: A=(1 m³,200 kPa), B=(3,200), C=(3,100), D=(1,100), ciclo A→B→C→D→A; eixo e legenda concordam. Equilíbrio mecânico, sem atrito/outros trabalhos, pressão de fronteira: W_AB=200(3−1)=+400 kJ; W_BC=W_DA=0; W_CD=100(1−3)=−200 kJ; W_líq=+200 kJ produzidos. Alternativamente área (200−100)(3−1)=200 kJ. Diferença ante 200 kJ publicado: 0. ΔU=0 é igualdade de estado para ciclo e não implica W=0. A=600 usa 200×3; C=100 omite fator ΔV=2 m³; D aplica indevidamente ΔU=0 ao trabalho; E tem magnitude correta e sinal oposto. Tolerância: igualdade nominal exata, com sinal e unidades; figura esquemática e não exige escala gráfica.

## Q10 — E

- Hash `aeb427a4ebc2b42fd02903a576e77183f7055790b47ba3c4ffc0afef33917af0`; base `#base-valvula-fase`. Para válvula em regime permanente, uma entrada/saída e mesma vazão mássica, balanço específico q−w=(h2−h1)+Δ(V²/2)+gΔz. Adiabática e sem trabalho, com variações cinética e potencial pequenas, h2−h1≈0 e h1≈h2 em kJ/kg. Aproximação deriva da negligência das variações e não de tolerância numérica especificada. h=u+pv com p em kPa e v em m³/kg é dimensionalmente coerente. s1=s2 não é necessidade (geração por irreversibilidade pode aumentá-la), u1=u2 e T1=T2 não valem para todo fluido, e estrangulamento pressupõe queda de pressão; só E expressa condição geral adequada. Não há valores de estado para medir erro de aproximação; tolerância numérica não aplicável por ausência de dados sobre as parcelas negligenciadas, não porque a relação seja exata em todos os regimes.

Não houve teste com estudantes nem certificação externa. Estes cinco registros não substituem o registro integral por ID e a revisão da entrega efetiva. Produto e controle não foram modificados.
