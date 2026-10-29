# FUN-02 r1 — diferenciais, caminhos e propriedades

Entrega congelada do Corretor em 27/10/2026, para auditoria independente. Critérios: FUN-02 e regra comum §3.2 da auditoria principal. Nenhum próximo ID foi iniciado; controle e checklist permanecem sob o coordenador.

A unidade 4.1 foi publicada no E1 com objetivos, recuperação matemática, teoria com hipóteses, exemplos de decisão e três problemas abertos com soluções/rubricas. P1 exige construir dois processos entre os mesmos estados sob uma janela térmica, integrar os trechos e fechar ciclo. P2 exige reconstruir potencial, testar domínio/condições, diagnosticar cancelamento de ciclo e identificar parâmetro. P3 integra compressão definida e distingue capacidade de propriedade, capacidade do caminho e condições da relação entre calor e entropia.

Os exemplos e problemas não são simples trocas de números. O [extrato individual](../evidencias/FUN-02/novos-registros-r1.json) registra hipóteses, demanda, etapas, fontes e exposição local. P1/P2 foram estimados avançados e P3 intermediário pelas decisões efetivamente exigidas; não houve validação empírica. As seis células afetadas de C01/C02/C03/C08/C09/C10 ligam a aula às atividades e conservam o alcance parcial.

## Evidências e resultados

- [Conferência científica e cobertura dos critérios](../evidencias/FUN-02/conferencia-cientifica-r1.md): autoria, modelos, fontes, cuidados de domínio, sinais, orientação, fronteira e reversibilidade interna/externa. O parecer independente ainda está pendente.
- [Verificação reproduzível](../evidencias/FUN-02/verificacao-r1.json): 240 verificações de estrutura/preservação, incluindo recomposição byte a byte do HTML anterior; 194 artigos e registros anteriores idênticos e 194 linhas anteriores do resumo preservadas. Compartilhados, esquema/validador e arquivos FUN-01 preservados.
- [Validação canônica](../evidencias/FUN-02/validacao-inventario-r1.json): 197 registros/197 artigos, 11 recursos, 1.062 links locais, zero erros/avisos. Os três títulos foram extraídos dos h3 publicados.
- [Cálculos do módulo](../evidencias/FUN-02/calculo-r1.json): 49 verificações. A [reprodução pelo coordenador](../evidencias/FUN-02/reproducao-coordenador-r1.json) concorda até resíduos de ponto flutuante. P1/P3 foram calculados pelo coordenador antes das soluções; P2 foi rederivado por ele com os resultados do apoio conhecidos.
- [Navegador final do coordenador](../evidencias/FUN-02/navegador-coordenador-r1.md), no mesmo hash HTML: sumário/âncoras, três soluções/rubricas, retorno por teclado e SVG legível; logs de erros/avisos vazios no teste. Alcance observado de 1265×712, sem teste móvel, leitor de tela ou piloto.

A reprodução estrutural está em `verificar-fun02-r1.mjs` (função `verificarFun02()`); o cálculo usa `calcularFun02(dados)` no módulo publicado com o JSON correspondente. Os ciclos e a observação de P2 são consumidos do pacote, sem avaliação de expressão textual.

## Arquivos congelados

O [manifesto r1](../evidencias/FUN-02/manifesto-r1.json) contém hashes, tamanhos, evidências e cópias espelhadas no pacote-r1. A fonte anterior e os deltas literais de integração também foram preservados.

| Arquivo | SHA-256 |
|---|---|
| modulos/e1-termodinamica.html | `719a53ef86075dd3be9c7d9603faca620ec07416d1e97a5017740abb5b74c01a` |
| assets/termodinamica/fun02-dados-v1.json | `511aac986e9122e5498cdf69609274685791000a19f140a09d539fca01676319` |
| assets/termodinamica/fun02-calculos-v1.mjs | `2fdd0e498c41db2f7f8e90d5114dcd015f5377e00901e6274f25262e13c79a70` |
| assets/termodinamica/fun02-caminhos-v1.svg | `f324acce9060eb15eeab58958649392f4e5b667fbaf2ad9b63e3c68fbe3eae35` |
| auditoria/termodinamica/inventario/inventario-questoes.json | `c577058429375c11196eb99ae6bd01a9020f5258d3981d72c58896829ed900a2` |
| auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md | `c650d94556d527725595dfc86b1feaa055a32a2d9060e9b4680f1a152e11cca4` |

Autoria: Corretor (teoria/P1/P3, integração, dados/cálculo e inventário); apoio_fun01 (preparação e P2, revisados na integração); coordenador (fontes complementares, conferência numérica, figura e navegador). Nenhum desses registros substitui o agente Auditor. Não há dados experimentais, dificuldade medida, certificação global de competências ou encerramento dos demais itens curriculares. Aguardando parecer de FUN-02 r1.
