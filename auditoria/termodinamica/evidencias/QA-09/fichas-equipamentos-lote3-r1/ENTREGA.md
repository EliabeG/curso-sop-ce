# QA-09 — verificação localizada de fichas de equipamentos e ciclos, lote 3

Data: 30/10/2026. Corretor automatizado `/root/qa_fichas`. **Aguardando Auditor independente.** Foram examinadas 14 fichas: 43–46, 61–63, 71–72, 79–80 e 84–86. Nenhuma alteração no formulário. A cobertura das demais fichas e de outras classes de conteúdo continua pendente; esta entrega não encerra QA-09.

Fotografia: `formulas/termodinamica.html`, SHA-256 `c27422b409a0a755448982c4074c6d6967fd3e91d7eae20274e218530f5c37b0`. O arquivo `resultado.json` registra número, ID, posição em bytes, tamanho e SHA-256 de cada artigo; posições vinculam-se exclusivamente à fotografia. As fórmulas selecionadas usam grandezas simbólicas, não valores numéricos de estados. Os valores abaixo foram **criados para testar sinais, fatores e coerência algébrica**, não constam como dados destas fichas, não foram medidos e não provam que os estados pertençam a uma substância ou instalação real.

## Relações, hipóteses e contas

| Ficha | Relação verificada e condições | Teste numérico artificial |
|---|---|---|
| 43 turbina | Primeira lei em regime permanente, adiabática, com ΔEC/ΔEP desprezíveis: `wt=h₁−h₂`; multiplicar por vazão dá potência, na mesma base de massa. | h₁=600, h₂=400 kJ/kg; ṁ=2 kg/s: wt=200 kJ/kg e Ẇt=400 kW. |
| 44 compressor | Mesmo balanço, trabalho recebido como magnitude positiva: `win=h₂−h₁`. | h₁=100, h₂=180 kJ/kg; ṁ=2 kg/s: win=80 kJ/kg e Ẇin=160 kW. |
| 45 bomba | Para referência adiabática reversível, `dh=v dp`; v aproximadamente constante dá `wb,s≈v(p₂−p₁)`. | v=0,001 m³/kg, p₂−p₁=1000 kPa: 1 kJ/kg; com 2 kg/s, 2 kW. `kPa·m³=kJ`. |
| 46 válvula | Sem calor nem qualquer trabalho não associado ao escoamento, em regime permanente com ΔEC/ΔEP desprezíveis, `h₁≈h₂`. | h₁=250 kJ/kg implica h₂≈250 kJ/kg; não exige temperatura constante nem processo reversível. |
| 61 Carnot | Entre dois reservatórios `TH>TL>0`, a eficiência reversível é `1−TL/TH` e limita a máquina cíclica. | TH=600 K, TL=300 K: limite 0,50; temperaturas são absolutas. |
| 62 limites de Carnot | Com QH fixado, `Wmax=QH(1−TL/TH)` e `QL,min=QH TL/TH`; obtidos de primeira lei e limite reversível. | QH=1000 kJ, TH=600 K, TL=300 K: Wmax=500 kJ e QL,min=500 kJ. |
| 63 COP Carnot | Para refrigerador ou bomba de calor reversível movido a trabalho entre os mesmos dois reservatórios, `COPR=TL/(TH−TL)` e `COPBC=TH/(TH−TL)`. | TH=600 K e TL=300 K dão COPR=1 e COPBC=2; diferença igual a 1 para o mesmo ciclo. |
| 71 eficiência isentrópica da turbina | Para a mesma entrada e mesma pressão de saída, com adiabaticidade e ΔEC/ΔEP desprezíveis, razão de trabalho real ao isentrópico é `(h₁−h₂,real)/(h₁−h₂,s)`. | h₁=600, h₂,real=400, h₂,s=350 kJ/kg: 200/250=0,80. Numerador e denominador não devem ser invertidos. |
| 72 eficiência isentrópica do compressor | Nas mesmas condições de comparação, eficiência é trabalho isentrópico sobre real: `(h₂,s−h₁)/(h₂,real−h₁)`. | h₁=100, h₂,s=160, h₂,real=180 kJ/kg: 60/80=0,75. |
| 79 Rankine simples | Com mesma vazão, bomba e turbina adiabáticas, ΔEC/ΔEP desprezíveis e nenhum trabalho não associado ao escoamento nos dois trocadores: `wt=h₃−h₄`, `wb=h₂−h₁`, `qin=h₃−h₂`, `qout=h₄−h₁`. | h=(100,110,500,300) kJ/kg: wt=200, wb=10, qin=390, qout=200; η=190/390=19/39≈0,48718; `qin−qout=190`. |
| 80 Brayton, trabalho líquido | Considerando somente turbina e compressor e calor externo recebido positivo, `Ẇliq=Ẇt−Ẇc`, `η=Ẇliq/Q̇in`. | Ẇt=1000, Ẇc=400, Q̇in=1200 kW: 600 kW e η=0,50. Não inclui consumos auxiliares fora da hipótese. |
| 84 compressão de vapor | Compressor e válvula adiabáticos; condensador, evaporador e válvula sem trabalho não associado ao escoamento; vazão única, sem trocas nas conexões e ΔEC/ΔEP desprezíveis. | h=(400,450,250,250) kJ/kg: qL=150, wc=50, qH=200 kJ/kg e COPR=3; `qH=qL+wc`. A igualdade h₃≈h₄ vem do balanço da válvula. |
| 85 condensador do ciclo | Para o ciclo completo sem outras trocas e consumo relevante, primeira lei implica `Q̇H=Q̇L+Ẇin`. | 150 kW extraídos e 50 kW consumidos implicam 200 kW rejeitados. |
| 86 aquecedor aberto | De `y hextração+(1−y) hágua=hsaída`, o isolamento é `y=(hsaída−hágua)/(hextração−hágua)`. Regime permanente, adiabático, sem trabalho, ΔEC/ΔEP desprezíveis e correntes compatíveis à pressão de mistura. | hágua=210, hextração=2700, hsaída=500 kJ/kg: y=290/2490=29/249≈0,11647; denominador não nulo e y∈[0,1]. |

## Fonte, verificação e limites

Foram consultadas em 30/10/2026 as exposições do livro aberto de Claire Yu Yan/UBC: [balanços de escoamento permanente](https://pressbooks.bccampus.ca/thermo1/chapter/key-equations-5/) e [ciclos de Carnot](https://pressbooks.bccampus.ca/thermo1/chapter/6-4-carnot-cycles/). Estas fontes sustentam os balanços e o limite reversível; não são a origem dos dados numéricos fictícios acima.

Da raiz, `python3 auditoria/termodinamica/evidencias/QA-09/fichas-equipamentos-lote3-r1/verificar.py` requer `lxml`, lê o documento e imprime JSON, sem escrever arquivos. O teste verifica unicidade dos 14 artigos, fotografia, texto MathML linearizado e 12 conjuntos de contas com frações exatas. Confirmei na marcação a estrutura das frações com seus numeradores e denominadores; o script não verifica sozinho a árvore MathML completa e tampouco extrai parâmetros físicos ou prova a validade física de estados arbitrários. SHA-256 script `82028029e739bb04d4d8aca23b639db582e414ccf2ac5fbaf54839d74f077d83`; resultado `fd3b46b8318b6515414596cc5093fdb61418e3c94dbad00145915c04a151ab11`.

Nenhum erro encontrado neste recorte pelo Corretor. Não foram realizados ensaio de navegador, revisão humana, aplicação com estudantes ou certificação externa. O Auditor independente deve conferir fonte, hipóteses e versão antes de aceitar o lote.
