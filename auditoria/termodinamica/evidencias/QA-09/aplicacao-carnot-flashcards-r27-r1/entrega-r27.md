# QA-09 — aplicação conjunta de Carnot e flashcards r27

30/10/2026. Executor `/root/next_formulas`. A coordenação autorizou as três candidatas isoladas de COP, Carnot e base de Carnot, e **somente a r2** do compressor, após parecer independente. **Aplicadas localmente, aguardando auditoria da versão efetiva.** QA-09 permanece aberto.

A base Carnot delimita dois reservatórios, temperaturas absolutas e indicadores de motor e de ciclos reversos; o cartão de Carnot explicita o mesmo domínio. O cartão de COP identifica trabalho líquido total recebido e positivo; o de compressor diferencia trabalho total não-fluxo de trabalho de eixo e preserva hipóteses da comparação isentrópica.

## Guardas e ensaio

`aplicar.mjs` SHA `c289a23e06c3546523cfa770c0b4350711ff24ffd37816eb0f8b18e32baec28f` requer `--executar-r27`, admite somente a raiz autorizada ou cópia `/tmp`, verifica fotos r26, inventários e nota oficiais, quatro manifestos, parecer das candidatas e auditoria r26 efetiva, gerador e mapeador. Verifica recortes únicos, offsets, deltas e o SHA conjunto aprovado `9af8e2c9ffe509e40594d086a9ef4ad75127fb4ca873efb305d3144e08f3fc49` antes da escrita. Recusa destinos existentes. O executor exato foi rodado integralmente em cópia antes da aplicação; resultado de ensaio SHA `71b8833f42583d7acc0501f5106a6b63d8b18566a96cf96bf6145f7c46f1d650` e mapa SHA `2eff0a63420831284ca726ed4efaadb436ffc6c976de151d2f70eb9e2e9790b4` coincidem byte a byte com a execução efetiva. Gravações são sequenciais, não transacionais; snapshots preservados permitem diagnóstico/reconciliação em caso de falha.

## Resultado e limites

Aula r26 `afc7ff0aba80596aa8aa7a3eeb5b9a470948c7d866c6911911b9b00fb243bac2` → r27 `9af8e2c9ffe509e40594d086a9ef4ad75127fb4ca873efb305d3144e08f3fc49`; formulário preservado `16329b7369c4ba927f5f7da30551f86934aad1f6a6e55627443dea5cb9fe0c02`. Inventário estrutural r27 `a58d7f0b0a5f097eef83ad83026ef49e801457b87f7cf2b2345c3dd915597c7c`; mapa r26→r27 `2eff0a63420831284ca726ed4efaadb436ffc6c976de151d2f70eb9e2e9790b4`. Inventário oficial atualizado `bc41bab109174695acd787c183dca7f8e58dd227c8389e48d83bc2b7a4e7e27e`, nota oficial `abb09d0926d24a111a7963cc8c0726d7eeeaffaa703468fb602977d71a55cfb4`; `resultado/edicoes-aplicadas.json` `24ecb7389b8e7dc215108420a798206d158af3afdbcc97b281b093b3eca9468f`. `resultado/` conserva fotos e inventário/nota anteriores.

A execução confirmou 197 artigos, 197 registros, 734 MathML, IDs/links/ARIA e formulário integral preservados. O mapa lista 11.206 pares externos preservados, dois contextos ancestrais e 199 pares internos a conferir; 816 referências e 138 relações de recursos mantidas. Validador canônico: 197 itens/artigos, 1.263 links locais e 29 recursos, sem erros ou avisos. Estes são testes estruturais, sem transferência automática de aceitabilidade científica; não houve navegador real, leitor de tela, alunos ou revisão humana. Solicita-se Auditor distinto da aplicação e dos pares afetados.
