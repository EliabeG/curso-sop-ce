# FUN-02 — Apoio autoral: integrabilidade e calibração

**Responsável:** agente de apoio do Corretor `apoio_fun01`. **Data:** 27/10/2026. **Versão:** r1. **Escopo:** somente o problema P2 de FUN-02. Este apoio não altera o produto, o inventário nem o controle. O parecer de aceite pertence ao Auditor.

## Objetivo, pré-requisitos e rastreabilidade

**Objetivo observável:** decidir se duas regras de acumulação admitem uma propriedade global, reconstruir o potencial admissível e produzir um contraexemplo orientado à alegação rejeitada; corrigir uma derivada cuja condição mantida foi trocada.

**Pré-requisitos:** coordenadas independentes e domínio; derivadas de potências e logaritmos; derivadas parciais e regra da cadeia; integral de uma variável e mudança de sinal ao inverter limites; diferença entre temperatura e coordenada adimensional; volume molar e energia molar. O uso de ln, a integração que aparece na reconstrução e a conversão por kelvin recebem preparação específica abaixo. A teoria geral de formas exatas, constantes de integração parcial e domínio é fornecida pela unidade FUN-02.

**Vínculos parciais:** C01 (restrições e domínio do modelo), C02 (critério matemático para uma propriedade candidata), C08 (integração, unidades e reprodução), C09 (refutação por contraexemplo e identificação condicionada ao modelo), C10 (parecer argumentado). A atividade não demonstra nenhuma dessas competências integralmente, não constrói equação fundamental de substância real e não substitui os problemas P1/P3 sobre calor e trabalho.

O modelo e os dados são autorais. O problema combina identificação de um parâmetro, cancelamento em ciclo não degenerado, reconstrução de potencial e troca de condição mantida. Não é uma troca de coeficientes dos exemplos da unidade f = θν ou η = (3θ² + ν)dθ + θdν. O enunciado isolado está em `enunciado-p2-r1.md`, para permitir sua resolução antes da consulta à solução.

## Preparação específica — coordenadas, logaritmos e trechos

