# QA-09 — FUN-02, dados e resultados P2/P3 na fotografia r9

Data: 30/10/2026. Corretor: agente automatizado `/root/next_graphics`. **Aguardando auditoria independente.** O escopo é a coerência dos dados e do script FUN-02 ligados fora dos artigos, confrontados com os resultados P2/P3 que os empregam. Não houve alteração da aula nem dos ativos. Não é aceite integral de QA-09 ou revisão completa de FUN-02.

## Versão e fronteira

Aula `modulos/e1-termodinamica.html` SHA-256 `2d6b8fb2f9c99e04d22c19d7b32bbc3eb20577459d9132e506f9c0acef3f2fc2`; inventário r9 SHA-256 `023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d`. Dados `assets/termodinamica/fun02-dados-v1.json`, versão autoral 1.0 de 27/10/2026, SHA-256 `511aac986e9122e5498cdf69609274685791000a19f140a09d539fca01676319`; script `assets/termodinamica/fun02-calculos-v1.mjs` SHA-256 `2fdd0e498c41db2f7f8e90d5114dcd015f5377e00901e6274f25262e13c79a70`. As referências da aula a dados e script estão fora dos artigos na seção/âncora `fun02-dados`, posições UTF-16 r9 252246 e 252344. P2 e P3 aparecem nos artigos segregados `fun02-e1-integrabilidade` (263254–288148, hash `17621376b554fe092fb9f880c910dd447b1f6716448ace454ac31f4427e9fcd2`) e `fun02-e1-calor-caminho` (288150–297759, hash `936a8ba00043cc49ad22d047338a78ae65b9c9e531dba634a5d943cfbd194a6c`). Eles não são somados como novos objetos fora dos 197.

O parecer [FUN-02-r1](../../../pareceres/FUN-02-r1.md) examinou os mesmos hashes dos ativos e outra fotografia da aula. Este confronto identifica o uso atual e refaz resultados, sem transferir automaticamente todos os aceites daquela versão. Os valores são dados didáticos, não tabelas experimentais.

## P2 — integrabilidade

No domínio aberto simplesmente conexo θ>0, ν>0, com θ=T/300 K, ν=vₘ/(0,001 m³/mol) e E₀=100 J/mol, os coeficientes são suaves. Para α, `M/E₀=ln θ+ln ν` e `N/E₀=ν+(θ−1)/ν`. Ambas as derivadas cruzadas são E₀/ν. Um potencial com referência Φ(1,1)=0 é `Φ/E₀=θ lnθ−θ+(θ−1)lnν+ν²/2+1/2`; suas parciais reproduzem M e N. O código usa o mesmo potencial sem o termo constante 1/2 e somente diferenças: isso não altera resultados.

Para β=α+E₀κ(θ−2)²dν/ν, a diferença entre as derivadas cruzadas é `2E₀κ(θ−2)/ν`. A coincidência na linha θ=2 não prova exatidão em uma vizinhança aberta se κ≠0. Num retângulo anti-horário com θ de a a b e ν de 1 a 2, a contribuição adicional é `E₀κ[(b−2)²−(a−2)²]ln2`; no largo 1→3 ela cancela para qualquer κ, enquanto no esquerdo 1→2 é `−100κ ln2`. A observação didática `−20 ln2` determina `κ=0,2` apenas dentro da família fornecida.

Para P=(1,1), Q=(2,2), `α_HV=α_VH=100(3 ln2+0,5)=257,944154168 J/mol`. Para β com κ=0,2, `β_HV=257,944154168` e `β_VH=271,807097779 J/mol`, diferença `−13,862943611 J/mol`, coincidente com a orientação do ciclo esquerdo. Em (2,2), a parcial a vₘ fixo é `(100/300)ln4=0,462098120 J/(mol·K)`; ao longo de ν=θ é `(100/300)(ln4+5/2)=1,295431454 J/(mol·K)`. A inclinação citada é da trajetória, não a parcial. Os números e condições concordam com JSON, código e solução P2, dentro do arredondamento da aula; o modelo matemático não demonstra admissibilidade física de uma substância.

