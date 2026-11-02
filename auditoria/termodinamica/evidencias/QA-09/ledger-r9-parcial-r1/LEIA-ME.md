# QA-09 — ledger parcial da fotografia r9

Data: 30/10/2026. Proponente: agente automatizado `/root/planning`. **Proposta aguardando auditoria independente.** Este registro não encerra QA-09 nem libera outro ID. Ele não modifica o inventário r9, as fontes nem o ledger histórico r7.

## O que registra

Na fotografia r9, o padrão de toda ocorrência, referência, registro de recurso e ativo específico é **pendente de integração neste ledger**. Isso não equivale a dizer que nenhuma revisão histórica tenha ocorrido; ela deve ser integrada somente após confronto de versão, identidade, contexto, dependências, alcance e parecer. Oito entradas correspondem exclusivamente aos oito deltas de flashcards, resumo e ficha 80 examinados pelo [parecer da aplicação](../../../pareceres/QA-09-aplicacao-flashcards-ficha80-auditoria-independente-20261030.md). O estado `conferido_no_escopo_localizado` aponta à **alteração** julgada nesse parecer; não afirma cobertura integral de todas as proposições do objeto, seus filhos, referências, recursos ou dependências.

O histórico r7 inclui outros blocos examinados; eles **não foram copiados automaticamente** para esta fotografia. Os mapas r7→r8 e r8→r9 são apoio à identidade, e uma integração futura deve reexaminar cada alcance e suas dependências. Os 197 artigos são segregados sob BAN-08 e não representam aprovação automática do material fora deles. Registros sobrepostos não são quantidade de cálculos nem porcentagem de execução.

Os dados indicam as coleções completas r9: 11.397 ocorrências, 815 referências, 138 registros de recursos e seis ativos específicos. O inventário é o índice de base fixado por SHA-256; o ledger só registra exceções a seu padrão pendente, sem enumerar ou apagar revisões anteriores. O gerador verifica a versão dos dois documentos e do inventário, os hashes da configuração, da lista de alterações e do parecer; extrai em unidades UTF-16 cada fragmento, confronta arquivo candidato, posição e hash, exige unicidade e localiza exatamente o objeto pertinente. Para o trecho do resumo, o hash da ocorrência corresponde ao texto direto, diferente do hash do `<li>` completo. Uma mudança posterior exige nova fotografia, análise de impacto e novo ledger, sem sobrescrever os arquivos atuais.

## Reprodução e limites

Da raiz do repositório, rode:

```sh
python3 auditoria/termodinamica/evidencias/QA-09/ledger-r9-parcial-r1/ledger.py --verificar auditoria/termodinamica/evidencias/QA-09/ledger-r9-parcial-r1/ledger.json
```

Sem `--verificar`, o gerador escreve o ledger em saída padrão; não grava arquivos por conta própria. O resultado salvo foi reproduzido com oito registros localizados. Um teste em cópia temporária que alterou o SHA de parecer em uma linha foi rejeitado. Esses testes verificam identidade, estrutura e integridade documental; não repetem independentemente as deduções científicas do parecer nem provam que toda a fonte e referências tenham sido revisadas. Não houve teste de navegador real, com alunos ou certificação externa neste trabalho.
