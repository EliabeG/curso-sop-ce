# QA-09 — candidata de referência WIKA em português

Data: 30/10/2026. Corretor automatizado `/root/reference_triage`. **Candidata isolada; não aplicada e aguardando revisão independente.** Essa proposta responde à falha de acesso observada no lote [referências gerais r13](../referencias-gerais-r13-20261030/entrega.md), sem substituir a auditoria integral de QA-09.

## Observação e destino

Na seção `#fontes`, índice de referência 680 do r13, a URL `https://www.wika.com/en-us/111_16_111_26.WIKA` retornou HTTP **410** ao ser aberta pela ferramenta de pesquisa web em 30/10/2026. Um resultado indexado ainda a identificava; a resposta não prova inacessibilidade universal. A página do mesmo fabricante para os mesmos modelos, [WIKA Brasil, manômetro com tubo Bourdon](https://www.wika.com/pt-br/111_16_111_26.WIKA), abriu diretamente. Ela identifica modelos 111.16 e 111.26 e descreve deformação do elemento sob pressão, transmitida ao mecanismo indicador. A [folha de dados PM 01.10](https://www.wika.com/media/Data-sheets/Pressure/Pressure-gauges/ds_pm0110_pt_br.pdf) também abriu; vincula o funcionamento ao fluido de processo e aos limites dos materiais do fabricante.

A candidata troca somente a URL por `https://www.wika.com/pt-br/111_16_111_26.WIKA`, preservando texto “WIKA — manômetro de tubo Bourdon”, atributos `target` e `rel`, e os números do modelo na URI. É uma página de **fabricante**, adequada como referência do equipamento descrito, não como norma universal ou validação de qualquer instalação. O arquivo novo é uma proposta; a evidência histórica preserva o endereço inglês e o resultado da tentativa. Sua disponibilidade futura pode mudar.

## Identidade e ensaio

Base r13: `modulos/e1-termodinamica.html` SHA-256 `f19000a7ddb1f3552b9633b0efec266fb3f6c5e5065808505a2f65b2005aefbc`; inventário r13 SHA-256 `0df99b79bcc2350581fcdded72435d30d07858de237a549e6228ca73682f8d9b`. O elemento `<a>` original em `#fontes` é único; posição e dois hashes estão em [manifesto.json](manifesto.json), sem a quebra final dos arquivos `original.html` e `candidata.html`.

O [verificador somente leitura](verificar.mjs), executado a partir da raiz, passou na identificação, hashes, substituição literal única e comparação dos 197 artigos por ID, ordem e hash. A simulação produz HTML SHA-256 `662b98f1dabd84eaa9830c148cb2c0ca02cfcc15aa9d6ffce225e283a7dc902e`. Não houve aplicação nem teste de navegador real; o script não acessa a rede.

## Repercussão e revisão

A modificação, se aprovada e aplicada, muda o hash integral do HTML e desloca posições posteriores; exige inventário/mapa novos, conferência de links e dos 197 itens e reavaliação do alcance dos pareceres afetados. Seu argumento se limita à referência na aula E1; não modifica outras disciplinas nem transcrições oficiais. Solicita-se Auditor independente para confirmar identidade, acesso e equivalência temática antes de qualquer aplicação, e nova revisão da versão efetiva após eventual aplicação. QA-09 permanece aberto e o próximo ID bloqueado.
