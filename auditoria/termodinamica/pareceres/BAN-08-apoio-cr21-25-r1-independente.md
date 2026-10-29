# BAN-08 — apoio científico independente CR21–CR25

Data 29/10/2026; autora dos cálculos e revisora: agente automatizado `/root/auditor_ban08_novo`. Exame parcial sem cegamento, sem aprovação global de BAN-08 nem liberação do próximo ID. Produto/controle não alterados. Enunciados históricos, dados e análise autoral na versão `modulos/e1-termodinamica.html`, SHA-256 `80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0`. Hashes individuais correspondem ao trecho bruto UTF-8 `<article>...</article>`. Fontes documentais de provas e gabaritos são as vinculadas em cada artigo e no inventário; a chave é evidência documental, não prova científica. Não fiz nova conferência documental integral dos originais nesta análise. CR24 é estudo crítico sem pontuação; os outros são pontuáveis.

Fontes dos modelos, acessadas em 29/10/2026: OpenStax, University Physics v.2 §2.1, https://openstax.org/books/university-physics-volume-2/pages/2-1-molecular-model-of-an-ideal-gas, para pV=nRT; NIST WTT density gas, https://wtt-pro.nist.gov/wtt-pro/help/properties/density_gas.html, para Z e expansão virial; BIPM, SI Brochure 9ª ed. V3.01 (2024), p. 133, conforme referência do artigo, índice https://www.bipm.org/en/publications/si-brochure/, conversão Celsius–kelvin. Dados do comando não são substituídos por tabelas externas.

## CR21 — C

Hash `5e112105b6213109cbaf04f2883ae27052a8c9027ed9d808a0fcd627a326784b`; C/E; base `#base-gas-modelo`. Para quantidade n e composição fixas, pV=nRT implica p=nRT/V; dadas duas entre p, V e T positivas, a terceira decorre do modelo. A frase original menciona três variáveis usuais e não diz que são independentes. Chave C compatível. O número três é contagem exata; não há grandezas medidas ou tolerância de exibição: não aplicável.

## CR22 — C

Hash `a4cb5f18bafa792df4cdc4f632c585b8b49b63f20d7e719b36131dc44d34c944`; C/E; bases `#base-leitura-matematica`, `#base-gas-energia`, `#base-gas-modelo`. Com p absoluta, T absoluta, Z=pV/(nRT), adimensional; rearranjo pV=ZnRT. Para modelo ideal Z=1 exatamente; Z significativamente afastado de 1 demonstra desvio da relação ideal de estado, razão suficiente para C. Z≈1 num único estado não prova idealidade universal nem quantifica outros desvios. O número 1 é limite exato do modelo; não há dados para tolerância ou desvio percentual, não aplicável.

## CR23 — E

Hash `5be283e9eeaad31c39004231ee391654e3f476aaede45b5b81f74163628c3405`; C/E; `#base-gas-modelo`. Figura associada `assets/questoes-reais-e1/figura-9d164690a624.png`, SHA-256 verificado `9d164690a6243cb31b9ea0f734b9a85ad4c6570398b9d5ef9278e4f44332bcc2`: esquema de recipiente isolado com gás e vácuo, sem escala ou números usados no julgamento. NIST relaciona Z=1+B/v_m+C/v_m²+…, logo pressão elevada não assegura que desvios desapareçam; temperatura elevada isoladamente não estabelece que a combinação alta pressão e alta temperatura se aproxima do ideal para todo gás. Chave E compatível, sem limiar ou grandezas para atribuir tolerância numérica. Não se prova que todo gás a alta pressão tenha um desvio específico.

## CR24 — estudo crítico, chave documental E, sem nota

Hash `7263887786f48bf00b02289fba4dcccfda7d655546d4c37da44e14a2d01ed438`; C/E sem pontuação; bases `#base-leitura-matematica`, `#base-gas-modelo`, `#base-absolutas`. Identidade conferida: prova local `downloads/termodinamica/provas/2025-01-19_trf6-analista-engenharia-mecanica_prova.pdf` hash `74a764fdb11ca13d527674c39206f44cbd4b5b1392cdee1f8bce9d8016ac4d79` e chave `downloads/termodinamica/gabaritos/2025-01-19_trf6-analista-engenharia-mecanica_gabarito.pdf` hash `0b5abca04a6892f48c7541018106445f6619f5f5863e061f631f0249899795e3`; isto não é nova transcrição da prova. Leitura literal: razão p_gás/p_água=(nR·373,15/V)/p_água, e n/V não foi dado: indeterminada ainda que se conheça a pressão da água. Não se aplica a razão de temperaturas a pressões de substâncias diferentes.

Na hipótese editorial de mesma amostra ideal com n e V fixos, a conversão T/K=t/°C+273,15 dá 100 °C→373,15 K e 0,01 °C→273,16 K; p2/p1=37315/27316≈1,36604920193, exibido 1,366, diferença ≈0,0000492, abaixo de 0,0005 (meia unidade da terceira casa, arredondamento ao mais próximo, empate para cima). É diferente de 1; E é coerente apenas nessa leitura condicionada e não transforma a redação literal em unívoca. Os valores originais são nominais; ponto triplo não define o kelvin atual. Critério de autocorreção exige distinguir pressões e declarar a hipótese, não pontuar a letra.

## CR25 — D

Hash `ad3f5a9cb6c50e2cacacb42b7e8d3a14a6c8cb13320c1048aea23cc599d50ed6`; múltipla escolha; bases `#base-leitura-matematica`, `#base-gas-modelo`. Gás ideal com n fixo: T2/T1=(p2/p1)(V2/V1)=2×1,5=3, com T em kelvin. Tfinal=300% do inicial, aumento (3−1)×100=200%; valores publicados todos exatos nas razões dadas e diferenças zero. A corresponde a 0,5T1; B a T1; C a 1,5T1; E a 4T1; somente D diz aumento 200%. Igualdade e comparação exatas dos fatores, não incerteza de medição. Percentual não se aplica diretamente a valores Celsius.

Nenhuma divergência numérica localizada. Este apoio não implica teste com estudantes, alteração de documentos originais ou aprovação do banco inteiro.
