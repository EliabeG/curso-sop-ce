# QA-09 — pressão de fronteira, entalpia e calor na teoria, r9

Data: 30/10/2026. Autor: agente automatizado `/root/next_theory` como Corretor. Estado: **candidatas isoladas, aguardando auditoria independente; não aplicadas**. Esta revisão é parcial, não encerra QA-09 e não libera o próximo ID. Não foram alterados a aula, o formulário ou inventários históricos.

## Versão e localização

`modulos/e1-termodinamica.html` SHA-256 `2d6b8fb2f9c99e04d22c19d7b32bbc3eb20577459d9132e506f9c0acef3f2fc2`; inventário r9 SHA-256 `023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d`. Os deslocamentos abaixo são UTF-16 e só identificam a fotografia r9. Os campos de texto direto são capturados separadamente da marcação HTML completa; seus hashes não são os hashes do elemento integral.

| Posição | Seção | Hash do texto direto r9 | Exame |
|---:|---|---|---|
| 165435 | energia | `993922dc816b0c2684ae205a1890d227bb7e606884478239f87a8737e14063d8` | A expressão isobárica é precedida, no mesmo bloco de aula, do requisito de processo quase estático e de pressão na fronteira. |
| 197407 | energia | `6f856d492c2419d1f9eb718b90e9858baa8b1b9c6a8e1dd9826b447ef8d43768` | A tabela e a dedução de gás ideal têm contexto de massa fixa, trabalho de fronteira, ΔEc/ΔEp desprezíveis, calores constantes e processo quase estático. |
| 199954 | energia | `0ca5ea6093bb2e42c319ad85401e6ccf6c88ced790993a3d0bf5fb1391201c02` | Reação a pressão constante: o texto remete genericamente a “condições adequadas” mas não identifica a igualdade entre a pressão que determina o trabalho e a pressão de H. Candidata abaixo. |
| 200231 | energia | `1b536f3d105ae3b920527925a73a87322ee84c5848737cac4761f069ecd3198d` | Na reversão entre os mesmos estados, ΔH troca de sinal: −50→+50 kJ. Dobrar a extensão duplica a variação total, preservadas as condições e a estequiometria. |
| 405901 | aplicações | `d1ccb7c4e5542572cd3b76b3230e9c837723d93c8db05bd7b349f4cf412f7f0c` | Vaporização de massa fechada: a frase diz pressão constante e trabalho pV, mas não identifica claramente a mesma pressão no trabalho e em H. O trecho subsequente de vaporizador permanente já exclui trabalho não associado ao escoamento. Candidata abaixo. |

## Derivação e contraste de pressões

Para um sistema fechado, com ΔEc e ΔEp desprezíveis e somente trabalho de fronteira, a primeira lei dá `Q=ΔU+Wb`. Se os estados inicial e final possuem pressão termodinâmica p comum, `ΔH=ΔU+p(V₂−V₁)`. Assim, `Q=ΔH` segue quando o trabalho de fronteira efetivo satisfaz `Wb=p(V₂−V₁)`. Um processo quase estático e isobárico é condição suficiente usual; ela não é a única hipótese concebível, e não se está exigindo reversibilidade como condição necessária universal.

Contraste **algébrico ilustrativo, não um processo experimental ou um ciclo físico validado**: se ΔU=400 kJ, ΔV=1 m³, p dos estados=100 kPa e um modelo com pressão de fronteira de 80 kPa fornece Wb=80 kJ, então Q=480 kJ, enquanto ΔH=500 kJ. Esse balanço mostra quais igualdades adicionais são necessárias; não demonstra por si só uma trajetória realizável com pressão termodinâmica uniforme constante durante toda a transformação. A candidata declara diretamente o trabalho requerido em vez de afirmar que toda transformação irreversível viola a identidade.

No exemplo de gás ideal do texto 197407, usando valores artificiais m=1 kg, cp=1,005, cv=0,718 e R=0,287 kJ/(kg·K), ΔT=100 K, obtêm-se ΔU=71,8, W=28,7 e Q=100,5 kJ; `mcpΔT=100,5 kJ`. A condição quase estática aparece no trecho que introduz a tabela. Para a fase de vaporizar, `hfg=hg−hf` e `m hfg` são variações de entalpia entre líquido e vapor saturados sob as condições declaradas; a igualdade do calor ao resultado depende das hipóteses de trabalho e energia. No volume de controle permanente, a redução `Q̇=ṁhfg` exige balanço estacionário, mesma vazão, termos cinético/potencial desprezíveis e trabalho não associado ao escoamento nulo. A resistência elétrica citada no curso é, corretamente, uma possibilidade que requer manter trabalho no balanço.

## Candidatas, verificações e referências

O [manifesto](manifesto.json), SHA-256 `02c70956250a209aae22d4fc0a46d13ee33e4f61a8d2ba8c10d0817214cd98e0`, registra os dois fragmentos originais e candidatos, suas posições e hashes. Os arquivos `combustao-original.html` e `vaporizacao-original.html` mantêm os elementos completos; as respectivas candidatas modificam somente a hipótese/identidade de pressão, sem alterar a fórmula ou valores do restante. A candidata de vaporização explicita `W=p(V₂−V₁)` com p termodinâmica constante e exclui outros trabalhos. Cada arquivo isolado tem quebra de linha final; hashes de fragmentos no manifesto excluem-na.

`verificar.mjs` SHA-256 `eb9f61a00531617acbb99707452d96e248483ed3fdfe26eb4fffedb9b99d5621` foi executado a partir da raiz: verifica fotografia, posição, unicidade, hashes, substituições literais e contraste aritmético, sem gravar arquivos ou alterar produto. Esse teste não comprova realizabilidade de um processo com os dados fictícios nem substitui revisão científica.

Fontes consultadas em 30/10/2026: [MIT, derivação Q=ΔH sob hipótese de trabalho pV e pressão constante](https://web.mit.edu/10.213/oldpages/f99/supp/readings/qdh/index.html), [MIT, trabalho em expansão quase estática](https://web.mit.edu/16.unified/OldFiles/www/FALL/thermodynamics/notes/node17.html), [MIT, mudança de fase e calor isobárico reversível](https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node62.html) e [NIST, entalpia de vaporização](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=920759), §6.1. São fontes para os modelos, não origem dos números artificiais acima.

A candidata deve ser julgada pelo Auditor independente, que deve verificar se o enunciado de cada trecho estava realmente insuficiente, se o novo domínio é suficiente e se preserva a distinção entre sistema fechado e volume de controle. Depois de eventual aplicação, congelar nova fotografia, reconciliar os deslocamentos e dependências e reauditar a versão efetiva, incluindo o efeito na ficha 40 e aceites pertinentes. Este lote não examinou todo o conteúdo numérico, não utilizou navegador real nem foi validado com alunos.
