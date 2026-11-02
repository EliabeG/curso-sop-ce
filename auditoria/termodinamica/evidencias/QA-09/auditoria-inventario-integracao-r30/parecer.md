# QA-09 — auditoria da integração estrutural r30

30/10/2026. Auditor: next_graphics, com apoio de contagem. Integração de planning: `LEIA-ME.md` SHA `54d71653b8370ae44286eee9385bbeedb6673f3e0bb097a5cb3ca12dcd26ade8`; `ledger.json` SHA `a709ebf211d59821b285e9347e6dee61eb088c87c38547e494adfb189ec5ae6d`; `gerar.mjs` SHA `9e75ca1f6883dbd20aca344ff34fea4e71e0c6d9cba56646ac386434ebdfbdea`.

**Parecer favorável à triagem estrutural no escopo do inventário fixado.** Os 11.409 registros têm IDs únicos e correspondem, na mesma ordem, às ocorrências do inventário r30; seus 162 grupos e estados reconciliam. A associação exata de 187 objetos às respectivas evidências é identificável; as outras 11.222 ocorrências permanecem pendentes nesta triagem. Trata-se de exaustividade em relação ao inventário fornecido, não de prova de que ele descobriu todo o conteúdo dinâmico, da suficiência do parser ou do mérito científico dos objetos.

## Associação e limites de independência

Os 187 registros compreendem 100 fichas, 50 exemplos, 28 diagnósticos, quatro elementos `figure` e cinco equações. O apoio documental independente conferiu IDs, intervalos, hashes e fontes dos quatro conjuntos, com respectivos pareceres. As cinco equações estão em dois exemplos já contados: contagens em níveis sobrepostos não representam cálculos independentes. Os nove blocos ou artigos sem ocorrência exata são mantidos separadamente, sem promover nós contidos por herança. Em cada associação o texto limita o alcance ao objeto e juízo referenciado; não se transfere aceite para filhos, pais, bases, fontes ou ativos.

Atuei anteriormente como Auditor do ledger das fichas e como autor ou revisor de lotes de diagnósticos, figuras e pontes anteriores. Aqui não aprovo novamente minha própria ciência; examino identificação e integração do material já registrado. O próprio parecer de fichas foi limitado à reconciliação, e os pareceres de ponte e equações têm seus respectivos limites. Não se infere uma nova reauditoria científica integral por este agrupamento.

As 816 referências, 138 recursos e seis ativos estão pendentes de avaliação individual *nesta triagem*; isso não afirma que nenhum tenha parecer histórico. As referências se dividem sintaticamente em 606 fragmentos locais, 138 caminhos/outros e 72 URLs HTTP, sem classificação semântica ou aceite por tipo. Os 197 artigos mantêm IDs e hashes do inventário, segregados para tratamento BAN-08, sem novo aceite para todos. O estado global é `QA09_EM_CORRECAO_NAO_APROVADO`.

## Reprodução

Executei o gerador do integrador com `--verificar`; confirmou 11.409 ocorrências, 162 grupos, 187 associações, 11.222 pendências e contagens das outras coleções. O gerador reextrai todas as ocorrências com o parser do projeto; não é parser independente nem exame de navegador. Meu `verificar.py` SHA `4dd3e08e6d1312b29e8970df9ee048dff7452745209a7c042c2b8d32d1f04027`, executável da raiz com `python3 auditoria/termodinamica/evidencias/QA-09/auditoria-inventario-integracao-r30/verificar.py`, confronta cada índice/ID, chaves de grupos, somas, estados, categorias apoiadas e coleções. Resultado SHA `068f5841869104f7da84ebde390f36c824c6f6528890445eec80320ad9482c2a`. Não reextrai autonomamente cada fragmento HTML nem refaz o mérito científico.

Reexecutei os nove negativos do integrador: alteração de ID, omissão, grupo, promoção, apoio, referência, recurso, ativo e artigo foram rejeitadas em cópias. Testam divergência da reconstrução, não adulteração coordenada de todas as bases nem sua correção científica. Não houve alteração do produto, acesso em navegador, avaliação por estudantes, revisão humana ou certificação externa; QA-09 permanece aberto.
