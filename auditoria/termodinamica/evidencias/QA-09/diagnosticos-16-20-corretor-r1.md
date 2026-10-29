# QA-09 — diagnósticos 16–20: exame do Corretor

Autor `/root/inspect_repo`. Módulo `modulos/e1-termodinamica.html` SHA-256 `7541e7c4c8314922992e99e8b62b40342c2d938e6edeac67ef9f74b69f86c17c`; inventário `auditoria/termodinamica/evidencias/QA-09/inventario-r4.json` SHA `44d19642bcf39109edf620e7304580b7a8a686e7c42cfa7101fa3d118a79d054`. Atribuição: apoio independente `auditoria/termodinamica/pareceres/QA-09-diagnosticos-16-20-apoio-independente-r1.md`, SHA `2dd4f595f7fa3a73eeac4b8bd973df434ee1879ac876b4c98e0b892d0818a922`, examinou os mesmos fragmentos; seus juízos não são aceite automático. Fontes remotas consultadas em 29/10/2026, sem cópia nem hash local; valores dos exercícios são didáticos.

## 16 — Materiais diferentes

Fragmento `c532f8d68448e4171a0be85ed5fda8db65f3d2984dbc3e568793842aba4849f6`. Com capacidades positivas constantes 2 e 6 kJ/K, sem outras interações, reação ou mudança de fase, o equilíbrio exige 2(Tf−90)+6(Tf−30)=0; assim 8Tf=360 e **Tf=45 °C**. O valor fica entre os extremos de 30 e 90 °C; média não ponderada daria 60 °C, incorreta neste modelo. A base `#base-mistura-termica` apresenta capacidades constantes e o balanço; o comando não repete essa condição. Exato para os valores nominais sob o modelo, sem incerteza experimental fornecida. [OpenStax, calorimetria](https://openstax.org/books/chemistry-2e/pages/5-2-calorimetry).

## 17 — Perda externa

Fragmento `a91c10b174fea3b8d18ea9382e6a3e34404a645706424171164a86f15dc6f7e3`. Com as capacidades constantes, recipiente incluído, trabalho nulo e perda líquida de 20 kJ, 4(Tf−80)+4(Tf−20)+2(Tf−20)=−20 kJ; logo 10Tf−440=−20 e **Tf=42 °C**. As diferenças em °C têm o mesmo incremento em K; o sinal da perda é negativo para o conjunto. Valores exatos para dados nominais e modelo, sem tolerância instrumental. Bases `#base-mistura-termica` e `#base-balanco-fechado`; [OpenStax, primeira lei](https://openstax.org/books/university-physics-volume-2/pages/3-3-first-law-of-thermodynamics).

## 18 — Fusão parcial

Fragmento `5d6ecc42c3790f16642342163647a88760466897f3a95cdc88b0aec1fc53578a`. A água ao esfriar de 20 para 0 °C libera 0,5×4,2×20=42 kJ; fundir 0,2 kg exige 0,2×334=66,8 kJ. Assim não derrete todo o gelo; massa fundida=42/334=0,12574850299… kg e restante=0,07425149701… kg, que arredondam a **0,126 e 0,074 kg**; em coexistência à temperatura de fusão fornecida Tf=0 °C. Cada valor publicado está no intervalo de arredondamento de ±0,0005 kg, sem implicar incerteza física das propriedades. O gelo começa na temperatura de fusão, sem termo de aquecimento sensível do gelo; isolamento e recipiente desprezível são dados. Base `#base-fase-calorimetria`; [OpenStax, calor latente](https://openstax.org/books/physics/pages/11-3-phase-change-and-latent-heat).

## 19 — Geração e excesso de CO₂

Fragmento `345887a5a233fa75a098ddabe3540edd95857c6fc0feea4c11b99fb64f44ea71`. Com geração apenas pelas pessoas, sem remoção adicional ou troca com outra zona, e volumes nas mesmas condições, G=20×300=6.000 mL/min=0,006 m³/min=0,36 m³/h. Excesso=500 ppm=0,0005; em mistura perfeita e regime estacionário, V̇=G/Δx=0,36/0,0005=**720 m³/h**. É a vazão que atinge exatamente o excesso limite sob esse modelo; mais vazão reduziria o excesso. A concentração externa já está descontada. Valores exatos para dados nominais, sem tolerância instrumental ou alegação de valor normativo. Base `#base-balanco-co2`; [NIOSH/CDC, balanço e mistura](https://stacks.cdc.gov/view/cdc/186564/cdc_186564_DS1.pdf).

O comando não elimina explicitamente outras fontes, remoção ou zonas; o apoio apresenta contramodelo com remoção adicional de 0,18 m³/h: a vazão para o mesmo excesso seria 0,18/0,0005=360 m³/h. O sumidouro é hipótese de teste e não dado original. **Ressalva em adjudicação:** não se conclui ainda se o contexto da base basta, embora a conta seja correta sob o modelo condicional.

## 20 — Bomba e potência

Fragmento `ad1478f21da750ea01a02368d9a3461193b9b19354ec4eb913d2e22fff048a32`. 36 m³/h=0,010 m³/s; potência hidráulica=ρgV̇H=1.000×10×0,010×15=1.500 W=1,5 kW; rendimento da bomba=1,5/3=0,50=**50%**. A referência é a potência de eixo, e H é altura manométrica total no modelo da base `#base-bomba-integrada`. Potência elétrica não é determinada sem rendimento do motor ou medida; igualdade exata para dados nominais, g=10 adotado pelo problema, sem precisão experimental especificada. Fonte [DOE, procedimento de teste de bombas](https://www.energy.gov/sites/prod/files/2015/12/f27/Pumps%20Test%20Procedure%20Final%20Rule.pdf), equação 10.
