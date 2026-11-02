# QA-09 — candidatas isoladas para as fichas 27–29, rodada r3

Data: 30/10/2026. Corretor: agente automatizado `/root/next_formulas`. Estado: **candidatas não aplicadas, aguardando revisão independente**. Elas respondem ao [parecer das fichas de fundamentos e calorimetria](../../../pareceres/QA-09-fichas-fundamentos-calorimetria-r10-auditoria-independente-20261030.md). QA-09 integral continua em correção e outro ID não está liberado. A rodada r3 responde à observação independente sobre o domínio de ℓ na ficha 29; a r1 é preservada.

## Hipóteses e alterações

- **27:** delimita o uso a um conjunto isolado de porções e recipiente de sólidos/líquidos em uma fase, capacidades apropriadas constantes que representem aproximadamente `ΔUᵢ=CᵢΔTᵢ`, efeitos de pressão/deformação e energia de mistura desprezíveis, sem reação ou mudança de fase; diz para incluir o recipiente uma vez ou desprezar sua capacidade. Esse é um modelo suficiente para o balanço ilustrado, não uma alegação de que seja o único modelo possível.
- **28:** delimita porções e recipiente ao mesmo modelo calorimétrico e explicita que `Eext=Qext−Wext` já inclui trabalho externo, sem contá-lo duas vezes. Mantém a possibilidade de energia externa e os sinais da ficha original. Para uma aplicação, as capacidades térmicas devem ser apropriadas para representar a variação de energia interna no modelo; não se devem ignorar efeitos mecânicos que sejam relevantes.
- **29:** especifica sistema fechado, substância pura em equilíbrio entre fases com temperatura e pressão termodinâmica p constantes durante a transformação, sem calor sensível incluído, apenas `Wb=p(V₂−V₁)`, sem outros trabalhos e com ΔEc/ΔEp desprezíveis. Identifica ℓ como magnitude da diferença de entalpia específica entre fases nas condições da transformação; restringir a substância pura em equilíbrio evita tratar como constante uma diferença de entalpia local em mistura com temperatura ou composição variáveis. Assim `Q=ΔU+Wb=ΔH`; fusão e vaporização recebem calor e as inversas o liberam no modelo indicado. A condição de trabalho pode ser satisfeita por processo quase estático, mas não se afirma reversibilidade como requisito universal.

As mudanças substituem a condição existente nas duas ocorrências de cada artigo (texto visível e `data-busca`), sem alterar as fórmulas, símbolos, unidades, links ou MathML. As condições são suficientes para os exercícios e não prometem abranger todos os casos físicos possíveis.

## Contrastes e testes

Para demonstrar por que C constante isoladamente não garante ΔU=CΔT, considere modelo fictício `u=cvT−a/v` com cv=1 kJ/(kg·K), a=1 kJ·m³/kg², 1 kg; expansão livre isolada de v=1 para 2 m³/kg e T de 300 para 299,5 K. Então `Δu=cvΔT−a(1/v₂−1/v₁)=−0,5+0,5=0`, mas `cvΔT=−0,5 kJ/kg`. Esse contramodelo de gás não se encaixa na nova hipótese de sólidos/líquidos e não demonstra que os exemplos de mistura do curso estivessem numericamente errados.

Para mudança de fase, contraste **apenas algébrico**, sem alegar processo físico completo: ΔH=200 kJ, p=100 kPa e ΔV=0,1 m³ implicam ΔU=190 kJ; se outro valor de trabalho Wb=5 kJ fosse imposto, Q=195 kJ em vez de ΔH. A candidata requer Wb=10 kJ nesse exemplo e elimina a ambiguidade; não afirma que pressão de fronteira diferente seja fisicamente compatível com cada trajetória arbitrária.

## Identidade e simulação

Formulário SHA-256 `01d5d79639cd17dfcaea38479019cf719e2601f5b35d446ab562e50d381fa5c9`; inventário r11 SHA-256 `720f2b9ace69ab8f07be685d5205040569cc72814f67d51d44786872469c07d7`. O manifesto registra âncoras, posições UTF-16 e hashes do artigo original e proposto. Cada original ocorre exatamente uma vez no formulário; cada condição substituída aparece duas vezes no artigo original. Os hashes de fragmentos excluem a quebra de linha final dos arquivos isolados.

`node auditoria/termodinamica/evidencias/QA-09/candidatas-calorimetria-27-29-r11-20261030-r3/verificar.mjs` faz apenas leitura e simulação em memória, confronta os dois documentos e substituições, e retornou `ok=true`: 100 fichas na mesma ordem, 97 não alvo byte a byte idênticas, MathML preservado nas candidatas e 191 elementos MathML no formulário. Testa também as contas dos contrastes. Isso não substitui leitura científica independente, testes de acessibilidade nem execução em navegador real.

Após parecer independente favorável, qualquer aplicação exige fotografia e mapa novos, reconciliação das posições/referências e recursos, verificação de busca e revelação, preservação das fichas/itens não afetados e reavaliação localizada de FOR-01. A versão efetivamente aplicada precisa de nova auditoria independente; nenhuma aprovação de proposta encerra QA-09.
