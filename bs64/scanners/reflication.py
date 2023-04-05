import requests
import re
import random
from core import nano
from core import regex
from core import decoder_encoder
from core import jsonInjector
from core import detactor
from requests.packages import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  






p="TrSAF45"

def reflication_(url):
    x=detactor.detactor_(url)
    y=decoder_encoder.decoder_(x)
    
    if(y):
        if nano.isJson(y)== True:
            #for rg,p in regex.XSS.items():
                user_agent=random.choice(regex.USR_AGENTS)
                z=jsonInjector.main_(y,p)
                payload=decoder_encoder.encoder_(z)
                link=url.replace(str(x),payload)
                try:
                    r = requests.get(link,verify=False,timeout=13,headers={'User-Agent':user_agent})
                    resp= r.content
                    x1 = re.search(p, str(resp))
                    if (x1):
                        print('\033[91mPossibly refliction\033[00m  '+link)
                except:
                    pass
        else:
            #for rg,p in regex.XSS.items():
                user_agent=random.choice(regex.USR_AGENTS)
                payload=decoder_encoder.encoder_(p)
                link=url.replace(str(x),payload)
                try:
                    r = requests.get(link,verify=False,timeout=13,headers={'User-Agent':user_agent})
                    resp= r.content
                    x1 = re.search(p, str(resp))
                    if (x1):
                        print('\033[91mPossibly refliction\033[00m  '+link)
                except:
                    pass
   
    else:
        #for rg,p in regex.XSS.items():
            user_agent=random.choice(regex.USR_AGENTS)
            payload=decoder_encoder.encoder_(p)
            link=url.replace(str(x),payload)
            try:
                r = requests.get(link,verify=False,timeout=13,headers={'User-Agent':user_agent})
                resp= r.content
                x1 = re.search(p, str(resp))
                if (x1):
                    print('\033[91mPossibly refliction\033[00m  '+link)
            except:
                pass





























