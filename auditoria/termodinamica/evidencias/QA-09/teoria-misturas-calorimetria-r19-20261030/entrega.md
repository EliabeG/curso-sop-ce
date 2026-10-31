# QA-09 — calorimetria, mistura térmica e mudança de fase, r19

## Recorte e identidade

Exame dos três blocos completos externos aos 197 artigos, na fotografia `aplicacao-notacao-fichas-r19-r1/resultado/depois-aula.html`, SHA-256 `9495c5a873dc67f6f1d6dd1919caa473f481a0bc029dbe97e3490adb1b530a65`; inventário `inventario-r19.json`, SHA-256 `ca99e56b3a5930cdd4f49f4d41a61eca19facc141b63da94dcd3b65039d03c2f`. As fichas e alguns exemplos relacionados já foram examinados em outros lotes; não se contabiliza esse histórico como trabalho novo. Os intervalos são índices de caracteres JavaScript na fotografia; o hash corresponde ao texto integral do contêiner.

| Âncora | Início | Fim | SHA-256 |
|---|---:|---:|---|
| base-calorimetria | 203897 | 206379 | 7c7e654b40f3d57c3d0d128ab5c48f9e9572f50a631c8123e45847df78228853 |
| base-mistura-termica | 206379 | 212704 | ee9bafa3d68b1ef06bd39268a717f2474472de6a981bd6b0423f85abcd9eef03 |
| base-fase-calorimetria | 212704 | 215090 | ddaaf9583c9fb8a99341184b41a8886d7e85f543ee2abdd3955c011d92888d88 |

## Contas e hipóteses

O aquecimento de 2 kg de material com c = 4,2 kJ/(kg K) por 30 K exige 252 kJ. Com 2 kW de potência e fração útil 0,8, a potência útil é 1,6 kJ/s e o tempo é 157,5 s. O modelo de calor sensível pressupõe c aproximadamente constante, mesma fase, e efeitos mecânicos e de pressão desprezíveis na aproximação usada.

Para a média ponderada, quantidades de 1 kg e 3 kg do mesmo material, inicialmente a 20 °C e 60 °C, resultam em 50 °C sob as hipóteses do modelo. Um recipiente de capacidade térmica 2 kJ/K inicialmente a 20 °C, trocando com dois corpos de capacidades 4 kJ/K a 80 °C e 4 kJ/K a 20 °C, resulta em 44 °C; ignorar o recipiente daria 50 °C. É uma temperatura de equilíbrio, não uma garantia de equilíbrio imediato.

No modelo de água e gelo a pressão atmosférica, água de 0,5 kg a 20 °C pode ceder 42 kJ ao atingir 0 °C, usando c = 4,2 kJ/(kg K). Para 0,1 kg de gelo a 0 °C, a fusão consome 33,4 kJ com ℓ = 334 kJ/kg; restam 8,6 kJ para aquecer 0,6 kg de água até aproximadamente 3,413 °C. Para 0,3 kg de gelo nas mesmas condições, a fusão completa exigiria 100,2 kJ: fundem aproximadamente 0,12575 kg e resta gelo a 0 °C. Admitem-se isolamento, perdas e capacidade do recipiente desprezíveis, parâmetros constantes e inexistência de outros trabalhos relevantes. Valores são aproximações didáticas.

## Questões para auditoria independente

1. **Mistura térmica.** Ao lado de Σ Cᵢ(Tf−Ti)=0 e da média ponderada, o texto informa capacidades constantes e positivas, isolamento, ausência de trabalho relevante, reação e mudança de fase. Mais adiante, alerta que reação ou entalpia de mistura relevante exige ampliação do modelo. A aplicabilidade da equação também depende de representar a variação de energia dos componentes por CᵢΔTᵢ e de desprezar a contribuição de mistura e de efeitos de pressão/deformação. Solicita-se julgar se a ressalva posterior torna suficientemente claro o domínio junto à fórmula, especialmente porque as fichas 27/28 já receberam qualificação semelhante na r12, sem que isso tenha modificado automaticamente esta base.

   Contramodelo contábil hipotético: duas porções líquidas inicialmente a 20 °C, com capacidades sensíveis de 2 kJ/K cada, em sistema fechado isolado, sem trabalho, reação nem mudança de fase. Suponha uma contribuição de energia interna de mistura de −40 kJ e um estado final a 30 °C. A variação sensível é +40 kJ e ΔU total é zero; a média ponderada isolada daria 20 °C. Não se atribuem esses valores a uma substância real: o exemplo mostra a hipótese adicional necessária na decomposição energética. Entalpia de mistura e energia interna de mistura não são intercambiáveis sem cuidado com pV.

2. **Mudança de fase.** A base apresenta |Qfase| = mℓ para uma mudança de fase “à pressão indicada” e associa ℓ à substância, transição e condições. Solicita-se explicitar o significado de ℓ e julgar se o contexto precisa delimitar o processo. Se ℓ for a magnitude da diferença de entalpia específica entre fases, condições suficientes para a equação são sistema fechado de massa fixa, substância pura em equilíbrio entre fases, T e pressão termodinâmica constantes durante a etapa, sem calor sensível ou outras parcelas relevantes, variações cinética e potencial desprezíveis e somente trabalho de fronteira Wb = pΔV. Uma definição operacional de calor latente para um processo específico pode usar outra convenção; por isso, a ausência de condições não prova, por si, que toda interpretação da frase seja falsa. A ficha 29 recebeu qualificação na r12; é uma localização distinta.

   Contraste algébrico de fronteiras: se ΔH = 200 kJ, p = 100 kPa e ΔV = 0,1 m³, então ΔU = 190 kJ. Com trabalho total de 5 kJ, a primeira lei exige Q = 195 kJ, não 200 kJ. É um balanço ilustrativo, não demonstração de uma trajetória real específica. Para misturas, composição de fases e temperatura de transição podem variar, o que pede tratamento adequado em vez de pressupor ℓ constante.

## Fontes e reprodutibilidade

- MIT OCW, *Solution Theory*, discussão termodinâmica de misturas: <https://ocw.mit.edu/courses/3-20-materials-at-equilibrium-sma-5111-fall-2003/764ba46faf34fb6f2439c6b52eb37fb9_mixtures.pdf>. Apoia a existência de contribuições de mistura; não valida os valores hipotéticos acima.
- MIT, *Q = ΔH*: <https://web.mit.edu/10.213/oldpages/f99/supp/readings/qdh/index.html>. Relaciona calor e entalpia em processo isobárico sob hipóteses de trabalho apropriadas; Wb = pΔV é condição suficiente na dedução acima, sem afirmar que todo processo precisa ser reversível.
- MIT OCW, *Unary Phase Transformations*: <https://ocw.mit.edu/courses/3-020-thermodynamics-of-materials-spring-2021/mit3_020s21_l10.pdf>. Contexto de equilíbrio e mudança de fase de substância pura.

No diretório raiz do repositório, execute `node auditoria/termodinamica/evidencias/QA-09/teoria-misturas-calorimetria-r19-20261030/verificar.mjs`. O script identifica fotografia, inventário e contêineres, verifica os cálculos e contrasta balanços. SHA-256 do script: `a5f6d4ab02e8e446185549a7e260727407ca715660955713cecf8a92b46da8be`. A inspeção científica dos textos e das condições é manual; o script não valida experimentalmente contramodelos nem garante correção fora deste recorte. Nenhum conteúdo de produto foi alterado neste lote.
