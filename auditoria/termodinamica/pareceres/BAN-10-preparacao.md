# BAN-10 — preparação independente da auditoria

Data: 27/10/2026. Responsável: Auditor AAA, agente automatizado independente da autoria. **Documento de preparação, sem aceite de entrega ou liberação de outro ID.** O Corretor ainda deve apresentar diagnóstico e plano antes de alterar o produto; o parecer definitivo depende de versão congelada.

## Base e limite do recorte

Base herdada de FON-09 r2: HTML `6ed5c74f03b2ce449f88e79d143c904442c524166a83afce8f12441d391a6625`; inventário `af30160109fa7e9e007e6de74eb1836896194ff90888aec75e0f8a4a86675618`. Banco atual: **197 itens — 30 iniciais, 80 CR, 80 AV e sete abertos**.

BAN-10 exige conferir especialmente CR09/24/68/79, pesquisar outros casos, distinguir texto oficial, gabarito oficial, interpretação técnica e dado suplementar, e retirar da nota de domínio ou reformular como estudo crítico quando uma ambiguidade impedir medida válida. Não se exige nesta rodada a auditoria numérica integral de BAN-08, o fechamento de BAN-07 ou a conferência global de fontes FON-01. Um cálculo ou uma conferência adicional necessária para decidir uma ambiguidade específica pertence ao recorte de BAN-10.

## Leituras preliminares por ID

| ID | Evidência consultada e questão decisória |
| --- | --- |
| CR09 | Prova TBG `888_TBG_019_01`, item 39, p. 1, consultada diretamente: o contexto não restringe expressamente a unidade de base da temperatura termodinâmica. Kelvin e grau Celsius têm papéis distintos no SI; escolher a letra oficial não resolve por si essa omissão. Separar o texto histórico da interpretação que pressupõe essa restrição. |
| CR24 | Prova TRF6 `034_TRF6_011_01`, item 52, p. 1: a comparação literal usa pressões de gás e de água. Para o gás, a razão dependeria de n/V não informado; a pressão da água no ponto triplo não pode ser substituída pela pressão do gás termométrico. A razão 373,15/273,16 somente pertence à leitura suplementar com o mesmo gás, mesma quantidade e volume fixo. |
| CR68 | Fontes oficiais, 15 células e dados corrigidos já conferidos em FON-09. Herdar somente mediante identidade. A afirmação sobre a possibilidade de reduzir perdas com baixa emissividade é separável dos dados de água defeituosos; esses defeitos não tornam automaticamente inválido o julgamento de emissividade. A explicação deve preservar as condições da comparação e evitar generalização a todos os modos de transferência. |
| CR79 | Prova FGV INPE TG15, tipo 1, item 30, p. 8, consultada diretamente. Alto vácuo não determina a razão entre condução pelos sólidos e radiação. Sob as mesmas condições fornecidas, variar condutâncias, áreas e emissividades pode inverter a predominância; faltam condições para demonstrá-la. Distinguir os mecanismos possíveis da predominância pressuposta pela alternativa oficial. |
| CR55 | Candidato adicional já registrado no inventário. A prova TBG `888_TBG_023_01`, item 47, p. 1, contém a expressão “pressão isentrópica”: a leitura textual oficial confirma que não foi introduzida pelo curso. Não corrigir silenciosamente a transcrição nem presumir intenção. O resfriamento isocórico também listado é incompatível com o Brayton ideal; esse erro independente pode manter o julgamento falso apesar da redação anômala. A decisão de uso deve explicar esse ponto. |

As quatro provas e os quatro respectivos gabaritos de CR09/24/55/79 foram abertos nas fontes oficiais. Após a obtenção dos PNGs pelo coordenador, o Auditor abriu pessoalmente as quatro imagens de gabarito e confirmou coluna, número e identidade: 39=E, 52=E, 47=E e TG15 tipo 1, 30=B. O último está na página física 4 do PDF, embora o rodapé impresso diga “Página 1 de 11”. Os hashes dos quatro PNGs e respectivos PDFs conferem; detalhes em [registro visual independente](C:/Users/User/Downloads/SOP-CE/auditoria/termodinamica/pareceres/BAN-10-preparacao-visual.json). As provas foram lidas textualmente na fonte oficial, sem alegação de inspeção visual própria dessas quatro páginas. CR68 já tem conferência visual em FON-09.

Fontes oficiais abertas nesta preparação:

