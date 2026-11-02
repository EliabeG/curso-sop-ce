# QA-09 — pontes de transferência e escolha de modelo, r21

30/10/2026. Corretor `/root/next_theory`. Leitura integral dos seis contêineres abaixo, situados na aula E1 como ponte para E2. Alguns exemplos, diagnósticos, fórmulas, figuras e a candidata específica EX-046 foram tratados em outros lotes; aqui são examinados no contexto inteiro dos blocos, sem contá-los como inéditos. A r21 pode estar em auditoria de aplicação; os resultados se referem exclusivamente à fotografia identificada e não constituem aceitação da versão inteira nem revisão completa de E2. Sem modificação de produto.

## Identidade

Fotografia `aplicacao-oficina-ex046-r21-r1/resultado/depois-aula.html` SHA `239fb6d9f307170adbb74e389b798d1ff3c9b8e0d8d2d6d874457b8a65f40238`; inventário `inventario-r21.json` SHA `d1d480c1c4ce0a31f9f4f0b8bf234be60c9867feae9336fbeefb06162e2826f1`. Intervalos são UTF-16 dos contêineres.

| Âncora | Intervalo | SHA-256 |
|---|---|---|
| base-transferencia | 449452–452269 | 62b2d9e3c3928f8c3658f441758c655a70ea1faaea44d37a811914419e289ec7 |
| base-trocadores | 452269–455901 | e3a891e5c67e0a92280ae9c78318f9d3d046c00605c857c3ebb250d5e09a02cc |
| base-radiacao-vacuo | 455901–458431 | a6cd5681c17a5440d2f6ecb9f60e59119f0d0c1f6feb9ee5a85293aa3ce10e19 |
| base-dilatacao | 458431–459553 | c5118d0aa02dae4be96485ba237df2cc113e5252f78f6a06f71997e0071e0b09 |
| base-geracao-face | 459553–462159 | 8e6e5374b2f4391f0adead00b525910b44df4f5a5b121421b71594af61476fa3 |
| base-escolha-modelo | 462159–464017 | 1fe60b25ce6fd1cfd6236459950c455b5c91c581beb17f17a55ccec49450ad17 |

## Conferência

