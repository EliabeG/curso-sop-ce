# QA-09 — auditoria independente dos vínculos E1 → E2, r22

Data 30/10/2026. Auditor `/root/reference_triage`; Corretor `/root/next_graphics`. **APROVADO o recorte de quatro vínculos**, apenas quanto à identidade, existência e correspondência temática indicadas. Não aprova o conteúdo científico integral de E2 ou de E1, não altera produto e não encerra QA-09.

A entrega auditada tem SHA `d231c67d5cacd4992b71da34e01cf8dbfe881d595ff5aafb3fadfbb04da990a1`; seu script SHA `486d248178d45509210507a68389aade02433abc1dae10528c9ec019216c5343`. Conferi as versões locais de `modulos/e1-termodinamica.html`, SHA `ddf6edd271e38eb318ff1756cfa60f5bc8632882357de2401c114479cb3a432f`, e `modulos/e2-transferencia-de-calor.html`, SHA `fc4f05c6569aa7074811d1fe9f21e3b3641beba267f19125ce9f8d784ee53d14`. A URL relativa resolve do diretório `modulos` ao arquivo E2 identificado. A fotografia é condição da conclusão; mudança posterior exige reconferência.

| Vínculo em E1 | Destino único em E2 | Conferência do assunto |
|---|---|---|
| E2 — condução | `#conducao` | Título 6, condução e resistências; texto inclui Fourier e resistência plana e radial. |
| E2 — convecção | `#conveccao` | Título 7, convecção; texto inclui Newton, h e números adimensionais. |
| E2 — balanço e métodos de cálculo de trocadores | `#trocadores` | Título 10, balanço, LMTD e ε–NUT; coerente com o rótulo de métodos. |
| E2 — radiação e geometria de troca | `#radiacao` | Título 8, radiação e fatores de forma; compatível com a indicação de geometria. |

O [verificador independente](../evidencias/QA-09/auditoria-recursos-vinculos-e2-r22-reference-triage-20261030/verificar.py), SHA `9f1e9d46a64a4b30b401cc0ace42b465dec74d759a0b69d33be072e980f9ee13`, confirmou por `HTMLParser` os hashes de ambos os arquivos, exatamente um link por destino entre os quatro links E1 para esse arquivo, todos fora de `article`, e cada ID único no E2 em uma `section`. Os títulos e assuntos acima foram lidos manualmente; o script não testa a ciência nem a renderização. A contagem de vínculos é deste recorte, sem recontar os 1.263 do validador geral como novas descobertas.

O parecer verifica arquivo e fragmento local, não rolagem real, implantação, acessibilidade, licença, todos os vínculos externos, cálculos em E2 ou qualidade científica dos destinos. Não houve navegação no curso, leitor de tela, teste com estudantes ou revisão humana. Uma análise integral de E2 permanece trabalho distinto; nenhuma aprovação é transferida automaticamente a outras versões.
