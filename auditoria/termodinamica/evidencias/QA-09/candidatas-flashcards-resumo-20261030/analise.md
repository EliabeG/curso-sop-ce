# QA-09 — candidatas isoladas de flashcards e resumo

Data: 30/10/2026. Preparação pelo Corretor automatizado `/root/qa_oficina`. **Candidatas não aplicadas, aguardando auditoria independente.** Referem-se aos ajustes obrigatórios dos pareceres `QA-09-flashcards-resumo-auditoria-independente-20261030.md` e `QA-09-flashcards-conceituais-auditoria-independente-r1.md`. O HTML e os inventários oficiais não foram editados nesta preparação. QA-09 e o próximo ID seguem bloqueados.

## Fotografia e método

O HTML da aula tem SHA-256 `57b13f0d6386764f1cc46ce543013b0eb75f7bfa97ffbd63ea331f38bfc5af8c`; o inventário r8 tem SHA-256 `ae75a258398c385398567457d98ebd49b9838c0c9a4eedc69ea8d2d72981b687`. Para cada caso, arquivos `*-original.html` e `*-candidata.html` isolam o elemento completo na fotografia. `manifesto.json` contém tipo, posição UTF-16, ID r8, hashes dos elementos e as substituições literais; os arquivos têm quebra de linha final não incluída nos hashes dos elementos. O hash de `texto_direto` do resumo no inventário omite descendentes e por isso não deve ser confundido com o hash de elemento inteiro.

São cinco correções exigidas e dois esclarecimentos adicionais relativos à ressalva do Auditor sobre pressão intermediária. Esses dois últimos não foram classificados no parecer anterior como erro numérico; são propostos para tornar os cartões autossuficientes quanto à finalidade e às hipóteses. Os sete fragmentos são independentes na fotografia r8; uma eventual aplicação conjunta deve confirmar que todos ainda correspondem ao documento vigente.

## Correções obrigatórias

| Nome e posição r8 | Alteração proposta | Razão |
|---|---|---|
| `cop`, 1261323 | Restringe a resposta ao refrigerador ou bomba de calor **acionados por trabalho**, e distingue calor útil retirado da fonte fria ou entregue à quente. | Preserva o COP usual dessa classe sem generalizar para refrigerador de absorção com entrada térmica no gerador. A [fonte DOE citada no parecer](https://www.energy.gov/sites/default/files/2017/06/f35/CHP-Absorption%20Chiller-compliant.pdf) ilustra a outra base. |
| `valvula`, 1265937 | Declara regime permanente, uma entrada e uma saída, ausência de calor e de trabalho não associado ao escoamento e EC/EP desprezíveis. | A acumulação em volume de controle transiente não força `h1≈h2`. A aproximação continua depender dessas condições físicas. |
| `compressor`, 1267176 | Preserva a fração MathML; acrescenta eficiência como trabalho isentrópico dividido pelo trabalho real de entrada positivo, regime permanente, uma entrada/saída, adiabático e EC/EP desprezíveis. Referência com mesma entrada e pressão de saída. | A razão de entalpias corresponde à razão de trabalhos sob o modelo especificado; calor de processo não é silenciosamente desprezado. |
| `trocador`, 1273639 | Acrescenta regime permanente e uma entrada e saída representativas por corrente, com igualdade das vazões em cada par. | Elimina a acumulação de entropia no volume de controle global externamente adiabático, justificando a soma `ṁΔs`; a irreversibilidade ainda pode gerar entropia. |
| `resumo`, 1283434 | Distingue processo de sistema fechado de massa fixa e volume de controle permanente com uma entrada e saída; conserva que adiabático sozinho não garante resultado isentrópico. | O balanço aberto em geral inclui entropia transportada por massa e acumulação; a igualdade de s das correntes depende da restrição indicada. |

## Ressalva sobre os dois cartões de pressão intermediária

As posições `1269562` e `1271918` mostram a mesma raiz quadrada, com resfriamento perfeito e “hipóteses equivalentes”. No laboratório anterior, a igualdade das razões de pressão é deduzida **como condição de mínimo do trabalho total** em duas compressões adiabáticas, mesmo gás ideal, `cp` e `cv` constantes, mesma vazão e mesma eficiência isentrópica constante, resfriamento à temperatura inicial, pressões absolutas extremas fixas e sem quedas de pressão, mudanças de EC/EP ou separação de massa relevante. Variações dessas premissas podem deslocar o ótimo; a expressão não é regra universal para qualquer compressor.

As candidatas `pressao-entrada-saida` e `pressao-1-3` acrescentam a finalidade de minimizar trabalho, estágio adiabático, gás ideal, calor específico e eficiência constantes e iguais, vazão igual, resfriamento perfeito e ausência das perdas relevantes; exigem pressão absoluta de saída maior que a entrada. Não alteram MathML ou valor calculado. Elas são apresentadas como melhorias de escopo, não como prova de erro na igualdade anterior. O Auditor deve verificar se o detalhamento da conservação de massa deve explicitar separação de massa e se todas as hipóteses do modelo foram representadas de modo inequívoco antes da aplicação.

## Reprodução, limites e etapa seguinte

`python3 auditoria/termodinamica/evidencias/QA-09/candidatas-flashcards-resumo-20261030/verificar.py` retornou `ok=true`, 7 candidatas, com reconstrução hipotética SHA-256 `7eb557d313e94d8504e1ca9b23f85c1a1d21b1e118bedcb439240fa6ed5991e7`. Esse hash **não corresponde ao HTML publicado** e só vale caso todas as sete substituições sejam aceitas e aplicadas exatamente sobre a base informada. O script é read-only; confere a integridade e identidade, não demonstra a suficiência física, acessibilidade, comportamento ou aceites. Não foi feito teste em navegador nem inspeção com estudantes.

Solicita-se a revisão independente das cinco correções e das duas melhorias; em especial a revisão deve confrontar modelos e redação e avaliar seu impacto no ensino/aceites anteriores. A eventual aplicação requer reconciliação de posição, atualização do inventário do HTML e fotografia, comprovação de preservação dos 197 artigos e registros, teste estrutural e novo parecer da versão efetiva. Nenhuma aprovação futura deste lote, sozinha, encerra QA-09.

SHA-256: manifesto `1dddd5384ded59e48386ea4eb87279b9f8f416384107f617003cf9ec9cea0345`; script `84b13f2cbc5aa165a697cd80af98e6e2ff3f18718937cbb708189eeaf4b89dee`. Os hashes individuais de fragmentos estão no manifesto.
