# BAN-07 — revalidação independente localizada de AV42, AV45 e AV52

Data: 29/10/2026. Auditor: agente automatizado `/root/auditor_ban08_novo`, independente do Corretor `/root/inspect_repo`. **Veredito: APROVADO para o alcance reaberto de BAN-07 nos três artigos efetivamente aplicados**, nos arquivos e condições identificados abaixo. Os ajustes de suficiência foram atendidos; revalido a ciência, a unicidade e a coerência do inventário no alcance afetado. Os 194 demais artigos e os limites do parecer r3 são herdados pela identidade demonstrada, não por repetição integral de seus cálculos. **Não aprovo BAN-08, não libero outro ID e não altero produto, controle ou registros históricos.** A coordenação decide o estado do controle; a atualização dos registros numéricos finais e demais pendências de BAN-08 continuam necessárias.

## Critério e versão

BAN-07 requer dados suficientes antes da tentativa, consistência física, comando, unidades, restrições, resposta única e justificativa dos distratores, inclusive valores que poderiam se equivaler por arredondamento. Não implica aceitação empírica de dificuldade ou domínio. Examinei a [entrega de aplicação](../entregas/BAN-08-aplicacao-av42-av45-av52-r1.md), SHA-256 `a6de16359e7a07beeb19fa95f673e4ca1a807ae37660d85c0af07438897c1865`; manifesto `auditoria/termodinamica/evidencias/BAN-08/aplicacao-av42-av45-av52-r1/manifesto-aplicacao-r1.json`, SHA-256 `b0f359212d9a7f100a44edbe513f2a610e1a8294ef229b48b18ad5e62d227f26`; [BAN-07-r3](BAN-07-r3.md), SHA-256 `009adc698bf2f88e28826b389a48e2526660efc9b7cc2ea3b598f0e06026d68b`; e as adjudicações locais AV42/45 e AV52, respectivamente `40135fea3ac4c3dc0695b731a436eea2f16832ff34fb2f453665d29882ce524f` e `82e211ebb30e0e7e58460167429c47730137db9b8e332f1e1ac7d42aeae258fb`.

A entrega parcial registra validação pendente no instante em que foi escrita. As evidências complementares foram produzidas depois, sem reescrever aquele manifesto; não interpreto o seu campo histórico como estado atual. O [apoio técnico independente](BAN-08-aplicacao-av42-av45-av52-auditoria-tecnica-independente-r1.md), SHA-256 `520e99f4f91c8f785770fe20a4363aae47f4b62fadc77b0cbc832e8c02e93e2d`, é de `/root/auditoria_av61_70` e contém verificações e recálculos próprios; foram confrontados com esta análise, sem atribuir sua execução a mim.

| Arquivo examinado | SHA-256 atual |
|---|---|
| `modulos/e1-termodinamica.html` | `9ec10053e40640feeb977baea742da3cbe4d546659f772f0256c6b3cb0720a55` |
| `auditoria/termodinamica/inventario/inventario-questoes.json` | `5e83ef8b27e4596e9d8d154aa19df1e8f836863a4ff76acac0ba5ea66e9af72c` |
| `auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md` | `1eba9f02611dcb1b1a58690a876a0541d9fe5eb57714496415306f95d5564e29` |
| `assets/curso.js` | `a20f4d19158073a9a1c48aabdfba8fa863b02063e16061c00b16448a6ccc2e13` |
| `assets/registro.js` | `46da94527d6639fe0265bd766286f1ef39623966105e00bda3b31f21ca2c247c` |

## Delta e base de herança

Comparei diretamente o HTML anterior `80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0` e o atual: os 197 IDs permanecem, em mesma ordem, e **apenas AV42, AV45 e AV52** mudaram. Substituir em memória os três artigos novos pelos anteriores reconstitui integralmente o HTML anterior, incluindo os outros 194 artigos, bases e texto fora dos artigos; nada foi gravado. As versões atuais dos três coincidem com as candidatas isoladas previamente revisadas e com as entradas do manifesto:

| ID | SHA-256 do artigo atual | Chave |
|---|---|---|
| AV42 | `81c755c3fbc510b3d5c1ff5678e5c14c548239a2563346a33b28bdedd650491e` | E |
| AV45 | `4999bebef5d3de5516753ad3390a1728be9b3ace5bf28d23037acb2783c661ba` | E |
| AV52 | `f920b246bea3d4b5e3d4b63cbfb5a4dd24ae11cff17877aeec73decf278cfc97` | D |

Reconfirmei que os demais registros individuais do inventário JSON permanecem iguais ao backup r3 e que os arquivos de código coincidem com os hashes r3. Dos 14 arquivos de preservação/evidência/parecer listados no manifesto r3, só HTML e resumo Markdown diferem, como esperado para a aplicação; os outros 12 coincidem. A validação atual confere 29 recursos do inventário. Isso sustenta herança localizada dos 194 artigos e dependências verificadas, com autoria e limitações de BAN-07-r3; não é uma nova inspeção de todos os arquivos externos, desempenho estudantil ou fontes históricas.

## Exame científico, comando e alternativas

**AV42 — E.** Antes da escolha, o comando agora fixa máquina cíclica, calor apenas com fonte quente e fria, 4.000 kJ da fonte quente e 1.000 kJ de trabalho líquido **no mesmo ciclo**, e trabalho como única outra transferência líquida. No modelo de motor de duas fontes das bases vinculadas, QL=4000−1000=3000 kJ/ciclo e η=1000/4000=25%. A=1000/3000=33,333…%→33,3%, erro de 0,0333 ponto percentual; B=100% e C=400% não são a razão correta; D=3000/4000=75% é fração rejeitada; E=25% é única. O contramodelo de entrada adicional e a ambiguidade temporal das adjudicações ficam excluídos no modelo comunicado. A expressão “única outra transferência líquida” é compreensível no contexto das duas trocas de calor e trabalho; explicitar “além dessas trocas de calor” poderia ser melhoria editorial, mas não é pendência científica obrigatória aqui.

