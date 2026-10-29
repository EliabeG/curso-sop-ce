# FOR-01 r2 — revisão individual das 100 fichas

Data: 28/10/2026. Entrega para auditoria independente; sem aprovação própria.

Nesta rodada, quatro fichas (23/46/79/84) e três trechos de aula receberam somente a correção R1-A. As outras 96 fichas e os 191 elementos MathML das 100 fichas permanecem idênticos à r1, assim como JS/CSS, 197 artigos e seus registros. A contagem “100 expressões” da documentação r1 foi imprecisa; a versão histórica não foi reescrita.

Autoria: Corretor (01–50), apoio_fun01 (51–100 e revisão textual das primeiras notas), integração/revisão final pelo Corretor; apoio documental e navegador do coordenador identificados em arquivos próprios. O diagnóstico abaixo descreve a leitura da base; o resultado registra o que ficou publicado. Fontes completas e hashes por ficha em [revisao-100-r2.json](revisao-100-r2.json).

## 01 — Variação e valor final

ID: `formula-variacao`. Decisão: ficha_mantida.

**Expressão:** A definição ΔX = X₂ − X₁ e o rearranjo X₂ = X₁ + ΔX estão corretos.

**Símbolos e unidades:** ΔX tem a mesma unidade de X; os índices identificam os estados inicial e final.

**Hipóteses:** É uma definição de variação, sem hipótese adicional sobre o processo.

**Ensino vinculado:** A aula define ΔX, exemplifica seu sinal e distingue variação de valor final.

**Resultado:** Mantida após conferência individual da expressão, símbolos/unidades, hipóteses e ensino vinculado. Condição publicada: Δ indica final menos inicial.

