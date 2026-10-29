# BAN-07 r1 — diagnóstico dos 80 exercícios AV

Data: 28/10/2026. Autor: agente automatizado `/root/corretor_aaa/apoio_ban07`, apoio do Corretor. Este arquivo não é parecer do Auditor nem aprovação da entrega.

Foram lidos integralmente os 80 artigos `av-e1-01` a `av-e1-80`, com demonstração da chave e análise específica das 400 alternativas. O registro estruturado contém comando, suficiência, hipóteses, unidades, restrições, solução, erros representados, unicidade, arredondamento, comentários existentes, trechos exatos afetados e propostas.

**Resultado do diagnóstico:** 65 itens para manter, 13 para corrigir comentários ou distratores e dois para esclarecer o modelo. Nenhuma troca de chave é proposta. Alterações em enunciados ou alternativas exigirão nova identidade de resposta; correções apenas em comentários preservam essa identidade. Nenhuma proposta foi implementada.

## Base e verificações

- HTML: `modulos/e1-termodinamica.html`, SHA-256 `0fc12a96fd30d366770a56c366fb61bc6a9fa7bd761e81fb40242a30f6dd78c7`.
- [Registro completo em JSON](diagnostico-80-av-r1.json), SHA-256 `59fb1dfe1f0c83ce9626a67ad638bf358df329b54eae7c5d2c504cdd3e92ad4e`.
- 80 IDs únicos; nenhum ausente; 80 hashes de artigo iguais ao extrato fornecido pelo Corretor.
- Comandos, 400 opções e 80 chaves registrados sem divergência em relação à base.
- 37 cálculos necessários à resposta/unicidade conferidos em JavaScript, sem divergência dos resultados derivados manualmente. Expressões, valores e tolerâncias computacionais estão por ID; isso não encerra BAN-08.
- Oito ocorrências de figuras inspecionadas visualmente em sete arquivos distintos, com hashes registrados. Nenhum dado gráfico necessário contradiz o comando. A leitura visual não equivale a auditoria integral de acessibilidade ou ao fechamento de BAN-09.
- Nenhuma equivalência por arredondamento gerou uma segunda opção correta. Em AV73, B/E são negações de área próximas semanticamente, ambas falsas; o problema é a pobreza dos distratores.
- Ao terminar a conferência, o HTML permanecia idêntico à base. Só os dois arquivos próprios deste apoio foram escritos.

## Achados e propostas mínimas

| Item | Decisão sugerida | Achado concreto | Proposta |
|---|---|---|---|
| av-e1-08 | corrigir | Distrator aritmético arbitrário sem mecanismo de erro de medição identificado. | Substituir D por 40 °C e explicar que é metade do span, leitura indevida de alcance total como semiamplitude e ainda sem o deslocamento LI; alternativamente definir outro erro de faixa verificável. |
| av-e1-10 | corrigir | 12×0,015=0,18, não 180; falta explicar conversão para 15L e multiplicação indevida, ou trocar o valor. | Preservando180, explicar o erro composto concreto: converter0,015 m³ em 15L e calcular12×15=180, em vez de dividir, mantendo ainda unidade e classificação indevidas. Alternativa mais simples: trocar D por 0,18 kg/m³ e manter diagnóstico de multiplicação. |
| av-e1-17 | corrigir | A opção B fala da pressão parcial, não da umidade relativa. A refutação precisa mostrar dependência pv(T, V, nv). | Substituir comentário B por: Quantidade fixa de vapor não torna sua pressão parcial independente de temperatura. No modelo ideal, pv=nvRT/V; a volume fixo, aumentarT aumenta pv. |
| av-e1-18 | corrigir | O comentário não identifica o erro que pode gerar600 kPa: substituir T1 por ΔT no denominador de p2=p1T2/T1. | Preservar A=600 kPa e substituir comentário por: Usar450−300=150 K no denominador, em vez de T1=300 K, gera200×450/150=600 kPa. A equação exige a temperatura inicial absoluta, não a variação de temperatura. |
| av-e1-33 | esclarecer | Essas condições isoladas não anulam outros modos de trabalho; o modelo de expansão livre sem dispositivos precisa ser inequívoco. | Acrescentar ao enunciado: Não há outros modos de trabalho nem interação energética relevante com a membrana. Manter a chave D e explicar W total nulo nessas condições. |
| av-e1-35 | corrigir | Distratores numéricos definidos por duplicação arbitrária, não por erro físico ou dimensional rastreável. | Substituir A/E por −0,120 kJ e +0,120 kJ; explicar divisão indevida por 1000 quando ΔU já está em kJ, combinada ou não com erro de sinal. Preservar B e os distratores C/D. |
| av-e1-37 | corrigir | O distrator não está associado a um erro calculável dos dados. | Trocar B por 5,37 kJ, gerado por(300−273,15)×0,20; comentário explica uso indevido da temperatura ambiente em°C em vez de K. Se usar aproximação 273, explicitar5,4 kJ e o arredondamento correspondente. |
| av-e1-38 | corrigir | O comentário confirma a origem arbitrária, sem erro conceitual justificável. | Trocar D por 25%, obtido por(Th−Tc)/(Th+Tc); explicar que usar soma das temperaturas no denominador não é a relação de Carnot. Preservar chave E. |
| av-e1-45 | corrigir | É refutável pelo limite, porém o erro que produz100 não é identificado; critério BAN-07 também exige plausibilidade específica. | Substituir A por 333,3 kJ e explicar a aplicação indevida de Qc=Qh·Tc/(Th+Tc); o denominador correto na relação reversível éTh. Preservar E. |
| av-e1-48 | corrigir | Distrator sem erro técnico contextual plausível; acerto favorecido por alternativa obviamente estranha à regeneração. | Substituir E por as duas correntes tenham a mesma temperatura em todo o regenerador; explicar que diferença térmica nula impede a transferência passiva pretendida. |
| av-e1-50 | esclarecer | Não impõe regime permanente, ausência de calor nos componentes ou base específica. Um compressor refrigerado pode consumir menos que o isentrópico sem violar a segunda lei. | Acrescentar: Considere compressor e turbina adiabáticos, em regime permanente, sem diferenças relevantes de energia cinética ou potencial; compare trabalhos por unidade de massa, para os mesmos estados de entrada e pressões de saída de cada componente. Manter C e ajustar solução às condições. |
| av-e1-57 | corrigir | Distrator aritmético arbitrário sem mecanismo próprio de erro. | Trocar C por 0,50% e explicar que escrever0,50 diretamente com o símbolo% esquece multiplicar a fração por 100; manter D=50%. |
| av-e1-58 | corrigir | Não há operação ou concepção específica geradora de 800. | Trocar D por 300 kPa e explicar que esse é o aumento p2−p1, enquanto o comando pede a pressão final. |
| av-e1-64 | corrigir | A opção fala em ação de pás em um difusor; o comentário precisa separar rotor que fornece energia e difusor que converte energia cinética em pressão, em vez de validar literalmente a descrição. | Reescrever comentário C: Nos compressores dinâmicos, o rotor transfere energia ao escoamento e o difusor ajuda a converter energia cinética em pressão. Pistão e parafuso comprimem volumes aprisionados; não operam por esse mecanismo dinâmico. |
| av-e1-73 | corrigir | Quatro distratores contraditórios/triviais; B e E quase repetem área nula. Não confrontam erros plausíveis sobre compactação. | Manter A e reformular B–E com erros próximos: B baixa área de troca por volume; C grande volume de material para armazenar calor como definição de compactação; D paredes necessariamente mais espessas para aumentar condução; E aletas com função apenas estrutural sem aumento de área térmica. Explicar cada diferença e não prometer desempenho ou pressão de perda invariável. |

