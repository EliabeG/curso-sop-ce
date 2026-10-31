# QA-09 — auditoria localizada de quatro fontes gerais na r17

Data: 30/10/2026. Auditor automatizado `/root/next_graphics`, distinto do Corretor `/root/reference_triage`. **Identidade, acesso observado e pertinência temática dos quatro vínculos confirmados no alcance abaixo.** O lote de origem r13 tinha 13 vínculos; este parecer cobre somente seus índices 673–676 e não aprova os outros nove nem encerra QA-09. Não altera o produto ou controle.

## Versão e identidade

Aula r17 SHA `6b0df1096d0b6de6995ffc51bf8489cb45ab954a7aabdeb3f48d068c9777c57c`; inventário r17 `b8eae39cc72cf807d7b84aad7e7a38423168b809231bc3b7f08c439d6d25163b`. Confrontei diretamente os elementos completos da r17 com os da cópia r13 `f19000a7ddb1f3552b9633b0efec266fb3f6c5e5065808505a2f65b2005aefbc`, o inventário r13 `0df99b79bcc2350581fcdded72435d30d07858de237a549e6228ca73682f8d9b` e as identidades do lote. A entrega histórica tem SHA `6f81d89b3a712bdbb23ed5c91759ca41ff6d30e97876df0cefd1a2368f0cf706` e suas identidades `58fd0bc7b7db347b85f54998d3f05d32858d298b2c4ffb8b5facdc1e963e5b84`. Mesmos bytes não bastam para transmitir aceite: reabri e examinei o tópico das fontes em 30/10/2026.

| Índice r13 | Início–fim UTF-16 r17 | SHA-256 do elemento `<a>` | Fonte |
|---:|---|---|---|
| 673 | 1300983–1301132 | `11a77bf3961df05fa1b82c6c8daa345e05c5fa2bb2d03376a83540fd16a050a3` | BIPM, unidades SI de base |
| 674 | 1301141–1301305 | `6aa48c2bb44605998f6d65e18ab89cd056dcf52e0f3802dc2a70d677ba0f7b3b` | MIT, entropia e trabalho perdido |
| 675 | 1301314–1301501 | `c0c9ff9cc865fcefdb4f73ac3ca50f95d4d3150f49eb790c314101ad0f3b6293` | MIT, Brayton e identidade de entalpia |
| 676 | 1301510–1301705 | `ace07f2ce9fc7929b80cd61c7c14b29662aacb3138cc8a50aaae987cc4239a24` | MIT, equilíbrio de fase de substância pura |

## Leitura e limites das fontes

* [BIPM, unidades de base](https://www.bipm.org/en/measurement-units/si-base-units) abriu e enumera as sete unidades, com kelvin, símbolo K, para temperatura termodinâmica. O vínculo e descrição são adequados; a lista não prova por si só todas as conversões, precisão ou hipóteses dos exemplos.
* [MIT, §6.6, entropia e energia indisponível](https://web.mit.edu/16.unified/www/SPRING/thermodynamics/notes/node48.html) abriu e apresenta perda de trabalho ligada à produção de entropia, com ambiente a T₀. Como contraste calculado por mim, para Q=1000 kJ transferidos de 600 a 400 K e T₀=300 K, `Sger=Q(1/400−1/600)=5/6 kJ/K` e `T₀Sger=250 kJ`; os trabalhos reversíveis de referência são 500 e 250 kJ. Temperaturas são absolutas; fonte e ambiente são reservatórios idealizados. Não generalizar a diferença a qualquer definição de trabalho sem fronteiras e estados de referência consistentes. Os números são fictícios.
* [MIT, §6.4, Brayton](https://web.mit.edu/16.unified/www/SPRING/thermodynamics/notes/node46.html) abriu e descreve ciclo ideal, `dh=Tds+dp/ρ` e trabalho líquido de turbina menos compressor. A identidade é para o modelo termodinâmico de composição adequada; a expressão de trabalho de componentes pressupõe suas hipóteses de regime, fluxos e energias. A página não valida automaticamente equipamento real, perdas ou eficiência numérica do curso.
* [MIT 3.020, aula 10](https://ocw.mit.edu/courses/3-020-thermodynamics-of-materials-spring-2021/mit3_020s21_l10.pdf), PDF de sete páginas, abriu; na p. 4 do PDF (p. impressa 3), uma derivação em T e p fixos para substância pura relaciona coexistência e igualdade de potenciais químicos. Não generaliza sozinha as restrições de transferência seletiva ou estabilidade de misturas multicomponentes.

As fórmulas das páginas MIT de HTML são imagens com texto alternativo na extração da ferramenta: isso não é inspeção de renderização completa. As consultas indicam acesso nessa ferramenta e data, não garantem disponibilidade futura, licença de reprodução ou verificação integral das fontes.

## Reprodução

`python3 auditoria/termodinamica/evidencias/QA-09/auditoria-fontes-segunda-lei-r17-20261030/verificar.py` retornou `ok: true`; SHA `7a4dcc131a90d56e5be6adad6e2615812321d3191096fbec474f6fac8068ec6d`. Confere quatro posições, links, hashes, unicidade na seção e equivalência dos elementos r13/r17, além da conta ilustrativa com frações exatas. Não acessa rede nem comprova o conteúdo remoto. Não houve navegador do curso, leitor de tela, alunos ou revisão humana; as outras referências e registros da matriz permanecem pendentes de integração específica.
