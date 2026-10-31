# QA-09 — funções de placar e tempo e opções de navegador, r15

Data: 30/10/2026. Corretor: agente automatizado `/root/next_graphics`. **Aguardando Auditor independente.** A verificação cobre recortes de código compartilhado e os cálculos indicados abaixo, não altera produto e não aceita globalmente QA-09. O contexto de aprendizagem é externo aos 197 artigos; os acertos hipotéticos são marcadores sintéticos e não reavaliam os gabaritos.

## Identidade e apresentação

Aula r15 `modulos/e1-termodinamica.html`, SHA-256 `f6c461f1d6039ea47dc7e97f9ad734bb0ea3fcb902f01ffdbf18d18d88e08d0e`; inventário r15 SHA-256 `c8c9c3a3e141eba47a16e9f85c69f97c6e8b8a55aab689c6120ef1a0070c9d9c`. A aula carrega `assets/curso.js` SHA-256 `a20f4d19158073a9a1c48aabdfba8fa863b02063e16061c00b16448a6ccc2e13` e `assets/registro.js` SHA-256 `46da94527d6639fe0265bd766286f1ef39623966105e00bda3b31f21ca2c247c`. O registro contém 30 questões para o módulo E1 na pontuação inicial, separada dos bancos complementares, que dispõem de mecanismo próprio não examinado aqui.

Lendo o código e executando as funções reais `resumirEstado`, `progressoDoModulo`, `textoDoPlacar`, `textoTempoSimulado` e `formatarTempo`, extraídas sem modificar o arquivo de produto em contexto simulado:

* De 30 registros, cenário de três respostas, duas iguais às chaves e uma diferente: progresso e resumo geram 3 respondidas, 2 acertos; chave obsoleta fictícia fora do registro não soma. Em treino, `2/3×100=66,666…%` é exibido `67% das respondidas`, arredondamento para inteiro; com zero respostas, não exibe percentual.
* O relógio converte milissegundos em segundos inteiros por truncamento para baixo e limita negativos a zero; `59 999 ms` → `00:00:59`, `3 661 000 ms` → `01:01:01`, `360 000 000 ms` → `100:00:00`.
* No ramo simulado genérico, estado sem correção mostra marcações e tempo atual, com correção mostra acertos e tempo final; amostras de 4 minutos para duração 3 mostram tempo esgotado, e 1 minuto de simulado corrigido mostra 1 minuto. O teste usa relógio controlado e não pressupõe que a aula E1 acione este ramo.

O script de conferência, SHA-256 `6241e84be0060a5d96e9a1e1f5281013469ffb12134a1595f1f2167cedd8ec7e`, reproduz-se na raiz com `node auditoria/termodinamica/evidencias/QA-09/placar-tempo-js-r15-20261030/verificar.cjs`. Resultado observado `ok: true`, registro E1 30. A extração identifica funções por marcadores textuais, fixa os hashes dos arquivos e testa as funções do produto; armazenamento, estado e relógio são simulados.

## Disponibilidade de navegador local

Em 30/10/2026, `command -v` não encontrou `chromium`, `chromium-browser`, `google-chrome`, `google-chrome-stable`, `firefox`, `webkit2png` ou `wkhtmltoimage`. Busca limitada em `/opt`, `/usr/lib`, `/usr/local/share`, `/usr/bin`, `/usr/local/bin` e cache também não encontrou binário Chromium/Chrome/Firefox/headless shell. O pacote Playwright está instalado no runtime; `chromium.executablePath()`, `firefox.executablePath()` e `webkit.executablePath()` apontam a caminhos inexistentes. A pesquisa é limitada aos locais indicados; não afirma ausência em todo o sistema.

Alternativas locais disponíveis são análise HTML estática e execução JS em VM com DOM simulado, úteis para verificações parciais e já empregadas nos lotes, mas não fornecem renderização, interação real, fontes visuais, impressão, armazenamento de navegador, acessibilidade nem fluxo de ponta a ponta. Um executável de navegador compatível ou um ambiente de testes com navegador instalado ainda é necessário para a leitura real exigida no plano. Não foi tentado baixar navegadores nem conectar a uma sessão de usuário.

## Limites

Não houve navegador, CSS, verificação visual, teclado, leitor de tela, persistência real ou concorrência de abas. Não foram executados o carregamento integral e os manipuladores de eventos de `curso.js`; nem inspeção integral de `registro.js`, bancos complementares, simulado, progresso, filtro, acessibilidade, geração de digitais ou conteúdo científico. Dados do ensaio são fabricados para exercitar os cálculos, não evidência de aprendizagem ou de erro de estudante. Verificação independente e os passos restantes de QA-09 continuam pendentes.
