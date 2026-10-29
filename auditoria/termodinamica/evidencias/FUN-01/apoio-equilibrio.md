# FUN-01 — Rascunho autoral: diagnóstico de uma bancada multicâmara

**Status:** apoio do Corretor, sujeito à integração e à revisão independente. **Data:** 27/10/2026. **Versão:** 1.0. **Responsável por este rascunho:** agente de apoio `apoio_fun01`. Não constitui parecer do Auditor nem aceite de FUN-01.

## Finalidade e lugar na unidade

**Objetivo observável:** produzir um diagnóstico que distinga equilíbrio térmico, balanço de forças, equilíbrio de transferência de matéria e coexistência de fases; rejeitar registros incompatíveis com o modelo e calcular um estado final sob restrições explicitadas.

**Pré-requisitos:** pressão absoluta; balanço estático de forças; quantidade de matéria e fração molar; gás ideal e pressão parcial; logaritmo natural; conservação de cada espécie; significado de potencial químico e de restrição de uma fronteira. Para a parte gravitacional: diferencial de uma função, integração com coeficiente constante e diferença entre grandezas molares e específicas por massa. A unidade deve ensinar previamente as relações da caixa de ferramentas abaixo; fornecer uma fórmula sem desenvolver seu significado não supre esse pré-requisito.

**Vínculo parcial com a matriz:** C01, fronteiras, restrições e hipóteses; C02, identificação de regiões e limites do par de propriedades; C07, composição e equilíbrio de transferência em mistura ideal não reativa; C08, reprodução e resíduos de conservação; C09, rejeição fundamentada de dados; C10, parecer técnico. A atividade não demonstra integralmente nenhuma dessas competências e não avalia misturas reais, reações, ciclos, exergia ou região supercrítica. Esses conteúdos não devem ser considerados cobertos por este rascunho.

O problema, seus números, a combinação das montagens e a rubrica são autorais. Não adapta questões Q, CR ou AV do E1 nem reproduz um exercício das fontes. É candidato a exercício independente; o Corretor deve confrontá-lo com o exemplo resolvido que vier a publicar, para evitar que ambos repitam a mesma sequência de decisões.

## Preparação a ensinar antes do exercício

**Potencial químico e comparação entre regiões.** O potencial químico molar μ_i mede a variação do potencial termodinâmico apropriado por mol acrescentado da espécie i, mantidas as demais variáveis pertinentes. Sua unidade é J/mol. Para descobrir se A tende a atravessar uma fronteira, comparam-se μ_A nos dois lados, à mesma temperatura e com as contribuições externas relevantes consideradas. Comparar μ_A de um lado com μ_B do outro não responde a essa pergunta. Uma barreira que bloqueia determinada troca retira aquela possibilidade de evolução: a inexistência de fluxo através dela não prova que os potenciais químicos correspondentes sejam iguais.

