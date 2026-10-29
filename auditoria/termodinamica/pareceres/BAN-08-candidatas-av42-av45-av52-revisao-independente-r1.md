# BAN-08 — revisão independente de candidatas AV42, AV45 e AV52

Data 29/10/2026. Revisor: agente automatizado `/root/auditoria_av61_70`. **Conclusão localizada: as três candidatas são cientificamente adequadas no recorte examinado**, sujeitas à decisão do Auditor principal e à verificação da versão integrada. São propostas isoladas, não aplicadas; este parecer não aprova produto futuro ou BAN-08, não libera próximo ID e não altera produto nem controle.

Confrontei cada candidato com o artigo corrente, enunciado anterior, adjudicação, resolução e cinco opções. A leitura não foi cega: eu mesmo levantei as ressalvas preliminares de AV42/45 e conhecia as chaves; a adjudicação é de `/root/auditor_ban08_novo`, a produção das candidatas é de `/root/inspect_repo`. Não trato meu parecer anterior, a identidade, o validador ou o manifesto como substituto desta revisão.

## AV42 — adequada localmente

O enunciado passa a declarar máquina cíclica que troca calor apenas com uma fonte quente e uma fria, 4000 kJ recebidos por ciclo, trabalho líquido de 1000 kJ e trabalho como outra forma de transferência líquida de energia. O modelo fecha a questão de totalidade das trocas e base temporal apontada na adjudicação. Para clareza editorial futura, a frase “a única outra transferência líquida de energia é o trabalho” pode ser redigida “além dessas trocas de calor, a única transferência líquida de energia é o trabalho”; a leitura no contexto das duas fontes basta para esta revisão localizada e a sugestão não altera a candidata examinada.

`Q_H=4000 kJ/ciclo`, `W=1000 kJ/ciclo`, `Q_L=3000 kJ/ciclo`, `η=1000/4000=25%`. A `33,3%≈1000/3000×100` usa rejeição como denominador; B 100% ignora a fração correta; C `4000/1000×100=400%` inverte a razão; D `3000/4000=75%` é fração rejeitada; E 25% é única correta. O arredondamento `33,333…→33,3%` erra menos que 0,05 ponto percentual. Chave E, alternativas e resoluções preservadas.

## AV45 — adequada localmente

O comando delimita ciclo com apenas fonte quente a 600 K e fria a 300 K, com 1000 kJ por ciclo da fonte quente e trabalho como outra forma de transferência líquida. As fontes são reservatórios de temperatura constante no modelo ensinado; o mínimo é limite reversível, não resultado garantido de máquina real. A mesma sugestão de clareza de AV42 se aplica à referência “outra transferência”, sem afetar a conclusão localizada.

`η_C=1−300/600=50%`; `W_máx=500 kJ/ciclo`; `Q_L,mín=500 kJ/ciclo`. A `1000×300/(600+300)=333,333…→333,3 kJ` implica aproximadamente 66,7% e viola o limite; B 1000 kJ pode acompanhar trabalho nulo, mas não é mínimo; C 300 kJ implicaria 70%; D zero implicaria 100%; E 500 kJ é única mínima. Aproximações 333,3 kJ e 66,7% respeitam meia unidade da última casa. Chave E, alternativas e resoluções preservadas.

## AV52 — adequada localmente

O comando passa a tratar 200 kW como potência térmica total, fixa a potência útil como turbina menos compressor e manda desprezar outros consumos; mantém demais valores. Isso exclui o consumo auxiliar do contramodelo adjudicado. Antes, `Ẇ=100−40=60 kW`, `η=60/200=30%`; depois, `Ẇ=100−50=50 kW`, `η=50/200=25%`. A 30→35% inverte a tendência final; B 20→25% calcula `40/200` e `50/200`; C 70→75% soma as potências de turbina e compressor; D 30→25% é única correta; E 50→50% usa apenas `100/200`. As operações são exatas para os valores nominais; não se infere incerteza de instrumento. O texto de resolução e a repetição no comentário D passam de “trabalho líquido” para “potência líquida” e explicitam outros consumos desprezíveis, compatível com as unidades kW. Chave D e cinco alternativas preservadas.

