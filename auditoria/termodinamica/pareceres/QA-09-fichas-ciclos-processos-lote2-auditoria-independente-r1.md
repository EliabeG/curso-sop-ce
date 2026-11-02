# QA-09 — auditoria independente de seis fichas de ciclos e processos, r1

Data: 30/10/2026. Revisor automatizado independente `/root/qa_oficina`. **Veredito: APROVADO para os coeficientes e expoentes do lote delimitado**, na fotografia examinada. Esta revisão não aprova integralmente as seis fichas, todas as fórmulas do curso, QA-09 ou o curso avançado; não libera o próximo ID.

## Critério e identidade

QA-09 requer inventariar e recalcular todo o conteúdo numérico externo aos itens BAN-08, incluindo fichas. Aqui o escopo abrange unicamente os coeficientes e expoentes das fichas 70, 81–83 e 89–90 e as hipóteses relevantes na entrega. Formulário `formulas/termodinamica.html`, SHA-256 `c27422b409a0a755448982c4074c6d6967fd3e91d7eae20274e218530f5c37b0`. Conferi diretamente cada ficha no HTML e sua árvore MathML: frações, índices, expoentes, sinais e limites aplicáveis. A comparação entre posições de bytes, IDs únicos e hashes dos seis fragmentos do `resultado.json` foi feita independentemente na mesma fotografia; os números identificam a versão e não autorizam transferência de aceite a outras.

## Conferência científica e numérica

- **70:** para gás ideal de composição fixa, `cp`, `cv` constantes e estados isentrópicos, `Δs=cp ln(T₂/T₁)−R ln(p₂/p₁)=0`; `R/cp=(k−1)/k`, derivando o expoente da ficha. De `pv^k=cte`, `T₂/T₁=(v₁/v₂)^(k−1)`. Teste artificial `k=1,5`, `p₂/p₁=8`, `v₁/v₂=4` dá 2 por ambas as relações.
- **81:** no Brayton ideal com isentrópicas e isobáricas, calor específico constante, `a=rp^((k−1)/k)=T₂/T₁=T₃/T₄`, portanto `qout/qin=1/a` e `η=1−1/a`. Para o ciclo artificial indicado na entrega, `a=2`, `qin=cp×600`, `qout=cp×300`, `η=0,5`.
- **82:** no Otto ar-padrão ideal de capacidades constantes, com duas isentrópicas e duas isocóricas, `qout/qin=1/r^(k−1)`. Para `r=16`, `k=1,5` e temperaturas fornecidas, `qin=cv×1200`, `qout=cv×300`, `η=0,75`.
- **83:** Diesel ar-padrão ideal requer dois trechos isentrópicos, adição isobárica, rejeição isocórica e `1<rc<r`, `r>1`, `k>1`. Na amostra artificial, `qin=cp×3600`, `qout=cv×2100`, `cp/cv=1,5`; `η=1−2100/5400=11/18≈0,611111`. A fórmula na árvore coincide com a relação de `r`, `rc` e `k` do material docente BYU.
- **89:** em escoamento permanente internamente reversível, desprezando EC/EP, o trabalho de eixo recebido específico é `∫v dp`; gás ideal e `pv^n=cte`, para `n>0`, `n≠1`, produzem `nRT₁/(n−1)[(p₂/p₁)^((n−1)/n)−1]`. Para `n=2`, `RT₁=100 kJ/kg` e `p₂/p₁=4`, dá `200 kJ/kg`. Não é diretamente a integral de trabalho de fronteira de sistema fechado.
- **90:** na compressão isotérmica interna reversível, `v=RT/p` fornece `RT ln(p₂/p₁)`; teste `RT=100 kJ/kg` e razão `e` resulta `100 kJ/kg`. Pressões devem ser absolutas positivas e a razão adimensional. O limite politrópico quando `n→1` coincide sob estas condições.

Os números do teste são artificiais para verificação algébrica, não propriedades de ar real ou exercício reproduzido do curso. As idealizações de Otto e Brayton foram confrontadas com [MIT, capítulo 5](https://ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_5.htm); a expressão de Diesel e a razão de corte com [BYU, Thermodynamic Cycles](https://ignite.byu.edu/che433/lectures/lecture_06_thermo2/slides.html). As deduções acima foram reconstruídas a partir das leis e dos modelos. As temperaturas artificiais altas não foram validadas como adequação de cp constante a um gás real.

## Evidências e critérios

Inspecionei `verificar.py` e o executei com saída dirigida a arquivo temporário: o JSON resultante equivale semanticamente a `resultado.json`. O programa lê o HTML e produz texto, sem regravar evidências; a inspeção de MathML e as relações acima são verificações adicionais independentes. Não se executou navegador ou tecnologia assistiva.

| Critério desta amostra | Resultado |
|---|---|
| Versão, localização, IDs e hashes dos seis artigos | Atendido na fotografia informada. |
| Hipóteses, expoentes, coeficientes e sinais | Atendido no recorte, com os modelos e domínios expostos. |
| Fonte e reprodução dos testes artificiais | Atendido no alcance acima; não representam experimentos. |
| Todos os números, índices e fórmulas das fichas e QA-09 integral | Não atendido nesta amostra; permanecem pendentes. |
| Próximo ID | Não liberado; QA-09 ainda em correção. |

Não houve revisão humana, aplicação a estudantes, ensaio em navegador nem certificação. Não identifiquei ajuste obrigatório nas ocorrências examinadas.

## SHA-256

- Entrega: `9cabfb28a811b16735588c88de8ceb5229eea48b19d49dd6db502e03e4656b8f`.
- Script: `82d12f69e184f1ec31cf880006f2b844ea7fcbd0cdda3d4b09ca380cac0c18d0`.
- Resultado: `f8ad48d09362c76b9253e7f6ce81efaa742802f9ccc961c3232b5d4d8b2b21a4`.
- Formulário: `c27422b409a0a755448982c4074c6d6967fd3e91d7eae20274e218530f5c37b0`.
