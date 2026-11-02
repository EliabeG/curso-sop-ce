# Inventário individual do banco de Termodinâmica — BAN-02 r3 + FUN-01 r2 + FUN-02 r1 + FON-09 r1 + BAN-10 r2 + FON-01 r1 + FON-02 r1 + BAN-07 r1

Data: 28/10/2026. Fonte canônica: [inventario-questoes.json](inventario-questoes.json). Cadastro e manutenção: [LEIA-ME.md](LEIA-ME.md).

Histórico: os 190 registros originais e os quatro registros FUN-01 foram preservados na inclusão FUN-02. A revisão BAN-10 atualiza somente os 12 casos explicitados ao final; os 185 demais registros permanecem idênticos à base FON-09. Foram acrescidos três problemas abertos FUN-02, totalizando 197 registros preenchidos por leitura individual. Este resumo apresenta nível estimado, competência de apoio, etapas e justificativa; o JSON contém também pré-requisitos, origem e identificadores, formato, hipóteses explícitas/implícitas, limites, exposição com evidências e encaminhamentos individuais. Nenhum registro atesta domínio integral de C01–C10 ou dificuldade medida com estudantes. A conferência documental restrita a CR68 em FON-09 está explicitada ao final; não equivale à revisão geral dos gabaritos.

## Método e alcance

Uma etapa é uma decisão, inferência ou transformação de modelo identificável. Não contamos separadamente somas, multiplicações, conversões mecânicas ou cada operação de uma fórmula. Juízos independentes sobre conceitos distintos podem constituir mais de uma etapa sem elevar automaticamente o nível. Reconhecimento e aplicação direta com dados/modelo fornecidos são iniciantes; integração de relações distintas ou leitura de diagrama com balanço pode ser intermediária. Nenhum dos 190 itens originais foi classificado como avançado. Os problemas FUN-01 e FUN-02 recebem classificação individual justificada abaixo; o formato aberto não basta para elevar nível.

As estimativas pertencem ao item completo, não ao título do assunto. AV37 fornece Gouy–Stodola, AV40 fornece a identidade termodinâmica, AV57 fornece inclusive o fator da potência, e AV53 pede apenas porcentagem de calor: esses itens permanecem iniciantes. Na classificação histórica BAN-02, CR09, CR24 e CR79 eram iniciantes pela marcação condicionada. Em BAN-10, nove itens passaram a estudo crítico com roteiro de justificativa sem nota; as notas já orientam a leitura, portanto não se afirma descoberta independente. CR79 passa a intermediário pela demanda nova de construir dois casos contrastantes. As linhas atuais abaixo representam os roteiros relidos, não apenas a antiga marcação. A distribuição não é nota do curso e não atende sozinha ao BAN-05.

CR01–80 e AV01–80 foram classificados pelo Corretor. Q01–30 receberam insumo do coordenador, revisado contra os artigos pelo Corretor; Q10 foi recalibrado para iniciante e Q15 condensado em uma etapa. Na rodada 2, todos os 80 pré-requisitos AV foram revistos individualmente e CR09/24/79 tiveram nível e demanda ajustados ao comando atual. Apoio técnico separado produziu contrato e validador; não atuou como Auditor.

| Banco | Total | Iniciante | Intermediário | Avançado |
|---|---:|---:|---:|---:|
| inicial | 30 | 27 | 3 | 0 |
| real | 80 | 70 | 10 | 0 |
| avalia | 80 | 72 | 8 | 0 |
| aberto (FUN-01) | 4 | 0 | 2 | 2 |
| aberto (FUN-02) | 3 | 0 | 1 | 2 |
| **Total** | **197** | **169** | **24** | **4** |

São 73 itens C/E, 117 de cinco alternativas e sete respostas abertas. Há sete PNGs distintos em 16 artigos, três pacotes JSON de dados, um módulo de cálculo referenciado diretamente por P2 FUN-02 e um SVG externo na solução de P1 FUN-02; SVGs internos pertencem ao hash do artigo. A figura é necessária para extrair a geometria em CR80 e apresenta o vácuo em CR33. Em AV80 e AV33 as mesmas informações estão escritas no texto. Diagramas e imagens contextuais não tornam o raciocínio automaticamente avançado.

## Exposição e pendências conhecidas

O registro compara os 80 pares CR/AV e relações locais específicas dos itens Q. Toda AV declara uma CR de origem; essa relação editorial foi separada da relação cognitiva efetivamente observada. CR25/AV25 repetem a transformação p×2 e V×1,5. CR28/AV28 repetem 100 J, 200 cal, 350 J e 4,2 J/cal. CR17/AV17 repetem a referência de 50% de umidade relativa. Outros pares alteram dados, método ou comando e estão descritos individualmente. Q26/Q27/Q29 retomam exemplos da aula; Q19/Q28 repetem procedimento com dados diferentes. Esses casos não podem ser anunciados como avaliações independentes.

O histórico do estudante é desconhecido em todos os casos. Para seis itens Q, nenhuma relação específica foi afirmada neste recorte; isso não significa ineditismo. A lista de relações é evidência local, não busca universal de todas as combinações possíveis nem auditoria de equivalência de avaliações.

- CR09: unidade SI versus unidade de base da temperatura termodinâmica; °C também é SI.
- CR24: leitura literal não determina a razão. A razão 373,15/273,16 depende do mesmo gás, mesma quantidade/volume e ponto triplo apenas como referência térmica.
- CR55: expressão “pressão isentrópica” já confirmada no documento oficial em BAN-10; manutenção motivada abaixo.
- CR68: densidade e tabela defeituosas foram preservadas e sinalizadas; não entram no juízo de emissividade nem devem ser reutilizadas para contas.
- CR79: vácuo não demonstra predominância radiativa sem dados de superfícies e contatos.

Na entrega histórica BAN-02, esses encaminhamentos não encerraram as revisões. FON-09 já recebeu aceite próprio. A atualização localizada BAN-10 e as conferências dos 12 casos estão explicitadas ao final; não se declara conferência oficial global ou aceite de BAN-07/BAN-08/FON-01.

## Ajustes da rodada 2

- R1-A: os metadados de AV45 e suas relações em Q16/CR45 agora usam calor recebido de 1.000 kJ e rejeição mínima de 500 kJ. CR42, que usa joules, foi preservada.
- R1-B: CR09/24/79 agora registram uma etapa iniciante de reconhecimento ou aplicação direta na leitura condicionada. A insuficiência da redação permanece nos campos de hipóteses, limites e revisão, sem ser promovida a capacidade avaliada.
- R1-C: as 80 listas AV foram reescritas pela tarefa efetiva. Foram removidas conversões, modelos e conteúdos que o comando não exige; incluídos os requisitos omitidos de entropia/segunda lei, porcentagem, Rankine e balanço cíclico.
- R1-D: AV57 registra expressamente Brayton ideal e calores específicos constantes, além da fórmula e fator já fornecidos.

As diferenças integrais e a revisão de pré-requisitos estão em [delta r1→r2](../evidencias/BAN-02/delta-r1-r2.json) e [revisão das 80 AV](../evidencias/BAN-02/pre-requisitos-r2.json). O pacote da rodada 1 foi preservado.

## Ajuste da rodada 3

AV20 recebeu somente o pré-requisito de distinguir extrapolação matemática do modelo ideal e domínio físico de um gás real, incluindo possível mudança de fase ou desvio da idealidade antes de 0 K. As alternativas D/E exigem essa distinção. Os dois requisitos matemáticos, as demais 79 listas AV, os níveis, as etapas e as estatísticas foram preservados. A revisão das 80 listas da r2 permanece histórica; o [delta r2→r3](../evidencias/BAN-02/delta-r2-r3.json) registra o único complemento atual.

## Questões iniciais

Todos os vínculos abaixo são **apoio fundamental** às competências, com alcance limitado explicitado no JSON.