**AV45 — E.** O comando agora fixa máquina cíclica, duas fontes a 600 e 300 K, entrada quente 1.000 kJ por ciclo e trabalho como única outra transferência líquida. Para fontes constantes e limite reversível ensinado na base, ηC=1−300/600=50%, Wmáx=500 e QL,mín=500 kJ/ciclo. A=333,3 kJ aproxima 1000×300/(600+300)=333,333…; a eficiência associada seria aproximadamente 66,7%, superior a 50%; erro de exibição <0,05 kJ e <0,05 ponto percentual. B=1000 pode corresponder a trabalho zero, mas não é mínimo; C=300 implicaria 70%; D=0 implicaria 100%; E=500 é única mínima. Uma máquina irreversível entre as mesmas fontes rejeita mais. O modelo exclui a fonte extra usada no contramodelo anterior, sem reescrever texto de banca: este item é autoral.

**AV52 — D.** O comando fixa potência térmica **total** de 200 kW, turbina 100 kW, compressor 40→50 kW e outros consumos desprezíveis; define potência líquida como turbina menos compressor antes da resposta. Líquidas 60→50 kW e eficiências 60/200=30%→50/200=25%. A inverte tendência; B=20%→25% usa consumo do compressor; C=70%→75% soma as potências; E=50%→50% ignora compressor; D é única. A resolução agora identifica potência líquida em kW e repete a hipótese relevante; a expressão ocasional “trabalho líquido” no comentário A não altera a conta nem atribui kW a energia. O auxiliar do contramodelo é excluído. Os números de AV52 são nominais e exatos na aritmética fornecida; os arredondamentos acima são de exibição, não incerteza de instrumento.

## Inventário, digitais e testes

Comparei recursivamente os inventários: alteraram-se apenas os três registros e os campos globais `fonte` e `metodo`. Os hashes e hipóteses atualizados correspondem aos artigos; em AV52 raciocínio e vínculo de competência passam de trabalho para potência. AV45 remove vínculo de gabarito relativo ao artigo anterior. As três revisões estão como `pendente`, corretamente sem reutilizar automaticamente a evidência velha para a nova versão; a decisão científica deste parecer é separada do registro e da decisão global BAN-08. O Markdown só adiciona nota sobre o ajuste e a revisão pendente; não reescreve o histórico.

Executei pessoalmente, em leitura, o validador canônico: **197 registros, 197 artigos, 29 recursos, 1.260 links locais, zero erros e avisos**. O parecer técnico atribui a mudança de 1.261 para 1.260 à remoção do campo de evidência antiga de AV45 e relata teste em memória de sua restauração; minha comparação confirma a remoção do campo, mas não reproduzi esse teste contrafactual. Não se restaura o link histórico como se validasse o artigo novo.

Após inspecionar que os scripts não gravam evidências, reexecutei `verificar-versao.mjs` e `testar-persistencia.mjs` do Corretor em execução própria. O primeiro confirmou snapshot idêntico, 197 artigos, 80 AV, três mudanças, chaves preservadas e nenhuma colisão de digitais entre os 80 AV atuais. As digitais mudam AV42 `d0b32333→595a0614`, AV45 `95231db6→10df36ad`, AV52 `d95e6b2d→0619ab1f`. O segundo usa funções reais em VM com DOM/localStorage simulados: preserva histórico antigo, separa respostas novas e placar, mostra aviso, permite releitura/refazer sem apagar o registro anterior e não sobrescreve o armazenamento simulado nas falhas de leitura/escrita ensaiadas. Conferi os seis hashes do relatório complementar do Corretor; coincidem. São testes controlados com adaptadores, não navegador real nem todos os históricos pessoais, e não demonstram aprendizagem, acessibilidade ou desempenho em alunos.

## Quadro de decisão

| Critério | Julgamento no alcance reaberto |
|---|---|
| Hipóteses decisivas antes da resposta | Atendidas nos três artigos e compatíveis com as bases. |
| Ciência, unidades e resultado | Atendidos nas demonstrações acima; os modelos e limites foram declarados. |
| Gabarito, alternativas e arredondamento | Cinco opções por artigo confrontadas, E/E/D únicas no modelo; nenhuma equivalência indevida. |
| Inventário, delta e herança r3 | Três registros e fonte/método atualizados; outros 194 e HTML externo preservados, recursos conferidos; herança com limites explicitados. |
| Digitais e persistência | Testes controlados reproduzidos no alcance declarado; sem prova de navegador real ou de todos os dados pessoais. |
| BAN-08 e próximos IDs | Fora deste aceite; requerem registro integral e decisão própria. Não há liberação da fila. |

**Decisão explícita:** alcance de BAN-07 reaberto pelas alterações de AV42, AV45 e AV52 **revalidado e aprovado** para os hashes indicados, sem pendência obrigatória nesses três itens no critério BAN-07. BAN-07-r3 permanece a evidência histórica da versão anterior e sustenta por identidade os demais artigos no alcance acima; este parecer complementa, não reescreve, aquele registro. A decisão não aprova BAN-08, não transforma metadados pendentes em registros numéricos finais e não representa revisão humana ou certificação externa.
