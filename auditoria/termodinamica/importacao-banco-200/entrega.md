# Importação documental — banco autoral 1–200

Data: 13/11/2026. Implementador: agente automatizado Codex.

Pedido atual do usuário: adicionar as questões do ZIP `Questoes_001_200_e_Gabaritos.zip` ao curso. Esta entrega é a importação desse material, não a retomada nem o fechamento do recálculo integral de QA-09. Não inicia outro ID da fila AAA e não transfere os aceites BAN-07/BAN-08 aos 200 itens importados.

## Conteúdo e limites

- Página própria com 200 artigos, 1.000 alternativas, comentários e referências às páginas dos quatro PDFs originais, copiados sem alteração de bytes.
- 50 tabelas extraídas para HTML e 46 complementos visuais recortados do documento, com texto correspondente na legenda. As imagens de contexto das capas não são questões.
- Numeração e gabaritos autorais preservados. Conferência dos 200 gabaritos detalhados com as duas tabelas de consulta rápida. A categoria por assunto é editorial, baseada nas Q34/Q41/Q42 citadas por item.
- Reutiliza `assets/curso.js` sem modificá-lo. O identificador `e1-banco-200` isola o armazenamento do banco dos módulos e bancos existentes. Não há inclusão das novas respostas na exportação geral do portal.
- A aula E1 recebe somente dois links e uma chamada para a nova página. Nenhum artigo antigo é editado; os demais módulos e o formulário são preservados.
- `gerar.py` permite reproduzir a importação com PyMuPDF a partir dos quatro PDFs locais. `inventario.json` registra fonte, página, alternativas, comentário, letra e hashes dos PDFs.

Esta entrega não declara revisão científica independente dos 200 cálculos, aplicação com estudantes, acessibilidade integral ou aprovação de QA-09. As afirmações de revisão interna nos PDFs pertencem ao material recebido e não constituem verificações realizadas nesta sessão.

## Verificação

Testes em Chromium real, desktop 1440×1000 e celular 390×844: correção certa/errada, refazer, persistência após recarga, filtros por assunto/volume/pendentes, busca e estado vazio. Nenhum erro JavaScript; sem transbordamento horizontal da página no celular. Sem JavaScript, os 200 artigos, tabelas e comentários continuam disponíveis. Referências locais e IDs únicos conferidos.

`node auditoria/termodinamica/inventario/validar-inventario.mjs`: `ok: true`, 197 artigos, 29 recursos, 1.263 vínculos locais, zero erros. A primeira execução apontou somente o hash da fonte alterado pelos links. A reconciliação atualiza apenas data, hash/snapshot da fonte e nota metodológica do inventário operacional, preservando integralmente seus registros por item e os snapshots históricos. `preservacao.json` prova igualdade byte a byte dos 197 artigos; `e1-snapshot.html` é a nova fotografia, sem substituir a anterior.

`git diff --check`: sem erros. O parecer independente delimita a revisão documental e funcional; QA-09 e a revisão científica dos novos cálculos permanecem abertos.

## Ajuste após revisão independente

Corrigido falso reconhecimento do esquema da Q75 como tabela: células ausentes distinguem o falso positivo da tabela de contadores. O importador também preserva desenhos fora das tabelas genuínas (Q39, Q42 e Q75), com tolerância nas bordas para não duplicar tabelas como figuras. São 50 tabelas HTML e 46 figuras na versão final.
