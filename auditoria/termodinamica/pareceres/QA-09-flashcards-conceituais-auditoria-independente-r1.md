# QA-09 — auditoria independente de 12 flashcards conceituais

Data: 30/10/2026. Revisor: agente automatizado independente `/root/audit_strategy`. **Veredito localizado: AJUSTES OBRIGATÓRIOS**, exclusivamente quanto ao alcance do cartão genérico sobre COP. Os demais cartões foram lidos no alcance abaixo; este parecer não aprova QA-09 integral nem libera outro ID.

## Identidade, escopo e método

HTML efetivo `modulos/e1-termodinamica.html`, SHA-256 `57b13f0d6386764f1cc46ce543013b0eb75f7bfa97ffbd63ea331f38bfc5af8c`; inventário r8 `ae75a258398c385398567457d98ebd49b9838c0c9a4eedc69ea8d2d72981b687`. Entrega `flashcards-conceituais-20261030/entrega.md`, SHA-256 `dd85fdbbc3cd10cc84f263063e1cb21d976c78103b11a935e4acc49ed16807e4`. Examinei os 12 elementos efetivos `details.flashcard` da seção `flashcards`, fora dos 197 artigos; não transferi automaticamente os resultados para outros cartões ou nós sobrepostos. Script independente [`verificar.py`](../evidencias/QA-09/auditoria-flashcards-conceituais-r1/verificar.py), SHA-256 `65c81d48853f71a357b644f47b5803e76b3e830c8bea6143ec3c889f41d3f381`, reextrai título e resposta dos 12 blocos pelo documento, seção, posição UTF-16 e hash e emite resultados sem escrever arquivos. O verificador do Corretor também foi lido e executado sem escrita.

## Achado: COP sem definição da fonte de acionamento

O cartão na posição UTF-16 **1261323**, hash de fragmento `3a59761411a2e8121725915610184bfa700ef7209c46dd2d5ac7a63de47fdebc`, tem título genérico “COP” e resposta “Calor útil transportado dividido pelo trabalho consumido”. Isso descreve o modelo usual de um ciclo acionado por trabalho, se a fronteira e o efeito útil forem definidos. Não é definição universal de todos os indicadores denominados COP: um refrigerador por absorção acionado por calor pode ter COP térmico definido pela carga útil de refrigeração dividida pela entrada térmica no gerador. O [documento técnico do Departamento de Energia dos EUA sobre chillers por absorção](https://www.energy.gov/sites/default/files/2017/06/f35/CHP-Absorption%20Chiller-compliant.pdf), consultado em 30/10/2026, apresenta essa base. Despesas auxiliares podem exigir outro indicador; não se presume que sejam nulas em qualquer instalação. A ressalva não cria obrigação de ensinar absorção fora do escopo prometido: corrige o alcance de uma afirmação genérica.

**Ajuste obrigatório:** delimitar a pergunta ou a resposta ao ciclo de refrigeração ou bomba de calor **acionado por trabalho**, preservando a escolha do calor útil da fonte fria para refrigerador e da fonte quente para bomba de calor; alternativamente, definir expressamente a energia de acionamento pertinente e distinguir a base térmica quando abordada. Preparar candidata isolada, confirmar identidade e ausência de outros efeitos, solicitar revisão independente da candidata e reauditar a versão efetiva com fotografia, inventário e mapa atualizados. Não foi implementada alteração por este Auditor.

## Demais cartões lidos

- **Sistema fechado / volume de controle:** definições breves compatíveis com a distinção de fronteira e fluxos; sistema fechado pode trocar energia e um volume de controle pode ser escolhido ainda que não haja fluxo de massa num caso específico.
- **Propriedades intensiva / extensiva:** definições curtas no contexto usual de sistemas homogêneos e efeitos de superfície/interação desprezíveis; não implicam que valores de propriedades intensivas sejam invariáveis diante de mudanças de estado.
- **Título:** fração mássica de vapor no modelo líquido–vapor saturado; não se deve confundi-la com fração molar de componente ou de fase.
- **Entropia, adiabático e isentrópico:** sínteses compatíveis com propriedade de estado, ausência de transferência de calor e entropia específica constante, respectivamente. Uma fronteira adiabática não elimina transferência por massa ou trabalho e não prova reversibilidade. O balanço completo não foi afirmado no cartão.
- **Estrangulamento:** a redação diz “frequentemente isoentálpica”, não universalmente; essa aproximação requer o modelo usual permanente, uma entrada e saída, outras interações de trabalho/calor e mudanças de energias cinética/potencial desprezíveis. Uma queda de pressão em qualquer dispositivo não é automaticamente um estrangulamento. Há ajuste separado já identificado no cartão de válvula que afirma igualdade de entalpia; este parecer não o encerra.
- **Regeneração e sequência de compressão:** o cartão de regeneração resume recuperação térmica para aquecimento de alimentação sem especificar arranjo; a sequência compressor–condensador–expansão–evaporador é válida para o ciclo simples descrito, não cobre todas as variantes possíveis.

Essas leituras não aprovam bases completas, o comportamento interativo dos cartões ou os nove cartões do outro lote. A ausência de valores numéricos explícitos não foi usada como justificativa automática para dispensar análise.

| Critério localizado | Decisão |
|---|---|
| Identidade dos 12 blocos r8 | Atendida; reextração e hashes conferem. |
| Suficiência científica e alcance do cartão genérico COP | **Não atendido:** explicitar o modelo acionado por trabalho ou a base energética apropriada. |
| Demais onze cartões | Sem divergência identificada sob os limites descritos; não substituem ensino ou verificação do contexto integral. |
| QA-09 global e próximo ID | Não atendido; continuam bloqueados. |

Não houve ensaio em navegador, leitor de tela, estudante, revisão humana ou certificação externa. A consulta da fonte externa não constitui ensaio empírico do curso nem prova a validade de outros sistemas ou de todos os cartões.
