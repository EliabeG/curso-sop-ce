# QA-09 — Auditoria independente de FUN-02 P1 e figura, r9

Data: 30/10/2026. Auditor: agente automatizado `/root/next_examples`, distinto do Corretor. **Veredito localizado: APROVADO para o caso P1, seus vínculos e a figura quantitativa nos limites abaixo.** QA-09 integral permanece em correção; não libera outro ID nem prova aprendizagem.

## Critério e fotografia

QA-09 requer conferência rastreável do conteúdo numérico, inclusive figuras, em todas as classes; esta revisão cobre apenas o caso P1 do pacote FUN-02, seu SVG e os dois vínculos de dados/scripts fora dos artigos. Não examina P2/P3 nem todos os recursos da disciplina. Li diretamente o HTML r9, o JSON, o SVG, o script e a entrega `fun02-figura-r9-20261030/entrega.md` (SHA-256 `f4624c06271f66cb70a9ea9ed7ed89ea19aebef0a333e6c5d5bf7ede649fb777`). O HTML SHA-256 `2d6b8fb2f9c99e04d22c19d7b32bbc3eb20577459d9132e506f9c0acef3f2fc2`, inventário r9 `023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d`, JSON `511aac986e9122e5498cdf69609274685791000a19f140a09d539fca01676319`, script `2fdd0e498c41db2f7f8e90d5114dcd015f5377e00901e6274f25262e13c79a70` e SVG `f324acce9060eb15eeab58958649392f4e5b667fbaf2ad9b63e3c68fbe3eae35` foram conferidos.

A figura pertence ao artigo `fun02-e1-caminhos`, segregado dos 197 artigos pelo inventário QA-09; o exame adicional do ativo não cria uma nova figura fora dos artigos e não transfere aprovação automaticamente a qualquer outro trecho. Os dois vínculos de dados e código estão fora desses artigos, sob `#fun02-dados`, posições UTF-16 252246 e 252344 e conferem diretamente no HTML.

## Recalculo independente

Dados são hipotéticos e internos; `R=8,314 J/(mol·K)` é aproximação de projeto. Para n=1 mol, A (300 K, 10 L) e B (450 K, 20 L), `p_A=249,420 kPa`, `p_B=187,065 kPa`; na rota isobárica o estado C está em 600 K, 20 L e 249,420 kPa; na isoterma D está em 300 K, 20 L e 124,710 kPa. Ambos estados intermediários estão entre os limites 250 e 650 K. Com calor específico molar constante `1,5R`, `ΔU=1,5(8,314)(450−300)=1870,65 J` em ambas as rotas.

A integral de pressão constante resulta `W_I=2494,20 J`. Recalculei a rota isotérmica por quadratura de Simpson independente com 10.000 subintervalos em L e kPa: `W_II=1728,8476977526154 J`, em acordo com `nRT ln(2)`. As unidades satisfazem 1 kPa·L=1 J. Pela primeira lei, com somente trabalho de fronteira e variações cinética/potencial desprezíveis, `Q_I=4364,85 J`, `Q_II=3599,49769775 J`. Ida por I e retorno por II invertida produz `W_ciclo=Q_ciclo=765,35230225 J` e `ΔU_ciclo=0`; a reversão térmica exige as hipóteses ideais do pacote. Os valores 2494,20; 1728,85 e 765,35 J na figura são consistentes com arredondamento à centésima; ±0,005 J é intervalo de apresentação, não incerteza experimental.

## Figura e evidência visual

Inspecionei a renderização isolada oferecida pelo Corretor: os estados A/C na isobárica, A/D na isoterma e as setas de C→B e D→B correspondem aos trajetos descritos. O SVG representa as duas trajetórias de A para B; o retorno II deve ser invertido no ciclo, como diz a legenda. A região sombreada fica entre isobárica e isoterma. Confirmei os 161 vértices isotérmicos, transformando coordenadas de volta para volume e pressão; maior discrepância à hipérbole `p=2494,2/V` foi 0,000515944 kPa, compatível com arredondamento das coordenadas. A área do polígono numérico forneceu 765,349161 J versus 765,352302 J pela integração analítica (diferença de −0,003141 J devido à aproximação poligonal e quantização); não foi usada para determinar o valor didático de referência. Conferi que o SVG e os marcadores refletem o quadro de estados e que o texto acessível e a legenda estão coerentes.

A função publicada `calcularFun02` executou 49 verificações internas, com W_I, W_II e ciclo iguais aos valores acima. O verificador independente [verificar_independente.py](../evidencias/QA-09/fun02-figura-auditoria-r9-20261030/verificar_independente.py), SHA-256 `60d61dac3a915cb03a25f576a183a09fd5d438856a443059886b1403ea67babd`, usa a quadratura, área do polígono, hashes e posições, sem escrita; executou com sucesso. Também executei o verificador do Corretor, que passou. Consultei [MIT §2.1](https://web.mit.edu/16.unified/www/SPRING/thermodynamics/notes/node14.html) para sinais e conservação e [OpenStax §3.4](https://openstax.org/books/university-physics-volume-2/pages/3-4-thermodynamic-processes) para trabalho quase estático e isoterma; elas fundamentam o modelo, não os números autorais.

## Quadro de alcance

| Critério localizado | Resultado |
|---|---|
| Identidade do SVG, JSON, código e contexto na fotografia | Atendido para hashes e vínculos identificados. |
| Estados, cálculos, unidades e aproximações de P1 | Atendido com hipóteses e precisão indicadas. |
| Eixos, curvas, setas, rótulos e área sombreada | Atendido na renderização isolada e no SVG; não há teste de navegador. |
| Correspondência de outros problemas e ativos | Fora do alcance; nenhuma aprovação presumida. |
| Critério integral QA-09 / próximo ID | Não atendido por este lote; permanece bloqueado. |

Não houve teste de navegador real, leitor de tela, aluno, revisão humana ou certificação externa. Não foram examinadas todas as descrições de acessibilidade, todas as referências ou os demais cálculos de FUN-02. O parecer anterior FUN-02 permanece vinculado a seu alcance e sua fotografia.
