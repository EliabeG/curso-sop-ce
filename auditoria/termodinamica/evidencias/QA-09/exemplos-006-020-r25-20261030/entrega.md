# QA-09 — reconciliação e recálculo EX-006–020 na r25

30/10/2026. Corretor `/root/next_examples`. **AGUARDANDO AUDITOR INDEPENDENTE; ressalva de hipótese em EX-010 e tabela de equipamento abaixo.** Este lote reexamina casos anteriormente auditados, não são 15 exercícios inéditos. Produto não alterado; QA-09 integral continua aberto.

## Identidade e dependências

Aula r25 SHA `ea0a7e3877c0a0250dac3d9c993c7922a03400929eb7a5dad39fcb27e3263c7e`, inventário SHA `6798d317db30bd69435ed14862cc03cd0f0c6313e40408dd8831052285984116`. `verificar.mjs` SHA `54150fea76054b327b9003710e605ee4a8b119cc3d4c7c02efb9d9a527cd3d5c`, executado da raiz com `node auditoria/termodinamica/evidencias/QA-09/exemplos-006-020-r25-20261030/verificar.mjs`, é somente leitura, confirma snapshots, referências de seção e título, ocorrência única, SHA, intervalos UTF-16 e aritmética nominal. A saída preservada `resultado.json` SHA `609b9134b94e3acac6e3af33b222d2c692c30ea1ea8b8a40d333a7085e34c1ef` contém posições, hashes e bases nas duas versões.

Todos 15 fragmentos r25 coincidem com a r7 após aplicação das correções EX-011/013. Os demais 13 coincidem também com seus hashes no mapa histórico `QA-09-mapa-independente-r1.json`, SHA `892b63067b87316009a89a8553e8288a9bc51c2c66929b33a4fd19d927d2ede9`; EX-011 e EX-013 usaram suas versões efetivas corrigidas da r7, não o hash pré-correção. A r7 é `aplicacao-exemplos-011-013-r1/e1-termodinamica-depois.html`, SHA `200f9b773050594d762cc596a5a89297024b245fc4f504081fc77baaed3db95f`, inventário `5090b9897a4698e0ad090f45182afba5880361aabc9fd3c3bdf848d971a85a1a`. Histórico EX-006–010 r8 `be7ae2dd51e69711ade463bfe791e3819d558972fc619df0c18c9300fab77401`; EX-012/014–020 r8 `577a64593f530cedfbfd265bcb842206ea37ab44be3890c6781f4b49652013fe`. Igualdade por si só não transfere aceite.

As bases ancestrais de EX-017/018 (`base-mistura-termica`) e EX-019 (`base-fase-calorimetria`) mudaram desde r7; as bases dos outros 12 permanecem iguais em bytes. As bases atuais de mistura explicitam capacidades constantes positivas, conjunto fechado/isolado e contribuição de mistura e efeitos de pressão/deformação desprezíveis; no caso do recipiente, Eext=Qext−Wext inclui as interações. A base de mudança de fase explicita trabalho de fronteira pΔV e Qfase=ΔH sob as hipóteses. Reli as versões atuais, que sustentam os cálculos do lote. O exemplo de turbina está no contêiner `Simplificações por equipamento`, e o identificador `base-turbina-potencia` pertence ao título do exemplo, não ao contêiner pai. A contagem de bases não corresponde a cálculos independentes nem revalida todas as figuras.

## Contas e limites dos modelos

