# QA-09 — candidata para diagnóstico 2, instrumentos

Data: 30/10/2026. Corretor: agente automatizado `/root/next_examples`. **Proposta isolada, não aplicada; aguarda Auditor independente.** Base `modulos/e1-termodinamica.html` SHA-256 `2d6b8fb2f9c99e04d22c19d7b32bbc3eb20577459d9132e506f9c0acef3f2fc2`; inventário r9 SHA-256 `023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d`.

## Insuficiência e correção

O [parecer independente dos diagnósticos 1–10](../../../pareceres/QA-09-diagnosticos01-10-r9-auditoria-independente-20261030.md), SHA-256 `ec141bf0549af65e6fccbabca00810ff91493d8d80935a84753ef1edf97b0e0a`, registrou que tubo metálico curvo com ponteiro não determina, por si, qual é o mensurando. Um manômetro pode receber diretamente a pressão do fluido de processo em um tubo de Bourdon; um termômetro a gás pode possuir um bulbo sensível à temperatura conectado por capilar a um mecanismo de Bourdon. Em ambos há tubo curvo e ponteiro, mas o mensurando do conjunto é diferente. O contramodelo é físico, não descreve o instrumento pretendido pelo diagnóstico.

A candidata substitui somente a segunda pergunta por: “Um tubo metálico curvo está conectado diretamente ao fluido do processo e se deforma devido à pressão desse fluido, acionando um ponteiro. Que instrumento é esse e que grandeza ele mede?” O objeto passa a identificar a pressão do próprio processo, sem confundir com a pressão interna de um sistema termométrico preenchido e isolado. A pergunta sobre instrumento e grandeza é preservada, assim como a resposta de manômetro de Bourdon e pressão. Não acrescenta marcas, alternativas ou gabarito à pergunta.

Os documentos da fabricante consultados em 30/10/2026 são [WIKA, manômetro de tubo de Bourdon, IN 00.01, p. 1](https://www.wika.com/media/Technical-information/English/ds_in0001_en_co.pdf) e [WIKA, termômetro acionado por gás TGT73, seção 2](https://www.wika.com/media/Operating-instructions/Operating-instructions/Temperature/Dial-thermometers/oi_tgt73_ex_en_de_fr_es.pdf). Mostram exemplos de mecanismos, não origem dos números didáticos do diagnóstico. Não se afirma que cada instrumento curvo seja de um único tipo.

## Conta e identidade

A primeira parte da questão é mantida byte a byte: limite inferior −20 °C e span 150 °C levam a limite superior de 130 °C. Span é diferença de temperatura, por isso 150 °C de intervalo correspondem a 150 K de intervalo; sem informação de incerteza instrumental. O [NIST, guia SI capítulo 8](https://www.nist.gov/pml/special-publication-811/nist-guide-si-chapter-8) sustenta equivalência numérica de intervalos Celsius e kelvin.

O manifesto JSON registra trecho original, candidata, posições UTF-16 520730–521217 e hashes dos fragmentos/arquivos; os arquivos isolados contêm quebra final que não faz parte dos fragmentos. O original ocorre exatamente uma vez na fotografia e seu hash coincide com inventário r9. `verificar.mjs` simula a substituição em memória e confere o delta literal único, parser, preservação byte a byte dos 197 artigos e cálculo de span; não grava o HTML nem os inventários.

## Alcance e encaminhamento

A simulação não verifica renderização em navegador, teste com alunos ou exatidão de todos os recursos. A candidata deve ser examinada por Auditor independente e, antes de uso no produto, deve-se confrontar novamente hash, contexto e ocorrência única. Após aplicação, atualizar inventário e mapa sem regravar históricos, confirmar os 197 artigos, links e dependências afetadas e submeter a versão efetiva a novo parecer independente. Nenhum outro ID é liberado; QA-09 integral permanece em correção.