**Coordenadas normalizadas não mudam as unidades da propriedade.** Se θ = T/T_ref e ν = v_m/v_ref, com referências constantes, então dθ = dT/T_ref e dν = dv_m/v_ref. A forma A(θ,ν)dθ + B(θ,ν)dν terá unidade J/mol se ambos os coeficientes tiverem essa unidade. Já uma derivada por kelvin exige o fator 1/T_ref: (∂Φ/∂T)_{v_m} = (1/T_ref)(∂Φ/∂θ)_ν. Manter ν constante equivale a manter v_m constante porque v_ref é constante. v_m é volume **molar**, em m³/mol, e não o volume específico por massa. A explicitação das coordenadas mantidas no diferencial total segue a notação do [apêndice 4.1 da University of Washington, CHEM452, Winter 2023](https://faculty.washington.edu/jcv2/CHEM452_WI2023/html/appendix_differentials.html).

**A integral de ln que será necessária.** Para uma variável adimensional x > 0, d(x ln x − x)/dx = ln x. Portanto ∫ ln x dx = x ln x − x + constante. A verificação por derivação evita depender de uma tabela de integrais. Por exemplo, ∫ de 1 até e de ln x dx = 1: nos limites, x ln x − x vale 0 e −1. Também ∫ de a até b de dx/x = ln(b/a), para a,b > 0. Todos os argumentos dos logaritmos são adimensionais.

**Como percorrer um retângulo sem presumir exatidão.** Num trecho com ν constante, dν = 0, e só se integra o coeficiente de dθ. Num trecho com θ constante, só se integra o coeficiente de dν. Inverter o sentido de um trecho troca o sinal de sua integral. Uma soma de quatro trechos pode resultar em zero por cancelamento; isso não transforma os quatro coeficientes em derivadas de uma propriedade. Os resultados devem ser interpretados com o teste e as condições de domínio ensinados na unidade. A independência de todos os caminhos e o teste global em domínio aberto simplesmente conexo são tratados no [OpenStax, Calculus 3, §6.3](https://openstax.org/books/calculus-volume-3/pages/6-3-conservative-vector-fields).

**Decisão curta antes do exercício.** Um relatório apresenta 240 J/mol como derivada de uma grandeza energética em relação à coordenada adimensional ζ = T/(400 K), mas coloca no cabeçalho “J/(mol·K)”. O cabeçalho está errado: para informar a derivada em relação a T com as mesmas outras coordenadas mantidas, é necessário dividir por 400 K, obtendo 0,600 J/(mol·K). Uma mudança de rótulo não efetua essa conversão. No P2, será necessário ainda decidir se a mesma outra coordenada foi mantida.

## Enunciado


Um registrador didático acumula incrementos com unidade de energia por mol ao percorrer pares de coordenadas. Sua documentação afirma que o valor acumulado entre dois pontos é sempre a variação de uma propriedade Φ. Você deve decidir se essa afirmação é compatível com as expressões do registrador e com os testes fornecidos.

Este é um **modelo matemático de consistência**, não uma equação fundamental de uma substância real. As coordenadas fazem referência a temperatura T e **volume molar v_m**, mas não se fornecem leis constitutivas que tornem o modelo uma descrição física completa. Exatidão matemática, por si só, não comprova estabilidade, admissibilidade termodinâmica ou interpretação como energia interna, calor ou trabalho.

## Coordenadas, domínio e versões

Defina **θ = T/T_ref** e **ν = v_m/v_ref**, com **T_ref = 300 K**, **v_ref = 0,001 m³/mol** e **E₀ = 100 J/mol**. O domínio de interesse é **D = {(θ,ν): θ > 0 e ν > 0}**. θ, ν e o parâmetro constante κ são adimensionais. Todos os logaritmos são naturais. Os caminhos são contínuos e suaves por trechos, inteiramente contidos em D.

A versão A registra a forma

**α = E₀[(ln θ + ln ν)dθ + (ν + (θ − 1)/ν)dν].**

A versão B registra uma família de formas

**β_κ = α + E₀ κ(θ − 2)² dν/ν.**

O valor κ é desconhecido, constante durante todos os ensaios. A forma β_κ é a família assumida para identificar esse parâmetro; nenhuma conclusão de identificação deve ser extrapolada a modelos de defeito arbitrários. Para uma forma ω, o registrador imprime **I_γ = ∫_γ ω**, em J/mol. Só será legítimo escrever I_γ = Φ(final) − Φ(inicial) se a existência dessa propriedade no domínio tiver sido demonstrada.

## Registros disponíveis

Um técnico verificou as derivadas cruzadas dos coeficientes de B apenas nos pontos da linha **θ = 2**, com ν > 0. Elas coincidiram. Em seguida, executou dois ciclos. Em ambos, cada par ordenado abaixo é (θ,ν), e os vértices são percorridos na ordem indicada, com ligação por segmentos retos. Essa ordem corresponde ao sentido anti-horário, com θ no eixo horizontal e ν no vertical.

| Ensaio com a versão B | Caminho orientado | Integral impressa |
|---|---|---:|
| C_largo | (1,1) → (3,1) → (3,2) → (1,2) → (1,1) | 0 J/mol |
| C_esquerdo | (1,1) → (2,1) → (2,2) → (1,2) → (1,1) | −20 ln 2 J/mol, aproximadamente −13,862944 J/mol |

Os valores exatos pertencem ao modelo didático. O valor decimal serve para reprodução e não introduz uma faixa de incerteza experimental. O parecer do técnico foi: “A igualdade das derivadas cruzadas na linha de calibração e o fechamento nulo de C_largo provam que B mede uma propriedade; o segundo ciclo deve ser descartado”.

Há ainda um relatório sobre a **versão A**. Após reconstruir seu potencial com referência **Φ(1,1) = 0**, o técnico percorreu a trajetória **γ: ν = θ**, tomando T como parâmetro. No ponto S = (2,2), registrou a inclinação

**s_γ = (E₀/T_ref)[ln 4 + 5/2] ≈ 1,295431 J/(mol·K),**

e a rotulou como **(∂Φ/∂T)_{v_m}**. O fator E₀/T_ref já carrega a unidade J/(mol·K).

## Parecer solicitado

1. Confira as dimensões de α, β_κ, I_γ e de uma derivada de Φ em relação a T. Declare as variáveis independentes e explique por que ν fixo equivale a v_m fixo neste modelo. Verifique a regularidade dos coeficientes e as propriedades do domínio necessárias ao teste global de exatidão.
2. Determine se A admite potencial global unívoco em D. Se admitir, reconstrua-o a partir dos coeficientes, imponha Φ(1,1) = 0 e confira o resultado por diferenciação. Explique por que a constante de uma integração parcial pode depender da outra coordenada.
3. Determine todos os valores de κ para os quais B admite potencial em D. Explique por que a coincidência das derivadas cruzadas na linha θ = 2 não prova exatidão em uma região aberta. Para κ diferente de zero, essa coincidência garante ao menos uma vizinhança bidimensional de exatidão em torno de um ponto dessa linha? Justifique.
4. Calcule as integrais nos dois ciclos com orientação explícita e identifique κ sob a família β_κ assumida. Analise o parecer do técnico. Mostre o mecanismo de cancelamento no ciclo largo: não basta afirmar genericamente que “um ciclo nulo não prova exatidão”.
5. Compare dois caminhos de P = (1,1) a Q = (2,2): γ_HV, que passa por (2,1), e γ_VH, que passa por (1,2). Calcule as integrais de A e de B nos dois percursos, usando κ identificado. Relacione a diferença entre os percursos ao ciclo C_esquerdo, respeitando a orientação. Esses caminhos devem fornecer um contraexemplo explícito à alegação de B, sem confundir sua integral com uma variação de uma propriedade inexistente.
6. Corrija o rótulo da inclinação s_γ. Calcule a parcial verdadeira (∂Φ/∂T)_{v_m} em S e obtenha a derivada ao longo de γ por regra da cadeia. Discuta se a inclinação publicada é numericamente errada, se a condição mantida foi trocada e por que uma derivada em relação a θ precisa ser convertida antes de ser informada por kelvin. Use o potencial de A; não presuma uma Φ para B quando κ for diferente de zero.
7. Proponha uma decisão sobre as versões A e B: aceitar como diferencial de propriedade, rejeitar essa interpretação ou corrigir o modelo. Se propuser κ = 0, explique o que acontece com a reprodução dos ensaios já registrados. Declare também o alcance da conclusão local/global, por que não se pode estender as fórmulas através de ν = 0 e por que unidades de energia não identificam automaticamente α ou β_κ como calor, trabalho ou energia interna de uma substância real.

Apresente integrais ou diferenças de potencial reproduzíveis, uma tabela de resultados e uma decisão argumentada. A concordância de um único número ou de uma única linha de calibração não substitui o teste da alegação no domínio declarado.

## Solução comentada

### 1. Dimensões, regularidade e domínio

θ, ν, κ, dθ e dν são adimensionais. E₀ tem unidade J/mol; os coeficientes de α e β_κ, suas integrais e o potencial Φ, quando existir, têm unidade J/mol. A derivada em relação a T tem unidade J/(mol·K). A variável física correspondente a ν é v_m, explicitamente molar.

As coordenadas independentes do modelo são θ e ν. Todos os coeficientes são de classe C¹, e de fato suaves, em D porque θ > 0 e ν > 0 tornam os logaritmos e as divisões regulares. O quadrante positivo é aberto e convexo: o segmento entre dois de seus pontos continua com as duas coordenadas positivas. Ele é, portanto, conexo e simplesmente conexo. A igualdade das derivadas cruzadas **em todo D**, nessas condições, é suficiente para a existência de um potencial global unívoco. Não se está aplicando o teste a uma curva isolada ou a um domínio de regularidade desconhecida.

### 2. Reconstrução e verificação do potencial de A

Escreva α = M_α dθ + N_α dν. Então

**M_α = E₀(ln θ + ln ν)** e **N_α = E₀[ν + (θ − 1)/ν]**.

As derivadas cruzadas são iguais a E₀/ν. A hipótese global é satisfeita em D. Para reconstruir Φ, integre M_α em θ, mantendo ν constante:

**Φ/E₀ = θ ln θ − θ + θ ln ν + g(ν).**

A “constante” dessa integração parcial é uma função g de ν: a derivação em θ não a detecta. Diferenciando em ν e comparando com N_α/E₀,

**θ/ν + g′(ν) = ν + (θ − 1)/ν**, portanto **g′(ν) = ν − 1/ν**.

Integrando, **g(ν) = ν²/2 − ln ν + C**. A condição Φ(1,1) = 0 exige C = 1/2. Logo,

**Φ(θ,ν) = E₀[θ ln θ − θ + (θ − 1)ln ν + ν²/2 + 1/2].**

A verificação completa devolve **(∂Φ/∂θ)_ν = E₀(ln θ + ln ν)** e **(∂Φ/∂ν)_θ = E₀[ν + (θ − 1)/ν]**. A referência vale zero em (1,1). O potencial é real e unívoco em D; a expressão explícita fornece também uma prova construtiva global. Uma referência aditiva diferente alteraria os valores de Φ, mas não seus diferenciais nem diferenças entre estados.

### 3. B: uma linha de coincidência não é uma região de exatidão

Para β_κ, M_β = M_α e N_β = N_α + E₀κ(θ − 2)²/ν. Assim,

**(∂M_β/∂ν)_θ = E₀/ν**,

**(∂N_β/∂θ)_ν = E₀[1 + 2κ(θ − 2)]/ν**.

As derivadas coincidem em todo D **se e somente se κ = 0**. Nesse caso β₀ = α e o potencial acima serve. Se κ ≠ 0, a diferença entre a segunda e a primeira derivada é **2E₀κ(θ − 2)/ν**, não identicamente nula.

Na linha θ = 2, essa diferença vale zero para qualquer κ. Contudo, toda vizinhança bidimensional aberta de um ponto dessa linha contém pontos com θ ≠ 2, onde a igualdade falha quando κ ≠ 0. Logo a coincidência na linha não garante nem uma vizinhança aberta de exatidão ao redor do ponto, muito menos exatidão global.

Ao restringir o percurso à linha θ = 2, dθ = 0 e β_κ = E₀(ν + 1/ν)dν, para qualquer κ. Existe uma antiderivada de uma variável ao longo dessa linha, E₀(ν²/2 + ln ν). Essa propriedade da restrição unidimensional não fornece uma Φ(θ,ν) no espaço bidimensional. A distinção local/global considera regiões abertas de estados, não apenas uma coincidência pontual.

### 4. Ciclos orientados e identificação de κ

A contribuição de α é nula em todo ciclo em D, porque α = dΦ. Para obter a contribuição adicional de B, é suficiente integrar os trechos, sem invocar um teorema de área não ensinado.

Considere o retângulo anti-horário (a,1) → (b,1) → (b,2) → (a,2) → (a,1), com 0 < a < b. Nos trechos horizontais, dν = 0. No vertical direito, θ = b e ν sobe de 1 a 2; a contribuição extra é **+E₀κ(b − 2)² ln 2**. No vertical esquerdo, θ = a e ν desce de 2 a 1; a contribuição extra é **−E₀κ(a − 2)² ln 2**. Portanto,

**∮ β_κ = E₀κ[(b − 2)² − (a − 2)²] ln 2.**

| Ciclo anti-horário | a, b | Integral de α | Integral de β_κ |
|---|---|---:|---:|
| C_largo | 1, 3 | 0 | E₀κ(1 − 1)ln 2 = 0 |
| C_esquerdo | 1, 2 | 0 | E₀κ(0 − 1)ln 2 = −E₀κ ln 2 |

O ciclo largo tem contribuições extras de mesma magnitude e sinais opostos: o lado direito soma E₀κ ln 2 e o esquerdo subtrai essa quantidade. É um ciclo simples, com área não nula, cujo resultado zero ocorre por cancelamento. Não é necessário retrilhar um caminho para produzir esse falso indício de exatidão. Os dois retângulos que dividem o ciclo largo na linha θ = 2 também dão contribuições opostas.

Sob a família β_κ assumida e com os dados exatos fornecidos,

**−100κ ln 2 = −20 ln 2 ⇒ κ = 0,200.**

O ciclo C_largo sozinho não identifica κ, pois seu valor é zero para qualquer parâmetro dessa família. C_esquerdo identifica κ porque seu fator −E₀ ln 2 é não nulo. Esse resultado é condicionado à forma do defeito postulada: dois ciclos não identificariam um campo de erro arbitrário. O parecer do técnico deve ser rejeitado; o segundo ciclo é coerente com B e é precisamente o contraexemplo que refuta sua interpretação como diferencial de uma propriedade global.

### 5. Dois caminhos entre os mesmos pontos

Para A, a diferença de potencial entre P = (1,1) e Q = (2,2) é

**Φ(Q) − Φ(P) = E₀(3 ln 2 + 1/2) ≈ 257,944154 J/mol.**

O cálculo por trechos confirma a decisão:

| Caminho de P a Q | Primeiro trecho de α | Segundo trecho de α | Soma de α |
|---|---:|---:|---:|
| γ_HV via (2,1) | E₀(2 ln 2 − 1) | E₀(3/2 + ln 2) | E₀(3 ln 2 + 1/2) |
| γ_VH via (1,2) | (3/2)E₀ | E₀(3 ln 2 − 1) | E₀(3 ln 2 + 1/2) |

Na versão B, o termo extra de γ_HV é zero: no trecho horizontal não há dν, e no vertical θ = 2 anula (θ − 2)². Em γ_VH, o trecho vertical acontece em θ = 1 e soma E₀κ ln 2; o horizontal novamente não acrescenta esse termo. Para κ = 0,200:

| Forma e caminho | Integral exata | Valor aproximado / J/mol |
|---|---|---:|
| α em γ_HV | E₀(3 ln 2 + 1/2) | 257,944154 |
| α em γ_VH | E₀(3 ln 2 + 1/2) | 257,944154 |
| β_0,2 em γ_HV | E₀(3 ln 2 + 1/2) | 257,944154 |
| β_0,2 em γ_VH | E₀(3 ln 2 + 1/2) + 20 ln 2 J/mol | 271,807098 |

Percorrer γ_HV de P a Q e retornar por γ_VH invertido produz C_esquerdo. Logo **I_HV − I_VH = −20 ln 2 J/mol ≈ −13,862944 J/mol** para B. Trocar a ordem troca o sinal. A coincide em ambos os caminhos por exatidão; B coincide com A num caminho particular porque o termo defeituoso se anula ao longo dele. Essa coincidência isolada também não demonstra existência de uma propriedade para B.

### 6. Corrigir uma condição mantida, sem inventar erro no número

Para o potencial de A, no ponto S = (2,2),

**(∂Φ/∂θ)_ν = E₀ ln 4**, e **(∂Φ/∂ν)_θ = (5/2)E₀**.

Como θ = T/T_ref, a parcial verdadeira a volume molar fixo é

**(∂Φ/∂T)_{v_m} = (E₀/T_ref)ln 4 ≈ 0,462098 J/(mol·K).**

Ao longo de γ, ν = θ e dν/dθ = 1. Aplicando a regra da cadeia,

**dΦ/dθ|_γ = (∂Φ/∂θ)_ν + (∂Φ/∂ν)_θ(dν/dθ) = E₀[ln 4 + 5/2]**, em S.

Multiplicar por dθ/dT = 1/T_ref fornece

**dΦ/dT|_γ = (E₀/T_ref)[ln 4 + 5/2] ≈ 1,295431 J/(mol·K).**

O número do relatório é correto como inclinação ao longo de γ. O rótulo de parcial a v_m constante está errado. O percurso mantém ν/θ = 1, enquanto v_m aumenta com T: dv_m/dT = v_ref/T_ref. A contribuição omitida ao trocar a condição mantida seria **(5/2)E₀/T_ref = 0,833333 J/(mol·K)**. Uma derivada por θ tem unidade J/mol, pois θ é adimensional; ela não pode ser chamada de derivada por kelvin sem a conversão.

Aqui “derivada ao longo do caminho” usa T ou θ como parâmetro; não se está usando uma derivada direcional normalizada por comprimento de arco no plano das coordenadas. Não se pode inferir uma capacidade térmica a volume constante a partir desses números: não foi estabelecido que Φ seja a energia interna de uma substância física.

### 7. Decisão e alcance

**A:** aceitar a interpretação matemática α = dΦ em todo D, com o potencial e a referência demonstrados. Isso certifica a consistência da acumulação como diferença de uma função de estado do modelo, não a admissibilidade de uma equação fundamental física.

**B com κ = 0,200:** rejeitar a interpretação como diferencial de propriedade em D. Suas integrais são quantidades associadas aos percursos especificados. O resultado não nulo de um ciclo basta para refutar o potencial global; o zero do outro não desfaz o contraexemplo.

**Possível correção:** retirar o termo adicional, isto é, impor κ = 0, torna B igual a A. Essa mudança faz C_esquerdo passar a zero; portanto não reproduz o valor −20 ln 2 já registrado. É preciso declarar que se corrigiu o algoritmo/modelo e, se houver registros anteriores, reprocessá-los ou investigar sua origem. Não é legítimo manter o mesmo relato dos ensaios e anunciar que todos continuam representados. Somar uma constante de referência à suposta propriedade não resolve a inexatidão, pois o diferencial de uma constante é zero.

**Domínio:** em D, regularidade e simples conexão autorizam a passagem do teste em toda a região para a conclusão global. Igualdade apenas na linha θ = 2 não dá garantia local bidimensional. As fórmulas não podem ser estendidas através de ν = 0 com o mesmo modelo: ln ν e 1/ν não são regulares ali. θ = 0 também está fora do domínio. A falta de simples conexão em algum outro domínio não provaria, por si, inexatidão; seria necessário reexaminar a garantia global ou verificar um potencial explícito. Neste problema não há furo no domínio positivo.

**Interpretação física:** dimensão de energia molar é necessária para o rótulo energético, mas não identifica uma interação ou propriedade física. Sem sistema, equação fundamental, restrições de processo e balanços correspondentes, não se pode chamar α ou β_κ de δQ, δW ou dU de uma substância real. O ciclo não nulo de B demonstra um defeito na alegação matemática do registrador; não é uma demonstração de violação experimental da primeira lei.

## Rubrica analítica — 10 pontos

| Critério | Pontos | Evidência para pontuação integral | Crédito parcial |
|---|---:|---|---|
| Coordenadas, unidades e domínio | 1,0 | Declara v_m molar, θ e ν independentes, unidades corretas, coeficientes C¹ e D aberto convexo/simplesmente conexo. | 0,5 se as unidades estiverem corretas, mas faltar justificar o domínio ou a regularidade. |
| Reconstrução de A | 2,0 | Integra mantendo a outra coordenada fixa, determina g(ν), aplica Φ(1,1) = 0 e verifica as duas parciais. | Até 1,0 se obtiver o potencial sem reconstrução ou sem a verificação completa; erro aritmético isolado não anula a modelagem correta. |
| B e limite local/global | 1,5 | Obtém o defeito das cruzadas, κ = 0 como único caso exato e explica por que θ = 2 não contém uma vizinhança aberta de exatidão para κ ≠ 0. | 0,8 se classificar κ corretamente, mas omitir a distinção entre linha e vizinhança. |
| Ciclos e identificação | 2,0 | Mostra os trechos verticais, orientação e cancelamento em C_largo; calcula C_esquerdo e identifica κ = 0,200 condicionado à família assumida. | Até 1,0 se acertar κ sem demonstrar a orientação ou o cancelamento; não atribuir pontuação integral a uma fórmula sem interpretação. |
| Contraexemplo por dois caminhos | 1,5 | Calcula as quatro integrais, mostra diferença de 20 ln 2 em B e relaciona I_HV − I_VH ao ciclo orientado. | 0,8 se demonstrar dependência do caminho, mas omitir parte dos cálculos ou a orientação da diferença. |
| Derivada e condição mantida | 1,0 | Obtém as duas derivadas, distingue o número correto do rótulo errado e faz a conversão 1/T_ref. | 0,5 se aplicar a regra da cadeia, mas omitir a unidade ou a condição mantida. |
| Decisão e limites | 1,0 | Decide sobre A/B, explica por que κ = 0 muda os ensaios e distingue integrabilidade matemática de admissibilidade física. | 0,5 se decidir corretamente, mas não discutir a alteração dos ensaios ou o alcance físico. |

**Critério pedagógico desta atividade:** pelo menos 8/10 e nenhum dos erros críticos abaixo. O limiar ainda não foi calibrado com estudantes; ele não constitui certificação das competências completas do curso.

**Erros críticos que exigem correção:**

- Certificar B por um único ciclo nulo, por igualdade em θ = 2 ou por concordância num caminho particular.
- Chamar a integral de β_0,2 de diferença entre valores de uma propriedade global Φ_B sem enfrentar o contraexemplo.
- Ignorar a orientação dos ciclos para conciliar sinais incompatíveis, ou inverter o sinal de um trecho sem inverter seu sentido.
- Omitir a condição mantida e declarar que (∂Φ/∂T)_{v_m} vale a inclinação de ν = θ.
- Usar o número de uma derivada por θ como se já estivesse em J/(mol·K), sem o fator 1/T_ref.
- Afirmar que redefinir a referência de Φ elimina a inexatidão, ou que impor κ = 0 continua reproduzindo C_esquerdo = −20 ln 2.
- Concluir que a exatidão encontrada comprova uma energia interna fisicamente admissível, ou que a dimensão energética transforma qualquer forma em calor ou trabalho.

## Fontes, dados e revisão

Consultas feitas em **27/10/2026**. Foram lidos o [OpenStax, Calculus Volume 3, §6.3](https://openstax.org/books/calculus-volume-3/pages/6-3-conservative-vector-fields), para potencial, independência de caminho e hipóteses do teste global, e o [apêndice 4.1, University of Washington, CHEM452, Winter 2023](https://faculty.washington.edu/jcv2/CHEM452_WI2023/html/appendix_differentials.html), para diferencial total e condições mantidas. A formulação resumida de exatidão da segunda fonte é usada com as condições explícitas de regularidade e domínio da primeira. Nenhum exemplo dessas fontes foi reproduzido.

**Dados autorais:** pacote E1-FUN02 v1.0, atividade `fun02-e1-integrabilidade`; T_ref = 300 K, v_ref = 0,001 m³/mol, E₀ = 100 J/mol; parâmetro κ constante; domínio positivo e ciclos conforme enunciado. O valor −20 ln 2 J/mol é dado exato do modelo, não uma medição laboratorial. Usar os valores sem arredondamento intermediário; os decimais publicados têm finalidade de conferência.

**Revisão:** coordenador rederivou potencial, ciclos, parâmetro e derivadas e informou concordância. A conferência não foi cega: resultados preliminares foram enviados antes da instrução de isolar o enunciado. O arquivo `enunciado-p2-r1.md` contém apenas o problema e está disponível para resolução independente do Auditor. A aprovação de FUN-02 permanece fora deste apoio.

**Limites da independência pedagógica:** o aluno recebe na preparação identidades de integração e conversão de coordenadas, mas precisa escolher o teste, obter o potencial, analisar o cancelamento não degenerado, identificar κ, construir o contraexemplo e reparar a condição mantida. A atividade não depende de gabaritos nem de dados dos bancos Q/CR/AV ou de FUN-01.


## Conferência numérica do apoio

As integrais de cada segmento foram recalculadas por quadratura de Simpson, com 10 000 subintervalos, diretamente dos coeficientes M e N. Esse procedimento foi confrontado com o potencial e com as expressões analíticas dos ciclos, sem usar o valor final analítico como integrando. Foram obtidos α(γ_HV) = 257,94415416798387 J/mol, α(γ_VH) = 257,944154167984 J/mol, β(γ_HV) = 257,94415416798387 J/mol e β(γ_VH) = 271,807097779183 J/mol. C_largo retornou −1,7337×10⁻¹² J/mol, resíduo numérico compatível com zero; C_esquerdo retornou −13,862943611199029 J/mol, contra o valor analítico −13,862943611198906 J/mol. O maior resíduo absoluto entre os cinco confrontos foi inferior a 1,8×10⁻¹² J/mol. A parcial a v_m fixo foi 0,46209812037329684 J/(mol·K) e a inclinação de γ foi 1,2954314537066303 J/(mol·K). A interpretação de zero é analítica; a quadratura é uma conferência numérica, não a prova de exatidão.