- **Fourier e Newton:** k=5 W/(m K) e gradiente −30 K/m dão fluxo +150 W/m²; por 2 m², 300 W. Parede linear de 60 a 40 °C em 0,10 m dá −200 K/m; k=0,5 produz +100 W/m² e, em 3 m², 300 W. Regime permanente unidimensional, k constante e sem geração são condições suficientes para o perfil linear. Newton hA(Ts−T∞) em W pressupõe coeficiente/temperaturas adequados à área e sinal declarado. Diferenças em °C e K são numericamente iguais, não temperaturas absolutas.
- **Trocador:** U=400, A=8, ΔTm=25 produz 80 kW; com U=300 e o resto fixo, 60 kW e redução de 25%. Resistência por área 0,002 m² K/W dá U=500 W/(m² K); mais 0,001 leva a 333,33 W/(m² K), cerca de 2/3 da taxa sob A e ΔTm fixos. O texto distingue a parede plana e o cálculo cilíndrico, as áreas de referência e o fator F específico do arranjo. A expressão de diferença média logarítmica deve ser usada no domínio do método, com hipóteses de perfis e propriedades; não implica que qualquer dispositivo isolado ou escoamento aceite F=1. [DOE Handbook, volume 2](https://www.energy.gov/sites/default/files/2026-04/DOE-HDBK-1012-92_VOL2.pdf) trata resistências e diferença média logarítmica.
- **Radiação:** no modelo de superfície cinza pequena, ambiente negro grande, temperaturas uniformes e visão completa, a troca líquida é εσA(Ts⁴−Tamb⁴). Para ε=0,60→0,30, taxa cai à metade quando A e temperaturas são fixos e taxa inicial não nula. σ aproximado da aula, 5,67×10⁻⁸ W/(m² K⁴), confere com [NIST/CODATA 2022](https://physics.nist.gov/cgi-bin/cuu/Value?sigma%7Csearch_for=stefan+boltzmann), 5,670374419…×10⁻⁸ exato no SI; arredondamento é apropriado. Temperaturas absolutas em K são indispensáveis. A ausência de gás residual não elimina condução por suportes ou radiação.
- **Dilatação:** 10×10⁻⁶ K⁻¹ × 10 m × 80 K = 0,008 m = 8 mm. Exige expansão livre, aquecimento uniforme e coeficiente aproximadamente constante. O deslocamento livre não determina tensão por si só.
- **Geração e face:** 3×2×1=6 m³, face 3×2=6 m²; 200 W/m³×6 m³=1200 W e 1200/(20 W/(m² K)×6 m²)=10 K; ambiente 20 °C, face 30 °C. O exemplo r21 identifica alimentação elétrica de 1200 W e conversão integral em geração térmica, sem contá-las duas vezes; não é verificação independente da aplicação r21. A regra exige coeficiente e temperatura de face adequados, hA>0, demais saídas térmicas desprezíveis, sem acumulação térmica e condição compatível com a origem da energia. Uma face uniforme não implica bloco uniforme. O [MIT, equações de condução com geração e resistência convectiva](https://ocw.mit.edu/courses/2-051-introduction-to-heat-transfer-fall-2015/2013cba86d06ea09582d9e4d7558f514_MIT2_051F15_EqnSheet_Q1.pdf) fornece os modelos; [MIT, primeira lei](https://ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_4.htm) dá o balanço de energia total.
- **Escolha de modelo:** a sequência fronteira, acumulação, propriedades, hipóteses e pedido é coerente; primeira lei não basta para provar atendimento da segunda. Não foi feita auditoria integral dos destinos de todos os links neste lote.

## Pontos para auditor independente

1. Em `base-geracao-face`, o parágrafo geral afirma que em regime permanente não há acumulação de energia e que o calor gerado internamente deve sair pela superfície exposta, sem indicar junto à expressão a origem da energia nem distinguir balanço térmico do balanço de energia total. Como geração térmica é conversão e não criação, em um sistema fechado em regime permanente com saída de calor positiva é preciso uma entrada energética compatível. O EX-046 já explicita entrada elétrica e não duplicação, mas o leitor pode aplicar a fórmula geral isoladamente. Solicita-se julgamento sobre clarificação no parágrafo/legenda, sem repetir a entrada elétrica como segundo termo do balanço térmico. Para um bloco fechado com apenas saída de calor de 1200 W e nenhuma entrada, dE/dt=−1200 W; não é regime permanente de energia total. Em contraponto, com trabalho elétrico recebido de 1200 W e saída convectiva de 1200 W, dE/dt=0.
2. Em `base-radiacao-vacuo`, a igualdade de razões Q̇rad,2/Q̇rad,1=ε2/ε1 é enunciada genericamente com os fatores comuns mantidos, mas a divisão requer taxa inicial não nula. Com Ts=Tamb=300 K, ε1=0,60 e ε2=0,30, as duas taxas são zero e a razão é 0/0 indefinida; com ε1=0 e Ts≠Tamb a razão também não existe. A afirmação de proporcionalidade Q̇2=(ε2/ε1)Q̇1 pode ser usada quando ε1>0, mesmo que ambas as taxas sejam nulas, mas divisão de taxas exige Q̇1≠0. O exemplo qualitativo de 50% pressupõe troca líquida inicial não nula; solicita-se avaliar a necessidade de qualificar explicitamente esse domínio.

## Reprodutibilidade

Na raiz do repositório, execute `node auditoria/termodinamica/evidencias/QA-09/teoria-pontes-transferencia-r21-20261030/verificar.mjs`. O script identifica fotografia, inventário e seis contêineres e recalcula os valores e o caso de divisão por zero; SHA `3c5e888f80962f82a5217fd6e86ca2c946b68b964ae1ed9394637b9bd3e68a18`, saída `ok`. Não demonstra validade dos modelos nem substitui auditoria científica independente. Fontes verificadas via ferramenta web em 30/10/2026; sem teste de navegador, leitor de tela ou alunos.
