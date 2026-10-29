# BAN-02 — Reapresentação r2

Data: 27/10/2026. Autor: agente automatizado Corretor `/root/corretor_aaa`. Estado: **entregue para nova auditoria independente**. A rodada 1 foi rejeitada; esta entrega responde exclusivamente a R1-A, R1-B, R1-C e R1-D. O Corretor não declara aprovação e não iniciou outro ID.

## Resposta aos ajustes obrigatórios

### R1-A — Unidades de AV45

Corrigidos os seis campos que propagavam J no lugar de kJ: evidência de exposição de Q16; evidência CR45→AV45; etapa 2, hipótese explícita, alcance da competência e evidência AV45→CR45. Agora concordam com o enunciado **1.000 kJ por ciclo** e a rejeição mínima de **500 kJ**. Q16 não ganhou um dado de calor no seu próprio enunciado: a correção pertence à descrição da relação com AV45. Os 900/90 kJ de CR45 e os 1.000/3.000 J de CR42 foram preservados. AV30 continua com seus 300 kJ corretos.

A relação corrigida também foi salva em `relacoes-cr-av-r2.json`; a versão r1 e os insumos antigos permanecem intactos como evidência histórica. Não houve substituição global em arquivos r1.

### R1-B — Demanda real de CR09, CR24 e CR79

Os três itens passaram de intermediário para **iniciante**, com **uma etapa** baseada no comando atual e na leitura condicionada esperada da prova:

| Item | Demanda registrada na r2 |
|---|---|
| CR09 | Reconhecer a unidade de base da temperatura termodinâmica, assumindo essa restrição não escrita na interpretação esperada. |
| CR24 | Aplicar a razão de temperaturas absolutas sob a leitura do mesmo gás com quantidade e volume constantes e julgar a razão igual a um. |
| CR79 | Reconhecer a associação de mecanismos da alternativa esperada, adotando predominância radiativa como pressuposto da prova. |

Notas críticas, insuficiências, hipóteses e ambiguidades foram preservadas. Não são mais contadas como resposta crítica produzida pelo estudante. Ajustei também pré-requisitos e alcance dos três registros para essa demanda; removi C09 de CR24/79 para não sugerir que o comando avalia a formulação da crítica. O método e o resumo agora fazem essa separação. Isso não valida a redação ou o gabarito dos itens.

Nova distribuição: **171 iniciantes, 19 intermediários e nenhum avançado**. Q: 27/3/0; CR: 72/8/0; AV: 72/8/0. São estimativas pelo conteúdo, sem piloto.

### R1-C — Pré-requisitos das 80 versões AV

Todas as **80 listas** foram revistas individualmente pela tarefa e reescritas, sem derivação automática da CR de origem. A [evidência individual](../evidencias/BAN-02/pre-requisitos-r2.json) contém o comando lido, a demanda, os pré-requisitos anteriores e os atuais para cada AV. O [delta integral](../evidencias/BAN-02/delta-r1-r2.json) permite conferir cada alteração.

| Item apontado | Ajuste aplicado |
|---|---|
| AV11 | Leitura da conversão fornecida e substituição; removidas unidades de potência/energia. |
| AV26 | Primeira lei e sinais de eixo/calor; removida conversão kcal/kJ. |
| AV30 | Isotermia, u(T) e primeira lei; removida leitura p–V como requisito. |
| AV33 | Incluídas segunda lei, entropia, irreversibilidade e distinção entre temperatura e entropia constantes. |
| AV39 | Balanço cíclico e Kelvin–Planck; removida conversão cal/J. |
| AV45 | Carnot e balanço cíclico; removida conversão °C/K. |
| AV53 | Redução percentual; regeneração e recuperação de calor retiradas do campo de requisito necessário. |
| AV56 | Associações Brayton e Rankine explícitas; retirado conhecimento de gerador sem função na associação pedida. |
| AV61 | Razão definida e porcentagem; removidos volume morto e reexpansão. |
| AV77 | Primeira lei do ciclo e identificação dos fluxos; não exige cálculo de mudança de fase. |

A revisão alcançou os demais casos, por exemplo AV17 (definição por pressões, sem exigir quantidade de vapor), AV37/40/57 (uso de relação fornecida), AV44 (ciclo e primeira lei, sem exigir eficiência), AV48 (direção térmica, sem contracorrente obrigatória), AV54 (classificação, sem razão de pressão), AV67 (dilatação livre, sem restrição mecânica), AV74 (UAΔTm, sem determinar resistência de incrustação) e AV79 (mecanismos presentes, sem comparação quantitativa). Conhecimentos contextuais não foram usados para inflar a lista.

