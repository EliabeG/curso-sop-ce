// Sondagem local somente leitura: não se conecta a navegador existente nem à rede.
const fs = require('node:fs');
const crypto = require('node:crypto');
const cp = require('node:child_process');
const path = 'auditoria/termodinamica/evidencias/QA-09/aplicacao-precisao-r30/resultado/depois-aula.html';
const data = fs.readFileSync(path);
const hash = crypto.createHash('sha256').update(data).digest('hex');
if (hash !== 'c719adae3464fb56ed2b0ad7014e0721c0aab2da444fb484ec0b40c5c0c8fbd4') throw Error('fotografia inesperada');
const candidates = ['chromium','chromium-browser','google-chrome','google-chrome-stable','firefox','firefox-esr','electron','wkhtmltoimage','docker','podman'];
const available = candidates.filter(x => cp.spawnSync('which', [x], {stdio:'ignore'}).status === 0);
(async () => {
  const playwright = require('playwright');
  const browsers = {};
  for (const engine of ['chromium','firefox','webkit']) {
    const executable = playwright[engine].executablePath();
    try {
      const browser = await playwright[engine].launch({headless:true, timeout:5000});
      browsers[engine] = {executable, exists:fs.existsSync(executable), launch:'sucesso'};
      await browser.close();
    } catch (error) {
      browsers[engine] = {executable, exists:fs.existsSync(executable), launch:'falhou', reason:error.message.split('\n')[0]};
    }
  }
  console.log(JSON.stringify({snapshot_sha256:hash,node:process.version,playwright:require('playwright/package.json').version,available_in_path:available,browsers}, null, 2));
})().catch(error => {console.error(error);process.exitCode=1});
