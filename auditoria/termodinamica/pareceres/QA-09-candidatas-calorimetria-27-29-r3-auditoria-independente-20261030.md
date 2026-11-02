# QA-09 — auditoria independente das candidatas de calorimetria, r3

Data: 30/10/2026. Auditor: agente automatizado `/root/next_theory`; Corretor: `/root/next_formulas`. **Veredito localizado: APROVADO para as três candidatas isoladas nas condições e fotografia especificadas.** A proposta não foi aplicada; este parecer não encerra QA-09 nem libera outro ID.

## Identidade e checagens

Formulário efetivo r11 SHA-256 `01d5d79639cd17dfcaea38479019cf719e2601f5b35d446ab562e50d381fa5c9`; inventário r11 `720f2b9ace69ab8f07be685d5205040569cc72814f67d51d44786872469c07d7`. Análise da r3 SHA-256 `844fc4f8e905caea8b7f4c617a8c019ebeba52e86d5d0b094615a71f9d1e61a7`; manifesto `b53d5e3156615bcf2a59ea25771f1d969d4447b4ab5442cb09094baa9336363d`; verificador do Corretor `caafd683715e4f9c4f3d7a1bdc1af2e1eebf417248bbf35950858460e7591249`.

Verificação independente em `evidencias/QA-09/auditoria-candidatas-calorimetria-27-29-r11-r3-20261030/verificar.mjs`, SHA-256 `bfea6a16fb8aefe84aa93c23b7a5d227db84a6e545b91c0cbf59c2f58ab9a357`, executada sem gravar no produto: três originais únicos e âncoras/intervalos corretos em r11; simulação com 100 fichas na mesma ordem, 97 fichas não alvo idênticas, todos os 191 elementos MathML preservados byte a byte, atributos de identificação, links e ARIA preservados. Cada substituição consta no texto visível e em `data-busca`. O verificador do Corretor também passou, inclusive nos contrastes numéricos. A verificação do atributo de busca não equivale a teste funcional real em navegador; não se realizou teste de acessibilidade.

## Exame científico

As fichas 27 e 28 passam a declarar condições suficientes para aproximar a contribuição de energia interna de cada porção por capacidade constante vezes variação de temperatura, incluindo o recipiente uma só vez. A 28 explicita `Eext=Qext−Wext`, evitando contar trabalho duas vezes. As condições respondem ao parecer anterior no domínio limitado proposto.

A ficha 29 responde aos apontamentos sobre r1 e r2: afirma substância pura em equilíbrio de fases, temperatura e pressão termodinâmica constantes durante toda a transformação, sem incluir calor sensível, sistema fechado e apenas trabalho `Wb=p(V₂−V₁)`. Com energia cinética e potencial desprezíveis, primeira lei e definição de entalpia dão `Q=ΔU+pΔV=ΔH`; a mesma diferença de entalpia específica entre fases vale para a massa transformada no modelo indicado. O uso de ℓ como magnitude preserva unidades e sinais apresentados. [MIT, derivação em pressão constante](https://web.mit.edu/10.213/oldpages/f99/supp/readings/qdh/index.html) apresenta a identidade para caso reversível; a candidata explicita a condição suficiente sobre o trabalho sem alegar que a reversibilidade integral seja universalmente necessária.

O parecer sobre r2 permanece como histórico: a igualdade de temperatura e pressão entre fases não dizia que eram constantes durante o processo. Na r3, a informação foi incluída tanto na condição visível quanto na busca. Essas hipóteses delimitam um modelo suficiente, não todos os casos de calorimetria ou de mudança de fase.

Qualquer aplicação requer nova fotografia e mapa, reconciliação de posições/referências e recursos, testes de busca e revelação, preservação dos itens não afetados e auditoria independente da versão efetivamente aplicada, além da reavaliação localizada de FOR-01. A aprovação aqui não presume essas etapas.
