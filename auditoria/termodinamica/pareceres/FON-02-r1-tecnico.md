# FON-02 r1 — subparecer técnico independente

Data: 28/10/2026. Revisor: agente automatizado /root/auditor_aaa/tecnica_fon01. Escopo exclusivo FON-02 r1 congelada.

**Resultado: ajuste documental necessário no índice individual de fontes (T1).** A integridade e a preservação do produto passaram. Este subparecer não julga a ciência dos 80 diagnósticos, não aprova o gate global e não libera próximo ID.

## Identidade da versão

| Objeto | SHA-256 |
|---|---|
| Manifesto FON-02 r1 | 25c420ff6f7650c982c402b3715c623ca7e68866f72e26bbbf0565fc6e065224 |
| HTML baseline FON-01 | 81eedea9f3731979125724ebb52d839ca68930164b7d7570a2a646d6f5bed2fe |
| HTML entregue FON-02 | 0fc12a96fd30d366770a56c366fb61bc6a9fa7bd761e81fb40242a30f6dd78c7 |
| Matriz dos 80 | ffeab0e9324624579772588dd010d2d70ad256e025290d06a0efb474fd5f9170 |
| Evidência deste subparecer | 1c2f806e68fd9aead878b0d355f08d87e478e0d5ada4e37fa2a341f960fee63a |

Os 55 arquivos, nove cópias finais e dois vínculos FON-01 do manifesto foram conferidos por bytes/SHA. Não há divergência. As nove cópias anteriores também correspondem aos hashes registrados.

## T1 — rastreabilidade individual incompleta e rótulos inexatos

Arquivo: revisao-suplementos-80-r1.json, campo registros[].fontes.ensino_e_fundamentos_ja_vinculados.

Os 80 registros contêm exatamente um alvo, sempre a primeira âncora do artigo baseline. Nos 80 casos, o rótulo corresponde exatamente ao trecho que vai do conteúdo dessa primeira âncora até o fechamento da última, com tags removidas. Por isso inclui outros rótulos, enunciados, opções, controles, comentários e fontes. Esse padrão é compatível com captura gulosa; o gerador não está arquivado no pacote para atribuir uma linha de código específica.

O levantamento independente encontrou **158 ocorrências de vínculos de ensino/fundamento** no baseline, contra 80 destinos retidos no campo: **78 destinos omitidos em 50 registros**, sendo 61 internos e 17 externos. Trata-se de ocorrências por item, sem deduplicar uma URL usada em itens diferentes.

| Caso | Alvo retido | Vínculos omitidos do campo |
|---|---|---|
| CR01 | #base-propriedades | #base-medidas |
| CR06 | #base-leitura-matematica | #base-instrumentos |
| CR10 | #base-leitura-matematica | #base-medidas; #base-propriedades |
| CR34 | Primeiro alvo de estudo | Entre outros, MIT node14, node40 e node41 |
| CR79 | #base-radiacao-vacuo | NASA Thermal Control |

Há cobertura redundante parcial: dez das 17 ocorrências externas têm a URL no catálogo global; somente CR80 também a relaciona no campo de IDs primários do próprio item. As sete ocorrências externas restantes, correspondentes a seis URLs distintas, não constam do catálogo atual: BIPM landing em CR09; OpenStax modelo molecular em CR24; MIT node40 e node41 em CR34; MIT propulsion node27 em CR51 e CR55; GUNT ET508 em CR62. A comparação do catálogo considera a URL sem fragmento, preservando caminho e consulta; não presume equivalência científica de URLs diferentes.

**O defeito pertence à matriz documental.** Todos os 158 vínculos continuam no HTML final e os internos resolvem para uma única âncora. Não há perda de navegação ou remoção de fonte do produto. O Markdown individual não renderiza esse campo e remete ao JSON; por isso não apresenta os rótulos corrompidos, mas também não recompõe o índice faltante. Os vínculos corretos permanecem recuperáveis no snapshot/extrato integral, o que não torna exato o campo estruturado.

