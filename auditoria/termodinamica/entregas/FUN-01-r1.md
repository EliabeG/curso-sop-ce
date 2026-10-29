# FUN-01 r1 — Estado, equilíbrio e graus de liberdade

**Entrega do Corretor, congelada para auditoria.** Data: 27/10/2026. Não declara aprovação do item nem do curso. Único ID trabalhado: FUN-01.

## Resultado concreto

Publicada a unidade **3.1** em [E1](../../../modulos/e1-termodinamica.html#fun01-estado-equilibrio), com acesso pelo sumário, recuperação, desenvolvimento conceitual, exemplos de decisão, quatro problemas abertos, soluções recolhidas e rubricas de 10 pontos. A página explica que a correção aberta usa rubrica, sem pontuação automática no painel de questões.

| Aceite | Evidência publicada |
|---|---|
| Objetivos observáveis e pré-requisitos | fun01-objetivos; fun01-entrada, com recuperação de base específica/molar, unidades e intervalos; preparação adicional para log e derivadas na bancada. |
| Equilíbrio térmico/mecânico/químico/de fases | fun01-equilibrio; distinção entre reação e transferência; fun01-preparacao-equilibrio ensina μ intrínseco/total, F em T,V fixos e estabilidade. |
| Estado simples compressível e independência | fun01-independencia: composição fixa, pares redundantes/suficientes, teste algébrico e Jacobiano local, condições de unicidade. |
| Composição e graus de liberdade | fun01-fases: derivação de Gibbs, fases versus quantidades, título puro, mistura binária, bases molares/mássicas, limites de Raoult/Dalton. |
| Saturação, misturas e supercrítico | problemas 1–3: dados redundantes/incompatíveis; seleção de regime e composições; garantia por dois limites críticos estritos. |
| Exemplo resolvido com decisões | Gás ideal(T,u)/(T,p); água saturada e dado redundante; contraste de composição/bolha; reservatórios com pressão parcial igual; mini parecer v/ρ. |
| Exercícios originais independentes | Quatro casos completos abaixo; inventário distingue relações temáticas, dados de referência compartilhados e subcomponentes de fixação. Não se promete ineditismo universal. |
| Soluções e rubricas | Cada article contém solução comentada, 10 pontos, erros críticos e referência de progressão≥ 8; problema 4 explicita mínimos adicionais. |
| Fontes e versão dos dados | NISTIR5078/1998, IAPWS R7-97(2012), fontes universitárias/primárias nos trechos; pacote E1-FUN01 v1.0 diferencia dados de referência de modelos fictícios. |
| Reprodução numérica | fun01-calculos-v1.mjs exporta calcularFun01(dados), 28 verificações; conferência separada do coordenador. |
| Matriz C01–C10 delimitada | Atualizadas somente células C01/C02/C07/C08/C09/C10; ligações aula→atividade, alcance parcial e lacunas remanescentes. Incluído ensino de parecer para avaliação escrita parcial C10. |

## Novos instrumentos

- **fun01-e1-saturacao:** tanque com V/m e entalpia conflitante; classificar pares, inferir título, comparar intervalos e propor observação independente sem acusação causal indevida. Estimativa intermediária.
- **fun01-e1-mistura:** quatro lotes binários ideais; escolher fases, rejeitar β inviável, fechar balanços, construir estados compatíveis quando z falta e distinguir β molar de título. Estimativa avançada dentro do modelo delimitado.
- **fun01-e1-supercritico:** quatro registros de água; limites determinísticos, melhorias isoladas/conjuntas e margem estrita, qualidade indefinida e redundância ρ/v. Estimativa intermediária.
- **fun01-e1-equilibrio:** coluna hidrostática com dados incompatíveis e duas células com membrana seletiva; comparar potenciais com gravidade, resolver estado final, testar estabilidade sob restrições e redigir parecer. Estimativa avançada dentro das hipóteses declaradas.

## Preservação e verificações

[verificacao-final-r1.json](../evidencias/FUN-01/verificacao-final-r1.json) registra 239 verificações aprovadas pelo script documental: os 190 artigos originais são idênticos; os 190 registros também; retirada da seção/menu e reversão das seis linhas permitidas da matriz reconstroem o HTML anterior byte a byte. Não houve mudança em registro.js, curso.js, curso.css, schema, validador ou guia do inventário. Controle e checklist principal não foram editados pelo Corretor.

[validacao-inventario-r1.json](../evidencias/FUN-01/validacao-inventario-r1.json): 194 registros/194 artigos, 8 recursos distintos e 1042 verificações de links locais, zero erros/avisos. Nove tabelas novas usam o padrão responsivo existente, caption, scope e rótulos de células. Âncoras da unidade presentes e IDs únicos.

[calculo-r1.json](../evidencias/FUN-01/calculo-r1.json) e [calculos-coordenador-r1.json](../evidencias/FUN-01/calculos-coordenador-r1.json) concordam nos quatro casos. Dados/código não mudaram depois dessa conferência. [Conferência científica do Corretor](../evidencias/FUN-01/conferencia-cientifica-r1.md) explicita fontes e limites; não é parecer do Auditor. Git não estava no PATH deste processo: a preservação foi comprovada por comparação integral e SHA-256, sem depender de diff de Git.

Coordenador inspecionou a versão de interface anterior ao último parágrafo químico, incluindo navegação, abertura das quatro soluções e tabelas em viewport observado 699×599; nenhum erro de console foi reportado. Uma checagem focada da versão congelada será anexada pelo coordenador em evidência separada. Não houve piloto com estudantes nem alegação de cobertura de todos os tamanhos de tela.

## Congelamento e autoria

[manifesto-r1.json](../evidencias/FUN-01/manifesto-r1.json) lista os cinco arquivos alterados/novos de produto/inventário e suas cópias imutáveis em pacote-r1. Snapshot anterior do HTML/inventário/resumo preservado no diretório FUN-01; pacotes BAN-02 r1/r2/r3 permanecem intactos.

| Arquivo | SHA-256 congelado |
|---|---|
| modulos/e1-termodinamica.html | `cacda8c7742eead77aa1e92021b01c085c1b7340201d5cca0ada8ff743a8b04f` |
| assets/termodinamica/fun01-dados-v1.json | `a73b4d6140219cbd6b005216bb7a44db0a68b05f21ca51b7ac4b1ca782dd1448` |
| assets/termodinamica/fun01-calculos-v1.mjs | `a0fbdc4e6e7291a563db2362d26f4107ad67f56843e741d96eef8eea5a8d2a88` |
| auditoria/termodinamica/inventario/inventario-questoes.json | `4b18b397b68b9a46aae4db4c526d7bc2e4712df0e65b33359ba414fc6112e4df` |
| auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md | `5242d53447dc9441109586d448793c324596745e2017546a19cb39ff5b854725` |

Corretor: autoria da unidade geral, problemas 1–3, integração, inventário e verificação. Apoio_fun01: preparação específica e problema 4, integrados/revistos pelo Corretor. Coordenador: fontes complementares, cálculo independente e navegador. **Revisão independente: pendente com auditor_aaa.**

## Limitações e gate

As competências são parcialmente avaliadas. A unidade não conclui GOV-02, BAN-03/04/05/07/08, PROP, MIX ou os demais FUN. Não oferece biblioteca completa de propriedades, modelo real de mistura, reação quantitativa, inferência probabilística nem avaliação empírica de aprendizagem. Não altera os gabaritos dos 190 itens anteriores.

O inventário mantém a revisão dos quatro novos itens como pendente até o parecer formal. Não avançarei para outro ID sem aprovação independente e liberação explícita do coordenador.
