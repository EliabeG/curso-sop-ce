"""Importa os quatro PDFs fornecidos pelo usuário. Requer PyMuPDF.
Execute da raiz: python auditoria/termodinamica/importacao-banco-200/gerar.py
Recria somente a página e imagens deste banco; não altera evidências históricas.
"""
from pathlib import Path
import fitz, re, html, json, hashlib
ROOT = Path(__file__).resolve().parents[3]
PDFS = ROOT / 'downloads/termodinamica/banco-autoral-200'
OUT = ROOT / 'assets/banco-autoral-e1'
OUT.mkdir(exist_ok=True)
for old_image in OUT.glob('questao-*.png'): old_image.unlink()
E = html.escape

def normal(t):
    return re.sub(r'\s+', ' ', t).strip()

def paras(t):
    return '<p>' + E(normal(t)) + '</p>'

def clean_page(p):
    return '\n'.join(b[4].strip() for b in p.get_text('blocks') if b[1] > 45 and b[3] < 795)

answers = {}
for fname in ['Gabarito_Comentado_Termodinamica_Avalia.pdf', 'Gabarito_Comentado_101_200_Termodinamica_Avalia.pdf']:
    d = fitz.open(PDFS / fname)
    txt = '\n'.join(clean_page(p) for p in list(d)[1:])
    matches = list(re.finditer(r'^(\d{3})\s*\|\s*([\s\S]+?)\nAlternativa ([A-E])\s*[-–]\s*', txt, re.M))
    assert len(matches) == 100, (fname, len(matches))
    for i, m in enumerate(matches):
        n = int(m[1]); end = matches[i+1].start() if i+1 < len(matches) else len(txt)
        body = txt[m.end():end].strip()
        # Cada comentário inclui a alternativa correta e sua fonte, sem revisão editorial.
        answers[n] = {'title': normal(m[2]), 'answer': m[3], 'comment': normal(body), 'file': fname,
                      'page': next(p.number+1 for p in d if re.search(r'^'+m[1]+r'\s*\|', p.get_text(), re.M))}
    quick = dict((int(n), a) for n,a in re.findall(r'(\d{2,3})-([A-E])', d[0].get_text()))
    assert len(quick) == 100
    assert all(answers[n]['answer'] == a for n,a in quick.items())

