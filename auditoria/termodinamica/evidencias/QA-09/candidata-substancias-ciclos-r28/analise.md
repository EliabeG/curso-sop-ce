# QA-09 — candidatas isoladas para substâncias e ciclos, fotografia r27

30/10/2026. Corretor `/root/next_graphics`. **NÃO APLICADAS, aguardando Auditor independente `/root/planning`.** Responde ao parecer `auditoria-substancias-r28/parecer.md` SHA-256 `8d60a5559fe8dea5147e20dceb19ecdfb45a7fc1a88782f8be444e891e804d6e`. Eu produzi a triagem que originou o parecer; `/root/planning` auditou o achado independentemente. Não altera produto ou controle, não conclui QA-09.

## Propostas e preservação

1. **Substâncias** — no contêiner da tabela, a introdução passa a restringi-la a estados fluidos de equilíbrio, pressão com coexistência líquido–vapor, fora do crítico e excluídas regiões sólidas/outras transições. No texto posterior, explicita que p e T em coexistência não distinguem líquido, vapor e frações intermediárias; pede propriedade independente adequada ou fração de fase e remete ao diagrama e modelo fora do domínio. No crítico o título não se aplica. As linhas e todos os MathML da tabela permanecem em bytes, incluindo x=0 e x=1 como limites e 0<x<1 quando as duas fases coexistem.
2. **Otto/Diesel** — a frase no mesmo contêiner dos modelos ar-padrão explicita gás ideal de composição fixa e calores específicos constantes nas expressões fechadas; seus textos, tabela e MathML permanecem. A condição já é uma convenção adotada em certos usos de ar-padrão: esta alteração é esclarecimento, não alegação de que as fórmulas estavam erradas no modelo constante. O contramodelo de c_v(T) variável com composição fixa, descrito em `graficos-r28-lote2/entrega.md`, permanece fora do domínio proposto.

Os valores físicos de contraste e os limites são discutidos nas fontes [IAPWS](https://iapws.org/faqs/faq1), [NIST](https://www.nist.gov/publications/thermodynamic-analysis-and-experimental-study-effect-atmospheric-pressure-ice-point) e [MIT 16.050](https://ocw.mit.edu/courses/16-050-thermal-energy-fall-2002/75666f9248981634a704fdf257ef529a_07_part2a.pdf); não são dados fictícios adicionados à aula. Em particular, água a 1 atm e −10 °C ilustra por que se excluem regiões sólidas, e acima da pressão crítica não se aplica T_sat líquido–vapor.

## Identidade e reprodução

Aula r27 `9af8e2c9ffe509e40594d086a9ef4ad75127fb4ca873efb305d3144e08f3fc49`; inventário r27 `a58d7f0b0a5f097eef83ad83026ef49e801457b87f7cf2b2345c3dd915597c7c`; manifesto `manifesto.json` SHA `536c06caca6923b0e431995fefb682bd196bc1ab95cf75c5ad2bd2cb5db60be6` registra dois intervalos disjuntos, três substituições e os hashes exatos dos fragmentos. Os arquivos individuais de trecho têm quebra terminal que não integra os hashes do manifesto.

`python3 auditoria/termodinamica/evidencias/QA-09/candidata-substancias-ciclos-r28/verificar.py`, SHA `611d15935b0712df9a96c4dc054837aed9b3b083fd5094a4908dad9ddbeb334d`, passou, somente leitura. A recomposição em memória preserva os 197 artigos da aula, 734 MathML e atributos ID/href/src/ARIA comparados; o formulário não é objeto de alteração. A aula combinada hipotética tem SHA `876e05056e5aa380ffc4d48247ff354510f9d237afb4c26ef67e3c82b81aa649`. Os novos subscritos textuais em Otto/Diesel poderão criar ocorrências adicionais no inventário; não assumo mapa sem reconstrução e auditoria da aplicação efetiva.

A proposta exige parecer científico e estrutural independente antes de eventual aplicação e revalidação localizada; teste automático não comprova apresentação, leitor de tela, aprendizagem ou revisão humana.
