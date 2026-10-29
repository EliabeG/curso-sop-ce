# QA-09 — exemplos EX-001 a EX-005: exame do Corretor

Autor `/root/inspect_repo`. A fonte é `modulos/e1-termodinamica.html`, SHA `49b0df4fe59dfd01913f4d41a5e6869705f4bf4d6ded251060f940cd5d12c91b`; inventário `auditoria/termodinamica/evidencias/QA-09/inventario-r5.json`, SHA `e21bc074025815cb5708875f938cb8a0de200ebecc66c4a7c8997493c01b0ea4`. IDs EX são do mapa independente, não do HTML. O apoio independente `auditoria/termodinamica/pareceres/QA-09-exemplos-01-05-apoio-independente-r1.md`, SHA `c2db3b00c88dd4d667007b57395142001616dc49a8c7ef1dcd92cb89bfa95b23`, examinou a versão anterior; os cinco hashes dos fragmentos foram comparados com a versão atual e são idênticos. O apoio tem autoria própria e seu alcance não é aceite global. Fontes remotas consultadas em 29/10/2026, sem captura ou hash local.

## EX-001 — propriedade intensiva

Fragmento `6a992834b2c455d4432b96b0d885fc7092fa3c034ced4947c7b2738ff78de535`. Amostra homogênea de 9 kg e 0,010 m³: ρ=9/0,010=900 kg/m³. Metades nas mesmas condições têm m=4,5 kg e V=0,005 m³; ρ=4,5/0,005=900 kg/m³. Sob o modelo homogêneo da base `#base-medidas`, cada metade conserva densidade e energia interna específica e possui metade da energia interna total. Exatidão aritmética para valores nominais, sem incerteza medida; não se identifica o material. Fonte: [NIST, grandezas e unidades](https://www.nist.gov/pml/special-publication-811/nist-guide-si-chapter-8). Compatível no modelo apresentado.

## EX-002 — faixa do transmissor

Fragmento `570d1bac8f5a29ec4350c974fbcc797810b3b5a6255f9a543c194c57eb9f96ae`. Com limite inferior −10 °C e span de 120 °C, limite superior=−10+120=110 °C; inversamente 110−(−10)=120 °C. Um intervalo de 120 °C equivale em magnitude a 120 K, sem acrescentar 273,15. Base `#base-instrumentos`; [WIKA, definição de span](https://www.wika.com/media/Operating-instructions/Operating-instructions/Flow/Primary-flow-elements/oi_dpfm_en.pdf). Valores nominais, resultado exato; não se confunde span com incerteza de instrumento.

## EX-003 — interpolação

Fragmento `0a78231e1675ba3b239b70b393c4136f645777d039bcfa5ba975b299c6426b39`. Pares (Y,X)=(0,10) e (40,90), com relação afim ensinada antes na base: X=10+(90−10)Y/40=10+2Y. Para Y=30, proporção 30/40=0,75 e X=10+0,75×80=70. Exato para dados nominais no modelo linear; duas marcas não demonstram que um instrumento real seja linear. Base `#base-instrumentos`; [NIST, calibração](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=905548). A solução corresponde ao modelo ensinado.

## EX-004 — título por entalpia

Fragmento `25c4b655ec5aa4c0d743f6d52e378254643a4e06716b19b0333dbe515ab618f6`. Mistura saturada, com hf=400, hg=2.400 e h=900 kJ/kg, valores na mesma base: x=(900−400)/(2.400−400)=500/2.000=0,25. Portanto massa vapor=25% e líquido=75%; as frações de volume não são necessariamente iguais às de massa. O dado h está entre hf e hg, consistente com a premissa de mistura. Fonte para propriedades de mistura e título: [DOE, fundamentos, volume 1](https://www.energy.gov/sites/default/files/2026-04/DOE-HDBK-1012-92_VOL1.pdf). Resultado exato para os dados hipotéticos; sem substância e pressão, não se certificam propriedades físicas de uma tabela real.

## EX-005 — gás ideal e constante aproximada

Fragmento `cf1e98634d3a42d137ab84e055555bb5bedb3962304fc7fbc8c58134a6b406c7`. Na base `#base-gas-modelo`, R≈0,082 atm·L/(mol·K); n=1 mol, T=320 K e V=26,24 L dão p=nRT/V=26,24/26,24=1 atm **absoluta** para essa constante arredondada. Com R=8,314462618… J/(mol·K), 1 L=0,001 m³ e 1 atm=101.325 Pa, R≈0,08205736608 atm·L/(mol·K) e p≈1,000699586 atm, diferença de 0,000700 atm (0,070%) em relação à aproximação; o valor publicado é coerente com o R adotado. [NIST, constante molar dos gases](https://physics.nist.gov/cgi-bin/cuu/Value?r%7Csearch_for=R). O modelo ideal e os dados são didáticos, sem incerteza experimental ou afirmação de exatidão para gás real.