Correção necessária: reconstruir cada registro a partir de âncoras individuais, com destino e texto próprios; conferir cobertura dos vínculos pertinentes e relações com o catálogo. A correção documental não requer alteração de enunciados, soluções ou links do curso. A [evidência JSON](FON-02-r1-tecnico.json) contém os 80 casos, alvos esperados, omissões, alcance e cobertura redundante.

## T2 — dois hashes literais com espaço interno

A tabela de entregas/FON-02-r1.md contém espaço interno nos hashes de revisao-suplementos-80-r1.json e navegador-coordenador-r1.md. Removido o espaço, ambos correspondem exatamente ao manifesto e aos bytes efetivos:

- Matriz: ffeab0e9324624579772588dd010d2d70ad256e025290d06a0efb474fd5f9170.
- Relatório de navegador: 62336e3ae7ed87ce927296e547b4d779c48d96bf85731438a792bc2785400a26.

É uma correção editorial para permitir copiar os 64 dígitos contíguos. Não há ambiguidade de versão nem bloqueio binário independente.

## Preservação e representações

A aplicação das 21 substituições locais autorizadas e das 71 trocas de summary reconstrói o HTML final integralmente, sem diferença residual. Os IDs dos 21 alvos coincidem com o escopo autorizado. Permanecem 197 artigos em mesma ordem, com 74 modificados e 123 idênticos em bytes.

Os 734 elementos MathML permanecem idênticos. Enunciados, alternativas, imagens, chaves, atributos e demais componentes oficiais são preservados. O placar conserva 71 itens de treino e nove estudos críticos, com os nove summaries críticos intactos.

Os componentes usados nas digitais dos 160 artigos CR/AV foram comparados e são idênticos. curso.js, curso.css, registro.js, formulário e seus JS/CSS coincidem com os snapshots anteriores. Isso demonstra preservação estática da identidade das respostas; não se declara nova suíte dinâmica de localStorage.

O inventário volta integralmente à versão anterior ao normalizar somente os hashes de artigo e fonte.sha256/snapshot. Nenhum campo pedagógico, origem, hipótese, etapa, classificação, recurso ou uso avaliativo foi reclassificado.

Os 80 blocos Markdown correspondem ao JSON em decisões, autoria, diagnósticos de adições, 21 trechos finais e contagens. Os trechos finais constam do HTML. O resumo do inventário preserva o corpo anterior, acrescenta FON-02 ao título e um apêndice coerente com o delta. Essa coerência não corrige T1, pois o campo defeituoso não é mostrado no Markdown.

## Validadores e limites

O verificador do autor foi lido integralmente e reproduzido por [adaptador](FON-02-r1-tecnico-reproduzir.mjs), com caminhos/imports equivalentes e a única escrita redirecionada para pareceres. Resultado: **205 verificações sem falha**, com [saída](FON-02-r1-tecnico-autor-reproduzido.json) byte a byte idêntica à evidência congelada, SHA-256 aa1030c11966550298f17441aadeac829b78fa03cb04e7d7c3109836d829ad61.

O validador canônico também foi chamado diretamente: **197 itens/artigos, 29 recursos e 1.236 links locais, zero erros/avisos**. As verificações do autor não medem a exatidão/cobertura de ensino_e_fundamentos_ja_vinculados, portanto seu sucesso não elimina T1. O registro independente contém 721 verificações: 719 atendidas e duas condições documentais não atendidas, ambas vinculadas a T1.

Não foram repetidas ciência, leitura visual de PDFs, consulta remota de fontes, captura de navegador ou suíte dinâmica de persistência. Esses limites não impedem o diagnóstico documental acima. A consolidação do gate cabe ao Auditor principal.

Somente este subparecer e suas evidências foram escritos em pareceres. Produto, inventário, controle e pacote do autor permaneceram intactos.
