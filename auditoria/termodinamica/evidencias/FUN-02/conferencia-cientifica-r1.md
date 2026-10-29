# Conferência do Corretor — FUN-02 r1

27/10/2026. Escopo exclusivo: diferenciais, caminhos e propriedades. Esta conferência registra autoria/revisão interna e evidências auxiliares; não constitui o parecer do Auditor.

| Critério | Implementação verificável |
|---|---|
| FUN-02: mesmos estados, caminhos e balanços | P1 exige construir dois caminhos sob restrição térmica, integrar cada trecho, rejeitar candidato inviável e fechar ciclo orientado. ΔU é comum, Q/W diferentes; alternativas válidas recebem crédito. |
| Diferenciais e domínio | Teoria distingue exatidão global/local, C¹, domínio aberto e hipótese suficiente de simples conexão; P2 reconstrói potencial e rejeita teste apenas numa linha ou num ciclo. |
| Parciais e condição mantida | Exemplo f=θν e trajetória ν=θ²; P2 diferencia potencial com ν fixo e ao longo de ν=θ, convertendo a base para kelvin; P3 distingue capacidade de propriedade e de caminho. |
| Objetivos e pré-requisitos | fun02-objetivos e fun02-entrada; recuperação guiada de integrais, sinais/unidades e preparação específica de ln e coordenadas antes dos problemas. |
| Teoria, hipóteses e decisões | Modelos ideal/calorífico, composição fixa, fronteira mecânica e sinais explicitados. Exemplos resolvidos de potencial, perfil p(V) e capacidade em isoterma. |
| Exercícios independentes | P1 construção/viabilidade; P2 diagnóstico de registrador e parâmetro; P3 compressão definida e crítica às capacidades. Exposição local detalhada nos três registros. P3 foi estimado intermediário, sem inflar nível pelo formato. |
| Soluções e rubricas | Três details com desenvolvimento, 10 pontos por atividade, alternativas válidas, erros críticos e regra comum de crédito para erros numéricos propagados. Limiar pedagógico 8/10 ainda não calibrado. |
| Fontes e versão | E1-FUN02 v1.0, 27/10/2026; seis fontes primárias no pacote. Modelos/dados didáticos autorais, R arredondado declarado, referências dimensionais explícitas e nenhuma extrapolação de tabela real. |
| Revisão numérica | Módulo reprodutível com 49 verificações. Coordenador calculou P1/P3 antes das soluções; P2 foi rederivado por ele com resultados do apoio conhecidos. Auditor fez preparação de P2 com enunciado isolado, sem aceite antecipado. |
| Integração C01–C10 | Seis células afetadas ligam teoria e atividade, conservam alcance parcial e lacunas. Não há declaração de competência integral nem encerramento GOV-02. |
| Preservação | 194 artigos e registros prévios idênticos; oito arquivos compartilhados/anteriores confirmados; reconstrução byte a byte da fonte anterior. |

## Decisões científicas e limites conferidos

- ∮δQ ou ∮δW pode ser zero num ciclo particular. Uma observação nula não prova exatidão, e a aula não exige que toda forma inexata dê integral não nula em qualquer laço. O ciclo largo de P2 cancela o defeito; o esquerdo identifica κ=0,2 na família declarada.
- A linha θ=2 não é uma vizinhança bidimensional. Restrição a uma curva admite antiderivada de uma variável sem criar potencial no domínio. Integrabilidade de modelo em J/mol não prova que seja energia de substância real.
- W=∫p dV está limitado ao modelo mecânico do enunciado. A inversão física do ciclo usa a reversibilidade explicitamente fornecida; não basta reverter uma curva de processo irreversível.
- P1 tem cinco combinações ordenadas válidas entre os três controles, e uma inválida por chegar a225 K; não se exige coincidência com o par de referência. O SVG quantitativo aparece apenas dentro da solução e possui dados equivalentes no texto/tabela.
- P3 não chama o calor de propriedade nem confunde C total e c molar. C_caminho negativo decorre do trabalho e não implica capacidade de propriedade negativa.
- Retirar apenas a reversibilidade externa não invalida automaticamente δQ/T_gás=dS para gás ainda internamente reversível, com estados e trabalho mantidos. Texto distingue temperatura interna e do reservatório, geração externa e eventual geração interna; balanço geral de entropia permanece fora do alcance desta unidade.

## Responsáveis e evidências

Corretor: teoria, P1/P3, leitura/revisão de P2, integração, cálculo, inventário e preservação. Apoio_fun01: preparação matemática e P2. Coordenador: fontes complementares, cálculos, SVG quantitativo e teste de navegador separado. Auditor independente: parecer formal ainda pendente.

Arquivos locais: calculo-r1.json; verificacao-r1.json; calculos-preliminares-coordenador-r1.json; reproducao-coordenador-r1.json; figura-coordenador-r1.json; revisao-coordenador-pre-congelamento-r1.md. O navegador é documentado pelo coordenador em evidência própria após conferir o hash final. Não houve piloto com estudantes, medição de dificuldade nem certificação externa. Os itens legados com limitações continuam registrados e não foram usados como comprovação da unidade nova.
