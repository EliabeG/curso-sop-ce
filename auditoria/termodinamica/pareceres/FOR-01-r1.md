# FOR-01 r1 — parecer independente

Data: 28/10/2026. Revisor: agente automatizado `/root/auditor_aaa`.

**Veredito: AJUSTES_OBRIGATORIOS. Próximo ID não liberado.**

## Escopo e versão

Critério FOR-01: conferir individualmente expressão, símbolos, unidades, hipóteses e vínculo efetivo com a aula das 100 fichas; balanços reduzidos não podem ser apresentados como universais. Foram examinadas as 100 fichas finais e os trechos pertinentes de seus 50 destinos distintos, os esclarecimentos locais na aula e as representações/documentos derivados. Não se exigiu ampliar FOR-02 ou implantar outra unidade.

| Arquivo congelado | SHA-256 |
|---|---|
| `formulas/termodinamica.html` | `e74b3b3a80bd003914c16bd46afd9ec2bc8abba6f374042da21cbf983a5c88fd` |
| `modulos/e1-termodinamica.html` | `dcb29695129041b0dea7383396d2af85f1d656d6414658f8983042bec1f598dd` |
| `auditoria/termodinamica/inventario/inventario-questoes.json` | `069b30f55e2c061a9beefff09252169d89d8e7134f537de6034dc76ced6c3665` |
| Manifesto r1 | `b8beebf1ee084ce8387f79c104194b44932e9af656889bcddadae94343ce2f5b` |
| Entrega r1 | `198cfe4b385a54935255e014071f3788a9a30b007f4165d9eed07c6621d582c5` |

## Evidência e critérios

A [matriz científica independente](FOR-01-r1-cientifico.json), SHA `18a7aa8509fe692e6c1b7b8ff62abe0989814230706d59b9a0955f59dc3071ee`, preserva um fundamento por ficha, suas expressões/condições, vínculos, dez deduções ou conferências numéricas e o achado abaixo. Ela confronta a [preparação anterior](FOR-01-preparacao.json), não apenas a narrativa do Corretor. As 96 fichas fora de R1-A atendem ao recorte examinado; as quatro pendentes têm expressões válidas sob hipóteses mais restritas que as publicadas.

O [subparecer técnico independente](FOR-01-r1-tecnico.md), SHA `29abea8760915f2fc792760d8731ed0c86c4382ee568c4d20f99883cc9af156f`, e seu [JSON](FOR-01-r1-tecnico.json), SHA `e58ae7de2cd40e9a0d1c68d59c39a1acdfd031e5d389c0a97593ff5e1322c643`, não identificaram bloqueador técnico. A reprodução em kernel novo confirmou 913 verificações, validação canônica de 197 artigos/registros, 29 recursos e 1.166 links, sem erros/avisos. Foram conferidas 45 entradas do manifesto e nove cópias. São **100 fichas contendo 191 blocos MathML**, todos preservados e válidos como XML.

| Critério aplicável | Resultado e fundamento |
|---|---|
| Registro individual das 100 fichas | Atendido. Identidade, revisão concreta e versão de cada ficha estão registradas; a matriz independente também cobre todas. |
| Expressões e dimensões | Atendido quanto à álgebra e às unidades, condicionado às hipóteses corretas. Foram interpretados os MathML e confrontadas as relações pesquisáveis; R1-A não exige alterar equações. |
| Símbolos, bases e sinais | Atendido, salvo a distinção incompleta entre parcela de eixo e trabalho total descrita em R1-A. Direções de Fourier/radiação, bases mássicas/molares e taxas estão delimitadas. |
| Hipóteses suficientes; reduções não universais | **Não atendido integralmente.** Fichas 23/46/79/84 deixam outros trabalhos não associados ao escoamento fora da exclusão necessária. |
| Ensino efetivo e coerência dos vínculos | Relações efetivamente ensinadas nos destinos. **Pendência de coerência local** em 23/79/84; na 46, a aula já exclui trabalho, mas a ficha enfraquece essa hipótese. |
| Fontes e raciocínio científico | Atendido no escopo, sem sanar R1-A. Fontes primárias conferidas nos pontos sensíveis, leitura visual de quatro páginas de CO₂/umidade e deduções independentes registradas. |
| Representações e manutenção | Atendido tecnicamente. Busca sincronizada; 61 fichas alteradas/39 intactas; 17 substituições em 14 alvos reconstroem integralmente a aula. |
| Preservação e escopo E1 | Atendido. 197 artigos/registros, FUN-01/FUN-02, resumo, JS/CSS e registro preservados. No inventário, somente `fonte.sha256` e `fonte.snapshot` mudaram. |
| Interface pertinente | Evidência funcional do coordenador aceita dentro dos [limites declarados](../evidencias/FOR-01/navegador-coordenador-r1.md). Não é navegação executada pelo Auditor. |
| Piloto, nova cobertura avançada e certificação global | Não aplicáveis a este aceite isolado; permanecem abertos os IDs próprios. |

