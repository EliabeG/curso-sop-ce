# QA-09 — auditoria independente dos exemplos EX-006–010 na fotografia r8

Data: 30/10/2026. Revisor: agente automatizado independente `/root/qa_fichas`. **Veredito: APROVADO no alcance localizado dos cinco exemplos e hipóteses conferidas.** QA-09 integral permanece em correção; este parecer não libera outro ID nem classifica o curso como avançado.

## Critério e versão

QA-09 requer inventariar e recalcular conteúdo numérico além dos 197 artigos, com referências verificáveis e resultados conferidos, inclusive exemplos e explicações. Esta revisão examina somente os cinco exemplos listados na [entrega do Corretor](../evidencias/QA-09/exemplos-006-010-r8-corretor-20261030/entrega.md), SHA-256 `4662333be137b9b6cdc8ea81878a5d931a1384d4439996c91b7910253e72d6b6`. A regra curricular comum não é encerrada com este recorte de verificação.

Aula `modulos/e1-termodinamica.html` SHA-256 `57b13f0d6386764f1cc46ce543013b0eb75f7bfa97ffbd63ea331f38bfc5af8c`; inventário r8 `ae75a258398c385398567457d98ebd49b9838c0c9a4eedc69ea8d2d72981b687`. Li os cinco blocos e seus contextos diretamente na aula. As posições UTF-16 são válidas apenas nessa fotografia. O registro do Corretor `resultado.json` tem SHA-256 `be7ae2dd51e69711ade463bfe791e3819d558972fc619df0c18c9300fab77401`; seu script somente leitura `conferir.mjs` tem SHA-256 `b3efe08ce5c8e3d38fc9eee8cc4734ba58e75e7265ef309b069c2de06c641f6d` e foi reproduzido com sucesso.

O teste [auditoria-independente.mjs](../evidencias/QA-09/exemplos-006-010-r8-corretor-20261030/auditoria-independente.mjs), SHA-256 `874fcac6a96adf1fa54a46a287bfaef8eee1324bac4aaf3b9d92d92dd67659c7`, confirmou os cinco fragmentos únicos, título, limites, SHA e identificação no r8, bem como o hash integral dos cinco blocos ancestrais das bases. Esses hashes coincidem com o [adendo anterior](QA-09-exemplos-06-10-bases-ex008-adendo-independente-r1.md); isso não valida automaticamente dependências externas nem as demais ocorrências dessas bases. O teste usa o parser do projeto e não avalia mérito científico por si só.

## Recálculo independente

| Exemplo | Resultados e condições examinadas |
|---|---|
| EX-006 | `T₂/T₁=(3/2)(6/5)=9/5=1,8`; valor final é 180% do inicial e aumento `80%`. A base fixa quantidade e composição de gás ideal e exige pressão e temperatura absolutas. Correto para razão de temperaturas em K. |
| EX-007 | `0,60/0,80=3/4`; pressão parcial final é 75% da inicial, queda relativa 25%. A variação de umidade relativa é −20 pontos percentuais. Correto na aproximação de mistura ideal indicada, com mesma T, fase de referência e pressão de saturação. |
| EX-008 | `(7−5)×0,02=0,04 kJ=40 J`, sinal positivo para líquido→vapor desfavorece localmente essa direção. No contexto de fases puras e T,p impostos, a diferença de potenciais permaneceu constante no modelo; interpretar a conta como variação finita exata exige persistência das fases e desprezo de efeitos interfaciais. Não generalizar para mistura cuja composição mude; não se trata de estados tabelados. O adendo anterior distingue o sinal local e os limites. |
| EX-009 | `0,90×200+(0,0002/2)(500²−300²)=180+16=196 kJ/kg`. Valor fixo de cp na entrada: `(0,90+0,0002×300)×200=192 kJ/kg`; em 400 K: `0,98×200=196 kJ/kg`, por linearidade particular. Correto para gás ideal de composição fixa e unidades declaradas. Multiplicar por massa converte Δh em ΔH; isso não é automaticamente a variação de energia interna. |
| EX-010 | `3000−2600=400 kJ/kg`; `2×400=800 kW`. A base estabelece regime permanente, adiabaticidade e ΔEC/ΔEP desprezíveis; w é trabalho não associado ao escoamento. Correto em termos de trabalho líquido, sem validar estados reais de vapor. |

Conferi a aritmética separadamente com frações exatas; valores e erros aritméticos são relativos aos dados hipotéticos fornecidos, não incerteza instrumental. A leitura de [MIT, equilíbrio de fases de um componente](https://ocw.mit.edu/courses/5-60-thermodynamics-kinetics-spring-2008/b312114e4e885b69b5746dcad660cc4f_lec_18.pdf), [ASHRAE, psicrometria](https://handbook.ashrae.org/Handbooks/F21/SI/F21_Ch01/F21_Ch01_si.aspx) e [DOE, fundamentos, vol. 1](https://www.energy.gov/sites/default/files/2026-04/DOE-HDBK-1012-92_VOL1.pdf), em 30/10/2026, sustenta os limites gerais citados; nenhuma dessas fontes é origem dos valores didáticos dos exemplos.

## Critérios e decisão

| Critério no recorte | Resultado |
|---|---|
| Documento, contexto, unicidade, posições e hashes dos cinco exemplos | Atendido na fotografia r8. |
| Identidade dos cinco blocos das bases | Atendido, sem transferência automática de aceites nem validação de outras dependências. |
| Hipóteses, números, unidades e sinais | Atendido nas condições descritas e com limites do EX-008. |
| Restante da seção, figuras, fontes dependentes e QA-09 integral | Fora deste recorte; permanecem pendentes. |
| Liberação de outro ID | Não autorizada. |

Não houve teste em navegador, avaliação com estudantes, revisão humana ou certificação externa. Mudança posterior do documento exige reconciliar o contexto e as posições antes de transferir qualquer evidência.
