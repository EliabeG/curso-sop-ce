# QA-09 — auditoria independente da aplicação da oficina 8.1, r1

Data: 29/10/2026. Revisor: agente automatizado independente `/root/auditoria_diagnosticos_seis`. **Veredito localizado: aplicação examinada sem ajustes obrigatórios identificados.** Não é aprovação global de QA-09, não altera produto ou controle e não libera o próximo ID. A decisão de continuidade cabe ao coordenador conforme o protocolo.

## Critério e escopo

O critério QA-09 exige inventariar e recalcular todas as ocorrências numéricas, incluindo exemplos, oficinas, diagnósticos, fichas, figuras e explicações, além dos itens já cobertos por BAN-08. Esta revisão cobre apenas os quatro blocos aplicados na oficina, as fotografias e o mapa r5→r6 e os efeitos localizados sobre BAN-02/07/08. A revisão integral de QA-09 permanece pendente.

## Candidatas aplicadas e contas

Os quatro originais ocorrem uma vez no HTML anterior e as quatro candidatas uma vez no atual; seus arquivos e hashes de fragmentos conferem com o manifesto. A substituição sucessiva dos quatro originais por essas candidatas reconstrói **byte a byte** o documento atual, que coincide com a fotografia posterior. Portanto, não houve outras alterações no HTML: bases, outros blocos, soluções, 28 diagnósticos e links foram preservados. Os hashes do parecer independente das candidatas e de todos os arquivos listados no manifesto de verificação conferem. A revisão anterior das candidatas examinou sua suficiência perante a adjudicação; a identidade aqui verificada estabelece que esses mesmos textos estão na versão efetiva.

Recálculo independente com os dados nominais e condições publicadas:

- Estado: `(1380−500)/(2700−500) = 0,40`; em 5 kg, vapor 2 kg e líquido 3 kg. A temperatura é a de saturação à pressão considerada, sem valor numérico fornecido. O diagnóstico seguinte, com os dados precedentes, dá título 0,70 e massas 5,6 e 2,4 kg em 8 kg.
- Pistão: `W_f = 120(0,15−0,40) = −30 kJ`; pela exclusividade, `W_total = −30 kJ`; `Q = −10 kJ` e `ΔU = +20 kJ`, com trabalho do sistema positivo.
- Turbina: `−50−Ẇ = 2(2800−3200) = −800 kW`; `Ẇ = 750 kW` produzido, sob regime permanente e demais condições explicitadas.
- Compressor: `−15−Ẇ = 3(290−250) = 120 kW`; `Ẇ = −135 kW`, isto é, 135 kW de eixo recebidos.

Os números são condicionados aos modelos e dados nominais, sem declaração de precisão instrumental. Os casos de duas fontes permanecem inalterados; sua suficiência contextual foi adjudicada anteriormente.

## Preservação e testes

Os 197 elementos `article` do HTML anterior e atual são idênticos e na mesma ordem; os 197 objetos individuais do inventário oficial também são idênticos. A única chave de topo do JSON alterada é `fonte`, que aponta ao hash e fotografia do HTML atual. O Markdown acrescenta apenas a seção histórica da aplicação, com link à entrega existente. Reexecutei o validador oficial sem gravar evidências: `ok=true`, 197 itens/artigos, 29 recursos, 1.263 links locais e nenhum erro ou aviso. Seu alcance é estrutural e documental, não certifica mérito científico ou aprendizagem.

Os hashes de `assets/curso.js`, `assets/registro.js` e ficha de fórmulas coincidem com a versão anterior. Reexecutei o teste de persistência BAN-08 após verificar que não regrava evidências: passou nos cenários de histórico, contagem, aviso, gravação/releitura, refazer e falhas. Usa funções reais com DOM e armazenamento simulados, concentra-se em AV42/45/52 e não constitui teste em navegador real nem acesso a dados pessoais. Os exemplos e casos da oficina não são os artigos pontuados; a preservação dos artigos e do código sustenta que os deltas não alteram as entradas das digitais ou respostas pontuadas. Não reexecutei `verificar-aplicacao-r1.mjs` porque ele grava a evidência histórica; os resultados acima são independentes da sua saída.

## Fotografias, mapa e limites

As fotografias r5 e r6 contêm 11.396 ocorrências cada e a mesma lista de 197 artigos excluídos. Confrontei os 11.396 pares na ordem com ambas as listas: arquivo, tipo, tag, seção, âncora, IDs, posições iniciais e hashes conferem; IDs são únicos em cada fotografia. As cinco substituições textuais dos quatro blocos coincidem com as cinco regiões e deltas UTF-16 do mapa; todos os deslocamentos iniciais conferem. Há 2.278 IDs deslocados, 11.386 hashes iguais e 10 diferentes: a seção ancestral, quatro blocos e cinco parágrafos. Os 10 intervalos atuais são reproduzidos pelas substituições nos intervalos anteriores.