| ID | Recálculo nominal e pressupostos |
|---|---|
| 006 | Gás ideal, massa/composição fixas e p,T absolutas: T₂/T₁=1,5×1,2=1,8; aumento **80%**, valor final 180% do inicial. |
| 007 | Mistura ideal, mesma T e fase de referência, fator de intensificação desprezado: pv₂/pv₁=0,60/0,80=0,75, queda **25%** ou 20 pontos percentuais de umidade relativa. |
| 008 | Transferência infinitesimal líquido→vapor em fases puras, T,p fixas, sem interface relevante: dG=(7−5)×0,02=**0,04 kJ = 40 J**; sinal desfavorece essa direção. Quantidade finita como igualdade exata requer potenciais constantes e fases persistentes; valores são fictícios. |
| 009 | Gás ideal de composição fixa com cp(T)=0,90+0,0002T: integral 0,90×200+0,0001(500²−300²)=**196 kJ/kg**; cp de entrada dá 192. Exatidão no ponto médio decorre desta função linear. |
| 010 | Turbina adiabática permanente, uma entrada e uma saída, ΔEc/ΔEp desprezíveis, trabalho total não associado ao escoamento: 3000−2600=**400 kJ/kg**; 2×400=**800 kW**. A base escreve trabalho por massa e descreve uma entrada/saída no singular, mas não exclui literalmente correntes adicionais ou especifica trabalho total na linha da tabela. Com duas saídas não equivalentes, h1−h2 de uma só corrente não determina trabalho total. Solicita-se adjudicação independente dessa lacuna de explicitação; as contas são válidas para o modelo declarado aqui. |
| 011 | Sistema fechado, rígido, único trabalho de eixo, ΔEc/ΔEp desprezíveis: Q=−40, W=−250 kJ, ΔU=−40−(−250)=**210 kJ**. |
| 012 | Fator indicado 4,2 J/cal: Q=420 J, ΔU=300 J, U₂=**350 J**. Usar 4,184 J/cal daria 348,4 J, outra convenção. |
| 013 | Único trabalho de fronteira W=200 kPa×(−0,020 m³)=−4 kJ; ΔU=−7−(−4)=**−3 kJ**. Exemplo separado de gás ideal de 1 kg com cv=0,70 e Q=35 kJ dá **50 K**. |
| 014 | Gás ideal de massa fixa, estados extremos pV=300 kPa·m³, curvas quase estáticas e trabalho de fronteira único: ΔU=0; caminhos a 300 e 100 kPa produzem **600 e 200 kJ**. A figura é dependência, não foi auditada como objeto visual aqui. |
| 015 | Expansão livre de gás ideal em volume rígido isolado, ΔU=0, T inicial/final igual, R=0,287: ΔS=0,287 ln 2≈**0,199 kJ/K** e Sger=ΔS. A integral por estados não torna reversível a expansão real. |
| 016 | Mesmo líquido/fase, c=4,2, trabalho/pressão desprezíveis: Q=2×4,2×30=**252 kJ**; potência útil 0,8×2=1,6 kJ/s dá **157,5 s**. |
| 017 | Mistura isolada de mesmo líquido, c constante, recipiente desprezível: (1×20+3×60)/4=**50 °C**. |
| 018 | Eext=0, capacidades 4,4,2 kJ/K, temperaturas 80,20,20 °C: Tf=(320+80+40)/10=**44 °C**; sem recipiente seria 50 °C. Saldo externo nulo não prova que cada interação individual seja nula. |
| 019 | Água inicial libera 0,5×4,2×20=42 kJ; 0,10 kg de gelo usa 33,4 kJ e 8,6/(0,6×4,2)=**3,41 °C**. Para 0,30 kg, fundem 42/334≈**0,126 kg**, restando gelo a 0 °C. Pressão atmosférica, conjunto isolado, sem capacidade do recipiente, calor latente indicado. |
| 020 | Tanque rígido inicialmente vazio, uma entrada de h constante, Q=W=0, parede e Ec/Ep desprezíveis, gás ideal com cp/cv constante: u₂=hin, T₂=1,4×300=**420 K**. Não é permanente enquanto acumula massa. |

Os valores são nominais, não medições, e não se afirmam incertezas instrumentais. O script testa a conta com dados digitados, não interpreta sozinho as hipóteses ou o material visual. A revisão da tabela em torno de EX-010 permanece aberta para o Auditor; preserva-se a distinção entre trabalho total não associado a escoamento e trabalho de escoamento já incorporado em h.

## Referências e pedido de auditoria

Fontes consultadas diretamente em 30/10/2026: [ASHRAE, psicrometria ideal e limites](https://handbook.ashrae.org/Handbooks/F21/SI/F21_Ch01/F21_Ch01_si.aspx); [MIT, potencial químico em equilíbrio de fases](https://ocw.mit.edu/courses/5-60-thermodynamics-kinetics-spring-2008/b312114e4e885b69b5746dcad660cc4f_lec_18.pdf); [MIT, balanço em escoamento](https://ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_6.htm); [MIT, tanque evacuado](https://web.mit.edu/16.unified/OldFiles/www/FALL/thermodynamics/notes/node17.html); [OpenStax, calorimetria](https://openstax.org/books/chemistry-2e/pages/5-2-calorimetry), [OpenStax, mudança de fase](https://openstax.org/books/physics/pages/11-3-phase-change-and-latent-heat) e [NIST, nota sobre calorias](https://www.nist.gov/pml/special-publication-811/nist-guide-si-footnotes). Não são fontes dos números postulados.

Solicita-se Auditor distinto para reexecutar verificações, contas e modelos, especialmente EX-010, 008 e as bases modificadas de EX-017–019. Não houve ensaio de navegador, leitor de tela, alunos, revisão humana ou certificação AAA; links e figuras não são integralmente revalidados.