### R1-D — Hipóteses de AV57

O campo explícito agora registra **Brayton ideal**, **calores específicos constantes**, a expressão de rendimento fornecida e o fator `rp^((k−1)/k) = 2`. A tarefa continua iniciante: substituição do fator, sem dedução da fórmula ou cálculo da potência fracionária.

## Evidências e preservação

- [JSON canônico atualizado](../inventario/inventario-questoes.json) e [resumo legível r2](../inventario/INVENTARIO_QUESTOES.md).
- [Delta r1→r2](../evidencias/BAN-02/delta-r1-r2.json): 112 diferenças de campos, restritas aos quatro achados, incluindo as 80 listas AV e os ajustes coerentes nos três CR.
- [Verificação r2 executada](../evidencias/BAN-02/verificacao-r2.json) e [módulo reproduzível](../evidencias/BAN-02/verificar-r2.mjs).
- [Manifesto r2](../evidencias/BAN-02/manifesto-r2.json) e cópias congeladas dos cinco artefatos de inventário em `evidencias/BAN-02/pacote-r2/`.

O verificador r2 executou **18 verificações dirigidas**, todas satisfeitas: escopo do delta, unidades e CR42, etapas/nível/ressalvas dos três CR, concordância das 80 revisões, hipóteses AV57, estatísticas, preservação das **22 evidências r1** listadas no manifesto e preservação dos quatro arquivos de produto. Incluiu a execução do validador canônico: **190 registros para 190 artigos, sete recursos, 1.022 referências locais, zero erros e avisos**.

A versão 1.1 do schema, o validador e o guia não foram alterados; não se repetiram testes de infraestrutura sem mudança. O produto, suas 190 questões e os aceites BAN-01/GOV-01 permanecem intactos. O controle de fluxo não foi editado pelo Corretor.

Para reproduzir a verificação dirigida no Node REPL:

```js
var v = await import("file:///C:/Users/User/Downloads/SOP-CE/auditoria/termodinamica/evidencias/BAN-02/verificar-r2.mjs");
var resultado = await v.verificarR2("C:/Users/User/Downloads/SOP-CE");
nodeRepl.write(resultado);
```

Essas verificações automatizadas conferem estrutura, escopo e condições explícitas dos ajustes; a suficiência científica e pedagógica continua sujeita ao Auditor. Sem nova auditoria completa de gabaritos, conferência oficial, psicometria ou alegação de domínio avançado. O apoio técnico fez somente leitura dirigida de R1-A/R1-D; o Corretor implementou todos os ajustes.

## SHA-256 da versão entregue

| Arquivo | SHA-256 |
|---|---|
| `auditoria/termodinamica/inventario/inventario-questoes.json` | `d17e2fcf73f2dbbe72005fb70ee6b36d1cad60ef90a1618abaf080d8bfd79507` |
| `auditoria/termodinamica/inventario/inventario.schema.json` | `c71033464d54e71e61d4dcbae56847a88720e5ff937c1e1f7179005ab22d149b` |
| `auditoria/termodinamica/inventario/validar-inventario.mjs` | `ddc8a6831422a868fb5a8b15b2f6653325f6644acf4f5c64dbf35bb0d2369fdd` |
| `auditoria/termodinamica/inventario/LEIA-ME.md` | `cdcd7e965bdc4a998b6e2fa784a53f84f295abcf9ade2d06ce62fff71d072449` |
| `auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md` | `2d82fbde8502a1f5096373f10cf0c57d2c23e7730f3a134dc2d0d7755e4b7590` |

### Produto preservado

| Arquivo | SHA-256 |
|---|---|
| `modulos/e1-termodinamica.html` | `b4e2d672c6feecb4289ad73bb9c16000ff5156720698f10153ff93fa0b788a8e` |
| `assets/registro.js` | `444a13658e0b869760296826be30267215293b18c3074f283b2a1ea252e828a2` |
| `assets/curso.js` | `81728c9fd1e96b738410e6b51cf4ab3ed785fb17753e68a988c1dcf236d8f899` |
| `assets/curso.css` | `b8ded6abc4548f378daab2e299a8a55ba81e8841c41049133a84d93848ee3eaa` |

Pacote congelado para nova auditoria. Nenhum próximo ID está liberado por esta entrega.