Na conferência científica, o ótimo da ficha 88 foi rederivado pela soma de dois termos positivos de produto constante; o resultado depende das temperaturas de entrada e eficiências iguais e constantes agora declaradas. Também foram conferidos o limite politrópico/isotérmico, o enchimento com entalpia de entrada constante, a coerência ppm/fração e os sinais/áreas na transferência térmica. As fontes e os limites de consulta estão individualizados no JSON; não se alegou leitura integral de todos os documentos externos.

## R1-A — excluir todo trabalho pertinente antes de reduzir calor a diferença de entalpia

Em escoamento permanente com variações cinética/potencial desprezíveis, o balanço é `Q̇ − Ẇnão-fluxo = ṁ(hsaída − hentrada)`. O trabalho de escoamento já está incluído em `h`; trabalho elétrico, por exemplo, não desaparece por não haver eixo. Essa distinção está na forma geral do [MIT, §2.5.2](https://web.mit.edu/16.unified/OldFiles/www/SPRING/thermodynamics/notes/node18.html) e na própria ficha 42.

**Contraprova autoral:** considere um vaporizador estacionário a pressão fixa, externamente adiabático, com a resistência elétrica dentro da fronteira, sem eixo e sem variações cinética/potencial relevantes. Entram líquido saturado e trabalho elétrico; sai vapor saturado. É possível ter `Q̇ = 0` e `Ẇel,in = ṁhfg > 0`. As condições publicadas na ficha 23 são satisfeitas, mas sua igualdade `Q̇ = ṁhfg` não vale. Não se trata de dado medido nem de escolher arbitrariamente termos incompatíveis com a física.

| Local | Pendência concreta |
|---|---|
| Ficha 23 e `#base-calor-latente` | A redução da taxa exclui somente trabalho de eixo. A parte fechada, limitada a trabalho pV, está correta. |
| Ficha 46 | “Sem calor ou trabalho de eixo” permite outra transferência de trabalho. A tabela do destino já diz “sem calor ou trabalho” e não precisa ser enfraquecida. |
| Ficha 79 e `#base-rankine` | Caldeira/condensador excluem somente eixo antes de usar as diferenças de entalpia como calor. |
| Ficha 84 e `#base-refrigeracao` | A ficha exclui somente eixo nos trocadores. A aula diz que evaporador/condensador “não produzem trabalho”, o que ainda permite receber trabalho. Isso não basta para suas igualdades de calor nem para a soma do ciclo. |

**Correção exigida:** delimitar a ausência de qualquer trabalho não associado ao escoamento nos componentes que usam `q = Δh` ou `hentrada ≈ hsaída`. Pode-se explicitar a fronteira e o modelo de componente passivo; deve ficar inequívoco que os trabalhos de entrada e de saída pertinentes estão excluídos, inclusive o elétrico. Preservar `pv` dentro da entalpia. Não substituir indiscriminadamente toda ocorrência de “eixo”: nas fichas 55 e 89 ela identifica a potência ou o trabalho mecânico estudado e não é a mesma redução contestada.

Sincronizar as condições e buscas das quatro fichas, os três alvos indicados e suas revisões individuais/representações derivadas. Não é necessário mudar os MathML, acrescentar fichas ou criar uma unidade sobre eletricidade.

Na documentação r2, usar a contagem correta: **100 fichas / 191 elementos MathML**. A expressão “100 MathML/expressões” em alguns relatos r1 foi imprecisa; o confronto técnico efetivo cobriu os 191 elementos. A [nota complementar do coordenador](../evidencias/apoio-coordenador/for01-contagem-mathml.json), fora do pacote congelado, registra a correção. Isso não é um segundo bloqueador nem invalida a preservação verificada.

## Reapresentação e decisão

Preservar o pacote r1 e entregar r2 com resposta a R1-A, delta integral e novos hashes. A evidência deve mostrar que o vaporizador da contraprova fica fora do modelo reduzido, ou é tratado pelo balanço geral com trabalho elétrico. Confirmar que as outras 96 fichas, os 191 MathML, os 197 artigos/registros, FUN-01/FUN-02 e a infraestrutura continuam preservados; atualizar apenas as referências globais do inventário necessárias à nova aula.

Não há outro ajuste obrigatório identificado nesta rodada. Os critérios já atendidos podem ser herdados por identidade na r2, com verificação do delta e dos testes pertinentes. Não é necessário repetir a auditoria das 100 fichas ou a infraestrutura intacta sem mudança que a justifique.

**FOR-01 r1 permanece rejeitado para passagem. Somente a reapresentação deste mesmo ID pode prosseguir após a liberação do coordenador.** Este parecer não certifica o curso inteiro como avançado, nem encerra FOR-02/FOR-03/FOR-05/FOR-06 ou QA-09. Não houve teste com alunos, impressão em papel/PDF ou auditoria completa de acessibilidade.
