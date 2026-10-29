# QA-09 — auditoria independente da aplicação dos diagnósticos 12, 14, 19, 26, 27 e 28, r1

Data: 29/10/2026. Revisor: agente automatizado independente `/root/auditoria_diagnosticos_seis`. **Veredito localizado: aplicação e reconciliação examinadas sem ajustes obrigatórios identificados.** Este parecer não aprova QA-09 global, não altera produto ou controle e não libera o próximo ID. A decisão de continuidade cabe ao coordenador após o atendimento integral do protocolo.

## Critério e alcance

QA-09 exige inventariar e recalcular cada ocorrência numérica fora dos 190 itens originais de BAN-08, incluindo exemplos, oficinas, 28 diagnósticos, fichas, novos projetos, figuras e explicações. Esta revisão cobre somente a aplicação dos seis fragmentos acima, seus cálculos e os efeitos localizados sobre BAN-02/07/08 e inventários; não cobre integralmente todas as ocorrências de QA-09. Conforme `PROTOCOLO_AAA.md`, aceite é vinculado à versão. O controle lido identifica QA-09 em correção e BAN-02/07/08 aprovados; este parecer não altera esses estados.

## Aplicação e mérito

Conferi os dois pareceres independentes das candidatas e seus hashes no manifesto. Para cada diagnóstico, o fragmento original ocorre uma vez no HTML anterior, a candidata uma vez no atual; o `antes` declarado ocorre uma vez no fragmento original e sua substituição pelo `depois` produz exatamente a candidata. Os seis arquivos candidatos e hashes de fragmentos conferem com o manifesto. A substituição sucessiva dos seis fragmentos no HTML anterior reconstrói **byte a byte** o arquivo atual e a fotografia posterior. Logo, preservam-se as bases, soluções, elos e demais trechos que não estão dentro dos seis deltas. Os seis blocos são exemplos explicativos, fora dos artigos pontuados.

Recálculos independentes para os dados nominais e as hipóteses explicitadas na versão efetiva:

| Diagnóstico | Conferência |
|---|---|
| 12 | `(140−50)/300 = 30%`; eficiência volumétrica `6/8 = 75%`, na base de sucção indicada. |
| 14 | Geração `60×2 = 120 W`, face `2 m²`, média `18 + 120/(6×2) = 28 °C`; demais faces isoladas. |
| 19 | `20×300 mL/min = 0,36 m³/h`; excesso `500 ppm`; `0,36/0,0005 = 720 m³/h`, mínimo no modelo estacionário. |
| 26 | `w_líq = 600+900−20 = 1.480 kJ/kg`; `q_in = 3.200 kJ/kg`; `η = 46,25%`, `q_out = 1.720 kJ/kg`. A existência de ciclo físico específico e seu atendimento à segunda lei não são demonstrados apenas pelo balanço. |
| 27 | Extração `(700−300)/(2300−300) = 0,20`; vazão remanescente `8 kg/s`; potência `8×250 = 2.000 kW`, conforme estágio estacionário adiabático descrito. |
| 28 | `dC/dt = [0,20+500(0,0004−0,0006)]/200 = 500 ppm/h` no instante inicial; `C_eq = 400 + (0,20/500)×10⁶ = 800 ppm`, assintótico sob condições mantidas. |

Os valores são condicionados aos modelos e dados nominais, sem alegação de precisão instrumental ou limite normativo de ventilação. A taxa inicial em D28 não é constante ao longo da evolução. O mérito dos detalhes das candidatas e suas hipóteses foi revisto nos dois pareceres identificados abaixo; a identidade comprovada estabelece sua aplicação à versão atual.

## Preservação e testes

Comparei todos os 197 elementos `article` do HTML anterior e atual: permanecem idênticos e na mesma ordem. Os 197 objetos individuais do inventário oficial são idênticos; a única chave de topo alterada é `fonte`, atualizada para o hash e fotografia do HTML atual. O Markdown possui apenas seção histórica acrescentada e o link nela apontado existe. O validador oficial, inspecionado quanto a gravação e executado sem redirecionar para evidências, retornou `ok=true`: 197 itens/artigos, 29 recursos, 1.263 links locais, nenhum erro ou aviso. Ele verifica estrutura e integridade, não mérito científico ou aprendizagem.

`assets/curso.js`, `assets/registro.js` e a ficha de fórmulas conservam os hashes da ponte anterior. Reexecutei o teste de persistência BAN-08, inspecionado antes da execução: passou nos cenários de histórico, contador, aviso, gravação/releitura, refazer e falhas de armazenamento. Usa funções reais com DOM e armazenamento simulados, concentra-se em AV42/45/52 e não é teste em navegador real nem acesso a dados pessoais. Os artigos e código das digitais preservados sustentam que os seis deltas não alteram as entradas de respostas pontuadas. O verificador do Corretor grava `verificacao-r1.json`; não o reexecutei sobre a evidência histórica. A análise independente acima não depende apenas da sua saída.

## Fotografias e mapa r4→r5

