# QA-09 — aplicação da referência WIKA na fotografia r15

30/10/2026. Executor `/root/next_examples`. Aplicada sobre r14 por sinal da coordenação, após os pareceres favoráveis da r14 efetiva, da candidata original e de sua reconciliação e ensaio na r14. **Aguardando auditor independente da versão efetiva.** A mudança troca o link WIKA inglês observado com resposta 410 pela página brasileira dos mesmos modelos; conserva rótulo e atributos. A verificação da disponibilidade refere-se às consultas registradas nos pareceres, não garante acesso futuro.

O executor `aplicar.mjs` SHA `4e6aa053ab7516d28f1e1fc9f29d2f1cff5e03679003e136b41baa37b1e497a3` exige hashes exatos das bases e dos três pareceres, identidade da reconciliação e dos blocos, além de destinos ainda inexistentes. O próprio modo `--apply` foi ensaiado em cópia descartável: recusou parecer adulterado antes da escrita e passou após restabelecer o parecer. O ensaio anterior do código de simulação e a reconciliação foram auditados independentemente. Snapshots anteriores e posteriores, edição e verificações estão no diretório `resultado/`.

Fotografia r15 e controles:

- Aula `modulos/e1-termodinamica.html` SHA `f6c461f1d6039ea47dc7e97f9ad734bb0ea3fcb902f01ffdbf18d18d88e08d0e`; formulário, integralmente preservado, `3ea110fda92c74253b69d89f5a6e62b288aa3bd99db6a51b54a6c67c8af82fce`.
- Inventário oficial JSON SHA `c1e13164e69d70a10d237682ab82ba1bca4c822691b8a5ff624e49bd2ad3876a`; Markdown `1953ff4afe439ec1c1b0f268d80752f5fc6dc881795ba89b1e76b45bd9daabea`.
- `inventario-r15.json` SHA `c8c9c3a3e141eba47a16e9f85c69f97c6e8b8a55aab689c6120ef1a0070c9d9c`; `mapa-correspondencia-inventario-r14-r15-r1.json` SHA `1a264971f918313d3a495f9af18f7f712c18b6bceeca5e1494dfdad2e9fb2533`.
- `resultado/verificacoes.json` SHA `785ed68384ac854bf3bc4d0e64cd8d9bc569b70ff41c1580a7474b29e69a5cbe`; `resultado/edicoes-aplicadas.json` SHA `87fd45a7d0b3c08e228b888c9e506da4299b8a337ed4d0d01068508900d3a020`.

Os hashes de aula, inventário estrutural e mapa coincidem com o ensaio. A verificação automática preservou os 197 artigos byte a byte e os 197 registros, os 734 MathML da aula e todo o formulário. O mapa identifica 11.397 pares externos de hash igual, um contexto ancestral e um par interno que exigem exame, 816 referências com uma troca e 138 relações de recursos. O validador passou com 1263 links locais e 29 recursos; não verifica acesso remoto.

Solicita-se Auditor distinto para confrontar pareceres, snapshots, delta, inventário, mapa, contexto ancestral e par interno, e revalidação localizada dos efeitos. Não houve navegador, leitor de tela, estudantes, revisão humana ou certificação externa. QA-09 não está concluído e nenhum aceite anterior é automaticamente transferido.
