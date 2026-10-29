# BAN-08 — auditoria independente da aplicação AV42, AV45 e AV52

Data 29/10/2026. Auditor: agente automatizado `/root/auditoria_av61_70`. **Conclusão localizada: aplicação compatível com as três candidatas e sem falha identificada nas verificações descritas.** Este parecer não aprova BAN-08 globalmente, não aprova indiscriminadamente BAN-07 para outras alterações e não libera próximo ID. Não modifiquei produto, controle ou evidências anteriores.

## Integridade e delta

Conferi a entrega `auditoria/termodinamica/entregas/BAN-08-aplicacao-av42-av45-av52-r1.md`, SHA-256 `a6de16359e7a07beeb19fa95f673e4ca1a807ae37660d85c0af07438897c1865`, e o manifesto `auditoria/termodinamica/evidencias/BAN-08/aplicacao-av42-av45-av52-r1/manifesto-aplicacao-r1.json`, SHA-256 `b0f359212d9a7f100a44edbe513f2a610e1a8294ef229b48b18ad5e62d227f26`. O manifesto congela o estado de entrega parcial com validação e persistência pendentes; os testes complementares vieram depois em arquivos separados, sem reescrevê-lo.

| Produto | SHA-256 antes | SHA-256 aplicado |
| --- | --- | --- |
| `modulos/e1-termodinamica.html` | `80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0` | `9ec10053e40640feeb977baea742da3cbe4d546659f772f0256c6b3cb0720a55` |
| `auditoria/termodinamica/inventario/inventario-questoes.json` | `486c53c5aa6c432831599c4eca170e4620d089b4eb15b480dbfb2cbfaf54c9ce` | `5e83ef8b27e4596e9d8d154aa19df1e8f836863a4ff76acac0ba5ea66e9af72c` |
| `auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md` | `35df191e2f7964adfb7b975668491e8ba39d983a5df93640a35d3d96ae142df8` | `1eba9f02611dcb1b1a58690a876a0541d9fe5eb57714496415306f95d5564e29` |

Os três produtos correspondem aos respectivos backups e cópias preparadas; o snapshot BAN-08 coincide com o HTML aplicado. Extração e comparação próprias dos trechos brutos mostram 197 artigos, IDs na mesma ordem e somente AV42/45/52 alterados. Cada um dos três é byte a byte igual à candidata isolada revisada. Substituí em memória os três trechos novos pelos antigos e recuperei o HTML anterior integralmente: os demais 194 artigos e todo o HTML exterior aos três foram preservados. Isso não é uma comparação integral de todos os arquivos do projeto: comparei ainda os backups de `assets/curso.js` e `assets/registro.js`, ambos idênticos aos arquivos correntes.

## Revalidação localizada de conteúdo

Esta revisão parte das candidatas efetivamente aplicadas; parecer próprio anterior `BAN-08-candidatas-av42-av45-av52-revisao-independente-r1.md` SHA-256 `bbc9741641fa852b2c3535da99795edafdfe001bd63153b0e65aec6c439bd3b4` documenta exame independente dos enunciados, cinco alternativas e comentários. As condições e resultados foram novamente conferidos:

- AV42, chave E: único aporte quente declarado de 4000 kJ por ciclo e trabalho líquido de 1000 kJ, trocas limitadas às duas fontes e trabalho; `η=25%`, rejeição 3000 kJ. A opção 33,3% é razão sobre rejeição arredondada, 400% é razão inversa e 75% é fração rejeitada.
- AV45, chave E: ciclo entre duas fontes a 600 K e 300 K, entrada 1000 kJ/ciclo; `η_C=50%` e rejeição mínima reversível `500 kJ/ciclo`. Valores 333,3, 300 e 0 kJ excederiam Carnot; 1000 kJ pode corresponder a trabalho zero, mas não ao mínimo.
- AV52, chave D: entrada térmica total 200 kW, turbina 100 kW, outros consumos desprezíveis; compressor 40→50 kW dá potência líquida 60→50 kW e eficiência 30%→25%. Os outros pares não reproduzem esse balanço. A resolução usa corretamente potência e não trabalho em kW.

Isso é revalidação científica BAN-07 localizada nos três artigos modificados e não uma substituição da auditoria dos 194 artigos inalterados. O aceite BAN-07 r3 refere-se ao HTML anterior; não é automaticamente transferido ao arquivo integral novo. A frase sobre a “única outra transferência líquida” em AV42/45 admite a sugestão editorial de explicitar “além dessas trocas de calor”; neste contexto das duas fontes não a trato como bloqueio científico, conforme parecer das candidatas.

## Inventário e validação

