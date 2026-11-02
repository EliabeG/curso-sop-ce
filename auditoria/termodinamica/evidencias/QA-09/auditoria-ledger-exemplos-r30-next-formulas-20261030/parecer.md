# QA-09 — auditoria independente do ledger de exemplos r30

30/10/2026. Auditor `/root/next_formulas`. **APROVADO NO RECORTE DE RASTREABILIDADE E RECONCILIAÇÃO**, não como nova aprovação científica independente de todos os 50 exemplos. O estado do ledger examinado continua registrando a pendência de auditoria porque antecede este parecer; nenhum ledger ou produto foi reescrito.

## Identidade, vínculos e reprodução

Conferi `LEIA-ME.md` SHA-256 `afeb1d5a2070acf019f66d5c6ecafda2181a8b0b283ddd5456e955fa52055cbf`; ledger `bdc36b0f7a303043453a433b246bd6abffddbb2bfd1e4afd9e49ab21baa6510a`; `ledger.mjs` `b983de6e4ec2edac9b48bb1b4dcc9537630e459a27f52ce1fbe1a39f2a6c1545`; reconciliação `6c24ffd6872a3d3dd61964854ca7dbfb63515699bf864565f43e122cae8e8d5c`; notas `ce32b2ca62d7267b4110681e0656741337bf14df09faea8ee5c1c6b0c721165b`; negativos `4b192d7c2fc4ff15064778cb5c948329f9536f629f9bf8fc85ee98f24a87c994` e saída `b989ad3a194f3c25760da57b61d3ffffdcf2902c9bd6f341a79b02d3fc744229`. A foto r30 é aula `c719adae3464fb56ed2b0ad7014e0721c0aab2da444fb484ec0b40c5c0c8fbd4`, formulário `949c44fc5b96703929770b2881383d449af890616d34b9ab10b998ca96c75749` e inventário `1ce69fc1ab71850abc3ab8dc3df82b04e78788b9e62a55919c609a708a7979b4`.

Vínculos: auditei EX041–050 r20 e inicialmente a candidata de EX046; depois foi apontada a necessidade de distinguir geração térmica de balanço de energia total, tratada na aplicação posterior. Elaborei candidata de EX027, auditei a ponte direta r30 e fiz a triagem das cinco equações que inclui EX028. Não reaprovo automaticamente a minha ciência histórica ou essas próprias alterações; este parecer avalia a trilha, a reconciliação e dependências localizadas. Outro agente fez leitura independente adicional das seis mudanças sem consulta externa.

Executei `node auditoria/termodinamica/evidencias/QA-09/ledger-exemplos-r30-r1/ledger.mjs --verificar auditoria/termodinamica/evidencias/QA-09/ledger-exemplos-r30-r1/ledger.json`: `ok:true`, 50 registros, 15 já na base e 35 acrescentados; a triagem executada pelo programa fixa insumos, fotos, pareceres e 13 mapas e reextrai contextos. Executei os oito negativos em cópias temporárias e os repeti capturando os erros: hash, posição, omissão, parecer, contexto, par, estado padrão e juízo foram rejeitados por `AssertionError`, código 1. Esses ensaios alteram o ledger de entrada para comparar com a estrutura reconstruída; não adulteram mapas completos nem provam semântica científica.

O [verificador adicional](verificar.py), SHA `018d53de9c9c7258cbfa6815278a06a19d2162dec0394a01f1c9a7ca01b57ebd`, reextrai os 50 fragmentos r30 e os 35 fragmentos históricos nas fotos de origem, recompõe cada cadeia nos mapas até r30, confere hashes dos pareceres referidos, as 50 linhas do relatório com as notas e a igualdade dos 15 juízos de base. Ele reproduz cinco mudanças de fragmento e seis de contexto. A comparação independente de hashes de parecer não significa concordância automática com seu mérito; a reextração dos contextos é feita pelo script da triagem original.

## Mudanças e pendências

- **EX010:** r26 explicita uma entrada/saída e trabalho total não de escoamento, mantendo 3000−2600=400 kJ/kg e 2×400=800 kW; a trilha inclui parecer de aplicação.
- **EX027:** r18 explicita calores totais e trabalho líquido como única outra interação; 1000−600=400 kJ e rendimento 0,4 no ciclo motor. O parecer da aplicação está identificado, não inferido apenas do hash.
- **EX028:** o fragmento efetivamente mudou r28→r29 em três legendas de W, que passaram a definir trabalho líquido total. O enunciado da candidata opcional para explicitar mais condições **não foi aplicado**. As afirmações não são contraditórias: uma modificação de legendas dentro do exemplo ocorreu; a proposta distinta de enunciado permaneceu de fora. A conta COPR=3 e COPBC=4 depende do contexto de ciclo simples, mesma fronteira e ausência de outras interações relevantes, não vale por mera igualdade de hashes.
- **EX044:** r22 explicitou superfície mais quente e taxa radiativa inicial não nula, domínio para razão 0,30/0,60=0,5 sob as demais condições fixas.
- **EX046:** r21 explicitou alimentação elétrica de 1200 W convertida na geração e proibiu dupla contagem; r22 esclareceu a energia convertida. O resultado Ts=30 °C depende dessas condições e da área exposta; geração térmica não cria energia total.
- **EX050:** fragmento permanece idêntico, mas o contexto mudou na r21: sistema, reservatórios e interfaces integram o conjunto, sem troca externa de entropia e com retorno das interfaces. O valor −1/3 kJ/K é atribuído ao conjunto nesse modelo, não à geração interna de um reservatório isolado. É contradição com segunda lei no cenário proposto.

Os 15 registros presentes no ledger anterior não são contados como 35 novos; 28 diagnósticos não integram a lista de 50. Os estados padrão de ocorrências, referências, recursos e ativos permanecem pendentes. Preservam-se a ressalva de EX028 e o registro de que a aplicação r29 ocorreu antes de ensaio por erro de diretório, sendo o ensaio posterior retrospectivo.

## Limites

A revalidação localizada do integrador e os pareceres existentes não equivalem a reexaminar independentemente todas as fontes, tabelas, bases, pais ou filhos, e a identidade dos fragmentos não certifica seu conteúdo científico. Não reabri fontes externas nesta auditoria; não houve navegador, leitor de tela, estudantes, revisão humana ou certificação externa. Não é aceite global de QA-09 nem aprovação de fotografia futura.