A correspondência usa ordem e posições; IDs deslocados não são identificadores duráveis. Hash igual, especialmente de texto direto, não garante contexto ou validade de dependências, nem transfere provas e aceites automaticamente. O mapa não cobre as listas separadas de referências/recursos nem demonstra completude visual ou mérito de todo QA-09. O segundo parser e sua validação estrutural são evidência do Corretor, não teste em navegador. Evidências anteriores continuam vinculadas às versões e escopos examinados.

## Efeitos localizados sobre aceites

- **BAN-02:** os 197 registros e artigos mantêm seus atributos e conteúdo; apenas a fotografia integral e o histórico foram atualizados. O validador não substitui reclassificação pedagógica integral.
- **BAN-07 e BAN-08:** os artigos, scripts e ficha foram preservados; os quatro deltas esclarecem modelos em blocos fora dos itens sem contrariar os cálculos aqui conferidos. Não identifiquei impacto sobre os resultados anteriormente validados para os 197 itens. Esta é uma ponte localizada entre versões, não nova auditoria integral dos gabaritos ou cálculos nem aprovação de QA-09.

| Critério da aplicação localizada | Resultado |
|---|---|
| Candidatas revisadas aplicadas com precisão | Atendido: substituições reproduzem o HTML efetivo byte a byte. |
| Hipóteses, contas e unidades dos quatro blocos | Atendido nas condições e com os limites descritos. |
| Preservação dos artigos, bases e inventário | Atendido: 197 artigos e 197 registros idênticos; fonte e histórico atualizados. |
| Mapa e fotografias | Atendido no escopo e com as limitações descritas. |
| Efeito nos aceites e persistência | Ponte localizada sem impacto identificado; persistência testada em ambiente simulado. |
| QA-09 integral e próximo ID | Não avaliados nesta revisão parcial; não há liberação. |

Não há ajuste obrigatório identificado para esta aplicação localizada; o restante de QA-09 permanece sujeito aos critérios integrais do protocolo.

## SHA-256

- HTML anterior `49b0df4fe59dfd01913f4d41a5e6869705f4bf4d6ded251060f940cd5d12c91b`; HTML atual e fotografia `dd47dc9dbc5c22f6f74a4fa67bd28b495cff775ff8ca04cec2c76c405dfefd1a`.
- Inventário oficial JSON anterior `9102ed042ff940c71604eadc361dcd3b4006a3bc1dc2a0e336cc0f2de0508edf`, atual `f80a1c6b542b3db14272ea8a0a1c710d8e4dd1906f4436dfc12b93547895fdf1`; Markdown anterior `898830d59f4162be64954315f13a85aa27e53efbcadc61f25cd82b22901425ab`, atual `f3578d669fd2cc7393879a293279fb5697d8bd8dd5a0fdb75adb57f53c704bfb`.
- Inventário QA-09 r5 `e21bc074025815cb5708875f938cb8a0de200ebecc66c4a7c8997493c01b0ea4`, r6 `a38b60799c23cf88fb0085e7c9bd82b4f22f58a4c7f89b6b418f8b3f5ae5d1aa`; mapa `295293dc34d75b8c25ec575dba4a2d96e29389de7a332cd7a3a98279ab3bb82d`; validação estrutural do Corretor `22572c940244a3572afd86d02b71621ee22a799fca9c9112cb81883ca1ec53c6`.
- Entrega r2 `eb7973ab2abe0ae098b9291c29e50710a08821447f05db2f5b4a52638207481f`; manifesto r1 `249654f56f678c59823262e0cb8a096e661a661b849574aa37562a5db20b4eaa`; manifesto de verificação r2 `5a5aa94d0ac318702f29fe5ffc80186d3792a921bc1233ebf1447b2ed6840500`; parecer das candidatas `a9ef64c60c99c456fa1574007711576ccb3ce1b60214ef7df0ad360bea42de43`.
- `assets/curso.js` `a20f4d19158073a9a1c48aabdfba8fa863b02063e16061c00b16448a6ccc2e13`; `assets/registro.js` `46da94527d6639fe0265bd766286f1ef39623966105e00bda3b31f21ca2c247c`; ficha `c27422b409a0a755448982c4074c6d6967fd3e91d7eae20274e218530f5c37b0`.
