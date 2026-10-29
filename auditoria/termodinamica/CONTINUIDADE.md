# Continuidade — Termodinâmica E1

**Fotografia:** 29/10/2026. Este guia registra um ponto de retomada, não substitui o [controle operacional](CONTROLE_AAA.json), o [protocolo Corretor–Auditor](PROTOCOLO_AAA.md) nem os critérios completos da [auditoria do curso](../../AUDITORIA_TERMODINAMICA_NIVEL_AVANCADO.md). Antes de retomar, confira o controle, os pareceres mais recentes e os hashes dos arquivos efetivos: um aceite pertence a uma versão e a um alcance, não é garantia para versões posteriores.

O objetivo é Termodinâmica avançada de engenharia no contexto de graduação e aplicações profissionais, preservando a preparação para concurso. O curso **ainda não está aprovado como avançado**. Os aceites abaixo são restritos aos itens e às versões examinadas; não demonstram aprendizagem de alunos, certificação externa nem cobertura total do núcleo.

## O que foi concluído

- **GOV-01:** promessa e competências de saída delimitadas; o desenvolvimento e a avaliação de todas as competências ainda não estão completos. [Parecer](pareceres/GOV-01-r1.md).
- **FUN-01:** estado, equilíbrio e graus de liberdade, com quatro problemas abertos, dados, soluções e rubricas. [Parecer final](pareceres/FUN-01-r2.md).
- **FUN-02:** diferenciais, caminhos e propriedades, com três problemas abertos, dados e rubricas. Dois são estimados como avançados no contexto dos modelos fornecidos; isso não é validação empírica. [Parecer](pareceres/FUN-02-r1.md).
- **BAN-01/BAN-02:** reorganização e correção das 30 questões iniciais e inventário individual dos itens. [BAN-01](pareceres/BAN-01-r2.md) · [BAN-02](pareceres/BAN-02-r3.md) · [inventário](inventario/INVENTARIO_QUESTOES.md).
- **BAN-07/BAN-08:** revisão de enunciados, alternativas e cálculos dos 197 itens existentes, com evidências por ID. Mudanças posteriores em AV42/45/52 foram revalidadas no alcance afetado. [BAN-07](pareceres/BAN-07-r3.md) · [revalidação localizada](pareceres/BAN-07-revalidacao-av42-av45-av52-r1-independente.md) · [BAN-08](pareceres/BAN-08-r1.md) · [registro numérico](evidencias/BAN-08/consolidado-197-corretor-r2.json).
- **BAN-10:** estudos críticos e questões oficiais ambíguas tratados com separação de interpretação técnica, fonte e gabarito; nove estudos críticos permanecem fora da nota. [Parecer](pareceres/BAN-10-r2.md).
- **FOR-01:** 100 fichas existentes revisadas quanto a expressões, símbolos, hipóteses e vínculos. Isso não encerra a cobertura do núcleo avançado. [Parecer](pareceres/FOR-01-r2.md).
- **FON-01/FON-02/FON-09:** confronto documental das questões oficiais, rastreabilidade de suplementos e tratamento dos dados defeituosos ligados a CR68. Preservam-se documento e gabarito oficiais; a correção de dados é identificada como editorial. [FON-01](pareceres/FON-01-r1.md) · [FON-02](pareceres/FON-02-r2.md) · [FON-09](pareceres/FON-09-r2.md).

Esses são 12 IDs aprovados no controle nesta fotografia. A quantidade de itens aprovados não mede percentual de aprendizagem nem de domínio avançado.

## Ponto de retomada: QA-09

**ID atual: QA-09, em correção; não aprovado.** Seu aceite exige inventariar e recalcular o conteúdo numérico além dos 197 itens, inclusive exemplos, oficinas, 28 diagnósticos, fichas, figuras e explicações. As contagens estruturais são categorias sobrepostas, não uma contagem de cálculos concluídos. [Preflight independente](pareceres/QA-09-preflight-independente-r1.md) · [mapa de apoio](pareceres/QA-09-mapa-independente-r1.md) · [plano](evidencias/QA-09/plano-execucao-r1.md).

Até esta fotografia, os diagnósticos 1, 6, 9, 12, 14, 19, 26, 27 e 28 receberam ajustes e auditoria localizada. Quatro correções da oficina foram aplicadas e auditadas: [parecer da aplicação](pareceres/QA-09-aplicacao-oficina-auditoria-independente-r1.md). O parecer não encerra QA-09 nem garante revisão do restante. As candidatas dos exemplos EX011 e EX013 foram revisadas, mas **ainda não estão aplicadas**: [análise](evidencias/QA-09/exemplos-011-013-analise-candidatas-r1.md) · [revisão independente](pareceres/QA-09-exemplos-011-013-revisao-candidatas-independente-r1.md). Confirme sua identidade e o estado no controle antes de qualquer aplicação.

