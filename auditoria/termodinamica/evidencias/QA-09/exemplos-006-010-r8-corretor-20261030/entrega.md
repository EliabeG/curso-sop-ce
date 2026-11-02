# QA-09 — reconciliação e recálculo EX-006–010 na fotografia r8

Data: 30/10/2026. Corretor: agente automatizado `/root/qa_examples`. Estado: **aguardando auditoria independente da fotografia r8**. Esses blocos receberam apoio independente anterior, não são ocorrências sem qualquer exame histórico; este trabalho confere novamente a versão r8 e respectivas bases, sem transferir aceite automaticamente. Não houve alteração de conteúdo. QA-09 integral permanece pendente.

## Identidade e reprodução

`modulos/e1-termodinamica.html` tem SHA-256 `57b13f0d6386764f1cc46ce543013b0eb75f7bfa97ffbd63ea331f38bfc5af8c`; o inventário r8 `ae75a258398c385398567457d98ebd49b9838c0c9a4eedc69ea8d2d72981b687`. Os cinco EX são IDs do mapa histórico e seus fragmentos brutos aparecem uma vez cada no documento, seção e contexto do inventário r8; posições UTF-16 e hashes individuais constam em `resultado.json` SHA-256 `be7ae2dd51e69711ade463bfe791e3819d558972fc619df0c18c9300fab77401`. A comparação por contexto incluiu o título; cada bloco ancestral `div.bloco-aula` das cinco bases foi extraído novamente e tem hash idêntico aos identificados no [adendo independente anterior](../../../pareceres/QA-09-exemplos-06-10-bases-ex008-adendo-independente-r1.md). Isso confirma os blocos dessas bases na fotografia, não garante todas as dependências externas ou gera aceite automático.

Reproduzir pela raiz: `node auditoria/termodinamica/evidencias/QA-09/exemplos-006-010-r8-corretor-20261030/conferir.mjs`. Ele lê os arquivos, confere hashes, posições, títulos e bases, refaz a aritmética e só escreve na saída padrão. SHA-256 `b3efe08ce5c8e3d38fc9eee8cc4734ba58e75e7265ef309b069c2de06c641f6d`. O programa usa parser comum ao projeto e dados digitados na rotina; não substitui leitura das hipóteses nem revisão científica independente.

## Recálculo

| ID | Modelo e conta | Conclusão |
|---|---|---|
| EX-006 | Gás ideal, massa e composição fixas, pressão e temperatura absolutas: p₂/p₁=1,5, V₂/V₁=1,2 e T₂/T₁=1,5×1,2=1,8. | T₂ corresponde a 180% de T₁ e o aumento relativo é (1,8−1)×100 = **80%**, não 180%. Razão de temperatura absoluta, não °C. |
| EX-007 | Mistura ideal da base, mesma temperatura e fase de referência, desprezando o fator de intensificação, de forma que pressão de saturação é a mesma: pv₂/pv₁=0,60/0,80=0,75. | Pressão parcial cai **25%**; a umidade relativa diminui 20 pontos percentuais ou 25% relativamente ao valor inicial. Temperatura diferente exige outras pressões de saturação. |
| EX-008 | Fases de substância pura, T e p fixas; avaliação local dG=(μv−μl)dn=(7−5)×0,02=0,04 kJ=40 J para a direção líquido→vapor. | Sinal positivo desfavorece essa direção localmente. Para interpretar como variação finita exata, adicionalmente é preciso que as fases puras subsistam, potenciais permaneçam constantes a T e p fixas e efeitos interfaciais sejam desprezíveis; não generalizar a misturas. Dados fictícios, não propriedades medidas da água. |
| EX-009 | Gás ideal de composição fixa com cp(T)=0,90+0,0002T, T em K e cp em kJ/(kg·K): integral 0,90×200+(0,0002/2)(500²−300²)=180+16. | **196 kJ/kg**; cp(300)×200=0,96×200=**192 kJ/kg**. Para esta função linear, cp(400)×200=0,98×200=196; isso não generaliza a qualquer função. |
| EX-010 | Turbina no contexto de regime permanente, adiabática, Ec/Ep desprezíveis; entalpias de mesma referência. | w=3.000−2.600=**400 kJ/kg**; 2×400=**800 kW**. O balanço fornece trabalho líquido não associado ao escoamento; os valores não validam estados reais de vapor. |

Resultados são aritmeticamente exatos para os números nominais do modelo; não foi informada incerteza instrumental. Particularmente, o sinal de EX-008 é local: a notação diferencial não deve ser tomada como validação genérica de um processo finito fora das condições citadas.

## Fontes e alcance

- [MIT, equilíbrio de fases em um sistema de um componente](https://ocw.mit.edu/courses/5-60-thermodynamics-kinetics-spring-2008/b312114e4e885b69b5746dcad660cc4f_lec_18.pdf): potencial químico e equilíbrio entre fases, para análise de EX-008.
- [ASHRAE, Psychrometrics, Fundamentals 2021](https://handbook.ashrae.org/Handbooks/F21/SI/F21_Ch01/F21_Ch01_si.aspx): relações psicrométricas ideais e limites de aplicação, para EX-007.
- [DOE, Fundamentals Handbook, Volume 1](https://www.energy.gov/sites/default/files/2026-04/DOE-HDBK-1012-92_VOL1.pdf): conservação e entalpia em escoamento, para EX-010; parâmetros aqui são didáticos, não extraídos de tabelas.
- Fontes e análises anteriores adicionais estão no parecer e adendo citados. Fontes externas consultadas em 30/10/2026; não houve captura local nem hash destas páginas.

Aguarda Auditor distinto. O recorte não reavalia todos os números nas cinco bases como ocorrências independentes, os demais exemplos, figuras ou QA-09 completo. Nenhum teste em navegador, teste com alunos, revisão humana ou certificação externa foi realizado.
