# QA-09 — auditoria independente do ledger parcial r9 r2

Data: 30/10/2026. Auditor: agente automatizado `/root/next_examples`, distinto do autor do ledger `/root/planning`. **Veredito localizado: APROVADO como registro parcial para a fotografia e os alcances abaixo.** Não é aceite da cobertura completa de QA-09 e não libera outro ID.

## Base e escopo

Examinei [ledger.json](../evidencias/QA-09/ledger-r9-parcial-r2/ledger.json), SHA-256 `972756beb2a76182ef76e97f95ddea8e550d805bddf77390909a4a748a354b0b`; gerador `ledger.py`, SHA-256 `13c4b7ce002df8529e6e9ac9f64fb3ee3fc02d15ea04693da949fe4a04e06bee`; `selecoes.json`, SHA-256 `80a5f967663c801ba6b6d25411693d207f338cad9d4f14308891025857f49367`; `verificar-textos.mjs`, SHA-256 `c6d53ef85a024a70326d6ac3461f40b8e3b28507de0abc60ea2e1f9e3c10acd7`. A fotografia fixada é inventário r9 SHA-256 `023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d`, com HTML da aula `2d6b8fb2f9c99e04d22c19d7b32bbc3eb20577459d9132e506f9c0acef3f2fc2` e formulário `cda652563a79c49a6c3d527ad1400c7f7597d33c9b8523ed8a26047b25c69feb`.

O gerador importa e reproduz a r1, conferindo o hash da fotografia e do parecer da r1, sem alterar os arquivos. Os oito registros preexistentes representam somente os oito deltas do parecer da aplicação r9. A r2 adiciona 34 linhas: oito exemplos/diagnósticos, nove fichas, dez textos diretos, dois vínculos e três ativos com alcance localizado, mais dois achados abertos de fichas 40 e 67. O exame FUN-02 P1 não aprova P2/P3, todas as funções dos ativos nem uma figura adicional fora dos 197 artigos. Os dois achados continuam abertos mesmo existindo candidatas isoladas; não se presume aplicação futura.

## Verificações independentes

- Reli o gerador e o auxiliar de texto para confirmar que somente leem as fontes, não executam geradores históricos e não sobrescrevem evidências. A execução `python3 auditoria/termodinamica/evidencias/QA-09/ledger-r9-parcial-r2/ledger.py --verificar auditoria/termodinamica/evidencias/QA-09/ledger-r9-parcial-r2/ledger.json` retornou `ok`, oito registros r1, 34 adicionais, dois achados abertos e QA-09 em correção.
- Confrontei separadamente os 34 índices, os metadados completos `identidade_r9` e SHA dos pareceres com o inventário e os arquivos efetivos. Confrontei os oito índices da r1 por ID, posição e hash. Os 42 pares coleção/índice são únicos, sem sobreposição entre r1 e r2; sua existência como registros não implica que os nós filhos, fontes ou classes sobrepostas também estejam revisados.
- Examinei os pareceres citados e suas versões: os oito exemplos/diagnósticos, nove fichas e dez textos diretos estão no alcance dos pareceres localizados r9; os dois vínculos e três ativos ficam limitados ao caso FUN-02 P1. As duas fichas 40/67 estão classificadas como achados abertos de pareceres com ajustes obrigatórios, não como aprovadas. A conferência deste ledger não repetiu todas as análises científicas dos pareceres.
- Copiei **apenas as dependências** para uma pasta temporária e apliquei sete modificações uma a uma: estado no JSON salvo, seleção, HTML da aula, formulário, parecer, ativo SVG e auxiliar de textos. Cada uma foi rejeitada; após restaurar as cópias, a verificação voltou a passar. O teste reproduzível [testar_copias.py](../evidencias/QA-09/auditoria-ledger-r9-r2-20261030/testar_copias.py), SHA-256 `8b59ad7962139d00feed3d2976a2fdfa03235fc6a9f6a0f3b8fc02776157d2e4`, não altera os originais.

O verificador detecta as modificações dos arquivos e hashes explicitamente fixados; ele não reavalia o mérito dos pareceres, nem valida automaticamente todos os arquivos citados neles ou conexões externas. O auxiliar usa o mesmo parser da fotografia, portanto essa prova não demonstra apresentação visual. Uma mudança de versão exige nova fotografia, reconciliação e exame de alcance; igualdade de hash de trecho não transfere automaticamente os demais pressupostos.

| Critério localizado | Resultado |
|---|---|
| Fotografia, identidade e unicidade das linhas | Atendido para os 42 registros; r1 e r2 preservadas sem sobreposição. |
| Estados e vínculo aos pareceres da mesma fotografia | Atendido no alcance textual registrado; dois achados mantidos abertos. |
| Reprodução e rejeição de adulterações | Atendido para os sete testes em cópias e dependências fixadas. |
| Classes não registradas | Pendentes de integração neste ledger, o que não apaga revisões históricas nem autoriza transferência automática. |
| Critério integral QA-09 e próximo ID | Não atendidos nesta parcela; continuam bloqueados. |

As 11.397 ocorrências, 815 referências, 138 registros de recursos e seis ativos são coleções sobrepostas e não representam número de cálculos ou percentual de conclusão. Não houve navegador real, leitor de tela, avaliação de aluno, revisão humana ou certificação externa.