## P3 — compressão politrópica

Para 1 mol de gás ideal com R=8,314 J/(mol·K), cᵥ,m=3R/2, T₁=300 K, V₁=0,020 m³, V₂=0,005 m³ e pV³ᐟ² constante, o vínculo mecânico é `T√V=constante`, então T₂=600 K; p₁=124710 Pa e p₂=997680 Pa. Sob trabalho de fronteira quase estático, sem outros trabalhos e ΔEc/ΔEp desprezíveis: `W=nR(T₂−T₁)/(1−3/2)=−4988,4 J`, `ΔU=12,471×300=3741,3 J`, `Q=ΔU+W=−1247,1 J`. O balanço fecha e aquecimento com calor saindo é consistente com entrada maior de trabalho.

Ao longo do caminho `C_caminho=n(cᵥ,m−2R)=−4,157 J/K`, constante neste modelo; isso difere de Cᵥ=12,471 J/K e Cₚ=20,785 J/K, ambos positivos. As correspondentes capacidades molares têm unidade J/(mol·K), numericamente iguais neste exercício somente porque n=1 mol. A relação `Q/ΔT=C_caminho` depende da constância deste caminho e não é identidade geral.

Com trocas internamente reversíveis, `δQ_rev/T = ncᵥ,m dT/T + nR dV/V` é exata no quadrante positivo. `ΔS=12,471 ln2+8,314 ln(1/4)=−2,881412830 J/K`; a integral ao longo do caminho concorda. `Q/T₁=−4,157 J/K` é diferente, pois T varia durante a transferência. Para troca com diferença finita de temperaturas, os estados fixam ΔS, mas uma eventual irreversibilidade apenas externa não elimina automaticamente a relação do gás internamente reversível; com geração interna, a fronteira e suas temperaturas importam. Expoente 3/2 não implica processo adiabático: γ=5/3 no modelo e Q calculado é negativo. Estes resultados conferem no JSON, na função e no texto P3.

## Reprodução, referências e limites

`python3 auditoria/termodinamica/evidencias/QA-09/fun02-p2-p3-recursos-r9-20261030/verificar.py` (SHA-256 `390f41e7c2b0dac075f272d9810d7fa9f1c49396b0909120d9a46f0bee9577a9`) confere hashes, posições e resultados com fórmulas analíticas independentes; executado com sucesso sem gravar arquivos. A função `calcularFun02` também foi importada e executada na fotografia atual, com 49 testes internos e saídas P2/P3 compatíveis; sua execução não substitui a dedução acima. As igualdades são para modelo e dados nominais; valores decimais exibidos são arredondados, não incertezas experimentais.

Fontes primárias consultadas em 30/10/2026: [OpenStax Calculus 3, §6.3](https://openstax.org/books/calculus-volume-3/pages/6-3-conservative-vector-fields) para potencial e domínio; [University of Washington, CHEM452, apêndice 4.1](https://faculty.washington.edu/jcv2/CHEM452_WI2023/html/appendix_differentials.html) para diferenciais e condições mantidas; [Purdue ME200, Wassgren, capítulo de entropia](https://engineering.purdue.edu/~wassgren/teaching/ME20000/NotesAndReading/Lec24_Reading_Wassgren.pdf) para distinção de temperatura da fronteira e geração de entropia. Essas referências sustentam o modelo, não são origem dos valores didáticos.

Não foram avaliados todos os blocos, toda a bibliografia, experiência em navegador, leitor de tela, ensino com alunos ou certificação externa. Os artigos e o conteúdo fora deles exigem reconciliação individual de alcance. Auditor independente deve examinar esta entrega, não apenas o programa. QA-09 permanece em correção.
