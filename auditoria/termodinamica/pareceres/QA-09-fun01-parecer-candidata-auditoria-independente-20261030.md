# QA-09 — revisão independente da candidata FUN-01 v e ρ

Data: 30/10/2026. Revisor: agente automatizado independente `/root/qa_diagnosticos`. **Veredito: candidata isolada adequada para o achado identificado.** Ela não foi aplicada ao HTML e não há aprovação da versão efetiva corrigida. O lote FUN-01 e QA-09 permanecem em correção; outro ID não está liberado.

## Critério, objeto e versão

QA-09 exige identificar e conferir os conteúdos numéricos e sua interpretação fora dos artigos já tratados em BAN-08. O [parecer anterior](QA-09-fun01-textos-tabela-auditoria-independente-20261030.md) identificou no mini parecer da âncora `fun01-parecer` uma inferência sem suporte sobre a procedência de medições de volume específico e densidade. Examino apenas a candidata dessa frase e seu impacto provável, não todos os textos e atividades de FUN-01.

HTML `modulos/e1-termodinamica.html` SHA-256 `200f9b773050594d762cc596a5a89297024b245fc4f504081fc77baaed3db95f`; inventário r7 `5090b9897a4698e0ad090f45182afba5880361aabc9fd3c3bdf848d971a85a1a`. A candidata fica em `auditoria/termodinamica/evidencias/QA-09/fun01-parecer-candidata-20261030/`: `analise.md` SHA-256 `896115b15e5d5badfaa068eaa53f0bbd27548241be284c6abcd5836460e9bd5f`, `original.html` `8e3356849c04119255f3a2d309e5fc59423a4b25c70d7528d655d4b97f40ea2e`, `candidata.html` `8f6646b348f707e126276ee8a7d9dcf66f8abede57ebb5cf688023b1c9b99e43`, `manifesto.json` `dd715d6f108d56903b33623e43a19146971dd01cde7dac86a49eaff6e5a7a2e8`. Os quatro são arquivos completos, incluindo quebra final dos fragmentos HTML isolados.

## Verificações independentes

O parágrafo original ocorre uma vez na fonte, começando na posição UTF-16 114112 dentro da unidade 3.1; a candidata não ocorre no HTML vigente. Retirada somente a quebra final dos fragmentos isolados, os hashes do original e da candidata são `bdcd77b078906b6727248748ec8a21ff50fb891522a0aa61b62fc5cddd07294f` e `7bc490923640adfe4d11c52c12ac26f4281bd51a46c348d1836e8807eed886d4`. A substituição literal única da frase `antes` pela frase `depois`, indicadas no manifesto, reproduz a candidata completa. O restante do parágrafo é idêntico.

Para a mesma amostra e mesmo instante, v=V/m e ρ=m/V implicam ρ=1/v. Assim 1/(0,004 m³/kg)=250 kg/m³ e ρv=1; os valores centrais são compatíveis e não são duas propriedades independentes de estado. A matemática não indica a origem das medições. Valores derivados um do outro e duas medições independentes poderiam produzir os mesmos números; sem incertezas não se certifica concordância metrológica. A candidata retira precisamente a afirmação não sustentada de obtenção por inversão e preserva os cálculos, o julgamento de redundância e a necessidade de uma propriedade independente em região e modelo adequados. Não determina a fase nem acusa um sensor.

O trecho proposto é explicação da unidade FUN-01 fora dos 197 artigos pontuados. Em inspeção de escopo, não há mudança proposta de enunciados, soluções de artigos, dados, fórmula ou scripts; isso não substitui confronto efetivo após edição. A aplicação mudará o hash integral e deslocará posições posteriores, exigindo nova fotografia/mapeamento, confronto dos 197 artigos e reavaliação localizada dos aceites de FUN-01 e BAN-02/07/08 potencialmente dependentes da versão, sem presumir transferência de aceite. A compatibilidade numérica dos itens vizinhos permanece apenas no alcance do parecer anterior.

| Critério localizado | Resultado |
|---|---|
| Identidade do original e integridade do delta | Atendido para a candidata isolada, mediante localização e hashes acima. |
| Correção do modelo, unidades e conclusão | Atendido sob as condições da mesma amostra e instante. |
| Distinção entre redundância e procedência das medições | Atendido na candidata; não inferida a origem. |
| Versão aplicada, regressão, inventário e impacto | Não executados; precisam de conferência e novo parecer após a aplicação. |
| QA-09 integral e próximo ID | Não atendido; permanecem bloqueados. |

Não foram realizados teste em navegador, revisão humana, avaliação com alunos ou certificação externa. A adequação da candidata não libera automaticamente outro ID nem aprova o curso como avançado.
