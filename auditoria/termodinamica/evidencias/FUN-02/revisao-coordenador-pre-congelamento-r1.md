# FUN-02 — revisão do coordenador antes do congelamento

Data: 2026-10-27. Estas observações foram encaminhadas durante a autoria; não são parecer do Auditor nem rejeição de pacote ainda não entregue.

## Entropia e irreversibilidade externa

O rascunho do problema 3 afirmava que retirar apenas a reversibilidade térmica, preservando caminho mecânico e hipóteses de trabalho, faria deixar de valer δQ_real/T_gás=dS. Essa conclusão obrigatória é excessiva: um gás uniforme e internamente reversível pode trocar calor com uma vizinhança a outra temperatura, havendo irreversibilidade externa. Nas hipóteses diferenciais ainda mantidas, δQ=C_V dT+p dV e sua divisão por T_gás fornece o diferencial de S do gás ideal. Não se deve confundir essa possibilidade com uma identidade geral para qualquer sistema irreversível, nem substituir silenciosamente a temperatura do gás pela do reservatório.

Solicitado ao Corretor: delimitar sistema, temperatura de fronteira do lado interno, vizinhança e eventual geração interna no comando/solução/rubrica, sem exigir um balanço geral de entropia fora do escopo de FUN-02. [Purdue ME200, capítulo6, p2](https://www.purdue.edu/freeform/me200/wp-content/uploads/sites/29/2023/03/ME-200-Chapter-6.pdf) e [Wassgren, §3.6.7, eq3.141–142](https://engineering.purdue.edu/~wassgren/teaching/ME20000/NotesAndReading/Lec24_Reading_Wassgren.pdf) fundamentam o uso de temperatura na fronteira do lado interno e processo internamente reversível.

## Consumo de dados no programa

O rascunho de cálculo P2 codificava a observação −20 ln2 e limites dos ciclos, embora o JSON também os descrevesse. Solicitei consumir os valores numéricos do pacote (coeficiente separado, sem avaliar texto como código) e os limites dos ciclos, ou validar explicitamente que o programa atende apenas a esse conjunto fixo. Não se está exigindo biblioteca geral de propriedades ou calculadora universal.

## Verificações próprias já realizadas

- P1/P3 resolvidos a partir dos enunciados antes de consultar soluções/código do autor; seis combinações de trechos conferidas para crédito a alternativas válidas.
- P2 rederivado após receber resultados preliminares junto ao modelo; essa revisão não foi cega e está assim identificada.
- Figura SVG quantitativa criada e inspecionada no navegador, com descrição acessível; integração final ainda depende do Corretor.

O atendimento destas observações será conferido no pacote integrado. Elas não encerram FUN-02 nem liberam outro ID.

## Atendimento observado no rascunho revisado

O Corretor revisou comando/solução/rubrica de P3: a igualdade para gás internamente reversível não é rejeitada apenas pela irreversibilidade externa, as temperaturas são distinguidas e o caso de geração interna é delimitado. A expressão da variação conjunta gás+reservatório foi conferida com Q<0 e reservatório mais frio: o sinal é positivo. A teoria curta também foi atualizada.

O programa passou a consumir coeficiente numérico da observação, centro da família de defeito, limites e orientação dos ciclos. A identificação usa o fator analítico dos limites fornecidos. A execução local produziu49 verificações e concordância com os cálculos próprios na precisão de ponto flutuante; hashes e diferenças estão em reproducao-coordenador-r1.json. Esta constatação antecede o congelamento e não substitui o parecer independente da versão entregue.
