"""Substituições aprovadas por artigo. Requer a base exata; salva delta reproduzível."""
import hashlib
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[5]
BASE = ROOT / "auditoria/termodinamica/evidencias/BAN-07"
TARGET = ROOT / "modulos/e1-termodinamica.html"
before = TARGET.read_text(encoding="utf-8")
assert hashlib.sha256(before.encode()).hexdigest() == "0fc12a96fd30d366770a56c366fb61bc6a9fa7bd761e81fb40242a30f6dd78c7"
delta = json.loads((BASE / "corretor/propostas-materiais-r1.json").read_text(encoding="utf-8-sig"))["deltas"]


def add(item, old, new, why="Esclarecer modelo ou relacionar distrator a erro concreto conforme plano aprovado."):
    delta.append({"id": item, "antes": old, "depois": new, "ocorrencias": 1, "motivo": why})


add("q-e1-02", "Não há divisão por 100 nessa soma.", "Dividir 200 por 100 dá 2, uma razão sem unidade. Atribuir kPa a esse resultado não converte pressão manométrica em absoluta; a conversão exige somar as duas pressões.")
for letter, old, new, old_comment, new_comment in [
    ("A", "Refrigerante do evaporador.", "Água líquida, aquecida pelos gases que passam por fora dos tubos.", "A questão trata de caldeira, não do ciclo de refrigeração.", "Essa disposição coloca água dentro dos tubos e gases por fora, como na caldeira aquatubular. Na flamotubular, os gases quentes percorrem o interior dos tubos."),
    ("B", "Somente óleo lubrificante.", "Apenas vapor produzido, pois esses tubos funcionam como superaquecedores.", "Lubrificante não é o fluido de troca térmica principal descrito.", "Confunde os tubos pelos quais passam os gases com um superaquecedor, no qual circula vapor. Os tubos aquecedores da flamotubular contêm os gases da combustão."),
    ("D", "Ar medicinal purificado.", "Mistura de água e gases de combustão em contato direto.", "Não corresponde ao aquecimento de água pela combustão.", "Ignora a parede dos tubos que separa gases e água. A troca de calor ocorre através dessa parede, sem exigir mistura entre os dois fluidos."),
    ("E", "Água e vapor necessariamente.", "Combustível antes da queima, pois esses tubos alimentam os queimadores.", "Essa descrição corresponde à aquatubular.", "Confunde a tubulação que alimenta combustível aos queimadores com os tubos aquecedores. Estes recebem gases quentes depois da combustão, não combustível antes da queima."),
]:
    add("q-e1-24", f'<li data-letra="{letter}">{old}</li>', f'<li data-letra="{letter}">{new}</li>')
    add("q-e1-24", old_comment, new_comment)
add("q-e1-26", '<li data-letra="A">3.030 kJ/kg.</li>', '<li data-letra="A">3.060 kJ/kg.</li>')
add("q-e1-26", "Parte do valor final e ultrapassa o intervalo.", "Usar 3.000 + 0,30 × (3.000 − 2.800) = 3.060 kJ/kg parte da referência final errada e ultrapassa o intervalo. O incremento deve ser somado a 2.800 kJ/kg.")


def option(item, letter, old, new):
    add(item, f'<strong>{letter}.</strong> {old}</span>', f'<strong>{letter}.</strong> {new}</span>')


def comment(item, letter, old, new):
    add(item, f'<strong>{letter} — Comentário:</strong> {old}</li>', f'<strong>{letter} — Comentário:</strong> {new}</li>')


