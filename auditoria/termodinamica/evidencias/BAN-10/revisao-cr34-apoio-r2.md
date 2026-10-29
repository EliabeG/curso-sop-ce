# BAN-10 r2 — apoio restrito a CR34 / R1-A

**Data:** 28/10/2026. **Papel:** apoio ao Corretor, não parecer de auditoria. Foram lidos o parecer `BAN-10-r1.md` em UTF-8 e as três notas primárias do MIT citadas abaixo. Não foram alterados produto, inventário ou evidências r1.

## Correção do diagnóstico anterior

A proposta do Corretor é cientificamente adequada: CR34 pode permanecer como estudo guiado de esclarecimento de modelos, sem alegar que a presença de trabalho adicional demonstra ambiguidade ou invalidade da afirmação oficial sobre aumento da energia interna.

Minha triagem r1 confundiu duas afirmações diferentes: **ΔU > 0**, que é o que o item afirma, e **ΔU = Q**, usada na resolução simplificada. Também tratou a escolha algébrica de trabalho no primeiro balanço como se bastasse para construir um processo possível. Esse diagnóstico deve ser substituído em r2, preservando r1 como registro histórico.

## Distinções que a nova redação precisa preservar

Para o balanço fechado com Q recebido positivo e W total produzido positivo:

\[
\Delta U+\Delta E_c+\Delta E_p=Q-W.
\]

