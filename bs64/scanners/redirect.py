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

from requests.packages import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



def redirect_(url):
    x=detactor.detactor_(url)
    y=decoder_encoder.decoder_(x)
    
    if(y):
        if nano.isJson(y)== True:
            for i in regex.payloads_OR_p:
                user_agent=random.choice(regex.USR_AGENTS)
                z=jsonInjector.main_(y,i)
                payload=decoder_encoder.encoder_(z)
                link=url.replace(x,payload)
                try:
                    r = requests.get(link,verify=False,timeout=13,headers={'User-Agent':user_agent})
                    cont=r.content
                    if 'k6unx4pudf8k5itoapaxjwzjigz' in str(cont):
                        if r.history :
                            print('\033[91m Possibly open redirection vulnerability\033[00m '+link)      
                        else:
                            print('\033[91m Possibly SSRF vulnerability\033[00m '+link)
                except:
                    pass
        else:
            for i in regex.payloads_OR_p:
                user_agent=random.choice(regex.USR_AGENTS)
                payload=decoder_encoder.encoder_(i)
                link=url.replace(x,payload)
                try:
                    r = requests.get(link,verify=False,timeout=13,headers={'User-Agent':user_agent})
                    cont=r.content
                    if 'k6unx4pudf8k5itoapaxjwzjigz' in str(cont):
                        if r.history :
                            print('\033[91m Possibly open redirection vulnerability\033[00m '+link)      
                        else:
                            print('\033[91m Possibly SSRF vulnerability\033[00m '+link)
                except:
                    pass
   
    else:
        for i in regex.payloads_OR_p:
            user_agent=random.choice(regex.USR_AGENTS)
            payload=decoder_encoder.encoder_(i)
            link=url.replace(x,payload)

            try:
                r = requests.get(link,verify=False,timeout=13,headers={'User-Agent':user_agent})
                cont=r.content
            
                if 'k6unx4pudf8k5itoapaxjwzjigz' in str(cont):
                    if r.history :
                        print('\033[91m Possibly open redirection vulnerability\033[00m '+link)      
                    else:
                        print('\033[91m Possibly SSRF vulnerability\033[00m '+link)
            except:
                pass



















