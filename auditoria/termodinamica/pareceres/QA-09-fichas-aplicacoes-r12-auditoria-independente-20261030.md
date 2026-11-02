# QA-09 — auditoria das fichas de compressores e aplicações, r12

Data: 30/10/2026. Auditor: agente automatizado independente `/root/next_graphics`. **Veredito localizado: AJUSTES OBRIGATÓRIOS nas fichas 88 e 99 para explicitar hipóteses.** Não foram identificadas divergências nas demais nove fichas no alcance abaixo. QA-09 permanece em correção e o próximo ID não está liberado.

## Fotografia e método

Formulário `formulas/termodinamica.html` SHA-256 `6857fd83e0b2e49c804903cff1dea4128a665ab22eb27bac4ab15d6c557ff756`; inventário r12 `457a56300aab8f612ebb7f136c7c2f62520abb49c005c209a238925179248d0e`. São examinadas as fichas 87, 88, 91–95 e 97–100, com posições e hashes individuais em `evidencias/QA-09/fichas-aplicacoes-r12-20261030/identidades.json`, SHA-256 `9a580c0daf5b33d97d1e460309ce8e54307928f237563dfe6567580a7d972ff1`; entrega do Corretor SHA-256 `423413f814659a9c97138d2266dd75af1f599c31a3b9e32d94c252c8b170d524`.

Li os cartões e os MathML da versão efetiva e confrontei cada fragmento com o índice r12. `evidencias/QA-09/auditoria-fichas-aplicacoes-r12-20261030/verificar.py`, SHA-256 `56d341159235d34c33c7491b5105f9028e2630230c498c89cd681d0d874f946b`, executado sem gravação, reproduziu as 11 identidades e aritmética fictícia. A verificação de ciência e condições é a análise textual abaixo, não a saída do programa sozinha. Os exemplos não são medições nem dados importados das fontes.

## Ficha 88 — pressão intermediária

A derivação convencional `p_i=√(p₁p₃)` segue quando os dois compressores operam em **regime permanente** como volumes de controle adiabáticos, com mesmo gás ideal, cp e cv constantes, eficiências isentrópicas iguais e constantes, intercooling perfeito até T₁ sem perda de pressão, mesmas vazões, sem mudança de fase e ΔEc/ΔEp desprezíveis. Com `a=(k−1)/k>0`, `r₁r₂=p₃/p₁=16`, a soma de trabalhos específicos é proporcional a `r₁^a+r₂^a−2`, mínima quando r₁=r₂=4, logo p_i=4 bar absolutos para p₁=1 e p₃=16 bar.

O cartão lista as hipóteses de fluido, eficiência, vazão e resfriamento, mas não declara regime permanente. Igualdade das vazões pode eliminar acúmulo de massa sem eliminar mudança da energia armazenada; se houver acumulação energética, o balanço de um estágio inclui `dE_VC/dt` e o trabalho instantâneo não é determinado só por ṁΔh. Isso não demonstra que qualquer transiente tenha ótimo diferente, mas mostra que o resultado estacionário não decorre das hipóteses visíveis. **Ajuste obrigatório:** explicitar regime permanente em ambos os estágios na descrição e manter as demais condições e pressões absolutas; não afirmar que o ótimo vale sem elas. As bases e cartões anteriores que o enunciam também não substituem uma hipótese essencial em ficha isolada.

## Ficha 99 — geração e calor por convecção

Em regime permanente, se `q‴` representa a geração térmica volumétrica total considerada, sem qualquer outra entrada ou saída de energia não contabilizada e com apenas uma face trocando calor por convecção, `q‴V=hA(T_s−T_∞)`. O exemplo artificial q‴=100000 W/m³, V=0,01 m³, h=10 W/(m²·K), A=2 m² resulta em 1000 W e ΔT=50 K. As hipóteses de temperatura uniforme na face, h médio, h>0 e A>0 estão presentes.

A ficha exclui outras **perdas**, mas não caracteriza expressamente se a geração informada engloba todas as entradas/conversões energéticas ou se existe outro aporte independente. Se, num balanço hipotético, além da geração térmica declarada houvesse 200 W de aporte mecânico líquido independente que não estivesse incluído em `q‴`, seriam 1200 W a rejeitar e ΔT=60 K. **Não se pode contar duas vezes** a dissipação mecânica se ela já estiver incorporada em `q‴`; nesse caso a geração total usada na equação já deve incluir seus 200 W. O exemplo revela a necessidade de definir a fronteira e a contabilidade energética, não uma prova de que um bloco específico tenha essa entrada. **Ajuste obrigatório:** dizer que `q‴` é o total de geração térmica relevante e não há outros aportes não contabilizados, ou especificar o balanço alternativo; preservar a exclusão de outras perdas e o regime permanente.

## Outras fichas

A leitura e recálculo confirmaram, sob as hipóteses escritas: 87 ηv=0,8; 91 q″x=20 W/m² e Q̇=60 W; 92 Q̇=600 W; 93 Q̇=600 W; 94 ΔTm=20 K e Q̇=40000 W; 95 1/U=0,026 m²·K/W e U=500/13≈38,461538 W/(m²·K); 97 razão 2 para mesmo modelo e perda inicial não nula; 98 ΔL=0,0012 m; 100 volume=3 m³ e área da face=6 m². 95 exige parede plana e área comum; 97 depende especificamente do modelo de radiação da ficha 96 e não afirma validade para trocas radiativas arbitrárias. A revisão localizada da ficha 97 não aprova integralmente a ficha 96.

## Fontes e decisão

Consultei a [folha MIT 2.051 de transferência de calor](https://ocw.mit.edu/courses/2-051-introduction-to-heat-transfer-fall-2015/e32f70f7e00f34953447b606cea0421f_MIT2_051F15_EqnSheet_Q2_v3.pdf), especialmente p. 1 para Fourier, convecção, resistências e geração no regime estacionário; o [guia NIST SP 960-11, §6.3.1.3](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication960-11.pdf), para coeficiente de dilatação; e o [resumo do artigo de Lugo-Méndez et al., 2021](https://pubmed.ncbi.nlm.nih.gov/33804170/) para limites de modelos de pressão intermediária. O texto integral do artigo não foi examinado nesta revisão; a derivação do ótimo apresentada acima é para o modelo explícito e não se atribui a essa fonte os valores fictícios. Os números são testes autorais.

| Critério do lote | Decisão |
|---|---|
| Fotografia, 11 identidades e contas nominais | Atendido. |
| Ficha 88: hipóteses do ótimo | Não atendido: regime permanente não explícito. |
| Ficha 99: fronteira e contabilização de energia | Não atendido: total de fontes e aportes não está explicitado. |
| Demais nove relações | Sem divergência no alcance e modelos informados. |
| QA-09 integral, FOR-01 e próximo ID | Pendentes: requer candidatas e revisão da versão efetiva, com revalidação de alcance. |

Após candidatas e parecer independente, qualquer aplicação exige nova fotografia/mapa, verificação das outras fichas, links e comportamento afetado e exame da validade de FOR-01 na versão aplicada. Não houve navegador real, leitor de tela, teste com alunos, revisão humana ou certificação externa nesta revisão.