| Item e fonte | Competências | Nível estimado | Etapas | Justificativa do raciocínio |
|---|---|---|---:|---|
| [Questão 1](../../../modulos/e1-termodinamica.html#q-e1-01) | C01 | iniciante | 1 | Reconhece a classe de fronteira a partir de vedação e trocas já declaradas; não escolhe um modelo. |
| [Questão 2](../../../modulos/e1-termodinamica.html#q-e1-02) | C02, C08 | iniciante | 1 | Uma conversão de referência de pressão, com ambas as parcelas fornecidas. |
| [Questão 3](../../../modulos/e1-termodinamica.html#q-e1-03) | C02 | iniciante | 1 | Pede apenas reconhecer duas propriedades intensivas. |
| [Questão 4](../../../modulos/e1-termodinamica.html#q-e1-04) | C02 | iniciante | 1 | Região e três entalpias já são dadas; basta isolar x, sem buscar tabela. |
| [Questão 5](../../../modulos/e1-termodinamica.html#q-e1-05) | C02 | iniciante | 1 | Reconhece o domínio de definição do título entre afirmações prontas. |
| [Questão 6](../../../modulos/e1-termodinamica.html#q-e1-06) | C02, C08 | iniciante | 1 | Modelo, massa, volume, temperatura e R fornecidos; substituição única na equação de estado. |
| [Questão 7](../../../modulos/e1-termodinamica.html#q-e1-07) | C03 | iniciante | 1 | Balanço fechado com termos negligenciados já indicados e somente uma diferença de energias. |
| [Questão 8](../../../modulos/e1-termodinamica.html#q-e1-08) | C03, C08 | iniciante | 1 | Trajetória quase estática e pressão constante explicitadas; aplica W=pΔV. |
| [Questão 9](../../../modulos/e1-termodinamica.html#q-e1-09) | C03, C08 | intermediario | 2 | Integra leitura gráfica e sinal de uma integral de caminho, ainda em geometria retangular elementar. |
| [Questão 10](../../../modulos/e1-termodinamica.html#q-e1-10) | C03 | iniciante | 1 | Todas as hipóteses de redução do balanço estão fornecidas; reconhece diretamente a condição isoentálpica, sem escolher modelo ou obter propriedades. |
| [Questão 11](../../../modulos/e1-termodinamica.html#q-e1-11) | C03, C08 | iniciante | 1 | Entalpias, vazão e simplificações são fornecidas; cálculo direto de potência. |
| [Questão 12](../../../modulos/e1-termodinamica.html#q-e1-12) | C03, C02 | iniciante | 1 | Aplicação de vΔp com volume e aumento de pressão dados e sinal já delimitado. |
| [Questão 13](../../../modulos/e1-termodinamica.html#q-e1-13) | C02, C03 | iniciante | 3 | Três reconhecimentos conceituais independentes; número de afirmações não cria modelagem avançada. |
| [Questão 14](../../../modulos/e1-termodinamica.html#q-e1-14) | C04, C09 | iniciante | 1 | Escolhe o dispositivo permitido por enunciado da segunda lei em alternativas explícitas. |
| [Questão 15](../../../modulos/e1-termodinamica.html#q-e1-15) | C03, C06 | iniciante | 1 | Aplica uma relação de eficiência com calor recebido e rejeitado dados; a subtração e a divisão não são decisões intelectuais independentes. |
| [Questão 16](../../../modulos/e1-termodinamica.html#q-e1-16) | C04, C06 | iniciante | 1 | Fontes em kelvin e reversibilidade já declaradas; aplica uma expressão conhecida. |
| [Questão 17](../../../modulos/e1-termodinamica.html#q-e1-17) | C03, C06 | iniciante | 2 | Solicita dois cálculos diretos com calor e trabalho informados, sem modelagem de estados. |
| [Questão 18](../../../modulos/e1-termodinamica.html#q-e1-18) | C04 | iniciante | 3 | Três juízos conceituais, sem calcular propriedades ou geração. |
| [Questão 19](../../../modulos/e1-termodinamica.html#q-e1-19) | C06 | iniciante | 1 | As duas quedas já estão prontas; basta escolher a ordem da razão. |
| [Questão 20](../../../modulos/e1-termodinamica.html#q-e1-20) | C06 | iniciante | 1 | Reconhece a ordem dos quatro equipamentos. |
| [Questão 21](../../../modulos/e1-termodinamica.html#q-e1-21) | C06 | iniciante | 1 | Contrasta duas definições de ciclo, sem derivação nem cálculo. |
| [Questão 22](../../../modulos/e1-termodinamica.html#q-e1-22) | C06, C03 | iniciante | 1 | Reconhece efeito qualitativo do intercooling sob modelo já ensinado; não otimiza nem calcula estágios. |
| [Questão 23](../../../modulos/e1-termodinamica.html#q-e1-23) | C03, C06 | intermediario | 2 | Relaciona estados a dois componentes e combina os respectivos balanços; propriedades continuam totalmente fornecidas. |
| [Questão 24](../../../modulos/e1-termodinamica.html#q-e1-24) | C01, C06 | iniciante | 1 | Pergunta factual sobre qual corrente passa nos tubos. |
| [Questão 25](../../../modulos/e1-termodinamica.html#q-e1-25) | C01, C03 | iniciante | 1 | A proposição incorreta é uma distinção conceitual entre tempo e espaço, sem cálculo. |
| [Questão 26](../../../modulos/e1-termodinamica.html#q-e1-26) | C02, C08 | iniciante | 1 | Uma interpolação com pontos e valor-alvo fornecidos; repete o exemplo disponível. |
| [Questão 27](../../../modulos/e1-termodinamica.html#q-e1-27) | C03, C06 | iniciante | 1 | O enunciado já fornece razões iguais; resolve a relação algébrica, sem demonstrar o mínimo. |
| [Questão 28](../../../modulos/e1-termodinamica.html#q-e1-28) | C06 | iniciante | 1 | Escolhe e aplica razão de diferenças de entalpia já dadas; dispensa obter estados. |
| [Questão 29](../../../modulos/e1-termodinamica.html#q-e1-29) | C01, C04 | intermediario | 2 | Reúne duas correntes e o balanço do conjunto; a prática repete os dados do exemplo. |
| [Questão 30](../../../modulos/e1-termodinamica.html#q-e1-30) | C02, C04, C09 | iniciante | 1 | Reconhecimento da afirmação falsa sobre válvulas entre conceitos já expostos, sem modelagem independente. |

## Questões reais atribuídas

Todos os vínculos abaixo são **apoio fundamental** às competências, com alcance limitado explicitado no JSON.

| Item e fonte | Competências | Nível estimado | Etapas | Justificativa do raciocínio |
|---|---|---|---:|---|
| [01. Quantidade de matéria](../../../modulos/e1-termodinamica.html#cr-e1-01) | C02 | iniciante | 1 | O julgamento usa a definição de intensividade sem cálculo ou escolha de modelo. |
| [02. Estado e caminho](../../../modulos/e1-termodinamica.html#cr-e1-02) | C02, C03 | iniciante | 1 | Basta confrontar a afirmação com a distinção entre propriedades e transferências. |
| [03. Movimento molecular](../../../modulos/e1-termodinamica.html#cr-e1-03) | C02 | iniciante | 1 | É reconhecimento conceitual de movimento molecular, sem modelo quantitativo. |
| [04. Líquido quase incompressível](../../../modulos/e1-termodinamica.html#cr-e1-04) | C02 | iniciante | 3 | Reconhece unidades e condições de uma comparação qualitativa por roteiro que já indica a omissão; não precisa obter propriedades, testar uma faixa ou construir um modelo novo. Estudo guiado sem pontuação: a nota inicial já revela a ressalva central, e a análise oferece autocorreção; não mede descoberta independente nem autonomia avançada. |
| [05. Unidades fundamentais](../../../modulos/e1-termodinamica.html#cr-e1-05) | C08 | iniciante | 1 | O item exige identificar unidades trocadas numa lista, não análise metrológica. |
| [06. Conversão de escalas](../../../modulos/e1-termodinamica.html#cr-e1-06) | C08 | iniciante | 1 | A hipótese linear é explicitada em suplemento editorial do curso; basta reconhecer TX=a+bTY no modelo delimitado. |
| [07. Bourdon ou termômetro?](../../../modulos/e1-termodinamica.html#cr-e1-07) | C08 | iniciante | 1 | Identifica atribuição incorreta do princípio de um instrumento. |
| [08. Faixa de um sensor](../../../modulos/e1-termodinamica.html#cr-e1-08) | C08 | iniciante | 1 | A definição de span leva a uma soma com dados fornecidos. |
| [09. Unidade de temperatura](../../../modulos/e1-termodinamica.html#cr-e1-09) | C08 | iniciante | 3 | Distingue grandezas/unidades e localiza uma restrição previamente apontada na nota; a justificativa agora é solicitada, mas não exige inferência independente da ambiguidade. Estudo guiado sem pontuação: a nota inicial já revela a ressalva central, e a análise oferece autocorreção; não mede descoberta independente nem autonomia avançada. |
| [10. Massa específica](../../../modulos/e1-termodinamica.html#cr-e1-10) | C02 | iniciante | 1 | A independência da quantidade resulta diretamente da razão m/V em amostra homogênea. |
| [11. Unidade termodinâmica](../../../modulos/e1-termodinamica.html#cr-e1-11) | C08 | iniciante | 1 | Recupera a unidade adequada entre cinco nomes conhecidos. |
| [12. Identificação das quatro leis](../../../modulos/e1-termodinamica.html#cr-e1-12) | C03, C04 | iniciante | 1 | Exige cotejo conceitual de quatro afirmações, sem construir balanços. |
| [13. Energia interna do gás ideal](../../../modulos/e1-termodinamica.html#cr-e1-13) | C02 | iniciante | 1 | A propriedade funcional já pertence ao modelo explicitado; não há cálculo. |
| [14. Ocupação do recipiente](../../../modulos/e1-termodinamica.html#cr-e1-14) | C02 | iniciante | 1 | É reconhecimento do comportamento usual de gases. |
| [15. Colisões moleculares](../../../modulos/e1-termodinamica.html#cr-e1-15) | C02 | iniciante | 1 | O julgamento recupera uma hipótese do modelo, sem balanço microscópico. |
| [16. Desumidificador: pressão parcial](../../../modulos/e1-termodinamica.html#cr-e1-16) | C07 | iniciante | 1 | A razão resulta diretamente das umidades dadas, sem determinar vazão ou composição. |
| [17. Significado de 50% de umidade](../../../modulos/e1-termodinamica.html#cr-e1-17) | C07 | iniciante | 1 | O item verifica significado de umidade relativa, não cálculo de mistura completa. |
| [18. Aumento de temperatura](../../../modulos/e1-termodinamica.html#cr-e1-18) | C02 | iniciante | 1 | Uma proporção do produto pV permite rejeitar a triplicação simultânea. |
| [19. Pressão pela equação de estado](../../../modulos/e1-termodinamica.html#cr-e1-19) | C02 | iniciante | 1 | É substituição direta da equação de estado com comparação final de um limiar. |
| [20. Extrapolação ao zero absoluto](../../../modulos/e1-termodinamica.html#cr-e1-20) | C02, C09 | iniciante | 1 | O item exige julgar uma extrapolação qualitativa e não calcular estados de gás real. |
| [21. Variáveis do gás](../../../modulos/e1-termodinamica.html#cr-e1-21) | C02 | iniciante | 1 | Reconhece variáveis de estado sem resolver um estado desconhecido. |
| [22. Fator de compressibilidade](../../../modulos/e1-termodinamica.html#cr-e1-22) | C02, C07 | iniciante | 1 | Julga a definição de um indicador já nomeado. |
| [23. Condições para idealidade](../../../modulos/e1-termodinamica.html#cr-e1-23) | C02, C09 | iniciante | 1 | Identifica a condição qualitativa errada sem determinar propriedades reais. |
| [24. Termômetro de gás](../../../modulos/e1-termodinamica.html#cr-e1-24) | C02 | iniciante | 3 | Aplica álgebra curta do gás ideal e compara duas leituras já indicadas; o roteiro solicita a crítica de suficiência, mas fornece o contraste central e a razão térmica. Estudo guiado sem pontuação: a nota inicial já revela a ressalva central, e a análise oferece autocorreção; não mede descoberta independente nem autonomia avançada. |
| [25. Temperatura relativa e aumento percentual](../../../modulos/e1-termodinamica.html#cr-e1-25) | C02, C08 | iniciante | 1 | Uma relação de estados com conversão de razão em percentual; não exige estado real ou modelagem aberta. |
| [26. Agitador e perda de calor](../../../modulos/e1-termodinamica.html#cr-e1-26) | C03, C08 | intermediario | 2 | Integra direção das transferências, conversão e balanço, com figura contextual. |
| [27. Compressão adiabática](../../../modulos/e1-termodinamica.html#cr-e1-27) | C03 | iniciante | 1 | A conclusão qualitativa usa hipóteses usuais, não resolve processo real. |
| [28. Energia final ou variação?](../../../modulos/e1-termodinamica.html#cr-e1-28) | C03, C08 | intermediario | 2 | Há dois alvos distintos, ΔU e Uf, após compatibilização das unidades. |
| [29. Compressão com resfriamento](../../../modulos/e1-termodinamica.html#cr-e1-29) | C03 | intermediario | 2 | Combina cálculo de trabalho e balanço energético com sinais físicos. |
| [30. Expansão isotérmica](../../../modulos/e1-termodinamica.html#cr-e1-30) | C03 | intermediario | 2 | Exige integrar identificação gráfica do processo com balanço, sem cálculo de ciclo completo. |
| [31. Poder calorífico](../../../modulos/e1-termodinamica.html#cr-e1-31) | C07 | iniciante | 1 | Reconhece o sentido da energia na definição. |
| [32. Reação e sentido inverso](../../../modulos/e1-termodinamica.html#cr-e1-32) | C07 | iniciante | 1 | A tarefa verifica sinais e definições, não composição ou equilíbrio reativo. |
| [33. Expansão livre no vácuo](../../../modulos/e1-termodinamica.html#cr-e1-33) | C03, C04 | intermediario | 2 | Requer interpretar a fronteira/figura e encadear balanço com modelo da substância. |
| [34. Aquecimento isocórico](../../../modulos/e1-termodinamica.html#cr-e1-34) | C03, C04 | intermediario | 3 | Integra o balanço energético e a restrição de entropia para distinguir condição da igualdade e sinal de ΔU. As hipóteses e a demonstração são fornecidas na análise, e o roteiro pede acompanhá-las: é estudo intermediário guiado, sem construção independente de processo nem evidência de autonomia avançada. |
| [35. Primeira lei adiabática](../../../modulos/e1-termodinamica.html#cr-e1-35) | C03 | iniciante | 3 | Aplica o balanço geral e interpreta um contramodelo de elevação já indicado no roteiro; a ressalva é solicitada, mas a hipótese ausente foi revelada previamente. Estudo guiado sem pontuação: a nota inicial já revela a ressalva central, e a análise oferece autocorreção; não mede descoberta independente nem autonomia avançada. |
| [36. Adiabático não significa sem trabalho](../../../modulos/e1-termodinamica.html#cr-e1-36) | C03, C04 | iniciante | 1 | O comando testa a distinção entre dois modos de transferência. |
| [37. Custo das irreversibilidades](../../../modulos/e1-termodinamica.html#cr-e1-37) | C05 | iniciante | 1 | Embora trate de exergia, pede apenas o sentido do efeito e não um balanço. |
| [38. Limite de Carnot](../../../modulos/e1-termodinamica.html#cr-e1-38) | C04 | iniciante | 1 | Reconhecimento do teorema, sem calcular ou determinar estados. |
| [39. Máquina com rendimento total](../../../modulos/e1-termodinamica.html#cr-e1-39) | C03, C04, C09 | intermediario | 4 | Integra conversão, balanço do ciclo e condições da segunda lei, comparando duas escolhas de fronteira explicitamente sugeridas. A ampliação do roteiro não prova autonomia avançada. Estudo guiado sem pontuação: a nota inicial já revela a ressalva central, e a análise oferece autocorreção; não mede descoberta independente nem autonomia avançada. |
| [40. Pressão e entalpia](../../../modulos/e1-termodinamica.html#cr-e1-40) | C02, C04 | iniciante | 1 | Usa um caso particular direto de relação fundamental; o nome Gibbs não torna a tarefa avançada. |
| [41. Equilíbrio entre fases](../../../modulos/e1-termodinamica.html#cr-e1-41) | C02, C07 | iniciante | 1 | Reconhece uma condição de equilíbrio; não calcula potencial químico ou composição. |
| [42. Eficiência calculada](../../../modulos/e1-termodinamica.html#cr-e1-42) | C06 | iniciante | 1 | Uma razão direta responde à pergunta; não é comparação completa de viabilidade. |
| [43. Congelamento e entropia](../../../modulos/e1-termodinamica.html#cr-e1-43) | C04 | iniciante | 1 | Testa delimitação conceitual do conjunto sujeito à segunda lei. |
| [44. Adiabático e rendimento](../../../modulos/e1-termodinamica.html#cr-e1-44) | C03, C04, C09 | iniciante | 1 | Um contraexemplo conceitual basta; não pede cálculo de estados. |
| [45. Máquina impossível](../../../modulos/e1-termodinamica.html#cr-e1-45) | C04, C06, C09 | intermediario | 3 | Acopla balanço de energia, limite da segunda lei e decisão. |
| [46. Transformações de Carnot](../../../modulos/e1-termodinamica.html#cr-e1-46) | C06 | iniciante | 1 | É identificação de processos, sem resolver suas relações de estado. |
| [47. Vazão e tipo de compressor](../../../modulos/e1-termodinamica.html#cr-e1-47) | C06 | iniciante | 1 | Solicita indicação geral de aplicação, não seleção de projeto. |
| [48. Regenerador em contracorrente](../../../modulos/e1-termodinamica.html#cr-e1-48) | C06 | iniciante | 1 | Reconhece arranjo e finalidade sob condição térmica usual. |
| [49. Pressão no Brayton real](../../../modulos/e1-termodinamica.html#cr-e1-49) | C06 | iniciante | 1 | A conclusão é qualitativa e recupera o sentido das perdas. |
| [50. Consumo do compressor](../../../modulos/e1-termodinamica.html#cr-e1-50) | C06 | iniciante | 1 | Reconhecimento do efeito das perdas, sem recompor um ciclo. |
| [51. Processos do Brayton](../../../modulos/e1-termodinamica.html#cr-e1-51) | C06 | iniciante | 1 | Basta identificar a sequência conhecida. |
| [52. Aumentar consumo melhora eficiência?](../../../modulos/e1-termodinamica.html#cr-e1-52) | C06, C09 | iniciante | 1 | Julga suficiência de uma condição por dependência direta do trabalho líquido. |
| [53. Recuperar calor da exaustão](../../../modulos/e1-termodinamica.html#cr-e1-53) | C06 | iniciante | 1 | Pergunta a finalidade do equipamento, não sua análise quantitativa. |
| [54. Aplicações de compressores](../../../modulos/e1-termodinamica.html#cr-e1-54) | C06 | iniciante | 1 | Compara definições e usos gerais sem dados de seleção. |
| [55. Rejeição de calor no Brayton](../../../modulos/e1-termodinamica.html#cr-e1-55) | C06 | iniciante | 1 | O erro decisivo é a natureza da rejeição de calor, uma identificação de modelo. |
| [56. Geração de eletricidade](../../../modulos/e1-termodinamica.html#cr-e1-56) | C06 | iniciante | 1 | É associação entre ciclo e aplicação tecnológica. |
| [57. Razão de pressões e eficiência](../../../modulos/e1-termodinamica.html#cr-e1-57) | C06 | iniciante | 1 | A conclusão resulta do comportamento monotônico de uma relação ideal. |
| [58. Compressão e pressão](../../../modulos/e1-termodinamica.html#cr-e1-58) | C02, C06 | iniciante | 1 | Reconhece evolução qualitativa do ciclo do pistão. |
| [59. Válvulas na compressão](../../../modulos/e1-termodinamica.html#cr-e1-59) | C01, C06 | iniciante | 1 | Identifica condição das válvulas, sem análise de trabalho ou massa. |
| [60. Vazão pulsante](../../../modulos/e1-termodinamica.html#cr-e1-60) | C06 | iniciante | 1 | Distingue comportamento instantâneo de fornecimento suavizado. |
| [61. Eficiência volumétrica](../../../modulos/e1-termodinamica.html#cr-e1-61) | C06 | iniciante | 1 | Reconhecimento de efeito do espaço morto sem calcular admissão. |
| [62. Etapa de admissão](../../../modulos/e1-termodinamica.html#cr-e1-62) | C01, C06 | iniciante | 3 | Reconhece duas fases do ciclo e as respectivas válvulas com o contraste temporal já indicado na nota; não dimensiona válvulas nem calcula um ciclo novo. Estudo guiado sem pontuação: a nota inicial já revela a ressalva central, e a análise oferece autocorreção; não mede descoberta independente nem autonomia avançada. |
| [63. Ciclo da turbina a gás](../../../modulos/e1-termodinamica.html#cr-e1-63) | C06 | iniciante | 1 | A identificação de família de ciclo é suficiente. |
| [64. Deslocamento positivo](../../../modulos/e1-termodinamica.html#cr-e1-64) | C06 | iniciante | 1 | Compara mecanismo básico, sem dimensionamento. |
| [65. Turbina a vapor](../../../modulos/e1-termodinamica.html#cr-e1-65) | C03, C06 | iniciante | 1 | O comando pede reconhecer o processo e efeito, sem calcular potência. |
| [66. Casco e tubos: mistura?](../../../modulos/e1-termodinamica.html#cr-e1-66) | C01, C03 | iniciante | 1 | Reconhece fronteiras de correntes e mecanismo do equipamento. |
| [67. Dilatação em tubulações](../../../modulos/e1-termodinamica.html#cr-e1-67) | C02, C09 | iniciante | 1 | Identifica função do acessório em aplicação térmica. |
| [68. Perda por radiação](../../../modulos/e1-termodinamica.html#cr-e1-68) | C03, C09 | iniciante | 1 | O alvo é uma proporcionalidade conceitual; a longa tabela e a figura não elevam a complexidade desse julgamento. |
| [69. Caminho do calor no trocador](../../../modulos/e1-termodinamica.html#cr-e1-69) | C03 | iniciante | 1 | Reconhece mecanismos e fronteiras, sem resolver rede térmica. |
| [70. Sentido da condução](../../../modulos/e1-termodinamica.html#cr-e1-70) | C04 | iniciante | 1 | A direção do fenômeno decide o julgamento. |
| [71. Convecção forçada](../../../modulos/e1-termodinamica.html#cr-e1-71) | C03 | iniciante | 1 | É identificação de mecanismo de movimentação do fluido. |
| [72. Escoamento paralelo](../../../modulos/e1-termodinamica.html#cr-e1-72) | C03 | iniciante | 1 | Reconhece uma definição geométrica de arranjo. |
| [73. Trocador compacto](../../../modulos/e1-termodinamica.html#cr-e1-73) | C03 | iniciante | 1 | A definição de grande área por volume permite avaliar a proposição. |
| [74. Incrustação e resistência térmica](../../../modulos/e1-termodinamica.html#cr-e1-74) | C03 | iniciante | 1 | Reconhecimento de fatores de influência sem previsão de desempenho. |
| [75. Sinal na lei de Fourier](../../../modulos/e1-termodinamica.html#cr-e1-75) | C04, C08 | iniciante | 1 | Interpreta o sinal de uma relação, sem solução de campo. |
| [76. Advecção e convecção](../../../modulos/e1-termodinamica.html#cr-e1-76) | C03 | iniciante | 1 | É discriminação conceitual de mecanismos de transporte. |
| [77. Função do condensador](../../../modulos/e1-termodinamica.html#cr-e1-77) | C06 | iniciante | 1 | O item exige identificar função e direção da troca térmica. |
| [78. Vantagem térmica da amônia](../../../modulos/e1-termodinamica.html#cr-e1-78) | C02, C06 | iniciante | 1 | Seleciona vantagem térmica conceitual, sem calcular COP ou riscos de instalação. |
| [79. Calor em câmara de vácuo](../../../modulos/e1-termodinamica.html#cr-e1-79) | C03 | intermediario | 4 | O novo roteiro solicita construir dois casos contrastantes e indicar parâmetros que mudam a predominância, além de reconhecer mecanismos. Essa tarefa justifica estimativa intermediária; a ressalva inicial e o exemplo de autocorreção impedem tratá-la como prova de descoberta autônoma ou nível avançado. Estudo guiado sem pontuação: a nota inicial já revela a ressalva central, e a análise oferece autocorreção; não mede descoberta independente nem autonomia avançada. |
| [80. Geração interna e convecção](../../../modulos/e1-termodinamica.html#cr-e1-80) | C03, C08 | intermediario | 4 | Integra geometria, geração, troca superficial e termo de acumulação, julgando uma simplificação indicada no roteiro. A crítica agora é solicitada, mas as notas revelam o ponto decisivo e não demonstram autonomia avançada. Estudo guiado sem pontuação: a nota inicial já revela a ressalva central, e a análise oferece autocorreção; não mede descoberta independente nem autonomia avançada. |

## Adaptações autorais no estilo Avalia

Todos os vínculos abaixo são **apoio fundamental** às competências, com alcance limitado explicitado no JSON.

| Item e fonte | Competências | Nível estimado | Etapas | Justificativa do raciocínio |
|---|---|---|---:|---|
| [AV-01. Quantidade de matéria](../../../modulos/e1-termodinamica.html#av-e1-01) | C02 | iniciante | 1 | A divisão está explicitada; pede apenas discriminar intensivas de totais. |
| [AV-02. Estado e caminho](../../../modulos/e1-termodinamica.html#av-e1-02) | C02, C03 | iniciante | 1 | Cinco alternativas verificam uma mesma distinção conceitual, sem balanço quantitativo. |
| [AV-03. Movimento molecular](../../../modulos/e1-termodinamica.html#av-e1-03) | C02 | iniciante | 1 | É sequência V/F de conceitos básicos, não inferência de modelo molecular. |
| [AV-04. Líquido quase incompressível](../../../modulos/e1-termodinamica.html#av-e1-04) | C02 | iniciante | 1 | A hipótese e seu domínio já são fornecidos; basta interpretar seu significado. |
| [AV-05. Unidades fundamentais](../../../modulos/e1-termodinamica.html#av-e1-05) | C08 | iniciante | 1 | Uma associação de unidades conhecidas resolve a tarefa. |
| [AV-06. Conversão de escalas](../../../modulos/e1-termodinamica.html#av-e1-06) | C08 | iniciante | 1 | É uma interpolação de um só intervalo conhecido; não exige analisar incerteza da calibração. |
| [AV-07. Bourdon ou termômetro?](../../../modulos/e1-termodinamica.html#av-e1-07) | C08 | iniciante | 1 | O instrumento é nomeado e descrito, exigindo recuperação de sua função. |
| [AV-08. Faixa de um sensor](../../../modulos/e1-termodinamica.html#av-e1-08) | C08 | iniciante | 1 | A definição de span leva a uma aplicação numérica direta. |
| [AV-09. Unidade de temperatura](../../../modulos/e1-termodinamica.html#av-e1-09) | C08 | iniciante | 1 | O comando explicita a grandeza e pede discriminar conceitos elementares de escala. |
| [AV-10. Massa específica](../../../modulos/e1-termodinamica.html#av-e1-10) | C02 | iniciante | 1 | Aplicação da definição de densidade com classificação conceitual simples. |
| [AV-11. Unidade termodinâmica](../../../modulos/e1-termodinamica.html#av-e1-11) | C08 | iniciante | 1 | Só se substitui um número na relação fornecida. |
| [AV-12. Identificação das quatro leis](../../../modulos/e1-termodinamica.html#av-e1-12) | C03, C04 | iniciante | 1 | Associação de definições; não se aplicam as quatro leis a um problema físico. |
| [AV-13. Energia interna do gás ideal](../../../modulos/e1-termodinamica.html#av-e1-13) | C02 | iniciante | 1 | A massa e a propriedade são dadas, dispensando seleção de modelo ou integração. |
| [AV-14. Ocupação do recipiente](../../../modulos/e1-termodinamica.html#av-e1-14) | C02 | iniciante | 1 | A pergunta é espacial/conceitual apesar do contexto de liberação. |
| [AV-15. Colisões moleculares](../../../modulos/e1-termodinamica.html#av-e1-15) | C02 | iniciante | 1 | As hipóteses do modelo são o próprio objeto da sequência V/F. |
| [AV-16. Desumidificador: pressão parcial](../../../modulos/e1-termodinamica.html#av-e1-16) | C07 | iniciante | 1 | Razão direta com hipóteses declaradas. |
| [AV-17. Significado de 50% de umidade](../../../modulos/e1-termodinamica.html#av-e1-17) | C07 | iniciante | 1 | Aplica o significado da indicação do higrômetro, não um balanço de mistura. |
| [AV-18. Aumento de temperatura](../../../modulos/e1-termodinamica.html#av-e1-18) | C02 | iniciante | 1 | Uma relação proporcional de estados com restrições explícitas. |
| [AV-19. Pressão pela equação de estado](../../../modulos/e1-termodinamica.html#av-e1-19) | C02 | iniciante | 1 | A substituição direta determina 1 atm sem consulta de propriedades. |
| [AV-20. Extrapolação ao zero absoluto](../../../modulos/e1-termodinamica.html#av-e1-20) | C02, C09 | iniciante | 1 | A relação já é dada; a tarefa seleciona conclusão e limite conceitual. |
| [AV-21. Variáveis do gás](../../../modulos/e1-termodinamica.html#av-e1-21) | C02 | iniciante | 1 | Julga a dependência expressa por uma equação, sem determinar propriedades. |
| [AV-22. Fator de compressibilidade](../../../modulos/e1-termodinamica.html#av-e1-22) | C02, C07 | iniciante | 1 | O enunciado já fornece os dois produtos; só requer uma razão e interpretação. |
| [AV-23. Condições para idealidade](../../../modulos/e1-termodinamica.html#av-e1-23) | C02, C09 | iniciante | 1 | Reconhece condições gerais de uma aproximação. |
| [AV-24. Termômetro de gás](../../../modulos/e1-termodinamica.html#av-e1-24) | C02, C09 | iniciante | 1 | Uma proporcionalidade direta responde sem comparar substâncias diferentes. |
| [AV-25. Temperatura relativa e aumento percentual](../../../modulos/e1-termodinamica.html#av-e1-25) | C02, C08 | iniciante | 1 | Mesma relação e percentuais de CR25, sem nova decisão de modelo. |
| [AV-26. Agitador e perda de calor](../../../modulos/e1-termodinamica.html#av-e1-26) | C03, C08 | iniciante | 1 | Todas as hipóteses e unidades são dadas; aplica diretamente entradas menos saídas, sem conversão adicional. |
| [AV-27. Compressão adiabática](../../../modulos/e1-termodinamica.html#av-e1-27) | C03 | iniciante | 1 | A inferência é qualitativa com restrições fornecidas, sem cálculo de estados. |
| [AV-28. Energia final ou variação?](../../../modulos/e1-termodinamica.html#av-e1-28) | C03, C08 | intermediario | 2 | A distinção entre ΔU e Uf exige duas relações encadeadas, embora os dados sejam repetidos. |
| [AV-29. Compressão com resfriamento](../../../modulos/e1-termodinamica.html#av-e1-29) | C03 | intermediario | 2 | Integra trabalho pΔV e balanço de energia com sinais. |
| [AV-30. Expansão isotérmica](../../../modulos/e1-termodinamica.html#av-e1-30) | C03 | iniciante | 1 | Uma simplificação direta do balanço dá o trabalho; não há integração de ciclo. |
| [AV-31. Poder calorífico](../../../modulos/e1-termodinamica.html#av-e1-31) | C07 | iniciante | 1 | Identifica a diferença entre duas definições. |
| [AV-32. Reação e sentido inverso](../../../modulos/e1-termodinamica.html#av-e1-32) | C07 | iniciante | 1 | Uma inversão de sinal e sua interpretação conceitual, sem reação química a balancear. |
| [AV-33. Expansão livre no vácuo](../../../modulos/e1-termodinamica.html#av-e1-33) | C03, C04 | intermediario | 2 | Integra primeira lei e entropia para distinguir temperatura constante de isentropia. |
| [AV-34. Aquecimento isocórico](../../../modulos/e1-termodinamica.html#av-e1-34) | C03 | intermediario | 2 | Encadeia balanço de energia e relação de propriedade para uma incógnita térmica. |
| [AV-35. Primeira lei adiabática](../../../modulos/e1-termodinamica.html#av-e1-35) | C03 | iniciante | 1 | Dados e convenção estão explícitos; uma relação direta determina o sinal. |
| [AV-36. Adiabático não significa sem trabalho](../../../modulos/e1-termodinamica.html#av-e1-36) | C03, C04 | iniciante | 1 | A contradição conceitual sobre trabalho decide a seleção. |
| [AV-37. Custo das irreversibilidades](../../../modulos/e1-termodinamica.html#av-e1-37) | C05 | iniciante | 1 | Multiplicação direta da relação explicitamente fornecida, apesar do tema exergia. |
| [AV-38. Limite de Carnot](../../../modulos/e1-termodinamica.html#av-e1-38) | C04 | iniciante | 1 | Uma substituição em ηmax=1−TL/TH resolve. |
| [AV-39. Máquina com rendimento total](../../../modulos/e1-termodinamica.html#av-e1-39) | C03, C04, C09 | intermediario | 2 | O julgamento distingue satisfação da primeira lei e violação da segunda, com cenário completamente delimitado. |
| [AV-40. Pressão e entalpia](../../../modulos/e1-termodinamica.html#av-e1-40) | C02, C04 | iniciante | 1 | Relação e simplificações já são fornecidas; resta uma aplicação direta, não uma derivação avançada. |
| [AV-41. Equilíbrio entre fases](../../../modulos/e1-termodinamica.html#av-e1-41) | C02, C07 | iniciante | 1 | Seleciona a condição de equilíbrio de fases já nomeada. |
| [AV-42. Eficiência calculada](../../../modulos/e1-termodinamica.html#av-e1-42) | C06 | iniciante | 1 | Uma razão direta entre grandezas já fornecidas. |
| [AV-43. Congelamento e entropia](../../../modulos/e1-termodinamica.html#av-e1-43) | C04 | iniciante | 1 | Aplica diretamente o critério ao saldo +0,10 kJ/K. |
| [AV-44. Adiabático e rendimento](../../../modulos/e1-termodinamica.html#av-e1-44) | C03, C04, C09 | iniciante | 1 | As três proposições usam diretamente definições de ciclo e primeira lei. |
| [AV-45. Máquina impossível](../../../modulos/e1-termodinamica.html#av-e1-45) | C04, C06, C09 | intermediario | 2 | Integra limite da segunda lei ao balanço de energia do ciclo. |
| [AV-46. Transformações de Carnot](../../../modulos/e1-termodinamica.html#av-e1-46) | C06 | iniciante | 1 | Reconhece a sequência canônica de processos. |
| [AV-47. Vazão e tipo de compressor](../../../modulos/e1-termodinamica.html#av-e1-47) | C06 | iniciante | 1 | A resposta é uma tendência de classificação explicitamente preliminar. |
| [AV-48. Regenerador em contracorrente](../../../modulos/e1-termodinamica.html#av-e1-48) | C06 | iniciante | 1 | Aplica a direção espontânea de transferência de calor. |
| [AV-49. Pressão no Brayton real](../../../modulos/e1-termodinamica.html#av-e1-49) | C06 | iniciante | 1 | Distingue processos ideais e perda de pressão por conhecimento qualitativo. |
| [AV-50. Consumo do compressor](../../../modulos/e1-termodinamica.html#av-e1-50) | C06 | iniciante | 1 | Reconhece efeitos de eficiências isentrópicas numa comparação delimitada. |
| [AV-51. Processos do Brayton](../../../modulos/e1-termodinamica.html#av-e1-51) | C06 | iniciante | 1 | Reconhecimento conjunto de processos isentrópicos e isobáricos. |
| [AV-52. Aumentar consumo melhora eficiência?](../../../modulos/e1-termodinamica.html#av-e1-52) | C06, C09 | intermediario | 2 | Encadeia balanço de potências e rendimento para duas condições. |
| [AV-53. Recuperar calor da exaustão](../../../modulos/e1-termodinamica.html#av-e1-53) | C06 | iniciante | 1 | O comando pede somente variação percentual do calor fornecido. |
| [AV-54. Aplicações de compressores](../../../modulos/e1-termodinamica.html#av-e1-54) | C06 | iniciante | 1 | Classifica quatro exemplos pela definição de família. |
| [AV-55. Rejeição de calor no Brayton](../../../modulos/e1-termodinamica.html#av-e1-55) | C06 | iniciante | 1 | Seleciona processo incompatível com a descrição canônica. |
| [AV-56. Geração de eletricidade](../../../modulos/e1-termodinamica.html#av-e1-56) | C06 | iniciante | 1 | Associa componentes aos ciclos nomeados. |
| [AV-57. Razão de pressões e eficiência](../../../modulos/e1-termodinamica.html#av-e1-57) | C06 | iniciante | 1 | A expressão e sua parte difícil já estão fornecidas. |
| [AV-58. Compressão e pressão](../../../modulos/e1-termodinamica.html#av-e1-58) | C02, C06 | iniciante | 1 | Substituição direta na lei de Boyle. |
| [AV-59. Válvulas na compressão](../../../modulos/e1-termodinamica.html#av-e1-59) | C01, C06 | iniciante | 1 | Reconhece sequência operacional e condição de abertura já delimitada. |
| [AV-60. Vazão pulsante](../../../modulos/e1-termodinamica.html#av-e1-60) | C06 | iniciante | 1 | Diferencia efeitos locais e a jusante de um reservatório. |
| [AV-61. Eficiência volumétrica](../../../modulos/e1-termodinamica.html#av-e1-61) | C06 | iniciante | 1 | Calcula diretamente a razão explicitamente definida. |
| [AV-62. Etapa de admissão](../../../modulos/e1-termodinamica.html#av-e1-62) | C01, C06 | iniciante | 1 | Associa fluxo já estabelecido à posição das válvulas. |
| [AV-63. Ciclo da turbina a gás](../../../modulos/e1-termodinamica.html#av-e1-63) | C06 | iniciante | 1 | Reconhece equipamento e sequência padrão de processos. |
| [AV-64. Deslocamento positivo](../../../modulos/e1-termodinamica.html#av-e1-64) | C06 | iniciante | 1 | Classifica mecanismo de compressão. |
| [AV-65. Turbina a vapor](../../../modulos/e1-termodinamica.html#av-e1-65) | C03, C06 | iniciante | 1 | O modelo reduzido está completamente delimitado e só exige aplicação direta. |
| [AV-66. Casco e tubos: mistura?](../../../modulos/e1-termodinamica.html#av-e1-66) | C01, C03 | iniciante | 1 | Reconhece função da parede e mecanismos de troca. |
| [AV-67. Dilatação em tubulações](../../../modulos/e1-termodinamica.html#av-e1-67) | C02, C09 | iniciante | 1 | Substituição na lei linear com conversão de unidade. |
| [AV-68. Perda por radiação](../../../modulos/e1-termodinamica.html#av-e1-68) | C03, C09 | iniciante | 1 | Apenas emissividade varia em uma expressão fornecida. |
| [AV-69. Caminho do calor no trocador](../../../modulos/e1-termodinamica.html#av-e1-69) | C03 | iniciante | 1 | Classifica mecanismos em interfaces e no sólido. |
| [AV-70. Sentido da condução](../../../modulos/e1-termodinamica.html#av-e1-70) | C04 | iniciante | 1 | Compara duas temperaturas para determinar sentido físico. |
| [AV-71. Convecção forçada](../../../modulos/e1-termodinamica.html#av-e1-71) | C03 | iniciante | 1 | Reconhece a origem externa do movimento. |
| [AV-72. Escoamento paralelo](../../../modulos/e1-termodinamica.html#av-e1-72) | C03 | iniciante | 1 | Aplica definições geométricas das configurações. |
| [AV-73. Trocador compacto](../../../modulos/e1-termodinamica.html#av-e1-73) | C03 | iniciante | 1 | Reconhece a finalidade básica de área elevada. |
| [AV-74. Incrustação e resistência térmica](../../../modulos/e1-termodinamica.html#av-e1-74) | C03 | iniciante | 1 | Repete uma relação direta para dois coeficientes fornecidos. |
| [AV-75. Sinal na lei de Fourier](../../../modulos/e1-termodinamica.html#av-e1-75) | C04, C08 | iniciante | 1 | Aplicação direta de expressão com sinal explícito. |
| [AV-76. Advecção e convecção](../../../modulos/e1-termodinamica.html#av-e1-76) | C03 | iniciante | 1 | Distingue definições e sinal físico do coeficiente. |
| [AV-77. Função do condensador](../../../modulos/e1-termodinamica.html#av-e1-77) | C06 | iniciante | 1 | Aplica diretamente balanço de energia do ciclo completo. |
| [AV-78. Vantagem térmica da amônia](../../../modulos/e1-termodinamica.html#av-e1-78) | C02, C06 | iniciante | 1 | Interpreta significado de uma propriedade por unidade de massa. |
| [AV-79. Calor em câmara de vácuo](../../../modulos/e1-termodinamica.html#av-e1-79) | C03, C09 | iniciante | 1 | As vias materiais e a hipótese do gás já estão dadas. |
| [AV-80. Geração interna e convecção](../../../modulos/e1-termodinamica.html#av-e1-80) | C03, C08 | intermediario | 2 | Integra seleção geométrica de área e volume ao balanço com convecção. |

## Integridade e evolução

O validador compara os registros com os artigos realmente presentes e detecta itens ausentes, órfãos, duplicados, hashes desatualizados e mudanças nos recursos. O contrato inclui novos IDs com mais de dois dígitos, respostas abertas e projetos, sem impor quantidade fixa. A versão 1.1 permite evoluir os estados de conferência oficial e de revisão de gabaritos com evidências locais condicionais. Atualizar um hash requer releitura, não apenas executar o programa.

Os resultados da verificação e hashes desta rodada estão na [entrega BAN-02-r3](../entregas/BAN-02-r3.md). O aceite cabe ao Auditor independente.


## Inclusão FUN-01 — quatro problemas abertos

Versão E1-FUN01 v1.0, 27/10/2026. Os casos avaliam partes de C01/C02/C07/C08/C09/C10; nenhuma competência é declarada integral. Problemas 1 e 3 são intermediários por combinarem relações e decisões dentro de modelos fornecidos; 2 e 4 acrescentam escolha de regime/restrições, contraexemplos ou estabilidade. Isso é julgamento cognitivo local, sem piloto ou certificação global. Soluções, dados, limites e rubricas estão publicados no E1. FUN-01 recebeu aprovação independente na rodada 2, conforme o parecer correspondente; seus quatro registros permanecem idênticos à versão aprovada.

| ID e atividade | Nível estimado | Etapas intelectuais | Vínculo parcial | Justificativa |
|---|---|---:|---|---|
| [fun01-e1-saturacao](../../../modulos/e1-termodinamica.html#fun01-e1-saturacao) — Problema 1 — Um tanque, três informações e um conflito | intermediario | 4 | C01, C02, C08, C09, C10 | Integra identificação de redundância, inversão da relação de mistura, checagem por entalpia e intervalos; pede justificar informação independente e limites. Região, propriedades e modelo são fornecidos, o que restringe a seleção autônoma de modelo. |
| [fun01-e1-mistura](../../../modulos/e1-termodinamica.html#fun01-e1-mistura) — Problema 2 — Quatro lotes e uma hipótese bifásica | avancado | 5 | C01, C02, C07, C08, C09, C10 | Exige decidir e justificar modelos de uma ou duas fases para lotes distintos, rejeitar soluções algébricas inviáveis, fechar balanços e construir mais de um estado compatível quando z falta. A autonomia é local ao modelo ideal fornecido; não se infere domínio avançado de misturas reais. |
| [fun01-e1-supercritico](../../../modulos/e1-termodinamica.html#fun01-e1-supercritico) — Problema 3 — O rótulo “supercrítico” é sustentado pelos dados? | intermediario | 4 | C01, C02, C08, C09, C10 | Combina duas restrições estritas e limites de erro para avaliar leituras e melhorias, depois julga dados redundantes e qualidade. O critério e as referências críticas são fornecidos; não exige resolver uma equação de estado ou um problema inverso não linear. |
| [fun01-e1-equilibrio](../../../modulos/e1-termodinamica.html#fun01-e1-equilibrio) — Problema 4 — Diagnóstico de uma bancada multicâmara | avancado | 7 | C01, C02, C07, C08, C09, C10 | Integra diagnóstico de dados conflitantes, derivação por balanço de forças, comparação de potenciais com gravidade, determinação de estado final sob restrições seletivas e teste de estabilidade com conservação. Exige rejeitar igualdades indevidas e defender limites do modelo; não se resume a substituir dados na relação fornecida. |

O conjunto separa partilha de dados de referência, relação temática e componentes de fixação da independência do diagnóstico completo. O mini parecer v/ρ reaparece como subcomponente do problema 3; a aula de fases fornece as relações usadas, mas não resolve os quatro lotes do problema 2. O exemplo de pressão parcial compara reservatórios dados, enquanto o problema 4 exige inventários finitos, redistribuição, estabilidade e gravidade. O histórico individual do estudante permanece desconhecido.

Autoria: Corretor (teoria, problemas 1–3, integração e inventário); apoio_fun01 (preparação específica e problema 4, revistos na integração); coordenador (fontes adicionais e conferência numérica independente). Nenhum desses papéis é o Auditor independente. Os 190 registros BAN-02 e suas linhas no resumo permanecem com o conteúdo aprovado.

## Inclusão FUN-02 — diferenciais e caminhos

Versão E1-FUN02 v1.0, 27/10/2026. Os três casos avaliam partes de C01/C02/C03/C08/C09/C10. A integração matemática não certifica uma equação fundamental física e a aplicação de entropia não substitui os balanços gerais da segunda lei. FUN-02 recebeu aprovação independente na rodada 1; seus três registros permanecem idênticos à versão aprovada.

| ID e atividade | Nível estimado | Etapas intelectuais | Vínculo parcial | Justificativa |
|---|---|---:|---|---|
| [fun02-e1-caminhos](../../../modulos/e1-termodinamica.html#fun02-e1-caminhos) — Problema 1 — Projetar caminhos dentro de uma janela de temperatura | avancado | 5 | C01, C02, C03, C08, C09, C10 | O aluno escolhe e constrói dois caminhos dentro de restrições, demonstra admissibilidade ao longo deles, rejeita uma alternativa e fecha ciclo com orientação escolhida. Não basta substituir números em um caminho pré-definido; a autonomia permanece limitada ao gás ideal e aos três controles fornecidos. |
| [fun02-e1-integrabilidade](../../../modulos/e1-termodinamica.html#fun02-e1-integrabilidade) — Problema 2 — Um registrador pode confundir percurso com propriedade? | avancado | 6 | C02, C08, C09, C10 | Exige diagnosticar uma falsa certificação com cancelamento não trivial de ciclo, identificar κ a partir de outro ensaio, construir contraexemplo entre rotas e distinguir derivada de caminho de parcial. A classificação depende dessas decisões integradas, não do uso isolado de derivadas. |
| [fun02-e1-calor-caminho](../../../modulos/e1-termodinamica.html#fun02-e1-calor-caminho) — Problema 3 — Aquecer a temperatura enquanto o gás perde calor | intermediario | 5 | C01, C02, C03, C08, C09, C10 | Integra relações distintas e exige crítica às interpretações, mas trajetória, modelo, coordenadas e hipóteses são fornecidos. A construção autônoma de um novo modelo não é necessária; os testes formais e fator1/T foram ensinados imediatamente antes. |

Os três registros contêm origem, pré-requisitos, hipóteses, etapas, limites e relações locais de exposição. A construção de caminhos com janela térmica difere do perfil linear resolvido na teoria; o registrador exige identificar um parâmetro e explicar cancelamento de ciclo, além da reconstrução de potencial ensinada; o terceiro caso aplica relações já fornecidas a uma compressão definida e é classificado como intermediário. O histórico individual do estudante permanece desconhecido.

Autoria: Corretor (teoria, problemas 1 e 3, integração, inventário); apoio_fun01 (preparação de integrais e problema 2, revistos na integração); coordenador (conferência de fontes/cálculos e figura quantitativa). Esses trabalhos são distintos do parecer do Auditor. A validação de preservação, recursos e reprodução está na [entrega FUN-02-r1](../entregas/FUN-02-r1.md).

## Atualização FON-09 — dados associados a CR68

A origem documental foi conferida na prova oficial (p. 3), no caderno fornecido (p. 14) e no HTML: a densidade literal e as cinco linhas já constam da prova. A transcrição histórica ficou identificada e recolhida, com aviso para não reutilizar seus dados; o conjunto editorial FON-09 v1.0 apresenta cinco linhas corrigidas e densidade com modelo/condição/precisão explícitos. Duas células da primeira linha são arredondamentos compatíveis, e as outras 13 células físicas são incompatíveis com a precisão impressa. As pressões são condições prescritas, não resultados corrigidos.

A letra C do item original 85 foi confirmada na página 1 do gabarito definitivo; a afirmação, alternativas, resolução e digital de resposta são preservadas. O campo de revisão histórica BAN-02 permanece, e essa conferência restrita não conclui BAN-08, BAN-10 ou FON-01. A origem de CR68 agora registra evidência documental, e seus recursos incluem dados corrigidos e as três fontes locais. Nível, competências, raciocínio e etapas não mudaram. Os outros 196 registros e todas as 197 linhas anteriores deste resumo permanecem iguais.

Ver [entrega FON-09-r1](../entregas/FON-09-r1.md), [origem e confronto integral](../evidencias/FON-09/conferencia-origem-r1.md) e [dados corrigidos](../../../assets/termodinamica/fon09-cr68-dados-v1.json). O parecer independente de FON-09 está pendente.


## BAN-10 r2 — decisões de uso e conferência localizada

A triagem percorreu197/197 itens. Nove estudos críticos ficam fora de acertos/erros e do denominador; o banco CR tem 71 itens de treino pontuável e 9 marcadores documentais. Os rótulos não constituem nota de domínio avançado. [Decisões por ID e fontes](../evidencias/BAN-10/decisoes-r2.json) · [Triagem autoral individual](../evidencias/BAN-10/triagem-r2.json). A chave oficial foi preservada nos 12 casos; confirmação documental e interpretação técnica são registros distintos. Nos nove críticos, o estado de gabarito histórico de BAN02 não é uma revisão numérica geral ou a certificação de resposta técnica universal.

| ID | Chave documental | Uso atual | Razão |
|---|---|---|---|
| [cr-e1-04](../../../modulos/e1-termodinamica.html#cr-e1-04) | C | Estudo crítico sem pontuação | Sensibilidades a grandezas de dimensões diferentes não são ordenáveis sem definir estado, escalas e perturbações. |
| [cr-e1-09](../../../modulos/e1-termodinamica.html#cr-e1-09) | E | Estudo crítico sem pontuação | O item omite a restrição a temperatura termodinâmica/unidade de base; grau Celsius também é unidade SI. |
| [cr-e1-24](../../../modulos/e1-termodinamica.html#cr-e1-24) | E | Estudo crítico sem pontuação | A razão literal entre pressão de gás e pressão de água não é determinada; a interpretação de termômetro exige a mesma amostra de gás. |
| [cr-e1-34](../../../modulos/e1-termodinamica.html#cr-e1-34) | C | Estudo crítico sem pontuação | Estudo pedagógico de modelos: distinguir a desigualdade ΔU>0 afirmada pelo original da identidade adicional ΔU=Q. Não foi demonstrada invalidade da chave C pela presença de outros trabalhos. |
| [cr-e1-35](../../../modulos/e1-termodinamica.html#cr-e1-35) | C | Estudo crítico sem pontuação | A conclusão usa energia interna onde a lei geral envolve energia total; faltam condições de energia cinética/potencial. |
| [cr-e1-39](../../../modulos/e1-termodinamica.html#cr-e1-39) | C | Estudo crítico sem pontuação | A conclusão de Kelvin–Planck exige explicitar calor total, trabalho líquido e ausência de outros efeitos; motor de combustão real não é automaticamente uma massa fechada cíclica. |
| [cr-e1-51](../../../modulos/e1-termodinamica.html#cr-e1-51) | C | Treino mantido com alcance delimitado | O ciclo nomeado é tomado em seu modelo ideal convencional, cujos quatro processos não são isotérmicos; não se afirma isso para todas as modificações ou máquinas reais. |
| [cr-e1-55](../../../modulos/e1-termodinamica.html#cr-e1-55) | E | Treino mantido com alcance delimitado | Há expressão anômala oficial, porém o resfriamento isocórico já torna falsa a descrição do Brayton convencional independentemente dela. |
| [cr-e1-62](../../../modulos/e1-termodinamica.html#cr-e1-62) | C | Estudo crítico sem pontuação | Durante esse movimento pode designar a etapa de admissão ou toda a descida, que pode incluir reexpansão com ambas as válvulas fechadas. |
| [cr-e1-68](../../../modulos/e1-termodinamica.html#cr-e1-68) | C | Treino mantido com alcance delimitado | A afirmação de possibilidade de reduzir perda radiativa é válida para superfície quente com demais condições comparáveis, independentemente dos dados de água defeituosos. |
| [cr-e1-79](../../../modulos/e1-termodinamica.html#cr-e1-79) | B | Estudo crítico sem pontuação | Alto vácuo reduz troca gasosa, mas não fixa predominância radiativa frente à condução por suportes e cabos. |
| [cr-e1-80](../../../modulos/e1-termodinamica.html#cr-e1-80) | D | Estudo crítico sem pontuação | Uniformidade espacial da superfície não determina acumulação nula; o valor único usa regime permanente e convecção como única troca exposta. |

Os nove roteiros solicitam justificativas orientadas, com autocorreção sem nota e sem correção automática do texto. O apoio propôs seus metadados; o Corretor os releu e integrou. As estimativas e etapas atuais se referem a esses roteiros. As versões AV correspondentes foram examinadas e não receberam exclusão automática; suas hipóteses explícitas sanam vários limites dos CR. A decisão conservadora de CR39 difere da leitura usual suficiente sugerida pelo apoio; ambas estão registradas, e a exclusão não declara a letra oficial errada. As conferências visuais de documentos foram feitas pelo coordenador automatizado; o Auditor emitirá parecer independente. BAN07/BAN08/FON01 permanecem sem aceite global.

Distribuição atual após os roteiros BAN-10: iniciante: 169; intermediario: 24; avancado: 4. A contagem não mede aprendizagem.

R2, R1-A: somente CR34 foi revisto. O original afirma ΔU>0; ΔU=Q requer soma W+ΔEc+ΔEp=0, não necessariamente cada termo nulo. A análise guiada usa também entropia e a relação de estado para sustentar o sinal sob as hipóteses declaradas. CR34 segue crítico por escolha pedagógica, sem demonstração de invalidade de C. O nível intermediário refere-se à combinação guiada das duas leis; os outros 196 registros não mudaram.


## FON-01 r1 — rastreabilidade documental dos 80 CR

As observações de conferência parcial nas seções históricas acima descrevem aquelas entregas. Nesta rodada, os 80 CR foram confrontados individualmente com fontes oficiais quanto a contexto/comando, alternativas, figuras, identificação, páginas e chave definitiva. O JSON marca conferencia_oficial=realizada e aponta para a [matriz dos 80](../evidencias/FON-01/conferencia-80-r1.json); o [resumo legível](../evidencias/FON-01/CONFERENCIA_80-r1.md) registra cada item. A decisão independente de aceite desta rodada está pendente.

CR56/TBG48 e CR67/Petrobras84 tiveram E→C oficialmente e já estavam corretos no curso. A anulação dos originais 82/83 do contexto de CR68 não alcança o original 85 selecionado. A prova CAESB atualizada em 11/05/2026 conserva CR80/questão38 na página física 5; suas referências no artigo e no catálogo de 12 provas foram atualizadas, com versão histórica marcada sem efeito preservada. Chave D e estudo crítico permanecem. Itaipu usa o número do modelo publicado, sem inferir tipo/cor individual; TG15/FGV não é o TG29 atingido pelo comunicado de 02/08/2024.

Nenhum nível, competência, pré-requisito, etapa, hipótese, uso crítico, gabarito ou recurso de cálculo dos 197 registros mudou nesta rodada. Fora dos metadados de origem dos 80 CR, mudaram somente o hash do artigo CR80 e fonte.sha256/snapshot, em consequência da referência documental. Os outros117 registros são idênticos. PDFs/catalogação histórica são preservados; o documento CAESB atual fica rastreado no pacote FON-01. Isto não conclui auditoria científica de gabaritos nem certifica aprendizagem ou ausência universal de retificações futuras.

## FON-02 r1 — origem dos suplementos nas resoluções

Os 80 artigos CR foram relidos integralmente, incluindo notas, roteiros críticos e dados corrigidos. O [registro individual](../evidencias/FON-02/revisao-suplementos-80-r1.json) e o [resumo legível](../evidencias/FON-02/REVISAO_SUPLEMENTOS_80-r1.md) distinguem dados oficiais, resultados derivados, conversões/convenções, modelos, hipóteses e exemplos autorais. A conferência documental FON-01 é reaproveitada por identidade dos componentes oficiais.

Foram esclarecidos 21 conteúdos locais (CR06/16/17/24/26/27/28/29/30/33/36/37/40/42/44/45/50/57/65/79/80) e identificada a autoria nos 71 resumos usuais. Os nove resumos críticos específicos permanecem. CR68 preserva o conjunto rastreável FON-09; CR79 mantém os valores do contramodelo, agora com relações e constante identificadas.

Enunciados, alternativas, figuras, chaves, digitais e uso no placar permanecem. As condições esclarecidas nas resoluções não foram cadastradas como condições fornecidas pela banca. Dos 197 registros, apenas 74 hashes de artigo mudaram; os demais campos individuais e recursos permanecem iguais, assim como os 123 registros restantes. No cabeçalho canônico, mudaram somente fonte.sha256/snapshot. A validação semântica independente de FON-02 está pendente; isto não conclui BAN-07/BAN-08/FON-10 nem certifica aprendizagem.

## Revisão BAN-07 r1 — versão submetida à auditoria

O diagnóstico integral contém197registros e731juízos individuais de opções. Foram corrigidos25artigos autorais(10Q e15AV), com20novasdigitais e cinco alterações somente de comentários; nenhuma chave foi trocada. Os80CR e sete problemas abertos permanecem integralmente preservados. Os nove estudos críticos continuam fora da pontuação. A verificação do Corretor dos25registros atingidos aponta ao [diagnóstico após correção](../evidencias/BAN-07/diagnostico-pos-correcao-197-r1.json); o [mapa de identidade](../evidencias/BAN-07/mapa-identidades-r1.json) distingue cada versão e mantém o histórico sem copiar letras antigas para novas digitais.

As hipóteses de Q02/Q09/AV33/AV50 foram explicitadas antes da tentativa. Foram sincronizados os hashes e os metadados realmente atingidos; os outros172registros permanecem idênticos. Níveis, competências e estatísticas do inventário foram preservados. A conferência do Corretor não é parecer de aprovação independente e não conclui BAN-08 ou classificação global do curso.

## BAN-07 r2 — versão submetida à auditoria

AV04, AV31 e AV62 têm distratores e comentários substituídos; CR06, CR26 e CR45 recebem hipóteses editoriais antes da resposta, sem alterar texto ou chave oficiais; a versão é sujeita à auditoria independente e não aprova o banco. As digitais foram recalculadas e as tentativas antigas não foram migradas. A aplicação depende da conclusão do parecer r1 e de eventual liberação do coordenador.

As análises complementares de [suplementos FON-02](../evidencias/BAN-07/revisao-fon02-complementar-r2.json), [triagem BAN-10](../evidencias/BAN-07/triagem-ban10-complementar-r2.json) e [identidade documental FON-01](../evidencias/BAN-07/confronto-fon01-cr-r2.json) são provisórias e preservam os registros históricos.

## Atualização localizada BAN-08 — AV42, AV45 e AV52

Os enunciados explicitam as condições de balanço necessárias: AV42 e AV45 delimitam as fontes e as trocas no ciclo; AV52 fixa a potência térmica total e despreza outros consumos. As cinco alternativas e as chaves foram preservadas; AV52 explicita a mesma condição na resolução. Na entrega inicial de aplicação, o JSON registrava as hipóteses atualizadas e a revisão do gabarito da versão efetiva como pendente; o parágrafo seguinte registra a revalidação posterior. As digitais mudam e o histórico anterior não é migrado para as novas respostas. A aprovação BAN-07 r3 é evidência da versão anterior, não aprovação automática desta alteração. Naquele momento, a revisão independente e os testes controlados de persistência da versão aplicada ainda eram necessários.

A [revalidação independente localizada de BAN-07](../pareceres/BAN-07-revalidacao-av42-av45-av52-r1-independente.md) verificou os três gabaritos na versão aplicada; o JSON aponta a essa evidência, sem aprovar BAN-08. Para AV45, a [evidência anterior de BAN-07](../evidencias/BAN-07/diagnostico-pos-correcao-197-r1.json) permanece como histórico da versão anterior, e não como prova isolada da versão atual.


## QA-09 — aplicação localizada no diagnóstico 1

O diagnóstico 1 explicita quatro partes de massas iguais; resolução preservada. Os 197 artigos permanecem byte a byte idênticos. O JSON registra a fotografia efetiva do módulo e a [entrega de aplicação](../evidencias/QA-09/aplicacao-diagnostico01-r1/entrega-r1.md) identifica a base anterior e a atual. Evidências e aceites históricos permanecem vinculados às respectivas versões e sua validade para alterações posteriores depende de revisão. A aplicação não aprova QA-09.


## QA-09 — aplicação localizada nos diagnósticos 6 e 9

O diagnóstico 6 declara exclusividade das transferências de energia e o 9 esclarece o ciclo e as trocas totais; soluções e os 197 artigos foram preservados. O JSON e a [entrega](../evidencias/QA-09/aplicacao-diagnosticos06-09-r1/entrega-r1.md) apontam à fotografia efetiva. As revisões e aceites históricos permanecem vinculados às versões examinadas. A aplicação aguarda auditoria independente e não aprova QA-09.


## QA-09 — aplicação dos diagnósticos 12, 14, 19, 26, 27 e 28

Foram explicitadas as condições dos balanços, preservando as resoluções e os 197 artigos. O JSON aponta à fotografia efetiva; a [entrega](../evidencias/QA-09/aplicacao-diagnosticos-seis-r1/entrega-r1.md) identifica hashes e versão anterior. A aplicação requer auditoria independente; as provas e os aceites históricos mantêm seus respectivos limites e versões. Não há aceite global de QA-09.


## QA-09 — aplicação localizada na oficina 8.1

Quatro blocos da oficina tiveram a atribuição de temperatura e as condições de balanço esclarecidas; os 197 artigos foram preservados. O JSON aponta à fotografia efetiva, e a [entrega](../evidencias/QA-09/aplicacao-oficina-r1/entrega-r1.md) registra hashes, limites e versões. A aplicação requer auditoria independente; QA-09 não está aprovado.

## QA-09 — aplicação localizada dos exemplos 011 e 013

Os exemplos de tanque e compressão explicitam exclusividade de trabalho e calor líquido, preservando as soluções. Os 197 artigos e registros individuais mantêm-se idênticos; o JSON aponta à nova fotografia. A [entrega](../evidencias/QA-09/aplicacao-exemplos-011-013-r1/entrega-r1.md) registra a versão, os testes e os limites. A aplicação aguarda auditoria independente e não aprova QA-09.

## QA-09 — aplicação localizada de correções de conteúdo

Aplicação de candidatas revisadas; os 197 artigos e registros individuais foram preservados. Consulte as edições e sua revisão na pasta `aplicacao-razao-percentual-r1`. A aplicação requer auditoria independente e não encerra QA-09.

## QA-09 — aplicação localizada em flashcards, resumo e ficha 80

Foram esclarecidas hipóteses em sete trechos de revisão e na ficha 80. Os 197 artigos e registros, 99 fichas não alvo e MathML do formulário foram preservados na verificação estática. Esta aplicação requer auditoria independente e não encerra QA-09.

## QA-09 — aplicação localizada das hipóteses de pressão e fichas 40/67

Foram esclarecidas hipóteses em trechos da aula e nas fichas 40/67. Os 197 artigos e registros, as 98 fichas não alvo e MathML do formulário foram preservados na verificação estática. Esta aplicação requer auditoria independente e não encerra QA-09.


## QA-09 — FUN-01 P3: redação sobre origem das colunas

O parágrafo da solução diferencia redundância ρ/v de afirmação sobre a origem instrumental dos dados; enunciado, dados e rubrica são preservados. Atualizou-se apenas o hash do artigo P3 no inventário oficial. A aplicação está sujeita a auditoria independente da versão efetiva e revalidação localizada de FUN-01, BAN-02, BAN-07 e BAN-08. QA-09 integral continua em correção.


## QA-09 — vínculo EnergyPlus 24.1 e condições em fichas 88/99

O vínculo de CO₂ foi atualizado para a seção HTML correspondente do EnergyPlus 24.1, e as fichas 88/99 tiveram hipóteses de regime permanente e de fontes térmicas explicitadas. Os 197 artigos e registros individuais foram preservados. Aplicação sujeita a auditoria independente e revalidação localizada; QA-09 integral continua em correção.


## QA-09 — aplicação conjunta de seis candidatas na fotografia r14

Foram explicitadas as hipóteses nas fichas 23, 58 e 59 e na base de eficiência isentrópica, identificadas as entalpias do diagnóstico 23 e contextualizada a referência OpenStax com contraponto MIT. Os 197 artigos e seus registros individuais foram preservados. A versão requer auditoria independente e revalidação localizada; QA-09 integral permanece aberto.


## QA-09 — referência WIKA na fotografia r15

O endereço WIKA da lista de fontes foi atualizado à página brasileira dos modelos 111.16 e 111.26. Os 197 artigos e seus registros individuais foram preservados. A versão requer auditoria independente e revalidação localizada; QA-09 integral permanece aberto.


## QA-09 — aplicação conjunta r16, 30/10/2026

Aplicadas cinco candidatas aprovadas na aula e no formulário; fotografia efetiva e efeitos aguardam auditoria independente. Os 197 registros permanecem inalterados. Ver evidências em `auditoria/termodinamica/evidencias/QA-09/aplicacao-conjunta-r16-r1/`.


## QA-09 — aplicação intercooling r17, 30/10/2026

Aplicada candidata aprovada em teoria; fotografia efetiva e efeitos aguardam auditoria independente. Os 197 registros permanecem inalterados. Ver evidências em `auditoria/termodinamica/evidencias/QA-09/aplicacao-intercooling-r17-r1/`.
