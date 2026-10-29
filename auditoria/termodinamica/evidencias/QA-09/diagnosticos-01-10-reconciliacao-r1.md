# QA-09 — reconciliação dos diagnósticos 01–10

Autor: `/root/inspect_repo`. Os exames iniciais `diagnosticos-01-05-corretor-r1.md` e `diagnosticos-06-10-corretor-r1.md` ficam preservados para o módulo SHA `9ec10053e40640feeb977baea742da3cbe4d546659f772f0256c6b3cb0720a55`; o módulo atual tem SHA `0de7342b99b9ebef8c1526f0b8eefb3544f000a4546d7b500558550d178285eb`. O delta de aplicação e a identidade dos demais diagnósticos estão em `aplicacao-diagnostico01-r1/verificacao-r1.json`. Nenhuma decisão abaixo é aceite global QA-09.

| Diagnóstico | Estado na versão atual e fundamentação |
| --- | --- |
| 01 | Insuficiência confirmada e candidata aprovada; aplicada com evidências em `aplicacao-diagnostico01-r1/entrega-r2.md`. A versão aplicada ainda requer revisão do Auditor. Com massas iguais, m/4 e V/4; densidade e temperatura iguais nas condições do enunciado. |
| 02 | 130 °C e manômetro Bourdon; compatível no exame do Corretor. |
| 03 | p₂/p₁=1,204673… ≈1,205 e aumento 20,4673…% ≈20,5%, com pressões absolutas e gás ideal. |
| 04 | Exame qualitativo compatível; idealidade não é garantida por alta pressão. |
| 05 | Razão 0,40 na aproximação ideal e mesma fase. `QA-09-adjudicacao-diagnosticos-01-05-independente-r1.md` considerou suficientes as hipóteses da base; a conclusão não é universal para ar úmido real. |
| 06 | Ajuste confirmado por `QA-09-adjudicacao-diagnosticos-06-08-independente-r1.md`: as duas transferências precisam ser exclusivas. `diagnostico06-candidata-r1.html` está isolada e pendente de revisão; o produto continua anterior. |
| 07 | Hipótese de desprezar variações macroscópicas consta da base; `QA-09-adjudicacao-diagnosticos-07-09-independente-r1.md` considerou suficiente nesse contexto. Não é resultado universal sem essa hipótese. |
| 08 | ΔH inversa=+30 kJ e PCS, nos mesmos estados/quantidades, são suficientes no contexto segundo adjudicação 06–08; não generalizar ΔH a todo calor de processo. |
| 09 | Ajuste confirmado pela adjudicação 07–09: esclarecer ciclo e totalidade das trocas. `diagnostico09-candidata-r1.html` está isolada e pendente de revisão; no modelo explicitado Qfrio mínimo=300 kJ. Produto continua anterior. |
| 10 | E destruída=42 kJ e Δh≈0,60 kJ/kg no modelo indicado; sem dados para quantificar o erro devido à variação de v. Revisão independente ainda necessária. |

Os hashes dos fragmentos e a demonstração de cada resposta encontram-se nos relatórios originais e nas candidatas. As fontes remotas foram consultadas sem snapshot; os valores de cada problema são dados didáticos. Não é possível atribuir a revisão independente dos itens remanescentes às adjudicações pontuais indicadas.
