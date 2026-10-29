"""Memória de conferência da releitura dos25artigos; não é parecer independente."""
import hashlib
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[5]
BASE = ROOT / "auditoria/termodinamica/evidencias/BAN-07"
diagnostic = json.loads((BASE / "diagnostico-pos-correcao-197-r1.json").read_text(encoding="utf-8"))
mapping = json.loads((BASE / "mapa-identidades-r1.json").read_text(encoding="utf-8"))
changed = {r["id"] for r in mapping["registros"] if r["artigo_alterado"]}

# Expressões numéricas resultam das demonstrações relidas, não da alternativa correta extraída.
numeric = {
    "q-e1-02": (200 + 100, "200+100", {"D": (200/100, "200/100: razão indevida sem unidade")}),
    "q-e1-09": ((200-100)*(3-1), "Área horária(200−100)(3−1)=200kJ", {}),
    "q-e1-15": ((1000-650)/1000*100, "(1000−650)/1000×100", {"C": ((1000+650)/1000*100, "Soma indevida dos fluxos")}),
    "q-e1-16": ((1-300/600)*100, "(1−300/600)×100", {"D": (600/300*100, "Razão invertida e sem complemento"), "E": ((600-300)/(600+300)*100, "Soma indevida das temperaturas no denominador")}),
    "q-e1-19": (400/500*100, "400/500×100", {"C": (400/(400+500)*100, "Soma indevida das quedas no denominador")}),
    "q-e1-26": (2800+30/100*200, "2800+0,30×200", {"A": (3000+.3*(3000-2800), "Referência final indevida")}),
    "q-e1-28": ((3200-2400)/(3200-2200)*100, "(3200−2400)/(3200−2200)×100", {"B": (2200/3200*100, "Razão de entalpias de estado em vez de quedas")}),
    "av-e1-08": (20+80, "LS=LI+span=20+80", {"D": (20+2*80, "Span confundido com semiamplitude")}),
    "av-e1-10": (12/.015, "ρ=m/V=12/0,015", {"D": (12*.015, "Produto em vez de razão; unidade e classificação indevidas")}),
    "av-e1-18": (200*450/300, "200×450/300", {"A": (200*450/(450-300), "ΔT em vez de T1 absoluta")}),
    "av-e1-35": (120, "W=−ΔU=+120kJ", {"A": (-120/1000, "Conversão indevida e sinal invertido"), "E": (120/1000, "Conversão indevida de valor já em kJ")}),
    "av-e1-37": (300*.20, "T0Sger=300×0,20", {"B": ((300-273.15)*.20, "Temperatura Celsius no produto que exige kelvin")}),
    "av-e1-38": ((1-300/500)*100, "(1−300/500)×100", {"D": ((500-300)/(500+300)*100, "Soma indevida no denominador")}),
    "av-e1-45": (1000*300/600, "Qfria mínimo=1000×300/600", {"A": (1000*300/(600+300), "Soma indevida no denominador")}),
    "av-e1-57": ((1-1/2)*100, "(1−1/2)×100", {"C": (1-1/2, "Fração0,50 rotulada como% sem multiplicar100")}),
    "av-e1-58": (100*.20/.05, "p2=p1V1/V2=100×0,20/0,050", {"D": (100*.20/.05-100, "Incremento de pressão confundido com pressão final")}),
}
conceptual = {
    "q-e1-13": "Vetor(F,V,V): calor/trabalho dependem do caminho; h=u+pv define entalpia; U retorna no ciclo. C(IIeIII) é a única combinação completa. As cinco combinações finais são refutadas individualmente.",
    "q-e1-18": "Vetor(V,F,V): entropia isolada pode aumentar; adiabático irreversível não implica isentrópico; parte de um sistema pode perder entropia. SomenteD(VFV) corresponde ao vetor.",
    "q-e1-24": "Caldeira flamotubular conduz gases quentes dentro dos tubos e água ao redor. A troca com aquatubular, a identificação de superaquecedor, a mistura direta e a alimentação de combustível representam quatro erros distintos; C permanece única.",
    "av-e1-17": "φ=pv/psat(T); φ=0,5 implicaD. Quantidade de vapor fixa não fixa sua pressão: pv=nvRT/V no modelo ideal. A referência de volume fixo é contraexemplo à independência universal de T, não dado acrescentado à pergunta.",
    "av-e1-33": "Q=0; Wfronteira=0 por recipiente rígido e expansão contra vácuo; outros trabalhos e energia da membrana explicitamente excluídos. ΔU=0 dá ΔT=0 no gás ideal. ΔS=mRln(Vf/Vi)>0. I,II,III verdadeiras; IV falsa; somenteD.",
    "av-e1-48": "Para aquecer passivamente o ar comprimido, exaustão precisa ser mais quente na entrada do regenerador; A. Mistura não é obrigatória, compressão mantém consumo, sentido inverso não aquece como pedido e igualdade térmica em todo equipamento elimina força motriz.",
    "av-e1-50": "Adiabatismo e regime permanente dão wc=h2−h1 e wt=h3−h4 por massa, EC/EP desprezíveis. Para entrada e pressão de saída iguais, geração de entropia eleva h de saída em relação à referência isentrópica (dh=Tds a p fixa e T>0). Assim wc sobe e wt cai; C. O enunciado final exclui compressor resfriado da classe comparada.",
    "av-e1-64": "Pistão e parafuso reduzem volume aprisionado; D. Nos dinâmicos, rotor fornece energia e difusor converte energia cinética em pressão. Não se valida literalmente pás no difusor ao refutarC; A/B/E contradizem o mecanismo ou sua energia.",
    "av-e1-73": "A razão elevada de área de troca/volume caracteriza compactação e explica o objetivo. B inverte essa razão; C confunde troca e armazenamento; D aumenta resistência à condução para mesmo material/área; E nega a função térmica das aletas. SomenteA responde. Não há promessa de perda de pressão ou desempenho invariáveis.",
}


