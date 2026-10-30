# QA-09 — auditoria independente da aplicação intercooling r17

30/10/2026. Auditor `/root/planning`; executor `/root/next_formulas`. **Parecer: APROVADA ISOLADAMENTE a aplicação e revalidação localizada do trecho de intercooling na r17.** QA-09 integral permanece em correção; este parecer não aprova os demais conteúdos nem transfere aceites automaticamente.

## Ciência e referência

Releitura do trecho efetivo e das suas hipóteses: a comparação fixa dois estágios adiabáticos do mesmo gás ideal, calores específicos constantes, a mesma entrada, razões de pressão e eficiências isentrópicas por estágio e ausência de perda de pressão no resfriador. Não inclui potência auxiliar. Para segundo estágio com cp>0, k>1, razão de pressão r₂>1 e eficiência isentrópica η₂>0 fixos, o trabalho específico recebido é `w₂=cp Tentrada,2 (r₂^((k−1)/k)−1)/η₂`. Reduzir a temperatura de entrada do segundo estágio reduz esse trabalho no modelo, enquanto a primeira etapa permanece igual por suas condições fixadas. Não se conclui que todo resfriamento reduza o consumo elétrico ou a potência total de qualquer instalação.

Recálculo independente com cp=1 kJ/(kg·K), k=1,4, T₁=300 K, r₁=r₂=4 e η₁=η₂=0,5: primeiro estágio consome 291,596573 kJ/kg. Sem intercooling, a segunda entrada é 591,596573 K, segundo estágio consome 575,025112 e total 866,621686 kJ/kg. Com retorno hipotético a 300 K, segundo estágio consome 291,596573 e total 583,193147 kJ/kg. Os valores são do exemplo controlado, não de um equipamento medido e não incluem auxiliares. As afirmações adjacentes sobre reaquecimento e regeneração foram preservadas; não são genericamente reavaliadas aqui.

Consultei o material do [MIT sobre ciclos ar-padrão](https://ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_5.htm) e a [dissertação Texas A&M sobre compressão em estágios](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/720949b2-1bd4-4884-9025-d39f685f11a5/content), fontes técnicas de contexto já examinadas no parecer da candidata. Elas não são fonte dos números hipotéticos acima. O endereço das fontes e demais referências do produto não foram alterados pela aplicação; a disponibilidade futura não está assegurada.

## Identidade e preservação

Aula r16 SHA `55754bfc631da9010e3c9afc73e3c458e349b535c429fe98abe28998897aab23` e r17 `6b0df1096d0b6de6995ffc51bf8489cb45ab954a7aabdeb3f48d068c9777c57c`; formulário mantido `dea4923117d09fa77cabacb0b65816cbf6d57b724d88285003804a1f1440389d`. Inventário r17 `b8eae39cc72cf807d7b84aad7e7a38423168b809231bc3b7f08c439d6d25163b`, mapa r16→r17 `0100c4363286b7b7615f3f9f98063eec1a2bf58661d5a6278586376f274b6623`, entrega `9c98b630be3ca880b5285be069f95d4e9c0012f0d4c2cbcc29fb4c240334184f`.

Meu verificador somente leitura `auditoria/termodinamica/evidencias/QA-09/auditoria-aplicacao-intercooling-r17-independente-r1/verificar.py`, SHA `681ed4fd6a330a9189a2be9550fb3766775b976c7fde794dbb5b88333d0c4ab4`, reproduziu a aula efetiva pela substituição única da candidata, confrontou a identidade dos 197 artigos e 197 registros oficiais, 734 blocos MathML da aula e o formulário completo, e recalculou o exemplo. O validador oficial executado na árvore efetiva confirmou 197 artigos e itens, 1.263 links locais e 29 recursos, sem erros/avisos; é teste documental, não científico ou remoto.

Apoio estrutural independente de `/root/next_examples`: `auditoria/termodinamica/pareceres/QA-09-mapa-r16-r17-apoio-auditoria-independente-r1.md`, SHA `753f9653bba1ce4d8ee3a4c1aeb1df6f5e102bdf70a38edde5156d5c23cd2c26`, verificou bijeção dos 11.400 pares, 73 internos (72 hashes iguais e um texto alterado), um ancestral, 816 fragmentos de referência e 138 relações de recursos. A conservação dos 197 artigos e registros sustenta a ausência de alteração aos escopos BAN pela aplicação, sem reauditar soluções; formulário integralmente inalterado, sem novo impacto FOR-01. Hash e pareamento não substituem exame científico nem atribuem aceite aos nós associados.

Não houve teste em navegador, leitor de tela, estudantes, revisão humana ou certificação externa. Os demais conteúdos e a cobertura integral continuam pendentes de integração e avaliação na fotografia vigente.