Próximas ações dentro de QA-09:

1. Reconciliar a fotografia e os pareceres atuais, incluindo os candidatos EX011/EX013, e verificar eventuais mudanças desde este documento.
2. Continuar o inventário e o recálculo individual das ocorrências ainda não cobertas em teoria, exemplos, oficinas, diagnósticos, fichas, figuras, textos e recursos necessários. Registrar resultado, unidades, hipóteses, tolerância, fonte, autor, revisor, versão e limites; justificar separadamente casos sem número aplicável.
3. Corrigir achados no mesmo ID, sincronizar registros e comportamento afetados e solicitar revisão independente. Reexaminar o alcance de aceites anteriores sempre que a mudança os afetar.
4. Consolidar evidências reproduzíveis e solicitar parecer integral de QA-09. Somente um parecer `APROVADO` sobre a versão efetiva e a liberação do coordenador permitem iniciar outro ID.

Os inventários de QA-09 usam posições no documento: editar texto desloca IDs. Use os mapas de correspondência e confira **documento, contexto, posição e hash**; hash isolado pode se repetir e não transfere prova automaticamente. Verifique saídas de scripts antes de executá-los: alguns regravam evidências históricas; prefira cópias ou destino temporário. A comparação e seus limites estão no [parecer do mapa r2→r3](pareceres/QA-09-mapa-r2-r3-auditoria-independente-r1.md) e no [parecer da oficina](pareceres/QA-09-aplicacao-oficina-auditoria-independente-r1.md).

## Como continuar até o nível avançado

Siga a ordem por dependências da seção 16 da auditoria, refinando-a apenas com justificativa e respeitando o bloqueio do ID atual. Depois dos bloqueios científicos e numéricos, ainda é necessário desenvolver e avaliar o núcleo de propriedades reais, balanços e transientes, entropia e exergia, ciclos completos, misturas e reações; criar problemas inéditos e projetos integradores com dados rastreáveis, soluções e rubricas; concluir matriz C01–C10, avaliação autônoma, acessibilidade, regressão e publicação. As dez portas ACE da seção 17 continuam pendentes. A matriz **GOV-02** só pode ser encerrada quando ensino e avaliação efetivos cobrirem as competências, não apenas com um plano.

Distinguir três declarações: material estruturado para nível avançado; aluno com domínio demonstrado; curso com resultados de aprendizagem medidos. As duas últimas dependem de evidências de desempenho e aplicação, que não foram produzidas nesta auditoria. Não use aprovações parciais, volume de conteúdo ou notas obtidas após consulta como prova de domínio.

## Papéis e reprodução

Os perfis reutilizáveis [Corretor](../../.github/agents/corretor-termodinamica.agent.md) e [Auditor](../../.github/agents/auditor-termodinamica.agent.md), junto de [AGENTS.md](../../AGENTS.md), descrevem funções; eles **não são processos automaticamente ativos**. Em uma nova sessão, recrie ou selecione agentes distintos quando a ferramenta permitir e mantenha a independência de autoria e revisão. O Corretor implementa e registra uma entrega; o Auditor examina a versão efetiva, os critérios e as evidências e emite `APROVADO`, `AJUSTES_OBRIGATORIOS` ou `BLOQUEADO_POR_DEPENDENCIA`; o coordenador mantém a fila, confere hashes e só libera o próximo ID após aprovação.

Para conferência estrutural do E1, o comando canônico é:

```sh
node auditoria/termodinamica/inventario/validar-inventario.mjs
```

O validador verifica estrutura e rastreabilidade, não correção científica ou aprendizagem. Testes de persistência em Node/VM com DOM e armazenamento simulados não são testes em navegador real; cada parecer delimita o que foi executado e por quem. Não atribua revisão humana, piloto, psicometria ou certificação externa sem evidência real.

O `PUBLICACAO.json` da raiz documenta uma publicação histórica e não é manifesto da versão atual de trabalho. A preparação de publicação e o manifesto efetivo pertencem a QA-07, ainda pendente. Consulte também os arquivos de fontes sob `downloads/termodinamica/` e os pareceres FON para procedência e limites; acesso público a material de terceiros não equivale a licença de reprodução irrestrita.

Alguns scripts e registros históricos preservam caminhos absolutos do ambiente original. São evidências de uma execução anterior, não instruções portáveis: antes de reproduzi-los, confira o código, adapte caminhos em cópia e mantenha os originais e seus hashes intactos.
