# QA-09 — candidata isolada para EX-031

Data: 30/10/2026. Autor: agente automatizado `/root/qa_examples`, Corretor. **Aguardando revisão independente; não aplicada ao HTML.** Responde ao bloqueio do [parecer do lote EX-031–040](../../../pareceres/QA-09-exemplos-031-040-auditoria-independente-r1.md). A candidata esclarece as hipóteses de transferência de energia; não encerra QA-09.

## Fotografia e delta

Fonte `modulos/e1-termodinamica.html` SHA-256 `200f9b773050594d762cc596a5a89297024b245fc4f504081fc77baaed3db95f`, inventário r7 SHA-256 `5090b9897a4698e0ad090f45182afba5880361aabc9fd3c3bdf848d971a85a1a`. O fragmento EX-031 é a `div.exemplo` da seção `ciclos`, início 381086 e fim 381963 na fotografia UTF-16 r7, ocorrência literal única no HTML. SHA-256 do fragmento sem newline `fa0b22cc94dc24f3c4fc2493c719f30ab4a0484149f081b681497f81d73536e6`; candidata `fdbd8e2cc5d4212af40051f854dca99420ae4ef7b1c887a82c9540fdae2a3d6a`. Arquivos isolados com uma quebra final: original `4ba5ca1d112ca575a5a4323690dc339672377a50a7061cb87e0e14a2206f59e4`; candidata `ef5b56119ac64659e702820301ca343b7f66ca2834042dd57ad9ea0edca71701`.

Após a frase existente “Equipamentos estacionários, com mudanças cinética/potencial desprezíveis; bomba/turbinas adiabáticas.” acrescenta-se exatamente:

> A caldeira e o reaquecedor recebem calor líquido externo, e o condensador rejeita calor líquido externo; esses três equipamentos não trocam trabalho além do trabalho de escoamento já incluído nas entalpias.

A ausência de trabalho não associado ao escoamento inclui eixo e eletricidade; o calor líquido não oculta balanços parciais de ganhos e perdas. Os dados, solução, estrutura, unidades e modelo de bomba/turbinas foram mantidos. A candidata só explicita o modelo necessário: não transforma entalpias fictícias em estados de um ciclo real validado.

## Balanços e contramodelo

Por kg, com convenção local de calor recebido e trabalho saindo positivos: `q−w=Δh` nos equipamentos estacionários. Sem trabalhos extras nos três equipamentos de troca térmica, caldeira q=3.100−210=2.890 kJ/kg e reaquecedor q=3.200−2.500=700, total qH=3.590; condensador rejeita 2.000. Turbinas produzem 1.600, bomba consome 10, Wlíq=1.590 e η=1.590/3.590=44,289693…%=44,29%; saldo 3.590−2.000=1.590 kJ/kg.

Antes da explicitação, uma resistência na fronteira da caldeira poderia receber **100 kJ/kg de trabalho elétrico**, sem alterar os dados do enunciado. Nessa hipótese, wcaldeira=−100; qcaldeira=2.790 para manter q−w=2.890; qH=2.790+700=3.490; Wlíq=1.600−10−100=1.490; rejeição continua 2.000. O saldo é 3.490−2.000=1.490, e a razão de trabalho líquido a calor externo é 1.490/3.490≈42,69%. É contramodelo de balanço, não uma comprovação de viabilidade de todos os estados; é excluído pela candidata.

## Teste e impacto a examinar

`python3 auditoria/termodinamica/evidencias/QA-09/exemplo-031-candidata-20261030/verificar.py` confere a base, hashes, ocorrência única, substituição literal e os balanços nominal e contramodelo; não grava e não executa a troca no curso. Script SHA-256 `e764105f7ebf76e5192a2b79c3aca2f9c7f79c2617b8835276c972508a20638f`.

A mudança está em `div.exemplo` fora dos 197 artigos. Sua aplicação futura modificará o hash integral do HTML e deslocará posições de ocorrências seguintes: requer conferir versão efetiva e localização por contexto e hash, mapa r7→nova fotografia, integridade de artigos/registros, atualização das referências necessárias, testes estruturais e revalidação do alcance de aceites anteriores afetados. Um hash igual em fragmentos não transfere aceite automaticamente. Revisão independente desta candidata e depois da aplicação efetiva são necessárias. Não houve navegador real, avaliação com estudantes ou certificação externa.
