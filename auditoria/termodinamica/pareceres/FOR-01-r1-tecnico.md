# FOR-01 r1 — subparecer técnico independente

Data: 28/10/2026. Revisor: agente automatizado de apoio ao Auditor AAA. Escopo: estrutura, representações, rastreabilidade, deltas, preservação e integridade. **Nenhum bloqueador técnico identificado nesse escopo.** Este apoio não concede aceite geral nem libera próximo ID.

Foram lidos o protocolo, o critério FOR-01, a preparação independente, o plano, o código do verificador, o JS do formulário, a entrega e o manifesto congelado. A matriz individual e os resultados completos estão em `FOR-01-r1-tecnico.json`, neste diretório.

## Versão examinada

| Arquivo | SHA-256 |
| --- | --- |
| Manifesto | `b8beebf1ee084ce8387f79c104194b44932e9af656889bcddadae94343ce2f5b` |
| Formulário | `e74b3b3a80bd003914c16bd46afd9ec2bc8abba6f374042da21cbf983a5c88fd` |
| Aula | `dcb29695129041b0dea7383396d2af85f1d656d6414658f8983042bec1f598dd` |
| Inventário | `069b30f55e2c061a9beefff09252169d89d8e7134f537de6034dc76ced6c3665` |

Conferidas **45 entradas** do manifesto, incluindo entrega, e **nove cópias**, em tamanho e hash, sem divergências. Os arquivos executados correspondem à versão congelada.

## Reprodução entregue

O kernel Node REPL foi reiniciado antes das importações. O script `verificar-for01-r1.mjs` foi lido integralmente antes de chamar `verificar()`: faz leituras, comparações e cálculos, sem gravação de produto. A chamada concluiu dentro de 30 segundos.

Resultado: **913/913 verificações satisfeitas**, idêntico ao JSON entregue. O validador canônico retornou **197 artigos/registros, 29 recursos e 1.166 links locais**, sem erros ou avisos. As contas seletivas presentes no verificador foram reproduzidas; isso não as converte em uma segunda revisão científica independente.

## Confronto independente

| Critério técnico | Evidência obtida |
| --- | --- |
| 100 fichas individualizadas | Cada ID foi confrontado com seu registro: número, título, grupo, hashes anterior/atual, condição, símbolos e vínculos coincidem. A matriz contém um resultado por ficha. |
| MathML | Os **191 blocos MathML** são literalmente iguais à base. Todos foram aceitos por `System.Xml.XmlDocument`, com `XmlResolver=null`, namespace MathML correto e zero erros. A quantidade de filhos de frações, índices, expoentes, sobre/subscritos também confere. |
| Conteúdo pesquisável | Para cada uma das 100 fichas, substituir apenas os textos anteriores de símbolos e condições pelos atuais reproduz exatamente o novo `data-busca`. Assim, títulos e expressões pesquisáveis permanecem conservados, e os esclarecimentos publicados estão pesquisáveis. |
| Delta do formulário | **61 fichas alteradas e 39 preservadas**. Cada trecho anterior ocorre uma vez; hashes dos trechos conferem. Os 61 deltas reconstroem o formulário inteiro e seus IDs coincidem com o conjunto efetivamente alterado. |
| Delta da aula | **17 substituições únicas em 14 alvos** reconstroem integralmente a aula. Os **197 artigos** foram comparados individualmente e permanecem iguais. |
| Inventário | Os **197 registros** permanecem iguais. Comparação independente encontra somente `fonte.sha256` e `fonte.snapshot`, exatamente como no delta declarado. |
| Vínculos | Três complementos nas fichas 03, 05 e 33; troca de destino na 85, para `base-refrigeracao`. O conjunto corresponde ao declarado; a existência dos destinos foi reproduzida. |
| Infraestrutura e partes aceitas | JS/CSS próprios do formulário, JS/CSS compartilhados, registro.js, resumo e unidades FUN-01/FUN-02 preservados, conforme verificações reproduzidas e integridade do pacote. Nenhum teste funcional desnecessário da infraestrutura intacta foi acrescentado. |

## Limites e encaminhamento

O confronto das representações verifica conservação literal de MathML/expressões pesquisáveis e sincronização dos textos alterados. Validade XML e igualdade com a base não certificam equivalência algébrica ou adequação científica; o Auditor principal está responsável pela ciência individual das 100 fichas e pela suficiência dos vínculos. Existência de âncora também não constitui comprovação pedagógica.

Não houve teste de navegador deste apoio, acesso ao navegador/armazenamento do usuário, aplicação com alunos ou impressão física/PDF. Os testes de interface do coordenador permanecem atribuídos a ele. Não foram executados scripts de aplicação nem modificados produto, controle ou evidências do Corretor.

**Ajustes técnicos obrigatórios identificados: nenhum.** O parecer geral de FOR-01 depende da consolidação científica pelo Auditor AAA.
