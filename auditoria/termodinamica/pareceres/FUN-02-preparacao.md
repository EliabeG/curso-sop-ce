# FUN-02 — preparação independente

Data: 27/10/2026. Revisor: agente automatizado `/root/auditor_aaa`. Apoio matemático independente: `/root/auditor_aaa/auditoria_tecnica_ban02`. Nenhum conteúdo da unidade foi editado por estes revisores. Não há parecer de implementação antes da entrega congelada.

## Escopo

FUN-02 exige diferenciais exatas/inexatas, integrais de processo/ciclo, derivadas parciais e condições mantidas. O aluno deve explicar a dependência de calor/trabalho em relação ao caminho e construir dois processos entre os mesmos estados com transferências distintas e balanços corretos. Aplicam-se os requisitos comuns da seção 3.2: objetivo, pré-requisitos, teoria/hipóteses, exemplo com decisões, prática independente inédita, solução/rubrica, fontes/versionamento, revisão científica/numérica e matriz C01–C10.

Não se antecipa o aceite de FUN-03/04, PROP ou ENT. As hipóteses mínimas de uso das relações precisam, entretanto, estar corretas nos próprios casos de FUN-02.

## Pontos que serão examinados

1. **Derivadas e condições mantidas:** identificar variáveis independentes, variável mantida e domínio; distinguir derivada parcial, diferencial total e derivada ao longo de um caminho. Relações especiais de gás ideal ou de calor específico constante não podem ser universalizadas. A preparação deve sustentar a matemática realmente cobrada.
2. **Exatidão:** no teste clássico para `M dx + N dy`, explicitar a regularidade pertinente e o domínio. Igualdade de derivadas cruzadas apenas num ponto ou num caminho não prova exatidão. Com coeficientes C¹ em domínio aberto simplesmente conexo, o teste fornece garantia global; em vizinhanças adequadas pode fornecer garantia local. Simples conexão é suficiente, não necessária para uma forma particular que possua potencial explícito. Um único ciclo de integral nula tampouco prova independência global.
3. **Significado termodinâmico:** `dU` é diferencial de propriedade; calor e trabalho são transferências associadas ao processo. A comparação geral de caminhos não proíbe coincidências particulares — por exemplo, o balanço restringe o trabalho adiabático entre estados dados. Restringir uma expressão a uma trajetória não transforma calor ou trabalho numa propriedade do sistema.
4. **Sinais e modelo:** o E1 já usa calor recebido positivo e trabalho realizado pelo sistema positivo, `ΔU=Q−W` quando as demais variações energéticas são desprezíveis. A unidade deve manter essa convenção ou traduzir expressamente qualquer referência oposta. O uso da pressão do sistema em `∫p dV` exige as hipóteses de fronteira/processo correspondentes; não vale para qualquer expansão irreversível.
5. **Caminhos e ciclos:** conferir que os dois processos têm de fato os mesmos estados extremos, mesma quantidade/composição e modelos compatíveis. Calcular propriedades, trabalho e calor por trechos; a diferença das transferências não pode mudar arbitrariamente `ΔU`. Conferir orientação, unidades e fechamento do ciclo. Distinguir integral formal no espaço de estados de processo físico admissível; não presumir que um processo irreversível possa ser simplesmente invertido.
6. **Prática e rubrica:** o comando deve exigir construção ou decisão independente, além de repetir uma comparação já resolvida com números trocados. A solução precisa justificar os caminhos e interpretar o balanço. A rubrica deve distinguir erro de modelo/sinal de erro aritmético, e avaliar as variáveis mantidas e o domínio quando pertinentes.
7. **Rastreabilidade e preservação:** verificar fontes reais versus parâmetros didáticos, executar cálculos próprios antes de depender das soluções, comparar metadados dos novos itens e manter o inventário. Conferir versões/hashes e preservação dos critérios anteriores; testes mecânicos são evidências complementares, não aceite científico.

## Fontes primárias e cautelas de leitura

- [MIT 16.Unified, §2.1](https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node15.html): primeira lei com a mesma convenção de sinais do E1.
- [MIT 16.Unified, §2.2](https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node16.html): balanço de ciclo e restrição adiabática. A interpretação auditada deve distinguir essa restrição particular da dependência geral de caminho.
- [MIT 16.Unified, §1.3.3](https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node12.html): pressão externa versus pressão do sistema, condições para sua aproximação e comparação de caminhos.
- [MIT 3.020, Spring 2021, aula 3](https://ocw.mit.edu/courses/3-020-thermodynamics-of-materials-spring-2021/mit3_020s21_l03.pdf): variáveis de processo e diferenciais. **Usa trabalho realizado sobre o sistema como positivo**, diferentemente do E1; a fonte não pode ser transposta sem conversão de sinais.
- [MIT 18.02SC, Fall 2010, V5, páginas 1–3](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/1bc33736db05b99f564ba15fe7174311_MIT18_02SC_MNotes_v5.pdf): potencial, independência de caminho, ciclos e condições de domínio.
- [UCI, teorema 2.27 e nota](https://webapps.math.uci.edu/~ndonalds/math162a/forms.html): apoio do subauditor para exatidão local. A distinção será verificada na matemática efetivamente publicada.

O apoio sugeriu testes de auditoria para evitar falsos critérios: forma angular no plano sem a origem (fechada, circulação não nula), uma forma inexata com um ciclo particular nulo, e um gradiente global no mesmo plano perfurado. São instrumentos de checagem do revisor, não imposição de que a aula inclua esses exemplos específicos nem uma unidade de topologia.

## Estado e dependências

Controle consultado: FUN-02, rodada 1, liberado ao Corretor. Não foi identificado impedimento novo dos P0 legados para uma unidade própria. Os itens CR09/CR24/CR68/CR79 permanecem fora da comprovação; qualquer reutilização afetada exige tratar antes o bloqueio correspondente. O próximo passo do Auditor é aguardar a entrega congelada e emitir parecer sobre a versão concreta, sem conceder aprovação prévia ou iniciar outro ID.
