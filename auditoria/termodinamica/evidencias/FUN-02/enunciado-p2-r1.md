# Problema 2 — Um registrador pode confundir percurso com propriedade?

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
