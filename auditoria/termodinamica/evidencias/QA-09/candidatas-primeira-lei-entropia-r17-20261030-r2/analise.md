# QA-09 — candidatas r2: primeira lei e entropia de escoamento

30/10/2026. Corretor `/root/next_graphics`. **Não aplicadas; aguardam reexame independente de `/root/reference_triage`.** A r1 permanece preservada em `candidatas-primeira-lei-entropia-r17-20261030/`; não se reescreveu o produto nem o histórico. O Auditor apontou que a expressão da r1 “taxa local de calor ... em toda a área” era dimensionalmente ambígua: uma integral espacial requer fluxo de calor por unidade de área ou elemento diferencial de taxa.

## Correção r2

Mantém-se a candidata da primeira lei da r1, que distingue contribuição positiva do calor recebido e saldo energético Q−W, e limita a igualdade entre variação de energia interna e total ao caso de variações cinética e potencial desprezíveis. A r2 também preserva as legendas que definem Q̇ⱼ como calor de uma parcela j, Tⱼ como temperatura uniforme do lado do volume de controle e j como índice de parcela.

A nota de entropia agora diz: “Se a temperatura variar na fronteira, integre o fluxo local de calor por unidade de área dividido pela temperatura absoluta local sobre a área de troca, ou divida a fronteira em parcelas isotérmicas adequadas.” Mantém sinal positivo para calor que entra. Dimensionalmente, `(kW/m²)/K` integrado em `m²` dá `kW/K`; para parcelas uniformes isso se reduz à soma das taxas divididas por suas temperaturas. A fórmula discreta é preservada; a integral é descrita no texto, não representada por MathML novo. O uso de uma temperatura média aritmética para dois aportes distintos não é suposto.

## Contrastes e fonte

No exemplo hipotético do parecer de origem, Q=+50 kJ e W=+100 kJ dão ΔE=−50 kJ; calor recebido não determina sozinho o sinal do saldo. Duas parcelas de 100 kW a 300 K e 600 K transferem 0,5 kW/K de entropia; 200/450 produz 4/9 kW/K. Para diferença entre entropia de massas de 0,6 kW/K, as produções obtidas são 0,1 e 7/45 kW/K, respectivamente. As temperaturas estão em kelvin e os dados são hipotéticos, sem identificar um equipamento específico.

[Purdue, balanço de entropia em volume de controle](https://engineering.purdue.edu/~wassgren/teaching/ME20000/NotesAndReading/Lec28_Reading_Wassgren.pdf), p. 1 do PDF, eqs. 4.139–4.142, apresenta o termo integrado na superfície; [MIT, primeira lei](https://ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_4.htm) apoia a convenção e o balanço da energia. Fontes consultadas em 30/10/2026; não são fonte dos números artificiais.

## Identidade, teste e limites

Aula r17 SHA `6b0df1096d0b6de6995ffc51bf8489cb45ab954a7aabdeb3f48d068c9777c57c`; inventário r17 `b8eae39cc72cf807d7b84aad7e7a38423168b809231bc3b7f08c439d6d25163b`. Manifesto da r2 `bc1d49ea7be22c50750a6a32440e69545f6ed3c0a438e079909a570dc6cded11`; preparador `07e66b0f009e00738a5a07f1170797f2fc67162c5609db49ee7f3f95ac3211d5`; verificador `1e69e528b679257b811b569d41869414bf75420e2d24f1314523fd11eccf2937`. Na raiz, executar `python3 auditoria/termodinamica/evidencias/QA-09/candidatas-primeira-lei-entropia-r17-20261030-r2/verificar.py`: passou, reconstruindo aula hipotética `b233fb4298cb7b4d6829c1e7ae3bd75819d88048db1cc5a0ea3b4168b834870b` e preservando 197 artigos, 734 MathML, IDs e destinos dos links. O teste não grava produto e não substitui o exame científico ou futura auditoria da aplicação.

O preparador grava arquivos apenas no próprio diretório da candidata e usa criação exclusiva; não reexecutá-lo sobre artefatos existentes. Não houve navegador real, leitor de tela, estudantes ou revisão humana. QA-09 e o uso da versão efetiva continuam dependentes de auditoria independente e reconciliação após aplicação.
