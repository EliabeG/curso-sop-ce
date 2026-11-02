# QA-09 — auditoria independente da candidata isentrópica r2

Data: 30/10/2026. Auditor: agente automatizado `/root/next_graphics`, distinto do Corretor `/root/next_theory`. **APROVADA apenas a proposta isolada r2** no alcance abaixo. O HTML do curso ainda não foi alterado por esta proposta; a versão efetiva após eventual aplicação requer nova auditoria. Não encerra QA-09 nem libera outro ID.

## Identidade e alterações

A proposta responde ao parecer `QA-09-teoria-segunda-lei-entropia-r13-auditoria-independente-20261030.md`. A primeira versão omitia explicitamente a composição comum e fixa usada para comparar entalpias à mesma pressão; solicitei ao Corretor essa condição e examinei a versão r2. Sua análise tem SHA-256 `95aa2c441da0d5a58cea23bec1d1519018d408d47c1fe7976ebbc5c32a576dd9`, manifesto `386ca34f0ccb2ce97d09168da4ff718685ce031abb8e94dbaa46f54c7ad6914d`. Aula r13 SHA-256 `f19000a7ddb1f3552b9633b0efec266fb3f6c5e5065808505a2f65b2005aefbc`; inventário r13 `0df99b79bcc2350581fcdded72435d30d07858de237a549e6228ca73682f8d9b`. Original do contêiner `base-isentropica` em UTF-16 331818–337684, SHA `c8a1b942f070d194b11f44fc8f8d190cba5571cf668cba384de6864816558d7b`; candidata r2 SHA `f73c2ca592fb347f95152429d99bb200a0512d66867cf444b7f513c55cc8e212`, sem quebra final dos arquivos isolados.

`evidencias/QA-09/auditoria-candidata-isentropica-r13-r2-20261030/verificar.mjs`, SHA-256 `3b8d01401d4167632e2243d03ba1e44db5ed4a51de928bce1e907967125fc08a`, conferiu as três trocas literais únicas, hashes, posição e comparação integral da candidata e produziu somente em memória HTML SHA-256 `3c4786f6eb27d2e602efb8c833e0d405dafa4bb61482216716dbed72465be16b`. Na simulação, 197 artigos, 734 elementos MathML, 1.432 elementos `<a>` e a sequência de IDs foram preservados. Isso não equivale a teste de navegador nem à inspeção da futura versão efetiva.

## Hipóteses, dedução e contramodelo

A r2 declara regime permanente, uma entrada e saída, equipamento adiabático, apenas trabalho de eixo, ΔEc/ΔEp desprezíveis; mesma substância de composição fixa, sem reação ou mistura, e referência adiabática internamente reversível com mesmo estado de entrada e pressão de saída. As diferenças real e de referência são positivas nos sentidos de turbina e compressor, mantendo razões definidas. A candidata identifica esse conjunto como modelo de comparação, sem afirmar que todo equipamento real seja adiabático.

Do balanço estacionário de energia no modelo, `w_t=h₁−h₂` na turbina e `w_c=h₂−h₁` como consumo no compressor. Com mesmo estado de entrada, mesmas pressões de saída e composição fixa, a condição adiabática dá s₂,real≥s₂,s=s₁; à pressão final constante, `dh=T ds` para estados de equilíbrio da mesma substância, e para T>0 obtém-se `h₂,real≥h₂,s`. Logo a queda de h e trabalho produzido da turbina não superam a referência, e o aumento de h e consumo do compressor não ficam abaixo dela. A redação da candidata vincula expressamente as frases à comparação adiabática, preservando os sinais e os índices originais.

O contramodelo fora do domínio adotado continua demonstrando a necessidade da condição: turbina estacionária com T₁=1000 K, T₂s=700 K, T₂=800 K, cp=1 e R=0,287 kJ/(kg·K), q=200 kJ/kg recebido, mesma p₂/p₁≈0,288584 e ΔEc/ΔEp desprezíveis. `w_real=400` e `w_s=300 kJ/kg`, enquanto a razão das quedas de entalpia é 2/3; `s_ger≈0,033531 kJ/(kg·K)>0` com fronteira a 2000 K. É uma conferência de balanços com dados fictícios, não projeto de equipamento. A exclusão de q relevante na r2 impede usá-lo indevidamente como caso da fórmula reduzida.

As [notas MIT, §6.9](https://web.mit.edu/16.unified/OldFiles/www/SPRING/thermodynamics/notes/node51.html), consultadas para o parecer do achado, apresentam eficiências adiabáticas para comparação à mesma razão de pressão com hipótese de energia cinética desprezível no modelo; não estabelecem a aplicabilidade universal da expressão. A r2 acrescenta condições para a forma didática aqui tratada.

| Critério localizado | Resultado |
|---|---|
| Regime, balanços e referência | Atendido na r2, para o modelo explicitado. |
| Mesma composição e domínio de razões | Atendido; condição foi acrescentada após a revisão da r1. |
| Frases sobre irreversibilidade | Atendido quando vinculadas à comparação adiabática descrita. |
| Preservação da marcação, fórmulas, artigos e links | Atendido na simulação, com os limites acima. |
| Aplicação, revalidação e QA-09 integral | Pendentes de versão efetiva e Auditor distinto. |

Após aprovação da coordenação para aplicação, conferir novamente base e hashes, gerar fotografia/mapa novos, reconduzir validação estrutural e analisar impacto em referências e pareceres anteriores. Uma futura auditoria deve examinar o texto aplicado, os vínculos e a validade delimitada dos aceites anteriores; não transferir automaticamente o aceite da r2. Não houve teste em navegador real, leitor de tela, aplicação com alunos, revisão humana ou certificação externa.
