# QA-09 — diagnósticos 11–15: exame do Corretor

Autor `/root/inspect_repo`. Módulo `modulos/e1-termodinamica.html` SHA-256 `7541e7c4c8314922992e99e8b62b40342c2d938e6edeac67ef9f74b69f86c17c`; inventário `auditoria/termodinamica/evidencias/QA-09/inventario-r4.json` SHA `44d19642bcf39109edf620e7304580b7a8a686e7c42cfa7101fa3d118a79d054`. Atribuição: o apoio independente `auditoria/termodinamica/pareceres/QA-09-diagnosticos-11-15-apoio-independente-r1.md` tem SHA `2c69b7ce19f67cc4e31af0059dddbc348431d527fa34a293b32817e10544d423`; examinou HTML anterior, mas seus cinco fragmentos mantêm hashes idênticos no atual. Seus juízos não são aceite automático. Fontes remotas consultadas em 29/10/2026, sem cópia nem hash local; dados dos problemas são nominais didáticos.

## 11 — Equilíbrio de fases e refrigerante

Fragmento `b03f1c142dc31638a159c7d145d770898d80eccbb10f6c6486c922e34d61891c`. Líquido e vapor podem coexistir com massas e densidades diferentes. Em equilíbrio completo e com transferência permitida, o potencial químico de cada componente comum é igual nas fases; restrições de permeabilidade podem modificar as condições aplicáveis. O [MIT, notas 10, p. 4 do PDF](https://ocw.mit.edu/courses/3-020-thermodynamics-of-materials-spring-2021/mit3_020s21_l10.pdf) demonstra a igualdade para uma substância; o material `#base-equilibrio-fases` apresenta o caso de componentes. Alto calor latente significa maior energia de vaporização por massa sob as condições relevantes, não garante COP ou segurança, conforme base `#base-calor-latente`. Exame conceitual efetivo, sem operação numérica ou tolerância de arredondamento; compatível no modelo apresentado.

## 12 — Ciclos e compressor

Fragmento `618ac9f908af2cd203e8c44ff47708b488aa0e80c61111b4a1e5e082c4e35ca7`. **Condicionalmente** a 300 kW ser entrada térmica total e 50 kW o único consumo descontado, potência líquida =140−50=90 kW e rendimento =90/300=0,30=30%. Com 6 L admitidos à sucção por deslocamento de 8 L na mesma base, eficiência volumétrica=6/8=0,75=75%; na compressão convencional antes da descarga, ambas as válvulas estão fechadas. Comparações exatas para dados nominais, sem tolerância de medição. Bases `#base-brayton-real`, `#base-valvulas-compressor` e `#base-eficiencia-volumetrica`; [MIT, Brayton](https://web.mit.edu/16.unified/www/SPRING/thermodynamics/notes/node46.html) fundamenta trabalho líquido.

O apoio observa que o enunciado não exclui consumo auxiliar nem deixa explícito que o calor é total. Exemplo de teste com 10 kW adicionais de consumo: (140−50−10)/300=26,666…%; o contramodelo não é dado do exercício. **Ressalva em adjudicação:** a conta publicada é correta sob as condições expostas, mas a suficiência do enunciado está em análise; não é aceite do item vigente.

## 13 — Trocadores e radiação

Fragmento `f632a9109e85568ba75dc475cc9c184359520812a962e4cf9874a6d133fbf140`. Sob Q̇=UAΔT média, área e diferença média efetiva constantes, U₂=0,70 U₁ implica Q̇₂=0,70 Q̇₁: **queda de 30%**, não de 70%; igualdade exata para dados nominais. Num trocador indireto convencional, há convecção no fluido quente, condução na parede e convecção no frio, sem mistura normal; suportes e cabos continuam conduzindo em vácuo e radiação não requer gás. Não se conclui que um mecanismo domine. Bases `#base-trocadores` e `#base-radiacao-vacuo`; [DOE, Fundamentals Handbook, vol. 2](https://www.energy.gov/sites/default/files/2026-04/DOE-HDBK-1012-92_VOL2.pdf) para transferência de calor. Compatível nas condições indicadas.

## 14 — Geração e face exposta

Fragmento `d31dc8c7929c0d00feccdf2f5baca49b3d957a5cb81c7ce36fd26a68330df849`. No modelo de saída térmica única pela face e média uniforme de h, V=2×1×1=2 m³, A=2×1=2 m², geração=60×2=120 W, ΔT=120/(6×2)=10 K e temperatura **média** da face =18+10=28 °C. Igualdade exata para dados nominais; sem incerteza de h informada. Base `#base-geracao-face`; [DOE, vol. 2](https://www.energy.gov/sites/default/files/2026-04/DOE-HDBK-1012-92_VOL2.pdf).

O enunciado diz apenas que uma face está exposta e exclui radiação; isso não necessariamente exclui condução por suporte nas demais faces. Num contramodelo com 60 W conduzidos ao suporte, a face dissiparia 60 W e sua média seria 18+60/(6×2)=23 °C. Este fluxo adicional é hipótese de teste, não dado original. **Ressalva em adjudicação:** 28 °C é condicionado à exclusividade da saída; não se atribui isolamento a faces não explicitamente isoladas apenas pela expressão “exposta”.

## 15 — Mistura de capacidades iguais

Fragmento `9ab4057c910696dc3cd65a11173b0e43c0a39435af075fb112b80d781a62013c`. Iguais massas, mesmo líquido e c constante dão capacidades iguais C. Com isolamento, recipiente desprezível, mesma fase e ausência de trabalho relevante, C(Tf−12)+C(Tf−24)+C(Tf−36)=0, logo **Tf=24 °C**. A média simples resulta de capacidades iguais, não do isolamento sozinho. Valor dentro do intervalo inicial e exato para valores nominais; sem tolerância experimental fornecida. Base `#base-mistura-termica`; [OpenStax, calorimetria](https://openstax.org/books/chemistry-2e/pages/5-2-calorimetry). Compatível no modelo ensinado.