## Pontos de interpretação

**AV50:** as relações de eficiência isentrópica usadas na solução pressupõem a classe adiabática e condições de comparação equivalentes. A base local menciona referências adiabáticas, mas o comando não impõe claramente essa restrição ao equipamento real. A proposta torna explícitos regime permanente, ausência de calor nos componentes, variações cinéticas/potenciais desprezíveis e trabalho por unidade de massa. As definições e restrições estão no [MIT, §6.9](https://web.mit.edu/16.unified/www/SPRING/propulsion/notes/node51.html).

O JSON registra um contraexemplo didático próprio: gás ideal a 300 K, razão de pressões 4 e R=0,287 kJ/(kg·K). A referência isentrópica consome 146,45 kJ/kg; uma compressão isotérmica resfriada construída com trabalho 132,62 kJ/kg apresenta geração de entropia positiva 0,04421 kJ/(kg·K). Esse exemplo não pertence ao enunciado e não representa medição de equipamento. Ele mostra por que não se deve comparar classes térmicas distintas como se a referência isentrópica fosse um mínimo irrestrito.

**AV33:** o desenho e o contexto sustentam a leitura usual de expansão livre sem dispositivos de trabalho. Entretanto, rigidez e isolamento térmico não anulam, isoladamente, eixo ou trabalho elétrico. A frase proposta explicita o modelo e a interação desprezível com a membrana; não demonstra invalidação da chave dentro do modelo pretendido.

**AV16/17 e AV24:** foram lidas as bases ligadas aos itens. A aproximação psicrométrica ideal e o uso de pressão absoluta estão estabelecidos antes da resolução; não se exigiu repetir artificialmente essas definições. Em AV17, o ajuste solicitado é do comentário B, que precisa refutar a pressão parcial efetivamente mencionada na alternativa.

**AV64:** distinguir rotor que transfere energia ao escoamento e difusor que converte energia cinética em pressão evita validar literalmente uma descrição imprecisa. A distinção entre mecanismos dinâmicos e de deslocamento positivo foi confrontada com a [ASHRAE, capítulo 38](https://handbook.ashrae.org/Handbooks/S24/SI/S24_Ch38/S24_Ch38_si.aspx).

## Limites

A plausibilidade atribuída a cada erro é teórica. Não houve aplicação com estudantes, estatística de discriminação, revisão humana ou certificação externa. Não foram executados testes de interface ou persistência, pois não houve edição do produto. O Corretor deve integrar estes achados com os demais 117 itens e submeter a versão resultante ao Auditor antes de qualquer avanço de ID.
