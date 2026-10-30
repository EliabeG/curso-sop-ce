# QA-09 — auditoria independente das candidatas de flashcards e resumo, r2

Data: 30/10/2026. Revisor: agente automatizado independente `/root/qa_diagnosticos`. **Veredito: APROVADAS as sete candidatas isoladas no alcance descrito**, com aplicação e reauditoria da versão efetiva ainda pendentes. Não conclui QA-09 nem libera outro ID.

## Identidade e alcance

As candidatas respondem às pendências dos pareceres de flashcards matemáticos/resumo e flashcards conceituais, com dois esclarecimentos adicionais sobre pressão intermediária. Examinei apenas essas sete propostas na fotografia r8, não todos os cartões ou a disciplina. O HTML `modulos/e1-termodinamica.html` tem SHA-256 `57b13f0d6386764f1cc46ce543013b0eb75f7bfa97ffbd63ea331f38bfc5af8c`; inventário r8 `ae75a258398c385398567457d98ebd49b9838c0c9a4eedc69ea8d2d72981b687`. Análise do Corretor `auditoria/termodinamica/evidencias/QA-09/candidatas-flashcards-resumo-20261030-r2/analise.md` SHA-256 `32003d5419d05d00e1a336ab023fa7ab183d0b01c40e08e192cff0c58cc544c4`; manifesto `dc906da64802545f62c4c7e232b16ca9737bb25abb1ae3d044c2fdad2dd76808`; script somente leitura `de986570cb2227ed50b927921931126ea35130eee5588f5d2ad36225de93d32a`.

Conferi cada original diretamente no HTML vigente, por posição UTF-16, ocorrência única e hash; cada candidata está ausente da versão atual. Cada trecho `antes` ocorre uma vez no original e sua substituição literal pelo trecho `depois` reconstrói a candidata correspondente. Os hashes abaixo são dos fragmentos **sem** a quebra final dos arquivos isolados. O script do Corretor retornou `ok=true`; seu hash de resultado `2d6b8fb2f9c99e04d22c19d7b32bbc3eb20577459d9132e506f9c0acef3f2fc2` é somente hipotético, não a versão aplicada.

| Candidata | SHA-256 sem quebra final |
|---|---|
| COP | `d5fb4be0c7fa1fd59c1e33f62548d6699ae5ef10bd440c5c0f2960318039cafd` |
| Válvula | `ed581a881c6c321528a4f060aee7a410528a4e74e955bd3f7208196439985ef1` |
| Compressor | `3683542f1df835e34f1cb3d19f8891beeec1ae83574fcfb7e2aa508ffc30aaeb` |
| Trocador | `76df1e61d560ded1aa22aedf761a54041b5f20cd1534754087be25356d2ea70c` |
| Resumo | `157535fb990ff134a40d24237b00af8513ee704ee0b867bc19153d89464ee07a` |
| Pressão, entrada/saída | `9bcafd2e58f5302ad7e191a85201089be19eef830ee19834743d9bd017a07ee0` |
| Pressão, 1/3 | `87614877fe961b9ef8ee8c93ecdc0600f831cde700864b1d50ced7adbebb58b5` |

## Modelos e verificações

- **COP:** para ciclo de compressão cujo acionamento é somente trabalho, a candidata distingue Q_L/W de refrigerador e Q_H/W de bomba de calor, com calor e trabalho na mesma base e fronteira. A resposta é explicitamente restrita à classe descrita; não generaliza o denominador a sistemas acionados por calor, como absorção. Não é avaliação do desempenho real de equipamento ou de todos os auxiliares fora da fronteira.
- **Válvula:** no modelo estacionário de uma entrada/saída, conservação da massa fornece vazões iguais; balanço de energia sem calor, trabalho não associado ao escoamento e variações cinética/potencial relevantes dá h₁≈h₂. As hipóteses adicionadas resolvem a ausência de restrição à acumulação. A aproximação não afirma transformação reversível.
- **Compressor:** com mesma entrada e pressão de saída para referência e caso real, regime permanente, uma entrada e saída, adiabático e energias cinética/potencial desprezíveis, trabalho específico de entrada iguala elevação de entalpia. A razão das elevações isentrópica e real coincide com trabalho de entrada isentrópico dividido pelo real. O índice isentrópico identifica a referência, não o processo real.
- **Trocador:** sob adiabaticidade externa, regime permanente e uma entrada e saída representativas por corrente sem perda de massa entre elas, `Ṡgen=Σṁ(s_saida−s_entrada)`; a soma pode ser positiva apesar da ausência de calor através da fronteira externa. A acumulação de um volume transiente não é ignorada fora desse modelo.
- **Resumo:** para massa fixa, balanço de entropia com calor zero e geração interna zero leva a ΔS=0; para volume de controle estacionário com uma entrada e saída, a conservação da massa e o mesmo balanço levam a s_saida=s_entrada. O texto não aplica essa conclusão à entropia média de um volume transiente cuja massa varia.
- **Pressões intermediárias:** nas hipóteses agora explicitadas, cada compressão adiabática usa o mesmo gás ideal, cₚ e cᵥ constantes, mesma eficiência isentrópica, mesma vazão e temperatura de entrada restaurada pelo resfriamento perfeito, em regime permanente e sem perdas de pressão. Para `a=(γ−1)/γ>0` e razões `r₁=p_i/p₁`, `r₂=p₃/p_i`, o trabalho por massa é proporcional a `(r₁ᵃ−1)+(r₂ᵃ−1)`; o produto `r₁r₂=p₃/p₁` é fixo. A soma é mínima quando `r₁ᵃ=r₂ᵃ`, logo `p_i=√(p₁p₃)`. Para 1 e 16 bar absolutos, p_i=4 bar. Condições reais diferentes podem deslocar o ótimo; a candidata não transforma a fórmula em regra universal.

A preservação das expressões MathML e legendas nos cinco cartões numéricos foi conferida por delta literal; não foram executados navegador nem leitor de tela. Após aplicação, a mudança dos hashes e posições exige nova fotografia e reconciliação por identidade, contexto e alcance. Conferir especificamente os 197 artigos e registros, links, scripts de flashcards, comportamento e dependências afetadas; não transportar automaticamente aceites de r8. Esta revisão não valida o texto que ainda não foi incorporado ao produto.

| Critério localizado | Resultado |
|---|---|
| Originais, candidatas, deltas e hashes | Atendido na fotografia r8; candidatas continuam isoladas. |
| Resolução das hipóteses dos quatro achados e COP | Atendido no modelo e na fronteira explicitados. |
| Finalidade e hipóteses dos cartões de pressão | Atendido para a minimização no modelo ideal delimitado. |
| Versão efetiva, regressão e revalidação após aplicação | Ainda não executados; novo parecer obrigatório. |
| QA-09 integral e próximo ID | Não atendidos; permanecem bloqueados. |

Não houve teste com estudantes, revisão humana ou certificação externa. Uma aprovação localizada não significa que o curso seja avançado como um todo.
