# QA-09 — Revisão independente da candidata isolada do diagnóstico 1, r1

Data: 29/10/2026. Responsável: apoio independente automatizado. Revisão pontual; não aplica alteração nem aprova QA-09.

## Decisão

**Candidata tecnicamente adequada para corrigir a insuficiência identificada**, sujeita à aplicação controlada e à verificação da versão aplicada, seus vínculos e artefatos dependentes. A alteração insere apenas `de massas iguais` no enunciado: “Divida uma amostra homogênea em quatro partes de massas iguais nas mesmas condições.” A resolução existente, sem modificação, decorre agora das hipóteses: cada massa é `m/4`; para densidade homogênea `ρ=m/V` e nas mesmas condições, cada volume é `(m/4)/ρ=V/4`. Temperatura e densidade permanecem iguais sob as condições enunciadas. Kelvin, símbolo K, é a unidade SI de base de temperatura termodinâmica. Não há alternativas de múltipla escolha neste diagnóstico; o `details` contém resposta explicativa e link de retomada.

O fragmento original exato está presente uma única vez no documento de origem. Comparação de bytes: candidata = original com a única substituição `em quatro partes nas mesmas condições` → `em quatro partes de massas iguais nas mesmas condições`; a solução, o link `#base-medidas`, o número, a marcação e demais palavras ficam intactos. O link corresponde ao `h3` de mesmo ID na fonte. Isto resolve o contramodelo 10%/20%/30%/40% descrito em `QA-09-adjudicacao-diagnosticos-01-05-independente-r1.md`.

## Identidade, progresso e limite da verificação

O trecho é `div.exemplo` dentro da seção `#preparacao-questoes`; não é um dos 197 `article` de BAN-08, não tem alternativas ou chave e não foi identificado como item de placar. Em `assets/curso.js`, o placar autoral seleciona `article.questao` (linha 1412), enquanto os bancos reais e Avalia selecionam `.concurso-item, .avalia-item` (linha 1212); nenhum seletor do script procura `.exemplo`, `.diagnostico` ou `preparacao-questoes`. A proposta não altera artigos, IDs ou estrutura do módulo; pela inspeção desses seletores e do delta, não há indicação de mudança de digitais ou respostas salvas dos bancos. A âncora da seção e do retorno à base ficam preservadas. Isso é conclusão estática sobre o código examinado, não teste em navegador ou garantia sobre estado de terceiros e extensões. Aplicação altera o hash do documento integral e pode invalidar fotografias e validações dependentes; deve haver confronto após aplicação, incluindo eventuais referências e aceites pertinentes. Os hashes de fragmentos do inventário QA-09 deste bloco passarão a representar a versão anterior.

## Conferência de hashes

- Documento de origem `modulos/e1-termodinamica.html`: `9ec10053e40640feeb977baea742da3cbe4d546659f772f0256c6b3cb0720a55`.
- Fragmento original exato, sem a nova linha adicionada ao arquivo: `38dfd58742e4dd620bced89730914ad6d3288e7856f0cadf312481c6c676ad25`; arquivo `diagnostico01-original-r1.html`: `80a22fe349ce210437582ddc0f06610a30e1259766d55c19d496e39276f62a29`.
- Fragmento candidato exato: `a3a7267bc9169ae0293ec449143d14f82144612793631c5a33537d7f71511896`; arquivo `diagnostico01-candidata-r1.html`: `105196333d9b8092d7f56401b296f86a6ed9ef7ad6796fe31a091cd7c6b2b506`. A diferença entre hashes de fragmento e arquivo decorre da nova linha final do arquivo isolado.
- Manifesto `diagnostico01-candidata-r1.json`: `4418c3909d7e3c937e95ee39102e9b5acb5b246cfee0b1c84edc3125623efb2c`; nele `inventario_sha256` refere-se a `auditoria/termodinamica/evidencias/QA-09/inventario-r2.json`, hash confirmado `8f37801a8dfdc073c3ee37357b36126a5235b8bb1fc4ad1f09215236bd5753f4`. Esse arquivo é distinto de `auditoria/termodinamica/inventario/inventario-questoes.json` (`adb2f7edd0bdfbf6d1f0ec0bc8aefd46b22d6728a0aa59fc3981281aac93fbcd`).
- Análise do Corretor `diagnostico01-analise-candidata-r1.md`: `3a536ad778fc930486251a9da38d632bacf851b12b39521219700ef630ad39c9`. Minha adjudicação anterior: `993e81a54a46771ff33bc03dc546cdadded091d706c7ab427571bb7c0ae32033`. Código `assets/curso.js`: `a20f4d19158073a9a1c48aabdfba8fa863b02063e16061c00b16448a6ccc2e13`.

Não foi avaliada aqui a correção dos demais diagnósticos nem qualquer aprovação global. Os resultados valem para os bytes identificados e a candidata isolada; não se deve confundir esta revisão com evidência de aplicação ou com teste de regressão.
