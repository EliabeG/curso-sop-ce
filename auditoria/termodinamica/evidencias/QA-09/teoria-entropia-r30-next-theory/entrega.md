# QA-09 — expansão livre, entropia e conexão com exergia, r30

30/10/2026. `/root/next_theory`. **Nenhum erro científico substantivo identificado no recorte; aguardando revisão independente.** Não houve edição do produto ou dos controles. Este trabalho não estabelece cobertura integral de entropia/exergia, mérito de outras regiões ou conclusão de QA-09.

## Fotografia e escopo

Fotografia efetiva `modulos/e1-termodinamica.html`, SHA-256 `c719adae3464fb56ed2b0ad7014e0721c0aab2da444fb484ec0b40c5c0c8fbd4`. Leitura integral específica do bloco `base-expansao-livre`, delimitado pelo contêiner UTF-16 `[204817,207046)`, SHA `f3405521cea64595e48e1b03da18afcb10d4017fe78f3d9b7009573dc46408cd`. Os blocos `base-entropia-gas` e `base-exergia` já foram revisados na r13 em `teoria-segunda-lei-entropia-r13-20261030`; foram consultados aqui apenas para conferir a conexão e confirmar suas identidades integrais inalteradas, não apresentados como nova cobertura integral. O verificador `verificar.mjs` fixa as identidades e reproduz as contas. Leitura e ciência não se reduzem a hashes ou cálculos automatizados.

## Expansão ideal

O recorte define recipiente rígido, fechado e isolado com gás ideal inicialmente em um compartimento e vácuo no outro, sem outro trabalho e com variação de energia cinética/potencial desprezível entre estados de equilíbrio. Na fronteira adotada, Q=W=0 e ΔU=0; para massa e composição fixas de gás ideal com capacidade térmica física positiva, U depende de T e os estados inicial e final têm mesma temperatura. A expansão não é quase estática e não existe pressão de equilíbrio uniforme que se possa integrar como se o processo real fosse reversível. Igualdade da temperatura **dos estados extremos** não implica que uma temperatura uniforme seja definida durante toda a expansão.

Como S é propriedade, uma trajetória reversível isotérmica auxiliar entre os mesmos estados fornece ΔS=mR ln(V₂/V₁), sem afirmar que a transferência de calor real seja a dessa trajetória. Para m=1 kg, R=0,287 kJ/(kg K) e V₂/V₁=2, ΔS=0,198933 kJ/K, arredondado 0,199; como a fronteira é fechada e adiabática, Sger=ΔS. Uma expansão reversível isotérmica auxiliar, para os mesmos estados com T=300 K, trocaria Q=W=mRT ln2≈59,680 kJ, enquanto na expansão livre os valores reais são zero. Comparar trajetórias de mesma mudança de estado não torna a transformação real reversível.

A relação de Gouy–Stodola já apresentada em `base-exergia`, aplicada à geração calculada com ambiente de referência a T₀=300 K e fronteira que inclui gás e o espaço inicialmente evacuado, resulta em destruição de exergia de 59,680 kJ. Essa é exergia destruída no processo e não deve ser identificada sem balanço com a exergia inicial do gás isoladamente, pois o vácuo, fronteira, ambiente e outras transferências influenciam a contabilidade. Não há alegação de teste de equipamento real.

## Contraste de gás real

A afirmação de que U constante não garante T constante para gás real está correta. Exemplo sintético de van der Waals, um mol com energia interna U=cv T−a/v, cv=20 J/(mol K), a=0,3658 Pa m⁶/mol² e volumes molares de 0,010 para 0,020 m³/mol: U₂=U₁ e T₁=300 K levam a T₂=299,0855 K. Para b=0,0000427 m³/mol, p=RT/(v−b)−a/v² fornece p₁≈246,846 kPa e p₂≈123,688 kPa. Constantes e equação são modelo didático, não uma medição de fluido nem prova de que cada gás real sempre resfrie; o sinal pode depender do modelo e do estado. O exemplo preserva unidade e condições de equilíbrio inicial/final.

Fontes primárias: [MIT, segunda lei e comparação entre expansão livre e reversível](https://www.ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_7.htm); [MIT OCW, variação de entropia de gás ideal e expansão livre](https://ocw.mit.edu/courses/16-050-thermal-energy-fall-2002/0d600615983322e758cd9d75fa3b6758_04_part1b.pdf). O contraste van der Waals é cálculo sintético independente, não dado retirado das fontes.

Sem avaliação visual em navegador, leitores de tela, prática com estudantes ou revisão humana; fontes e contas do recorte não demonstram competências avançadas completas.
