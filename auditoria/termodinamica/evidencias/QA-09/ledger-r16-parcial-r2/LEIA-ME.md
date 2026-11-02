# QA-09 — ledger parcial r16, revisão 2

30/10/2026. Autor `/root/planning`. **Aguardando auditoria independente desta integração r2.** Não altera a r1 ou outros ledgers, nem conclui QA-09. Preserva os oito registros da r1, cujo parecer independente está fixado, e adiciona apenas D11–20 após leitura e recálculo em r16, com contexto e alcance individuais descritos em [reconciliação](reconciliacao-d11-20.md). As quatro coleções têm padrão `pendente_de_integracao`; todos os itens fora dos 18 registros listados seguem pendentes, sem apagar avaliações históricas. Nós pais, filhos, bases, fontes e recursos não recebem aprovação automática.

Os dez diagnósticos têm parecer histórico independente r12 e revalidação específica r16; as bases ligadas foram confrontadas. A base Brayton sofreu mudança, examinada na reconciliação com apoio do parecer de aplicação r16. Os 11.400 registros estruturais, 816 referências, 138 relações de recursos e seis ativos se sobrepõem e não representam porcentagem científica. Os 197 artigos são tratados separadamente.

O script emite JSON somente em stdout e pode verificar a fotografia já salva:

```sh
node auditoria/termodinamica/evidencias/QA-09/ledger-r16-parcial-r2/ledger.mjs --verificar auditoria/termodinamica/evidencias/QA-09/ledger-r16-parcial-r2/ledger.json
```

Ele fixa a r1 e seu parecer independente e reconstrói sua saída; fixa snapshot e inventário r12, inventário, aula e formulário r16 via gerador r1, parecer histórico, parecer r16, reconciliação e parser. Checa os dez recortes, bases e cálculos selecionados. O script não acessa referências remotas, não substitui leitura nem validação científica independente. Qualquer mudança nas entradas exige nova fotografia e reavaliação. Verificação positiva e teste negativo de adulteração do estado foram realizados. Nenhuma evidência de navegador real, estudantes, revisão humana ou certificação externa é alegada.
