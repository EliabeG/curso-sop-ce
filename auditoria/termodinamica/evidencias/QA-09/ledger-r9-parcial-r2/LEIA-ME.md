# QA-09 — integração parcial r2 do ledger r9

Data: 30/10/2026. Autor automatizado: `/root/planning`. **Aguardando auditoria independente.** QA-09 permanece em correção. Este arquivo é uma extensão nova da mesma fotografia r9 e preserva a r1, seu parecer e o histórico r7. Não substitui a auditoria integral.

O ledger mantém os oito registros restritos da [r1](../ledger-r9-parcial-r1/ledger.json), cujo parecer independente é identificado no próprio arquivo, e acrescenta 34 registros com pareceres específicos da fotografia r9: oito exemplos/diagnósticos, nove fichas de gases/fases, dez campos diretos da teoria, dois vínculos de FUN-02 P1 e três ativos examinados somente no âmbito desse caso, mais **dois achados abertos** (fichas 40 e 67). Das 34 novas linhas, 32 correspondem somente aos recortes examinados; duas assinalam pendências. Os lotes das fichas 40 e 67 foram julgados `AJUSTES OBRIGATÓRIOS`; não se classificam aqui as demais fichas desses lotes como aprovadas.

Não se importaram automaticamente os achados ou aceites de fotografias anteriores: registros que não aparecem continuam pendentes **de integração nesta r2**, o que não elimina revisões já realizadas. O estado de uma linha refere-se ao alcance declarado no parecer, e não transfere cobertura a filhos, pais, fórmulas adjacentes, fontes, recursos, outros trechos ou versões. O exame de FUN-02 P1 não transforma a figura do artigo segregado em figura adicional fora dos 197 artigos nem aprova todos os dados e funções dos ativos. A classificação dos dois vínculos é limitada à identidade/uso verificado; não confirma genericamente todas as referências.

As coleções r9 permanecem separadas: 11.397 ocorrências estruturais, 815 referências, 138 registros de recursos e seis ativos específicos. São conjuntos sobrepostos, não contagens de cálculos nem porcentagem de conclusão. Os 197 artigos seguem tratados por BAN-08, sem transferência automática para QA-09. A seleção está em [selecoes.json](selecoes.json), com identidade completa e SHA dos pareceres; o arquivo está fixado por SHA no gerador. Antes de uso, as fontes, contextos e dependências ainda requerem o julgamento independente.

## Reprodução

```sh
python3 auditoria/termodinamica/evidencias/QA-09/ledger-r9-parcial-r2/ledger.py --verificar auditoria/termodinamica/evidencias/QA-09/ledger-r9-parcial-r2/ledger.json
```

O programa lê e verifica a r1 e seu parecer, fontes e inventário; reconstrói os 34 índices/identidades contra r9, verifica os pareceres, reextrai os fragmentos de exemplos e fichas e confronta vínculos e hashes de ativos. Para dez campos de texto direto, o auxiliar Node recompõe o texto direto a partir do parser usado pelo inventário e confere o respectivo hash. Ele lê dados e escreve somente em stdout; não atualiza arquivos. `--verificar` confronta a saída reconstruída com o JSON salvo. A reprodução passou; alteração simulada do hash de um parecer no JSON em diretório temporário foi rejeitada. Isso é verificação de identidade e estrutura, não refaz a ciência dos pareceres e não comprova renderização em navegador ou aprendizagem.

Uma mudança em qualquer documento, inventário, arquivo de seleção, parecer ou ativo fixado faz a verificação falhar e exige nova fotografia e avaliação de impacto. Não houve teste com alunos, revisão humana ou certificação externa nesta integração.
