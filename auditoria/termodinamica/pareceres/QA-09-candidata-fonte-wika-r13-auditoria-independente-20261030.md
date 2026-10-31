# QA-09 — auditoria independente da candidata WIKA r13

Data: 30/10/2026. Auditor: `/root/next_formulas`; corretor: `/root/reference_triage`. **Parecer: APROVADA ISOLADAMENTE**, limitada à troca proposta e à fotografia verificada. Não é aprovação integral de QA-09 nem comprovação de funcionamento futuro do endereço. Produto não alterado nesta auditoria.

## Verificação externa independente

Abri a [página do fabricante WIKA Brasil](https://www.wika.com/pt-br/111_16_111_26.WIKA): o conteúdo está em português e identifica os modelos 111.16 e 111.26, manômetros com tubo Bourdon de liga de cobre para montagem em painel. A descrição associa a deformação do tubo sob pressão ao mecanismo de indicação. A [folha de dados PM 01.10](https://www.wika.com/media/Data-sheets/Pressure/Pressure-gauges/ds_pm0110_pt_br.pdf), pp. 1–2 e 5, confirma modelos, princípio, aplicações e especificações. A fonte é adequada para o equipamento indicado pelo rótulo, não estabelece exigências universais para todas as instalações ou instrumentos.

A abertura da [URL inglesa original](https://www.wika.com/en-us/111_16_111_26.WIKA) retornou 410 na ferramenta consultada em 30/10/2026; isso é uma observação daquele acesso, não prova que o endereço falha para todo usuário ou que foi permanentemente removido. Não foi possível comparar o conteúdo ao vivo da versão inglesa; a identidade de modelo decorre do identificador da URI original e da designação explícita da página brasileira, não de uma comparação integral das duas páginas.

## Identidade e delta

Confirmei o SHA-256 da base `modulos/e1-termodinamica.html` como `f19000a7ddb1f3552b9633b0efec266fb3f6c5e5065808505a2f65b2005aefbc` e do inventário r13 como `0df99b79bcc2350581fcdded72435d30d07858de237a549e6228ca73682f8d9b`. O manifesto da candidata tem SHA-256 `7e06a9cbedafca22020d40abcf28744e7369b36aba870070090c8d5e3b21c01f`. A referência 680 é identificada na seção `#fontes` pelo recorte e URL antigos; o original ocorre uma vez. A candidata troca somente `en-us` por `pt-br` no `href`, preservando rótulo e atributos. Os hashes de fragmento do manifesto são calculados sem a quebra de linha terminal dos arquivos de amostra.

Inspecionei e executei o verificador de leitura da candidata: confirmou hashes dos fragmentos, posição UTF-16 e referência no inventário, ocorrência única, substituição literal, análise HTML e preservação dos 197 artigos em ordem e conteúdo. O HTML simulado tem SHA-256 `662b98f1dabd84eaa9830c148cb2c0ca02cfcc15aa9d6ffce225e283a7dc902e`. Esse teste é uma simulação sem acesso à rede e não substitui conferência da versão efetiva após aplicação. Como r13 é a base confrontada, se houver mudança da fotografia antes da aplicação, reencontrar o elemento pelo conteúdo e conferir novamente o delta e a nova base; não confiar nas posições antigas.
