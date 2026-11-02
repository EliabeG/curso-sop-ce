# QA-09 — auditoria independente das candidatas da ficha 60 e EX-027, r17

Data: 30/10/2026. Auditor automatizado `/root/next_theory`; Corretor `/root/next_formulas`. **Veredito localizado: APROVADAS como candidatas isoladas.** Produto não alterado; esta revisão não aprova QA-09 integral nem substitui auditoria da aplicação efetiva.

## Identidade e ensaios

Aula r17 SHA `6b0df1096d0b6de6995ffc51bf8489cb45ab954a7aabdeb3f48d068c9777c57c`, formulário r17 `dea4923117d09fa77cabacb0b65816cbf6d57b724d88285003804a1f1440389d`, inventário r17 `b8eae39cc72cf807d7b84aad7e7a38423168b809231bc3b7f08c439d6d25163b`. Análise candidata SHA `d1024614357975aca67b041e08c40ecea1458ac9ed3adeb863428d3e5e43196e`, manifesto `4a61b863e2acfe76c043d58322e695ad2139653199240737b56ed0c5c70c1c92`. O parecer do lote de fichas deste Auditor foi refeito sob nome exclusivo `QA-09-fichas-unidades-modelos-balancos-r17-auditoria-next-theory-r2-20261030.md`, SHA `9c88d8910ef084d388ecc999319402f9473b996aba589f65027d684a094a6b40`, com rastreio da colisão anterior; outro parecer distinto permanece preservado. O exame de EX-027 parte também de `QA-09-exemplos-021-030-r17-auditoria-independente-20261030.md`, SHA `9c13cc19ee74fcbfbf5bc4bbf2dac21c3e4a7b6723c7824456473c421ddfe241`.

Confrontei os fragmentos, alterações e MathML com o manifesto e a fotografia. Meu script somente leitura `evidencias/QA-09/auditoria-next-theory-ficha60-ex027-r17-20261030/verificar.mjs`, SHA `a140e5675df0dd4b3d4705d0566f520c14c445dea14c982157691c8f54dd3345`, passou com reconstituição dos deltas, ocorrência única e correspondência ao inventário, 99 outras fichas preservadas, 197 artigos da aula idênticos e 191/734 elementos MathML preservados, além de IDs, links e atributos ARIA. Os hipotéticos SHAs são formulário `463c00149e36217404cf98bad4f5bed3db828c87d19d1c8e6038678193e9d895` e aula `36d46e4d240a5a79732faac3d7d2a7a0eab813ca01ac8cb3dd9d16552bb51f53`. O script do Corretor também passou; são simulações, não testes em navegador real.

## Ficha 60

A candidata passa a especificar Win como trabalho líquido **total recebido e positivo**, QL e QH como magnitudes relativas ao mesmo ciclo, período e fronteira, e ausência de outras interações energéticas relevantes. Também define no próprio cartão `COPR=QL/Win`, incluindo a ocorrência de busca. Com o balanço do ciclo `QH=QL+Win`, segue `COPBC=QH/Win=COPR+1`; a condição Win>0 torna as razões definidas. O caso hipotético de 100 kJ brutos recebidos e 20 kJ produzidos dá Win=80; com QL=300 e QH=380, COPR=3,75 e COPBC=4,75. O valor 100 bruto não pode ser usado como trabalho líquido do ciclo. [DOE, definição de COP sobre trabalho líquido](https://www.energy.gov/cmei/femp/incorporate-minimum-efficiency-requirements-heating-and-cooling-products-federal) é apoio conceitual, não fonte dos números.

## EX-027

O enunciado candidato fixa 1000 kJ como calor **total recebido** da fonte quente, 600 kJ como calor **total rejeitado** à fria e trabalho líquido como única outra transferência de energia pela fronteira. Para ciclo completo, W=1000−600=400 kJ e η=400/1000=40%. Os cálculos, símbolos e MathML permanecem os mesmos; o novo comando exclui outras entradas térmicas como o contraste anterior de 1000+200−600=600 kJ. Naquele contraste, fontes a 800, 600 e 300 K dão Sger=600/300−1000/800−200/600=5/12 kJ/K>0, mostrando que a energia adicional não era automaticamente excluída pela segunda lei. Os dados são hipotéticos e não constituem um dispositivo validado.

Uma eventual aplicação exige nova fotografia, mapa, conciliação de referências e recursos, teste de busca/revelação, reavaliação localizada de FOR-01 e auditoria independente da versão efetiva. Não houve ensaio com alunos, leitor de tela ou revisão humana.