articles = []; manifest = []
for volume, fname in enumerate(['Banco_100_Questoes_Termodinamica_Avalia.pdf', 'Banco_101_200_Termodinamica_Avalia.pdf'], 1):
    d = fitz.open(PDFS / fname)
    assert len(d) == 103
    for p in list(d)[3:]:
        text = p.get_text()
        n = int(re.search(r'QUESTÃO (\d{3})', text)[1]); a = answers[n]; qid = f'ba-e1-{n:03}'
        options = list(re.finditer(r'^([A-E])\)\s', text, re.M))
        assert [m[1] for m in options] == list('ABCDE')
        source_start = text.index('Fonte da ideia:')
        opts = [normal(text[m.end(): options[i+1].start() if i<4 else source_start]) for i,m in enumerate(options)]
        source = normal(text[source_start:text.index('Rumo à SOP |')])
        alt_y = min(b[1] for b in p.get_text('blocks') if re.match(r'A\)\s', b[4]))
        blocks = [b for b in p.get_text('blocks') if b[1] > 45 and b[3] <= alt_y+0.1]
        # O título do volume 1 é repetido no cabeçalho HTML.
        if volume == 1 and normal(blocks[0][4]) == a['title']: blocks = blocks[1:]
        tables = [t for t in p.find_tables().tables if all(c is not None for row in t.extract() for c in row)]
        stem_parts = []
        if tables:
            elements = []
            for table in tables:
                rows = table.extract(); table_html = '<div class="tabela-rolagem"><table><caption>Dados da questão '+str(n)+'</caption><thead><tr>'
                table_html += ''.join('<th scope="col">'+E(normal(c or ''))+'</th>' for c in rows[0]) + '</tr></thead><tbody>'
                table_html += ''.join('<tr>'+''.join('<td>'+E(normal(c or ''))+'</td>' for c in row)+'</tr>' for row in rows[1:])+'</tbody></table></div>'
                elements.append((table.bbox[1], table_html))
            for b in blocks:
                if not any(fitz.Rect(b[:4]).intersects(fitz.Rect(t.bbox)) for t in tables): elements.append((b[1], paras(b[4])))
            extra_drawings = [x for x in p.get_drawings() if x['rect'].y0>45 and x['rect'].y1<alt_y and x['rect'].height>1 and not any((fitz.Rect(t.bbox) + (-1,-1,1,1)).contains((x['rect'].tl+x['rect'].br)/2) for t in tables)]
            if len(extra_drawings)>2:
                y0 = min(x['rect'].y0 for x in extra_drawings)-4
                rest = [b for b in blocks if b[1]>=y0]
                elements = [entry for entry in elements if entry[0]<y0]
                name = f'questao-{n:03}.png'
                pix = p.get_pixmap(matrix=fitz.Matrix(1.7,1.7), clip=fitz.Rect(39,y0,p.rect.width-39,alt_y-4), alpha=False)
                pix.save(OUT/name)
                elements.append((y0,f'<figure class="cr-figura"><img src="../assets/banco-autoral-e1/{name}" width="{pix.width}" height="{pix.height}" loading="lazy" alt="Esquema da questão {n}; descrição textual a seguir."><figcaption>'+E(normal(' '.join(b[4] for b in rest)))+'</figcaption></figure>'))
            stem_parts = [x[1] for x in sorted(elements, key=lambda x:x[0])]
        else:
            drawings = [x for x in p.get_drawings() if x['rect'].y0>45 and x['rect'].y1<alt_y and x['rect'].height>1]
            if len(drawings)>2 or any(im for im in p.get_images()):
                # Recorte do complemento visual, preservando setas, curvas e legendas.
                first = blocks[0]; stem_parts.append(paras(first[4]))
                rest = blocks[1:]
                if rest:
                    y0 = min([b[1] for b in rest]+[x['rect'].y0 for x in drawings]) - 4
                    clip = fitz.Rect(39,y0,p.rect.width-39,alt_y-4)
                    name = f'questao-{n:03}.png'
                    pix = p.get_pixmap(matrix=fitz.Matrix(1.7,1.7), clip=clip, alpha=False)
                    pix.save(OUT/name)
                    stem_parts.append(f'<figure class="cr-figura"><img src="../assets/banco-autoral-e1/{name}" width="{pix.width}" height="{pix.height}" loading="lazy" alt="Esquema da questão {n}; descrição textual a seguir."><figcaption>'+E(normal('\n'.join(b[4] for b in rest)))+'</figcaption></figure>')
            else:
                stem_parts = [paras(b[4]) for b in blocks]
        refs = set(re.findall(r'Q\s*(34|41|42)\b',source))
        subject = {'34':'energia','41':'carnot','42':'cop'}[next(iter(refs))] if len(refs)==1 else 'integrados'
        subject_label = {'energia':'Balanços de energia','carnot':'Máquinas térmicas e Carnot','cop':'Refrigeração e COP','integrados':'Balanços e sistemas acoplados'}[subject]
        stem = '\n'.join(stem_parts)
        article = f'''<article class="avalia-item" id="{qid}" data-cr-assunto="{subject}" data-cr-banca="Volume {volume}" data-cr-gabarito="{a['answer']}" aria-labelledby="{qid}-titulo">
<p class="cr-meta">Banco autoral Rumo à SOP · Volume {volume} · questão {n:03}</p>
<h3 id="{qid}-titulo">{n:03}. {E(a['title'])}</h3><p class="cr-assunto">{subject_label}</p>
<div class="cr-enunciado" id="{qid}-enunciado">{stem}</div>
<fieldset class="cr-alternativas" aria-describedby="{qid}-enunciado"><legend>Selecione uma alternativa.</legend>'''
        article += '\n'.join(f'<label for="{qid}-{letter}"><input type="radio" id="{qid}-{letter}" name="{qid}" value="{letter}"><span><strong>{letter}.</strong> {E(opt)}</span></label>' for letter,opt in zip('ABCDE',opts))
        article += f'''</fieldset><div class="cr-acoes" hidden><button type="button" class="botao" data-cr-acao="corrigir">Conferir resposta</button><button type="button" class="botao" data-cr-acao="refazer">Refazer questão</button></div>
<p class="cr-feedback" role="status" aria-live="polite"></p>
<details class="cr-resolucao"><summary>Ver gabarito e comentário</summary><p><strong>Gabarito do material autoral: {a['answer']}.</strong></p>{paras(a['comment'])}<p><a href="../downloads/termodinamica/banco-autoral-200/{a['file']}#page={a['page']}">Consultar comentário no PDF original (p. {a['page']})</a></p></details>
<p class="nota">{E(source)}</p><p><a href="../downloads/termodinamica/banco-autoral-200/{fname}#page={p.number+1}">Questão no PDF original (p. {p.number+1})</a></p></article>'''
        articles.append(article)
        manifest.append({'id':qid,'numero':n,'volume':volume,'caderno':fname,'pagina':p.number+1,'gabarito':a['answer'],'comentario_pdf':a['file'],'comentario_pagina':a['page'],'enunciado_pdf':normal('\n'.join(b[4] for b in blocks)),'alternativas':dict(zip('ABCDE',opts)),'comentario':a['comment']})
