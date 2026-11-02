# QA-09 — auditoria independente da aplicação FUN-01 P3, r11

Data: 30/10/2026. Auditor automatizado `/root/planning`, distinto de `/root/next_examples`, Corretor da aplicação, e `/root/next_graphics`, autor da candidata. **Veredito: APROVADO para a aplicação localizada do P3 na versão efetiva e para a revalidação de alcance descrita.** QA-09 integral permanece em correção e o próximo ID não está liberado.

## Critério e versões

QA-09 exige conferência rastreável do conteúdo numérico fora dos itens BAN-08 e análise do impacto quando uma alteração repercute sobre itens já avaliados. Esta revisão cobre a alteração localizada na solução do artigo autoral `fun01-e1-supercritico`, o inventário, mapa e efeito pertinente em FUN-01 e BAN-02/07/08. Não aprova a totalidade de QA-09 nem substitui a revisão de outros conteúdos.

Aula anterior r10 SHA-256 `a8bed8a91a36a1c1f41cd75e3c1858fecb4e14a506e582ad1fdb186d275805e3`; aula r11 efetiva `f76c39a3e1d8c349ebf0df72cc20a3ab21c68960c8451799bad90a9dcc4bd8c7`; formulário inalterado `01d5d79639cd17dfcaea38479019cf719e2601f5b35d446ab562e50d381fa5c9`. Inventário r10 `3497cbf9ffcbe0a1e2eb84eeb9e34c0cfb6e0ed63a2747795bf75832454e2f6c`; r11 `720f2b9ace69ab8f07be685d5205040569cc72814f67d51d44786872469c07d7`; mapa `3c50f64d7f5a318edfc7544c2f2c628ca8789d45efdef8dcb08c88eac027cc3a`. A [entrega do Corretor](../evidencias/QA-09/aplicacao-fun01-p3-r11-r1/entrega-r1.md) tem SHA-256 `19dec9ca526b6d3bdce51908b1ef8af394ff7df0d9e8369b77a5155fea83c06d`.

## Aplicação e conferência científica

Reconstruí a aula r11 substituindo o único parágrafo original pela candidata aprovada; a reconstrução reproduz o HTML efetivo byte a byte e a fotografia posterior. O fragmento original tem SHA-256 `7b13d7adbb3ec83f676edadbebf7a0246d139ff24bf4931350d7580708b47bd9`, a candidata `ce23ebfff83d3172e72046551cf365a967a098b0640c01acb56480154ccd7015`, ambos sem a quebra final dos arquivos isolados. O artigo anterior tem SHA-256 `2fad0e042fb945eb44d0f2abe2c4e64322434195395fa4e5c084f17854f432a7` e o atual `ab2d00867b0f11bc75810b84c74f8347e308fbf26b07f62de8fc11e0eb378c4d`.

Li enunciado, dados, solução e rubrica diretamente na versão efetiva. A frase agora diz que uma coluna **pode** ser calculada a partir da outra pela identidade `v=1/ρ`, sem afirmar que isso determine a procedência instrumental. Essa redação preserva a dependência termodinâmica e não supõe aquisição independente nem processamento por inversão. Para ρ=800 kg/m³, v=0,00125 m³/kg é recíproco; a igualdade nominal não estabelece como um sensor obteve os valores nem sua incerteza de medição. O enunciado e a rubrica mantêm a pergunta e o objetivo de reconhecer redundância e propor par adequado.

Recalculei as classificações nominais com unidades consistentes: A tem caixa T=[645;655] K e p=[22,00;22,20] MPa, que cruza ambos os limites críticos 647,096 K e 22,064 MPa; B atinge no máximo 641 K, abaixo de Tc; C atinge no máximo 20,1 MPa, abaixo de pc. Melhorar somente uma medida de A deixa a outra caixa cruzar o limite; melhorar ambas para ±1 K e ±0,01 MPa eleva os mínimos a 649 K e 22,09 MPa. Para centros fixos, a garantia estrita exige εT<2,904 K e εp<0,036 MPa; igualdade toca o limite e não garante a desigualdade. D tem 700 K e 25 MPa no caso hipotético exato e satisfaz os dois critérios, enquanto título x líquido–vapor não se aplica à região identificada. Essas contas são para dados didáticos e hipóteses da atividade, não incerteza estatística ou medição real. Um modelo de propriedades da água permanece necessário para obter h, v e s numericamente.

