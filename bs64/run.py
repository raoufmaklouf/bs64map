from core import decoder_encoder
from core import jsonInjector
from core import detector
from core import nano
from scanners import lfi
from scanners import xss
from scanners import ssrf
from scanners import redirect
from scanners import crlf
from scanners import ssti
from scanners import reflication
import sys
import threading
from alive_progress import alive_bar

file_=sys.argv[1]
f=open(file_,'r')
urls=[]
for x in f:
    x=x.rstrip()
    urls.append(x)

cont=[]

def xssF(i):
    xss.xss_(i)

def redirectF(i):
    redirect.redirect_(i)
    
 def sqlscanF(i):
     sqlinjection.sqlinjection_(i)

def lfiF(i):
    lfi.lfi_(i)

def sstiF(i):
    ssti.ssti_(i)
    
def crlfF(i):
    crlf.crlf_(i)

def ssrfF(i):
    ssrf.ssrf_(i)

def reflictionF(i):
    reflication.reflication_(i)

with alive_bar(len(urls)) as bar:
    for itm in urls:
        itm=itm.rstrip()
        x=detector.detector_(itm)
        bar()
        if(x):
    
            if '?' in itm:
                if nano.inject_param(itm,'raoufTest') not in cont:
                    cont.append(nano.inject_param(itm,'raoufTest'))
                    p1 = threading.Thread(target=lfiF, args=(itm,))
                    p1.start()
                    p2 = threading.Thread(target=xssF, args=(itm,))
                    p2.start()
                    p3 = threading.Thread(target=ssrfF, args=(itm,))
                    p3.start()
                    p4 = threading.Thread(target=redirectF, args=(itm,))
                    p4.start()
                    p5 = threading.Thread(target=crlfF, args=(itm,))
                    p5.start()
                    p6 = threading.Thread(target=sstiF, args=(itm,))
                    p6.start()
                    p7 = threading.Thread(target=reflictionF, args=(itm,))
                    p7.start()
                    
                    p1.join(timeout=10)
                    p2.join(timeout=10)
                    p3.join(timeout=10)
                    p4.join(timeout=10)
                    p5.join(timeout=10)
                    p6.join(timeout=10)
                    p7.join(timeout=10)
                    
                
                
            else:
            
                p1 = threading.Thread(target=lfiF, args=(itm,))
                p1.start()
                p2 = threading.Thread(target=xssF, args=(itm,))
                p2.start()
                p3 = threading.Thread(target=ssrfF, args=(itm,))
                p3.start()
                p4 = threading.Thread(target=redirectF, args=(itm,))
                p4.start()
                p5 = threading.Thread(target=crlfF, args=(itm,))
                p5.start()
                p6 = threading.Thread(target=sstiF, args=(itm,))
                p6.start()
                p7 = threading.Thread(target=reflictionF, args=(itm,))
                p7.start()

                p1.join(timeout=10)
                p2.join(timeout=10)
                p3.join(timeout=10)
                p4.join(timeout=10)
                p5.join(timeout=10)
                p6.join(timeout=10)
                p7.join(timeout=10)
                
            
    
   
