# QA-09 — ensaio em cópia da ficha 80, 30/10/2026

Autor: agente automatizado `/root/qa_fichas`. Estado: **ensaio preparado, não aplicado ao produto; aguarda auditoria independente e decisão do coordenador**. A [candidata isolada](../ficha-080-candidata-20261030/ENTREGA.md) foi aprovada para aplicação pelo [parecer independente](../../../pareceres/QA-09-ficha-080-revisao-candidata-independente-20261030.md), que não examina a versão aplicada. Este ensaio não encerra QA-09, não reaprova FOR-01 integral nem libera outro ID.

## Preparação e reproduções

O script `preparar.py` lê a aula, formulário, inventário e candidata aprovados, exige suas fotografias por SHA-256, aplica a substituição uma vez **em memória** e grava somente em um diretório novo informado como argumento. Não edita o formulário efetivo, não regrava histórico e falha se o destino já existir. Para repetir sem sobrescrever este ensaio, execute da raiz:

```sh
python3 auditoria/termodinamica/evidencias/QA-09/ficha-080-aplicacao-ensaio-20261030/preparar.py /tmp/qa09-ficha80-reproducao-NOVO
```

Requer Python 3 e `lxml`; use um destino ainda inexistente. O script só aceita, dentro do repositório, o subdiretório `ensaio` deste pacote. O ensaio fornecido contém `formulario.antes.html`, `formulario.proposto.html` e `resultado.json`. A execução reproduzida em `/tmp` deu a mesma fotografia proposta; seu resultado de metadados foi copiado para o ensaio. As fotografias são cópias, não a versão vigente.

## FOR-01 e preservação do alcance

A versão base do formulário coincide byte a byte com a cópia aprovada em `evidencias/FOR-01/pacote-r2/formulas/termodinamica.html`, SHA-256 `c27422b409a0a755448982c4074c6d6967fd3e91d7eae20274e218530f5c37b0`. O formulário proposto é reconstruído pela substituição literal da ficha 80, SHA-256 `cda652563a79c49a6c3d527ad1400c7f7597d33c9b8523ed8a26047b25c69feb`. A simulação verificou:

- **100 fichas**, na mesma ordem, e somente a ficha 80 alterada; as demais 99, inclusive as quatro corrigidas por FOR-01 R1-A (23, 46, 79 e 84), permanecem byte a byte iguais à fotografia aprovada.
- **191 elementos MathML** byte a byte idênticos; 11 grupos e sequências de IDs, referências `href`/`src` e atributos ARIA selecionados preservadas; a condição e `data-busca` da ficha 80 contêm a mesma frase adicional.
- **103 vínculos** das fichas para a aula, com 50 destinos distintos: todos os fragmentos existem na aula r8, SHA-256 `57b13f0d6386764f1cc46ce543013b0eb75f7bfa97ffbd63ea331f38bfc5af8c`. A verificação é de existência, não valida a adequação semântica de cada vínculo.

Verificação adicional manual dos arquivos atuais contra o pacote FOR-01 r2: `assets/formulario-e1.js`, `assets/formulario-e1.css` e `assets/curso.css` são idênticos; `assets/curso.js`, `assets/registro.js` e o HTML da aula têm hashes diferentes da fotografia histórica. Isso não demonstra um defeito nem transfere aprovação: seus efeitos e as revalidações intermediárias devem ser examinados pelo Auditor na extensão pertinente antes de qualquer conclusão sobre FOR-01 na versão final. Não foram reexecutadas as verificações históricas integrais de FOR-01: o script histórico inclui fotografia e deltas específicos da rodada r2 e não é um verificador universal de versões posteriores.

## Limites e próximos passos

Inventário r8 conferido: `ae75a258398c385398567457d98ebd49b9838c0c9a4eedc69ea8d2d72981b687`. Uma aplicação futura deve reconciliar o arquivo efetivo e o inventário mais recente (não presumir que r8 continuará atual), gerar nova fotografia e correspondência de IDs/posições, verificar os vínculos e dependências afetados, e submeter a versão efetiva a parecer independente. A simulação é análise estática; não é teste em navegador, leitor de tela, impressão, ensaio com alunos ou certificação externa.

SHA-256: `preparar.py` `468813907fcd3b2f34da34cf2b93e8368038ab64d385385dadf33d3d32ccdbc0`; `ensaio/resultado.json` `8f4789bc109bf3a99cda625c386c7c1a39384fdb7e9631badd1e22465d734e7c`; fotografia anterior `c27422b409a0a755448982c4074c6d6967fd3e91d7eae20274e218530f5c37b0`; proposta `cda652563a79c49a6c3d527ad1400c7f7597d33c9b8523ed8a26047b25c69feb`.
