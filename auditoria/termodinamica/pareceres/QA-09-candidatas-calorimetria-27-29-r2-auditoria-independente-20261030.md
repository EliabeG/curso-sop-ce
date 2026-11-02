# QA-09 — auditoria independente das candidatas de calorimetria, r2

Data: 30/10/2026. Auditor: agente automatizado `/root/next_theory`; Corretor: `/root/next_formulas`. **Veredito localizado: AJUSTE OBRIGATÓRIO na ficha 29; fichas 27 e 28 sem objeção no escopo examinado.** A proposta r2 não foi aplicada; este parecer não encerra QA-09 nem libera outro ID.

## Identidade e checagens

Formulário efetivo r11 SHA-256 `01d5d79639cd17dfcaea38479019cf719e2601f5b35d446ab562e50d381fa5c9`; inventário r11 `720f2b9ace69ab8f07be685d5205040569cc72814f67d51d44786872469c07d7`. A análise da r2 é `ab5b9faa28ac89668cab10d3de679a73cba247f0e3c050ce12b16f505ee5becc`; manifesto `9df3459d7595736f2265e66c71c634678bd20080372e74d103e94fd8a8258ec7`; verificador do Corretor `9d42a39898acbd95fcda8b31e35e77c95046885db659a6383cadb2bdf7c5b33d`.

Verificação independente em `evidencias/QA-09/auditoria-candidatas-calorimetria-27-29-r11-r2-20261030/verificar.mjs`, SHA-256 `d170ba7150d20f8b51cf36eff52e5eb7e791af78fe44c861fefb92b2d2e684ed`, executada sem gravar no produto: três originais únicos e âncoras/intervalos corretos em r11; simulação com 100 fichas na mesma ordem, 97 fichas não alvo idênticas, 191 elementos MathML preservados, atributos de identificação, links e ARIA preservados. Cada substituição consta no texto visível e em `data-busca`. O verificador do Corretor também passou. Não se realizou teste real em navegador, nem de acessibilidade.

## Exame científico

As fichas 27 e 28 passam a declarar condições suficientes para aproximar a contribuição de energia interna de cada porção por capacidade constante vezes variação de temperatura, incluindo o recipiente uma só vez. A 28 explicita `Eext=Qext−Wext`, evitando contar trabalho duas vezes. As condições respondem ao parecer anterior no domínio limitado proposto.

Na 29, restringir a substância pura e equilíbrio de fases corrige parte da lacuna apontada na primeira candidata: misturas podem apresentar variações de composição e temperatura durante a mudança de fase. A condição de trabalho `Wb=p(V₂−V₁)`, sem outros trabalhos, além de ΔEc e ΔEp desprezíveis, é uma hipótese suficiente para `Q=ΔH` quando p é constante; veja [MIT, derivação em pressão constante](https://web.mit.edu/10.213/oldpages/f99/supp/readings/qdh/index.html). Porém, embora a **análise** afirme pressão constante, o **cartão** diz apenas que as fases estão à mesma temperatura e pressão p. Igualdade das condições das fases não afirma que esses valores permaneçam constantes durante a transformação: por exemplo, ao longo de estados de saturação a pressão e temperatura de equilíbrio podem mudar. Nessa trajetória uma diferença de entalpia local entre fases pode variar e não se justifica uma única ℓ constante multiplicada por toda a massa transformada.

**Ajuste obrigatório:** explicitar no próprio texto visível e em `data-busca` que a temperatura e a pressão termodinâmica p permanecem constantes durante toda a transformação, mantendo as demais condições. Isso torna rastreável a hipótese alegada na análise e restringe o domínio suficientemente para o modelo. A igualdade `Q=ΔH` não exige alegar reversibilidade completa universalmente. O exame não conclui que todos os casos físicos de mudanças de fase pertencem ao modelo.

A aplicação exige nova candidata com sua própria identidade e parecer, nova fotografia e mapa, testes de busca e revelação e auditoria da versão aplicada. Nenhuma dessas etapas foi presumida neste parecer.