assert len(articles)==200 and sorted(answers)==list(range(1,201))
links = ''.join(f'<li><a href="../downloads/termodinamica/banco-autoral-200/{p.name}">{label}</a></li>' for p,label in [(PDFS/'Banco_100_Questoes_Termodinamica_Avalia.pdf','Caderno 1 — questões 1 a 100'),(PDFS/'Gabarito_Comentado_Termodinamica_Avalia.pdf','Gabarito comentado — 1 a 100'),(PDFS/'Banco_101_200_Termodinamica_Avalia.pdf','Caderno 2 — questões 101 a 200'),(PDFS/'Gabarito_Comentado_101_200_Termodinamica_Avalia.pdf','Gabarito comentado — 101 a 200')])
page = '''<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover"><title>200 questões de Termodinâmica — Rumo à SOP</title><meta name="description" content="Resolva 200 questões autorais de Termodinâmica, com balanços de energia, Carnot e COP, gabaritos comentados e PDFs originais."><meta name="curso:modulo" content="e1-banco-200"><link rel="stylesheet" href="../assets/curso.css"><link rel="stylesheet" href="../assets/banco-autoral-e1.css"><link rel="icon" href="../assets/icone.svg" type="image/svg+xml"><script src="../assets/registro.js"></script><script src="../assets/curso.js"></script></head>
<body class="pg-modulo"><a class="pular" href="#conteudo">Pular para o conteúdo</a><header class="topo"><a class="marca" href="../index.html"><span class="marca-selo">SOP</span><span class="marca-texto">Engenharia Mecânica · SOP-CE</span></a><div class="topo-acoes"><button type="button" class="botao botao-tema" data-acao="tema" hidden>Tema</button></div></header>
<main class="pagina banco-autoral-200" id="conteudo"><header class="mod-cabecalho"><p class="eyebrow">E1 · Banco complementar Rumo à SOP</p><h1>200 questões de Termodinâmica</h1><p class="lead">Balanços de energia · máquinas térmicas e Carnot · refrigeração e COP</p><p><a class="botao" href="e1-termodinamica.html">Voltar à aula de Termodinâmica</a> <a class="botao" href="../formulas/termodinamica.html">Consultar fórmulas</a> <a class="botao" href="#pdfs">Baixar cadernos e gabaritos</a></p></header>
<div class="box box-dica"><p>Questões <strong>autorais</strong> dos dois cadernos fornecidos, baseadas nos princípios das Q34, Q41 e Q42 da prova de Engenheiro Mecânico da Prefeitura de Porto Alegre/RS, Instituto Avalia, edital 122/2025, tipo 1. Não são questões oficiais da banca nem previsão da prova da SOP.</p><p>Resolva em sessões de 10 a 20 itens e abra o comentário depois de responder. O banco concentra três temas e não cobre todo o programa de Termodinâmica. As respostas ficam salvas neste navegador, em armazenamento próprio deste banco, separado dos bancos anteriores e da exportação geral do portal.</p><p>Enunciados, dados, esquemas e gabaritos foram importados dos PDFs. A classificação por assunto é editorial. <a href="e1-termodinamica.html#energia">Revisar primeira lei</a> · <a href="e1-termodinamica.html#segunda-lei">Revisar Carnot</a> · <a href="e1-termodinamica.html#ciclos">Revisar COP</a>.</p></div>
<section id="pdfs" aria-labelledby="h-pdfs"><h2 id="h-pdfs">Cadernos e gabaritos originais</h2><ul>''' + links + '''</ul></section>
<section class="banco-concursos" id="treino-avalia" aria-labelledby="h-banco"><h2 id="h-banco">Resolver as questões</h2><div class="cr-controles" hidden><div class="cr-filtros"><label for="av-assunto">Assunto<select id="av-assunto"><option value="">Todos os assuntos</option><option value="energia">Balanços de energia</option><option value="carnot">Máquinas térmicas e Carnot</option><option value="cop">Refrigeração e COP</option><option value="integrados">Balanços e sistemas acoplados</option></select></label><label for="av-banca">Caderno<select id="av-banca"><option value="">Ambos os volumes</option><option>Volume 1</option><option>Volume 2</option></select></label><label for="av-busca">Buscar questão<input id="av-busca" type="search" maxlength="120" placeholder="Número, título ou trecho do enunciado"></label><label class="cr-pendentes"><input id="av-pendentes" type="checkbox"> Somente não respondidas</label></div><p id="av-placar" role="status" aria-live="polite"></p><p id="av-armazenamento"></p></div><p id="av-vazio" hidden>Nenhuma questão corresponde aos filtros. Altere o assunto, o caderno ou a busca.</p><div class="cr-lista">''' + '\n'.join(articles) + '''</div></section></main><footer class="rodape"><p>Material independente de preparação · <a href="e1-termodinamica.html">Voltar ao E1</a></p></footer></body></html>\n'''
(ROOT/'modulos/e1-termodinamica-200-questoes.html').write_text(page)
data = {'origem':'ZIP Questoes_001_200_e_Gabaritos.zip fornecido pelo usuário','escopo':'Importação documental; não constitui recálculo científico nem aceite de QA-09/BAN-08','pdfs':[{ 'arquivo':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(PDFS.glob('*.pdf'))],'questoes':manifest}
(ROOT/'auditoria/termodinamica/importacao-banco-200/inventario.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
print(f'{len(articles)} questões; {len(list(OUT.glob("*.png")))} figuras; 4 PDFs')
