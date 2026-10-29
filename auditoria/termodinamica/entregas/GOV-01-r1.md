# Entrega GOV-01 — rodada 1

**Data:** 27/10/2026, America/Sao_Paulo.  
**Responsável:** agente automatizado Corretor AAA (/root/corretor_aaa).  
**Estado:** entregue para auditoria independente, sem autoaprovação.  
**Único ID liberado:** GOV-01.  
**Fonte do critério:** AUDITORIA_TERMODINAMICA_NIVEL_AVANCADO.md, versão 1.0, seção 4.

## Critério e implementação

> Publicar os resultados de aprendizagem C01–C10 e distinguir preparação para concurso de formação avançada aplicada. Aceite: cada promessa aponta para conteúdos e instrumentos que efetivamente a avaliam; nenhuma promessa de cobertura universal de provas ou de todos os ramos da Termodinâmica.

A seção inicial do E1 agora informa que o nível atual é intermediário e que o percurso avançado está em desenvolvimento. Foram publicados os dez resultados-alvo com uma coluna separada de prática disponível, vínculos aula → exercício e desenvolvimento ainda necessário. Cada capacidade anunciada como atual é delimitada ao que o enunciado efetivamente solicita; nenhuma questão curta é apresentada como prova de autonomia avançada.

O lead da página e a meta description passaram de “Domine...” para uma descrição de estudo e treino com o percurso avançado explicitamente em desenvolvimento. A promessa anterior “Ao terminar esta aula...” foi substituída pela delimitação concreta. A abertura também diferencia treino de concursos de formação aplicada, restringe o escopo E1 e fornece uma sequência de estudo com destinos existentes.

O quadro C07 identifica apenas introduções a umidade, fator Z e PCS/PCI. C10 declara ensino sistemático e instrumento próprio de avaliação ainda indisponíveis; não foi inventado um link ou apresentado um roteiro de raciocínio como rubrica de relatório. Os casos Q26 e Q29 são explicitamente identificados como fixação com dados retomados de exemplos.

## Arquivo de produto alterado

Somente `modulos/e1-termodinamica.html`: duas ocorrências do lead (texto visível e meta description) e a introdução anterior à guia de notação. Todo o restante do HTML mantém identidade de bytes com a versão aprovada em BAN-01-r2. A identidade visual usa as classes já existentes `box`, `box-dica`, `bloco-aula`, `tabela` e `roteiro-estudo`; cabeçalhos e células mantêm `scope` e `data-rotulo`. Não foram alterados CSS, JavaScript, registro, formulário ou outros módulos.

| Arquivo | SHA-256 antes | SHA-256 entregue |
|---|---|---|
| modulos/e1-termodinamica.html | a69846fbe1dd1bb8ef3ce3a685ffc2a308d6595a8f95a8637da523e77e231d1d | b4e2d672c6feecb4289ad73bb9c16000ff5156720698f10153ff93fa0b788a8e |

Arquivos compartilhados conferidos e preservados:

| Arquivo | SHA-256 inalterado |
|---|---|
| assets/registro.js | 444a13658e0b869760296826be30267215293b18c3074f283b2a1ea252e828a2 |
| assets/curso.js | 81728c9fd1e96b738410e6b51cf4ab3ed785fb17753e68a988c1dcf236d8f899 |
| assets/curso.css | b8ded6abc4548f378daab2e299a8a55ba81e8841c41049133a84d93848ee3eaa |

## Evidências e verificação

Em `../evidencias/GOV-01/`:

- `e1-termodinamica.antes.html` e `base.json`: base congelada antes de GOV-01.
- `introducao-antes.html`, `introducao-depois.html` e `mudancas-r1.json`: substituição exata e lista de 14 novos IDs.
- `vinculos-promessas-r1.md` e `.json`: conferência semântica individual das dez linhas e do alcance das atividades.
- `verificar-gov01-r1.mjs` e `verificacao-r1.json`: verificador reproduzível e resultado desta execução.

Resultados: **190/190 artigos de questões idênticos**, incluindo as 30 questões de BAN-01; gabarito aprovado preservado; **43 vínculos novos com destinos já existentes**; 1.204 IDs anteriores preservados, 14 novos e **zero duplicatas**. O verificador também reconstrói o HTML esperado pelas únicas substituições autorizadas e exige igualdade integral com o arquivo entregue. O registro das digitais permanece inalterado, pois nenhuma questão mudou.

Reprodução: `node auditoria/termodinamica/evidencias/GOV-01/verificar-gov01-r1.mjs`. O script termina sem erro quando todas as asserções passam e exporta `resultado`. Esta execução usou o runtime node_repl.

O hash global do HTML muda ao acrescentar a delimitação; o conteúdo protegido por BAN-01 continua integralmente igual e está comparado artigo por artigo, além da comparação das partes externas à introdução. Assim não houve revisão inadvertida de gabarito, enunciado ou justificativa já aprovados.

## Aplicação das regras comuns e limites

GOV-01 é uma entrega de governança e comunicação curricular. Não cria uma nova unidade científica nem declara concluído um resultado avançado; os requisitos de novas aulas, exemplos, exercícios inéditos e rubricas continuam atribuídos aos itens curriculares próprios. As promessas atuais estão apoiadas em explicação e verificação concreta; os objetivos sem ensino/avaliação integral estão identificados como pendentes. Concluir GOV-01 não encerra GOV-02, BAN-02 ou qualquer competência C01–C10.

A verificação realizada é estática e editorial, incluindo leitura da pertinência das atividades. Não houve ensaio de navegador, leitor de tela, aplicação com estudantes ou certificação externa. Nenhuma avaliação integral do banco foi inferida da publicação dos vínculos. A fonte dos objetivos é a auditoria versão 1.0; os conteúdos e instrumentos vinculados pertencem à base preservada, identificada pelo hash acima. Não foram adicionados novos dados físicos.

A entrega aguarda parecer do Auditor; nenhum próximo ID foi iniciado.
