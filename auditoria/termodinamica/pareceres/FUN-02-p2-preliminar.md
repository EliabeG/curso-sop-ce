# FUN-02 — resolução independente preliminar de P2

Revisor: agente automatizado `/root/auditor_aaa`. Data: 27/10/2026. **Memória de resolução, sem parecer geral ou liberação de FUN-02.**

Fonte única consultada nesta resolução: `evidencias/FUN-02/enunciado-p2-r1.md`, SHA-256 `b9bed721d7732979261e6cab2ca79f5fb7df61696de78a4b172d0c17a88b0e2b`. Não foram lidas soluções, valores do coordenador ou demais arquivos da implementação. Resultados numéricos próprios: [JSON](FUN-02-p2-preliminar-calculos.json).

## Dimensões, domínio e potencial de A

θ, ν, κ, seus diferenciais e os argumentos dos logaritmos são adimensionais. α, βκ e suas integrais têm unidade J/mol. Φ também é molar, em J/mol; uma derivada em relação a T tem unidade J/(mol·K). As coordenadas independentes podem ser (θ,ν) ou (T,v_m), por transformação linear invertível com referências constantes positivas. Fixar ν equivale a fixar v_m.

O domínio D é aberto, convexo e portanto simplesmente conexo. Os coeficientes são suaves nele. Escrevendo α = M dθ + N dν, obtém-se

\[
M_\nu=E_0/\nu=N_\theta.
\]

O teste de exatidão global aplica-se; também podemos demonstrar o resultado construindo o potencial. Integrar M em θ fornece

\[
\Phi/E_0=\theta\ln\theta-\theta+\theta\ln\nu+g(\nu).
\]

Uma integração parcial deixa uma função da coordenada mantida, porque sua derivada em θ é zero. Comparar a derivada em ν com N dá `g′(ν)=ν−1/ν`, logo `g(ν)=ν²/2−lnν+C`. A referência exigida determina `C=1/2`:

\[
\boxed{\Phi=E_0[\theta\ln\theta-\theta+(\theta-1)\ln\nu+\nu^2/2+1/2]}.
\]

Em (1,1), o colchete vale zero. Sua derivada em θ é `lnθ+lnν`, e em ν é `ν+(θ−1)/ν`, confirmando ambos os coeficientes. Os logaritmos são unívocos em D.

## Exatidão de B e ciclos

Para B,

\[
\partial_\theta N_B-\partial_\nu M
=\frac{2E_0\kappa(\theta-2)}{\nu}.
\]

Isso desaparece em todo D somente para `κ=0`. Se `κ≠0`, a igualdade na linha θ=2 não fornece exatidão em nenhuma vizinhança bidimensional de seus pontos: qualquer bola aberta contida em D contém valores θ≠2 onde a expressão não zera. A restrição a uma linha não é esse teste bidimensional.

α tem integral nula em ambos os ciclos. Para a parcela adicional, os segmentos horizontais têm `dν=0`. Num retângulo anti-horário com lados θ=a e θ=b, entre ν=1 e ν=2,

\[
\oint(\beta_\kappa-\alpha)
=E_0\kappa[(b-2)^2-(a-2)^2]\ln2.
\]

No ciclo largo, os dois quadrados valem 1. A lateral direita contribui `+E₀κ ln2` e a esquerda `−E₀κ ln2`: cancelam para qualquer κ. O resultado nulo não identifica κ nem prova propriedade.

No ciclo esquerdo, os quadrados valem 0 e 1; a integral é `−E₀κ ln2`. Comparar com o ensaio exato `−20 ln2 J/mol` dá **κ=0,20**, dentro da família assumida. O segundo ciclo é compatível com B inexata e não deve ser descartado para salvar a interpretação do técnico.

## Percursos entre P e Q

Para A, `Φ(Q)−Φ(P)=E₀(3 ln2+1/2)`. O cálculo por trechos confirma:

- HV: horizontal `E₀(2 ln2−1)` e vertical `E₀(3/2+ln2)`.
- VH: vertical `3E₀/2` e horizontal `E₀(3 ln2−1)`.

Para B, a contribuição adicional em HV é zero, pois o segmento vertical tem θ=2. Em VH, o segmento vertical tem θ=1 e acrescenta `E₀κ ln2=20 ln2 J/mol`.

| Integral | A / J·mol⁻¹ | B, κ=0,20 / J·mol⁻¹ |
|---|---:|---:|
| P→Q por HV | 257,944154168 | 257,944154168 |
| P→Q por VH | 257,944154168 | 271,807097779 |
| C_largo | 0 | 0 |
| C_esquerdo | 0 | −13,862943611 |

O percurso HV seguido do inverso de VH é C_esquerdo na orientação indicada. Portanto `I_HV−I_VH=−20 ln2 J/mol` para B, coincidindo com o ciclo. Suas integrais diferentes entre os mesmos pontos são o contraexemplo explícito; não são duas variações de uma Φ de B.

## Parcial versus derivada ao longo de γ

Em S, T=600 K e v_m=0,002 m³/mol. Para o potencial de A,

\[
\left(\frac{\partial\Phi}{\partial T}\right)_{v_m}
=\frac{E_0}{T_{ref}}(\ln\theta+\ln\nu)
=\frac{E_0}{T_{ref}}\ln4
\approx0,462098120\;\mathrm{J/(mol\,K)}.
\]

Ao longo de ν=θ, `v_m(T)=v_ref T/T_ref`. A regra da cadeia fornece

\[
\frac{d\Phi_\gamma}{dT}
=\left(\frac{\partial\Phi}{\partial T}\right)_{v_m}
+\left(\frac{\partial\Phi}{\partial v_m}\right)_T
\frac{dv_m}{dT}.
\]

Em S, a segunda parcial vale `(E₀/v_ref)(5/2)=250000 J/m³` e `dv_m/dT=v_ref/T_ref`. Sua contribuição é `0,833333333 J/(mol·K)`, resultando em **1,295431454 J/(mol·K)**. Logo o número publicado está correto para a derivada no caminho, mas seu rótulo de parcial está errado. A derivada em θ deve ser multiplicada por `dθ/dT=1/T_ref` antes de ser informada por kelvin; a mesma conversão se aplica à derivada total parametrizada por θ.

## Decisão preliminar sobre o modelo

A pode ser aceita como diferencial de uma função escalar global em D. B com κ identificado deve ter essa interpretação rejeitada. Impor κ=0 transforma B em A, mas passa a prever zero no ciclo esquerdo: não reproduz o ensaio exato já registrado. Tal correção demanda reconhecer mudança de versão ou refazer os ensaios pertinentes, não apagar arbitrariamente a evidência anterior.

A afirmação global de A está limitada a D. Em ν=0 há singularidades; as fórmulas não podem atravessá-la. O logaritmo de θ também restringe a expressão real adotada a θ>0. Exatidão e unidades de energia não demonstram lei constitutiva, estabilidade ou identificação física como U, Q ou W. Esta conclusão é sobre o registrador matemático explicitamente declarado, sem extrapolar a identificação de κ para defeitos arbitrários.

A versão final integrada deverá ser comparada com este enunciado antes de reaproveitar a memória. Não há ainda avaliação do ensino, das soluções/rubricas ou do pacote FUN-02 como um todo.
