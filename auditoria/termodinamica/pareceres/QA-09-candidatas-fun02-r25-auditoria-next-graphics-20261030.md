# QA-09 — auditoria independente de quatro candidatas FUN-02 r25

30/10/2026. Auditor automatizado `/root/next_graphics`, distinto do Corretor `/root/next_theory`. **APROVADAS as quatro candidatas em escopo isolado**, e a composição hipotética abaixo é estruturalmente reproduzível. Fui autor do parecer que identificou as ressalvas e trabalhei anteriormente em recursos FUN-02; não preparei nem apliquei as candidatas. A aprovação não se estende à aplicação efetiva, aos três artigos FUN-02 ou ao conjunto de QA-09.

## Conteúdo e contramodelos

- **Escala:** a nova frase fixa composição, referência extensiva coerente de U e trabalho de fronteira como única modalidade. A mesma trajetória T,V implica que p, U, Q e W dobram quando n dobra, sob o modelo ideal descrito; a capacidade molar não dobra. O contramodelo anterior com trabalho elétrico adicional deixa de satisfazer a premissa. A igualdade de trabalho de fronteira a p dV identifica a condição mecânica adotada.
- **Parciais:** a frase apresenta dV=0 como suficiente, admite coeficiente parcial nulo no caminho com dV≠0 e diferencia esse caso da independência de U em relação a V na região. O exemplo matemático f=x+(y−x)² em y=x, com dy=dx e parcial em y nula na curva, confirma a necessidade da distinção. O cálculo de θν e a notação de variáveis fixas permanecem.
- **Trabalho:** a premissa de exclusividade do trabalho de fronteira se aplica aos modelos de pistão descritos antes da equação para δQ e da tabela. O tanque rígido adiabático com entrada elétrica de 500 J, W_total=−500 J e ΔU=+500 J fica fora do modelo, como deve ocorrer; volume fixo sozinho não anula trabalho total.
- **Fator:** explicita trabalho total exclusivamente p dV reversível e conserva trocas térmicas reversíveis, S−S*=n c_v,m ln(T/T*)+nR ln(V/V*) e distinção entre exatidão matemática e entropia. As observações posteriores sobre temperatura da fronteira e irreversibilidade externa permanecem.

O raciocínio de sinais usa a [primeira lei do MIT](https://ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_4.htm), e as modalidades de trabalho são distinguidas em seu [capítulo 3](https://ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_3.htm). A decomposição e as variáveis fixas constam do [apêndice 4.1 da University of Washington](https://faculty.washington.edu/jcv2/CHEM452_WI2023/html/appendix_differentials.html). As fontes suportam modelos, não os dados hipotéticos dos contramodelos.

## Identidade e preservação

Fotografia r25 SHA `ea0a7e3877c0a0250dac3d9c993c7922a03400929eb7a5dad39fcb27e3263c7e`. Os manifestos de escala, parciais, trabalho e fator têm SHA respectivamente `89c37950a565509a6e0d7d54e657f4fd9b6cb174a30429108bfd943e60f8ac89`, `ef267f6481e3377334309a593ae70b7853fff7254c653b294896c03ba3574e37`, `5fee9a61920cfd5a93c0ed47049fbdd3de55676dc0742567ab77a4291d7c2960` e `5bfadef7a0fb1052ffb7c1e09fdf78719464ec6ba61a5f040a4b969e6ed5c21b`. Em cada trecho, o original extraído coincide com o fragmento e o candidato é exatamente a substituição única declarada. Quatro intervalos são disjuntos.

A aplicação conjunta simulada em memória resulta no SHA de aula hipotética `941fdd136277bd67502f332cd42e9a58c8d58362c36fa9d0176075220b83726b`. Preserva os 197 artigos em bytes, 734 MathML em ordem e atributos ID, href, src e ARIA comparados; não altera formulário ou outros documentos. `python3 auditoria/termodinamica/evidencias/QA-09/auditoria-candidatas-fun02-r25-independente-20261030/verificar.py`, SHA `9ad3272932612730f24e8a947315b18bffbef3677fa739dfedcea8a4f669542f`, reproduz essas verificações sem escrita em produto.

A combinação simulada não substitui verificação da aplicação efetiva, mapeamento de ocorrências e revalidação localizada. Fontes podem mudar; não houve teste de navegação, leitor de tela, alunos ou revisão humana. As candidatas permanecem não aplicadas e QA-09 aberto.
