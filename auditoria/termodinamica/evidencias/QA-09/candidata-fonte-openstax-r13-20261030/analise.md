# QA-09 — candidata para contextualizar fonte sobre expansão adiabática

Data: 30/10/2026. Corretor automatizado `/root/reference_triage`. **Candidata isolada, não aplicada; aguarda auditoria independente.** Responde ao achado do [parecer de referências FUN-02](../../../pareceres/QA-09-referencias-fun02-r12-r13-auditoria-independente-20261030.md), sem encerrar QA-09.

## Problema e proposta

O vínculo à [OpenStax, University Physics 2, §3.4](https://openstax.org/books/university-physics-volume-2/pages/3-4-thermodynamic-processes) é pertinente à discussão de processos, mas sua seção de processos adiabáticos afirma em termos gerais que a expansão realiza trabalho e reduz temperatura. Uma expansão livre adiabática de gás ideal, em recipiente externo rígido e isolado, pode ocorrer sem trabalho ou calor na fronteira externa; desprezando ΔEc/ΔEp, ΔU=0, de modo que a temperatura final de equilíbrio é igual à inicial. O [MIT, Thermodynamics, §4.2](https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node33.html), consultado diretamente em 30/10/2026, descreve explicitamente esse contraponto. Isso não nega que a expansão adiabática contra pistão com trabalho resistente possa reduzir a temperatura.

Em vez de apagar ou alterar a fonte histórica, a proposta mantém o vínculo OpenStax e acrescenta, no mesmo parágrafo, a limitação da frase geral e o contraponto MIT com hipóteses explícitas: gás ideal, expansão para vácuo, recipiente rígido e isolado, sem outros trabalhos, ΔEc/ΔEp desprezíveis e comparação dos estados de equilíbrio. A ressalva é para o leitor da aula, não apenas para a auditoria. O modelo não estende o resultado a gases reais, nem confunde a falta de calor com reversibilidade.

## Identidade e ensaio

Aula r13 `modulos/e1-termodinamica.html`, SHA-256 `f19000a7ddb1f3552b9633b0efec266fb3f6c5e5065808505a2f65b2005aefbc`; inventário r13, SHA `0df99b79bcc2350581fcdded72435d30d07858de237a549e6228ca73682f8d9b`. O elemento `<p>` em `#fun02-processos`, UTF-16 245623–246179, é único. Seu fragmento original SHA-256 `37b90e79163a716c0b4e7693eca618655655d30d9f987568c76044d326839fc4`; a candidata SHA `f9e1e4bebdb5966ee15c710dbb8ad8bdbf96eeffed8995fed1af24b5528426b0`; exclui-se a quebra final dos arquivos isolados. O [manifesto](manifesto.json) e os arquivos `original.html`/`candidata.html` preservam a prova do delta.

O verificador [somente leitura](verificar.mjs) foi executado da raiz; passou a verificação das bases, posição, unicidade, cópia exata do texto original antes da adição, parser, dois vínculos e 197 artigos preservados em ordem e por hash. A simulação em memória gera HTML SHA `f4c9c2af55daf072fc60498f369960a90b01d853593ddda8cae846222d32946c`. Não houve teste em navegador real, acesso programático à rede pelo verificador nem aplicação ao HTML efetivo. A fonte MIT aponta para um recurso externo que pode mudar ou ficar indisponível.

## Encaminhamento e impacto

Solicita-se Auditor distinto para verificar fonte, interpretação, hipóteses, os dois vínculos e a versão dos arquivos. Caso aprovada e aplicada, a mudança acrescenta uma referência externa e texto direto, altera SHA do HTML e offsets posteriores; é preciso inventário e mapa novos, conferência dos 197 artigos, referências/recursos e revalidação dos aceites FUN-02/BAN relevantes ao alcance afetado. Após aplicação, nova auditoria deve ler a versão efetiva. Esta proposta não altera outras disciplinas, não comprova nível avançado nem libera o próximo ID.
