# BAN-08 — apoio científico independente AV31–AV35

Data 29/10/2026. Autora das contas e revisora: agente automatizado `/root/auditor_ban08_novo`. Leitura sem cegamento; exame parcial, sem aprovação global de BAN-08 nem liberação do próximo ID. Produto/controle não modificados. Fonte dos artigos e bases locais: `modulos/e1-termodinamica.html` SHA-256 `80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0`; hashes individuais correspondem ao trecho bruto UTF-8 `<article>...</article>`. Questões autorais de cinco alternativas pontuáveis; as ligações CR são apenas origem da transformação, não fontes dos dados novos. Operações com dados didáticos não afirmam precisão experimental.

Fontes de princípios consultadas em 29/10/2026: DOE, glossário Higher/Lower Heating Value, https://www.energy.gov/cmei/fuels/glossary (PCS/PCI); OpenStax University Physics v.2 §3.6, https://openstax.org/books/university-physics-volume-2/pages/3-6-adiabatic-processes-for-an-ideal-gas e §4.1, https://openstax.org/books/university-physics-volume-2/pages/4-1-reversible-and-irreversible-processes (expansão livre); OpenStax Physics §12.2, https://openstax.org/books/physics/pages/12-2-first-law-of-thermodynamics-thermal-energy-and-work (primeira lei). As bases do próprio módulo são identificadas abaixo.

## AV31 — E

Hash `2b2015e4ce0ec1bbea95c3da375ec316239d427f44454cfa43ca007c777fff7a`; base `#base-termoquimica`. Versão atual r2 revisada: com mesma referência de temperatura, PCS considera água formada no estado líquido e PCI no estado de vapor; a diferença está associada à condensação, E. A inverte PCS/PCI, B atribui diferença a temperaturas de referência distintas mesmo com fase igual, C impõe igualdade universal, D envolve trabalho de bomba. Formulação válida para combustíveis que geram água; não se estabelece valor universal da diferença ou eficiência de equipamento. Nenhum dado, cálculo ou resultado numérico no artigo; tolerância numérica não aplicável. Não alego refazer a auditoria documental BAN-07 do delta da versão.

## AV32 — E

Hash `5d53de738a3e1b78ce907920d3ee56add57516359d4b4f36880aa2caa7d6e500`; base `#base-termoquimica`. Se ΔH_direta=H_produtos−H_reagentes=−80 kJ para quantidade indicada, então ΔH_inversa=H_reagentes−H_produtos=+80 kJ, entre mesmos estados e composição; endotérmica na convenção de calor a pressão constante sem outros trabalhos. E. A=−160 altera sinal e magnitude, B classifica sinal positivo como exotérmico, C faz ΔH zero, D conserva sinal direto. Igualdade nominal exata sob os dados fornecidos, diferença 0; não se infere incerteza experimental.

## AV33 — D

Hash `18647f755fc3deb6a9a4aafcb815851a9fcc1244ff0288b0117c8c0620349d1f`; bases `#base-expansao-livre`, `#base-entropia-gas`. Figura `assets/questoes-reais-e1/figura-9d164690a624.png` SHA-256 verificado `9d164690a6243cb31b9ea0f734b9a85ad4c6570398b9d5ef9278e4f44332bcc2`, recipiente isolado, gás, membrana e vácuo; imagem sem valores quantitativos. Fronteira externa rígida e isolada, nenhum outro trabalho nem energia da membrana: Q=0, W=0, ΔU=0. Para gás ideal de composição fixa e capacidade positiva, ΔT=0. Como Vf>Vi, ΔS=nR ln(Vf/Vi)>0; não usar p dV reversível para o processo real. I, II e III verdadeiras, IV falsa: D; A omite III, B omite II e inclui IV, C inclui IV, E inclui IV e omite I/III. Os zeros e desigualdade são exatos no modelo; não há razão de volumes para resultado numérico ou tolerância.

## AV34 — B

Hash `3ae8bcce339a9cfb8899c0dda553455c5cc89fbd8cb6fd39b753b96f7cbcbc20`; bases `#base-leitura-matematica`, `#base-balanco-fechado`, `#base-gas-energia`. Recipiente fechado rígido elimina trabalho de fronteira; item exclui outros trabalhos e ΔEC/ΔEP. Q=ΔU=144 kJ, mcv=2×0,72=1,44 kJ/K, ΔT=144/1,44=100 K, valores publicados coincidem. A=50 duplica massa, C=200 omite massa, D copia calor numérico em K, E supõe que volume fixo implica temperatura fixa. Regra: igualdade nominal exata para cv constante fornecido, sem inferência de medição; uma parede rígida só não excluiria outros modos de trabalho, como lembrado no artigo.

## AV35 — B

Hash `17b85fe40845327cbdfba0bd7d354a5f394034351617d0f22d23e80af6eb4300`; bases `#base-leitura-matematica`, `#base-primeira-lei`. Com Q=0, ΔU=−120 kJ e ΔEC=ΔEP=0, ΔU=Q−W implica W=+120 kJ produzido, publicado +120 e diferença 0. A=−0,120 e E=+0,120 têm magnitude mil vezes menor; A também troca sinal; C=0 omite trabalho; D=−120 indica trabalho entrando. Todas são distintas de B com as unidades impressas. Regra de comparação: igualdade aritmética nominal exata sem incerteza de medida.

Nenhuma divergência numérica localizada. Este apoio não encerra o banco nem implica teste com alunos ou certificação externa.