O [verificador independente](../evidencias/QA-09/auditoria-aplicacao-fun01-p3-r11-20261030/verificar.mjs), SHA-256 `8ce45ad67ca6c58ac329850c0f3ec5a722afd41b5ec145d747d4573b2abb322d`, executou sem erro e confirma a reconstrução, hashes, artigos, registros, elementos MathML, ancestral e contas de limites. Não testa a experiência em navegador.

## Impacto, mapa e testes

Os 196 artigos não alvo estão idênticos e na mesma ordem; o P3 é exatamente o artigo anterior com a troca única no parágrafo, preservando enunciado, dados, respostas restantes e rubrica. Os 196 registros não alvo do inventário oficial são idênticos; no P3 somente `localizacao.sha256_artigo` mudou, e nos campos globais somente `fonte` mudou para a fotografia efetiva. Os 734 MathML da aula e o formulário permaneceram iguais. O inventário oficial JSON tem SHA-256 `f2605176763a61832417506517373a16736717d5cc23de7494e901322c394856`; o Markdown `1e5251583294cc3a497bba6693671e6f996f624012c218121c66e5866380bef9` acrescenta seção histórica.

O [verificador independente do mapa](../evidencias/QA-09/auditoria-aplicacao-fun01-p3-r11-20261030/mapa.py), SHA-256 `a0674d651912e134593b619364d09d555fc6e22fe88932222d29ebc305686eda`, conferiu 11.397 pares únicos e seus campos/contextos e deslocamentos: 11.396 externos e um ancestral alterado (`fun01-estado-equilibrio`), cujo hash em ambas fotografias foi recalculado. As 815 referências preservaram destinos e metadados, com deslocamentos esperados. Dos 138 registros de recursos, 105 apontam à aula e refletem seu hash atual; os demais e os seis ativos específicos não mudaram. Dos 197 artigos segregados no inventário QA, somente P3 mudou de hash. Hash igual ou mapa de posição não transfere automaticamente aceites para outras dependências.

Há também [apoio estrutural](QA-09-mapa-r10-r11-apoio-estrutural-r1.md), SHA-256 `edc37bc995c832e66c317977bb7d0cbb29f38e6467f67633d8fbd4416ed4886a`, de agente que **criou a candidata**; por essa relação ele não é aqui tratado como parecer científico independente, mas sua comparação documental concorda com a reconstrução e o mapa acima.

O validador canônico passou com 197 artigos/itens, 29 recursos e 1.263 links locais, sem erro ou aviso. O teste de persistência BAN-08 passou seis cenários em DOM e armazenamento simulados; seus casos dizem respeito às questões AV42/45/52, não demonstram interação do P3 em navegador. As alterações preservam campos, rubrica, outras soluções e dependências do caso examinado. Isso sustenta **revalidação localizada** do efeito desta frase sobre FUN-01 e os aceites BAN-02/07/08, identificando o novo hash do P3; não representa nova auditoria integral de todas as unidades, registros ou aprendizado.

| Critério localizado | Resultado |
|---|---|
| Identidade e reconstrução do único delta | Atendidas na versão r11 efetiva. |
| Ciência, contas nominais e domínio da solução P3 | Atendidos no alcance e modelo declarados. |
| 196 demais artigos/registros, enunciado e rubrica | Preservados na comparação byte a byte. |
| Mapa, fontes e impacto FUN-01/BAN | Verificação e revalidação localizadas; não há transferência automática de demais aceites. |
| QA-09 integral e próximo ID | Não atendidos, permanecem bloqueados. |

Não houve ensaio em navegador real, revisão humana, teste com alunos ou certificação externa. Esta aprovação não classifica o curso como avançado.
