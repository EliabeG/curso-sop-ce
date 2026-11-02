# QA-09 — candidata isolada para ficha 80, rendimento Brayton

Data: 30/10/2026. Corretor: agente automatizado `/root/qa_fichas`. Estado: **candidata não aplicada; aguarda revisão independente**. Responde ao [ajuste obrigatório do lote 3](../../../pareceres/QA-09-fichas-equipamentos-lote3-auditoria-independente-20261030.md). Não encerra QA-09, não reaprova FOR-01 nem libera outro ID.

## Identidade e hipótese acrescentada

O documento atual `formulas/termodinamica.html` tem SHA-256 `c27422b409a0a755448982c4074c6d6967fd3e91d7eae20274e218530f5c37b0`; inventário r8 SHA-256 `ae75a258398c385398567457d98ebd49b9838c0c9a4eedc69ea8d2d72981b687`. A ficha é o artigo `formula-brayton-liquido`, número 80, seção `ciclos`, posições UTF-16 r8 188405–190773; o fragmento ocorre uma só vez na fotografia. SHA-256 do fragmento sem a quebra final do arquivo isolado: original `be53d6d4b8ef9305ad4392713fd7ce2c59379393187d06bf0234116ffc431ea5`; candidata `9dcaed2872d4754bb8151aae1ada14a4c45a07557e6ed70ec5569b8c4cfc0897`.

Após a condição atual, propõe-se acrescentar tanto no texto visível quanto na cópia de busca `data-busca`:

> Para η como rendimento motor: Q̇in > 0 e Ẇt > Ẇc.

Na marcação, os sinais `>` são representados por `&gt;` em ambos os pontos. Essas condições estabelecem denominador positivo e trabalho líquido produzido positivo na interpretação indicada. A identidade `Ẇliq = Ẇt − Ẇc` continua válida como diferença algébrica; a restrição é apresentada para interpretar η como rendimento de motor. Mantêm-se o texto anterior, as expressões MathML, símbolos, IDs e ligação à aula.

Com dados hipotéticos do lote 3, `(1000−400)/1200=0,5`, respeitando ambos os limites. `Q̇in=0` produz divisão indefinida; `Q̇in=1200` e `Ẇt=400<Ẇc=1000` produzem razão negativa e não descrevem rendimento de motor produtor de trabalho. São exemplos matemáticos de domínio, não estados de equipamento validados. A base de potência pode ser substituída consistentemente por energia por ciclo ou por massa, como já dizia a ficha.

## Simulação, arquivos e consequências da aplicação

Os arquivos `original.html` e `candidata.html` incluem uma quebra final; seus hashes são respectivamente `e8efc9eba607ac6007c039feab009696f81bbae281015e4159d5697079c76565` e `2cb229664df358a36d1aa0650b295e63c3b4081fc9491e6987db4949f38ce446`. O `manifesto.json` registra a fotografia e o delta; SHA-256 `076bb2b4b885507d65964dc423202d34ae05d7a2a63fce399c395d8ee808d003`.

O script `verificar.py`, SHA-256 `6359777bbe5e5365e4dc891f2dec4ebff21bd431e51f6aef4488a57a4e55ab15`, lê somente os arquivos e testa a substituição **em memória**: confirmou ocorrência única, duas inserções idênticas, texto visível e índice de busca sincronizados, 100 fichas na mesma ordem, outras 99 fichas inalteradas e 191 elementos MathML idênticos na comparação estática do parser `lxml`. O hash previsto da fotografia simulada é `cda652563a79c49a6c3d527ad1400c7f7597d33c9b8523ed8a26047b25c69feb`. Reproduzir com `python3 auditoria/termodinamica/evidencias/QA-09/ficha-080-candidata-20261030/verificar.py`; requer `lxml` e imprime apenas em stdout. O teste não grava o formulário.

Se aprovada e aplicada, a edição mudará o hash integral do formulário e as posições posteriores. A aplicação exige conferir a base atual, mapear o inventário r8 à nova fotografia por documento, contexto, posição e hash, verificar estrutura/funcionalidade relevante, examinar a repercussão de FOR-01 e demais aceites afetados e solicitar auditoria independente da versão efetiva. A candidata não demonstra execução em navegador, teste de leitor de tela, revisão humana, teste com alunos ou evidência de aprendizagem.