Assim, **ΔU = Q se e somente se W + ΔEc + ΔEp = 0**, dentro desse balanço. Anular os três termos individualmente é condição suficiente, mas não necessária. Volume constante elimina o trabalho de fronteira associado à variação de volume; não autoriza, sozinho, identificar trabalho de fronteira com todo o trabalho. Isso esclarece a **igualdade**, sem refutar o **sinal** afirmado no original. [MIT, §2.1](https://web.mit.edu/16.unified/www/SPRING/thermodynamics/notes/node14.html).

Para estudar o sinal, declare um sistema de **massa e composição fixas**, gás ideal simples, estados inicial e final de equilíbrio no **mesmo volume**, temperaturas positivas e **cv(T) > 0** na faixa. Declare também que há quantidade positiva de calor entrando, **sem parcelas de calor saindo**, em temperaturas de transferência Tb finitas e positivas. Tb é a temperatura pertinente à transferência na fronteira escolhida, não automaticamente a temperatura uniforme do gás ou a de um reservatório distante.

O balanço de entropia é

\[
\Delta S=\sum_j\int\frac{\delta Q_j}{T_{b,j}}+S_{ger}>0,
\qquad S_{ger}\geq 0.
\]

A identidade entre estados do gás ideal fornece, usando cv específico por massa,

\[
\Delta S=m\int_{T_1}^{T_2}\frac{c_v(T)}{T}\,dT
+mR\ln\frac{V_2}{V_1}
=m\int_{T_1}^{T_2}\frac{c_v(T)}{T}\,dT.
\]

Como o integrando é positivo, ΔS > 0 implica T₂ > T₁. Logo

\[
\Delta U=m\int_{T_1}^{T_2}c_v(T)\,dT>0.
\]

Não é preciso supor cv constante nem que o processo real seja reversível. A relação de entropia é uma identidade entre estados; não se substitui o balanço irreversível por `dS = δQ/T`. As relações do gás ideal constam do [MIT, §5.4](https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node40.html); a aplicação conjunta e a conclusão acima são uma dedução para o modelo declarado, compatível com a análise da segunda lei no [MIT, §5.5](https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node41.html).

**Consequência:** W não é um número livre que permita escolher ΔU ≤ 0 mantendo todas essas condições. Trabalho não transporta entropia. Um conjunto que satisfaça apenas o balanço energético, mas exija ΔS ≤ 0 com entrada térmica de entropia positiva, não é um contramodelo admissível. O argumento não exige W = 0; ele restringe conjuntamente as trocas e estados possíveis.

**Limite importante de linguagem:** “calor exclusivamente entrando” é mais forte que “calor líquido positivo”. Se houver entradas e saídas em temperaturas distintas, Q líquido > 0 não determina sozinho o sinal da integral de transferência de entropia. Não usar essa observação como uma nova declaração de invalidade do item: seria outra interpretação, que exigiria fronteira, trocas e admissibilidade física demonstradas. A proposta atual pode simplesmente explicitar a leitura de aquecimento e encerrar essa alegação de contramodelo.

## Redação sugerida

**Justificativa editorial:** “Este estudo guiado distingue a afirmação de aumento da energia interna da igualdade ΔU = Q usada em um modelo simplificado. A chave oficial C é coerente com a leitura usual de aquecimento isocórico do gás ideal. A presença de outro trabalho, isoladamente, não demonstra que a afirmação seja falsa. A atividade permanece sem pontuação por escolha pedagógica de esclarecimento, não por uma anulação técnica ou oficial do item.”

**Roteiro:**

1. O original afirma ΔU > 0 ou ΔU = Q? Escreva o balanço completo e a condição exata para obter a igualdade. Zerar cada termo separadamente é necessário ou apenas suficiente?
2. No modelo explicitado acima, use o balanço de entropia e a identidade do gás ideal para decidir o sinal de ΔS, ΔT e ΔU. Identifique as hipóteses usadas em cada passagem.
3. Uma proposta escolhe trabalho total para obter ΔU ≤ 0 na primeira lei, mantendo o mesmo volume e calor exclusivamente entrando. Explique por que satisfazer essa equação, sozinho, não demonstra um processo possível.

As duas relações de entropia devem estar ensinadas ou fornecidas antes da tentativa. O exercício pode pedir que o aluno interprete o sinal de uma integral de integrando positivo; não precisa exigir sua avaliação numérica.

**Autocorreção sem nota:** distinguir igualdade e desigualdade; obter a condição sobre a soma dos termos, sem transformar uma hipótese suficiente em necessária; usar corretamente a segunda lei e as propriedades do gás ideal; rejeitar trabalho arbitrário como prova de contramodelo; declarar o significado de calor exclusivamente entrando. Manter explícito que a letra documental não corrige a justificativa escrita.

## Metadados cognitivos proporcionais

- **formato.comando:** comparar a marcação com a chave oficial sem pontuação e justificar, por roteiro escrito, a diferença entre ΔU > 0 e ΔU = Q, as condições da igualdade e a restrição da segunda lei sobre um suposto contramodelo.
- **Pré-requisitos:** primeira lei total e convenção Q/W; trabalho de fronteira versus total; balanço de entropia de sistema fechado e temperatura de transferência; relações U(T) e S(T,V) do gás ideal com cv(T) > 0; distinção entre condição necessária e suficiente e sinal de integral com integrando positivo.
- **raciocinio.categoria:** `julgamento_delimitado`.
- **Etapas:** (1) identificar o alcance da afirmação oficial; (2) obter a condição exata da igualdade pelo balanço energético; (3) combinar o balanço de entropia com a identidade de estado para estabelecer o sinal; (4) avaliar o suposto contramodelo pelas duas leis e declarar o alcance da conclusão.
- **numero_etapas:** 4.
- **Nível estimado:** `intermediario`, **se esse roteiro de duas leis for efetivamente solicitado**. A integração da conservação com a restrição entrópica e a distinção necessária/suficiente ultrapassam uma substituição direta. A nota revela o contraste e a atividade fornece autocorreção: não é evidência de autonomia avançada nem dificuldade empiricamente validada. Se o roteiro se limitar a reconhecer uma conclusão pronta, não justificar elevação de nível apenas pelo texto da nota.
- **Vínculo/alcance:** apoio delimitado a C03 na redução do balanço e a uma parte de C04 na admissibilidade pela segunda lei. Caso C04 seja incorporada, sincronizar o vetor `competencias` com o alcance; não declarar cobertura integral. A justificativa é solicitada para estudo guiado sem nota, não certificação independente de domínio.

Esta nota corrige somente a fundamentação de CR34 e suas consequências pedagógicas. Não reabre os outros 196 itens nem altera a decisão de pontuação.
