# QA-09 — candidata isolada para o diagnóstico 23, r13

30/10/2026. Preparada por `/root/next_examples`; **não aplicada e pendente de revisão independente**. A candidata responde ao achado em `auditoria/termodinamica/pareceres/QA-09-diagnosticos21-25-r13-auditoria-independente-20261030.md`; não implica aprovação do lote nem conclusão de QA-09.

## Identidade e alteração

Fonte r13 `modulos/e1-termodinamica.html`, SHA-256 `f19000a7ddb1f3552b9633b0efec266fb3f6c5e5065808505a2f65b2005aefbc`; inventário r13 SHA-256 `0df99b79bcc2350581fcdded72435d30d07858de237a549e6228ca73682f8d9b`. Na seção `#preparacao-questoes`, o bloco `<div class="exemplo">` com `h3` “23. Misturador com calor recebido” ocupa o intervalo UTF-16 [534074, 534884), hash `e5e87b30397cc0394b10b1194461e7bf64fd0e831184d4b91eeae0d234cd5073`. `original-r13.html` reproduz esse bloco; `candidata.html`, hash `7ff95d0d97ccbf5c2fa3475c0d5d4019fb2657686e4daebc3d55536fc9b66d10`, altera uma única frase:

- Antes: “Duas correntes entram em regime permanente: 2 kg/s a 100 kJ/kg e 1 kg/s a 400 kJ/kg.”
- Candidata: “Duas correntes entram em regime permanente: a primeira tem vazão mássica de 2 kg/s e entalpia específica de 100 kJ/kg; a segunda tem vazão mássica de 1 kg/s e entalpia específica de 400 kJ/kg.”

Os demais bytes do bloco ficam iguais, inclusive resolução, hipóteses já declaradas e links para as bases. A candidata mantém o exercício e identifica o tipo de energia fornecido, que a unidade sozinha não identifica.

## Contramodelo e solução

O parecer independente aponta a ambiguidade. Para ilustrá-la, imagine, apenas como contramodelo, um mesmo gás ideal fictício com cᵥ = 0,718 e R = 0,287 kJ/(kg·K), de modo que cₚ = 1,005 kJ/(kg·K), e referência comum u = cᵥT e h = cₚT. Se 100 e 400 kJ/kg designarem **energias internas específicas** das entradas, suas entalpias são, respectivamente, (1,005/0,718)×100 ≈ 139,972 e (1,005/0,718)×400 ≈ 559,889 kJ/kg. No misturador adiabático com vazões 2 e 1 kg/s, h₃ ≈ 279,944 kJ/kg. Este cenário serve para demonstrar a lacuna do texto anterior; não são dados adicionados ao exercício e não contraria a candidata, que agora nomeia as grandezas.

Com as entalpias fornecidas pela candidata e o balanço da base `#base-misturador-correntes` (referência comum e apropriada, permanente, uma saída, sem trabalho ou mudanças cinética/potencial), ṁ₃ = 3 kg/s e h₃ = (2×100+1×400)/3 = 200 kJ/kg em condição adiabática. Com 30 kW de calor líquido recebido, h₃ = (600+30)/3 = 210 kJ/kg. O balanço determina entalpia, não temperatura ou fase sem dados adicionais. Valores são nominais; não se inferem precisão instrumental ou propriedade de uma substância real.

## Verificação e alcance

`python3 auditoria/termodinamica/evidencias/QA-09/candidata-diagnostico23-r13-20261030/verificar.py` executa leitura do r13, verifica os hashes de ambos os blocos e presença única, prova a alteração textual exata, simula em memória e reverte byte a byte, confere a contagem de artigos e recalcula ambos os resultados. O teste não escreve no produto, não examina em navegador e não valida por si o modelo físico nem todos os links. A aplicação, se aceita e autorizada, exigirá nova fotografia e mapa, reconciliação dos 197 artigos, checagem de links e inspeção independente da versão efetiva. Pedimos a outro Auditor examinar original e candidata, contramodelo, solução e preservação antes de qualquer aplicação.
