from playwright.sync_api import sync_playwright
import json, os
from urllib.parse import urljoin
URL=os.environ.get('BANCO_URL','http://127.0.0.1:8000/modulos/e1-termodinamica-200-questoes.html')
results=[]
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 page=b.new_page(viewport={'width':390,'height':844});errs=[];page.on('pageerror',lambda e:errs.append(str(e)))
 page.goto(URL);page.wait_for_selector('html.js-completo');assert page.locator('.avalia-item').count()==200
 page.locator('#av-banca').select_option('Volume 2');assert page.locator('.avalia-item:visible').count()==100
 page.locator('#av-busca').fill('101');assert page.locator('#ba-e1-101').is_visible()
 page.locator('#ba-e1-101-C').check();page.locator('#ba-e1-101 [data-cr-acao=corrigir]').click();assert 'correta.' in page.locator('#ba-e1-101 .cr-feedback').inner_text()
 assert page.locator('#ba-e1-101 .cr-resolucao').get_attribute('open') is not None
 page.reload();page.wait_for_selector('html.js-completo');assert page.locator('#ba-e1-101-C').is_checked()
 keys=page.evaluate('Object.keys(localStorage)');assert 'sopmec:avalia:v2:e1-banco-200' in keys and 'sopmec:avalia:v2:e1' not in keys
 assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
 page.locator('#ba-e1-101 [data-cr-acao=refazer]').click();assert not page.locator('#ba-e1-101-C').is_checked()
 page.locator('.botao-tema').click();assert page.locator('.botao-tema').inner_text()
 for link in page.locator('#pdfs a').all():assert page.request.get(urljoin(URL,link.get_attribute('href'))).status==200
 assert not errs,errs
 results=['200 artigos','filtro volume','busca 101','conferência C Q101','resolução aberta','persistência reload','armazenamento isolado','refazer','tema','PDFs HTTP 200','mobile sem overflow','sem pageerror']
 no=b.new_context(java_script_enabled=False);np=no.new_page();np.goto(URL);assert np.locator('.avalia-item').count()==200;np.locator('#ba-e1-001 summary').click();assert np.locator('#ba-e1-001 details').get_attribute('open') is not None;results.append('comentários sem JS')
 b.close()
print(json.dumps(results,ensure_ascii=False))
