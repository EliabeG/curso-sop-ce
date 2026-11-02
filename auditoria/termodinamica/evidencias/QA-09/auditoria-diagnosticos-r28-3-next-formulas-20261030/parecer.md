# QA-09 — auditoria independente dos diagnósticos D01–D05

30/10/2026. Auditor `/root/next_formulas`. **APROVADO NO RECORTE** da fotografia r27, considerando os enunciados, as respostas e as condições apresentadas nas bases vinculadas. O nome `diagnosticos-r28-3` identifica o lote de evidência, não uma versão r28 da aula. Não representa aceitação global da aula ou dos bancos.

## Identidade e método

Li os cinco recortes e os trechos pertinentes de suas bases. A entrega `diagnosticos-r28-3/entrega.md` tem SHA-256 `a207960549fa1df851e783d62fdcba4ad7a92de6a8742e6b3b56f60a3f645fbc`; `identidades.json`, `6f66ff4568d1d201d98b82bea686bcb83edc48acdd246657bdf3e0c92a36aad1`; `verificar.py`, `0419e8b50e3479e3262bd2cca76ae994b369e98f5d1d317f766a3cc5028ddf61`. A fotografia `aplicacao-carnot-flashcards-r27-r1/resultado/depois-aula.html` e a aula corrente no momento desta verificação tinham SHA `9af8e2c9ffe509e40594d086a9ef4ad75127fb4ca873efb305d3144e08f3fc49`; inventário r27 `a58d7f0b0a5f097eef83ad83026ef49e801457b87f7cf2b2345c3dd915597c7c`.

Executei `python3 auditoria/termodinamica/evidencias/QA-09/diagnosticos-r28-3/verificar.py` e comparei a saída ao manifesto por `diff`: idênticos, código 0. O script reextrai os cinco intervalos UTF-16 e confere hashes, numeração, destinos únicos e contas selecionadas; não verifica a física por si. Revi os modelos independentemente e abri as fontes indicadas.

## Contas, hipóteses e limites

| Diagnóstico | Verificação independente |
|---|---|
| D01 | Para amostra homogênea dividida em quatro partes de igual massa e mesmas condições, cada parte tem m/4 e V/4, pois a densidade é uniforme; ρ e T permanecem. Kelvin, K, é unidade de base SI para temperatura termodinâmica. |
| D02 | Span é limite superior menos inferior: −20 + 150 = 130 °C. O tubo curvo acoplado a ponteiro caracteriza manômetro de Bourdon e mede pressão. O enunciado não especifica a referência da leitura, portanto não se conclui pressão absoluta ou manométrica. |
| D03 | Com composição e massa fixas, gás ideal, V fixo e pressões absolutas, p₂/p₁=T₂/T₁=353,15/293,15≈1,20467; crescimento ≈20,47%. Razões de temperaturas Celsius não preservam a origem absoluta. |
| D04 | Sólidos apresentam vibrações e partículas de líquidos se movem; energia cinética microscópica não é exclusividade de gases. Pressão alta não garante idealidade: afastamento da condensação e baixa densidade favorecem o modelo, mas não definem erro quantitativo universal. |
| D05 | Na aproximação de mistura ideal e fator de intensificação desprezado da base, com mesma T e fase de referência, pᵥ₂/pᵥ₁=φ₂/φ₁=0,30/0,75=0,40. Umidade relativa não é fração mássica. O enunciado sozinho não explicita esse modelo; o recorte depende da base e a igualdade não deve ser generalizada sem atender às condições de ar real. |

Abri [BIPM, unidades de base](https://www.bipm.org/en/measurement-units/si-base-units), que identifica o kelvin e seu símbolo; [WIKA, modelos 111.16/111.26](https://www.wika.com/pt-br/111_16_111_26.WIKA), que descreve o princípio do tubo Bourdon; e [ASHRAE Handbook 2021, capítulo 1](https://handbook.ashrae.org/Handbooks/F21/SI/F21_Ch01/F21_Ch01_si.aspx), que distingue aproximações de gás perfeito e propriedades de ar úmido real. Essas fontes são apoio para os pontos indicados, não origem dos valores hipotéticos; esta revisão não constitui aprovação integral das fontes ou bases.

Não houve teste em navegador, leitor de tela, alunos ou revisão humana; não examino outros diagnósticos, outras fotografias ou o curso inteiro. Produto e controles não foram alterados.
