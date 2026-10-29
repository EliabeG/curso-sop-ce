# FON-01 r1 — exame técnico independente

Data: 28/10/2026. Revisor: agente automatizado /root/auditor_aaa/tecnica_fon01, delegado pelo Auditor AAA. Escopo exclusivo desta versão do FON-01.

**Resultado: sem impedimento técnico identificado.** Este relatório é insumo do Auditor principal; não aprova o gate global, não libera outro ID e não certifica o curso como avançado.

## Versão efetivamente examinada

- Manifesto: SHA-256 91684a6c5dcb945ff9c8841cb6cc02ca82b50c7eb285a2a2b18863eb413dc628.
- HTML final: SHA-256 81eedea9f3731979125724ebb52d839ca68930164b7d7570a2a646d6f5bed2fe.
- Matriz integral: SHA-256 563e70deab73fc10c6af355db9a267a5342243427529efc6407a640436278d42.
- [Registro estruturado](FON-01-r1-tecnico.json): SHA-256 c882bdc846741343078479d2f62bc8354ba73f85895e592e71f3ba976028db12.

Os 108 arquivos do manifesto, as 10 cópias e os dois pacotes referenciados, de 31 e 30 arquivos, foram lidos em disco e tiveram tamanho/hash conferidos. Não houve divergência. O manifesto permaneceu com o hash congelado ao final do exame. O HTML baseline coincide com o snapshot/preparação do Auditor e com a versão anterior indicada.

## Escopo e preservação

A aplicação das três substituições declaradas reconstrói o HTML final inteiro, sem diferença residual: duas referências de CR80 e a linha CAESB do catálogo de 12 provas. Os 197 artigos mantêm IDs e ordem; 196 são idênticos em bytes. Somente o artigo CR80 difere, pelas referências documentais.

No inventário, a comparação recursiva e a reversão apenas dos campos autorizados restituem integralmente o JSON anterior. Mudam os metadados de conferência dos 80 CR, a referência atual/histórica de CR80, seu hash de artigo e fonte.sha256/snapshot. Os outros 117 registros são idênticos. Níveis, competências, etapas, hipóteses, gabaritos e demais campos permanecem iguais.

O resumo do inventário preserva as 332 linhas do corpo histórico, altera o título para incluir FON-01 r1 e acrescenta o apêndice da rodada. Seus quantitativos e descrição do delta correspondem aos dados canônicos. O catálogo de downloads e seus 24 PDFs históricos permanecem preservados; a nova matriz CAESB tem cópia identificada no pacote FON-01.

Formulário, JavaScript e CSS próprios, curso.js, curso.css e registro.js foram comparados em bytes com o pacote FOR-01 r2 e são idênticos. O validador canônico conserva SHA-256 0bd26bcf6288b3bd159ac7c167bfeb4a1a49bbebe784d26a3a93739fcb7790d5. Os 734 elementos MathML da aula permanecem idênticos; o formulário preservado contém 191.

A função digitalDoBanco foi lida: usa enunciado, imagens e alt, valores/rótulos das respostas e chave. Os componentes e atributos de 160 artigos dos bancos CR/AV foram comparados antes/depois e são idênticos. As referências modificadas ficam fora desses componentes. Isso demonstra preservação estática da identidade usada nas respostas salvas; não se apresenta como novo teste dinâmico de localStorage.

## Matriz, recursos e representações

A matriz contém exatamente 80 IDs únicos do inventário, cobrindo 12 famílias. Foram verificados campos obrigatórios, tipos/identificadores, hashes dos artigos baseline e entregues, correspondência das URLs oficiais com as origens no inventário, fragmentos de página, recursos gráficos e seus hashes. A matriz não tem JSON Schema próprio; o contrato estrutural aqui é explícito, além do schema canônico do inventário.

O contador independente pypdf abriu os 25 PDFs distintos, incluindo CAESB atual e histórica. Todas as páginas físicas declaradas de prova/chave estão dentro do documento correspondente. A conferência semântica da posição e do conteúdo pertence ao Auditor principal.

Os 80 blocos de CONFERENCIA_80-r1.md correspondem ao JSON em número original, cargo, aplicação, URLs/páginas, chave, quatro notas de comparação e autoria. As 12 linhas de famílias também coincidem em cargo, código, data e quantidade. Não se identificou contradição entre essas representações.

## Execução reproduzida

O script do autor foi lido integralmente antes da execução. Como grava sua própria evidência, um [adaptador de reprodução](FON-01-r1-tecnico-reproduzir.mjs) manteve o corpo de verificações, forneceu os caminhos/imports equivalentes e redirecionou exclusivamente a única escrita para o diretório do Auditor. O script congelado e a evidência original permaneceram intactos.

Resultado: **777 verificações sem falha**, com [saída reproduzida](FON-01-r1-tecnico-autor-reproduzido.json) byte a byte igual à congelada, SHA-256 aa539ae40355509fd32294714035e397009e4b0788cc02dce3d14abfd32ec7b0. O validador canônico foi também chamado diretamente: **197 itens/artigos, 29 recursos, 1.234 links locais, zero erros e avisos**.

O registro independente contém 1.592 verificações técnicas sem falha. Contagens medem cobertura de comparações; não substituem mérito científico ou leitura documental.

Para reproduzir, a partir da raiz do projeto, execute o Node fornecido pelo ambiente com auditoria/termodinamica/pareceres/FON-01-r1-tecnico-reproduzir.mjs. Para repetir a contagem de páginas, execute Python com pypdf e [FON-01-r1-tecnico-paginas.py](FON-01-r1-tecnico-paginas.py). Ambas as saídas ficam exclusivamente em pareceres.

## Limites

Não foram refeitas a leitura visual dos 80 itens, a auditoria científica, a pesquisa remota de atos ou a suíte dinâmica de persistência. As evidências de origem e o parecer semântico são atribuições separadas do Auditor principal. URLs foram conferidas estruturalmente e contra a matriz/inventário, sem alegar nova consulta HTTP. Não se concluem FON-02, FON-10, BAN-07/BAN-08 ou qualquer outro ID.

Nenhum produto, inventário, controle, matriz ou arquivo do Corretor foi escrito por este subagente. Foram criados apenas este relatório e suas evidências em pareceres.