def number(value):
    value_text = value
    found = re.match(r"([+−-]?\d[\d.,]*)", value)
    if not found:
        if value.startswith("zero"):
            return 0., 0
        raise ValueError(value)
    token = found[1].replace("−", "-").rstrip('.')
    if ',' in token:
        token = token.replace('.', '').replace(',', '.')
    elif re.fullmatch(r"[+\-]?\d{1,3}(?:\.\d{3})+", token):
        token = token.replace('.', '')
    decimals = len(token.split('.')[-1]) if '.' in token else 0
    value = float(token)
    if "consumidos" in value_text:
        value = -value
    return value, decimals


rows = []
for record in diagnostic["registros"]:
    item_id = record["id"]
    if item_id not in changed:
        continue
    row = {"id": item_id, "sha256_artigo": record["sha256_artigo"], "chave": record["comando_e_uso"]["chave_atual"], "opcoes_examinadas": len(record["alternativas"]), "resultado": "coerente na releitura do Corretor", "observacoes": []}
    assert row["opcoes_examinadas"] == 5
    if item_id in numeric:
        expected, expression, distractors = numeric[item_id]
        observed = []
        values = []
        for option in record["alternativas"]:
            value, decimals = number(option["texto"])
            tolerance = .5*10**(-decimals)+1e-9
            compatible_number = abs(expected-value) <= tolerance
            compatible_type = item_id != "av-e1-10" or "kg/m³ e intensiva" in option["texto"]
            observed.append({"opcao": option["opcao"], "valor": value, "casas_decimais": decimals, "compatibilidade_numerica": compatible_number, "compatibilidade_unidade_classificacao": compatible_type, "compatibilidade_com_resposta": compatible_number and compatible_type})
            values.append(value)
        compatible = [o["opcao"] for o in observed if o["compatibilidade_com_resposta"]]
        assert compatible == [row["chave"]], (item_id, compatible)
        assert len({o["texto"] for o in record["alternativas"]}) == 5, item_id
        if item_id != "av-e1-10":
            assert len(set(values)) == 5, item_id
        else:
            row["observacoes"].append("B/E têm mesmo valor800kg/m³, mas classificação intensiva/extensiva distinta; sóB responde ao par pedido. A também troca a grandeza/unidade para volume específico.")
        row["demonstracao_numerica"] = {"expressao": expression, "resultado": expected, "opcoes": observed, "equivalencias_correta_apos_arredondamento": compatible}
        row["distratores_recalculados"] = []
        for letter, (result, error) in distractors.items():
            option = next(o for o in record["alternativas"] if o["opcao"] == letter)
            value, decimals = number(option["texto"])
            assert abs(result-value) <= .5*10**(-decimals)+1e-9, (item_id, letter, result, value)
            row["distratores_recalculados"].append({"opcao": letter, "resultado_do_erro": result, "erro": error})
    else:
        row["demonstracao_conceitual"] = conceptual[item_id]
    rows.append(row)
assert len(rows) == 25
report = {"id": "BAN-07", "rodada": 1, "data": "2026-10-28", "autor": "/root/corretor_aaa", "html_sha256": diagnostic["html_sha256"], "artigos": len(rows), "opcoes": sum(r["opcoes_examinadas"] for r in rows), "numericos": len(numeric), "conceituais": len(conceptual), "registros": rows, "limites": ["Conferência científica do próprio Corretor; não é parecer independente.", "Plausibilidade dos erros é teórica, sem piloto com estudantes.", "Tolerância de meia unidade da última casa é critério de arredondamento das opções, não incerteza física.", "Cálculos necessários ao gabarito/unicidade; não encerra BAN-08 integral."]}
(BASE / "corretor/verificacao-cientifica-25-r1.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"artigos": len(rows), "opcoes": report["opcoes"], "numericos": len(numeric), "conceituais": len(conceptual)}, ensure_ascii=False))
