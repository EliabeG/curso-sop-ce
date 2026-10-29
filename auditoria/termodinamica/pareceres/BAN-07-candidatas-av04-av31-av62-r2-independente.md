# BAN-07 — revisão preliminar independente das candidatas AV04, AV31 e AV62

Data: 29/10/2026. Revisor: `/root/auditoria_av61_70`, agente automatizado independente do Corretor. **As três candidatas estão aprovadas somente como redações isoladas, no escopo científico abaixo.** Nenhuma foi aplicada por esta revisão; isso não aprova a futura entrega r2, nem BAN-07, nem libera outro ID. AV69 não é objeto desta revisão.

## Critério, versão e método

BAN-07 requer suficiência e consistência, resposta única, demonstração da chave e justificativa dos distratores com erros plausíveis. O parecer [BAN-07-r1](BAN-07-r1.md), SHA-256 `a7a5b0acb7bf5d8648e7403d15a947083d45dfa857e3250caf602ee6db0b60ef`, confirmou os ajustes AV04-E, AV31-B e AV62-B. A plausibilidade julgada aqui é teórica, sem dados de escolhas reais de estudantes.

Li os três fragmentos integrais, JSONs, texto de r1 e bases de estudo ligadas antes das alternativas. Li todas as alternativas e comentários, derivei a chave sob as hipóteses acessíveis, conferi o mecanismo específico do distrator e procurei segunda resposta plausivelmente correta. Comparei cada artigo isolado ao artigo do HTML r1: revertendo apenas os dois literais informados (texto da opção e seu comentário), a comparação é exatamente igual em cada caso; cada literal novo ocorre uma vez. A comparação remove apenas o terminador de linha fora do artigo. O HTML real permanece com SHA-256 `de614a44d796ca04268915f89f502060db2772835c072036a990802eff912b80`, igual à r1, e os demais quatro arquivos declarados também coincidem com o parecer r1. Não foram executados os verificadores do Corretor; a identidade dos fragmentos, a reversão e a análise científica são desta revisora. Nenhuma evidência de comportamento em navegador ou armazenamento foi produzida.

| Candidata isolada | SHA-256 do fragmento completo | SHA-256 do JSON | SHA-256 do artigo r1 |
|---|---|---|---|
| AV04 | `6ed8f664d46db759064d42ee073379bda2b8c1c7018ae3418d22774e14f72501` | `973c4c2b82c8ae97ed4f8a784399df44d9cf3f75d80e303943844f368777b05f` | `25f60f37c5a530e2a2d19a9f0743d8941e83178ebb6663947566fd34f0bbfead` |
| AV31 | `2b2015e4ce0ec1bbea95c3da375ec316239d427f44454cfa43ca007c777fff7a` | `51dcf6eeba809fdf5294ddc0b86e5d048424697041930b1fe37b5c6a706e96c1` | `5ad8025f710d611c6b661937f00ff0ab4c9acc366056f9b12fa80fa81c7b8faf` |
| AV62 | `795e127dad4361f30a6056f49479171b12c849388cdcdebde7fc09561be75ae7` | `4c8604d81bf884e5459d26f006c051451357d31a6085b96c8d80724345e0f0bc` | `3afa637b59ec0aa48e6885ab0877b0ed1bada0bcebe86c841d221e1559235148` |

## AV04-E — aprovada como proposta isolada

Com água líquida longe do ponto crítico e faixa moderada, a base define o modelo operacional v≈constante na faixa. O novo E exige **temperatura necessariamente constante**: confunde incompressibilidade com isotermia e não é consequência do modelo. Como contramodelo, num modelo de v constante e calor específico positivo, bomba adiabática irreversível pode consumir trabalho específico vΔp+ε, ε>0, produzindo ΔT=ε/c>0; ε pequeno mantém a faixa declarada. Assim um caso possível de temperatura constante não faz E necessária. O comentário explica exatamente a distinção.

- A é falsa: o inventário de massa de um volume de controle pode variar, por exemplo enchendo um tanque parcialmente ocupado com líquido de densidade constante; não se confunde material incompressível com massa invariável em todo volume de controle.
- B é falsa: bomba pode elevar pressão enquanto v varia desprezivelmente; confunde incompressível com isobárico.
- C é falsa: v=1/ρ é positivo para densidade finita; confunde variação desprezível com valor nulo.
- **D é única correta**, enunciando a aproximação na faixa, e seu comentário concorda com a base.
- E é falsa e plausível como troca de grandezas constantes: temperatura em lugar de volume específico. Sua nova justificativa corresponde ao texto.

