# BAN-10 r1 — leitura das decisões

Data: 27/10/2026. Autoria: Corretor AAA, agente automatizado. Documento de entrega para revisão, sem aprovação própria.

A triagem de apoio leu os 197 itens da base FON-09 e registrou motivo por ID. O Corretor examinou os candidatos, os pontos adicionais do Auditor, os roteiros integrados e as fontes técnicas. O coordenador obteve documentos oficiais, renderizou páginas e fez a conferência visual registrada nos três relatórios abaixo. São papéis distintos; nenhum desses apoios é o parecer final do Auditor.

## Resultado concreto

Nove itens passaram a estudos críticos, com roteiro de justificativa e autocorreção sem nota: **CR04, CR09, CR24, CR34, CR35, CR39, CR62, CR79 e CR80**. As letras oficiais ficam preservadas. A função real do banco deixa esses itens fora do numerador e do denominador do treino, inclusive com marcações antigas. O feedback informa somente concordância documental, sem classificar a leitura técnica como certa/errada. Nenhuma mudança representa anulação oficial.

**CR51, CR55 e CR68 permanecem no treino**, por decisões distintas. CR51 reconhece o ciclo Brayton convencional nomeado, sem estender sua descrição a todas as modificações reais. CR55 continua falso pelo resfriamento isocórico, independentemente da expressão anômala já presente na prova. CR68 afirma uma possibilidade coerente de redução da parcela radiativa sob condições comparáveis; não depende dos dados de água. Os dois detalhes FON-09 e o arquivo de dados foram preservados integralmente.

O caso CR39 teve duas leituras autorais: o apoio considerou suficiente o modelo usual de máquina térmica cíclica; o Corretor escolheu exclusão conservadora, pois o texto também nomeia motor de combustão e não explicita totalidade das trocas/fronteira. O roteiro pede que o estudante declare essa escolha. Essa diferença de decisão foi preservada, sem converter a chave C em gabarito oficial supostamente errado.

## Fontes e interpretações

O [registro individual de decisões](decisoes-r1.json) inclui para cada caso: fonte oficial, arquivo local, SHA-256, página física do PDF, número original, chave documental, hipótese adicional, motivo de uso, roteiro e análise autoral. A fonte técnica junto a cada análise permite localizar a fundamentação. A prova e o gabarito locais estão também acessíveis no artigo.

- [Conferência visual CR09/24/55/79](conferencia-visual-coordenador-r1.json): E/E/E/B; a expressão “pressão isentrópica” é oficial. No gabarito FGV, a referência correta é a página física 4, embora seu rodapé diga página 1.
- [Conferência complementar CR04/39/34/35/62](conferencia-visual-complementar-coordenador-r1.json): C/C/C/C/C, com contexto e omissões identificados.
- [Conferência CR51/80](conferencia-visual-cr51-cr80-coordenador-r1.json): C/D. A justificativa oficial de CR80, página 5, usa balanço sem acumulação; não acrescenta essa condição ao comando da página 4.
- [FON-09: origem e dados de CR68](../FON-09/conferencia-origem-r1.md): conferência herdada mediante identidade dos documentos e dos dados, sem nova consulta NIST.

A análise de CR04 usa a diferença dimensional entre expansividade e compressibilidade, conforme DeVoe, §7.1. CR09 distingue a unidade de base kelvin da unidade SI grau Celsius, conforme BIPM. CR24 separa a razão de pressões de substâncias diferentes da comparação da mesma amostra ideal, conforme a equação de estado. CR34/35 usam o balanço da energia total do sistema fechado; isocoria e adiabaticidade não apagam parcelas adicionais por si mesmas. CR62 distingue reexpansão de admissão efetiva. CR79 contrapõe radiação e condução sólida, sem deduzir predominância só do vácuo. CR80 distingue uniformidade espacial de regime permanente.

Os números dos dois contramodelos de CR79 foram calculados pelo coordenador em [registro separado](contraprova-cr79-coordenador-r1.json): são montagens autorais admissíveis, não medições nem dados da prova. A formulação publicada explicita superfície negra, área, temperaturas, condutâncias e transporte gasoso desprezado. Variar a condutância inverte a predominância sem contrariar os dados originais.

## Cobertura, persistência e limites

O [diagnóstico individual](triagem-apoio-r1.json) conserva hashes da base e distingue ausência de indício, modelo usual, candidato e melhoria futura. CR78, AV17 e AV37 têm encaminhamentos específicos que não demonstraram ambiguidade de resposta no recorte: desempenho do refrigerante não se resume a calor latente; comentário de distrator AV17 merece revisão; AV37 não depende do gráfico. Isso não equivale a auditoria integral numérica, gráfica ou de todos os distratores.

As versões AV correspondentes aos críticos foram lidas individualmente. Nenhuma exclusão foi herdada só por parentesco de tema. Os sete abertos FUN-01/FUN-02 não foram modificados. O novo roteiro não constitui avaliação reservada nem demonstração de autonomia; notas e soluções ficam disponíveis. CR79 foi reclassificado de iniciante para intermediário pela construção solicitada de dois casos, sem declaração de nível avançado.

Os 160 enunciados/alternativas/chaves CR/AV e suas digitais foram preservados. Por isso as respostas armazenadas continuam identificando a mesma escolha documental; não se presume que uma escolha antiga represente execução do novo roteiro. As 30 questões iniciais e seu registro não mudaram. Nenhum conteúdo de outro módulo, CSS, dados FUN-01/FUN-02/FON-09, schema ou validador mudou.

As verificações automatizadas e o navegador são evidências separadas. Os testes controlados executam a função real `iniciarBanco` com fixtures de DOM/armazenamento; não simulam aprendizagem ou leitores de tela. O aceite de BAN-10 pertence exclusivamente ao Auditor. BAN-07, BAN-08 e FON-01 globais continuam abertos.

## Reprodução documental

`integrar-r1.mjs` registra a primeira integração e bloqueia sua execução sobre uma base já alterada; houve refinamentos editoriais posteriores. Para reproduzir a versão final, os deltas completos `delta-html-r1.json` e `delta-js-r1.json` são a referência: aplicar cada substituição uma única vez às cópias em `antes/` reconstrói integralmente os dois produtos, como conferido em `reconstrucao-deltas-r1.json`. O delta do inventário separa alterações globais e campos dos 12 registros; o pacote preserva o JSON e o resumo finais.