## Identidade, verificação e impactos

HTML corrente `modulos/e1-termodinamica.html` SHA-256 `80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0`. Pacote de `/root/inspect_repo`: `auditoria/termodinamica/evidencias/BAN-08/propostas-av42-av45-r1/manifesto-candidatas-r1.json` SHA-256 `723882a0286bb20c3280d0ea03991075d18c808e226d87c8d43f029b68db309e`; conferi os nove arquivos por hash contra o manifesto. Hash de artigo original é trecho bruto `<article>...</article>` UTF-8; hash de candidata é o arquivo HTML integral, aqui igual ao trecho candidato.

| Item | SHA-256 original | SHA-256 candidata HTML | SHA-256 JSON de proposta | Digital anterior → candidata |
| --- | --- | --- | --- | --- |
| AV42 | `83c8604cddfbc4d5f0d6782bd8605ff8eb9d462661716b4d69fc2abbdfbb89a9` | `81c755c3fbc510b3d5c1ff5678e5c14c548239a2563346a33b28bdedd650491e` | `cb8d8190b13a2bd7897478e042bd5920904d74e878603262fa41251c6e020f7f` | `d0b32333` → `595a0614` |
| AV45 | `3babe8cb08138fd4ad42f7358c5208b70974370d17a62d30490075e7b5019b50` | `4999bebef5d3de5516753ad3390a1728be9b3ace5bf28d23037acb2783c661ba` | `9ab927d3f64579061159a70a8174b6095a198617876eec0d80ed497930361f14` | `95231db6` → `10df36ad` |
| AV52 | `857e03ade94e02060d1f4db104c7e7f11de8396182589d3d1bc64be59351c7a8` | `f920b246bea3d4b5e3d4b63cbfb5a4dd24ae11cff17877aeec73decf278cfc97` | `82307222806853f9c0fadfc8629d5fc9970acf065a1881907e8f237eaa318272` | `d95e6b2d` → `0619ab1f` |

O diff próprio mostrou apenas mudança de enunciado em AV42/45 e, em AV52, enunciado e duas ocorrências idênticas do comentário da chave. Reexecutei os verificadores do Corretor após inspeção de que escrevem apenas em stdout: reversão reconstruiu artigos anteriores, e ensaio em memória com funções de `assets/curso.js` encontrou os 197 artigos e 80 AV, com IDs/chaves preservados, somente esses três artigos alterados, digitais novas e ausência de colisões entre AV atuais e com digitais históricas BAN-07 disponíveis. Isso é atribuído à execução dos verificadores do Corretor, não a um teste independente em navegador. `assets/curso.js` SHA-256 `a20f4d19158073a9a1c48aabdfba8fa863b02063e16061c00b16448a6ccc2e13`.

O código calcula a digital do enunciado, opções e chave e lê respostas pela digital. Se essas propostas forem aplicadas, as respostas anteriores têm outra identidade e não contam para os três artigos novos; a leitura estática indica preservação do registro antigo, mas não comprova persistência de navegador. A ausência de colisões no banco e histórico disponível não cobre todas as versões salvas por usuários. Integração exige verificar digitais/armazenamento em cópia, inventário e resumo, registros numéricos e revalidação BAN-07 localizada na versão efetiva, sem regravar evidências históricas. Não houve teste de estudantes, navegador ou certificação externa.

Fontes de decisão: `auditoria/termodinamica/pareceres/BAN-08-adjudicacao-av42-av45-r1-independente.md` SHA-256 `40135fea3ac4c3dc0695b731a436eea2f16832ff34fb2f453665d29882ce524f`; `auditoria/termodinamica/pareceres/BAN-08-adjudicacao-av52-r1-independente.md` SHA-256 `82e211ebb30e0e7e58460167429c47730137db9b8e332f1e1ac7d42aeae258fb`. Modelo de primeira e segunda leis é o das bases `#base-eficiencia-cop`, `#base-carnot-prova`, `#base-limite-carnot`, `#base-brayton-real` do HTML corrente.
