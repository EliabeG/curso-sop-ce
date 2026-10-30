# QA-09 — auditoria independente de fronteiras, leitura matemática, leis e expansão livre

30/10/2026. Auditor `/root/next_examples`, distinto do autor `/root/reference_triage`. **Parecer: ajuste obrigatório localizado na definição geral de pressão; recomendação opcional para a premissa algébrica de Q.** Demais verificações abaixo conferem no recorte; não se aprova o curso inteiro, QA-09 ou uma alteração futura. Produto e controles não alterados.

## Identidade e reprodução

Examinei `revisao-r28-reference-2/entrega.md` SHA `55a7ae483bb0f18a771604bf35e5421f00db37eab09ac8e01a306995b6494a6c`, `identidades.json` SHA `a2d2c205016a3d2fdc1e73b3e0ecd358d447cc66573a71f48ddeb8b3ff24b6b8` e `verificar.py` SHA `25e0ef1d5a1ce3c12480a497263658c9310180bafaecad2eda4ba7aa8119f1ca`, executado sem escrita (`ok`). Fotografia atual e inventário SHA `9af8e2c9ffe509e40594d086a9ef4ad75127fb4ca873efb305d3144e08f3fc49` e `a58d7f0b0a5f097eef83ad83026ef49e801457b87f7cf2b2345c3dd915597c7c`. Meu teste independente somente leitura `auditoria/termodinamica/evidencias/QA-09/auditoria-revisao-r28-reference-2/verificar.py` SHA `47a84654b6872a888010cb5f9adc5842afdce3d4bb70a0dc1243f41a0eea1c5f` reextraiu os quatro intervalos UTF-16 e respectivos hashes e recalculou os contrastes. Os programas não interpretam automaticamente o alcance de uma frase.

## Pressão: correção localizada necessária

Em `base-leitura-matematica`, a frase “Pressão é força normal por área: p = F/A” apresenta uma igualdade escalar como definição sem distinguir valor local de média sobre área finita. Isso pode induzir um resultado local incorreto em problema de pressão variável, mesmo que o exemplo aritmético esteja certo. Numa face plana de 0,010 m², cada metade de 0,005 m² com pressão uniforme de 10 e 30 kPa tem forças normais 50 e 150 N; o total é 200 N, e F/A=20 kPa é a média na face, embora as pressões locais sejam 10 e 30 kPa. Para a força vetorial em superfície curva, as direções normais devem ser integradas, não se supõe uma única direção. [NASA, forças de pressão](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/aerodynamic-force/) distingue aplicação local e soma vetorial.

Recomendo **ajuste obrigatório** no próprio bloco: indicar que, em face plana de área positiva, F⊥/A é pressão média e também a pressão local se uniforme, ou apresentar a definição local diferencial apropriada. A ficha 05 já faz essa distinção mas não corrige automaticamente a afirmação da base. Preservar os 200 N, 0,010 m² e 20 kPa como média; não inferir que o problema diga explicitamente pressão uniforme.

## Isolar ΔT: melhoria, não erro demonstrado

O texto diz “de Q=mcᵥΔT, divida ...” no item de manipulação algébrica. A igualdade é apresentada como premissa condicional, não como lei universal afirmada para todo aquecimento. Para m·cᵥ≠0, a operação é válida. Se for interpretada como modelo físico, exige hipóteses adicionais: por exemplo gás ideal de massa fixa e cᵥ constante, volume fixo, sem outro trabalho relevante e ΔEc/ΔEp desprezíveis. Com m=1 kg, cᵥ=0,718, cp=1,005 e ΔT=100 K, essa hipótese isocórica dá 71,8 kJ; uma trajetória isobárica quase estática com apenas trabalho pΔV daria 100,5 kJ. O caso isobárico simplesmente não satisfaz a igualdade inicial; não refuta a manipulação proposta. A [primeira lei do MIT](https://ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_4.htm) sustenta a dependência do balanço das interações.

É **recomendável, não obrigatório por erro demonstrado**, acrescentar que Q=mcᵥΔT é premissa algébrica e m·cᵥ≠0, ou um exemplo físico suficiente explicitamente delimitado. Não se deve afirmar que volume fixo seja a única condição possível para a igualdade.

## Demais blocos

Fronteira: sistema fechado impede massa de atravessar, mas pode trocar energia; volume de controle admite massa e um conjunto isolado não troca massa nem energia. Os modelos de fechamento, rigidez e isolamento são distintos. Leis: entropia gerada não negativa, e a frase sobre terceira lei restringe-se ao cristal puro perfeito; isso não cobre entropia residual geral. Expansão livre: recipiente rígido, fechado, isolado e sem outro trabalho, com variações macroscópicas desprezíveis, dá ΔU=0; para gás ideal, T final de equilíbrio é igual à inicial, mas ΔS=0,287 ln 2≈0,198933 kJ/K para os dados e Sger=ΔS>0. [MIT, expansão livre](https://ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_7.htm) apoia o contraste. Números dos contramodelos são sintéticos e não extraídos das fontes.

Escopo restrito aos quatro fragmentos e aos exemplos descritos. Fontes consultadas diretamente nesta revisão; não foram testados navegador, leitor de tela, estudantes, nem revisão humana ou certificação externa.