option("av-e1-08", "D", "160 °C.", "180 °C.")
comment("av-e1-08", "D", "Não há fundamento para duplicar o alcance.", "Calcular 20 + 2 × 80 = 180 °C trata o alcance como semiamplitude e duplica indevidamente o intervalo. O span já é a diferença completa entre os limites: basta somá-lo a 20 °C.")
option("av-e1-10", "D", "180 kg/m³ e extensiva.", "0,18 kg/m³ e extensiva.")
comment("av-e1-10", "D", "Multiplica grandezas que deveriam ser divididas e erra a classificação.", "O produto indevido 12 × 0,015 dá 0,18, mas sua unidade seria kg·m³, não kg/m³. A massa específica exige dividir massa por volume; também é falsa a classificação extensiva, pois essa propriedade é intensiva.")
comment("av-e1-17", "B", "A umidade relativa muda quando a pressão de saturação muda com a temperatura.", "Quantidade fixa de vapor não torna sua pressão parcial independente da temperatura. No modelo ideal, pv = nvRT/V; a volume fixo, aumentar T aumenta pv. A alternativa confunde quantidade fixa com pressão parcial constante.")
comment("av-e1-18", "A", "Duplica o resultado correto sem justificativa.", "Usar 450 − 300 = 150 K no denominador, em vez de T1 = 300 K, gera 200 × 450/150 = 600 kPa. A relação exige a temperatura inicial absoluta, não a variação de temperatura.")
add("av-e1-33", "Após a ruptura da membrana, analise os estados de equilíbrio inicial e final, desprezando alterações cinéticas e potenciais.", "Não há outros modos de trabalho nem interação energética relevante com a membrana. Após sua ruptura, analise os estados de equilíbrio inicial e final, desprezando alterações cinéticas e potenciais.")
option("av-e1-35", "A", "−240 kJ.", "−0,120 kJ.")
option("av-e1-35", "E", "+240 kJ.", "+0,120 kJ.")
comment("av-e1-35", "A", "Erra simultaneamente sinal e magnitude.", "Divide indevidamente 120 por 1.000, embora a energia já esteja em kJ, e ainda troca o sinal do trabalho realizado pelo sistema. O valor correto é +120 kJ.")
comment("av-e1-35", "E", "Duplica a variação sem motivo.", "Dividir 120 por 1.000 como se o dado estivesse em joules produz 0,120. O dado já está em kJ; essa conversão indevida reduz o trabalho por um fator mil.")
option("av-e1-37", "B", "1,5 kJ.", "5,37 kJ.")
comment("av-e1-37", "B", "Não corresponde ao trabalho perdido: 300 K × 0,20 kJ/K = 60 kJ. Dividir temperatura por entropia também seria dimensionalmente inválido e não produziria o valor desta alternativa.", "Converter 300 K para 26,85 °C e usar esse número na multiplicação dá 26,85 × 0,20 = 5,37. Gouy–Stodola exige a temperatura ambiente absoluta em kelvin; por isso a perda é 60 kJ.")
option("av-e1-38", "D", "20%.", "25%.")
comment("av-e1-38", "D", "A diferença de 200 K não deve ser dividida por um valor arbitrário de 1.000 K.", "Usar (500 − 300)/(500 + 300) dá 25%. O denominador de Carnot é a temperatura absoluta da fonte quente, não a soma das temperaturas.")
option("av-e1-45", "A", "100 kJ.", "333,3 kJ.")
comment("av-e1-45", "A", "Daria eficiência de 90%, acima do limite.", "Usar 1.000 × 300/(600 + 300) dá aproximadamente 333,3 kJ, por colocar a soma das temperaturas no denominador. Isso daria eficiência de cerca de 66,7%, superior ao limite de Carnot de 50%.")
option("av-e1-48", "E", "a temperatura seja medida exclusivamente em Fahrenheit.", "as duas correntes tenham a mesma temperatura em todo o regenerador.")
comment("av-e1-48", "E", "A condição física não depende da escala usada para expressar as temperaturas.", "Temperaturas iguais em toda a troca anulam a diferença térmica necessária à transferência passiva. Confundir equilíbrio térmico com a condição de funcionamento impede o aquecimento pretendido.")
add("av-e1-50", "Duas turbinas a gás são comparadas para as mesmas condições de entrada, mesma razão de pressões e mesma temperatura de entrada da turbina. Em relação ao modelo ideal isentrópico, as irreversibilidades tendem a", "Duas turbinas a gás são comparadas. Considere seus compressores e turbinas adiabáticos, em regime permanente, sem diferenças relevantes de energia cinética ou potencial. Compare trabalhos por unidade de massa: para cada componente, mantenha os mesmos estados de entrada e as mesmas pressões de saída ao comparar o equipamento real com sua referência ideal isentrópica. Nessas condições, as irreversibilidades tendem a")
old_solution = "O compressor real requer mais trabalho para a mesma elevação de pressão; a turbina real extrai menos trabalho para a mesma expansão. O trabalho líquido diminui."
new_solution = "Nas condições adiabáticas declaradas e para as mesmas referências de entrada e pressão de saída, o trabalho consumido por unidade de massa é wc = h2 − h1 no compressor e o produzido é wt = h3 − h4 na turbina. As irreversibilidades elevam a entalpia de saída relativamente à referência isentrópica: o compressor consome mais e a turbina produz menos. O trabalho líquido específico diminui. Essa comparação não estabelece mínimo irrestrito para compressores refrigerados."
delta.append({"id": "av-e1-50", "antes": old_solution, "depois": new_solution, "ocorrencias": 2, "motivo": "Sincronizar solução e comentário da chave com a classe térmica de comparação."})
option("av-e1-57", "C", "25%.", "0,50%.")
comment("av-e1-57", "C", "Aplica uma divisão adicional por 2 sem fundamento.", "Escrever a fração 0,50 diretamente com o símbolo % esquece a multiplicação por 100. A fração 0,50 corresponde a 50%, não a 0,50%.")
option("av-e1-58", "D", "800 kPa.", "300 kPa.")
comment("av-e1-58", "D", "Duplica indevidamente o resultado.", "300 kPa é o aumento p2 − p1 = 400 − 100. O comando pede a pressão absoluta final, 400 kPa, não o incremento de pressão.")
comment("av-e1-64", "C", "Isso corresponde ao princípio de equipamentos dinâmicos.", "Nos compressores dinâmicos, o rotor transfere energia ao escoamento e o difusor ajuda a converter energia cinética em pressão; não se deve atribuir esse fornecimento de energia a pás no difusor. Pistão e parafuso comprimem volumes aprisionados, por mecanismo distinto.")
for letter, old, new, old_comment, new_comment in [
    ("B", "ausência de superfície de contato térmico.", "baixa área de transferência de calor por unidade de volume.", "Transferência entre correntes e superfícies requer área disponível.", "Confunde pequeno volume externo com pequena área térmica. A compactação requer área elevada por volume; reduzir essa razão não explica a capacidade de troca pretendida."),
    ("C", "isolamento térmico completo entre todos os fluidos.", "grande volume de material para armazenar calor como definição de compactação.", "Isolamento completo impediria a troca desejada.", "Confunde transferência entre correntes com armazenamento térmico. Capacidade térmica do material não define a razão área de troca por volume que caracteriza a compactação."),
    ("D", "coeficiente de transferência necessariamente nulo.", "paredes necessariamente mais espessas para aumentar a condução.", "Coeficiente nulo eliminaria a capacidade de trocar calor.", "Para mesmo material e área, aumentar a espessura aumenta a resistência à condução. A espessura não é o critério de compactação e pode depender de requisitos mecânicos."),
    ("E", "redução obrigatória da área interna para zero.", "aletas com função apenas estrutural, sem aumento da área térmica.", "Contraria a finalidade de aumentar a área disponível.", "Ignora a função térmica das aletas, que ampliam a superfície disponível. Essa ampliação não garante sozinha desempenho ilimitado nem perda de pressão invariável."),
]:
    option("av-e1-73", letter, old, new)
    comment("av-e1-73", letter, old_comment, new_comment)

after = before
for row in delta:
    match = re.search(r'<article\b[^>]*\bid="' + re.escape(row["id"]) + r'"[^>]*>[\s\S]*?</article>', after)
    assert match, row["id"]
    original = match.group()
    count = original.count(row["antes"])
    assert count == row["ocorrencias"], (row["id"], row["antes"], count)
    changed = original.replace(row["antes"], row["depois"])
    after = after[:match.start()] + changed + after[match.end():]

expected = json.loads((BASE / "diagnostico-197-integrado-r1.json").read_text(encoding="utf-8"))["implementacao_proposta"]["artigos"]
assert set(row["id"] for row in delta) == set(expected)
TARGET.write_text(after, encoding="utf-8", newline="\n")
result = {"id": "BAN-07", "rodada": 1, "base_sha256": hashlib.sha256(before.encode()).hexdigest(), "resultado_sha256": hashlib.sha256(after.encode()).hexdigest(), "artigos": expected, "substituicoes": delta}
(BASE / "corretor/delta-artigos-r1.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"artigos": len(expected), "substituicoes": len(delta), "sha256_html": result["resultado_sha256"]}, ensure_ascii=False))
