# QA-09 — reconciliação dos 50 exemplos na fotografia r30

30/10/2026. Integrador `/root/planning`. **A revalidação individual pelo integrador aguarda Auditor independente.** A base é `ledger-fichas-r30-r1/ledger.json` SHA `08829096cacc3e90842fca2be7c80f89bbdc12311844880e0d828ee81cb5e9d2`, com parecer independente de reconciliação `auditoria-ledger-fichas-r30/parecer.md` SHA `90a518be77f31b09f05665efcbfeed8c4aec37ac5410971fbf7b14ea0545be59`. A referência preserva os 78 objetos da ponte anterior e as 100 fichas. Dentre os 50 exemplos, EX001–005 e EX031–040 já estavam na base; os 35 restantes são acrescentados sem contar duas vezes os 15 anteriores. Outros registros e coleções continuam com estado padrão pendente; QA-09 permanece aberto.

Aula r30 `c719adae3464fb56ed2b0ad7014e0721c0aab2da444fb484ec0b40c5c0c8fbd4`, formulário `949c44fc5b96703929770b2881383d449af890616d34b9ab10b998ca96c75749` e inventário `1ce69fc1ab71850abc3ab8dc3df82b04e78788b9e62a55919c609a708a7979b4`. A [reconciliação por exemplo](reconciliacao.md), SHA `6c24ffd6872a3d3dd61964854ca7dbfb63515699bf864565f43e122cae8e8d5c`, registra resultado, hipóteses e efeito de alterações para cada um; `notas.json` SHA `ce32b2ca62d7267b4110681e0656741337bf14df09faea8ee5c1c6b0c721165b` contém os juízos atribuídos. O estado de cada registro é provisório até parecer independente da integração.

Cinco fragmentos mudaram desde suas revisões de origem: EX010 (r26), EX027 (r18), EX028 (legendas r29), EX044 (r22) e EX046 (r21). Seis contextos mudaram, incluindo o de EX050 (r21). Cada alteração tem parecer de aplicação ou parecer de equações/contexto vinculado no ledger e julgamento local no relatório. Para EX028, a candidata opcional que explicitaria os totais no enunciado **não foi aplicada**; as legendas foram efetivamente alteradas para trabalho líquido total e o cálculo permanece condicionado ao modelo do ciclo simples que consta do bloco. O verificador confronta literalmente ambas as redações para não confundir os fatos.

## Reprodução somente leitura

`node auditoria/termodinamica/evidencias/QA-09/ledger-exemplos-r30-r1/ledger.mjs --verificar auditoria/termodinamica/evidencias/QA-09/ledger-exemplos-r30-r1/ledger.json`

O programa fixa a base, fotos, inventários, 13 mapas e os lotes/pareceres pelo manifesto de insumos; reexecuta a triagem com composição de identidade de cada um dos 35 exemplos e comparação dos recortes e contextos, confere os 15 objetos anteriores e refaz seleção de contas. Reusa os snapshots existentes e não copia páginas ou inventários. Identidade e aritmética não substituem interpretação física. A foto ativa é fixada: depois de qualquer mudança, usar árvore isolada com snapshots ou reconciliar de novo, não suprimir guardas.

Oito mutações em cópias do ledger foram rejeitadas: hash de fragmento, posição, omissão, parecer, contexto, par de mapa, estado padrão e juízo. Isso verifica comparação com a estrutura reconstruída, não adulteração de um mapa inteiro nem correção científica. `negativos.py` SHA `4b192d7c2fc4ff15064778cb5c948329f9536f629f9bf8fc85ee98f24a87c994`; saída SHA `b989ad3a194f3c25760da57b61d3ffffdcf2902c9bd6f341a79b02d3fc744229`.

- `ledger.mjs` SHA `b983de6e4ec2edac9b48bb1b4dcc9537630e459a27f52ce1fbe1a39f2a6c1545`.
- `ledger.json` SHA `bdc36b0f7a303043453a433b246bd6abffddbb2bfd1e4afd9e49ab21baa6510a`.

Meu vínculo anterior como autor dos pareceres de EX006–020 e EX021–030, da aplicação de EX010/EX046 e da ponte de 15 exemplos é declarado: a presente consolidação precisa de Auditor distinto. O parecer das cinco equações do ciclo simples tem vínculo declarado com o executor r30 e não aprova toda a base. O incidente r29 — execução real antes de ensaio por erro de diretório, seguida de ensaio retrospectivo — permanece documentado. Não houve navegador, leitor de tela, estudantes, revisão humana, certificação externa ou alteração de produto nesta integração.