**Vínculos finais:** [base-leitura-matematica](../../../../modulos/e1-termodinamica.html#base-leitura-matematica). Fontes: `algebra`.

## 02 — Energia, potência e duração

ID: `formula-taxas`. Decisão: ficha_mantida.

**Expressão:** Q/Δt e W/Δt representam taxas médias; multiplicar a taxa média pela duração recupera a energia transferida.

**Símbolos e unidades:** A equivalência kJ/s = kW e o intervalo de tempo em segundos estão definidos.

**Hipóteses:** A condição distingue taxa média de taxa constante. A expressão não deve ser interpretada como definição de taxa instantânea.

**Ensino vinculado:** A aula apresenta o caso de um aquecedor de potência constante e a conversão entre potência e energia.

**Resultado:** Mantida após conferência individual da expressão, símbolos/unidades, hipóteses e ensino vinculado. Condição publicada: Taxas médias no intervalo; a última expressão vale para taxa constante.

**Vínculos finais:** [base-leitura-matematica](../../../../modulos/e1-termodinamica.html#base-leitura-matematica). Fontes: `algebra`, `si`.

## 03 — Conversões e produtos de unidades

ID: `formula-conversoes`. Decisão: ficha_corrigida.

**Expressão:** Os fatores de conversão entre múltiplos de mil, unidades cúbicas, litros e calorias termoquímicas estão corretos. O valor 4,184 corresponde à caloria termoquímica.

**Símbolos e unidades:** J, kJ, W, kW, Pa, kPa, L, mm e cm³ usam conversões compatíveis.

**Hipóteses:** Preservar a aproximação explicitamente fornecida no enunciado, quando houver.

**Ensino vinculado:** O alvo atual ensina o SI e os produtos de unidades. A alteração prevista acrescenta #base-balanco-fechado, que trata de cal e kcal, com o texto “Conferir calorias e sinais”.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Use a aproximação de J/cal fornecida na questão, se houver.

**Vínculos finais:** [base-leitura-matematica](../../../../modulos/e1-termodinamica.html#base-leitura-matematica); [base-balanco-fechado](../../../../modulos/e1-termodinamica.html#base-balanco-fechado). Fontes: `si`, `nist_cal`.

## 04 — Temperatura absoluta e intervalos

ID: `formula-temperatura`. Decisão: ficha_mantida.

**Expressão:** O deslocamento de 273,15 entre as escalas e a igualdade numérica dos intervalos em Celsius e kelvin estão corretos.

**Símbolos e unidades:** T e t distinguem temperatura absoluta e temperatura em graus Celsius.

**Hipóteses:** A necessidade de usar temperaturas absolutas em razões está explicitada.

**Ensino vinculado:** A aula explica a lei zero, a conversão de escalas e o exemplo de 10 °C = 283,15 K.

**Resultado:** Mantida após conferência individual da expressão, símbolos/unidades, hipóteses e ensino vinculado. Condição publicada: Razões de temperaturas em gás ideal, Carnot, entropia e radiação usam K.

**Vínculos finais:** [base-absolutas](../../../../modulos/e1-termodinamica.html#base-absolutas). Fontes: `si`.

## 05 — Pressão absoluta e manométrica

ID: `formula-pressao`. Decisão: ficha_corrigida.

**Expressão:** p_abs = p_man + p_atm e p = F_normal/A estão corretos nas condições indicadas.

**Símbolos e unidades:** N/m² = Pa; usar kPa exige a conversão correspondente. A pressão é uniforme ou representa uma média sobre a área.

**Hipóteses:** As pressões somadas devem estar na mesma unidade; a força considerada é normal à superfície.

**Ensino vinculado:** #base-absolutas ensina a referência de pressão. A alteração prevista acrescenta #base-leitura-matematica para p = F/A, com o texto “Retomar força por área”.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Todas as pressões na mesma unidade; F⊥/A representa pressão uniforme ou média.

**Vínculos finais:** [base-absolutas](../../../../modulos/e1-termodinamica.html#base-absolutas); [base-leitura-matematica](../../../../modulos/e1-termodinamica.html#base-leitura-matematica). Fontes: `algebra`, `si`.

## 06 — Densidade e volume específico

ID: `formula-densidade`. Decisão: ficha_mantida.

**Expressão:** ρ = m/V e v = V/m = 1/ρ estão corretos.

**Símbolos e unidades:** As unidades kg/m³ e m³/kg estão explicitadas.

**Hipóteses:** As razões se referem à mesma amostra e ao mesmo estado; a interpretação de um sistema homogêneo é ensinada.

**Ensino vinculado:** A aula divide uma amostra e verifica que sua densidade permanece a mesma.

**Resultado:** Mantida após conferência individual da expressão, símbolos/unidades, hipóteses e ensino vinculado. Condição publicada: Use massa e volume da mesma amostra e do mesmo estado.

**Vínculos finais:** [base-medidas](../../../../modulos/e1-termodinamica.html#base-medidas). Fontes: `algebra`, `si`.

## 07 — Propriedades por unidade de massa

ID: `formula-especificas`. Decisão: ficha_corrigida.

**Expressão:** u = U/m, h = H/m e s = S/m dividem corretamente cada propriedade total pela massa.

**Símbolos e unidades:** U e H são energias totais; S é entropia total. Com m em kg, u e h ficam em kJ/kg e s em kJ/(kg·K).

**Hipóteses:** A condição prevista deve ser lida apenas para estas relações: U, H e S são totais; u, h e s são por unidade de massa. Não é uma regra universal de letras maiúsculas e minúsculas e não exige gás ideal.

**Ensino vinculado:** A aula ensina a divisão de uma propriedade extensiva pela massa. Essa explicação também cobre s, mesmo sem uma linha separada para a entropia.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Nestas relações, U, H e S são totais; u, h e s são por unidade de massa.

**Vínculos finais:** [base-propriedades](../../../../modulos/e1-termodinamica.html#base-propriedades). Fontes: `firstlaw`, `algebra`.

## 08 — Faixa do instrumento

ID: `formula-span`. Decisão: ficha_mantida.

**Expressão:** Span = L_sup − L_inf e seu rearranjo estão corretos.

**Símbolos e unidades:** O intervalo e os limites usam a mesma unidade; os limites são identificados.

**Hipóteses:** O span é distinguido do limite superior da faixa.

**Ensino vinculado:** A aula define o span e usa o exemplo L_sup = −10 °C + 120 °C = 110 °C.

**Resultado:** Mantida após conferência individual da expressão, símbolos/unidades, hipóteses e ensino vinculado. Condição publicada: Span é a diferença entre os limites.

**Vínculos finais:** [base-instrumentos](../../../../modulos/e1-termodinamica.html#base-instrumentos). Fontes: `algebra`.

## 09 — Duas escalas lineares

ID: `formula-escalas`. Decisão: ficha_corrigida.

**Expressão:** A interpolação afim e o ganho b = (X₂ − X₁)/(Y₂ − Y₁) estão corretos quando os denominadores são não nulos.

**Símbolos e unidades:** A alteração prevista define a como deslocamento, na unidade de X, e b como ganho, na unidade de X por unidade de Y; 1 e 2 são pontos de calibração.

**Hipóteses:** A forma fracionária exige X₂ ≠ X₁ e Y₂ ≠ Y₁. A resposta é linear; proporcionalidade direta exige a = 0. As origens das escalas não precisam coincidir.

**Ensino vinculado:** A aula deriva ganho e deslocamento e apresenta um exemplo. O vínculo deve ser mantido.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Resposta linear; X₂ ≠ X₁ e Y₂ ≠ Y₁ para as razões. Proporcionalidade direta exige a = 0.

**Vínculos finais:** [base-instrumentos](../../../../modulos/e1-termodinamica.html#base-instrumentos). Fontes: `algebra`.

## 10 — Razão, aumento e redução percentual

ID: `formula-percentual`. Decisão: ficha_mantida.

**Expressão:** As expressões calculam aumento e redução em relação ao valor de referência, respeitando a orientação dos sinais.

**Símbolos e unidades:** As razões são adimensionais e sua apresentação em porcentagem está explicitada.

**Hipóteses:** A exigência de X₁ inicial positivo evita denominador nulo e uma referência inadequada para a interpretação percentual proposta.

**Ensino vinculado:** A aula distingue valor final igual a 140% do inicial de aumento de 40%, além de apresentar a redução percentual.

**Resultado:** Mantida após conferência individual da expressão, símbolos/unidades, hipóteses e ensino vinculado. Condição publicada: A referência do percentual é o valor inicial.

**Vínculos finais:** [base-leitura-matematica](../../../../modulos/e1-termodinamica.html#base-leitura-matematica). Fontes: `algebra`.

## 11 — Concentração em ppm e geração total

ID: `formula-ppm-geracao`. Decisão: ficha_corrigida.

**Expressão:** A conversão C = C_ppm × 10⁻⁶ e o produto para somar a geração de fontes iguais estão corretos.

**Símbolos e unidades:** A alteração prevista define C como fração volumétrica, G como taxa volumétrica total de geração de CO₂, N como número de pessoas e a geração individual em unidade de vazão por pessoa.

**Hipóteses:** As vazões volumétricas devem usar as mesmas condições de referência. O produto N vezes a geração por pessoa pressupõe que todas as pessoas tenham a geração individual adotada.

**Ensino vinculado:** #base-balanco-co2 ensina a geração total, as unidades e o exemplo com 16 pessoas. Os valores do exercício não são apresentados como limites normativos.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Geração conhecida; some fontes e use vazões de gás nas mesmas condições de referência.

**Vínculos finais:** [base-balanco-co2](../../../../modulos/e1-termodinamica.html#base-balanco-co2). Fontes: `coord_co2`.

## 12 — Quantidade de matéria e constante do gás

ID: `formula-mols`. Decisão: ficha_mantida.

**Expressão:** n = m/M, R = Rᵤ/M e os valores aproximados de Rᵤ estão corretos. O número de Avogadro apresentado é exato.

**Símbolos e unidades:** M em kg/mol é compatível com m em kg e n em mol. R usa energia por kg e por kelvin; Rᵤ usa energia por mol e por kelvin.

**Hipóteses:** A compatibilidade entre as bases mássica e molar está explicitada.

**Ensino vinculado:** A aula explica o mol, a conversão entre as constantes por massa e por mol e um cálculo em atm·L.

**Resultado:** Mantida após conferência individual da expressão, símbolos/unidades, hipóteses e ensino vinculado. Condição publicada: Unidades de massa e de quantidade de matéria devem ser coerentes.

**Vínculos finais:** [base-gas-modelo](../../../../modulos/e1-termodinamica.html#base-gas-modelo). Fontes: `si`, `ideal`.

## 13 — Equação de estado do gás ideal

ID: `formula-gas-ideal`. Decisão: ficha_corrigida.

**Expressão:** pV = mRT = nRᵤT e pv = RT estão corretos para o modelo indicado.

**Símbolos e unidades:** A alteração prevista completa m em kg, V em m³, v em m³/kg, n em mol e T em K. R e Rᵤ usam J ou kJ por sua respectiva base, de modo compatível com pV em Pa·m³ ou kPa·m³.

**Hipóteses:** O modelo de gás ideal e o uso de pressão e temperatura absolutas já estão declarados; a composição determina a constante específica R.

**Ensino vinculado:** #base-gas-modelo deriva as bases mássica e molar; #base-gas-energia também explicita as unidades.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Modelo ideal; Pa·m³ → J ou kPa·m³ → kJ, com R compatível.

**Vínculos finais:** [base-gas-modelo](../../../../modulos/e1-termodinamica.html#base-gas-modelo). Fontes: `ideal`.

## 14 — Gás ideal em dois estados

ID: `formula-dois-estados`. Decisão: ficha_corrigida.

**Expressão:** A relação combinada entre estados e o produto das razões de pressão e volume estão corretos.

**Símbolos e unidades:** A alteração prevista exige a mesma unidade entre p₁ e p₂ e entre V₁ e V₂. As temperaturas permanecem em kelvin.

**Hipóteses:** A mesma quantidade de gás ideal e a mesma composição devem ser mantidas nos dois estados.

**Ensino vinculado:** A aula apresenta a derivação da relação e um exemplo de aumento percentual composto.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Mesma quantidade e composição de gás ideal; use a mesma unidade de pressão nos dois estados e a mesma unidade de volume.

**Vínculos finais:** [base-gas-modelo](../../../../modulos/e1-termodinamica.html#base-gas-modelo). Fontes: `ideal`, `algebra`.

## 15 — Restrições dos processos de gás ideal

ID: `formula-restricoes`. Decisão: ficha_corrigida.

**Expressão:** As três reduções da equação de estado estão corretas para as restrições indicadas.

**Símbolos e unidades:** A alteração prevista identifica cte como constante, p como pressão absoluta em Pa ou kPa, V em m³ e T em K, mantendo as unidades entre estados.

**Hipóteses:** Além da quantidade de gás, a composição deve permanecer fixa. Impõe-se apenas a restrição declarada para cada relação.

**Ensino vinculado:** A aula exige quantidade e composição fixas e explica por que reação ou vazamento podem invalidar a relação simplificada.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Gás ideal com quantidade e composição fixas; imponha somente a restrição declarada.

**Vínculos finais:** [base-gas-modelo](../../../../modulos/e1-termodinamica.html#base-gas-modelo). Fontes: `ideal`.

## 16 — Fator de compressibilidade

ID: `formula-compressibilidade`. Decisão: ficha_corrigida.

**Expressão:** Z = pV/(nRᵤT) = pv/(RT) e Z = 1 no modelo ideal estão corretos.

**Símbolos e unidades:** A alteração prevista substitui a remissão genérica por símbolos locais: Z adimensional, pressão absoluta, volumes total e específico, quantidade de matéria, temperatura e constantes em bases compatíveis.

**Hipóteses:** Z pode ser calculado para um gás real. Encontrar Z = 1 em um estado não comprova, sozinho, toda a idealidade das propriedades energéticas.

**Ensino vinculado:** A aula calcula Z = 0,80 e interpreta o desvio em relação à equação de estado ideal.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Z mede o desvio da equação de estado ideal.

**Vínculos finais:** [base-gas-modelo](../../../../modulos/e1-termodinamica.html#base-gas-modelo). Fontes: `ideal`, `algebra`.

## 17 — Relações entre calores específicos

ID: `formula-calores-especificos`. Decisão: ficha_mantida.

**Expressão:** cp − cv = R para gás ideal e k = cp/cv estão corretos.

**Símbolos e unidades:** Os calores específicos e R usam a mesma base, J/(kg·K) ou kJ/(kg·K); k é adimensional.

**Hipóteses:** A restrição da diferença cp − cv ao gás ideal e a comparação na mesma temperatura estão explicitadas.

**Ensino vinculado:** A aula apresenta as relações e o uso de k nas relações isentrópicas.

**Resultado:** Mantida após conferência individual da expressão, símbolos/unidades, hipóteses e ensino vinculado. Condição publicada: Relação de diferença: gás ideal; cp e cv avaliados na mesma temperatura.

**Vínculos finais:** [base-gas-energia](../../../../modulos/e1-termodinamica.html#base-gas-energia). Fontes: `ideal_energy`.

## 18 — Variações de energia do gás ideal

ID: `formula-energia-gas`. Decisão: ficha_corrigida.

**Expressão:** Δu = cvΔT, Δh = cpΔT e ΔU = mcvΔT estão corretos no modelo indicado.

**Símbolos e unidades:** As grandezas totais e específicas estão distinguidas; o intervalo de temperatura está identificado.

**Hipóteses:** A alteração prevista explicita massa fixa para a expressão de ΔU. Gás ideal, composição fixa e calores específicos constantes na faixa já delimitam o restante do modelo.

**Ensino vinculado:** A aula separa a dependência de u e h com a temperatura da aproximação de calor específico constante; o balanço fechado mostra o fator massa.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Gás ideal de composição fixa e calores específicos constantes na faixa; a relação para ΔU pressupõe massa fixa.

**Vínculos finais:** [base-gas-energia](../../../../modulos/e1-termodinamica.html#base-gas-energia). Fontes: `ideal_energy`.

## 19 — Energia cinética translacional média

ID: `formula-cinetica-molecular`. Decisão: ficha_mantida.

**Expressão:** A energia cinética translacional média de (3/2)kBT está correta no modelo cinético clássico de gás ideal.

**Símbolos e unidades:** O resultado é energia por molécula em J; kB tem unidade J/K e T é dada em K.

**Hipóteses:** A ficha não confunde a contribuição translacional com toda a energia interna molecular; esse limite está explícito.

**Ensino vinculado:** A aula discute rotação, vibração, colisões elásticas e valores médios, sem afirmar que todas as moléculas têm a mesma velocidade.

**Resultado:** Mantida após conferência individual da expressão, símbolos/unidades, hipóteses e ensino vinculado. Condição publicada: Modelo cinético ideal elementar; não é toda a energia interna de qualquer gás molecular.

**Vínculos finais:** [base-molecular](../../../../modulos/e1-termodinamica.html#base-molecular). Fontes: `kinetic`.

## 20 — Energia com calor específico variável

ID: `formula-energia-c-variavel`. Decisão: ficha_mantida.

**Expressão:** As integrais de cv(T) e cp(T), de T₁ a T₂, estão corretas.

**Símbolos e unidades:** Calores específicos em kJ/(kg·K) e temperatura em K produzem variações de energia específica em kJ/kg.

**Hipóteses:** Gás ideal e composição fixa estão explícitos; as relações não são estendidas automaticamente a gases reais.

**Ensino vinculado:** A aula integra uma expressão linear de cp, obtém 196 kJ/kg e compara aproximações.

**Resultado:** Mantida após conferência individual da expressão, símbolos/unidades, hipóteses e ensino vinculado. Condição publicada: Gás ideal; propriedades de tabela ou integração substituem a aproximação de c constante.

**Vínculos finais:** [base-calor-variavel](../../../../modulos/e1-termodinamica.html#base-calor-variavel). Fontes: `ideal_energy`.

## 21 — Título da mistura saturada

ID: `formula-titulo`. Decisão: ficha_corrigida.

**Expressão:** x = mg/(mf + mg), com 0 ≤ x ≤ 1, define corretamente a fração mássica de vapor.

**Símbolos e unidades:** x é adimensional; as massas devem usar a mesma unidade.

**Hipóteses:** A alteração prevista delimita substância pura em equilíbrio líquido–vapor abaixo do ponto crítico. x = 0 e x = 1 representam os limites saturados.

**Ensino vinculado:** A seção #substancias ensina a fração mássica e a coexistência em equilíbrio; FUN-01 distingue mistura bifásica e estado supercrítico.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Substância pura em equilíbrio líquido–vapor, abaixo do ponto crítico; x = 0 e x = 1 são os limites saturados. Título é fração mássica.

**Vínculos finais:** [substancias](../../../../modulos/e1-termodinamica.html#substancias). Fontes: `quality`.

## 22 — Propriedade da mistura saturada

ID: `formula-mistura`. Decisão: ficha_corrigida.

**Expressão:** A média ponderada pelas massas e sua inversão para obter x estão corretas.

**Símbolos e unidades:** A alteração prevista especifica v em m³/kg, u e h em kJ/kg, s em kJ/(kg·K), além de x adimensional e dos índices f e g.

**Hipóteses:** A substância deve ser pura, em equilíbrio líquido–vapor, com f e g na mesma condição de saturação. A inversão exige yg ≠ yf e exclui o ponto crítico.

**Ensino vinculado:** A seção explica propriedades específicas e traz um exemplo com entalpia. A regra não deve ser usada para interpolar temperatura ou pressão pelo título.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Substância pura em equilíbrio líquido–vapor; f e g na mesma saturação. A inversão exige yg ≠ yf, excluindo o ponto crítico.

**Vínculos finais:** [substancias](../../../../modulos/e1-termodinamica.html#substancias). Fontes: `quality`, `algebra`.

## 23 — Calor latente de vaporização

ID: `formula-latente`. Decisão: ficha_corrigida.

**Expressão:** hfg = hg − hf está correto. As expressões de calor e taxa de calor exigem os modelos reduzidos explicitados nas alterações.

**Símbolos e unidades:** A alteração prevista identifica as entalpias específicas em kJ/kg, a massa vaporizada em kg, Q em kJ, Q̇ em kW e ṁ em kg/s. hf e hg correspondem aos estados saturados de líquido e vapor.

**Hipóteses:** A parte fechada já limita o trabalho a pV. A redução de escoamento exige excluir todo trabalho não associado ao escoamento, recebido ou fornecido, inclusive elétrico; a r1 excluía somente eixo, condição insuficiente.

**Ensino vinculado:** #base-calor-latente agora declara a exclusão completa e demonstra por que um vaporizador adiabático com resistor interno deve usar Q̇−Ẇnão-fluxo=ṁhfg. O termo pv permanece em h.

**Resultado:** R1-A corrigido: exclusão de todo trabalho não associado ao escoamento, recebido ou fornecido, inclusive elétrico; condições e data-busca sincronizadas. Condição publicada: Vaporização completa de substância pura, de líquido a vapor saturados, a pressão fixa. Para Q: massa fechada, só trabalho pV. Para Q̇: escoamento permanente sem qualquer trabalho não associado ao escoamento, recebido ou fornecido, inclusive elétrico; pv já integra h. Despreze variações cinética e potencial.

**Vínculos finais:** [base-calor-latente](../../../../modulos/e1-termodinamica.html#base-calor-latente). Fontes: `firstlaw`, `mit_cv`, `phase`.

## 24 — Interpolação linear em tabela

ID: `formula-interpolacao`. Decisão: ficha_corrigida.

**Expressão:** A interpolação linear local está correta.

**Símbolos e unidades:** A propriedade mantém sua unidade e as três temperaturas usam a mesma escala.

**Hipóteses:** A alteração prevista exige Ta ≠ Tb e T entre os dois valores conhecidos. A pressão e a região de fase permanecem as mesmas, sem atravessar uma transição de fase.

**Ensino vinculado:** O alvo amplo contém a fórmula e o exemplo de 230 °C, que resulta em 2.860 kJ/kg. A orientação sobre não atravessar uma mudança de fase está presente.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Mesma pressão e região de fase; Ta ≠ Tb e T entre os dois valores. Aproximação local, sem atravessar transição de fase.

**Vínculos finais:** [aprofundamento-aplicado](../../../../modulos/e1-termodinamica.html#aprofundamento-aplicado). Fontes: `algebra`.

## 25 — Umidade relativa

ID: `formula-umidade`. Decisão: ficha_corrigida.

**Expressão:** φ = pv/psat e a razão entre umidades à mesma temperatura são válidas na aproximação de ar úmido ideal adotada; não devem ser apresentadas como definição geral de uma mistura real.

**Símbolos e unidades:** A alteração prevista define φ como fração, pv como pressão parcial do vapor e psat(T) como pressão de saturação da água pura sobre a fase de referência escolhida. As pressões usam a mesma unidade.

**Hipóteses:** Explicitar a aproximação ideal e o desprezo do fator de intensificação. A razão final exige a mesma temperatura e pv₁ ≠ 0, equivalentemente φ₁ ≠ 0.

**Ensino vinculado:** #base-umidade apresenta a razão como definição e deve receber a mesma delimitação. Esse ajuste não exige implementar psicrometria de misturas reais.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Aproximação de ar úmido ideal, desprezando o fator de intensificação. A razão final exige mesma temperatura e pv1 ≠ 0 (φ1 ≠ 0).

**Vínculos finais:** [base-umidade](../../../../modulos/e1-termodinamica.html#base-umidade). Fontes: `humidity`.

## 26 — Capacidade térmica e calor sensível

ID: `formula-capacidade-termica`. Decisão: ficha_mantida.

**Expressão:** C = mc e Qsens = mcΔT estão corretos no modelo de calor sensível delimitado.

**Símbolos e unidades:** Capacidade térmica total em J/K, calor específico em J/(kg·K) e massa em kg estão distinguidos.

**Hipóteses:** Uma única fase, calor específico constante, sólidos ou líquidos e efeitos de trabalho e pressão desprezíveis já estão explicitados.

**Ensino vinculado:** A aula delimita o modelo e calcula 252 kJ e 157,5 s sem confundir energia com potência.

**Resultado:** Mantida após conferência individual da expressão, símbolos/unidades, hipóteses e ensino vinculado. Condição publicada: Sólidos/líquidos em uma fase; c constante, trabalho e efeitos de pressão desprezíveis.

**Vínculos finais:** [base-calorimetria](../../../../modulos/e1-termodinamica.html#base-calorimetria). Fontes: `calorimetry`.

## 27 — Balanço da mistura e temperatura final

ID: `formula-equilibrio-mistura`. Decisão: ficha_corrigida.

**Expressão:** O balanço ΣCi(Tf − Ti) = 0 e a temperatura final como média ponderada estão corretos.

**Símbolos e unidades:** Ci = mici tem unidade J/K; as temperaturas usam a mesma escala e as capacidades são positivas.

**Hipóteses:** A alteração prevista explicita conjunto isolado, capacidades constantes, ausência de trabalho relevante, reação e mudança de fase, além de energia de mistura e variações cinética e potencial desprezíveis. Excluir apenas reação não elimina a energia de mistura.

**Ensino vinculado:** A aula apresenta Tf = 50 °C e já ressalva a entalpia de mistura ao final. O vínculo deve ser mantido.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Conjunto isolado; capacidades constantes; sem trabalho relevante, reação ou mudança de fase. Despreze energia de mistura e variações cinética/potencial.

**Vínculos finais:** [base-mistura-termica](../../../../modulos/e1-termodinamica.html#base-mistura-termica). Fontes: `calorimetry`, `firstlaw`.

## 28 — Recipiente e energia externa na mistura

ID: `formula-recipiente-mistura`. Decisão: ficha_corrigida.

**Expressão:** A contribuição do recipiente deve ser somada uma única vez. Eext = Qext − Wext está correto na convenção adotada.

**Símbolos e unidades:** A alteração prevista define Ci e Crec em J/K, as temperaturas iniciais de cada porção e do recipiente, a temperatura final e Eext em J. Calor entrando e trabalho saindo são positivos.

**Hipóteses:** Usar capacidades constantes, sem reação ou mudança de fase, e desprezar energia de mistura e variações cinética e potencial. Incluir as trocas externas com seus sinais.

**Ensino vinculado:** A aula calcula 44 °C incluindo o recipiente e explica como tratar perdas, agitador e entalpia de mistura.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Capacidades constantes; sem reação ou mudança de fase; energia de mistura e variações cinética/potencial desprezíveis. Inclua o recipiente uma vez e as trocas externas com sinal.

**Vínculos finais:** [base-mistura-termica](../../../../modulos/e1-termodinamica.html#base-mistura-termica). Fontes: `calorimetry`, `firstlaw`.

## 29 — Energia para transformar uma fase

ID: `formula-fase-calorimetria`. Decisão: ficha_corrigida.

**Expressão:** |Qfase| = mℓ está correto para o calor da mudança de fase nas condições indicadas; não representa qualquer variação de energia interna.

**Símbolos e unidades:** m é a massa efetivamente transformada; ℓ é o calor latente específico positivo, em J/kg ou kJ/kg. |Qfase| é a magnitude do calor na unidade correspondente.

**Hipóteses:** A alteração prevista delimita pressão fixa, apenas trabalho de fronteira e variações cinética e potencial desprezíveis. Fusão e vaporização recebem calor; os processos inversos o liberam.

**Ensino vinculado:** A aula fixa a pressão, separa as etapas e exemplifica fusão parcial. A condição local deve impedir que Q seja interpretado como uma energia genérica.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Mudança de fase a pressão fixa, só trabalho de fronteira e variações cinética/potencial desprezíveis; fusão/vaporização recebem calor, suas inversas o liberam.

**Vínculos finais:** [base-fase-calorimetria](../../../../modulos/e1-termodinamica.html#base-fase-calorimetria). Fontes: `phase`, `firstlaw`.

## 30 — Energia cinética e potencial

ID: `formula-energia-mecanica`. Decisão: ficha_corrigida.

**Expressão:** ΔEc = m(vel₂² − vel₁²)/2 e ΔEp = mg(z₂ − z₁) estão corretos para o movimento macroscópico de translação considerado.

**Símbolos e unidades:** Massa em kg, velocidade em m/s, g em m/s² e altura em m produzem energia em J; converter antes de somar a termos em kJ.

**Hipóteses:** A alteração prevista explicita massa fixa, translação não relativística e g aproximadamente constante na diferença de altura. As alturas usam a mesma referência e a velocidade descreve o movimento macroscópico do conjunto.

**Ensino vinculado:** #base-primeira-lei nomeia Ec e Ep, mas não apresenta essas expressões. O alvo precisa de uma recapitulação delimitada ou de vínculo para um trecho existente que as ensine.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Massa fixa, movimento de translação não relativístico; g aproximadamente constante na diferença de altura.

**Vínculos finais:** [base-primeira-lei](../../../../modulos/e1-termodinamica.html#base-primeira-lei). Fontes: `mechanics_k`, `mechanics_p`.

## 31 — Primeira lei: sistema fechado

ID: `formula-balanco-fechado`. Decisão: ficha_mantida.

**Expressão:** O balanço total de energia de um sistema fechado está correto e preserva as variações de energia cinética e potencial.

**Símbolos e unidades:** Todos os termos devem usar a mesma unidade de energia.

**Hipóteses:** A convenção de calor entrando e trabalho saindo positivos está explícita; trabalho recebido pelo sistema tem sinal negativo.

**Ensino vinculado:** A aula distingue o balanço total de sua redução ΔU = Q − W, atendendo ao cuidado central do critério P0.

**Resultado:** Mantida após conferência individual da expressão, símbolos/unidades, hipóteses e ensino vinculado. Condição publicada: Q entra positivo; W sai positivo. Trabalho recebido tem W negativo.

**Vínculos finais:** [base-primeira-lei](../../../../modulos/e1-termodinamica.html#base-primeira-lei). Fontes: `firstlaw`.

## 32 — Energia interna e valor final

ID: `formula-u-final`. Decisão: ficha_mantida.

**Expressão:** ΔU = Q − W e U₂ = U₁ + Q − W são coerentes nas condições indicadas.

**Símbolos e unidades:** Estados e transferências usam J ou kJ. A variação de energia não deve ser confundida com a energia final.

**Hipóteses:** Sistema fechado e variações de energia cinética e potencial desprezíveis estão explicitados.

**Ensino vinculado:** A aula apresenta o caso do agitador e o cálculo da energia final, com conversões de unidades.

**Resultado:** Mantida após conferência individual da expressão, símbolos/unidades, hipóteses e ensino vinculado. Condição publicada: Sistema fechado; ΔEC e ΔEP desprezíveis; convenção Q entra, W sai.

**Vínculos finais:** [base-balanco-fechado](../../../../modulos/e1-termodinamica.html#base-balanco-fechado). Fontes: `firstlaw`.

## 33 — Sistema fechado adiabático

ID: `formula-adiabatico`. Decisão: ficha_corrigida.

**Expressão:** Q = 0 e ΔU = −W estão corretos para a redução indicada do balanço fechado.

**Símbolos e unidades:** A alteração prevista define Q como calor recebido, ΔU como variação da energia interna e W como trabalho realizado pelo sistema, todos na mesma unidade, J ou kJ.

**Hipóteses:** A ficha deve explicitar sistema fechado e ΔEc e ΔEp desprezíveis. Ser adiabático não significa que W seja nulo.

**Ensino vinculado:** A alteração prevista acrescenta #base-balanco-fechado, com o texto “Retomar casos do balanço fechado”, para apoiar as condições da redução.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Sistema fechado; ΔEC e ΔEP desprezíveis; adiabático não significa W = 0.

**Vínculos finais:** [base-primeira-lei](../../../../modulos/e1-termodinamica.html#base-primeira-lei); [base-balanco-fechado](../../../../modulos/e1-termodinamica.html#base-balanco-fechado). Fontes: `firstlaw`.

## 34 — Trabalho de fronteira

ID: `formula-fronteira`. Decisão: ficha_corrigida.

**Expressão:** A integral de p dV está correta para o trabalho de fronteira na trajetória quase estática indicada.

**Símbolos e unidades:** A alteração prevista define W como trabalho de fronteira em kJ, p como pressão absoluta na fronteira em kPa e V em m³.

**Hipóteses:** A pressão deve corresponder à fronteira no modelo adotado. Expansão dá trabalho positivo e compressão, negativo; a expressão não representa todos os modos de trabalho.

**Ensino vinculado:** A aula ensina a integral, a área no diagrama e a convenção de sinais. FUN-02 aprofunda o assunto sem precisar ser alterado neste ajuste.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Processo quase estático, com pressão na fronteira representada por p.

**Vínculos finais:** [base-trabalho-fronteira](../../../../modulos/e1-termodinamica.html#base-trabalho-fronteira). Fontes: `firstlaw`.

## 35 — Trabalho a pressão constante

ID: `formula-isobarico`. Decisão: ficha_corrigida.

**Expressão:** W = p(V₂ − V₁) está correto quando a pressão de fronteira permanece constante.

**Símbolos e unidades:** A alteração prevista define p como pressão absoluta constante em kPa, V em m³ e W como trabalho de fronteira em kJ.

**Hipóteses:** A trajetória quase estática e isobárica está explicitada; a pressão usada é a pressão absoluta na fronteira.

**Ensino vinculado:** A aula integra a pressão constante e contrasta esse caso com a transformação isotérmica.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Processo quase estático isobárico; não confunda redução de volume com ΔV positivo.

**Vínculos finais:** [base-trabalho-fronteira](../../../../modulos/e1-termodinamica.html#base-trabalho-fronteira). Fontes: `firstlaw`, `algebra`.

## 36 — Trabalho isotérmico do gás ideal

ID: `formula-isotermico`. Decisão: ficha_corrigida.

**Expressão:** W = mRT ln(V₂/V₁) e ΔU = 0 estão corretos para o gás ideal em transformação isotérmica. Concluir Q = W também exige que W represente o único modo de trabalho considerado no balanço reduzido.

**Símbolos e unidades:** R em kJ/(kg·K), m em kg e T em K produzem trabalho em kJ; V₂/V₁ é adimensional.

**Hipóteses:** A alteração prevista explicita massa e composição fixas, transformação isotérmica reversível, apenas trabalho de fronteira e variações cinética e potencial desprezíveis.

**Ensino vinculado:** A aula ensina a expressão. O trecho de balanço fechado declara a hipótese de apenas trabalho de fronteira para os processos apresentados.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Gás ideal de massa e composição fixas, transformação isotérmica reversível, só trabalho de fronteira; ΔEC/ΔEP desprezíveis.

**Vínculos finais:** [base-trabalho-fronteira](../../../../modulos/e1-termodinamica.html#base-trabalho-fronteira). Fontes: `firstlaw`, `ideal_energy`.

## 37 — Calor nos processos isocórico e isobárico

ID: `formula-calor-processos`. Decisão: ficha_corrigida.

**Expressão:** Qisocórico = mcvΔT e Qisobárico = mcpΔT estão corretos nas condições indicadas.

**Símbolos e unidades:** A alteração prevista define Q e W em kJ, m em kg, cp e cv em kJ/(kg·K), ΔT em K ou intervalo em °C, p em kPa e V em m³. W é trabalho de fronteira.

**Hipóteses:** Usar gás ideal de massa e composição fixas, calores específicos constantes e apenas trabalho de fronteira. A etapa isobárica deve ser quase estática; desprezar variações cinética e potencial.

**Ensino vinculado:** A aula deriva Qp = ΔU + pΔV e a tabela declara a hipótese de trajetória quase estática.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Gás ideal de massa e composição fixas, calores específicos constantes, só trabalho de fronteira; isobárico quase estático; ΔEC/ΔEP desprezíveis.

**Vínculos finais:** [base-balanco-fechado](../../../../modulos/e1-termodinamica.html#base-balanco-fechado). Fontes: `firstlaw`, `ideal_energy`.

## 38 — Balanço de um ciclo fechado

ID: `formula-ciclo`. Decisão: ficha_mantida.

**Expressão:** ΔU no ciclo é zero e Qlíq = Wlíq está correto quando o sistema retorna ao estado inicial e não há variação líquida de energia mecânica.

**Símbolos e unidades:** As transferências são somas algébricas por ciclo, em kJ, conforme definido.

**Hipóteses:** Calor e trabalho não precisam ser nulos em cada etapa. A condição explicita o tratamento das variações cinética e potencial.

**Ensino vinculado:** A aula explica o retorno de uma propriedade ao valor inicial e a interpretação do ciclo horário.

**Resultado:** Mantida após conferência individual da expressão, símbolos/unidades, hipóteses e ensino vinculado. Condição publicada: Retorno ao mesmo estado, sem variação líquida de energia cinética ou potencial.

**Vínculos finais:** [base-trabalho-fronteira](../../../../modulos/e1-termodinamica.html#base-trabalho-fronteira). Fontes: `firstlaw`.

## 39 — Expansão livre isolada de gás ideal

ID: `formula-expansao-livre`. Decisão: ficha_corrigida.

**Expressão:** Na expansão livre do gás ideal, Q = W = 0. Pelo balanço total de energia, isso implica ΔU = −ΔEc − ΔEp. Somente com essas variações desprezíveis se conclui ΔU = 0 e, no modelo indicado, T₂ = T₁. A expressão ΔS = mR ln(V₂/V₁) = Sger então está correta.

**Símbolos e unidades:** Q e W são transferências de energia; ΔU é a variação de energia interna; ΔEc e ΔEp são as variações cinética e potencial, todas em unidades de energia compatíveis. T₁ e T₂ são temperaturas absolutas; ΔS e Sger são entropias.

**Hipóteses:** A alteração prevista explicita gás ideal em recipiente externo rígido, fechado e isolado, expansão para o vácuo, ausência de outros trabalhos e estados de equilíbrio com ΔEc e ΔEp desprezíveis. Q = W = 0, sozinho, não permite concluir ΔU = 0.

**Ensino vinculado:** A aula deriva ΔU = 0 sem nomear as variações cinética e potencial. É necessário explicitar o desprezo desses termos na hipótese inicial; a rigidez da parede externa, isoladamente, não elimina variações macroscópicas de energia.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Gás ideal em recipiente externo rígido, fechado e isolado; expansão para vácuo, sem outros trabalhos; estados de equilíbrio com ΔEC/ΔEP desprezíveis.

**Vínculos finais:** [base-expansao-livre](../../../../modulos/e1-termodinamica.html#base-expansao-livre). Fontes: `firstlaw`, `ideal_energy`, `mit_ideal_s`.

## 40 — Entalpia de reação e reação inversa

ID: `formula-reacao`. Decisão: ficha_corrigida.

**Expressão:** Qp = ΔH e a inversão do sinal para a reação inversa entre os mesmos estados estão corretos no modelo indicado.

**Símbolos e unidades:** A energia corresponde à quantidade de reação especificada; não deve ser tratada automaticamente como energia por mol.

**Hipóteses:** A alteração prevista explicita sistema fechado, pressão constante, apenas trabalho pV e variações cinética e potencial desprezíveis. A inversão deve manter os mesmos estados e referências.

**Ensino vinculado:** A aula trata de reação exotérmica e de sua inversa, além de comparar PCS e PCI sem mudar a base da comparação.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Qp = ΔH: sistema fechado, pressão constante, só trabalho pV e ΔEC/ΔEP desprezíveis. Inversão entre os mesmos estados.

**Vínculos finais:** [base-termoquimica](../../../../modulos/e1-termodinamica.html#base-termoquimica). Fontes: `firstlaw`, `algebra`.

## 41 — Definição de entalpia específica

ID: `formula-entalpia`. Decisão: ficha_mantida.

**Expressão:** h = u + pv é a definição correta de entalpia específica; ela não depende da idealidade do gás.

**Símbolos e unidades:** u e h em kJ/kg, p em kPa e v em m³/kg tornam pv compatível com kJ/kg.

**Hipóteses:** Não é necessário supor gás ideal ou regime permanente para definir h. A condição atual apenas interpreta seu uso no escoamento.

**Ensino vinculado:** O bloco de energia explica entalpia e escoamento sem restringir a definição a máquinas.

**Resultado:** Mantida após conferência individual da expressão, símbolos/unidades, hipóteses e ensino vinculado. Condição publicada: A parcela pv incorpora o trabalho de escoamento.

**Vínculos finais:** [energia](../../../../modulos/e1-termodinamica.html#energia). Fontes: `mit_cv`.

## 42 — Primeira lei: uma entrada e uma saída

ID: `formula-balanco-escoamento`. Decisão: ficha_corrigida.

**Expressão:** q − w = Δh + (vel₂² − vel₁²)/2000 + gΔz/1000 está correto na base de kJ/kg.

**Símbolos e unidades:** Os divisores 2000 e 1000 combinam o fator da energia cinética e a conversão de J/kg para kJ/kg. A alteração prevista define q como calor específico e w como trabalho específico não associado ao escoamento; h já inclui pv.

**Hipóteses:** Usar volume de controle fixo em regime permanente, com uma entrada e uma saída representativas. Calor entrando e trabalho saindo são positivos; o trabalho de escoamento não deve ser somado novamente.

**Ensino vinculado:** A aula apresenta a forma em J/kg e explica a divisão por 1000. O vínculo apoia a prevenção de somas indevidas entre J/kg e kJ/kg.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Volume de controle fixo em regime permanente, com uma entrada e uma saída representativas; q entra e w sai positivos.

**Vínculos finais:** [energia](../../../../modulos/e1-termodinamica.html#energia). Fontes: `mit_cv`.

## 43 — Turbina: trabalho e potência produzidos

ID: `formula-turbina`. Decisão: ficha_mantida.

**Expressão:** wt = h₁ − h₂ e a potência ṁ(h₁ − h₂) estão corretos.

**Símbolos e unidades:** kg/s multiplicado por kJ/kg resulta em kW; as magnitudes produzidas estão declaradas.

**Hipóteses:** Regime permanente, turbina adiabática e variações de energia cinética e potencial desprezíveis estão explícitos. Não é necessário exigir isentropia para esse balanço.

**Ensino vinculado:** O exemplo de 800 kW fornece os estados e as convenções utilizadas.

**Resultado:** Mantida após conferência individual da expressão, símbolos/unidades, hipóteses e ensino vinculado. Condição publicada: Regime permanente, adiabática; variações de velocidade e altura desprezíveis.

**Vínculos finais:** [base-turbina-potencia](../../../../modulos/e1-termodinamica.html#base-turbina-potencia). Fontes: `mit_cv`.

## 44 — Compressor: trabalho e potência consumidos

ID: `formula-compressor`. Decisão: ficha_mantida.

**Expressão:** O consumo específico como magnitude h₂ − h₁ e a potência correspondente estão corretos; o sentido do trabalho é oposto ao da turbina.

**Símbolos e unidades:** kJ/kg, kg/s e kW estão definidos de forma completa.

**Hipóteses:** Regime permanente, compressor adiabático e variações de energia cinética e potencial desprezíveis estão explícitos.

**Ensino vinculado:** A tabela no alvo define a magnitude consumida e não a confunde com eficiência isentrópica.

**Resultado:** Mantida após conferência individual da expressão, símbolos/unidades, hipóteses e ensino vinculado. Condição publicada: Regime permanente, adiabático; variações de velocidade e altura desprezíveis.

**Vínculos finais:** [energia](../../../../modulos/e1-termodinamica.html#energia). Fontes: `mit_cv`.

## 45 — Bomba ideal: líquido incompressível

ID: `formula-bomba`. Decisão: ficha_mantida_alvo_corrigido.

**Expressão:** wb,s ≈ vΔp e a potência correspondente estão corretos para líquido aproximadamente incompressível no caminho isentrópico.

**Símbolos e unidades:** m³/kg multiplicado por kPa resulta em kJ/kg; as magnitudes consumidas estão identificadas.

**Hipóteses:** A ficha já declara regime permanente, processo adiabático reversível, v aproximadamente constante e variações cinética e potencial desprezíveis.

**Ensino vinculado:** A tabela da aula menciona apenas líquido quase incompressível sob o rótulo “Bomba ideal”. O alvo precisa explicitar as hipóteses que a ficha já apresenta corretamente.

**Resultado:** A ficha já estava delimitada; a linha da bomba na aula recebeu as hipóteses faltantes. Condição publicada: Regime permanente, adiabático reversível; v aproximadamente constante; ΔEC/ΔEP desprezíveis.

**Vínculos finais:** [energia](../../../../modulos/e1-termodinamica.html#energia). Fontes: `mit_cv`, `mit_gibbs`.

## 46 — Válvula de estrangulamento

ID: `formula-valvula`. Decisão: ficha_corrigida.

**Expressão:** h₁ ≈ h₂ está correto na aproximação de estrangulamento delimitada.

**Símbolos e unidades:** h é dado em kJ/kg; igualdade de entalpia não exige temperatura constante.

**Hipóteses:** Para h₁≈h₂, além do regime permanente, adiabaticidade e variações mecânicas desprezíveis, deve ser nulo todo trabalho não associado ao escoamento. Ausência de eixo não exclui trabalho elétrico.

**Ensino vinculado:** A tabela vinculada já excluía calor e trabalho, sem restringir a eixo; foi preservada. A condição da ficha agora coincide com esse modelo passivo.

**Resultado:** R1-A corrigido: exclusão de todo trabalho não associado ao escoamento, recebido ou fornecido, inclusive elétrico; condições e data-busca sincronizadas. Condição publicada: Regime permanente, sem calor e sem qualquer trabalho não associado ao escoamento, recebido ou fornecido, inclusive elétrico; pv já integra h. ΔEC/ΔEP desprezíveis.

**Vínculos finais:** [energia](../../../../modulos/e1-termodinamica.html#energia). Fontes: `mit_cv`.

## 47 — Balanço de trocador ao ambiente adiabático

ID: `formula-trocador-balanco`. Decisão: ficha_mantida.

**Expressão:** A energia perdida pela corrente quente igual à energia recebida pela corrente fria está correta para duas correntes sem trocas externas relevantes.

**Símbolos e unidades:** Cada lado tem dimensão de potência: kg/s × kJ/kg = kW. Os índices quente/frio e entrada/saída estão definidos.

**Hipóteses:** Regime permanente, somente duas correntes, ausência de trabalho e calor externos e variações cinética e potencial desprezíveis estão explicitados. O conjunto adiabático não impede a troca de calor entre as correntes.

**Ensino vinculado:** A aula declara isolamento externo e balanço entre as correntes, sem impor ausência de transferência interna.

**Resultado:** Mantida após conferência individual da expressão, símbolos/unidades, hipóteses e ensino vinculado. Condição publicada: Regime permanente, sem trabalho e sem calor externo; ΔEC/ΔEP desprezíveis.

**Vínculos finais:** [energia](../../../../modulos/e1-termodinamica.html#energia). Fontes: `mit_cv`.

## 48 — Acumulação de massa

ID: `formula-acumulacao-massa`. Decisão: ficha_corrigida.

**Expressão:** dmVC/dt = Σṁin − Σṁout está correto por conservação de massa.

**Símbolos e unidades:** Ambos os lados têm unidade kg/s e os índices estão definidos.

**Hipóteses:** A alteração prevista explicita volume de controle fixo e inclusão de todas as entradas e saídas. Regime permanente exige acumulação de massa nula; acumulação de massa nula, sozinha, não prova que todas as propriedades estejam em regime permanente.

**Ensino vinculado:** A aula sobre enchimento do tanque distingue rigidez, adiabaticidade e regime permanente, preservando o termo de acumulação.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Volume de controle fixo; inclua todas as entradas e saídas. Regime permanente exige acumulação nula.

**Vínculos finais:** [base-balanco-transiente](../../../../modulos/e1-termodinamica.html#base-balanco-transiente). Fontes: `mit_cv`.

## 49 — Balanço transiente de energia

ID: `formula-acumulacao-energia`. Decisão: ficha_corrigida.

**Expressão:** dUVC/dt = Q̇ − Ẇ + Σin ṁh − Σout ṁh está correto quando as contribuições cinética e potencial são desprezadas. É um balanço reduzido, não a forma universal.

**Símbolos e unidades:** kJ/s = kW. A alteração prevista define UVC armazenada em kJ, Q̇ entrando e Ẇ saindo em kW, ṁ em kg/s e h em kJ/kg. Ẇ exclui o trabalho de escoamento já incluído em h.

**Hipóteses:** Usar volume de controle fixo, com entalpia representativa de cada corrente. Desprezar energia cinética e potencial tanto no armazenamento quanto nas correntes.

**Ensino vinculado:** A aula delimita o desprezo de energia cinética e potencial e define o trabalho empregado; não apresenta a redução como um balanço universal.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Volume de controle fixo; energias cinética/potencial desprezíveis no armazenamento e nas correntes. Ẇ exclui trabalho de escoamento já incluído em h.

**Vínculos finais:** [base-balanco-transiente](../../../../modulos/e1-termodinamica.html#base-balanco-transiente). Fontes: `mit_cv`.

## 50 — Energia em um intervalo com entrada e saída

ID: `formula-intervalo-energia`. Decisão: ficha_corrigida.

**Expressão:** Integrar os termos ṁh com h constante em cada corrente produz as parcelas mh. A massa dessas parcelas é a que atravessa a fronteira no intervalo.

**Símbolos e unidades:** As energias são totais em kJ, as massas atravessadas em kg e as entalpias em kJ/kg. A alteração prevista define Q entrando e W saindo, excluindo o trabalho de escoamento.

**Hipóteses:** Usar volume de controle fixo e o mesmo recorte de energia da ficha 49. Cada corrente deve manter h constante; se h variar, integrar ṁh no tempo.

**Ensino vinculado:** A aula distingue a massa inicialmente armazenada da massa que atravessa a fronteira e exige integração quando a entalpia da corrente varia.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Volume de controle fixo; h constante em cada corrente; energias cinética/potencial desprezíveis. Se h variar, integre ṁh no tempo.

**Vínculos finais:** [base-balanco-transiente](../../../../modulos/e1-termodinamica.html#base-balanco-transiente). Fontes: `mit_cv`.

## 51 — Tanque evacuado: enchimento adiabático

ID: `formula-enchimento-tanque`. Decisão: ficha_corrigida.

**Expressão:** u₂=h_in; T₂=(cp/cv)T_in — Integrar d(mu)=h_in dm com m₁=0 dá m₂u₂=m₂h_in. Com u=cvT+b e h=cpT+b, resulta T₂=cp Tin/cv; a referência b cancela.

**Símbolos e unidades:** Unidades coerentes: u,h em kJ/kg e T em K; cp/cv adimensional. Definir 2 como estado final do tanque e in como entrada.

**Hipóteses:** Evacuação inicial, rigidez, Q=W=0 e desprezo da parede/EC/EP estão presentes. Falta constância de h_in; para a relação térmica, cp e cv devem ser constantes individualmente.

**Ensino vinculado:** #base-balanco-transiente contém o balanço geral, sua integração para h constantes e o exemplo T₂=420 K; vínculo adequado.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Tanque rígido inicialmente evacuado, uma entrada e nenhuma saída; entalpia de entrada constante; Q=W=0; armazenamento na parede e EC/EP desprezíveis. Para T₂: mesmo gás ideal de composição fixa, cp e cv constantes e T_in constante.

**Vínculos finais:** [base-balanco-transiente](../../../../modulos/e1-termodinamica.html#base-balanco-transiente). Fontes: `mit_cv`.

## 52 — CO₂: acumulação no ambiente

ID: `formula-co2-acumulacao`. Decisão: ficha_corrigida.

**Expressão:** V dCi/dt=G+V̇(Ce−Ci) — Soma entrada V̇Ce, geração G e saída −V̇Ci; aumento de Ci intensifica a remoção líquida.

**Símbolos e unidades:** Dimensão de todos os termos: m³/h quando as concentrações são frações. G e V̇ têm unidades, mas G não está definido e V̇ não é explicitamente ar exterior na ficha.

**Hipóteses:** Mistura completa, diluição, volume/densidade constantes, fluxos iguais e ausência de remoções estão declarados. Falta mesma referência de T,p para volumes.

**Ensino vinculado:** #base-balanco-co2 ensina o balanço e todas essas hipóteses, inclusive ar exterior e condições comuns dos volumes.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Ambiente bem misturado, CO₂ diluído, volume/densidade constantes; vazões de entrada/saída iguais e na mesma referência T,p; sem outras fontes, remoções ou zonas.

**Vínculos finais:** [base-balanco-co2](../../../../modulos/e1-termodinamica.html#base-balanco-co2). Fontes: `nist_co2`.

## 53 — CO₂: vazão exterior em regime estacionário

ID: `formula-co2-vazao`. Decisão: ficha_corrigida.

**Expressão:** V̇=G/(Ci−Ce); Ci=Ce+G/V̇ — Anular acumulação na 52 e isolar V̇ ou Ci. G/V̇ é adimensional.

**Símbolos e unidades:** Concentrações em fração e conversão de ppm corretas. Completar unidade de G e significado das duas concentrações.

**Hipóteses:** Estacionário, bem misturado e G>0/Ci>Ce corretos; explicitar diluição, vazões iguais e ausência de outras fontes/remoções para evitar generalização.

**Ensino vinculado:** #base-balanco-co2 ensina modelo diferencial e redução estacionária, com exemplos de ambas as formas.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Zona única bem misturada e estacionária; CO₂ diluído, volume/densidade constantes, vazões de entrada/saída iguais e na mesma referência T,p, sem outras fontes/remoções. G>0, V̇>0 e Ci>Ce. Se fornecido o excesso, ele já é Ci−Ce.

**Vínculos finais:** [base-balanco-co2](../../../../modulos/e1-termodinamica.html#base-balanco-co2). Fontes: `nist_co2`.

## 54 — Renovações por hora

ID: `formula-renovacoes`. Decisão: ficha_mantida.

**Expressão:** n_ren=V̇/V — (m³/h)/m³=h⁻¹.

**Símbolos e unidades:** h⁻¹ com V̇ em m³/h e V em m³; n_ren definido.

**Hipóteses:** Ar exterior explicitamente distinguido de recirculação. Não exige equilíbrio de concentração para definir a taxa.

**Ensino vinculado:** #base-balanco-co2 ensina a razão, exemplo 600/200=3 h⁻¹ e ressalva de recirculação.

**Resultado:** Mantida após conferência individual da expressão, símbolos/unidades, hipóteses e ensino vinculado. Condição publicada: Vazão exterior; recirculação não equivale a renovação exterior.

**Vínculos finais:** [base-balanco-co2](../../../../modulos/e1-termodinamica.html#base-balanco-co2). Fontes: `nist_co2`.

## 55 — Potência hidráulica e rendimento de bomba

ID: `formula-bomba-potencia`. Decisão: ficha_corrigida.

**Expressão:** Ph=ρgV̇H; ηb=Ph/Peixo — ρgV̇H tem kg·m²/s³=W.

**Símbolos e unidades:** Unidades SI corretas; H identificado como altura manométrica. Definir H como carga mecânica total, ρ como densidade do líquido.

**Hipóteses:** A distinção entre potência no eixo e elétrica está correta. Acrescentar regime permanente/líquido aproximadamente incompressível.

**Ensino vinculado:** #base-bomba-integrada define H como energia por peso e ensina conversão de vazão; suporte adequado.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Bomba em regime permanente com líquido aproximadamente incompressível; H é a carga total acrescentada ao líquido. Potências como magnitudes positivas. Para potência elétrica, incluir o rendimento do motor.

**Vínculos finais:** [base-bomba-integrada](../../../../modulos/e1-termodinamica.html#base-bomba-integrada). Fontes: `doe_pump`, `doe_eff`.

## 56 — Misturador: duas entradas e uma saída

ID: `formula-misturador-correntes`. Decisão: ficha_corrigida.

**Expressão:** ṁ₃=ṁ₁+ṁ₂; ṁ₃h₃=Q̇−Ẇ+ṁ₁h₁+ṁ₂h₂; h₃=(ṁ₁h₁+ṁ₂h₂)/(ṁ₁+ṁ₂) — Balanço geral estacionário: 0=Q̇−Ẇ+Σṁh_in−Σṁh_out. Média é combinação convexa com vazões positivas.

**Símbolos e unidades:** kg/s e kJ/kg produzem kW; mesma referência das entalpias explicitada.

**Hipóteses:** Permanente e EC/EP desprezíveis explícitos; a média só para Q̇=Ẇ=0 está corretamente separada. Falta convenção de sinais local.

**Ensino vinculado:** #base-misturador-correntes contém as três expressões, Q entrando/W saindo e cautelas químicas.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Regime permanente; EC/EP desprezíveis; Q̇ entra e Ẇ sai positivos. A média de entalpias exige Q̇=Ẇ=0 e vazão total positiva. Com reação, inclua energia química nas propriedades.

**Vínculos finais:** [base-misturador-correntes](../../../../modulos/e1-termodinamica.html#base-misturador-correntes). Fontes: `mit_cv`.

## 57 — Bocal e difusor: entalpia e velocidade

ID: `formula-bocal-difusor`. Decisão: ficha_mantida.

**Expressão:** h₁−h₂=(vel₂²−vel₁²)/2000; vel₂=√[vel₁²+2000(h₁−h₂)] — h₁+vel₁²/(2·1000)=h₂+vel₂²/(2·1000); raiz retorna módulo da velocidade, não componente assinada.

**Símbolos e unidades:** h em kJ/kg e velocidades em m/s; conversão 2000 é correta. Índices entrada/saída definidos.

**Hipóteses:** Permanente, adiabático, sem trabalho, variação de altura desprezível e radicando não negativo. Não exige reversibilidade.

**Ensino vinculado:** #base-bocal-difusor ensina ambos os sentidos de conversão entalpia/energia cinética e exemplo.

**Resultado:** Mantida após conferência individual da expressão, símbolos/unidades, hipóteses e ensino vinculado. Condição publicada: Permanente, adiabático, sem trabalho, altura desprezível. Argumento da raiz não negativo; não requer reversibilidade.

**Vínculos finais:** [base-bocal-difusor](../../../../modulos/e1-termodinamica.html#base-bocal-difusor). Fontes: `mit_cv`.

## 58 — Máquina térmica: trabalho e rendimento

ID: `formula-eficiencia`. Decisão: ficha_mantida.

**Expressão:** Wliq=QH−QL; η=Wliq/QH=1−QL/QH — Retorno ao estado inicial anula ΔE do ciclo; dividir Wliq=QH−QL por QH.

**Símbolos e unidades:** Energias em mesma base por ciclo; η adimensional. QH/QL definidos como calor recebido/rejeitado.

**Hipóteses:** Magnitudes positivas e mesmo ciclo explícitos; título identifica máquina térmica.

**Ensino vinculado:** #base-eficiencia-cop fornece balanço, convenção de magnitudes e rendimento.

**Resultado:** Mantida após conferência individual da expressão, símbolos/unidades, hipóteses e ensino vinculado. Condição publicada: QH e QL são magnitudes positivas do mesmo ciclo.

**Vínculos finais:** [base-eficiencia-cop](../../../../modulos/e1-termodinamica.html#base-eficiencia-cop). Fontes: `open_carnot`.

## 59 — COP do refrigerador

ID: `formula-cop-refrigerador`. Decisão: ficha_mantida.

**Expressão:** COP_R=QL/Win — Efeito útil dividido pelo consumo; não há restrição COP≤1.

**Símbolos e unidades:** Mesma unidade para calor retirado da fonte fria e trabalho consumido; razão adimensional.

**Hipóteses:** Mesmo ciclo/fronteira e possibilidade de COP>1 corretamente declarados.

**Ensino vinculado:** #base-eficiencia-cop apresenta definição de refrigerador movido a trabalho e exemplo.

**Resultado:** Mantida após conferência individual da expressão, símbolos/unidades, hipóteses e ensino vinculado. Condição publicada: Mesmo ciclo e fronteira; COP é adimensional e pode exceder 1.

**Vínculos finais:** [base-eficiencia-cop](../../../../modulos/e1-termodinamica.html#base-eficiencia-cop). Fontes: `open_cop`.

## 60 — COP da bomba de calor

ID: `formula-cop-bomba-calor`. Decisão: ficha_mantida.

**Expressão:** COP_BC=QH/Win; COP_BC=COP_R+1 — QH/Win=QL/Win+1.

**Símbolos e unidades:** QH entregue à fonte quente e Win consumido na mesma base; COP adimensional.

**Hipóteses:** Mesmo ciclo/fronteira e ausência de outras trocas relevantes explicitados.

**Ensino vinculado:** #base-eficiencia-cop ensina ambos os COPs e a identidade para o mesmo ciclo.

**Resultado:** Mantida após conferência individual da expressão, símbolos/unidades, hipóteses e ensino vinculado. Condição publicada: Mesmo ciclo e fronteira, sem outras trocas relevantes.

**Vínculos finais:** [base-eficiencia-cop](../../../../modulos/e1-termodinamica.html#base-eficiencia-cop). Fontes: `open_cop`.

## 61 — Limite de rendimento de Carnot

ID: `formula-carnot`. Decisão: ficha_mantida.

**Expressão:** ηC=1−TL/TH; η≤ηC — Entropia das fontes exige QL/TL−QH/TH≥0; dividir o balanço energético por QH.

**Símbolos e unidades:** Temperaturas em K e rendimentos adimensionais. TH/TL identificam reservatórios.

**Hipóteses:** Máquina cíclica com apenas dois reservatórios e TH>TL>0 estão explícitos.

**Ensino vinculado:** #base-limite-carnot apresenta a fórmula, a referência reversível e diferença das irreversíveis.

**Resultado:** Mantida após conferência individual da expressão, símbolos/unidades, hipóteses e ensino vinculado. Condição publicada: Máquina cíclica entre dois reservatórios; TH > TL > 0.

**Vínculos finais:** [base-limite-carnot](../../../../modulos/e1-termodinamica.html#base-limite-carnot). Fontes: `open_carnot`.

## 62 — Trabalho máximo e rejeição mínima

ID: `formula-limites-carnot`. Decisão: ficha_corrigida.

**Expressão:** Wmax=QH(1−TL/TH); QL,min=QH TL/TH — Multiplicar η≤1−TL/TH por QH fixo e usar QL=QH−Wliq.

**Símbolos e unidades:** Unidades de energia e K corretas, mas faltam os significados dos símbolos no detalhe.

**Hipóteses:** Dois reservatórios fixos e reversibilidade na igualdade declarados; falta fixar também QH para que máximo/mínimo sejam determinados.

**Ensino vinculado:** #base-carnot-prova deduz a rejeição mínima e exemplifica para QH fixado.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Máquina cíclica entre apenas dois reservatórios fixos com TH>TL>0, para calor recebido QH>0 fixado. Wmax e QL,min são limites atingidos pelo ciclo reversível.

**Vínculos finais:** [base-carnot-prova](../../../../modulos/e1-termodinamica.html#base-carnot-prova). Fontes: `open_carnot`.

## 63 — COPs reversíveis de Carnot

ID: `formula-cop-carnot`. Decisão: ficha_corrigida.

**Expressão:** COP_R,C=TL/(TH−TL); COP_BC,C=TH/(TH−TL) — Para referência reversível QH/TH=QL/TL e Win=QH−QL.

**Símbolos e unidades:** K correto; falta explicitar COP_R,C e COP_BC,C como razões adimensionais.

**Hipóteses:** Reversível e mesmos dois reservatórios declarados; acrescentar TL>0 ao domínio TH>TL.

**Ensino vinculado:** #base-limite-carnot contém as duas formas e as respectivas definições.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Refrigerador ou bomba de calor reversível, movido a trabalho entre os mesmos dois reservatórios fixos; TH>TL>0.

**Vínculos finais:** [base-limite-carnot](../../../../modulos/e1-termodinamica.html#base-limite-carnot). Fontes: `open_cop`, `open_carnot`.

## 64 — Entropia: sistema fechado

ID: `formula-balanco-entropia`. Decisão: ficha_corrigida.

**Expressão:** ΔS=∫₁²δQ/Tb+Sger; Sger≥0 — Exemplo diagnóstico: +100 kJ a 400 K e −100 kJ a 300 K dão calor líquido zero, mas transferência de entropia −0,08333 kJ/K.

**Símbolos e unidades:** kJ/K, kJ e K coerentes. Definir ΔS=S₂−S₁ e geração total no intervalo.

**Hipóteses:** Q positivo entrando e reversibilidade interna corretos. A notação com um Tb precisa delimitar como tratar várias partes da fronteira a temperaturas distintas.

**Ensino vinculado:** #base-entropia contém a mesma integral e define temperatura local; adequado como base, mas deve explicitar soma sobre contatos.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Sistema fechado com um contato térmico uniforme a Tb; calor entrando positivo. Para vários contatos, some as integrais locais; nunca divida calor líquido por uma temperatura arbitrária. Sger = 0 no processo internamente reversível.

**Vínculos finais:** [base-entropia](../../../../modulos/e1-termodinamica.html#base-entropia). Fontes: `mit_entropy`.

## 65 — Entropia de sistema isolado

ID: `formula-entropia-isolado`. Decisão: ficha_mantida.

**Expressão:** ΔS=Sger≥0 — Sem transferência de massa/calor, resta geração. Trabalho não transfere entropia, mas o isolamento aqui também o elimina.

**Símbolos e unidades:** Entropia total e gerada em kJ/K.

**Hipóteses:** Isolamento de massa e energia explicitado; uma parte pode perder entropia.

**Ensino vinculado:** #base-entropia ensina a desigualdade para sistema isolado e diferencia geração de transferência.

**Resultado:** Mantida após conferência individual da expressão, símbolos/unidades, hipóteses e ensino vinculado. Condição publicada: Sem trocas de massa ou energia; uma parte do conjunto pode perder entropia.

**Vínculos finais:** [base-entropia](../../../../modulos/e1-termodinamica.html#base-entropia). Fontes: `mit_entropy`.

## 66 — Sistema e vizinhança: entropia total

ID: `formula-entropia-total`. Decisão: ficha_mantida.

**Expressão:** ΔStotal=ΔSsistema+ΔSviz; ΔStotal≥0 — Somar balanços dos dois subsistemas cancela transferências internas; resta geração total.

**Símbolos e unidades:** As parcelas têm unidade kJ/K e vizinhança é parte do conjunto.

**Hipóteses:** Conjunto total isolado e desigualdade apenas para soma corretamente declarados.

**Ensino vinculado:** #base-entropia explica que parte pode perder entropia e o conjunto não; soma é extensão direta por aditividade.

**Resultado:** Mantida após conferência individual da expressão, símbolos/unidades, hipóteses e ensino vinculado. Condição publicada: Conjunto total isolado; a soma, não cada parcela, deve ser não negativa.

**Vínculos finais:** [base-entropia](../../../../modulos/e1-termodinamica.html#base-entropia). Fontes: `mit_entropy`, `open_entropy`.

## 67 — Calor reversível e entropia

ID: `formula-calor-reversivel`. Decisão: ficha_mantida.

**Expressão:** δqrev=T ds; qrev=∫₁²T ds — Dimensão T ds=kJ/kg; integração é ao longo da trajetória reversível escolhida.

**Símbolos e unidades:** qrev em kJ/kg, T em K e s em kJ/(kg·K).

**Hipóteses:** Trajetória reversível de referência explícita; alerta sobre calor real irreversível evita universalização.

**Ensino vinculado:** #substancias inclui “Calor reversível no diagrama T–s”, expressão diferencial e interpretação da área. Integral é continuação direta.

**Resultado:** Mantida após conferência individual da expressão, símbolos/unidades, hipóteses e ensino vinculado. Condição publicada: Trajetória reversível de referência; área em T–s não é calor real de todo processo.

**Vínculos finais:** [substancias](../../../../modulos/e1-termodinamica.html#substancias). Fontes: `open_entropy`, `mit_gibbs`.

## 68 — Gás ideal: entropia por T e p

ID: `formula-entropia-tp`. Decisão: ficha_corrigida.

**Expressão:** Δs=cp ln(T₂/T₁)−R ln(p₂/p₁) — Substituir dv/v=dT/T−dp/p em ds=cv dT/T+R dv/v e cp=cv+R.

**Símbolos e unidades:** Unidades e pressão absoluta corretas; s, cp e R só têm unidades e não nomes na ficha.

**Hipóteses:** Título impõe gás ideal; composição fixa/cp constante e logaritmos de razões corretos.

**Ensino vinculado:** #base-entropia-gas contém expressão e nomes dos símbolos, estado inicial/final.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Composição fixa e cp constante; ln de razões adimensionais.

**Vínculos finais:** [base-entropia-gas](../../../../modulos/e1-termodinamica.html#base-entropia-gas). Fontes: `mit_ideal_s`.

## 69 — Gás ideal: entropia por T e v

ID: `formula-entropia-tv`. Decisão: ficha_corrigida.

**Expressão:** Δs=cv ln(T₂/T₁)+R ln(v₂/v₁) — Integração de ds=cv dT/T+R dv/v; expansão isotérmica ideal aumenta s.

**Símbolos e unidades:** Sinal de volume correto. Falta unidade de v e nome de cv/R; volumes devem usar mesma base por massa.

**Hipóteses:** Gás ideal no título, composição fixa e cv constante explícitos.

**Ensino vinculado:** #base-entropia-gas ensina a fórmula e v em m³/kg.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Composição fixa e cv constante; não omita o sinal positivo do termo de volume.

**Vínculos finais:** [base-entropia-gas](../../../../modulos/e1-termodinamica.html#base-entropia-gas). Fontes: `mit_ideal_s`.

## 70 — Relações isentrópicas do gás ideal

ID: `formula-isentro-gas`. Decisão: ficha_corrigida.

**Expressão:** T₂/T₁=(p₂/p₁)^((k−1)/k); pv^k=cte; T₂/T₁=(v₁/v₂)^(k−1) — Δs=0 fornece T v^(k−1)=constante; com pv=RT resulta pv^k=constante.

**Símbolos e unidades:** Pressão absoluta e temperatura K corretas; falta unidade de v e caracterizar k como adimensional.

**Hipóteses:** Gás ideal isentrópico com capacidades constantes explícito; composições/referências devem ser as mesmas.

**Ensino vinculado:** #base-entropia-gas ensina forma T,p e pv^k; a forma T,v decorre imediatamente da equação de estado e da forma de entropia.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Mesmo gás ideal de composição fixa em sequência de estados isentrópicos, com cp e cv constantes.

**Vínculos finais:** [base-entropia-gas](../../../../modulos/e1-termodinamica.html#base-entropia-gas). Fontes: `mit_ideal_s`.

## 71 — Eficiência isentrópica da turbina

ID: `formula-isentropica-turbina`. Decisão: ficha_corrigida.

**Expressão:** ηt=(h₁−h₂,real)/(h₁−h₂,s) — Na turbina wt=h₁−h₂; eficiência é trabalho real dividido pelo isentrópico de referência.

**Símbolos e unidades:** h em kJ/kg e eficiência adimensional; explicitar h como entalpia específica, 2,real como saída real.

**Hipóteses:** Mesma entrada e pressão final, adiabaticidade e ΔEC/ΔEP desprezíveis presentes. Falta declarar regime permanente.

**Ensino vinculado:** #base-isentropica ensina definição real/ideal, saída de referência e comparação; condições operacionais devem ser explicitadas junto da fórmula.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Turbina em regime permanente, adiabática, com ΔEC/ΔEP desprezíveis. Comparar a mesma entrada e mesma pressão de saída; referência s isentrópica. Denominador h₁−h₂,s>0.

**Vínculos finais:** [base-isentropica](../../../../modulos/e1-termodinamica.html#base-isentropica). Fontes: `purdue_turb`, `mit_cv`.

## 72 — Eficiência isentrópica do compressor

ID: `formula-isentropica-compressor`. Decisão: ficha_corrigida.

**Expressão:** ηc=(h₂,s−h₁)/(h₂,real−h₁) — wc=h₂−h₁; razão de trabalho ideal para real.

**Símbolos e unidades:** h em kJ/kg e ηc adimensional; o detalhe não define 1 e 2,real.

**Hipóteses:** Mesma entrada/pressão final, adiabático e EC/EP desprezíveis presentes. Falta regime permanente.

**Ensino vinculado:** #base-isentropica ensina razão ideal/real e saída s na mesma pressão.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Compressor em regime permanente, adiabático, com ΔEC/ΔEP desprezíveis. Mesma entrada e pressão de saída na referência isentrópica; h₂,real−h₁>0.

**Vínculos finais:** [base-isentropica](../../../../modulos/e1-termodinamica.html#base-isentropica). Fontes: `purdue_ref`, `mit_cv`.

## 73 — Entropia: volume de controle permanente

ID: `formula-entropia-vc`. Decisão: ficha_corrigida.

**Expressão:** Ṡger=Σsai ṁs−Σent ṁs−Σj Q̇j/Tj≥0 — Isolar geração em 0=Σent ṁs−Σsai ṁs+ΣQ̇j/Tj+Ṡger; sinais verificados.

**Símbolos e unidades:** Todas as parcelas em kW/K. ṁ, s e Tj têm unidades, mas convém nomear correntes e contatos.

**Hipóteses:** Sem acumulação e calor positivo entrando explícitos. Cada Tj deve representar temperatura uniforme no contato j; substituir soma por integral se distribuída.

**Ensino vinculado:** #aprofundamento-aplicado ensina o balanço completo estacionário, não só uma ocorrência do símbolo; exemplo de trocador adiabático coerente.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Volume de controle estacionário. Q̇j positivo entrando por contato j de temperatura uniforme Tj>0. Se a temperatura variar ao longo da fronteira, integrar Q̇/T localmente; Ṡger≥0.

**Vínculos finais:** [aprofundamento-aplicado](../../../../modulos/e1-termodinamica.html#aprofundamento-aplicado). Fontes: `mit_entropy`.

## 74 — Gouy–Stodola: exergia destruída

ID: `formula-exergia`. Decisão: ficha_mantida.

**Expressão:** Xdest=T₀Sger; Ẋdest=T₀Ṡger — K·kJ/K=kJ; Sger≥0 e T₀>0 implicam Xdest≥0.

**Símbolos e unidades:** kJ e kW corretos; T₀ K, Sger kJ/K e taxa kW/K.

**Hipóteses:** Ambiente a T₀ constante e diferença entre geração e ΔS declaradas.

**Ensino vinculado:** #base-exergia define trabalho útil máximo e ensina Gouy–Stodola com exemplo numérico.

**Resultado:** Mantida após conferência individual da expressão, símbolos/unidades, hipóteses e ensino vinculado. Condição publicada: Ambiente a T0 constante; Sger não é necessariamente ΔS do sistema.

**Vínculos finais:** [base-exergia](../../../../modulos/e1-termodinamica.html#base-exergia). Fontes: `mit_lost`.

## 75 — Identidades termodinâmicas

ID: `formula-identidades`. Decisão: ficha_mantida.

**Expressão:** du=T ds−p dv; dh=T ds+v dp — dh=du+p dv+v dp cancela −p dv.

**Símbolos e unidades:** Base específica consistente: kPa·m³/kg=kJ/kg; T ds na mesma unidade.

**Hipóteses:** Propriedades de equilíbrio, substância simples compressível e composição fixa declaradas.

**Ensino vinculado:** #base-gibbs deriva dh a partir de du e h=u+pv; alerta que a identidade não é calor/trabalho real de qualquer processo.

**Resultado:** Mantida após conferência individual da expressão, símbolos/unidades, hipóteses e ensino vinculado. Condição publicada: Propriedades de equilíbrio de substância simples compressível e composição fixa.

**Vínculos finais:** [base-gibbs](../../../../modulos/e1-termodinamica.html#base-gibbs). Fontes: `mit_gibbs`.

## 76 — Entalpia em variação isentrópica

ID: `formula-entalpia-isentro`. Decisão: ficha_corrigida.

**Expressão:** ds=0 ⇒ dh=v dp; Δh≈v(p₂−p₁) — ds=0 anula T ds; se v>0, sinal de dh acompanha dp.

**Símbolos e unidades:** h kJ/kg, v m³/kg e p kPa coerentes. s aparece na expressão sem definição/unidade no detalhe.

**Hipóteses:** v aproximadamente constante corretamente exigido para a forma finita. Falta repetir o domínio simples compressível/composição fixa.

**Ensino vinculado:** #base-gibbs explica ambas as formas, integração se v variar e hipótese da identidade.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Substância simples compressível de composição fixa, estados de equilíbrio ao longo de uma isentrópica. A forma finita exige v aproximadamente constante; caso contrário, usar Δh=∫ₚ₁^ₚ₂ v dp nessa isentrópica.

**Vínculos finais:** [base-gibbs](../../../../modulos/e1-termodinamica.html#base-gibbs). Fontes: `mit_gibbs`.

## 77 — Gibbs e equilíbrio de fases

ID: `formula-gibbs-fases`. Decisão: ficha_corrigida.

**Expressão:** G=H−TS; dG=(μg−μf)dn; μg=μf no equilíbrio — dG=μf(−dn)+μg dn; igualdade anula a primeira variação, mas não substitui análise de estabilidade.

**Símbolos e unidades:** Unidades extensivas/mol corretas; nomear f como líquido e g como vapor, em vez de somente “fases”.

**Hipóteses:** Mesmo componente, T,p fixas e dn positivo líquido→vapor corretos. “Usualmente só trabalho pV” deve virar hipótese explícita, com outros componentes fixos.

**Ensino vinculado:** #base-equilibrio-fases explica transferência, mínimo de Gibbs e μl/μv. A ficha usa f/g: harmonização local necessária.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Transferência infinitesimal do mesmo componente entre fases líquida f e vapor g em um conjunto fechado a T,p fixas; somente trabalho pV, sem campos/interfícies relevantes. Outras quantidades independentes mantidas fixas. A igualdade de μ é necessária ao equilíbrio entre fases presentes com troca permitida.

**Vínculos finais:** [base-equilibrio-fases](../../../../modulos/e1-termodinamica.html#base-equilibrio-fases). Fontes: `wash_gibbs`, `mit_phase`.

## 78 — Entropia com calor específico variável

ID: `formula-entropia-c-variavel`. Decisão: ficha_corrigida.

**Expressão:** Δs=∫T₁^T₂ cp(T)/T dT−R ln(p₂/p₁) — Integração de ds=cp(T)dT/T−R dp/p, válida para diferença de propriedade entre estados.

**Símbolos e unidades:** Unidades corretas; definir R específico e Δs, não só listar unidades.

**Hipóteses:** Gás ideal, composição fixa, cp(T) e log adimensional declarados; não exige processo real reversível.

**Ensino vinculado:** #base-calor-variavel contém exatamente a forma e explica integração/limites do gás ideal.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Gás ideal de composição fixa; cp varia com T; argumentos de logaritmos são adimensionais.

**Vínculos finais:** [base-calor-variavel](../../../../modulos/e1-termodinamica.html#base-calor-variavel). Fontes: `mit_ideal_s`.

## 79 — Rankine: balanços por equipamento

ID: `formula-rankine`. Decisão: ficha_corrigida.

**Expressão:** wt=h₃−h₄; wb=h₂−h₁; qin=h₃−h₂; qout=h₄−h₁; η=(wt−wb)/qin — Soma telescópica das quatro diferenças: (h₃−h₂)−(h₄−h₁)=(h₃−h₄)−(h₂−h₁).

**Símbolos e unidades:** Estados 1–4 identificados e kJ/kg correto; definir todas as energias como magnitudes e η adimensional.

**Hipóteses:** Os balanços qin=h₃−h₂ e qout=h₄−h₁ exigem caldeira e condensador sem qualquer trabalho não associado ao escoamento, recebido ou fornecido, inclusive elétrico. As demais hipóteses e o trabalho pv incorporado a h foram preservados.

**Ensino vinculado:** #base-rankine recebeu a mesma exclusão completa nos dois trocadores; estados, quatro balanços, eficiência e distinção da isentropia ficaram intactos.

**Resultado:** R1-A corrigido: exclusão de todo trabalho não associado ao escoamento, recebido ou fornecido, inclusive elétrico; condições e data-busca sincronizadas. Condição publicada: Rankine simples sem extrações, mesma vazão, regime permanente e ΔEC/ΔEP desprezíveis; bomba/turbina adiabáticas. Caldeira/condensador sem qualquer trabalho não associado ao escoamento, recebido ou fornecido, inclusive elétrico; pv já integra h. qin>0 e trabalho líquido positivo.

**Vínculos finais:** [base-rankine](../../../../modulos/e1-termodinamica.html#base-rankine). Fontes: `mit_cv`, `mit_rankine`.

## 80 — Brayton: trabalho líquido e rendimento

ID: `formula-brayton-liquido`. Decisão: ficha_mantida.

**Expressão:** Ẇliq=Ẇt−Ẇc; η=(Ẇt−Ẇc)/Q̇in — Subtrair consumo do compressor da produção da turbina na mesma fronteira.

**Símbolos e unidades:** Taxas kW e magnitude consumida identificadas; uma base única exigida.

**Hipóteses:** Sem outros consumos explicitado. Título e Q̇in externo delimitam rendimento do conjunto.

**Ensino vinculado:** #base-brayton-real ensina exatamente a diferença e mostra exemplo de potência líquida.

**Resultado:** Mantida após conferência individual da expressão, símbolos/unidades, hipóteses e ensino vinculado. Condição publicada: Sem outros consumos; também vale com energias por ciclo ou por kg, em uma única base.

**Vínculos finais:** [base-brayton-real](../../../../modulos/e1-termodinamica.html#base-brayton-real). Fontes: `mit_brayton`.

## 81 — Rendimento do Brayton ideal

ID: `formula-brayton-ideal`. Decisão: ficha_mantida.

**Expressão:** rp=palta/pbaixa; ηB=1−rp^(-(k−1)/k) — Com T₂/T₁=T₃/T₄=rp^((k−1)/k), razão de calores leva à forma exibida.

**Símbolos e unidades:** Razão de pressões absolutas e eficiência adimensionais; k=cp/cv.

**Hipóteses:** Gás ideal, capacidades constantes, duas isentrópicas/isobáricas e viabilidade motora declarados.

**Ensino vinculado:** #base-brayton ensina a relação e limites de alterações do ciclo; #base-brayton-real detalha viabilidade.

**Resultado:** Mantida após conferência individual da expressão, símbolos/unidades, hipóteses e ensino vinculado. Condição publicada: Gás ideal, cp/cv constantes, duas isentrópicas e duas isobáricas; ciclo motor viável.

**Vínculos finais:** [base-brayton](../../../../modulos/e1-termodinamica.html#base-brayton). Fontes: `mit_brayton`.

## 82 — Rendimento do Otto ideal

ID: `formula-otto`. Decisão: ficha_mantida.

**Expressão:** r=Vmax/Vmin; ηO=1−r^(-(k−1)) — Qout/Qin=(T₄−T₁)/(T₃−T₂)=r^(1−k).

**Símbolos e unidades:** r,k,η adimensionais; volumes na mesma unidade, inferível pela razão e nome.

**Hipóteses:** Ar-padrão ideal com capacidades constantes e adição isocórica; título Otto identifica as demais etapas.

**Ensino vinculado:** #ciclos contém a tabela Otto/Diesel, compressão/expansão isentrópicas, definição de r e fórmula.

**Resultado:** Mantida após conferência individual da expressão, símbolos/unidades, hipóteses e ensino vinculado. Condição publicada: Modelo ar-padrão ideal, calores específicos constantes; adição de calor isocórica.

**Vínculos finais:** [ciclos](../../../../modulos/e1-termodinamica.html#ciclos). Fontes: `mit_otto`.

## 83 — Rendimento do Diesel ideal

ID: `formula-diesel`. Decisão: ficha_corrigida.

**Expressão:** rc=V₃/V₂; ηD=1−r^(-(k−1))(rc^k−1)/[k(rc−1)] — T₂/T₁=r^(k−1), T₃/T₂=rc e T₄/T₁=rc^k. Substituir qin=cp(T₃−T₂), qout=cv(T₄−T₁).

**Símbolos e unidades:** r,rc,k e ηD são adimensionais, mas ηD não definido e V₂/V₃ não nomeados além do trecho.

**Hipóteses:** Modelo ar-padrão/capacidades constantes/adição isobárica corretos; domínio rc=1 gera 0/0 e ciclo precisa de expansão após adição.

**Ensino vinculado:** #ciclos contém fórmula e definição verbal da razão de corte. Não atribui estados 2/3, supridos pela ficha.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Diesel ar-padrão ideal com cp e cv constantes: compressão/expansão isentrópicas, adição isobárica e rejeição isocórica. r>1, k>1 e 1<rc<r no ciclo convencional não degenerado.

**Vínculos finais:** [ciclos](../../../../modulos/e1-termodinamica.html#ciclos). Fontes: `mit_diesel`.

## 84 — Refrigeração por compressão de vapor

ID: `formula-refrigeracao`. Decisão: ficha_corrigida.

**Expressão:** qL=h₁−h₄; wc=h₂−h₁; qH=h₂−h₃; h₃≈h₄; COP_R=(h₁−h₄)/(h₂−h₁) — Com h₃=h₄: qH−qL=h₂−h₁=wc.

**Símbolos e unidades:** Índices e kJ/kg corretos; definir qL,qH,wc como magnitudes e COP adimensional.

**Hipóteses:** Condensador, evaporador e válvula não recebem nem fornecem qualquer trabalho não associado ao escoamento, inclusive elétrico. Compressor e válvula são adiabáticos; pv continua em h. Dizer apenas que os trocadores não produzem trabalho não excluía recebimento.

**Ensino vinculado:** #base-refrigeracao agora exclui trabalhos nos dois sentidos nos componentes passivos. Estados, relações de entalpia, soma de calor e trabalho do ciclo e COP ficaram intactos.

**Resultado:** R1-A corrigido: exclusão de todo trabalho não associado ao escoamento, recebido ou fornecido, inclusive elétrico; condições e data-busca sincronizadas. Condição publicada: Ciclo simples estacionário com mesma vazão; ΔEC/ΔEP desprezíveis. Compressor e válvula adiabáticos. Condensador, evaporador e válvula sem qualquer trabalho não associado ao escoamento, recebido ou fornecido, inclusive elétrico; pv já integra h. Desprezar trocas nas ligações. wc>0.

**Vínculos finais:** [base-refrigeracao](../../../../modulos/e1-termodinamica.html#base-refrigeracao). Fontes: `purdue_ref`, `mit_cv`.

## 85 — Calor rejeitado no condensador

ID: `formula-condensador`. Decisão: ficha_corrigida.

**Expressão:** Q̇H=Q̇L+Ẇin — Primeira lei do ciclo: Q̇L+Ẇin−Q̇H=0.

**Símbolos e unidades:** Magnitudes em kW, definidas corretamente.

**Hipóteses:** Ciclo permanente sem outras trocas/consumos é condição suficiente; nenhuma irreversibilidade precisa ser anulada.

**Ensino vinculado:** #base-eficiencia-cop ensina definições e diferença entre COPs; o exemplo explícito QH=600+200 está em #base-refrigeracao.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Ciclo permanente, sem outras perdas/trocas ou consumos relevantes.

**Vínculos finais:** [base-refrigeracao](../../../../modulos/e1-termodinamica.html#base-refrigeracao). Fontes: `open_cop`, `purdue_ref`.

## 86 — Fração extraída para aquecedor aberto

ID: `formula-extracao-aquecedor`. Decisão: ficha_mantida.

**Expressão:** y=(hsaída−hágua)/(hextração−hágua) — yh_extração+(1−y)h_água=h_saída ⇒ y(h_extração−h_água)=h_saída−h_água.

**Símbolos e unidades:** y definido por vazão extraída/principal; h em kJ/kg, grandezas de cada corrente identificadas.

**Hipóteses:** Aquecedor aberto estacionário, adiabático, sem trabalho, EC/EP desprezíveis, pressões compatíveis, 0≤y≤1 e denominador não nulo estão explícitos.

**Ensino vinculado:** #base-ciclos-variantes deduz a equação da massa e energia, calcula y e distingue aquecedor fechado.

**Resultado:** Mantida após conferência individual da expressão, símbolos/unidades, hipóteses e ensino vinculado. Condição publicada: Aquecedor aberto, permanente, adiabático, sem trabalho; EC/EP desprezíveis; pressões compatíveis; 0≤y≤1 e denominador não nulo.

**Vínculos finais:** [base-ciclos-variantes](../../../../modulos/e1-termodinamica.html#base-ciclos-variantes). Fontes: `mit_cv`.

## 87 — Eficiência volumétrica

ID: `formula-volumetrica`. Decisão: ficha_mantida.

**Expressão:** ηv=Vfresco,admitido/Vdeslocado — Massa admitida vezes volume específico na sucção produz volume equivalente admitido; dividir pelo deslocamento.

**Símbolos e unidades:** Razão adimensional com mesmos volumes por ciclo ou vazões na mesma base.

**Hipóteses:** Referência de sucção explícita; não confunde com eficiência isentrópica.

**Ensino vinculado:** #base-eficiencia-volumetrica ensina volume varrido, gás fresco referido à sucção e exemplo 3,5/5.

**Resultado:** Mantida após conferência individual da expressão, símbolos/unidades, hipóteses e ensino vinculado. Condição publicada: Volume admitido referido às condições de sucção; não é eficiência isentrópica.

**Vínculos finais:** [base-eficiencia-volumetrica](../../../../modulos/e1-termodinamica.html#base-eficiencia-volumetrica). Fontes: `purdue_comp`.

## 88 — Pressão intermediária ideal: dois estágios

ID: `formula-intermediaria`. Decisão: ficha_corrigida.

**Expressão:** pi=√(p₁p₃); pi/p₁=p₃/pi — Com z=ln(pi/p₁), R=p₃/p₁ e A=cpT₁/ηc>0: w=A[e^(az)+R^a e^(−az)−2]. w′=Aa[e^(az)−R^a e^(−az)]; w″=Aa²[e^(az)+R^a e^(−az)]>0. Único mínimo z=ln(R)/2 ⇒ pi=√p₁p₃. Sem resfriamento perfeito ou com η dependente da razão, essa função muda.

**Símbolos e unidades:** Todas pressões absolutas na mesma unidade; raiz de pressão² tem dimensão de pressão.

**Hipóteses:** Estágios equivalentes, intercooling perfeito e perdas desprezíveis não explicitam modelo de propriedades nem objetivo de otimização.

**Ensino vinculado:** #aprofundamento-aplicado afirma trabalho mínimo e eficiência igual, mas também omite gás ideal/cp constante e independência da eficiência em relação à pressão escolhida. A aula precisa acompanhar a condição corrigida.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Mínimo trabalho total de dois estágios adiabáticos: mesmo gás ideal, cp e cv constantes, mesma eficiência isentrópica constante; resfriamento até T₁ sem perda de pressão, mesma vazão, sem mudança de fase. ΔEC/ΔEP desprezíveis; p₃>p₁>0 fixas.

**Vínculos finais:** [aprofundamento-aplicado](../../../../modulos/e1-termodinamica.html#aprofundamento-aplicado). Fontes: `tamu_two`, `purdue_comp`.

## 89 — Compressão politrópica: trabalho consumido

ID: `formula-politropico`. Decisão: ficha_corrigida.

**Expressão:** win=np/(np−1) R T₁[(p₂/p₁)^((np−1)/np)−1] — Para escoamento reversível δwin=v dp. v=v₁(p₁/p)^(1/np); integrar p₁→p₂ e usar p₁v₁=RT₁. A exclusão np>0 limita o caso convencional de compressão volumétrica, sem alegar que todos os processos com np<0 sejam matematicamente inexistentes.

**Símbolos e unidades:** R específico kJ/(kg·K), T₁ K e trabalho kJ/kg; np não confunde com mol.

**Hipóteses:** Escoamento permanente reversível, gás ideal e pv^np constante explícitos. Excluir somente np=1 não evita divisão por np=0; compressão requer p₂>p₁.

**Ensino vinculado:** #aplicacoes ensina o fator np do escoamento e sua diferença para o trabalho de fronteira. O domínio da aula também só exclui 1.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Gás ideal de composição fixa em compressão estacionária internamente reversível, pv^np constante com np constante >0 e np≠1; p₂>p₁>0; ΔEC/ΔEP desprezíveis.

**Vínculos finais:** [aplicacoes](../../../../modulos/e1-termodinamica.html#aplicacoes). Fontes: `purdue_comp`, `mit_gibbs`.

## 90 — Limite isotérmico: trabalho consumido

ID: `formula-compressao-isotermica`. Decisão: ficha_mantida.

**Expressão:** win=RT ln(p₂/p₁) — Integrar v dp=RT dp/p com T constante; também limite np→1 da expressão 89.

**Símbolos e unidades:** R em kJ/(kg·K), T K e win kJ/kg; pressões absolutas; trabalho positivo na compressão.

**Hipóteses:** Gás ideal, escoamento permanente internamente reversível isotérmico e EC/EP desprezíveis declarados.

**Ensino vinculado:** #aplicacoes contém expressão e diferença entre trabalho de escoamento e fronteira.

**Resultado:** Mantida após conferência individual da expressão, símbolos/unidades, hipóteses e ensino vinculado. Condição publicada: Gás ideal em escoamento permanente, compressão isotérmica internamente reversível; ΔEC/ΔEP desprezíveis.

**Vínculos finais:** [aplicacoes](../../../../modulos/e1-termodinamica.html#aplicacoes). Fontes: `purdue_comp`, `mit_gibbs`.

## 91 — Lei de Fourier: fluxo e taxa

ID: `formula-fourier`. Decisão: ficha_corrigida.

**Expressão:** q″x=−kt dT/dx; Q̇=q″A — A componente tem sinal oposto ao gradiente para kt>0; multiplicação por área normal preserva o sinal.

**Símbolos e unidades:** W/m², W/(m·K), K/m e W coerentes. Falta definir x e distinguir componente assinada de magnitude de fluxo na segunda linha.

**Hipóteses:** Uma dimensão e uniformidade do fluxo na área explícitas; área deve ser normal ao eixo do fluxo. Não há necessidade de impor permanente à lei local.

**Ensino vinculado:** #base-transferencia explica eixo, sinal e exemplo −30 K/m→+150 W/m²; conteúdo adequado.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Condução unidimensional de Fourier, kt>0. Para Q̇=q″xA, fluxo uniforme na área perpendicular a x. Q̇ e q″x são positivos em +x.

**Vínculos finais:** [base-transferencia](../../../../modulos/e1-termodinamica.html#base-transferencia). Fontes: `mit_cond`.

## 92 — Gradiente em uma parede plana

ID: `formula-gradiente`. Decisão: ficha_corrigida.

**Expressão:** dT/dx=(T₂−T₁)/L; Q̇=kt A(T₁−T₂)/L — T₁=60, T₂=40, L=0,1 dá gradiente −200 K/m e Q̇>0. Inverter o eixo inverte ambas as componentes, não o calor físico.

**Símbolos e unidades:** L m, kt W/(m·K), A m² e Q̇ W; T₁/T₂ posicionadas x=0/L corretamente. Acrescentar unidade das temperaturas e gradiente.

**Hipóteses:** Perfil linear, permanente, kt constante, sem geração declarados. “Positivo no sentido 1→2” não nomeia a grandeza; gradiente e Q̇ têm sinais opostos.

**Ensino vinculado:** #base-transferencia ensina o eixo da esquerda para direita, gradiente −200 K/m e Q̇ positivo; suporte real e correto.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Parede plana de área constante, condução unidimensional permanente, kt constante e sem geração interna. x cresce da face 1 para a face 2. Q̇ é positivo no sentido 1→2; dT/dx pode ser negativo.

**Vínculos finais:** [base-transferencia](../../../../modulos/e1-termodinamica.html#base-transferencia). Fontes: `mit_cond`.

## 93 — Convecção: lei de Newton

ID: `formula-newton`. Decisão: ficha_corrigida.

**Expressão:** Q̇=hc A(Ts−T∞) — Q̇=∫A hlocal(Ts−T∞)dA=hc,médio A(Ts−T∞) para diferença uniforme.

**Símbolos e unidades:** hc W/(m²·K), A m² e Q̇ W corretos; Ts/T∞ definidos.

**Hipóteses:** Ts uniforme declarado e sinal superfície→fluido correto. Falta T∞ uniforme e identificar hc como valor uniforme ou média sobre a área.

**Ensino vinculado:** #base-transferencia contém lei de Newton e interpretação do sinal; pode receber a mesma delimitação em uma frase.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Ts e T∞ uniformes na área considerada; hc uniforme ou médio sobre essa área. Q̇ positivo da superfície para o fluido; diferença de temperatura em K ou °C.

**Vínculos finais:** [base-transferencia](../../../../modulos/e1-termodinamica.html#base-transferencia). Fontes: `mit_conv`.

## 94 — Trocador: coeficiente global

ID: `formula-ua`. Decisão: ficha_corrigida.

**Expressão:** Q̇=UA ΔTm; ΔTm=F ΔTlm — Dimensão U A ΔT é W. Para U espacialmente variável, Q̇=∫U ΔT dA; fatorizar um valor arbitrário de U não é identidade geral.

**Símbolos e unidades:** U e A com mesma referência e F adimensional corretos. Faltam significado/unidade de Q̇ e de ΔTlm.

**Hipóteses:** Permanente e fator adequado ao arranjo corretos; explicitar U constante/médio compatível e hipóteses do método LMTD.

**Ensino vinculado:** #base-trocadores ensina UA, referência de área, necessidade de F e exemplo; não define ΔTlm nem hipóteses para usar F.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Trocador estacionário, sem trocas externas relevantes, U aproximadamente constante. Use média logarítmica e fator F válidos para o arranjo e os perfis térmicos; A deve corresponder à referência de U.

**Vínculos finais:** [base-trocadores](../../../../modulos/e1-termodinamica.html#base-trocadores). Fontes: `mit_hx`, `ahtt`.

## 95 — Resistências térmicas por área

ID: `formula-resistencias`. Decisão: ficha_corrigida.

**Expressão:** 1/U=1/hq+L/kt+1/hf+R″dep — Rcond,plana=L/(ktA); U=1/(ARtotal). Em cilindro, integrar dr/(2πrℓkt) produz logaritmo.

**Símbolos e unidades:** Todas as parcelas em m²·K/W. Definir q/f como quente/frio, R″dep como soma dos depósitos, L espessura.

**Hipóteses:** Plano em série e área comum estão declarados. A cautela “tubos exigem conversão entre áreas” é incompleta: a condução cilíndrica tem resistência logarítmica, não apenas L/kt convertido.

**Ensino vinculado:** #base-trocadores contém a soma plana e adverte converter áreas em tubos; mesma ressalva incompleta sobre geometria.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Parede plana em regime permanente, condução 1D, kt constante, sem geração; resistências em série na mesma área. Tubos exigem resistência cilíndrica e áreas próprias; converter a área não torna válida a expressão plana.

**Vínculos finais:** [base-trocadores](../../../../modulos/e1-termodinamica.html#base-trocadores). Fontes: `mit_conv`, `mit_res`, `mit_hx`.

## 96 — Troca líquida por radiação

ID: `formula-radiacao`. Decisão: ficha_corrigida.

**Expressão:** Q̇rad=εσA(Ts⁴−Tamb⁴); σ≈5,67×10⁻⁸ W/(m²·K⁴) — Emissão εσATs⁴ menos absorção εσATamb⁴; se Ts=Tamb, troca líquida nula.

**Símbolos e unidades:** Constante, expoentes e K corretos. ε adimensional e Q̇rad W.

**Hipóteses:** Superfície cinza pequena, entorno grande aproximadamente negro e visão completa com temperaturas uniformes explicitados. Falta convenção de sinal e meio não participante.

**Ensino vinculado:** #base-radiacao-vacuo ensina expressão, limitações de geometria e perdas por outros mecanismos; adequado.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Superfície cinza pequena, uniforme, com visão completa de grande entorno aproximadamente negro e isotérmico; meio intermediário não participante. Q̇rad positivo da superfície para o entorno.

**Vínculos finais:** [base-radiacao-vacuo](../../../../modulos/e1-termodinamica.html#base-radiacao-vacuo). Fontes: `mit_rad`, `mit_view`.

## 97 — Comparar duas emissividades

ID: `formula-razao-radiativa`. Decisão: ficha_mantida.

**Expressão:** Q̇rad,2/Q̇rad,1=ε₂/ε₁ — Cancelar σA(Ts⁴−Tamb⁴), que deve ser não nulo; ε₁ também não pode ser zero.

**Símbolos e unidades:** Razão adimensional, emissividades e perdas identificadas.

**Hipóteses:** Mesmas área, temperaturas, geometria e modelo da ficha96; denominador não nulo explicitado.

**Ensino vinculado:** #base-radiacao-vacuo deriva a razão por cancelamento e alerta contra duas superfícies cinzas comparáveis.

**Resultado:** Mantida após conferência individual da expressão, símbolos/unidades, hipóteses e ensino vinculado. Condição publicada: Mesmo modelo da ficha de radiação; mesmas área, temperaturas e geometria; perda inicial não nula.

**Vínculos finais:** [base-radiacao-vacuo](../../../../modulos/e1-termodinamica.html#base-radiacao-vacuo). Fontes: `mit_rad`, `mit_view`.

## 98 — Dilatação linear livre

ID: `formula-dilatacao`. Decisão: ficha_corrigida.

**Expressão:** ΔL=αL L₀ ΔT; L₂=L₀+ΔL — L₂=L₀e^(αΔT) ⇒ ΔL≈L₀αΔT para |αΔT| pequeno. Não exigir exponencial na ficha: basta nomear a aproximação.

**Símbolos e unidades:** K⁻¹, m e intervalo em K/°C corretos; índices inicial/final merecem definição por extenso.

**Hipóteses:** Livre, aquecimento uniforme e coeficiente quase constante explícitos. Falta afirmar aproximação linear/pequena deformação.

**Ensino vinculado:** #base-dilatacao ensina deslocamento livre e exclui cálculo de tensões, mas não explicita a linearização.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Dilatação livre e aquecimento uniforme. Aproximação linear para |αLΔT|≪1, com coeficiente de dilatação aproximadamente constante na faixa.

**Vínculos finais:** [base-dilatacao](../../../../modulos/e1-termodinamica.html#base-dilatacao). Fontes: `open_expansion`.

## 99 — Geração interna e face exposta

ID: `formula-geracao`. Decisão: ficha_corrigida.

**Expressão:** q‴V=hc Aexp(Ts−T∞); Ts=T∞+q‴V/(hc Aexp) — No permanente, ∫V q‴dV=∫A h(Ts−T∞)dA. Com hipóteses propostas, reduz aos produtos; geração positiva impõe Ts>T∞.

**Símbolos e unidades:** W/m³·m³=W; lado convectivo W; diferença de temperaturas K. q‴ não está definido por nome e falta domínio do denominador.

**Hipóteses:** Permanente, única face exposta, temperatura superficial uniforme, demais faces isoladas e sem outras perdas corretos. Falta geração uniforme ou média volumétrica e hc uniforme/médio.

**Ensino vinculado:** #base-geracao-face ensina balanço, geometria e que o interior pode ter gradiente; evita hipótese desnecessária de bloco isotérmico.

**Resultado:** Correções de condição, símbolos ou vínculo aplicadas; data-busca sincronizada. Condição publicada: Regime permanente; q‴ uniforme ou média no volume; Ts e T∞ uniformes, hc médio na face. Demais faces isoladas, sem radiação ou outras perdas; hc>0 e Aexp>0.

**Vínculos finais:** [base-geracao-face](../../../../modulos/e1-termodinamica.html#base-geracao-face). Fontes: `mit_generation`, `mit_conv`.

## 100 — Volume do bloco e área da face

ID: `formula-geometria`. Decisão: ficha_mantida.

**Expressão:** V=abc; Aface=ab — Conferência geométrica própria: a×b é área da face; extrusão por c gera abc. A fonte térmica apoia a necessidade de separar área/volume, não é citada como origem dessa identidade geométrica.

**Símbolos e unidades:** a,b,c em m, V m³ e A m²; profundidade identificada.

**Hipóteses:** Bloco retangular e face a×b escolhida explicitamente.

**Ensino vinculado:** #base-geracao-face ensina produto abc, área ab e distinção em relação à área total 2(ab+ac+bc).

**Resultado:** Mantida após conferência individual da expressão, símbolos/unidades, hipóteses e ensino vinculado. Condição publicada: Bloco retangular; a profundidade participa do volume, não da área ab.

**Vínculos finais:** [base-geracao-face](../../../../modulos/e1-termodinamica.html#base-geracao-face). Fontes: `mit_generation`.

## Fontes e limites

- `algebra`: Conferência autoral de definições e rearranjos — Diferenças, médias, razões, interpolação afim, soma de capacidades e unidades rederivadas diretamente. Não é uma norma externa nem ensaio experimental.
- `si`: [BIPM, SI Brochure, 9ª edição, versão 4.01 (2026)](https://www.bipm.org/en/publications/si-brochure) — Consulta primária reutilizada de BAN-10: unidades SI, kelvin/Celsius, mol e constantes definidoras. Sem alegar nova inspeção integral nesta rodada.
- `nist_cal`: [NIST SP811, notas 9 e 19](https://www.nist.gov/pml/special-publication-811/nist-guide-si-footnotes) — Texto web: caloria termoquímica = 4,184 J exatamente; litro = dm³. A tabela B.8 não expôs o termo pesquisado; a nota 9 foi efetivamente lida.
- `ideal`: [OpenStax University Physics 2, §2.1](https://openstax.org/books/university-physics-volume-2/pages/2-1-molecular-model-of-an-ideal-gas) — Equação do gás ideal e bases por molécula/mol; pressão e temperatura absolutas.
- `kinetic`: [OpenStax University Physics 2, §2.2, equação 2.6](https://openstax.org/books/university-physics-volume-2/pages/2-2-pressure-temperature-and-rms-speed) — Conferida a energia cinética translacional média 3kBT/2 e distinção da energia interna de gás molecular.
- `firstlaw`: [MIT Thermodynamics §2.4, primeira lei](https://web.mit.edu/16.unified/www/SPRING/thermodynamics/notes/node14.html) — Balanço total fechado, Q entrando e W saindo; a redução para energia interna depende das variações mecânicas. Derivações locais de calor a p constante e de ciclo usam esse balanço.
- `ideal_energy`: [MIT Thermodynamics §2.4.1](https://web.mit.edu/16.unified/www/SPRING/thermodynamics/notes/node17.html) — du=cv(T)dT, dh=cp(T)dT, integração, aproximação de capacidades constantes e cp−cv=R para gás ideal.
- `calorimetry`: [OpenStax University Physics 2, §1.4](https://openstax.org/books/university-physics-volume-2/pages/1-4-heat-transfer-specific-heat-and-calorimetry) — Capacidade térmica e calorimetria sensível; balanços com recipiente rederivados. O valor de caloria dessa seção não é usado para a caloria termoquímica da ficha 03.
- `phase`: [OpenStax University Physics 2, §1.5](https://openstax.org/books/university-physics-volume-2/pages/1-5-phase-changes) — Calor de mudança de fase e massa transformada. Limites de pressão/trabalho são estabelecidos pela primeira lei; a descrição informal de supercrítico dessa página não foi importada.
- `quality`: [ASHRAE Handbook 2025, capítulo 2, §1.2](https://handbook.ashrae.org/Handbooks/F25/IP/f25_ch02/f25_ch02_ip.aspx) — Texto sobre qualidade como fração mássica e dependência p/T em saturação pura. Média de propriedades específicas deriva da aditividade e das massas; não se generaliza a p/T ou misturas zeotrópicas.
- `mechanics_k`: [OpenStax University Physics 1, §7.2](https://openstax.org/books/university-physics-volume-1/pages/7-2-kinetic-energy) — Energia cinética translacional clássica, referencial e unidade J.
- `mechanics_p`: [OpenStax University Physics 1, §8.1](https://openstax.org/books/university-physics-volume-1/pages/8-1-potential-energy-of-a-system) — Diferença de energia potencial gravitacional mgΔz em campo uniforme; no curso usa-se EP para distingui-la da energia interna U.
- `humidity`: [ASHRAE Handbook 2021, capítulo 1, §§5–6, equações 12/13/23](https://handbook.ashrae.org/Handbooks/F21/SI/F21_Ch01/F21_Ch01_si.aspx) — Texto distingue saturação real, fator de intensificação e aproximação de gases perfeitos. Apoio visual NIST Bell/Lemmon/Harvey e pinpoint estão no relatório do coordenador.
- `coord_co2`: Apoio documental do coordenador: Persily/deJonge 2017 e NIST TN2213 — Relatório lido e integrado; URLs, páginas, PDFs e capturas reais do coordenador no pacote. Balanço usa frações e geração volumétrica coerente, sem adotar limites normativos.
- `mit_cv`: [MIT, Thermodynamics and Propulsion §2.5](https://web.mit.edu/16.unified/OldFiles/www/SPRING/thermodynamics/notes/node18.html) — Conferidos balanço de volume de controle, energia cinética e §2.5.4.1: a integração do tanque declara entalpia de entrada constante.
- `nist_co2`: [NIST TN 2213, §2.1, pp. impressas 2–3 / PDF 8–9](https://nvlpubs.nist.gov/nistpubs/TechnicalNotes/NIST.TN.2213.pdf) — Conferidos balanço de zona única, mesma vazão volumétrica de entrada/saída, ausência de diferenças espaciais e razão Q/V. A ficha usa fração, não o valor numérico em ppm.
- `doe_pump`: [DOE, Pumps Test Procedure Final Rule, equação (10), p. 103](https://www.energy.gov/sites/default/files/2015/12/f27/Pumps%20Test%20Procedure%20Final%20Rule.pdf) — Expressão primária Pu=ρQHg com H definido como carga total da bomba; consulta ao trecho indexado da publicação.
- `doe_eff`: [DOE, Improving Pumping System Performance](https://www.energy.gov/sites/default/files/2014/05/f16/pump.pdf) — Conferida definição de eficiência da bomba como potência transmitida ao líquido dividida pela potência no eixo; não pela potência elétrica.
- `open_cop`: [OpenStax University Physics 2 §4.3](https://openstax.org/books/university-physics-volume-2/pages/4-3-refrigerators-and-heat-pumps) — Conferidos COP de refrigeração e aquecimento e balanço W=QH−QL, com trabalho fornecido ao ciclo.
- `open_carnot`: [OpenStax University Physics 2 §4.5](https://openstax.org/books/university-physics-volume-2/pages/4-5-the-carnot-cycle) — Conferidos limite de Carnot e igualdade entre ciclos reversíveis ligados aos mesmos dois reservatórios.
- `mit_entropy`: [MIT 2.60J, Lecture 2, slides 7–8](https://ocw.mit.edu/courses/2-60j-fundamentals-of-advanced-energy-conversion-spring-2020/54a791b898a31befeea178f796efcd9c_MIT2_60s20_lec2.pdf) — Conferidos balanços de entropia de massa de controle e volume de controle, distinguindo transferência e geração.
- `open_entropy`: [OpenStax University Physics 2 §4.6](https://openstax.org/books/university-physics-volume-2/pages/4-6-entropy) — Conferida definição da variação de entropia por trajetória reversível e temperatura absoluta; a integração é pelo caminho.
- `mit_gibbs`: [MIT Thermodynamics §5.3](https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node39.html) — Conferidas du=Tds−pdv e dh=Tds+vdp como identidades de propriedades; calor e trabalho reais exigem hipóteses adicionais.
- `mit_ideal_s`: [MIT Thermodynamics §5.4](https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node40.html) — Conferida forma diferencial ds=cv dT/T+R dv/v e integração com cv constante. Forma T,p e relações isentrópicas conferidas por substituição pv=RT e cp=cv+R.
- `purdue_ref`: [Purdue, C. Wassgren, §3.8.3, pp. 307–310](https://engineering.purdue.edu/~wassgren/teaching/ME20000/NotesAndReading/Lec35_Reading_Wassgren.pdf) — Conferidos COP de compressão de vapor, balanços por entalpia e eficiência isentrópica do compressor com mesma pressão final.
- `mit_lost`: [MIT Thermodynamics §6.6](https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node49.html) — Conferida relação entre trabalho perdido e geração total de entropia sob ambiente de referência a T0 constante.
- `wash_gibbs`: [University of Washington, Gibbs Energy Minimization, p. 3](https://courses.washington.edu/mengr524/sp15/handouts/gibbs_min.pdf) — Conferidas definição de μ como derivada de G a T,p e demais quantidades fixas e condição de mínimo de G. A diferença entre fases resulta da conservação dn_f=−dn_g.
- `mit_phase`: [MIT Materials Science, Lecture 14](https://wikis.mit.edu/confluence/display/MSEDG/Lecture%2B14) — Conferida transferência entre duas fases a T,p fixas e igualdade do potencial químico do mesmo componente móvel.
- `mit_rankine`: [MIT Thermodynamics §8.5](https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node65.html) — Conferidos equipamentos e processos do ciclo Rankine; a numeração da ficha é própria e os balanços foram rederivados da primeira lei estacionária.
- `mit_brayton`: [MIT Thermodynamics §3.7](https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node28.html) — Conferidos quatro processos, trabalho líquido e redução do rendimento por relações isentrópicas para gás ideal com calores constantes.
- `mit_otto`: [MIT Thermodynamics §3.5.1](https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node26.html) — Conferida dedução η=1−r^(1−k) com calor a volume constante e compressão/expansão isentrópicas.
- `mit_diesel`: [MIT Thermodynamics §3.6](https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node27.html) — Conferida eficiência por temperaturas; expressão da ficha em r e rc rederivada usando adição isobárica e relações isentrópicas.
- `purdue_comp`: [Purdue ME418, Chapter SM6, pp. SM6.2–SM6.7](https://www.purdue.edu/freeform/me418/wp-content/uploads/sites/30/2024/09/Chapter-SM-6-Ref-Compressors.pdf) — Conferidos referência de sucção, definição de admissão por deslocamento e expressão politrópica com fator n/(n−1); não se confunde com trabalho de uma única etapa fechada.
- `tamu_two`: [C. E. Pelli, Texas A&M, The Energy Efficiency of Dehumidified Two-Stage Air Compression, §§4.2–4.4, pp. 17–20](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/720949b2-1bd4-4884-9025-d39f685f11a5/content) — Conferido modelo ideal de dois estágios, intercooling isobárico até temperatura inicial e média geométrica minimizadora; extensão a eficiências iguais e constantes rederivada neste apoio.
- `mit_cond`: [MIT Thermodynamics §16.3](https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node117.html) — Conferidos Fourier com sinal negativo, parede plana de área constante, perfil linear e gradiente (T2−T1)/L.
- `mit_conv`: [MIT Thermodynamics §17.2](https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node123.html) — Conferidos q″=h(Ts−T∞) e resistências de convecção/condução em série.
- `mit_res`: [MIT Thermodynamics §16.4](https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node118.html) — Conferidas resistência L/(kA), soma em série e conversão para resistência multiplicada pela área comum.
- `mit_hx`: [MIT Thermodynamics §18.5](https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node131.html) — Conferidos coeficiente global com área declarada e diferença média logarítmica deduzida para hipóteses do trocador.
- `ahtt`: [J. H. Lienhard IV/V, A Heat Transfer Textbook, 6ª edição, §3.2](https://ahtt.mit.edu/wp-content/uploads/2024/04/AHTTv600.pdf) — Trecho primário indexado: método LMTD com U razoavelmente constante e fator F para arranjos apropriados; não valida qualquer média arbitrária.
- `mit_rad`: [MIT Thermodynamics §§19.2 e 19.4](https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node135.html) — Conferidas emissividade/absortividade de corpo cinza; geometria e fator de vista tratados no §19.4. Derivação do balanço emissão menos absorção feita neste apoio.
- `mit_view`: [MIT Thermodynamics §19.4](https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node137.html) — Conferidos fator de vista e troca líquida entre superfícies; encerramento completo permite F=1 para a superfície interna que não se vê.
- `open_expansion`: [OpenStax University Physics 2 §1.3](https://openstax.org/books/university-physics-volume-2/pages/1-3-thermal-expansion) — Conferida distinção entre dL/dT=αL e aproximação linear para pequenas variações relativas.
- `mit_generation`: [MIT Thermodynamics §18.1](https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node127.html) — Conferida geração volumétrica em W/m³ e balanço estacionário de energia. Caso de única face convectiva foi rederivado diretamente.
- `purdue_turb`: [Purdue ME200, HW36, turbina de referência](https://engineering.purdue.edu/ME200/files/homework/HW36/ME200-Spring2020-HW36-web.html) — Conferidos modelo estacionário adiabático, EC/EP desprezíveis e relação h_out=h_in−ηt(h_in−h_out,s), equivalente à ficha.

- Não fecha FOR-02, FOR-03, ENE, CIC ou outros IDs. Não acrescenta novas fichas ou certificação de nível do curso.
- Números das verificações são casos autorais de verificação, não dados experimentais ou atividades novas do aluno.
- Fontes web foram lidas nos trechos indicados; as consultas do apoio e do coordenador estão atribuídas. Não se afirma inspeção integral dos PDFs nem consulta independente duplicada pelo Corretor.
- O resumo do inventário de questões permanece idêntico porque seus 197 registros não mudaram. Somente fonte.sha256 e fonte.snapshot do JSON canônico mudaram em razão da aula.
