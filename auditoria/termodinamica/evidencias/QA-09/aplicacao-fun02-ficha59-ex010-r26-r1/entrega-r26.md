# QA-09 — aplicação conjunta FUN-02, ficha 59 e EX-010 r25 → r26

30/10/2026. Executor `/root/next_examples`. **APLICADA, AGUARDANDO AUDITORIA INDEPENDENTE E REVALIDAÇÃO LOCALIZADA.** A coordenação autorizou a aplicação das seis candidatas aprovadas; este registro não é aprovação científica da versão aplicada nem encerra QA-09.

A aula recebeu quatro ajustes FUN-02 sobre escala, derivadas parciais, trabalho de fronteira e fator integrante, além do ajuste de EX-010 e tabela de equipamentos. O formulário recebeu a condição de trabalho líquido total positivo no COP da ficha 59. Os enunciados e dados dos 197 artigos pontuados são preservados em bytes; suas dependências de contexto devem ser reavaliadas pelo Auditor quando alcançadas pelas mudanças, não automaticamente aceitas por identidade.

## Bases e pareceres

Aula r25 SHA `ea0a7e3877c0a0250dac3d9c993c7922a03400929eb7a5dad39fcb27e3263c7e`, formulário `694ee3d26e8f5679d565986cfb0ad8c10aa98667fc8ffb62a569a87679847a58`, inventário `6798d317db30bd69435ed14862cc03cd0f0c6313e40408dd8831052285984116`. Auditoria da aplicação r25 `QA-09-aplicacao-fun01-fases-r25-auditoria-independente-20261030.md` SHA `647bbcdaa8e9d5ceb8940a22823701953261e4f43ee207095356c416b672c659`.

- FUN-02: parecer `QA-09-candidatas-fun02-r25-auditoria-next-graphics-20261030.md` SHA `40845c48b69da96a2cb0ad3318a4285373c6d091da5b91ebdcffecefb3ce1d63`. Manifestos escala, parciais, trabalho e fator respectivamente `89c37950a565509a6e0d7d54e657f4fd9b6cb174a30429108bfd943e60f8ac89`, `ef267f6481e3377334309a593ae70b7853fff7254c653b294896c03ba3574e37`, `5fee9a61920cfd5a93c0ed47049fbdd3de55676dc0742567ab77a4291d7c2960`, `5bfadef7a0fb1052ffb7c1e09fdf78719464ec6ba61a5f040a4b969e6ed5c21b`.
- Ficha 59: parecer `QA-09-candidata-ficha59-r25-auditoria-reference-triage-20261030.md` SHA `7db90a3ade1b8463271fcce4bc8d1a0a3ef84895355a71e073791d554b847fee`; manifesto `228c16439f800be7b4753b728c42f4a856f88c18b2528b18d8b588c53c82743e`.
- EX-010/tabela: parecer `QA-09-candidata-ex010-equipamentos-r25-auditoria-independente-20261030.md` SHA `99e0310a24dc4ab7d30a1e0dff4c6380c9a75cb4844c4f12a5a15b97eb31578a`; manifesto `9374290e0e6203e356e71b3d87b4e8df9aa714e4c5f04556a9aa2113f01c2da7`. Fui também autor dessa candidata; o parecer citado é de Auditor distinto.

## Guardas e ensaio

O executor `aplicar.mjs` SHA `171d57ed80e6bf8c47a9cbdbae077eac5c49796f686c2482a9850561d6482a0d` confere fotos, pareceres e seis manifestos por hash, trechos e reconstrução literal, exclusividade dos destinos e ausência de sobreposição por documento. Os cinco intervalos da aula são disjuntos, inclusive os blocos adjacentes; os deslocamentos são calculados em UTF-16 a cada substituição. Na ficha 59 cada alteração aparece duas vezes, em texto visível e busca, e ambas são verificadas. A comparação independente em memória, por substituições em ordem decrescente, previu aula `afc7ff0aba80596aa8aa7a3eeb5b9a470948c7d866c6911911b9b00fb243bac2`; o formulário hipotético `16329b7369c4ba927f5f7da30551f86934aad1f6a6e55627443dea5cb9fe0c02` coincide com aquele calculado pelo Auditor da candidata. Os deltas e seus offsets constam em `resultado/edicoes-aplicadas.json` SHA `49161293439d1c4cdcce5f38efb81b3af90854a33e5a6acf6af5f5e72b5c2f5f`; snapshots antes/depois dos dois documentos e inventários anteriores estão em `resultado/`.

Gerador `inventariar-r26.mjs` SHA `e08977dc2338e13e733c51ba7c0816363a571feee68b292ee1172610fdde1c0c`; mapeador `mapear.py` SHA `713e3514ba92fb7dfef5c0660878f6c6f79510eefd5186652b0f62fc85076f72`. O executor passou com `--apply` em cópia descartável sob `/tmp`, e a aplicação efetiva reproduziu byte a byte aula, formulário, inventário oficial e mapa. Verificações no ensaio e na versão efetiva SHA `01459a1407ef6ab278c7e5ec88b63e5376768bc2bb6cf692766b64228385bcca`; o marcador no ensaio assinala auditoria pendente porque o comando `--apply` foi usado na cópia. O executor não é transacional; falha após escrita exigiria examinar e reconciliar o estado antes de repetição. Aqui completou sem erros.

## Fotografia efetiva

- Aula r26 SHA `afc7ff0aba80596aa8aa7a3eeb5b9a470948c7d866c6911911b9b00fb243bac2`; formulário SHA `16329b7369c4ba927f5f7da30551f86934aad1f6a6e55627443dea5cb9fe0c02`.
- `inventario-r26.json` SHA `d73d6b239822b288329a75fc1f976419ccae7047d1bc74ba161102a529038241`; mapa `mapa-correspondencia-inventario-r25-r26-r1.json` SHA `4cf2e325012929faa2f16c3a01bb8710847cb6f302aef74f2c012dfce8decc9d`.
- Inventário oficial JSON SHA `6858e6ae494c8996518a9bd12169905cc1bedd7457f3f99c86a6d7b4ff80f3f0`; histórico Markdown SHA `e612f97e23794447f5f96b98954501281ba3ad5c5c11efd23368c8268044e1b7`.
- Preservados 197 artigos/registros, 99 fichas não alvo, 734 MathML da aula e 191 do formulário em bytes, bem como atributos de identidade/links/ARIA testados. Validador canônico: 1263 links locais e 29 recursos, sem erros/avisos.
- Mapa: 11405 ocorrências r25 e 11407 r26, 11011 pares externos, 3 pares ancestrais e 391 internos a conferir, 2 adicionadas ou reestruturadas. As 816 referências e 138 ocorrências de recursos foram preservadas sem alterações de referências. Mapeamento estrutural não transfere aceites.

Solicita-se Auditor distinto para os seis deltas efetivos, suas interações e os 391 pares internos, 3 ancestrais e 2 itens adicionados/reestruturados; verificar contextos dos artigos e revalidar localmente. Testes estruturais não certificam ciência integral, apresentação, acessibilidade real ou aprendizagem.