As fotografias contêm 11.396 ocorrências cada e a mesma lista de 197 artigos excluídos. Confrontei cada um dos 11.396 pares, na ordem, com ambas as listas: arquivo, tipo, tag, seção, âncora, ID, posição inicial e hash de fragmento conferem; IDs são únicos em cada fotografia. As seis regiões e seus acréscimos UTF-16 coincidem com os textos substituídos, e todos os deslocamentos iniciais previstos conferem. Há 971 IDs deslocados, 11.383 hashes iguais e 13 diferentes: seção ancestral, seis blocos e seus seis parágrafos. Os 13 intervalos atuais são reproduzidos pelas seis substituições nos intervalos anteriores. O segundo parser do Corretor informa validação estrutural, não comprova completude visual ou mérito numérico.

O mapa corresponde por ordem e posições, não fornece IDs duráveis. Igualdade de hash, em particular de texto direto, não demonstra identidade de contexto ou validade de provas dependentes, e não transfere aceite automaticamente. O mapa não cobre as listas separadas de referências e recursos; mudanças de suas posições não foram objeto de revalidação completa aqui. As evidências anteriores continuam vinculadas às versões e aos escopos que examinaram.

## Efeitos localizados sobre BAN-02, BAN-07 e BAN-08

- **BAN-02:** os 197 registros e artigos permanecem íntegros e os metadados de fonte foram atualizados. Não foi identificado efeito dos seis deltas nos atributos ou vínculos dos itens inventariados; o validador não substitui uma nova classificação pedagógica integral.
- **BAN-07 e BAN-08:** os 197 artigos, scripts e fichas preservados, com as alterações restritas às hipóteses dos seis exemplos, não indicam alteração das questões ou contradição com os cálculos conferidos nesta revisão. Esta é uma ponte localizada com a versão anterior e seus pareceres, não uma nova revisão integral de todos os gabaritos ou valores, nem aceite de QA-09.

## Quadro de critérios para esta entrega

| Critério | Situação e justificativa |
|---|---|
| Correspondência entre candidatas revisadas e versão efetiva | Atendido: reconstrução integral e hashes conferidos. |
| Hipóteses, cálculos, unidades e soluções dos seis diagnósticos | Atendido no escopo descrito; valores e limites acima. |
| Preservação de artigos, bases e inventário oficial | Atendido: 197 artigos e objetos idênticos; alterações exclusivamente declaradas. |
| Rastreabilidade das fotografias e mapa | Atendido para os 11.396 pares, suas posições e intervalos; limites de contexto e listas separadas indicados. |
| Efeito em BAN-02/07/08 e persistência | Atendido como ponte localizada, com teste simulado e limites acima. |
| Aceite integral de QA-09 e liberação do próximo ID | Não avaliados por esta revisão parcial; continuam sujeitos à revisão integral e à decisão do coordenador. |

Não há ajuste obrigatório identificado para esta aplicação localizada. Outras ocorrências, figuras e atividades de QA-09 permanecem sujeitas à conferência integral exigida pelo critério original.

## Identificação SHA-256

- HTML anterior `7541e7c4c8314922992e99e8b62b40342c2d938e6edeac67ef9f74b69f86c17c`; HTML atual e fotografia `49b0df4fe59dfd01913f4d41a5e6869705f4bf4d6ded251060f940cd5d12c91b`.
- Inventário oficial JSON anterior `6910b7b3ec783040859302bc21ebbd463a8faf447ddfce36bf745b5a261d0d55`; atual `9102ed042ff940c71604eadc361dcd3b4006a3bc1dc2a0e336cc0f2de0508edf`. Markdown anterior `e4b2a2db2aae0d574fc0fe2f44801a27edbd99a57cb75d2e2648da7c1e4a9be2`; atual `898830d59f4162be64954315f13a85aa27e53efbcadc61f25cd82b22901425ab`.
- `inventario-r4.json` `44d19642bcf39109edf620e7304580b7a8a686e7c42cfa7101fa3d118a79d054`; `inventario-r5.json` `e21bc074025815cb5708875f938cb8a0de200ebecc66c4a7c8997493c01b0ea4`; mapa `52486372721335228b8f38ed44b42b04452d665fb5ec7a2ddf221bfdea0c5265`; validação estrutural do Corretor `07a054c627915ea508f3fc2796ebdaf015cfe5a7f394abc3f5846992fbc1eb3f`.
- Entrega r2 `e0e508a169cdada3aea943aff89752b060197044dc7baafb794595d3dd0fdcd9`; manifesto r1 `89547c854fa312e3b23baf6f86530c5c99c80417421e3450be1df781de10efc7`; manifesto de verificação r2 `3d9c30ff8196cf9f436ca474c47130493af8ed0677b568660a96ed233ed9baf3`. Todos os arquivos listados neste último conferem com os hashes registrados.
- Parecer candidatas 12/14/19 `f18ab2020d36cbaa7494b62e16aa2b12436e1bd370c83347c9ee343479670d01`; parecer 26/27/28 `a05268e50dcb43fb4331b25ae3f217ce332df6c6a63dab0b504db925af51db95`.
- `assets/curso.js` `a20f4d19158073a9a1c48aabdfba8fa863b02063e16061c00b16448a6ccc2e13`; `assets/registro.js` `46da94527d6639fe0265bd766286f1ef39623966105e00bda3b31f21ca2c247c`; ficha `c27422b409a0a755448982c4074c6d6967fd3e91d7eae20274e218530f5c37b0`.
- Controle lido `9808b9a1bbe4d793b06491219762d587739f51277b215e482168f09de6176f42`; nenhuma modificação de controle foi realizada nesta revisão.
