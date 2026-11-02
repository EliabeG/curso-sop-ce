# QA-09 — triagem de fórmulas e seleção de equações contextualizadas r30

30/10/2026. Corretor `/root/next_formulas`. **Aguardando Auditor distinto.** A triagem mede relação estrutural com o ledger direto r30, não revisa integralmente todos os pareceres históricos nem converte contenção em aprovação científica. Não modifica produto ou controle. Alguns conteúdos selecionados já tiveram análise em fotos anteriores; o novo lote individualiza cinco ocorrências de equação na foto r30 e seus exemplos, não alega ineditismo histórico.

## Foto e método

Aula preservada `aplicacao-precisao-r30/resultado/depois-aula.html`, SHA-256 `c719adae3464fb56ed2b0ad7014e0721c0aab2da444fb484ec0b40c5c0c8fbd4`; inventário r30 SHA `1ce69fc1ab71850abc3ab8dc3df82b04e78788b9e62a55919c609a708a7979b4`; ledger direto r30 r2 SHA `58d31ac8b26366c543cc439b3b4dc0c7c9428d191949c8ac49d801b4a459dc12`, cuja ponte foi aprovada no recorte de rastreabilidade em parecer SHA `e0e46c5ad44ff523cdcd50ab14c156db48fb0cf756297673fa4192f1d7d5d2ee`. O ledger tem 78 objetos e 43 IDs distintos de contexto; seu estado incorporado ainda registra auditoria pendente por refletir a foto anterior ao parecer. Não o reescrevo.

`triagem.mjs` SHA `8de75476bdbcde4311ef42578511c41b7010f3210d4f1c58715a4f2becca24e9`, somente leitura, reconstitui contextos da aula, cruza limites UTF-16 com 78 objetos e 43 contextos e confere identidade das cinco equações selecionadas; `resultado.json` SHA `4640600d604ed019f4c20e44ead5bb267244c0b717514eb30c0e207e0129ce0e` guarda contagens, recortes, hashes e exemplos. Reproduza com `node auditoria/termodinamica/evidencias/QA-09/triagem-formulas-r30-20261030/triagem.mjs` e compare a saída a `resultado.json`. Contenção não indica automaticamente cobertura científica, e ausência de contenção no ledger atual não prova ausência de parecer histórico. Objeto e contexto podem se sobrepor; ocorrências têm hierarquia e as categorias não são conteúdos independentes.

## Resultado da triagem estrutural

| Categoria do inventário | Total | Fora dos 78 objetos **e** dos 43 contextos do ledger |
|---|---:|---:|
| Texto direto | 9512 | 6018 |
| Atributos significativos | 807 | 720 |
| MathML | 711 | 407 |
| Equação contextualizada | 99 | 32 |
| Ficha do formulário | 100 | 78 |
| Tabela | 37 | 25 |
| Exemplo ou diagnóstico | 78 | 8 |
| Caso de oficina | 4 | 4 |
| Flashcard | 21 | 21 |
| Seção | 32 | 31 |
| Figura | 8 | 0 |

Esses números são da regra de **contenção integral no mesmo arquivo**, não uma medida de conteúdo aprovado ou porcentagem. Seção pai pode não estar contida embora um filho esteja; dados de figura em objetos não implicam que toda figura tenha aprovação científica. Os conjuntos de 11.409 ocorrências, 816 referências, 138 relações de recursos e seis ativos mantêm estado padrão `pendente_de_integracao` no ledger, sem promoção por esta triagem. Lotes anteriores de fórmulas, tabelas, exemplos, casos e flashcards podem existir fora dessa seleção do ledger.

## Lote selecionado — cinco equações em dois exemplos de ciclos

Escolhi as cinco ocorrências `equacao_contextualizada` nas posições 375817, 376747, 378744, 380581 e 382269. Nenhuma está contida nos objetos ou contextos do ledger direto; o manifesto identifica seus limites e hashes. Todas estão no bloco `base-refrigeracao`, intervalo UTF-16 370901–384308, SHA `467b2324a8e742e6c0cb60565ccf3d74480f434d3fb044eefe5eb78f2377a4b7`. A escolha é diferente dos lotes anteriores de fichas, ao tratar cinco ocorrências da **aula** com legendas MathML e exemplos completos. O bloco de ciclos foi examinado historicamente em r15, inclusive estes números; ver `auditoria-teoria-ciclos-r15-20261030/parecer.md`. O texto do refrigerador foi posteriormente modificado nas aplicações r29/r30: não transfiro a identidade ou aceite anterior para esta foto sem leitura.

1. **Motor:** QH=1000 kJ recebido e QL=600 kJ rejeitado como totais; trabalho líquido única outra transferência energética e ciclo fecha. Wlíq=1000−600=400 kJ por ciclo; η=400/1000=0,40. QH>0; o resultado é adimensional. A primeira lei não certifica temperaturas ou validade da segunda lei para fontes arbitrárias.
2. **Refrigerador e bomba de calor:** QL=600 kJ e Win líquido total=200 kJ por ciclo implicam COPR=3. Sob as hipóteses do ciclo simples do bloco (duas trocas externas de calor relevantes, compressor/válvula adiabáticos e sem outras trocas relevantes), QH=600+200=800 kJ e COPBC=4. As legendas explicitam trabalho líquido total recebido; mesma fronteira, ciclo e ausência de outra entrada energética são requisitos para COPBC=COPR+1. Sem essas condições, 800 não decorre somente de 600 e 200.

Contramodelo de domínio: se a mesma fronteira recebe adicionalmente 100 kJ de calor de acionamento não incluído em QL, o balanço resulta QH=900 kJ e a relação 800 deixa de valer; a conta original exige que essa entrada seja excluída. É balanço sintético, não descrição do ciclo de compressão apresentado. Para um exemplo que também satisfaça a segunda lei, motor entre fontes de 600 K e 300 K tem geração do conjunto 600/300−1000/600=1/3 kJ/K; refrigerador entre 270 K e 300 K tem 800/300−600/270=4/9 kJ/K. Esses valores de fonte são **hipotéticos**, não dados da aula nem prova de validade para temperaturas não especificadas.

As cinco fórmulas e legendas foram lidas na fotografia; não detectei erro nas contas sob as hipóteses citadas. A interpretação do exemplo de refrigeração depende do bloco de ciclo simples e de seus termos totais; solicito ao Auditor decidir se o exemplo isolado deveria explicitar as exclusões junto do enunciado. As condições e limites do parecer r15 e das aplicações posteriores permanecem separados; esta análise não aprova o bloco inteiro.

## Fontes e limites

O [parecer histórico r15](../auditoria-teoria-ciclos-r15-20261030/parecer.md) declara consulta ao [MIT, refrigeradores](https://web.mit.edu/16.unified/OldFiles/www/FALL/thermodynamics/notes/node25.html) para os modelos, não para os números sintéticos. A tentativa de reabertura web nesta rodada retornou erro sem conteúdo; não reivindico nova verificação externa das fontes. Sem navegador, leitor de tela, alunos, revisão humana ou certificação externa; esta triagem não encerra QA-09.
