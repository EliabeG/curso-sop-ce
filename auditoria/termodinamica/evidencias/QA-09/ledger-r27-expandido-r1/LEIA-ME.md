# QA-09 — consolidação parcial expandida da fotografia r27

30/10/2026. Integrador `/root/planning`. **A consolidação aguarda auditor independente.** Preserva o ledger parcial r27 e seu parecer sem regravá-los. O nome r28 nos lotes identifica a rodada de evidências; todos os recortes aqui são da foto **r27**, aula `9af8e2c9ffe509e40594d086a9ef4ad75127fb4ca873efb305d3144e08f3fc49`, formulário `16329b7369c4ba927f5f7da30551f86934aad1f6a6e55627443dea5cb9fe0c02` e inventário `a58d7f0b0a5f097eef83ad83026ef49e801457b87f7cf2b2345c3dd915597c7c`.

A base preserva os 18 objetos individualmente revalidados, com seus vínculos aos contextos e parecer da ponte. Além deles, 45 recortes explícitos constam em seção separada: **22 fichas** 01–22, **6 blocos** de entrada e escopo FUN, **4 SVGs**, **3 artigos com gráficos** AV-06/30/37 e **10 diagnósticos** D06–10/D21–25. Cada um carrega posição, hash, entrega, parecer independente e alcance restrito; os três PNGs também carregam identidade dos arquivos. No gráfico AV-06 permanece registrada a recomendação de esclarecimento editorial. As fichas preservam recomendações sobre domínio de denominadores e os diagnósticos dependem das hipóteses das bases indicadas nos respectivos pareceres.

O estado `conferido_no_escopo_localizado` não promove automaticamente ocorrências de inventário, pais, filhos, links, bases, fórmulas, referências ou recursos. Os conjuntos se sobrepõem e não representam percentual de conclusão. A existência de parecer não demonstra acessibilidade, aprendizagem, proveniência oficial das figuras ou revisão humana. Demais registros seguem pendentes de integração; QA-09 continua aberto. Minha autoria do parecer dos seis blocos teóricos é declarada: a integração não substitui sua auditoria, feita anteriormente em papel distinto do autor do lote, nem torna independente a presente consolidação.

## Reprodução somente leitura

`python auditoria/termodinamica/evidencias/QA-09/ledger-r27-expandido-r1/ledger.py --verificar auditoria/termodinamica/evidencias/QA-09/ledger-r27-expandido-r1/ledger.json`

O gerador/verificador reabre a fotografia, inventário, base, pareceres, entregas e manifestos com hashes fixados, reextrai os 45 recortes, confere três PNGs e destinos dos diagnósticos e preserva integralmente os 18 objetos da base. Sem argumentos imprime JSON em stdout. Verificação positiva passou; quatro mutações em cópias temporárias — hash, posição, remoção de recorte e estado padrão — foram rejeitadas. Essas verificações não realizam julgamento científico nem criam novo aceite por hash.

- `ledger.py` SHA `ff9818c4f9aa2e84b49f1b6c4f8169209c24034f8b0e696a5f93b6038fd227a8`.
- `ledger.json` SHA `c91f24e8af862fe452c4d4c4ee9b9a987f548aada987d6501ae06773144ce051`.