Sem quantidades numéricas a arredondar, nem equivalência de proposições. A chave D, comando e demais alternativas permanecem iguais a r1. A análise não prevê temperatura real de uma bomba específica.

## AV31-B — aprovada como proposta isolada

Na comparação padrão com base comum de combustível, temperatura e pressão de referência iguais, o PCS considera água dos produtos líquida e o PCI vapor. Quando se forma água, a diferença é a parcela de condensação, não uma mudança de temperatura de referência. O novo B confunde calor sensível entre temperaturas diferentes com a contribuição da mudança de fase mantendo a água na mesma fase; sua justificativa corrige essa confusão. A expressão n[hᵥ(Tref,pref)−hₗ(Tref,pref)] representa a diferença na convenção indicada; água no produto pode estar em referência hipotética, sem supor vapor e líquido em equilíbrio com pressão total da mistura. Se não se formar água, não se promete diferença estritamente positiva universal.

- A inverte a identificação: atribui recuperação somente ao PCI, em vez do PCS.
- B introduz diferenças de temperaturas e mantém fase, trocando calor sensível pela diferença de referência de fases; é falso no modelo comparado e plausível.
- C impõe igualdade para qualquer combustível; basta um combustível que produza água para refutar a obrigação universal.
- D confunde consumo elétrico auxiliar de equipamento com definição de poder calorífico do combustível.
- **E é única correta** no modelo e na leitura de comparação ensinados: identifica a parcela de condensação no PCS. O comentário da candidata expressa os estados de referência.

As cinco afirmações são semanticamente distintas; arredondamento não se aplica. O comando, a chave E e os outros quatro distratores permanecem iguais. A resposta refere-se à convenção de poder calorífico, não à eficiência real de uma instalação.

## AV62-B — aprovada como proposta isolada

A etapa especifica entrada efetiva de gás; na base de compressor alternativo normal com válvulas automáticas, a pressão de sucção supera a pressão da câmara suficientemente para abrir a admissão e a descarga permanece fechada. O novo B diz que a admissão abre **somente quando** a pressão da câmara supera a da sucção. Na etapa de entrada normal, essa condição está invertida: B não se torna verdadeira só porque contém as mesmas posições de D. O comentário identifica corretamente a inversão e a hipótese de válvula automática. Não se estende o juízo a acionamento forçado, falhas ou transientes excepcionais.

- A troca admissão e descarga, arranjo normal da descarga.
- B mantém as posições de D, mas acrescenta condição de pressão incompatível; confunde diferença requerida para descarga com a necessária à admissão.
- C fecha as duas válvulas durante toda a entrada, inviabilizando a passagem descrita.
- **D é única correta**: admissão aberta e descarga fechada na etapa indicada.
- E mantém a descarga aberta durante toda a sucção normal; não descreve as posições usuais.

A redação e o comentário B expressam o erro concreto confirmado em r1. Não há alternativas numéricas ou arredondamento. Enunciado, chave D e as outras opções permanecem iguais. A aprovação é condicionada ao modelo convencional acessível previamente, não à afirmação de que todos os compressores alternativos possíveis usam exatamente esse acionamento.

## Critérios, limitações e reapresentação

| Critério | Resultado nas três candidatas |
|---|---|
| Mudanças pretendidas e chaves | Cada fragmento reverte exatamente ao r1 ao desfazer a alternativa e comentário modificados; D, E, D mantidos. |
| Suficiência e consistência | Atendidas nas hipóteses indicadas e bases vinculadas; nenhuma generalização para todos os dispositivos reais. |
| Cinco alternativas, chave única e comentários | Examinados individualmente acima; sem segunda resposta correta identificada. |
| Plausibilidade do distrator alterado | Erros de isotermia, calor sensível e diferencial invertido são específicos e coerentes com a redação efetiva; plausibilidade é teórica. |
| Equivalência após arredondamento | Não aplicável: três itens conceituais, sem alternativas numéricas. |
| Produto, identidades digitais, persistência e navegador | Candidatos isolados não comprovam aplicação nem comportamento. Se aplicados, conferir novos hashes, inventário, colisões de digitais, histórico sem migração, aviso, placar e persistência após recarga, no produto efetivo. |

**Decisão:** AV04-E, AV31-B e AV62-B aprovadas como candidatas literais isoladas, sem ajustes científicos adicionais identificados nesta revisão. Qualquer alteração posterior exige novo confronto. A aceitação da entrega real r2 depende de exame integrado e das pendências científicas de BAN-07; somente o coordenador controla os próximos passos. Sem piloto, psicometria, certificação externa ou revisão humana alegados.
