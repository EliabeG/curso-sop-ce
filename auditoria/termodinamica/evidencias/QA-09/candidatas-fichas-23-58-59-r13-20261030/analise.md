# QA-09 — candidatas isoladas das fichas 23, 58 e 59

Data: 30/10/2026. Corretor: agente automatizado `/root/next_formulas`. **Não aplicadas; aguardam auditoria independente.** Respondem ao [parecer das três fichas](../../../pareceres/QA-09-fichas-latente-cop-r13-auditoria-independente-20261030.md). QA-09 integral e próximo ID continuam bloqueados.

## Condições propostas

- **23 — calor latente:** permanece a vaporização completa de substância pura, com estados saturados à mesma pressão termodinâmica constante. Para a fórmula de calor em sistema fechado, explicita apenas trabalho de fronteira `Wb=p(V₂−V₁)` e nenhum outro trabalho; para a razão de vazão, requer `hfg≠0`. Preserva a condição diferente de escoamento permanente, sem trabalho não associado ao escoamento, inclusive elétrico, e a negligência de ΔEc/ΔEp. A igualdade de pressão e trabalho é suficiente para `Q=ΔH=m hfg`, sem impor reversibilidade universal. O divisor zero precisa ser excluído.
- **58 — rendimento:** identifica QH como **todo** calor recebido e QL como **todo** calor rejeitado no mesmo ciclo/fronteira, ambos positivos, e exige Wlíq>0 para regime motor. Isso mantém a expressão para várias fontes, desde que os símbolos sejam os totais; não a restringe a dois reservatórios.
- **59 — COP:** limita a expressão `COPR=QL/Win` ao refrigerador acionado por trabalho, sem outra fonte energética de acionamento, com QL e Win na mesma fronteira e período e Win>0. A restrição não exclui o calor QL retirado da fonte fria, que é o efeito útil; “outra fonte de energia de acionamento” refere-se ao suprimento que move o ciclo. COP pode exceder 1. Para absorção aquecida, a razão térmica usada como COP pode ter outra base; a fórmula por trabalho não é apresentada como indicador genérico de todos os refrigeradores.

As substituições afetam as condições em texto visível e `data-busca` de cada ficha, sincronizadas, sem alterar MathML, fórmulas, símbolos, valores ou vínculos. Expressões de desigualdade são codificadas em HTML quando necessário.

## Testes e contrastes

- Valores fictícios hf=500, hg=2500 kJ/kg dão hfg=2000 kJ/kg; m=2 kg implica m hfg=4000 kJ e Q̇=6000 kW implica ṁ=3 kg/s. Para Q=ΔH do sistema fechado, o trabalho precisa corresponder à pressão usada na diferença de entalpia.
- Em máquina cíclica com entradas térmicas fictícias de 500 e 50 kJ e rejeição de 300 kJ, `QH=550 kJ`, `QL=300 kJ`, Wlíq=250 kJ e η=5/11≈0,4545. Usar apenas 500 como total recebido omite uma interação.
- Num refrigerador por absorção fictício, QL=600 kJ, calor de acionamento=1000 kJ e trabalho elétrico=40 kJ, COP térmico=0,6 enquanto QL/Win=15 é uma razão diferente. A candidata 59 delimita a fórmula ao caso de acionamento por trabalho. A fonte fria continua entrando no balanço como calor útil, não é excluída como acionamento.

## Identidade e simulação

Formulário r13 SHA-256 `5f3f31a4801f96a2b78b40c75d37392f6b16d264901ac313ac00458901970285`; inventário r13 SHA-256 `0df99b79bcc2350581fcdded72435d30d07858de237a549e6228ca73682f8d9b`. O manifesto registra âncoras, posições UTF-16 e hashes dos três fragmentos. Arquivos isolados possuem quebra de linha final, excluída dos hashes dos fragmentos. Cada original ocorre uma vez e cada condição duas vezes no artigo correspondente.

`node auditoria/termodinamica/evidencias/QA-09/candidatas-fichas-23-58-59-r13-20261030/verificar.mjs` reconstrói a alteração somente em memória, confere a fotografia e os hashes, testa os contrastes e verifica 100 fichas na mesma ordem, 97 não alvo byte a byte iguais e 191 MathML preservados. A execução retornou `ok=true`, sem gravação no produto. O teste não é ensaio em navegador ou parecer científico independente.

## Próximos passos

Auditor independente deve julgar as hipóteses, particularmente o significado de totais na ficha 58 e o limite de acionamento na 59, conferir elementos, identidade e hashes, e verificar se a 23 mantém distinção entre processo fechado e volume de controle. Após aplicação, gerar fotografia/mapa novos, reconciliar as posições e dependências, verificar as demais fichas, links e comportamento de busca/revelação e reavaliar FOR-01 no alcance alterado. A versão aplicada exige novo parecer independente. Não houve teste com alunos, revisão humana ou certificação externa.
