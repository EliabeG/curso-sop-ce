# BAN-02 — Entrega r1

Data: 27/10/2026. Autor: agente automatizado Corretor `/root/corretor_aaa`. Estado: **entregue para auditoria independente; não aprovado pelo próprio Corretor**. Nenhum próximo ID foi iniciado.

## Critério e escopo

> Criar registro por ID com competência, pré-requisitos, origem, formato, nível, raciocínio requerido, número de etapas, hipóteses e exposição prévia. Aceite: os 190 itens atuais estão classificados individualmente e os novos entram no mesmo registro; nível não é inferido só pelo título do assunto.

Foi criado o inventário exclusivo do E1, com 30 Q, 80 CR e 80 AV. HTML do curso, 190 artigos, registro de respostas, scripts e estilo publicados permanecem inalterados. BAN-01 e GOV-01 foram preservados pelos hashes do produto aprovado. O controle de fluxo não foi editado pelo Corretor.

## Artefatos entregues

- [JSON canônico](../inventario/inventario-questoes.json): todos os campos individuais, alcance de competência, hipóteses e relações com evidência.
- [Resumo legível](../inventario/INVENTARIO_QUESTOES.md): método, distribuição, ressalvas e tabela individual dos 190 itens.
- [Contrato 1.1](../inventario/inventario.schema.json) e [guia de cadastro/manutenção](../inventario/LEIA-ME.md): novos IDs sem limite de dois dígitos, itens abertos/projetos e estados futuros de revisão com evidência condicional.
- [Validador reproduzível](../inventario/validar-inventario.mjs): descoberta dinâmica fonte↔registro, duplicados, omissões, órfãos, metadados estruturais e hashes de artigo/recursos.
- [Verificação desta rodada](../evidencias/BAN-02/verificacao-r1.json), [testes técnicos do apoio](../evidencias/BAN-02/testes-validador-r1.json) e [script consolidado de fixtures](../evidencias/BAN-02/testar-validador-r1.mjs).
- [Manifesto SHA-256 completo](../evidencias/BAN-02/manifesto-r1.json), snapshot do HTML anterior e sete figuras, além de cópias congeladas dos cinco artefatos de inventário em `evidencias/BAN-02/pacote-r1/`.

## Conteúdo e decisões

Todos os itens têm competência(s), pré-requisitos, atribuição/identificadores/fontes disponíveis, formato de resposta, nível estimado justificado, etapas intelectuais enumeradas com contagem coerente, hipóteses explícitas/implícitas/limites e exposição conhecida ou desconhecida. Formato não é confundido com demanda cognitiva; figuras contextuais não são promovidas a leitura gráfica necessária. Todos os vínculos com C01–C10 estão delimitados como apoio fundamental, sem atestar competência avançada integral.

A classificação resultou em **168 iniciantes, 22 intermediários e nenhum avançado**. Não é resultado psicométrico nem classificação final do curso. CR09/24/79 incluem leitura crítica condicionada da insuficiência/ambiguidade; essa condição é visível e não converte defeito editorial em qualidade avançada.

Os 80 pares CR/AV foram comparados individualmente. O vínculo declarado de origem é separado de dados repetidos, transformação/procedimento comum, reformulação de conceito ou relação temática. Estão explícitos CR25/AV25 e CR28/AV28 com dados repetidos; Q26/27/29 com exemplos reutilizados; Q19/28 com mesmo procedimento e dados diferentes; CR80/AV80 com geometria e parte dos dados repetidas. O histórico do estudante permanece desconhecido. Seis itens Q não receberam relação específica neste recorte; ausência de relação não significa ineditismo.

CR09, CR24, CR55, CR68 e CR79 têm ambiguidades/defeitos nomeados e encaminhamentos. Em CR68, a densidade e a tabela defeituosas não entram no julgamento da emissividade. CR24 só admite a razão térmica condicionada ao mesmo gás; CR79 não permite demonstrar predominância radiativa a partir do vácuo sozinho. As hipóteses ausentes de outros itens permanecem nos campos próprios. Nenhum desses problemas foi corrigido ou certificado nesta entrega.

O coordenador forneceu leitura e anotações Q01–30, preservadas em `insumo-q-coordenador.json`; o Corretor revisou fonte e comentários, integrou os registros e recalibrou Q10 e a contagem de Q15. O Corretor classificou CR01–80 e AV01–80. O apoio `/root/corretor_aaa/suporte_ban02` implementou contrato/validador e testes técnicos, sem classificar itens nem substituir o Auditor.

## Verificações executadas

O validador foi executado sobre o JSON final: **190 registros e 190 artigos, sete recursos e 1.022 referências locais verificados, zero erros e zero avisos**. Hashes dos sete snapshots de imagem conferem com os originais. Os hashes de produto abaixo conferem com a base aprovada.

Os testes técnicos do apoio exercitaram descoberta de Q100, novos abertos/projetos, omissões/órfãos/duplicados, campos obrigatórios, etapas incoerentes, deriva de fonte/artigo/recurso, referências inválidas e estados condicionais. A evidência distingue versões efetivamente executadas: na evolução 1.1 passaram três cenários positivos, 11 negativos novos e 20 regressões; o reforço final do schema também rejeitou evidência remota no teste isolado. O script consolidado exportado reúne os casos para reprodução, mas **essa cópia consolidada não foi executada como arquivo**: o ambiente não oferece Node CLI configurado. A validação final real foi executada pelo Node REPL, conforme o guia. Não há alegação de execução do arquivo que não ocorreu.

Não houve teste de navegador novo porque o produto não foi editado. Esta rodada não conferiu novamente fontes oficiais, não auditou todos os gabaritos, não produziu piloto, distratores novos, rubrica de problema aberto ou comprovação de independência dos bancos. Esses trabalhos pertencem aos IDs próprios e permanecem pendentes.

## SHA-256 da versão entregue

| Arquivo | SHA-256 |
|---|---|
| `auditoria/termodinamica/inventario/inventario-questoes.json` | `740792085cfede3b91131187ebf40ce614b943e296991e05af5d601498ca287f` |
| `auditoria/termodinamica/inventario/inventario.schema.json` | `c71033464d54e71e61d4dcbae56847a88720e5ff937c1e1f7179005ab22d149b` |
| `auditoria/termodinamica/inventario/validar-inventario.mjs` | `ddc8a6831422a868fb5a8b15b2f6653325f6644acf4f5c64dbf35bb0d2369fdd` |
| `auditoria/termodinamica/inventario/LEIA-ME.md` | `cdcd7e965bdc4a998b6e2fa784a53f84f295abcf9ade2d06ce62fff71d072449` |
| `auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md` | `508d0d2f17d8220d9b69eee8bd60e71c6999bb56ffdd7ff9547dc26174a94c2d` |

### Produto preservado

| Arquivo | SHA-256 |
|---|---|
| `modulos/e1-termodinamica.html` | `b4e2d672c6feecb4289ad73bb9c16000ff5156720698f10153ff93fa0b788a8e` |
| `assets/registro.js` | `444a13658e0b869760296826be30267215293b18c3074f283b2a1ea252e828a2` |
| `assets/curso.js` | `81728c9fd1e96b738410e6b51cf4ab3ed785fb17753e68a988c1dcf236d8f899` |
| `assets/curso.css` | `b8ded6abc4548f378daab2e299a8a55ba81e8841c41049133a84d93848ee3eaa` |

O pacote está congelado para o Auditor. Somente parecer independente seguido de liberação explícita do coordenador permite iniciar outro ID.