O diff próprio do JSON encontra mudanças nos três registros e nos campos globais de fonte/método, sem mudanças dos outros registros. Os hashes apontam aos artigos atuais e o snapshot atual; as hipóteses novas são registradas, a fonte atualizada, e os três gabaritos constam `pendente` para a versão efetiva. AV52 ajusta descrição de raciocínio/competência de trabalho para potência; AV45 remove evidência anterior de verificação, corretamente sem usar aceite antigo como verificação da versão nova. O resumo Markdown só acrescenta a nota localizada sobre as mudanças e pendências. Examinar os metadados e manter `pendente` não é aceitar gabarito global ou validar aprendizagem.

Reexecutei o validador canônico após inspecionar que imprime resultado sem regravar evidências: 197 registros/artigos, 29 recursos, 1260 links locais, zero erros e avisos; alcance estrutural/documental. Coincide com a evidência do Corretor `validacao-inventario-r1.json`, SHA-256 `c4dc681129269100f30415b4f536c466a6337b76ea96aac4883897b339b8ee40`. A integridade das fontes históricas BAN-07 é referida pelo vínculo de versão anterior, não uma reauditoria de todo o arquivo histórico.

**Diferença de 1261 para 1260 links em relação à r3:** o diff mostra a retirada de um único campo de caminho validado, `revisao.evidencia_gabarito` de AV45, que apontava a `auditoria/termodinamica/evidencias/BAN-07/diagnostico-pos-correcao-197-r1.json`; o estado passou de `verificado` para `pendente`, pois o artigo mudou. Os outros vínculos dos 197 registros e o HTML exterior aos três artigos são preservados, e as candidatas não mudaram os links dos artigos. Para isolar a contagem, executei `validateInventory` com o inventário atual e uma cópia somente em memória que restaura esse campo e o estado anterior: os resultados foram respectivamente 1260 e 1261, ambos estruturalmente válidos. Essa restauração hipotética não foi gravada e **não valida** o artigo novo pela evidência antiga. A redução de um link decorre dessa remoção deliberada de vínculo de gabarito da versão anterior, não de perda inadvertida de link do conteúdo; a versão atual permanece corretamente pendente de decisão.

## Digitais e persistência

Reexecutei os dois testes complementares do Corretor, após leitura do código e confirmação de que não escrevem arquivos de evidência. `verificar-versao.mjs`, SHA-256 `a60fa67a0a7fea4bf3944e6662d9e57afac04f3ee01905fb9857f2115db30ab2`, usa em memória as funções reais de digital com adaptador do parser: 197 artigos, 80 AV, chaves/IDs preservados e nenhuma colisão no banco AV atual. Sua evidência `versao-verificada.json` SHA-256 `bb4759ca49bc2e1b03070f7c40fb94f848e7ef58896e23aca110a1e9bd577392`. Digitais e chaves:

| Item | Chave | Digital anterior → atual |
| --- | --- | --- |
| AV42 | E | `d0b32333` → `595a0614` |
| AV45 | E | `95231db6` → `10df36ad` |
| AV52 | D | `d95e6b2d` → `0619ab1f` |

`testar-persistencia.mjs`, SHA-256 `2b8f10564ce71a7dbfdad1b4ee063caa026e0b0cc2a08db008723c43c30f1eaf`, executa funções reais de armazenamento e placar com DOM e localStorage simulados, usando as digitais acima e um quarto item. Confirmou aviso de versão anterior, histórico preservado sem migração automática, placar apenas das respostas novas, gravação/releitura, refazer sem apagar a digital antiga e falhas de leitura/escrita sem sobrescrita. Evidência `persistencia-r1.json` SHA-256 `0c57a2856a3e835d0b137b6a24b3d1f8e61f8153a16c4a08ad9b712c86ece6db`. O teste é atribuído ao Corretor e reexecutado aqui; não é navegador real, não inclui o DOM integral nem dados pessoais reais. A comparação com digitais históricas conhecidas foi feita no ensaio das candidatas, cujo conteúdo e digitais coincidem com a aplicação, mas não cobre todas as versões eventualmente armazenadas por usuários.

## Limites

O relatório complementar do Corretor `relatorio-validacao-r1.json`, SHA-256 `71f4040af42db93e1ccd4f256e69d74333864ea12cf9bef064971dba3cfb8995`, foi conferido com os seis arquivos listados; todos os hashes coincidem. Ele atribui ao Corretor o recálculo por ID da versão efetiva `recalculo-av42-av45-av52-r1.json`, SHA-256 `2cec1fffb163edafdbeef6fb69ed06180239c56df58a9770593be546a3f49f79`; a revalidação independente consta neste parecer, sem modificar o registro do Corretor.

Não testei com estudantes, não alego validação empírica de aprendizagem, navegadores reais ou certificação externa. A análise cobre a versão com hashes acima; qualquer alteração posterior exige novo confronto. Os recálculos da versão efetiva dos três itens estão identificados separadamente dos registros da versão anterior; o fechamento global BAN-08 exige reconciliar o conjunto dos registros com suas identidades. O Auditor principal decide aceite localizado e estado dos controles.
