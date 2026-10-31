# QA-09 — auditoria independente da aplicação das fichas 27–29 e 52–53, r12

Data: 30/10/2026. Auditor automatizado `/root/planning`, distinto de `/root/next_examples` (aplicação) e `/root/next_formulas` (candidatas). **Veredito: APROVADO no alcance localizado dos cinco deltas e da revalidação descrita.** QA-09 integral permanece em correção e o próximo ID não está liberado.

## Critério e versões

QA-09 exige inventário e recálculo do conteúdo numérico além dos 197 artigos, incluindo fichas e explicações. Esta auditoria verifica apenas as cinco candidatas, a versão efetiva, a reconstrução, o mapa e os efeitos locais sobre FOR-01; não aprova o restante do ID ou o curso inteiro.

Aula, sem modificação nesta etapa, SHA-256 `f76c39a3e1d8c349ebf0df72cc20a3ab21c68960c8451799bad90a9dcc4bd8c7`. Formulário r11 `01d5d79639cd17dfcaea38479019cf719e2601f5b35d446ab562e50d381fa5c9`; formulário r12 efetivo `6857fd83e0b2e49c804903cff1dea4128a665ab22eb27bac4ab15d6c557ff756`. Inventários r11 `720f2b9ace69ab8f07be685d5205040569cc72814f67d51d44786872469c07d7` e r12 `457a56300aab8f612ebb7f136c7c2f62520abb49c005c209a238925179248d0e`; mapa r11→r12 `1c67bdda8f5996c6a230e4556277dbbfac270e64ec5b2ac0cabccdee4b3680ef`. A [entrega do Corretor](../evidencias/QA-09/aplicacao-fichas-calorimetria-co2-r12-r1/entrega-r1.md) tem SHA-256 `a9a48d7b2192869008a88698a94e37dfd42681bf6d993a33b7793d313925e8d9`.

## Identidade e ciência

Reconstruí o formulário r12 a partir da fotografia r11 e dos cinco pares original/candidata já examinados, por substituições literais únicas; o resultado é idêntico byte a byte ao formulário efetivo e à fotografia posterior. A aula antes, depois e efetiva é idêntica. O verificador independente [verificar.mjs](../evidencias/QA-09/auditoria-aplicacao-fichas-r12-independente-20261030/verificar.mjs), SHA-256 `cb4e08ea4a1b02e7ae28183578b63ab3cb7c435a0c3417c52319b66522b94ef6`, confirmou os hashes individuais e a ordem e unicidade dos cinco pares.

- **Ficha 27:** para o conjunto isolado, somar ΔUᵢ≈Cᵢ(Tf−Ti) e desprezar energia de mistura, deformações e demais termos conforme a ficha resulta em `ΣCᵢ(Tf−Ti)=0` e `Tf=ΣCᵢTi/ΣCᵢ` para soma de capacidades não nula. Porções e recipiente devem ser contabilizados uma vez. Teste artificial de 1 e 3 kg do mesmo líquido com c constante, a 20 e 60 °C, resulta Tf=50 °C; não é modelo universal para qualquer material ou mudança de fase.
- **Ficha 28:** a mesma soma inclui o recipiente e iguala `Eext=Qext−Wext`, com calor recebido e trabalho saindo positivos. O trabalho externo já faz parte de Eext e não deve ser duplicado. Com capacidades hipotéticas 1, 3 e 1 kJ/K, temperaturas 20, 60 e 20 °C e Eext=30 kJ, Tf=(20+180+20+30)/5=50 °C no modelo.
- **Ficha 29:** para substância pura em equilíbrio durante a mudança de fase a p e T constantes, com massa fechada, apenas trabalho de fronteira `Wb=pΔV` e ΔEc/ΔEp desprezíveis, Q=ΔH. Se m transforma e ℓ é a magnitude da diferença de entalpia específica entre fases, |Qfase|=mℓ; por exemplo, 2 kg×200 kJ/kg=400 kJ. As restrições impedem usar o valor como calor universal em trajetórias com outros trabalhos ou aquecimento sensível não contabilizado.
- **Fichas 52–53:** o modelo diluído e bem misturado requer G e vazões volumétricas na mesma referência de T e p do ambiente, com conversão quando fornecidas em outra base. Para uma conversão hipotética de gás ideal a mesma pressão, 0,010 m³/h a 600 K corresponde a 0,005 m³/h a 300 K. Com V=300 m³, V̇=30 m³/h, Ce=0,0004 e Ci=0,0006, a taxa inicial é (0,005+30×(0,0004−0,0006))/300 = −3,333… ppm/h; no caso estacionário com excesso de 0,001, V̇=5 m³/h. Estes são testes do modelo, não medições; outras pressões e comportamento real exigem conversão apropriada.

