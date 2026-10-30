# Preparação de aplicação combinada — QA-09

Preparado em 30/10/2026 pelo agente automatizado `/root/qa_teoria`. **Aplicação realizada:** a fotografia e os resultados estão em `entrega-r1.md`. O programa exige liberação da coordenação depois dos pareceres r7 e da aprovação das candidatas; os resultados precisam ser examinados por Auditor independente. O nome histórico desta pasta não limita os pares que ela pode receber.

`aplicar-r1.mjs --apply <configuração.json>` recebe objeto `{"edicoes":[...]}`. Cada entrada exige `id`, `original`, `candidata`, `original_sha256` e `candidata_sha256`; os caminhos são relativos à raiz, e os SHA-256 são do texto do fragmento sem a única quebra de linha final, não do arquivo com quebra. Confere hash da aula r7 e do inventário r7, presença única de cada original, ausência da candidata, não sobreposição, integridade dos 197 artigos e registros, e rejeita arquivos de saída já existentes. Depois faz substituição e cria fotografias, atualiza apenas a fonte do inventário oficial, gera r8 e um mapa r7→r8 e executa o validador. Faz alterações em vários arquivos sequencialmente e **não é transacional**: execute após criar cópia de segurança e verifique o resultado antes de qualquer publicação. Nunca sobrescreva evidência existente ao tentar novamente.

O mapeador compara ordem, documento, tag, tipo, seção, âncora, posição fora dos blocos, 815 referências e 138 registros de recursos; hashes do próprio E1 nos recursos são confrontados com as duas fotografias. Para ocorrências dentro dos blocos substituídos, associa apenas por ordem e contexto e marca que precisam de exame individual. Hash igual não transfere aceite, e a revalidação localizada de BAN-02/07/08 e FUN-01 fica a cargo do Auditor. Os parâmetros, candidatas e configuração devem ser examinados novamente no instante da aplicação.

Ensaio executado em cópia isolada da fotografia r7, sem alterar a versão de trabalho: a candidata percentual e dois blocos fictícios adicionais foram aplicados; o mapeador apresentou 11.396 pares, 815 referências, 138 recursos, 197 artigos preservados e seis hashes diferentes. Validador retornou `ok=true` para 197 itens, 29 recursos e 1.263 links. Isso é um teste do mecanismo, não das outras candidatas. Para repetir, crie uma cópia integral descartável (inclusive links e ativos), entre nela e execute:

```sh
python3 auditoria/termodinamica/evidencias/QA-09/aplicacao-razao-percentual-r1/preparar-ensaio.py --copia-descartavel
node auditoria/termodinamica/evidencias/QA-09/aplicacao-razao-percentual-r1/aplicar-r1.mjs --apply auditoria/termodinamica/evidencias/QA-09/aplicacao-razao-percentual-r1/ensaio-config.json
```

Os dois blocos com `[ensaio isolado]` são deliberadamente artificiais e não devem integrar o curso ou o controle. Não se recomenda executar em uma pasta com saídas anteriores. A execução não testa navegador, aprendizagem ou exatidão de todas as referências externas.
