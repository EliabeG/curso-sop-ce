# QA-09 — auditoria independente das fichas 13–18 e 20–22, r9

Data: 30/10/2026. Revisor: agente automatizado independente `/root/next_theory`, distinto do Corretor `/root/next_formulas`. **Veredito localizado: APROVADO**, somente para as expressões, dados de teste e hipóteses aqui examinados nas nove fichas e na fotografia indicada. Não há aprovação de QA-09 integral e o próximo ID continua bloqueado.

## Critério, fotografia e extensão

QA-09 exige inventariar e recalcular o conteúdo numérico além dos 197 artigos, inclusive exemplos, oficinas, diagnósticos, fichas, projetos, figuras e explicações; cada ocorrência precisa de referência verificável e resultado conferido. Esta entrega parcial não responde a todo o critério. A regra comum curricular é pertinente ao encerramento de conteúdos, não transforma esta revisão das fichas existentes em conclusão curricular ou avaliação de alunos.

Examinei diretamente as fichas `formula-gas-ideal`, `formula-dois-estados`, `formula-restricoes`, `formula-compressibilidade`, `formula-calores-especificos`, `formula-energia-gas`, `formula-energia-c-variavel`, `formula-titulo` e `formula-mistura`, seus textos, hipóteses, unidades, estrutura dos 20 elementos MathML e os dados de teste. O formulário `formulas/termodinamica.html` tem SHA-256 `cda652563a79c49a6c3d527ad1400c7f7597d33c9b8523ed8a26047b25c69feb`; o inventário r9 tem `023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d`. A [entrega do Corretor](../evidencias/QA-09/fichas-gases-fases-r9-20261030/entrega.md) examinada tem SHA-256 `da7297a4ba67707bd06feaf6b7cb1a233d9c900a2bac269b7813433715971fbf`.

Reconstituí as nove identidades por arquivo, ID, posição UTF-16, estrutura e hash de fragmento r9. Conferi o MathML com leitura do código fonte e parsing XML dos 20 elementos; isso não comprova apresentação no navegador. Os nove hashes constam da entrega. A rotina própria de auditoria [verificar.py](../evidencias/QA-09/auditoria-fichas-gases-fases-r9-20261030/verificar.py), SHA-256 `6829bdcdc9744873070c18bd309c0cf109348620bb96da00d1abe19e86df0a16`, não grava dados e foi executada com sucesso. Também reproduzi a rotina read-only do Corretor. Os testes usam modelos artificiais e igualdades exatas, não representam medições ou tabela de fluido.

## Verificações independentes

| Fichas | Resultado e domínio conferido |
|---|---|
| 13–15 | `pV=mRT=nRᵤT` e `pv=RT`; com mesma massa/composição, `pV/T` é igual nos dois estados. As três restrições são alternativas. Usando p₁=100 kPa, V₁=0,861 m³ e T₁=300 K, `p₁V₁/T₁=0,287 kJ/K`; a p₂=200 kPa e T₂=400 K, V₂=0,574 m³. As demais contas para V, T ou p fixo conferem separadamente. |
| 16–18 | `Z=pV/(nRᵤT)=pv/(RT)` é adimensional. Z=1 isolado é compatibilidade pontual da equação de estado, não prova de idealidade global. `cp−cv=R` e `k=cp/cv` aplicam-se como descrito; `Δu=cvΔT`, `Δh=cpΔT`, `ΔU=mcvΔT` exigem gás ideal, composição fixa, calores constantes na faixa e massa fixa para ΔU. 0,718×100=71,8, 1,005×100=100,5 kJ/kg e 2×71,8=143,6 kJ. |
| 20 | Integração explícita no teste: ∫₃₀₀⁴⁰⁰ (0,8+0,001T)dT=115,0 kJ/kg e ∫₃₀₀⁴⁰⁰ (0,513+0,001T)dT=86,3 kJ/kg. A diferença 28,7 kJ/kg coincide com RΔT; os coeficientes lineares usam kJ/(kg·K²). As relações em gás ideal são de propriedades e não exigem processo isobárico/isocórico. |
| 21–22 | `x=mg/(mf+mg)` com massa total positiva e x entre 0 e 1. Para propriedade específica extensiva por unidade de massa, `y=(1−x)yf+xyg`, com inversão se yg≠yf e fases à mesma saturação. Com x=0,25, os testes fornecem h=1000, u=900 kJ/kg, v=0,25075 m³/kg e s=2,5 kJ/(kg·K), como registrados. A inversão perto do crítico pode ser sensível. A ficha indica substância pura líquido–vapor; não usar x fora desse domínio como título. |

Pressões e temperaturas absolutas são empregadas nos quocientes; temperaturas em kelvin para as razões. As relações são exatas nos modelos e dados nominais, sem tolerância experimental reivindicada. Na comparação de valores aproximados, a entrega manteve o valor exato ou dígitos de guarda.

## Fontes confrontadas

- [NASA Glenn, equação de estado](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/equation-of-state-ideal-gas-2/): relações para gás ideal e constantes em bases molar e mássica.
- [NBS/NIST, Natural Gas Handbook, p. 17, equações 4–5](https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nbsir86-3057.pdf): definição de Z na equação de estado; o documento trata gás natural e não fornece os dados artificiais do teste.
- [NASA Glenn, cp e cv](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/specific-heats-cp-and-cv-1/) e [MIT, u e h para gás ideal](https://www.ocw.mit.edu/ans7870/16/16.unified/thermoF03/mud/T6newmud.html), item 1: relações de propriedades e distinção de restrições de processo.
- [DOE-HDBK-1012/1-92](https://www.energy.gov/documents/doe-hdbk-1012-92vol1), pp. impressas 34 e 43–46: título e propriedades específicas de mistura. A forma para u segue da aditividade da energia interna; os valores do teste não foram extraídos de tabelas reais.

As referências foram acessadas em 30/10/2026 e dão suporte aos modelos no escopo exposto. Não foi feita pesquisa de todas as referências do curso nem validação de todas as propriedades reais possíveis.

## Quadro de critérios e decisão

| Critério localizado | Resultado |
|---|---|
| Identidade da fotografia e dos nove trechos | Atendido por hashes, posições, IDs e leitura direta. |
| Expressões, MathML, condições e unidades | Atendido no alcance indicado por leitura da estrutura e das premissas; sem ensaio de renderização. |
| Cálculos, domínio e fontes | Atendido para os modelos e testes artificiais acima; nenhum erro identificado no alcance. |
| QA-09 integral | Não atendido nesta entrega: demais ocorrências, figuras, fontes, recursos e integração da cobertura continuam pendentes. |
| Liberação do próximo ID | **Não liberado** até parecer integral de QA-09 e decisão da coordenação. |

Não houve navegador real, avaliação com alunos, revisão humana ou certificação externa. Mudança posterior da fonte ou das dependências exige reconciliação e reavaliação do alcance; a aprovação localizada não se transfere automaticamente.
