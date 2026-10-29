# Protocolo Corretor–Auditor — Termodinâmica

Data de criação: 27/10/2026. Escopo exclusivo: E1 Termodinâmica.

## Mandato

Executar as correções de `AUDITORIA_TERMODINAMICA_NIVEL_AVANCADO.md` uma de cada vez. O Corretor implementa; o Auditor verifica independentemente e exige ajustes até que todos os critérios aplicáveis à correção estejam satisfeitos. O coordenador só libera o próximo ID depois de um parecer explícito `APROVADO` para a versão efetivamente examinada.

“AAA” é a exigência interna de qualidade integral definida pelos critérios da auditoria e por este protocolo. Aprovar um item não classifica automaticamente o curso inteiro como avançado: essa decisão depende das dez portas ACE e de todas as evidências exigidas.

## Papéis e permissões

- **Corretor:** pode editar os arquivos necessários ao ID liberado, produzir evidências e corrigir rejeições do mesmo ID. Não pode aprovar a própria entrega, marcar outros itens concluídos nem iniciar o ID seguinte por conta própria.
- **Auditor:** lê a entrega, o critério original, as dependências e os arquivos resultantes; reproduz verificações pertinentes. Não implementa a correção que está auditando. Pode escrever pareceres e exigir ajustes objetivos. Não usa a narrativa do Corretor como única evidência.
- **Coordenador:** controla a fila e o arquivo `CONTROLE_AAA.json`, encaminha pareceres e libera cada próximo ID. Não converte rejeição em aprovação sem uma nova revisão.

## Regra de bloqueio

1. Apenas um ID pode estar em implementação/revisão de cada vez.
2. Antes de editar, o Corretor lê o item integral, sua definição comum de aceite e as dependências relevantes.
3. A entrega identifica arquivos, mudanças, verificações realizadas, resultados e limitações; atribui uma versão e registra SHA-256 dos arquivos alterados.
4. O Auditor examina a versão entregue e emite `APROVADO`, `AJUSTES_OBRIGATORIOS` ou `BLOQUEADO_POR_DEPENDENCIA`.
5. Em caso de ajustes, o Corretor trabalha somente nesse ID e responde ponto a ponto; segue nova auditoria.
6. Um bloqueio real de dados/ferramenta/evidência deve ser documentado; não autoriza ignorar o critério, inventar verificação nem declarar o curso avançado.
7. Somente `APROVADO`, com evidências e sem pendência obrigatória, libera o próximo ID.
8. Se houver alteração posterior nos arquivos que invalide um parecer, reabrir o item afetado. Melhorias novas não preservam automaticamente uma aprovação de versão anterior.

## Padrão de aprovação

- Todos os critérios de aceite do item e das regras comuns pertinentes foram atendidos.
- A correção é científica e pedagogicamente coerente com o escopo e o nível exigido.
- Enunciados, soluções, hipóteses, unidades, fontes, figuras e comportamento concordam, na extensão afetada.
- Evidências são reproduzíveis. Inspeção de código, cálculo, testes de navegador e aplicação com estudantes são identificados separadamente.
- Não há pendência relevante escondida em ressalva, amostragem insuficiente ou promessa de trabalho futuro.
- Não foram modificados conteúdos de outros módulos. Mudanças compartilhadas estritamente necessárias ao E1 requerem verificação do alcance.

Requisitos gerais destinados a conteúdo curricular novo não devem ser aplicados artificialmente a uma correção mecânica de alternativas; aplicar os critérios que realmente pertencem à entrega, sem reduzir o aceite específico.

## Estrutura dos pareceres

Cada parecer deve ser salvo em `auditoria/termodinamica/pareceres/<ID>-r<rodada>.md` e conter:

1. ID, rodada, data e veredito.
2. Critério original e escopo exato examinado.
3. Versão, arquivos e hashes examinados.
4. Verificações independentes e seus resultados.
5. Quadro de todos os critérios: atendido/não atendido/não aplicável com justificativa.
6. Ajustes obrigatórios concretos, se houver, e evidência necessária à reapresentação.
7. Decisão explícita sobre a liberação do próximo ID.

O parecer deve identificar o revisor como agente automatizado. Não atribuir assinatura, qualificação humana, teste com alunos ou certificação externa inexistentes.

## Ordem inicial

1. `BAN-01`: eliminar o gabarito ABCDE repetido das 30 questões iniciais, mantendo correção e coerência dos comentários.
2. `GOV-01`: tornar explícita a promessa e as competências de saída, sem anunciar como entregue conteúdo ainda pendente.
3. `BAN-02`: inventariar individualmente os itens existentes para orientar as demais correções.
4. Seguir a ordem por dependências da seção 16 da auditoria, preservando prioridade aos bloqueios P0 encontrados.
5. Fechar `GOV-02` somente quando as competências obrigatórias tiverem ensino e avaliação efetivos. Um mapa de lacunas pode orientar o planejamento, mas não atende, sozinho, ao seu critério de aceite.

Reordenação registrada em 27/10/2026 após preflight independente do Auditor: o aceite de GOV-02 depende da implantação do núcleo. Antecipar sua aprovação apenas com intenções violaria o protocolo. GOV-01 pode delimitar o alvo futuro e as promessas atualmente sustentadas, sem classificar antecipadamente o curso inteiro como avançado.

A ordem pode ser refinada pelo coordenador com justificativa registrada. Refinar a ordem nunca libera a passagem enquanto a correção atual estiver rejeitada.

## Estado e continuidade

`CONTROLE_AAA.json` registra o ID atual, estados por item, IDs dos agentes, entregas e pareceres. Em retomadas, os agentes devem ler esse arquivo e o último parecer antes de trabalhar. O registro é a memória operacional deste projeto; um arquivo salvo não significa que exista execução automática em segundo plano.

Estados permitidos: `pendente`, `liberado`, `em_correcao`, `aguardando_auditoria`, `ajustes_obrigatorios`, `aprovado`, `bloqueado_por_dependencia`.

As extensões ESP continuam condicionadas ao escopo da auditoria. As evidências empíricas de AVA-07 mantêm as duas etapas ali definidas. Nenhuma etapa pode ser declarada executada sem ter sido realizada.
