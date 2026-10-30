# QA-09 — auditoria independente da candidata de fração de vapor

Data: 30/10/2026. Revisor automatizado independente `/root/qa_oficina`. **Veredito: candidata tecnicamente adequada no escopo isolado**, sujeita à aplicação fiel e auditoria da versão efetiva. Não houve alteração da aula nesta revisão, não há aprovação global de QA-09 nem liberação de outro ID.

## Identificação e delta

A base é `modulos/e1-termodinamica.html` SHA-256 `200f9b773050594d762cc596a5a89297024b245fc4f504081fc77baaed3db95f`, e inventário r7 SHA-256 `5090b9897a4698e0ad090f45182afba5880361aabc9fd3c3bdf848d971a85a1a`. O parágrafo original ocorre uma vez, na seção `fun01-estado-equilibrio` e posição UTF-16 `102479–103112`; o candidato não ocorre nessa base. Os SHA-256 dos fragmentos, sem a quebra final dos arquivos isolados, conferem: original `8fa3fc141421746dcdb71f2dbf11d00201c00fdd09b6ff51b1ec0579feb745d2`, candidata `541ec23acd9a6e81e66034c432227bd20934bfa72105b734854d6a995f848cb4`. O delta preserva o início do parágrafo, sua marcação e a distinção entre composição líquida xA e fração mássica total de vapor x; troca somente a última afirmação e seu desenvolvimento.

## Conferência independente

Para `nV,nL≥0`, `nV+nL>0`, massas molares médias positivas de cada fase existente e `β=nV/(nV+nL)`, as massas são `mV=nV M̄V`, `mL=nL M̄L`. Dividindo `mV/(mV+mL)` pelo total molar, segue

`x=β M̄V / [(1−β) M̄L + β M̄V]`.

Para `0<β<1` e denominador positivo, `x−β = β(1−β)(M̄V−M̄L)/[(1−β)M̄L+βM̄V]`; portanto a igualdade se verifica exatamente quando as massas molares médias das fases são iguais. Nos limites de fase única, β=0 dá x=0 e β=1 dá x=1; a composição da fase ausente não precisa ser medida nem definida no próprio extremo. A formulação candidata faz a mesma distinção ao usar “nos limites”.

Contramodelo da exclusividade anterior: duas espécies diferentes com mesma massa molar fictícia 28 g/mol, `nL=6 mol` e `nV=4 mol`, têm `β=0,4`, massas `mL=168 g` e `mV=112 g` e `x=112/280=0,4`, mesmo sendo mistura. Composições de fase diferentes são possíveis no modelo fictício; a observação não depende de nomear uma mistura real. Como verificação adicional, com `β=0,4`, `M̄V=20` e `M̄L=40 g/mol`, a expressão resulta `x=8/(24+8)=0,25`, mostrando que igualdade não é universal em misturas.

A candidata elimina a alegação de que apenas a substância pura produz igualdade e mantém a diferença entre bases. Não identifica uma fonte externa para o exemplo por ser contramodelo didático deduzido de definições; ele não afirma dados de substância real. O trecho sobre grau de liberdade e equilíbrio fora da frase modificada não foi reavaliado aqui.

| Critério da candidata localizada | Resultado |
|---|---|
| Base, posição, contexto, unicidade e hashes | Atendido para a fotografia informada. |
| Conversão de bases e condições de igualdade | Atendido sob massas molares positivas e total de matéria não nulo; limites interpretados por fração de fase. |
| Preservação do contexto e distinção xA/x | Atendido na candidata isolada. |
| Aplicação, revalidação de dependências e QA-09 integral | Não atendidos; continuam pendentes. |

Antes de aplicar, confrontar novamente a base efetiva, reconciliar versões e referências, preservar os artigos e registros não modificados, atualizar fotografias/inventários e submeter o arquivo efetivamente alterado a nova auditoria. Não houve ensaio em navegador, revisão humana ou certificação.

## SHA-256

- Análise: `3e33944247f7b33895ffe757656535662c2ca60d7c1ad14eff808b149a2bc822`.
- Manifesto: `9f85331b5a442a366885839d8acb283932aeda5d2215b440fdade404c4f96fc1`.
- Arquivos isolados com quebra final: original `5d3d1fe2cfe31011c6272369f48b45c183259a6410a9b567f831f4d6d267fe7d`; candidata `30c142d3bfd591c4f6acd6aa08d3d491cd5b7b340fe5b1799f88084ea0b99274`.