- CR09: [prova TBG](https://cdn.cebraspe.org.br/concursos/tbg_23/arquivos/888_TBG_019_01.PDF#page=1) e [gabarito definitivo](https://cdn.cebraspe.org.br/concursos/tbg_23/arquivos/GAB_DEFINITIVO_888_TBG_019_01.PDF#page=1).
- CR24: [prova TRF6](https://cdn.cebraspe.org.br/concursos/trf6_24/arquivos/034_TRF6_011_01.PDF#page=1) e [gabarito definitivo](https://cdn.cebraspe.org.br/concursos/trf6_24/arquivos/GAB_DEFINITIVO_034_TRF6_011_01.PDF#page=1).
- CR55: [prova TBG Mecânica](https://cdn.cebraspe.org.br/concursos/tbg_23/arquivos/888_TBG_023_01.PDF#page=1) e [gabarito definitivo](https://cdn.cebraspe.org.br/concursos/tbg_23/arquivos/GAB_DEFINITIVO_888_TBG_023_01.PDF#page=1).
- CR79: [prova INPE TG15](https://conhecimento.fgv.br/sites/default/files/concursos/tg15.pdf#page=8) e [gabarito definitivo retificado, TG15](https://conhecimento.fgv.br/sites/default/files/concursos/gabarito-definitivo-inpe-tecnologista-retificado-02.08.pdf#page=4).

Referências técnicas primárias consultadas:

- [NIST SP 330, seção 2](https://www.nist.gov/pml/special-publication-330/sp-330-section-2): unidade de base kelvin, temperatura Celsius e sua unidade. A tentativa de abrir diretamente o PDF do BIPM falhou por timeout; essa tentativa não conta como leitura do PDF.
- [NIST, Primary Acoustic Thermometry up to 800 K, §1.2](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=100632): a termometria a volume constante compara pressões da mesma amostra gasosa. Usar a relação e suas hipóteses; o texto histórico não deve ser usado como definição atual do kelvin baseada no ponto triplo.
- [NASA, Thermal Control, §7.2.1 e §7.2.3](https://www.nasa.gov/smallsat-institute/sst-soa/thermal-control/): radiação, condução e dependência das ligações térmicas. A presença de vácuo não fixa a predominância entre esses mecanismos.
- [MIT Unified, §6.4, Brayton em coordenadas T–s](https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node47.html): duas etapas isentrópicas e duas trocas de calor isobáricas no ciclo ideal.

## Cobertura que será exigida da entrega

1. Registro de triagem por ID para os **197 itens da versão-base**, com conclusão e razão suficiente para localizar a leitura. Uma busca por palavras ou somente os cinco campos de ambiguidades já existentes não comprova a cobertura. Resultados sem indício, indícios descartados com fundamento e casos tratados devem ser distinguíveis.
2. Para cada caso material, expor a passagem relevante, a fonte/versão quando oficial, as interpretações tecnicamente defensáveis, quais hipóteses são adicionais e se a diferença pode mudar a resposta ou a validade da medida. “A banca disse” não substitui demonstração técnica; uma hipótese didática legítima também não é automaticamente um defeito.
3. Decisão individual de tratamento: manutenção justificada, restrição de uso, retirada da pontuação pertinente ou estudo crítico efetivo. Estudo crítico deve pedir/analisar justificativas e reconhecer insuficiência quando cabível; não basta trocar o título e continuar punindo uma leitura física defensável.
4. Atualizar inventário, textos de feedback, referências e dados suplementares em coerência com o tratamento. Preservar claramente o gabarito documental quando a alteração for apenas do uso pedagógico; não chamar uma decisão editorial de anulação oficial.

As notas independentes de BAN-02 e as auditorias das sete tarefas abertas são insumos de busca, não aceites automáticos de BAN-10. Entre as pistas adicionais das notas anteriores estão CR39 (condições de aplicação de Kelvin–Planck) e CR51 (modelo de Brayton); ainda exigem decisão contextual, não foram classificados como inválidos neste preflight. AV24 e AV79 já explicitam condições que faltam aos respectivos CR; correspondência temática não impõe a mesma decisão de validade. A revisão integral da triagem será feita contra a entrega congelada.

## Aplicação efetiva na interface e persistência

A leitura do código atual mostra dois fluxos: `iniciarBanco` mantém placares CR/AV separados das questões iniciais e do registro de progresso. Seu `filtrar` conta toda resposta como correta/incorreta segundo `data-cr-gabarito`; `mostrarResposta` usa feedback categórico. Assim, a exclusão deve ser demonstrada no fluxo real escolhido e na informação que o aluno vê, inclusive para respostas antigas já salvas. Uma observação em Markdown não modifica essas contagens.

Na revisão serão confrontados os numeradores/denominadores aplicáveis, rótulos de comparação com gabarito oficial versus julgamento técnico, filtragem, resposta/refazer e recarga do histórico. Se a implementação tocar código compartilhado, comprovar comportamento preservado para artigos sem a nova marcação e para outros módulos; a autorização curricular continua exclusiva do E1. A solução pode manter histórico documental sem usá-lo como evidência válida de domínio, desde que a interface e os cálculos implementem essa distinção.

Não se exige criar nesta correção uma certificação global de domínio nem concluir BAN-03/07/08/12 ou QA-04. Será exigida a correção concreta dos efeitos identificados no recorte, sem alegar como implementado o que estiver apenas planejado.

## Estado

**Preflight concluído; sem parecer de aceite.** Nenhuma dependência identificada impede começar o diagnóstico de BAN-10. A análise da triagem completa, eventual conferência documental adicional motivada por novos casos e os testes da implementação dependem da entrega e de suas decisões concretas. Produto, controle e checklist não foram alterados pelo Auditor.
