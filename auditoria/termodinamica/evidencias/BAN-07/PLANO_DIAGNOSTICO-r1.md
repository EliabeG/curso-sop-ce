# BAN-07 r1 — diagnóstico integrado e plano antes da edição

Data: 28/10/2026. Corretor/integrador: agente automatizado `/root/corretor_aaa`. Escopo exclusivo: BAN-07. **Produto ainda não alterado. Este plano depende da confirmação de fronteira do coordenador; não é parecer de aprovação.**

Base: `modulos/e1-termodinamica.html`, SHA-256 `0fc12a96fd30d366770a56c366fb61bc6a9fa7bd761e81fb40242a30f6dd78c7`.

## Evidência integral e completude

O [diagnóstico integrado](diagnostico-197-integrado-r1.json), SHA-256 `f7220fa6aa029f241f68df26a4117968099bd9c61e95866926a46fcc788f3354`, contém 197 registros únicos: 30 Q, 80 CR, 80 AV e sete problemas abertos. As 731 decisões individuais de opções cobrem 117 múltipla escolha × cinco opções e 73 C/E × duas opções. Nos sete abertos, a alternativa vazia é justificada pelo formato; solução, rubrica e família de respostas foram examinadas.

Os três diagnósticos originais são preservados e identificados com SHA no integrado. O integrador conferiu correspondência de IDs, hashes de artigo, seções obrigatórias e quantidade/ordem de opções com o extrato. A [conferência reproduzível dos 167 registros retomados](corretor/conferencia-recarga-r1.json) confirma 581 juízos individuais, nenhuma falta estrutural e identidade dos sete artigos abertos e cinco recursos aceitos. O integrado corrige somente os 80 localizadores textuais `av-e 1-XX` para `av-e1-XX` e registra as escolhas concretas de AV08/10, sem reescrever os originais do apoio.

Resultado: 163 manter, nove estudos críticos preservados, quatro esclarecer e 21 corrigir. Os nove críticos CR04/09/24/34/35/39/62/79/80 continuam documentais, fora da nota, com chave oficial e análise técnica distinguidas. Nenhuma alteração dos 80 CR ou dos sete abertos é proposta. Herança histórica com hash divergente não foi apresentada como identidade integral; a releitura atual é identificada por artigo.

## Fronteira proposta: 25 artigos

Nenhuma chave será trocada. São 20 novas digitais (oito Q e 12 AV) e cinco correções somente de comentário. O número 18 preliminar foi atualizado porque AV10 e AV58 terão alternativas corrigidas.

| Artigo | Alteração mínima proposta | Digital |
|---|---|---|
| Q02 | Declarar leitura manométrica +200 kPa relativamente à atmosfera de 100 kPa; explicar D como razão indevida 200/100=2 com unidade de pressão atribuída incorretamente. | nova |
| Q09 | Declarar sistema fechado, fronteira móvel, equilíbrio mecânico sem atrito, pressão conjugada a dV e ausência de outros trabalhos; pedir trabalho realizado pelo sistema. | nova |
| Q13 | Acrescentar por que cada combinação A–E acerta/falha, preservando análise das proposições. | preservada |
| Q15 | C: 135%→165%; comentário calcula a soma indevida (1000+650)/1000. | nova |
| Q16 | E: 25%→33,3% por (600−300)/(600+300); D explica 600/300=200% sem o complemento, distinguindo simples inversão dentro da fórmula. | nova |
| Q18 | Acrescentar análise das cinco combinações, preservando análise das três proposições. | preservada |
| Q19 | C: 45%→44,4% por 400/(400+500). | nova |
| Q24 | Manter C. A: água nos tubos, confundindo aquatubular; B: apenas vapor, confundindo superaquecedor; D: mistura direta de água e gases, ignorando parede; E: combustível antes da queima, confundindo alimentação. Sincronizar quatro refutações. | nova |
| Q26 | A: 3030→3060 kJ/kg; refutar uso de 3000+0,30(3000−2800), com referência errada para a entalpia final. | nova |
| Q28 | B: 60%→68,75%; explicar uso incorreto 2200/3200 em vez da razão de quedas. | nova |
| AV08 | D: 160→180 °C; explicar 20+2×80, tratando span como semiamplitude. | nova |
| AV10 | D: 180→0,18 kg/m³ e extensiva; explicar produto 12×0,015, unidade do produto incorreta e classificação extensiva falsa. | nova |
| AV17 | Refutar a afirmação sobre pressão parcial efetivamente escrita: quantidade fixa de vapor não torna pv independente de T; no modelo ideal pv=nvRT/V. | preservada |
| AV18 | Explicar A=600 por uso de ΔT=150 K como denominador no lugar de T1=300 K. | preservada |
| AV33 | Declarar ausência de outros trabalhos e interação energética relevante com membrana. Manter D e solução de ΔU=0 no modelo declarado. | nova |
| AV35 | A/E: −240/+240→−0,120/+0,120 kJ; explicar conversão indevida por 1000, com ou sem troca de sinal. | nova |
| AV37 | B: 1,5→5,37 kJ; explicar uso indevido de (300−273,15) °C em lugar de 300 K em T0Sger. | nova |
| AV38 | D: 20%→25%; explicar (500−300)/(500+300). | nova |
| AV45 | A: 100→333,3 kJ; explicar 1000×300/(600+300), denominador indevido, e eficiência acima de Carnot. | nova |
| AV48 | E: temperatura igual das correntes em todo regenerador; refutar pela ausência da diferença térmica necessária ao reaproveitamento passivo. | nova |
| AV50 | Explicitar compressor/turbina adiabáticos, regime permanente, EC/EP desprezíveis, comparação por massa e condições de entrada/pressão final equivalentes; ajustar solução à classe declarada. | nova |
| AV57 | C: 25%→0,50%; explicar esquecimento da conversão fração→porcentagem. | nova |
| AV58 | D: 800→300 kPa; explicar pressão final confundida com incremento p2−p1. | nova |
| AV64 | Refutar C distinguindo rotor que fornece energia e difusor que converte energia cinética em pressão; não validar literalmente pás no difusor. | preservada |
| AV73 | B–E: baixa área/volume; armazenar calor como definição de compacto; paredes necessariamente mais espessas para aumentar condução; aletas apenas estruturais. Refutar separadamente. | nova |