Os exemplos são artificiais, com dados nominais e unidades indicadas, sem incerteza instrumental. As expressões são exatas no modelo quando as aproximações declaradas forem adotadas; igualdade de resultado didático não valida uma instalação ou experimento real.

## Preservação, mapa e comportamento

Das 100 fichas, apenas as cinco indicadas mudaram; as outras 95 são byte a byte idênticas, na mesma ordem. Os 191 elementos MathML do formulário são idênticos. A aula e seus 197 artigos mantêm-se iguais; o inventário oficial também permanece com SHA-256 `f2605176763a61832417506517373a16736717d5cc23de7494e901322c394856`. Os 103 vínculos das fichas para a aula apontam a 50 destinos existentes; a existência do destino não comprova qualidade didática ou acessibilidade.

O verificador independente [mapa.mjs](../evidencias/QA-09/auditoria-aplicacao-fichas-r12-independente-20261030/mapa.mjs), SHA-256 `56acfd27f6a8a23d47e6abdb32bb71a5e39accc5f975ef012376582ea84c697d`, examinou todos os 11.397 pares: 11.238 externos com deslocamentos esperados e 159 internos com hashes reconstituídos nas duas fotografias. Foram 15 hashes internos diferentes e dois externos de seções ancestrais. As 815 referências preservam seus valores e metadados; os 138 registros de recursos mantêm vínculos e têm seus hashes atuais conferidos, com três registros apontando para o formulário atualizado. Os seis ativos específicos não mudaram. O [parecer de apoio independente](QA-09-mapa-r11-r12-apoio-auditoria-independente-r1.md), SHA-256 `b7bab4fa4dc8fb37e9755052056714f8d5480647acf21f92d1f840c9dfd114bc`, concluiu a mesma correspondência estrutural. Hash igual ou mapeamento não transfere automaticamente outros aceites.

O validador canônico passou com 197 itens/artigos, 29 recursos e 1.263 links locais, sem erros ou avisos. Usando as 100 fichas atuais e o código real de `assets/formulario-e1.js` em Node/VM com DOM simulado, as cinco buscas pelas novas hipóteses encontraram suas respectivas fichas e uma busca inexistente retornou zero. O teste [testar-filtro.cjs](../evidencias/QA-09/auditoria-aplicacao-fichas-r12-independente-20261030/testar-filtro.cjs), SHA-256 `fa8601c935b09b101c1d0c4901ae2b6abae0cfdd83c9f79bf67744628342af33`, é simulação, não ensaio em navegador real. O teste de persistência BAN-08 também passou em DOM/armazenamento simulados; seus cenários não são teste específico das fichas.

O confronto das 95 demais fichas, MathML, destinos, código e das cinco condições alteradas sustenta **revalidação localizada de FOR-01 para o delta examinado**, sem afirmar nova revisão integral de todas as fichas. A aula inalterada preserva os 197 artigos no alcance desse delta. Outros pareceres e ledgers exigem reconciliação de versão e dependências antes de integração em r12.

| Critério localizado | Resultado |
|---|---|
| Identidade e aplicação das cinco candidatas | Atendido por reconstrução da versão efetiva. |
| Modelos, unidades e contas dos trechos | Atendidos nas hipóteses e limites explicitados. |
| Outras fichas, MathML, aula e vínculos | Preservados no alcance comparado. |
| Mapa, recursos e FOR-01 | Conferidos e revalidados somente no alcance localizado. |
| Navegador real, aprendizagem e QA-09 integral | Não atendidos nesta parcela; próximo ID continua bloqueado. |

Não houve revisão humana, ensaio em navegador, teste com alunos ou certificação externa. Esta aprovação localizada não classifica o curso inteiro como avançado.
