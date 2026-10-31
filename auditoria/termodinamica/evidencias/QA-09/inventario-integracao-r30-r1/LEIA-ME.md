# QA-09 — triagem estrutural exaustiva e integração r30

30/10/2026. Integrador `/root/planning`. **Triagem aguardando Auditor independente; QA-09 permanece em correção.** Este ledger identifica cada registro da fotografia e associa somente evidências cujo objeto tem identidade exata no inventário. Agrupar ou localizar um fragmento não confere mérito científico; não há classificação automática de texto como não numérico ou não aplicável. Nenhuma ocorrência recebe aceite final de QA-09 aqui.

Foto fixada: aula `c719adae3464fb56ed2b0ad7014e0721c0aab2da444fb484ec0b40c5c0c8fbd4`, formulário `949c44fc5b96703929770b2881383d449af890616d34b9ab10b998ca96c75749`, inventário `1ce69fc1ab71850abc3ab8dc3df82b04e78788b9e62a55919c609a708a7979b4`. A lista contém **11.409 ocorrências**, cada uma com índice e ID do inventário fixado, grupo e estado; posição, âncora, hash e estado original permanecem no inventário de origem referenciado, sem copiar a fotografia. Os 162 grupos combinam documento, seção e tipo, para distribuir a revisão; representam fronteiras estruturais, não unidades independentes de cálculo.

## Estados e alcance

- **187 ocorrências com juízo localizado documentado:** 100 fichas, 50 exemplos, 28 diagnósticos, quatro elementos `figure` e cinco equações contextualizadas. Cada associação aponta ao ledger ou resultado e a seu parecer, com hash e ressalvas. A revisão independente dos ledgers é de rastreabilidade e reconciliação: não se apresenta como nova auditoria científica integral dos 187 objetos. As cinco equações derivam do lote `triagem-formulas-r30-20261030`, com parecer `auditoria-triagem-formulas-r30/parecer.md`; o Auditor declarou vínculo com a aplicação r30. Seus objetos se sobrepõem aos exemplos, logo as contagens não representam 187 cálculos distintos.
- **11.222 ocorrências `pendente_de_merito_e_classificacao`:** não têm associação exata a um dos quatro conjuntos incorporados nesta triagem. Isso **não afirma ausência de parecer histórico**; novos lotes podem trazer evidências e revalidação individual. Uma ocorrência interna a objeto revisado continua pendente até ter seu próprio alcance examinado e documentado; a correspondência não se propaga para filhos, pais, conteúdo de base, fontes ou ativos.
- **Nove unidades com juízo sem ocorrência exata:** seis blocos FUN e três artigos gráficos constam separadamente, com posição/hash e a fonte da ponte. Nenhuma ocorrência é promovida por estar contida neles. Os 197 artigos segregados são listados com IDs e hashes conforme o inventário e continuam com tratamento BAN-08 próprio; conteúdo fora dos artigos segue em QA-09. Nenhum estado novo é atribuído ao mérito de todos os artigos.
- **Referências, recursos e ativos:** as 816 referências têm agrupamento apenas sintático (606 fragmentos locais, 138 caminhos locais/outros e 72 URLs HTTP), e todas seguem pendentes de avaliação individual. As 138 relações de recursos e seis ativos específicos também seguem pendentes. Índice e hash do registro original permitem recuperar seus metadados do inventário; URLs, referências e recursos não se tornam fontes verificadas por estarem listados.

| Tipo de ocorrência | Total | Juízo local associado exatamente | Pendente nesta triagem |
|---|---:|---:|---:|
| Texto direto | 9.512 | 0 | 9.512 |
| Atributos significativos | 807 | 0 | 807 |
| MathML | 711 | 0 | 711 |
| Fichas | 100 | 100 | 0 |
| Equações contextualizadas | 99 | 5 | 94 |
| Exemplos e diagnósticos | 78 | 78 | 0 |
| Tabelas | 37 | 0 | 37 |
| Seções | 32 | 0 | 32 |
| Flashcards | 21 | 0 | 21 |
| Figura | 8 | 4 | 4 |
| Casos de oficina | 4 | 0 | 4 |

As categorias são sobrepostas; por exemplo `<figure>` e `<svg>` podem ser registros aninhados, bem como MathML, texto e equação. A tabela mostra vínculo documental por registro e **não é porcentagem de progresso**, nem diz que uma ficha, figura ou exemplo implica aprovação de todos os seus nós. As recomendações e pendências dos pareceres originais continuam vigentes. Os cinco nós de equação e os dois exemplos que os contêm contam em categorias diferentes.

## Reprodução e teste somente leitura

`node auditoria/termodinamica/evidencias/QA-09/inventario-integracao-r30-r1/gerar.mjs --verificar auditoria/termodinamica/evidencias/QA-09/inventario-integracao-r30-r1/ledger.json`

O gerador fixa os hashes das duas páginas, inventário, três ledgers e seus pareceres, resultado e parecer das cinco equações e parser. Reextrai os fragmentos de **todas as 11.409 ocorrências**, usando a mesma lógica de texto direto/atributos e o parser do projeto; confere IDs únicos, associações exatas, contagens e categorias das demais coleções. A reextração não prova que o parser descobriu todo conteúdo dinâmico, nem reavalia hipóteses, fonte, visualização ou aprendizagem. Sem argumento imprime o ledger em stdout; usa arquivos já existentes e não grava fotografias adicionais. Guardas falham em foto divergente.

Nove testes negativos em cópias do ledger rejeitaram mudança de ID, omissão, grupo, promoção sem suporte, apoio, referência, recurso, ativo e artigo. Esses testes comparam o arquivo com a reconstrução; não adulteram todas as entradas em conjunto nem comprovam correção científica ou independência do parser. `negativos.py` SHA `e054239390e7dec4a413b7d0701df9697a2473066f1489483b20c2cdbf32c2d1`; saída SHA `520a89845ee498b5431008061c4a0fcc0f6e8794e76af6f2838ee682edfa4409`.

- `gerar.mjs` SHA `9e75ca1f6883dbd20aca344ff34fea4e71e0c6d9cba56646ac386434ebdfbdea`.
- `ledger.json` SHA `a709ebf211d59821b285e9347e6dee61eb088c87c38547e494adfb189ec5ae6d`.

Fui integrador dos ledgers de fichas e exemplos e da ponte anterior; a presente estrutura requer Auditor distinto, com vínculos declarados, e não substitui os pareceres científicos originais. Não houve alteração de produto ou evidência histórica, navegação real, leitor de tela, estudantes, revisão humana ou certificação externa.
