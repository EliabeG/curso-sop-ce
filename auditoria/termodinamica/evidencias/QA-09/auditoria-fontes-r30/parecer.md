# QA-09 — auditoria independente de fontes-r30

Data: 2026-10-30. Auditor: next_graphics. Objeto: `fontes-r30/entrega.md`, SHA-256 `35c2345e35a15174b2c0ea9739348977a58b4e6230a1e6882012364e94dc0be4`; verificador do autor `a9f61832d09c5105bb66317c7fd342ff0551c0b863203e95edf66d6e0211f399`. Foto r30 da aula `c719adae3464fb56ed2b0ad7014e0721c0aab2da444fb484ec0b40c5c0c8fbd4`, formulário `949c44fc5b96703929770b2881383d449af890616d34b9ab10b998ca96c75749`, inventário `1ce69fc1ab71850abc3ab8dc3df82b04e78788b9e62a55919c609a708a7979b4`.

## Parecer e independência

**Aprovada a rastreabilidade local no escopo declarado; confirmação externa independente parcial.** Os sete endereços e seus elementos correspondem à fotografia e ao inventário; as três fontes adicionais são material de apoio da evidência, e não referências vinculadas na aula ou no formulário. O conteúdo remoto inteiro e a disponibilidade atual dos dez endereços não foram confirmados independentemente nesta auditoria. O relatório original distingue suas próprias consultas e limitações; este parecer não transforma os relatos do autor em observação independente.

O Auditor deste parecer é autor da entrega `tabelas-r30` que contém as três fontes adicionais. Verificou aqui sua identificação e classificação como apoio; não emite novo aceite independente da própria análise científica ou dos próprios contramodelos. A entrega `fontes-r30` é de outro agente, reference_triage. Não houve alteração do produto.

## Reprodução local

Execute `python3 auditoria/termodinamica/evidencias/QA-09/auditoria-fontes-r30/verificar.py` a partir da raiz do repositório. O verificador independente, SHA-256 `6abb3102fdb1777f917f481f2f8a9f51fb3af59f83abfcd79cf3bfe949f52c4c`, confronta hashes, inventário, offsets UTF-16, elementos e URLs na aula congelada, extraindo `href` com decodificação HTML. `resultado.json`, SHA-256 `77a4fe1d81ae1d4632138e79d84b9da24e8d11fd014bbefecd5761ccfbc698fc`, registra sucesso e os sete hashes individuais. Também identifica as três URLs adicionais no relatório de tabelas e verifica ausência no inventário de referências de aula e formulário. A integridade local não prova disponibilidade ou correção científica das páginas.

## Conferência externa e limites

As consultas a seguir usaram resultados indexados oficiais, não necessariamente uma abertura atual da página ou PDF integral:

* IUPAC [C01032](https://goldbook.iupac.org/terms/view/C01032/html): o índice oficial apresenta o verbete de potencial químico e a derivada de Gibbs. [C01023](https://goldbook.iupac.org/terms/view/C01023): o índice oficial identifica o verbete de equilíbrio químico e sua definição. O autor registrou resposta HTTP 403 na tentativa direta; nesta revisão as tentativas da ferramenta de consulta falharam sem retornar código HTTP. Portanto 403 é uma limitação de acesso observada pelo autor, não prova de link quebrado e não foi reproduzida independentemente aqui.
* [MIT 2.43, aula 09](https://ocw.mit.edu/courses/2-43-advanced-thermodynamics-spring-2024/ocw_243_lecture09_2024mar05_v2_transcript.pdf): índice oficial identifica o recurso e a disciplina de 2024; não reproduzimos a abertura direta da transcrição nem conferimos integralmente as afirmações do autor sobre seu conteúdo nesta revisão.
* [MIT Unified, node17](https://web.mit.edu/16.unified/OldFiles/www/FALL/thermodynamics/notes/node17.html): consulta direta anterior nesta sessão mostrou o contexto da primeira lei e exemplo de válvula; não garante acesso presente ou revisão integral.
* Apoio [transcrição MIT 8.333](https://ocw.mit.edu/courses/8-333-statistical-mechanics-i-statistical-mechanics-of-particles-fall-2013/8a857cba1c051ac073a8c9d106dc7501_l2Q31eoy_rY.pdf): índice oficial consultado anteriormente nesta sessão apresenta discussão de van der Waals e parâmetros de exclusão de volume e atração. A extração indexada contém ruído, não substitui leitura direta do trecho integral; a ressalva do autor permanece.
* NISTIR 5078, NIST WebBook de amônia, NASA `realspec`, NASA equação de estado e artigo NIST 905791: identidade local e relato do autor examinados, mas nossas tentativas adicionais de pesquisa externa retornaram falha de serviço sem conteúdo. Não confirmamos independentemente o conteúdo remoto nem refutamos a consulta documentada pelo autor. O applet NASA e dados numéricos das tabelas não foram ensaiados neste parecer.

Resultado limitado a sete vínculos identificados e três fontes adicionais; não é auditoria das demais referências, de todas as equações do curso, da funcionalidade de um applet, nem aceite científico global. Recomenda-se repetir consulta direta quando o serviço permitir, preservando o histórico e sem classificar respostas 403 como links inválidos.
