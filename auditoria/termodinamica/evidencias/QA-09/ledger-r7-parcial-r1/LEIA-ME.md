# QA-09 — ledger esparso da fotografia r7, proposta r1

Data: 30/10/2026. Autor: agente automatizado `/root/audit_strategy`. Esta é uma **proposta de estrutura de acompanhamento**, não um parecer de aprovação de QA-09; precisa de revisão independente antes de ser usada para decisões de cobertura. Não altera o inventário histórico nem o controle operacional.

`ledger.json` fixa o SHA-256 do inventário r7, os documentos e cada parecer citado. O padrão de todas as coleções é **pendente de integração neste ledger**. Não é uma afirmação de que revisões históricas deixaram de ocorrer: elas devem ser incorporadas apenas depois do confronto de sua versão, contexto, posição, hash, fontes e parecer. A proposta começa com 12 blocos explicitamente cobertos por pareceres localizados na mesma fotografia: EX-011, EX-013 e EX-021–030. O registro não estende a aprovação automaticamente aos filhos, ancestrais, outros trechos, imagens, referências, recursos, ativos ou versões futuras.

Coleções são separadas e indexadas a partir de zero no r7 fixado por hash: 11.396 ocorrências, 815 referências, 138 registros de recursos e seis ativos específicos. Essas contagens se sobrepõem, não medem cálculos, não são porcentagem de progresso e não provam completude do inventário. Os 197 artigos identificados como escopo de BAN-08 são explicitamente segregados, sem importar o aceite deles para qualquer apresentação externa; valores e contextos fora desses artigos continuam sujeitos a QA-09.

Para cada novo registro, exigir identificação integral (coleção, índice na fotografia e os demais campos de identidade aplicáveis), estado, justificativa e alcance, versão, parecer independente e seu SHA-256. A classificação de uma referência como navegação ou a de um trecho como não aplicável deve resultar de leitura específica e justificativa; não assumir não aplicabilidade por ausência de algarismos. Todo achado não resolvido continua aberto. Cada lote e sua reprodução devem ser verificados por agente distinto do autor. Não copiar os estados por similaridade ou igualdade isolada de hash após edição; documentar o delta, reconciliar correspondências e rever dependências.

A ferramenta reproduz o ledger parcial sem modificar arquivos existentes:

```sh
python3 auditoria/termodinamica/evidencias/QA-09/ledger-r7-parcial-r1/ledger.py --verificar auditoria/termodinamica/evidencias/QA-09/ledger-r7-parcial-r1/ledger.json
```

Sem `--verificar`, o script emite a fotografia proposta na saída padrão. O script verifica os hashes do inventário, documentos, mapa e pareceres e reextrai os fragmentos no HTML; rejeita alterações da base em vez de tentar conciliá-las. Seu teste é estrutural e não substitui o recálculo e a avaliação científica dos pareceres. O gerador r7 e demais históricos não são executados nem regravados. Teste em navegador, revisão humana e resultados empíricos de aprendizagem não foram realizados por este ledger.