As fontes já lidas e registradas no diagnóstico sustentam os modelos. Para Q24, acrescentar à evidência a fonte primária Spirax Sarco, *Shell Boilers*: https://www.spiraxsarco.com/learn-about-steam/the-boiler-house/shell-boilers. A fonte foi consultada pelo coordenador nesta rodada. A plausibilidade dos erros é teórica; não há piloto com estudantes.

## Arquivos do produto que poderão mudar

1. `modulos/e1-termodinamica.html`: somente os 25 artigos da tabela. Preservar os outros 172 artigos, todo o conteúdo externo aos artigos, IDs, chaves, fontes/figuras oficiais e os elementos MathML existentes.
2. `assets/curso.js`: mudança estritamente condicionada a E1 para conservar tentativas das versões anteriores e informar que não contam nas versões revisadas. A alteração deriva das novas digitais de BAN-07; não encerra auditorias globais de persistência.
3. `assets/registro.js`: sincronizar apenas `modulos.e1.questoes` com as 30 digitais vigentes; demais módulos e metadados preservados.
4. `auditoria/termodinamica/inventario/inventario-questoes.json`: atualizar hashes/digitais e diagnóstico de BAN-07 dos registros efetivamente atingidos, sem declarar BAN-08 ou outros IDs concluídos.
5. `auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md`: sincronizar o resumo derivado do inventário e a identificação da versão.

Além desses cinco arquivos, escrever somente evidências e entrega de BAN-07: substituições exatas por artigo, mapa de identidade anterior→nova, verificação do delta, testes pertinentes, pacote congelado, manifesto SHA-256 e entrega r1. O coordenador controla `CONTROLE_AAA.json`, checklist e liberação; o Corretor não aprova sua própria entrega. Nenhum CSS, formulário, dado de propriedades, PDF, figura ou outro módulo requer edição.

## Tentativas, identidade e regressão

O mapa de identidade deve identificar os 197 artigos e demonstrar exatamente 20 digitais alteradas e cinco artigos com comentários alterados mantendo digital. As 20 versões novas exigem nova tentativa; nenhuma letra antiga será copiada para uma digital nova. Manter snapshot anterior e vínculo por ID.

Em Q E1, `lerEstadoModulo` conservará entradas antigas sintaticamente válidas de respostas, erros e `simulado.marcadas`; `resumirEstado`, renderização, filtro e portal continuam percorrendo somente digitais vigentes. Uma gravação subsequente não pode descartar o histórico. `estadoVazio` não pode causar apagamento automático quando somente histórico válido resta. A limpeza explicitamente solicitada pelo usuário conserva sua semântica documentada. Outros módulos permanecem com a regra anterior. O aviso de versões anteriores será exibido apenas quando realmente houver tentativas antigas.

AV já relê e conserva o mapa completo de digitais válidas; manter esse mecanismo. Acrescentar aviso proporcional de versões anteriores, sem criar migração de letras. Falha de leitura ou JSON inválido não autoriza gravar mapa vazio sobre dados anteriores.

Verificações obrigatórias após edição: reprodução integral do HTML pelas substituições aprovadas; releitura científica dos 25 artigos e conferência das cinco alternativas/combinações de cada um; equivalências e arredondamentos; mapa de digitais; preservação de todos CR/abertos e dos demais artigos; registro fora E1; recursos e MathML. Testar funções reais de persistência com armazenamento antigo/atual, erro, simulado, gravação subsequente, leitura bloqueada/JSON inválido e outro módulo. O coordenador realizará o teste de interface antes/depois em navegador CUA na origem temporária e fornecerá evidência atribuída. Nenhuma verificação futura é declarada executada neste plano.

O pacote será submetido ao Auditor independente `/root/auditor_aaa`. Só parecer explícito `APROVADO`, sobre a versão congelada, pode autorizar a seleção do próximo ID pelo coordenador.
