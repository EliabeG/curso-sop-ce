# QA-09 — auditoria independente dos recursos FUN-02 P2/P3, r9

Data: 30/10/2026. Revisor: agente automatizado independente `/root/next_theory`, distinto do Corretor `/root/next_graphics`. **Veredito localizado: APROVADO**, para a associação dos dados e script aos resultados P2/P3 examinados na fotografia abaixo. Não encerra QA-09, não renova integralmente FUN-02 e não libera o próximo ID.

## Critério e identificação

QA-09 exige inventariar e recalcular o conteúdo numérico fora dos 197 artigos, inclusive recursos, exemplos, oficinas, diagnósticos, fichas, projetos, figuras e explicações, com referências verificáveis e resultados conferidos. Esta revisão examina os dois recursos compartilhados acessíveis pela aula e seus usos P2/P3, não todos os registros nem todas as capacidades do script. P2 e P3 são artigos já segregados; o confronto deles com dados externos não os soma como novas atividades fora da classe BAN-08.

Fotografia da aula: `modulos/e1-termodinamica.html` SHA-256 `2d6b8fb2f9c99e04d22c19d7b32bbc3eb20577459d9132e506f9c0acef3f2fc2`; inventário r9 SHA-256 `023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d`; dados `fun02-dados-v1.json` SHA-256 `511aac986e9122e5498cdf69609274685791000a19f140a09d539fca01676319`; código `fun02-calculos-v1.mjs` SHA-256 `2fdd0e498c41db2f7f8e90d5114dcd015f5377e00901e6274f25262e13c79a70`. Entrega do Corretor [entrega.md](../evidencias/QA-09/fun02-p2-p3-recursos-r9-20261030/entrega.md), SHA-256 `82d148c185119d8d87e48f149856dd36ac1b66adfd2187531e7102e57e4cdaa0`.

Examinei diretamente os dados, o código, os dois artigos e as referências à dupla de recursos em `fun02-dados`. O identificador, posição r9 e hash integral dos artigos conferem: P2 `fun02-e1-integrabilidade`, 263254–288148, `17621376b554fe092fb9f880c910dd447b1f6716448ace454ac31f4427e9fcd2`; P3 `fun02-e1-calor-caminho`, 288150–297759, `936a8ba00043cc49ad22d047338a78ae65b9c9e531dba634a5d943cfbd194a6c`. As duas referências externas aos artigos estão nas posições 252246 e 252344. Os dados são didáticos autorais, não propriedades experimentais de uma substância real.

## Recálculo independente

**P2:** no domínio θ,ν>0, aberto e simplesmente conexo, para α as derivadas cruzadas valem E₀/ν. Derivando `Φ/E₀=θ lnθ−θ+(θ−1)lnν+ν²/2+1/2` recuperam-se os dois coeficientes e Φ(1,1)=0. O código utiliza a mesma função sem a constante aditiva e calcula diferenças, o que não muda os resultados. Para β, a diferença `∂Nβ/∂θ−∂Mβ/∂ν=2E₀κ(θ−2)/ν` anula-se na linha θ=2 sem provar exatidão numa vizinhança aberta quando κ≠0. Para os ciclos anti-horários do enunciado, o ciclo largo cancela, e o esquerdo é `−E₀κ ln2=−20 ln2` J/mol, implicando κ=0,2 na família proposta.

Com P=(1,1), Q=(2,2), os dois caminhos de α dão `100(3 ln2+0,5)=257,944154168 J/mol`. A contribuição extra de β no caminho VH é `20 ln2`, produzindo 271,807097779 J/mol, enquanto HV continua 257,944154168 J/mol; HV−VH=−13,862943611 J/mol concorda com a orientação do ciclo esquerdo. Em S=(2,2), a parcial a volume molar fixo é `(100/300) ln4=0,462098120 J/(mol·K)`; a derivada em ν=θ inclui o termo de caminho e é `(100/300)(ln4+2,5)=1,295431454 J/(mol·K)`. Esse resultado não transforma uma linha de igualdade das derivadas cruzadas em prova global.

**P3:** os dados fixam 1 mol de gás ideal, R=8,314 J/(mol·K), cᵥ,m=3R/2, T₁=300 K, V₁=0,020 m³, V₂=0,005 m³ e pV^(3/2) constante. De `TV^(1/2)=constante`, T₂=600 K; p₁=124710 e p₂=997680 Pa. Com trabalho de fronteira no modelo quase estático, sem outros trabalhos ou variações de Ec/Ep, `W=−2nRΔT=−4988,4 J`; `ΔU=n(3R/2)ΔT=3741,3 J`; logo `Q=ΔU+W=−1247,1 J`. A temperatura aumenta, embora calor saia, porque o trabalho recebido é maior em magnitude.

Para o caminho, `C_caminho=n(cᵥ,m−2R)=−4,157 J/K`, ao passo que Cᵥ=12,471 e Cₚ=20,785 J/K são positivos; sua coincidência numérica com as respectivas capacidades molares deriva apenas de n=1 mol. `ΔS=n cᵥ,m ln2+nR ln(1/4)=−(nR/2)ln2=−2,881412830 J/K`. `Q/T₁=−4,157 J/K` não é ΔS porque T varia; o cálculo da integral exige a temperatura de transferência pertinente. A igualdade do gás internamente reversível pode persistir se a irreversibilidade estiver na interação térmica externa, sem atribuí-la indevidamente à temperatura do reservatório. O expoente 3/2 não é γ=5/3 e não implica processo adiabático.

## Reprodução e fontes

O script próprio de auditoria [verificar.py](../evidencias/QA-09/auditoria-fun02-p2-p3-r9-20261030/verificar.py), SHA-256 `c1715bbb109c8859a86029c413c575b9d7bbb117ed3f88520fe6afe50172633a`, não grava arquivos. Ele confirmou hashes dos quatro arquivos, ambos artigos, as duas referências, uma quadratura independente dos dois caminhos de β e os cálculos analíticos de P2/P3; importou e executou `calcularFun02`, que retornou 49 testes internos. Executei também o verificador do Corretor após inspeção de suas saídas. Os resultados concordaram com as soluções examinadas; precisão numérica com tolerância absoluta de 10⁻⁸ ou relativa de 10⁻¹¹ na verificação independente, não uma declaração de precisão experimental.

Confrontei [OpenStax, campos conservativos e domínio](https://openstax.org/books/calculus-volume-3/pages/6-3-conservative-vector-fields), [Universidade de Washington, diferenciais](https://faculty.washington.edu/jcv2/CHEM452_WI2023/html/appendix_differentials.html) e [Purdue, entropia e temperatura de fronteira](https://engineering.purdue.edu/~wassgren/teaching/ME20000/NotesAndReading/Lec24_Reading_Wassgren.pdf). A consulta foi realizada em 30/10/2026; as referências sustentam os métodos gerais e não são fonte dos números hipotéticos.

| Critério localizado | Resultado |
|---|---|
| Identidade de aula, recursos e referências | Atendido na fotografia e nos dois artigos identificados. |
| P2: domínio, potencial, caminhos e unidades | Atendido no modelo matemático especificado; exatidão não demonstra admissibilidade física. |
| P3: balanços, capacidade de caminho e entropia | Atendido sob as hipóteses de estado e fronteira registradas. |
| Revisão integral de FUN-02 ou QA-09 | Não atendida por este recorte. |
| Liberação do próximo ID | **Não liberado.** |

Não houve navegador, revisão humana, aplicação com estudantes ou certificação externa. Alterações posteriores requerem análise de alcance e reconciliação; hash igual por si só não transfere automaticamente aprovações a outros usos ou versões.
