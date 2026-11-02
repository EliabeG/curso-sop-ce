# QA-09 — auditoria independente das candidatas de primeira lei e entropia, r2

Data: 30/10/2026. Auditor automatizado `/root/reference_triage`, distinto do Corretor `/root/next_graphics`. **Veredito localizado: APROVADAS as duas candidatas r2 para aplicação**, sem aprovação automática da versão efetiva. QA-09 integral permanece aberto e o próximo ID bloqueado.

## Identidade e revisão da rodada

As propostas respondem ao [parecer de achados](QA-09-primeira-lei-entropia-r17-auditoria-independente-20261030.md). Na r1, o Auditor solicitou distinguir a taxa total de calor do fluxo local por unidade de área na integral espacial, para evitar ambiguidade dimensional; o Corretor preservou a r1 e apresentou r2 com essa correção. Esta revisão examina a proposta r2, não a aplicação ao produto.

Aula r17 SHA-256 `6b0df1096d0b6de6995ffc51bf8489cb45ab954a7aabdeb3f48d068c9777c57c`; inventário r17 `b8eae39cc72cf807d7b84aad7e7a38423168b809231bc3b7f08c439d6d25163b`. [Análise do Corretor](../evidencias/QA-09/candidatas-primeira-lei-entropia-r17-20261030-r2/analise.md) SHA-256 `dca76355c943e7b44ee65ba7261ea631295df27a81d0e7e6a7c2ac4ac209a300`; manifesto SHA `bc1d49ea7be22c50750a6a32440e69545f6ed3c0a438e079909a570dc6cded11`.

Os blocos `base-primeira-lei` (UTF-16 157256–162652) e `base-entropia-escoamento` (426459–441261) foram verificados por contexto, posição, unicidade e SHA na fonte efetiva e nos arquivos isolados. Reconstituí as cinco substituições literais declaradas: o resultado é byte a byte cada candidata. A simulação combinada independente gera HTML SHA-256 `b233fb4298cb7b4d6829c1e7ae3bd75819d88048db1cc5a0ea3b4168b834870b`.

O [script independente](../evidencias/QA-09/auditoria-candidatas-primeira-lei-entropia-r17-r2-20261030/verificar.mjs), SHA-256 `1d5b8ce746450310538fd81cd8d8ac2f6b208b4fe41ae9c2dd4e5fa45c59655a`, foi executado somente em leitura e passou: parser, hashes, reconstrução, 197 artigos por hash e ordem, 734 elementos MathML por hash e ordem, e 1.433 destinos de elementos `<a>` preservados. Não constitui teste de links em rede ou navegador, nem aprova alterações em outros arquivos.

## Exame científico

**Primeira lei.** A redação proposta explica que Q recebido contribui positivamente para a variação de energia total, W realizado pelo sistema contribui negativamente, e o saldo é `Q−W`. Preserva a convenção `Q>0` entrando e `W>0` saindo. Somente ao desprezar variações cinética e potencial a variação de U coincide, no modelo simplificado, com a da energia total. O contramodelo do parecer anterior, `Q=+50 kJ`, `W=+100 kJ`, `ΔE=−50 kJ`, deixa de contradizer o texto: a contribuição térmica positiva não determina o sinal do saldo. As equações geral e reduzida, unidades e MathML foram preservados.

**Entropia de escoamento.** O somatório `Σ Q̇_j/T_j` se aplica a parcelas j com temperatura da fronteira uniforme do lado do volume de controle, com calor entrando positivo. A candidata passa a identificar essa condição nas legendas de `Q̇_j`, `T_j` e j. Para temperatura variável, explica integrar o **fluxo local de calor por unidade de área** dividido pela temperatura absoluta local sobre a superfície, ou usar parcelas isotérmicas adequadas. Com fluxo em kW/m², T em K e área em m², a integral resulta em kW/K; evita integrar uma taxa total em kW diretamente sobre área. A soma de `100/300+100/600=0,5 kW/K` não equivale a `200/450=4/9 kW/K`; com saída menos entrada de entropia de massa `0,6 kW/K`, a geração resultante é `0,1 kW/K`. Dados são nominais ilustrativos, não projeto físico completo. A proposta não impõe média aritmética nem omite `Ṡger`.

Confrontei novamente a [primeira lei no MIT](https://ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_4.htm) e a [segunda lei para volume de controle na Purdue, eqs. 4.139–4.142](https://engineering.purdue.edu/~wassgren/teaching/ME20000/NotesAndReading/Lec28_Reading_Wassgren.pdf), p. 1 do PDF: esta apresenta o termo de transferência de calor integrado na superfície. A fonte não fornece os valores hipotéticos do teste. Diferenças de temperatura fora da fronteira não são automaticamente geração dentro do volume de controle; o texto proposto usa a temperatura do lado do volume de controle.

| Critério da proposta localizada | Resultado |
|---|---|
| Base, identidade e cinco deltas | Atendidos na fotografia r17. |
| Saldo de energia versus contribuição do calor | Atendido pela nova redação e convenção declarada. |
| Parcelas isotérmicas e integral de fluxo local | Atendidos em texto, condições, sinais e dimensões; equação discreta e MathML preservados. |
| Preservação da estrutura afetada no ensaio | 197 artigos, 734 MathML e destinos de links idênticos na simulação; não é teste em navegador. |
| Versão efetivamente aplicada e QA-09 completo | Não examinados; permanecem pendentes. |

Após aplicação, congelar nova fotografia e mapa, reavaliar o alcance afetado e solicitar Auditor independente sobre a versão real. Não houve revisão humana, piloto, leitor de tela, teste com estudantes ou certificação externa. Os demais blocos, fontes e requisitos de QA-09 não estão aprovados por este parecer.