**Mistura ideal e logaritmo.** A pressão parcial de A é p_A = y_Ap. A relação do modelo é μ_A = μ_A°(T) + RT ln(p_A/p°). O argumento do logaritmo é adimensional: duas pressões devem ser escritas na mesma unidade antes de formar o quociente. ln é o logaritmo natural, inverso da exponencial; ln(1) = 0, ln(r) > 0 se r > 1 e ln(r) < 0 se 0 < r < 1. A identidade ln(a) − ln(b) = ln(a/b) permite comparar dois estados da mesma espécie à mesma T sem conhecer o valor de referência μ_A°: Δμ_A = RT ln(p_A,2/p_A,1). Para calcular, pode-se usar a tecla `ln` ou `Math.log` em JavaScript. RT tem unidade J/mol; a razão e seu logaritmo não têm unidade. Esse uso de pressão parcial e potencial químico segue a [aula 13 do MIT 3.020](https://ocw.mit.edu/courses/3-020-thermodynamics-of-materials-spring-2021/mit3_020s21_l13.pdf).

**Decisão resolvida curta, anterior e diferente do problema.** Dois reservatórios grandes de mistura ideal, à mesma temperatura, apresentam: γ com p = 80 kPa e y_A = 0,250; δ com p = 160 kPa e y_A = 0,125. Um relatório afirma que “a diferença de pressão total, sozinha, prova diferença de potencial químico de A”. A afirmação é rejeitada: p_A,γ = p_A,δ = 20 kPa, logo μ_A,δ − μ_A,γ = RT ln(1) = 0. As pressões totais distintas não bastam para decidir a transferência seletiva de A. Isso também não prova equilíbrio em relação a B: suas pressões parciais são 60 e 140 kPa. Esta decisão compara estados dados; não envolve redistribuição em volumes finitos nem calcula o estado final do exercício.

**Energia gravitacional e convenção.** Neste material, μ(T,p) exclui energia gravitacional. Uma quantidade dn, em mol, tem massa M dn e energia potencial gravitacional Mgz dn. Portanto, a variação energética relevante para comparar a mesma espécie em alturas diferentes contém o potencial molar μ̃ = μ + Mgz. Para um líquido incompressível isotérmico, dμ = V̄ dp e V̄ = M/ρ. O balanço hidrostático produz dp/dz = −ρg; ao substituir, dμ/dz = −Mg e d(μ + Mgz)/dz = 0. A pressão e o potencial químico intrínseco podem variar enquanto o potencial molar total permanece constante. Isso é uma derivação para as hipóteses indicadas, não uma regra de que todo gradiente é compatível com equilíbrio. O diferencial de G e sua relação com μ são apresentados em [Tong, §4.4](https://www.damtp.cam.ac.uk/user/tong/statphys/statmechhtml/S4.html#S4.SS4).

**Função a minimizar e teste de estabilidade.** Para as células com T e volumes fixos, a função apropriada é F = U − TS. Uma transferência infinitesimal de A, da região de origem para a de destino, altera F por (μ_A,destino − μ_A,origem)dn. O sentido espontâneo permitido reduz F. A igualdade dos potenciais químicos fornece um ponto estacionário; um segundo teste é necessário para afirmar que ele é mínimo. Para uma referência constante n_ref e uma quantidade positiva n(ξ), a regra da cadeia fornece d ln[n(ξ)/n_ref]/dξ = (1/n)dn/dξ. Essa identidade será suficiente para o teste na mistura ideal. Pode ser verificada pela derivação do logaritmo ou usada como relação matemática já estabelecida. Não é necessário dominar teoria geral de estabilidade para este exercício. O critério de mínimo de F a T,V fixos e a presença do termo material em seu diferencial são tratados em [Tong, §4.4](https://www.damtp.cam.ac.uk/user/tong/statphys/statmechhtml/S4.html#S4.SS4).

## Enunciado para o aluno

Você recebeu a responsabilidade de validar a afirmação: “A bancada está em equilíbrio porque não há movimento visível e os manômetros indicam pressões iguais”. Produza um parecer com modelo, cálculos, decisão e limitações. A bancada possui dois módulos sem conexão material entre si.

### Módulo H — coluna com duas fases de uma substância pura

Um recipiente rígido vertical contém uma coluna líquida de altura **H = 2,00 m**, com vapor da mesma substância acima de uma interface plana. Defina **z = 0** no fundo e **z = H** na interface. A gravidade aponta para baixo. A capilaridade, tensões de cisalhamento, campos elétricos, reações e gradiente de pressão na pequena região de vapor podem ser desprezados. O líquido conduz calor. Não há parede térmica ou mecânica dentro da coluna. As forças exercidas pelas paredes laterais não sustentam o peso do líquido na direção vertical.

A substância **X é um modelo didático fictício**, não é água e não deve ser procurada em tabelas reais. Na vizinhança utilizada, seu líquido é incompressível, com **ρ = 1 000 kg/m³** e massa molar **M = 0,0200 kg/mol**. A **300,00 K**, as fases líquida e vapor podem coexistir em equilíbrio numa interface plana a **p_sat = 10,000 kPa absolutos**. Nessa temperatura, acima dessa pressão a fase líquida é a fase estável; não há outra transição relevante na faixa de pressões da atividade. Use **g = 9,81 m/s²**. Esses são parâmetros definidos pelo modelo, não medições de propriedades de uma substância real.

Dois registros foram apresentados, sempre com observação de líquido e vapor na interface:

| Registro | T na interface | T no fundo | p na interface | p no fundo | Declaração do operador |
|---|---:|---:|---:|---:|---|
| H-1 | 300,00 K | 302,00 K | 10,000 kPa | 10,000 kPa | Equilíbrio térmico, mecânico e de fases em toda a coluna |
| H-2 | 300,00 K | 300,00 K | 10,000 kPa | Valor que você deve determinar | Equilíbrio possível com pressão não uniforme |

Considere os números exatos dentro do modelo para testar consistência. Na parte experimental do parecer, discuta separadamente a necessidade de incertezas, calibração e resolução dos sensores. H-1 não deve ser “corrigido” por uma incerteza inventada.

### Módulo D — transferência seletiva em mistura ideal

Duas células pequenas, **α e β**, estão à mesma altura, cada uma com volume rígido **V = 0,0100 m³**, contendo uma mistura gasosa ideal dos componentes **A e B**, sem reação ou condensação na faixa considerada. As duas células permanecem em contato com um mesmo reservatório térmico a **300,00 K**. A gravidade dentro delas é desprezível.

Uma membrana fixa separa as células. Ela deixa passar **apenas A**, não armazena quantidade relevante dessa espécie e bloqueia completamente B. O suporte mantém os dois volumes constantes mesmo quando as pressões são diferentes; a deformação e o trabalho da membrana são desprezíveis. A membrana não cria uma diferença adicional de energia potencial para A entre seus dois lados. A bancada é fechada à matéria externa. No instante inicial, imediatamente após habilitar a passagem de A:

| Célula | T | p absoluta | Fração molar de A |
|---|---:|---:|---:|
| α | 300,00 K | 100,0 kPa | 0,800 |
| β | 300,00 K | 100,0 kPa | 0,200 |

Use **R = 8,314 J/(mol·K)**. Não há controlador que mantenha as pressões das células em 100 kPa durante a transferência.

### Caixa de ferramentas e convenções

Para uma substância pura homogênea, defina aqui **μ(T,p)** como potencial químico molar intrínseco, excluindo energia gravitacional. A temperatura constante, **dμ = V̄ dp**, sendo **V̄ = M/ρ** no líquido incompressível. Ao comparar alturas diferentes, o potencial molar total é **μ̃ = μ + Mgz**. Usar outra convenção de μ é permitido, desde que declarada e sem contar a gravidade duas vezes.

Em uma mistura gasosa ideal, **p_i = y_i p = n_i RT/V** e **μ_i(T,p_i) = μ_i°(T) + RT ln(p_i/p°)**. A referência da mesma espécie é a mesma nas duas células. Só se comparam diretamente potenciais químicos **da mesma espécie**. Para o conjunto α + β a temperatura e volumes fixos, a função que deve diminuir nas mudanças espontâneas permitidas é **F = U − TS**; sua variação material é **dF = Σ μ_i dn_i**. Não é necessário calcular a velocidade nem o tempo da transferência.

### Entregas exigidas

1. Desenhe as fronteiras e identifique quais trocas e deslocamentos cada uma permite. Diga quais critérios de equilíbrio podem ser impostos em cada conexão e quais não decorrem das restrições existentes.
2. Julgue H-1 separadamente nos aspectos térmico, mecânico e de fases. Derive o perfil de pressão requerido para H-2 por balanço de forças e calcule a pressão no fundo. Indique onde é válido usar p = p_sat(300 K), sem aplicar essa igualdade indiscriminadamente à coluna.
3. Para H-2, calcule μ_fundo − μ_interface e compare μ̃ nos dois níveis. Explique se o gradiente de pressão e a diferença de μ intrínseco contradizem o equilíbrio.
4. Decida se D está inicialmente em equilíbrio em relação à transferência permitida. Calcule a diferença inicial μ_A,α − μ_A,β e justifique o sentido inicial de transferência com o sinal da variação de F. Determine o estado final: quantidades de cada espécie em cada célula, pressões, frações molares e quantidade líquida de A transferida. Verifique a conservação de cada componente. Usando ξ como a quantidade de A transferida de α para β e a derivada do logaritmo ensinada na preparação, mostre que o ponto encontrado é um mínimo de F em relação a essa transferência; explicite por que isso não testa processos excluídos pelo modelo.
5. Julgue a afirmação “o estado final de D é impossível porque as pressões e as composições não são iguais”. Explique o papel do suporte e da impermeabilidade a B. Diga o que mudaria se, depois, a membrana passasse a deixar B atravessar, mantendo os mesmos volumes e temperatura.
6. Para uma **amostra pequena, sem variação gravitacional significativa**, classifique os dados abaixo como suficientes, insuficientes por redundância, insuficientes por falta de composição, ou incompatíveis com as condições declaradas. Especifique qual aspecto do estado se pretende determinar e qual dado faltante resolveria a deficiência: (a) X com líquido e vapor em equilíbrio, T = 300 K e p = 10 kPa, buscando a fração mássica de vapor; (b) X com líquido e vapor em equilíbrio numa interface plana, T = 300 K e p = 12 kPa; (c) mistura ideal A/B homogênea com T = 300 K e p = 100 kPa, buscando o estado intensivo completo incluindo composição; (d) a mesma mistura com T, p e y_A conhecidos, buscando seu estado intensivo, e depois buscando sua quantidade total.

Conclua com uma decisão sobre cada registro, os dados que ainda seriam necessários para uma validação experimental e os limites do seu cálculo. Uma lista de números sem decisões físicas não satisfaz a tarefa.

## Solução comentada para integração

### 1. As restrições vêm antes das igualdades

Em H, líquido e vapor trocam calor e partículas na interface. Ausentes curvatura e efeitos capilares, o balanço mecânico impõe continuidade da pressão **na interface**, à mesma altura. A coexistência em equilíbrio impõe a mesma temperatura e o mesmo potencial químico da substância nos dois lados dessa interface. Esses critérios são locais. A coluna tem um campo de pressão e não deve ser tratada como um único estado homogêneo com uma pressão global.

Em D, os volumes individuais não podem variar. A parede fixa e seu suporte podem equilibrar forças mesmo quando p_α ≠ p_β. A transferência de A é permitida, exigindo μ_A,α = μ_A,β no equilíbrio correspondente. A transferência de B é proibida; não existe a exigência de μ_B iguais para esse estado sob restrição. O reservatório térmico fixa a mesma temperatura em ambas as células. A igualdade inicial de pressões não fornece informação suficiente sobre o equilíbrio material.

### 2. Diagnóstico de H

**H-1 é incompatível com a declaração de equilíbrio térmico:** os dois valores de temperatura diferem dentro de um líquido condutor sem barreira interna. Um perfil estacionário mantido por aquecimento e resfriamento externos ainda teria transferência de calor e não seria equilíbrio térmico. Esses mecanismos nem foram especificados no modelo. A simples ausência de movimento visível não estabelece equilíbrio.

**H-1 também é incompatível com equilíbrio mecânico:** para uma lâmina de líquido com seção S e espessura dz, o balanço vertical é p(z)S − p(z+dz)S − ρS dz g = 0. Logo,

**dp/dz = −ρg**, e **p(z) = p(H) + ρg(H − z)**.

Para H-2, **p(0) = 10 000 + 1 000 × 9,81 × 2,00 = 29 620 Pa = 29,620 kPa absolutos**. O sinal é verificável: a pressão aumenta ao descer. Dimensionalmente, ρgH tem unidade kg/(m·s²) = Pa. Impor pressão uniforme eliminaria justamente a força que equilibra o peso do líquido. A relação é a aplicação, a este modelo, do balanço hidrostático tratado no [OpenStax, seção 14.1](https://openstax.org/books/university-physics-volume-1/pages/14-1-fluids-density-and-pressure).

**Fases:** os dados locais T_interface = 300 K e p_interface = 10 kPa são compatíveis com a coexistência estipulada pelo modelo. Isso não torna H-1 um estado global de equilíbrio nem informa o equilíbrio do fundo a 302 K: não foi fornecida a curva de saturação nessa temperatura. Em H-2, a pressão de saturação vale na interface. O fundo contém líquido a 300 K e p > p_sat, portanto líquido comprimido conforme o modelo, e não uma mistura líquido–vapor saturada a 29,620 kPa. Igualdade de potencial químico de fases em contato é um critério da coexistência, como desenvolvido por [Tong, seção 5.1.1](https://www.damtp.cam.ac.uk/user/tong/statphys/statmechhtml/S5.html#S5.SS1.SSS1).

### 3. Potencial químico e gravidade em H-2

**V̄ = M/ρ = 2,00 × 10⁻⁵ m³/mol**. Então,

**μ(0) − μ(H) = V̄[p(0) − p(H)] = 0,3924 J/mol**.

O termo gravitacional da interface excede o do fundo por **MgH = 0,3924 J/mol**. Portanto,

**[μ(0) + Mg·0] − [μ(H) + MgH] = 0**.

O mesmo resultado segue de dμ̃/dz = V̄(dp/dz) + Mg = −(M/ρ)ρg + Mg = 0. A unidade de V̄Δp é m³·Pa/mol = J/mol, a mesma de MgH. O potencial intrínseco é maior no fundo; a contribuição gravitacional é maior no alto. O equilíbrio não exige μ(T,p) intrínseco uniforme quando se comparam alturas diferentes sob essa convenção. A dedução usa a relação molar dμ = V̄ dp, obtida de G = nμ e do diferencial de G para substância pura a T constante; essas identidades e a distinção de F e G são apresentadas por [Tong, seção 4.4](https://www.damtp.cam.ac.uk/user/tong/statphys/statmechhtml/S4.html#S4.SS4).

### 4. Diagnóstico e estado final de D

Inicialmente, p_A,α = 80 kPa e p_A,β = 20 kPa. Com a mesma referência para A,

**μ_A,α − μ_A,β = RT ln(80/20) = 3 457,695 J/mol > 0**.

Se dn > 0 mol de A passam de α para β, dF = (μ_A,β − μ_A,α)dn < 0. O sentido inicial permitido é, assim, **α → β**. A igualdade de T e p total não basta: a composição altera a pressão parcial e o potencial químico. A expressão de μ em função da pressão parcial e a lei de Dalton utilizadas aqui são as da [aula 13 do MIT 3.020, primavera de 2021](https://ocw.mit.edu/courses/3-020-thermodynamics-of-materials-spring-2021/mit3_020s21_l13.pdf), partes 2 e 6.

Em cada célula, a quantidade inicial total é **n₀ = p₀V/(RT) = 0,400930158 mol**. Os inventários são:

| Quantidade | Inicial em α / mol | Inicial em β / mol | Final em α / mol | Final em β / mol |
|---|---:|---:|---:|---:|
| A | 0,320744126 | 0,080186032 | 0,200465079 | 0,200465079 |
| B | 0,080186032 | 0,320744126 | 0,080186032 | 0,320744126 |

A condição final μ_A,α = μ_A,β implica p_A,α = p_A,β. Como T e V são iguais, n_A,α = n_A,β. A conservação de A determina metade de seu total em cada célula. B permanece em sua célula original. Obtêm-se:

- **p_A final = 50,0 kPa**, em ambos os lados;
- **p_B,α final = 20,0 kPa** e **p_B,β final = 80,0 kPa**;
- **p_α final = 70,0 kPa** e **p_β final = 130,0 kPa**;
- **y_A,α final = 5/7 = 0,714286** e **y_A,β final = 5/13 = 0,384615**;
- transferência líquida de A de α para β: **0,120279047 mol**.

Os totais de A e de B são individualmente **0,400930158 mol**, antes e depois. Não se conserva a quantidade total de cada célula isoladamente, pois A cruza sua fronteira; conserva-se a de cada componente no conjunto α + β. Os valores finais n, p e y também satisfazem pV = nRT e p_A = y_Ap em cada célula. Comparações numéricas devem usar valores sem arredondamento intermediário.

A solução é estável em relação à única transferência material liberada: com ξ mol de A transferidos de α para β, n_A,α = n_A,α,inicial − ξ e n_A,β = n_A,β,inicial + ξ. Diferenciando dF/dξ = μ_A,β − μ_A,α com essas dependências, obtém-se d²F/dξ² = RT[1/n_A,α + 1/n_A,β] > 0 no domínio com ambas as quantidades positivas. Assim, o ponto de igualdade de μ_A é um mínimo em relação a essa coordenada permitida, não apenas um ponto estacionário arbitrário. A equação não prova estabilidade frente a processos que o modelo excluiu.

### 5. Por que as pressões finais podem diferir

O estado final é um **equilíbrio sob as restrições da membrana**, em relação às transferências permitidas. O suporte equilibra uma diferença de pressão de **60,0 kPa**; o resultado não representa um pistão livre. A inexistência de deslocamento do suporte não exige igualdade das pressões. A composição de B permanece desigual porque B não atravessa.

Se a passagem de B for liberada mantendo T e os volumes, seu potencial químico será maior em β, pois sua pressão parcial é 80 kPa contra 20 kPa em α. B passará inicialmente de β para α. No novo equilíbrio, cada espécie terá metade de sua quantidade total em cada célula: p_A = p_B = 50 kPa, p_total = 100 kPa e y_A = y_B = 0,500 em ambas. A alteração remove uma restrição; não invalida o equilíbrio anterior em relação à transferência de A. A igualdade de potenciais químicos se refere à espécie cuja troca foi liberada, conforme o tratamento de equilíbrio material nas [notas de H. S. Reall, seção 1.14](https://www.damtp.cam.ac.uk/user/hsr1000/stat_phys_lectures.pdf).

### 6. Suficiência de dados e parecer

| Caso | Classificação e motivo | Informação complementar |
|---|---|---|
| a | T e p são compatíveis, mas redundantes na curva de coexistência. Não determinam a fração mássica de vapor x. | x, ou uma propriedade global adequada, como v, com v_f e v_g conhecidos e a relação de mistura. A mera existência das duas fases só indica 0 < x < 1. |
| b | Incompatível com duas fases em equilíbrio na interface plana descrita: a 300 K o modelo exige 10 kPa, não 12 kPa. | Investigar qual declaração ou medida falhou. Não inventar um título para conciliar T e p incompatíveis. |
| c | Insuficiente para o estado intensivo completo de uma mistura de composição desconhecida. T e p não determinam y_A. | Uma composição independente, por exemplo y_A; então y_B = 1 − y_A. |
| d | T, p e y_A determinam o estado intensivo da mistura ideal não reativa sob as hipóteses dadas. Não determinam sua escala extensiva. | V ou n para determinar a quantidade total. Com V, n = pV/(RT). |

H-1 deve ser rejeitado como registro de equilíbrio global: há duas incompatibilidades demonstradas, térmica e mecânica. H-2 é compatível com os critérios examinados, incluindo gravidade e coexistência na interface; os dados não autorizam inventar quantidade de vapor ou propriedades totais do recipiente. D não está inicialmente em equilíbrio de transferência de A e alcança o estado calculado sob restrição. Nenhuma conclusão fornece tempo de relaxação, dimensionamento da membrana ou validação de um equipamento real.

Para uma bancada real, o parecer deve exigir identificação da substância e validade dos modelos de propriedade, calibração e posição dos sensores, incertezas e tolerâncias, verificação do contato térmico, ausência de correntes ou fontes ativas não modeladas, integridade e seletividade da membrana e evidência de estabilização. São dados necessários para confrontar o modelo com uma experiência; não são justificativas retroativas para aceitar H-1.

## Rubrica analítica — 10 pontos

Aplicar aos produtos observáveis. Créditos parciais exigem raciocínio escrito. Um erro aritmético isolado com modelo correto não elimina os pontos conceituais; erros de modelo não são compensados por resultados numéricos coincidentes.

| Critério | Pontos | Evidência para pontuação integral | Crédito parcial típico |
|---|---:|---|---|
| Fronteiras, trocas e restrições | 1,5 | Distingue coluna, interface, células e conjunto; explica rigidez, seletividade e reservatório térmico; não impõe critérios correspondentes a trocas proibidas. | 0,8: identifica sistemas, mas não relaciona uma restrição ao critério correspondente. 0: resolve D como pistão livre ou como células fechadas à passagem de A. |
| Diagnóstico térmico e de fases | 1,5 | Rejeita H-1 termicamente; separa compatibilidade local da interface de equilíbrio global; usa saturação na interface e reconhece falta de dados para o fundo a 302 K. | 0,8: rejeita T desigual, mas generaliza incorretamente a condição de saturação a todos os pontos. |
| Balanço mecânico | 1,5 | Deriva dp/dz = −ρg; calcula 29,620 kPa com base absoluta, sinal e dimensão; explica por que pressão uniforme seria incompatível. | 0,8: resultado correto, sem derivação ou com justificativa incompleta. 0: mantém p uniforme por “equilíbrio”. |
| Potencial químico e gravidade | 1,5 | Calcula +0,3924 J/mol para μ_fundo − μ_interface; mostra igualdade de μ̃; explicita convenção e não duplica gravidade. | 0,8: entende compensação mas erra um sinal ou unidade sem alterar a conclusão. 0: exige μ intrínseco uniforme sob a convenção dada. |
| Transferência seletiva e estado final | 2,5 | Calcula Δμ_A, sentido por dF, inventários, p, y e transferência; verifica conservação de A e B; justifica estabilidade na coordenada liberada e a alteração ao liberar B. | Até 1,5: modelo e sentido corretos, mas faltam verificação de conservação, estabilidade ou parte dos valores. Até 0,8: calcula Δμ, mas não fecha o estado final. |
| Suficiência de dados e comunicação | 1,5 | Classifica os quatro casos com objeto do estado e dado faltante; produz parecer com decisões e limites, sem alegar domínio integral do curso. | 0,8: acerta pelo menos três casos, mas não distingue estado intensivo de quantidade total ou omite limites experimentais. |

**Referência pedagógica proposta para domínio desta atividade:** pelo menos 8/10, sem os erros críticos abaixo, com os critérios “balanço mecânico”, “potencial químico e gravidade” e “transferência seletiva” cada um com ao menos 70% de seus pontos. Esse limiar é uma proposta de rubrica, ainda sem validação empírica; não substitui o gate do Auditor nem certifica nível avançado do curso.

**Erros críticos que exigem correção antes de considerar o objetivo atingido:**

- Afirmar que equilíbrio mecânico exige pressão uniforme mesmo com peso do líquido ou suporte da membrana.
- Usar p_sat como pressão de todos os pontos do líquido em H-2, ou afirmar duas fases locais no fundo apenas porque há vapor no topo.
- Declarar equilíbrio de D inicialmente só porque T e p_total são iguais, ou usar p_total no lugar de p_A para calcular a diferença de μ_A.
- Confundir igualdade de μ da mesma espécie entre regiões com igualdade de μ_A e μ_B entre espécies diferentes.
- Fazer B atravessar a membrana antes da retirada dessa restrição, ou conservar n de cada célula como se A não pudesse atravessá-la.
- Exigir igualdade de μ intrínseco entre alturas ignorando o termo gravitacional definido, ou contar Mgz duas vezes.
- Concluir que (T,p) na saturação determina x, ou que T e p determinam uma composição desconhecida.

## Fontes consultadas e versão dos dados

Consultas realizadas em **27/10/2026**. Os endereços a seguir foram abertos e seu conteúdo pertinente foi lido; não se usaram listas de resultados como validação científica. Nenhum número de propriedade da substância X foi atribuído a essas fontes.

| Fonte primária/universitária | Trecho utilizado | Limite de uso |
|---|---|---|
| [OpenStax / Rice University, University Physics, volume 1, §14.1](https://openstax.org/books/university-physics-volume-1/pages/14-1-fluids-density-and-pressure) | Balanço hidrostático e pressão com profundidade, densidade constante. | Não fornece dados para X nem valida membranas. |
| [MIT OCW, 3.020 Thermodynamics of Materials, primavera de 2021, aula 13](https://ocw.mit.edu/courses/3-020-thermodynamics-of-materials-spring-2021/mit3_020s21_l13.pdf) | Partes 2 e 6: pressão parcial e potencial químico da mistura ideal. | Aplicação apenas ao modelo ideal, sem reações nesta atividade. |
| [David Tong, University of Cambridge, Classical Thermodynamics, §4.4](https://www.damtp.cam.ac.uk/user/tong/statphys/statmechhtml/S4.html#S4.SS4) | F a T,V fixos; diferenciais de F e G; G = μN para substância pura. | A convenção da fonte por partícula é convertida aqui à base molar; a dedução com gravidade é apresentada integralmente no rascunho. |
| [David Tong, University of Cambridge, Phase Transitions, §5.1.1](https://www.damtp.cam.ac.uk/user/tong/statphys/statmechhtml/S5.html#S5.SS1.SSS1) | Condições locais de coexistência de fases. | Não se utiliza a equação de van der Waals nem seus parâmetros. |
| [H. S. Reall, University of Cambridge, Statistical Physics, 26/01/2018, §1.14](https://www.damtp.cam.ac.uk/user/hsr1000/stat_phys_lectures.pdf) | Equilíbrio material sob liberação de troca de partículas. | Mesma espécie; fronteiras e campos externos devem ser considerados antes da igualdade. |
| [MIT OCW, 2.43 Advanced Thermodynamics, primavera de 2024, aula 4](https://ocw.mit.edu/courses/2-43-advanced-thermodynamics-spring-2024/resources/ocw_243_lecture04_2024feb16_mp4/) | Ementa específica sobre condições de equilíbrio e diferença de pressão por curvatura. | Confirma a relevância de declarar interface plana e capilaridade desprezada; não se afirma ter revisado integralmente o vídeo. |

**Pacote de dados didáticos:** `FUN01-EQ-modelo-v1`, definido integralmente no enunciado desta versão. R = 8,314 foi deliberadamente arredondado e é o valor de reprodução esperado. Os números de X, geometria e composições são escolhidos para a atividade. Não há tabela externa de propriedades necessária, nem extrapolação de propriedades de água. A avaliação de substâncias reais e dados supercríticos deve ocorrer em outra atividade da unidade.

**Consistência local do modelo X:** uma representação que realiza as condições usadas na isoterma T₀ = 300 K é μ_l(T₀,p) = V̄_l(p − p_sat) e μ_v(T₀,p) = RT₀ ln(p/p_sat), escolhendo zero comum em p_sat. A primeira corresponde ao líquido incompressível; a segunda, a um vapor ideal. Ambas coincidem a 10 kPa. Entre 10 e 29,620 kPa, μ_l < μ_v, compatível com líquido estável. Essa construção é apenas um testemunho de consistência na faixa utilizada; não é uma equação de estado calorífica completa de X. Não autoriza obter capacidades térmicas, calor latente, curva de saturação em outras temperaturas ou tempo de relaxação. Em particular, a solução não calcula p_sat(302 K).

## Reprodução numérica mínima

Código JavaScript independente de bibliotecas, com as grandezas no SI. Os testes verificam os balanços e as duas relações de estado, não somente constantes finais digitadas.

```javascript
const R = 8.314, T = 300, V = 0.010, p0 = 100000;
const rho = 1000, g = 9.81, H = 2, M = 0.020, psat = 10000;
const n0 = p0 * V / (R * T);
const initial = {aA: 0.8*n0, bA: 0.2*n0, aB: 0.2*n0, bB: 0.8*n0};
const final = {
  aA: (initial.aA + initial.bA)/2,
  bA: (initial.aA + initial.bA)/2,
  aB: initial.aB,
  bB: initial.bB
};
const pa = (final.aA + final.aB)*R*T/V;
const pb = (final.bA + final.bB)*R*T/V;
const ya = final.aA/(final.aA + final.aB);
const yb = final.bA/(final.bA + final.bB);
const residuals = {
  A_mol: final.aA + final.bA - initial.aA - initial.bA,
  B_mol: final.aB + final.bB - initial.aB - initial.bB,
  equal_partial_A_Pa: ya*pa - yb*pb,
  a_equation_of_state_J: pa*V - (final.aA + final.aB)*R*T,
  b_equation_of_state_J: pb*V - (final.bA + final.bB)*R*T,
  column_total_potential_Jmol: (M/rho)*(rho*g*H) - M*g*H
};
const tolerances = {
  A_mol: 1e-12, B_mol: 1e-12, equal_partial_A_Pa: 1e-8,
  a_equation_of_state_J: 1e-10, b_equation_of_state_J: 1e-10,
  column_total_potential_Jmol: 1e-12
};
for (const [name, residual] of Object.entries(residuals)) {
  if (Math.abs(residual) > tolerances[name]) throw new Error(name);
}
console.log({
  pressure_bottom_Pa: psat + rho*g*H,
  intrinsic_mu_bottom_minus_interface_Jmol: M*g*H,
  initial_muA_alpha_minus_beta_Jmol: R*T*Math.log(4),
  transfer_A_mol: initial.aA - final.aA,
  final, pressure_alpha_Pa: pa, pressure_beta_Pa: pb,
  yA_alpha: ya, yA_beta: yb,
  curvature_F_J_per_mol2: R*T*(1/final.aA + 1/final.bA),
  residuals
});
```

**Conferência do apoio:** expressões recalculadas em JavaScript com precisão numérica de ponto flutuante; sinais e unidades conferidos por balanço de forças, conservação de espécies e redução de F; transferência de A = 0,12027904738994469 mol, Δμ_A inicial = 3457,695395505231 J/mol, pressão inferior = 29620 Pa, diferença intrínseca de μ = 0,3924 J/mol. A revisão independente pelo Auditor continua pendente. Este arquivo não altera produto, inventário ou controle de auditoria.
