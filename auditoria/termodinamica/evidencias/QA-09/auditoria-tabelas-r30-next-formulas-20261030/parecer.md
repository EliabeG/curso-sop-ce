# QA-09 — auditoria independente das tabelas e modelos de gás r30

30/10/2026. Auditor `/root/next_formulas`. **APROVADO NO RECORTE ALGÉBRICO E DE IDENTIDADE**, com fontes externas não revalidadas nesta sessão. Não se trata de aprovação de todas as tabelas, bibliografia ou ciência da aula. Vínculo anterior: fui autor de revisão de fichas 01–22, incluindo a 16, e auditei quatro figuras na r27; o presente parecer não reivindica que esses trabalhos sejam reavaliados por autor independente de si próprio.

## Identidade e alcance

Entrega `tabelas-r30/entrega.md` SHA-256 `5a19f59166c38e86c115c6c4fb034b76073eb136aa2d7905cf28b978f8546d30`; `resultado.json` `e2a6e4cd7254875d8e642ce07aa2a60d01d4e42a63b8131a852bf5190caa3f30`; `verificar.py` `e64c956ec2f08405b934af9229e318a02407d1b1e0db445167c16f376294b9c8`. Foto da aula r30 `c719adae3464fb56ed2b0ad7014e0721c0aab2da444fb484ec0b40c5c0c8fbd4`; inventário `1ce69fc1ab71850abc3ab8dc3df82b04e78788b9e62a55919c609a708a7979b4`. Executei o verificador de leitura e comparei sua saída integral com o JSON por `diff`: idêntica, código 0. Ele confere os três recortes de tabelas e dois blocos de gás, além dos cálculos declarados. Li também o conteúdo efetivo e as hipóteses imediatamente anteriores às tabelas; existência de hash não prova a adequação do texto nem a semântica das equações.

## Avaliação localizada

- **Notação:** calor/trabalho totais Q/W, específicos q/w, taxas em kW=kJ/s, u/h e v por massa e s em kJ/(kg K) estão coerentes com a convenção local. A tabela distingue a variável s de entropia específica do índice s de estado isentrópico.
- **Equilíbrio:** a tabela e o bloco anterior diferenciam regime permanente de equilíbrio sujeito a restrições; pressão uniforme não é imposta em presença de forças de corpo ou capilaridade. A igualdade do potencial químico da mesma espécie entre fases vale sob as condições indicadas e troca permitida; equilíbrio de reação interior exige Σνiμi=0. Não há implicação de igualdade entre potenciais de espécies distintas nem de que uma tabela diagnostique equipamento real.
- **Processos:** o bloco anterior limita a massa fixa de gás ideal, trabalho apenas de fronteira, ΔEC/ΔEP desprezíveis e capacidades constantes, com trabalho quase estático e reversibilidade adicional para a adiabática. Nesse alcance, W=0 em volume fixo, Q=mcₚΔT a p constante, ΔU=0 em isotérmica e pVᵏ constante na adiabática reversível conferem. Para os segmentos 300 e 100 kPa com ΔV=2 m³, os trabalhos são 600 e 200 kJ respectivamente. O verificador registra a diferença de 200 kJ de um ciclo separado; a conferência dos dois caminhos acima é minha conta adicional.
- **Gás e Z:** 1×0,287×300/0,861=100 kPa; usando 90 kPa com os demais dados, Z=90/100=0,9. Z=1 no modelo ideal não significa que todo estado real com Z=1 tenha todas as propriedades e derivadas ideais. O texto efetivo diz que Z=1 no modelo ideal e não formula a recíproca global. A recomendação de clareza da entrega é proporcional ao que foi observado.

## Contramodelo independente e fontes

Para p=RT/(v−b)−a/v², u=cvT−a/v, R=1, a=2, b=1, cv=1, v=2 e T=1 em unidades coerentes, recalculei com frações exatas: p=1/2, Z=pv/(RT)=1, (∂p/∂v)T=−1/2 e (∂u/∂v)T=a/v²=1/2. A identidade de equilíbrio T(∂p/∂T)v−p também dá 1/2, coerente com a derivada de u. Tc=8a/(27Rb)=16/27<T, cv=1 e cp=3 no ponto; ele não é ramo mecanicamente instável. Isso é modelo sintético, não propriedade medida de substância real. Contrasta Z pontual com dependência de energia em volume sem generalizar a partir do exemplo.

As fontes NASA, NIST e MIT listadas na entrega são apresentadas ali com ressalva de acesso; não se diz que NASA e material MIT de equilíbrio foram integralmente reabertos nessa rodada. Nesta auditoria tentei abrir NASA, NIST e MIT e também executar busca: a ferramenta externa retornou erro sem conteúdo, portanto **não confirmei independentemente acessibilidade, identidade ou suporte dos documentos**. O parecer aprova a análise algébrica acima, não as fontes. As hipóteses e equações foram avaliadas diretamente nos artefatos; uma verificação externa futura permanece separada.

## Limites

O script não valida automaticamente qualidade científica, modelo físico, navegador, apresentação visual ou leitor de tela. O contramodelo não é aceitação de equação de estado para um fluido real. Não houve estudantes, revisão humana ou certificação externa. Nenhum HTML, controle ou evidência examinada foi modificado; QA-09 permanece aberto.
