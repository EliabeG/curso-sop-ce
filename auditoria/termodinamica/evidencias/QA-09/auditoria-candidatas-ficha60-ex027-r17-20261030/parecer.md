# QA-09 — auditoria independente das candidatas ficha 60 e EX-027, r17

30/10/2026. Auditor automatizado `/root/next_graphics`, distinto do Corretor `/root/next_formulas`. **APROVADAS como propostas isoladas no alcance abaixo; não aplicadas.** Não se aprova a futura aplicação ou QA-09 integral.

## Identidade e preservação

Análise examinada SHA `d1024614357975aca67b041e08c40ecea1458ac9ed3adeb863428d3e5e43196e`, manifesto `4a61b863e2acfe76c043d58322e695ad2139653199240737b56ed0c5c70c1c92`, programa do Corretor `7a1b6ac85a6509b374731f64537d9dcb83d4df35fda83ec53b67fb3976589e4a`. A fotografia fixa aula `6b0df1096d0b6de6995ffc51bf8489cb45ab954a7aabdeb3f48d068c9777c57c`, formulário `dea4923117d09fa77cabacb0b65816cbf6d57b724d88285003804a1f1440389d`, inventário `b8eae39cc72cf807d7b84aad7e7a38423168b809231bc3b7f08c439d6d25163b`.

Comparei os dois fragmentos originais, os candidatos e os deltas manifestados. Na ficha 60 mudam somente condição e legenda, cada qual replicada em `data-busca`; no EX-027 muda somente o enunciado. MathML de ambos permanece idêntico. Na simulação, reverter cada fragmento candidato recupera integralmente os bytes do documento original. Os documentos hipotéticos têm SHA `463c00149e36217404cf98bad4f5bed3db828c87d19d1c8e6038678193e9d895` (formulário) e `36d46e4d240a5a79732faac3d7d2a7a0eab813ca01ac8cb3dd9d16552bb51f53` (aula). O teste do Corretor também passou para 99 fichas não alvo, 197 artigos e 191/734 MathML.

## Ficha 60

O cartão explicita mesmo ciclo/fronteira/período, trabalho líquido total recebido positivo, os dois calores e ausência de outras interações relevantes. Assim, na aproximação em que as demais interações são desprezadas, `QH=QL+Win`, `COPR=QL/Win` e `COPBC=QH/Win=COPR+1`. Exige denominador não nulo e mesma base de energia. A nova legenda identifica QH e QL como magnitudes e Win como trabalho **líquido**, sem interpretá-lo como potência elétrica ou de um único acionamento bruto.

No contraste fictício, 100 kJ entrando e 20 kJ saindo dão Win=80; com QL=300 e QH=380, `COPR=3,75` e `COPBC=4,75`. Se as fontes estão a 300 K e 350 K, `Sger=380/350−300/300=3/35 kJ/K>0`, portanto o balanço ilustrativo não viola as duas leis. Dividir QH pela entrada bruta 100 dá 3,8, outra razão que não obedece à identidade pretendida. Não é uma instalação medida.

## EX-027

A candidata identifica ciclo, calor total de entrada 1000 kJ, rejeição total 600 kJ e trabalho líquido como única outra transferência. ΔE=0 para o ciclo, logo W=400 kJ e η=400/1000=40%, preservando os valores e a solução. Isso verifica balanço de primeira lei; a viabilidade pela segunda lei não pode ser concluída sem temperaturas e demais condições.

O contraste da entrega, de dois calores de entrada de 1000 e 200 kJ e rejeição de 600 kJ, fornece W=600 kJ; a 800, 600 e 300 K, `Sger=600/300−1000/800−200/600=5/12 kJ/K>0`. A nova redação exclui o aporte extra. É exemplo nominal, não prova de realização de um equipamento. As [notas MIT sobre refrigeradores](https://web.mit.edu/16.unified/OldFiles/www/FALL/thermodynamics/notes/node25.html) e [primeira lei](https://ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_4.htm), reabertas em 30/10/2026, apoiam os modelos, não os números fictícios.

## Rastreio e limites

A análise registra que dois auditores gravaram versões de parecer no mesmo caminho e a anterior não ficou preservada; uma reavaliação posterior sob nome exclusivo existe, mas não permite reconstruir a versão perdida. Esta auditoria julga o conteúdo efetivo das candidatas e o parecer disponível, sem afirmar recuperação desse histórico.

`python3 auditoria/termodinamica/evidencias/QA-09/auditoria-candidatas-ficha60-ex027-r17-20261030/verificar.py` passou; SHA `7b711939d5f834f216ea3c0a5bdf0bd08e0d81505a136882fb81c90f93a45495`. O programa verifica hashes, offsets, reconstrução, preservação MathML e contramodelos em frações exatas, sem gravar produto. Não houve navegador, leitor de tela, estudantes ou revisão humana. A aplicação, se realizada, exige nova fotografia, reconciliação dos efeitos e Auditor distinto.
