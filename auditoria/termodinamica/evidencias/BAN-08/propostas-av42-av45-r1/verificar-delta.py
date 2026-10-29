from pathlib import Path
import re,hashlib,json
from fractions import Fraction as F
root=Path("auditoria/termodinamica/evidencias/BAN-08/propostas-av42-av45-r1")
s=Path("modulos/e1-termodinamica.html").read_text(encoding="utf-8")
assert hashlib.sha256(Path("modulos/e1-termodinamica.html").read_bytes()).hexdigest()=="80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0"
for n in (42,45,52):
 id=f"av-e1-{n}";old=re.search(r'<article\b[^>]*\bid="'+id+r'"[^>]*>.*?</article>',s,re.S).group();new=(root/f"AV{n}-candidata.html").read_text(encoding="utf-8")
 pattern=r'(<div class="cr-enunciado" id="'+id+r'-enunciado"><p>)(.*?)(</p></div>)'
 oldentry=re.search(pattern,old,re.S).group(2);newentry=re.search(pattern,new,re.S).group(2)
 reverted=new.replace(newentry,oldentry)
 if n==52:
  a="Desprezando outros consumos, a potência líquida é turbina menos compressor. Antes: (100 − 40)/200 = 30%. Depois: (100 − 50)/200 = 25%. Mais consumo isolado do compressor reduz a eficiência."
  b="O trabalho líquido é turbina menos compressor. Antes: (100 − 40)/200 = 30%. Depois: (100 − 50)/200 = 25%. Mais consumo isolado do compressor reduz a eficiência."
  assert reverted.count(a)==2;reverted=reverted.replace(a,b)
 assert reverted==old
 print(id,hashlib.sha256(new.encode()).hexdigest(),"opções, chave e restante preservados")
assert F(1000,4000)==F(1,4) and 4000-1000==3000 and abs(F(1000,3000)*100-F(333,10))<F(5,100)
assert 1-F(300,600)==F(1,2) and 1000*F(1,2)==500 and abs(F(1000*300,600+300)-F(3333,10))<F(5,100)
assert F(100-40,200)==F(3,10) and F(100-50,200)==F(1,4)
print("Contas das três candidatas conferidas; apenas mudanças declaradas e sem autoaprovação.")
