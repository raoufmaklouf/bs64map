import requests
import re
from core import nano
from core import regex
from core import decoder_encoder
from core import jsonInjector
from core import detactor
from requests.packages import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)





test1="58784"
test2='32110'


def ssti_(url):
    x=detactor.detactor_(url)
    y=decoder_encoder.decoder_(x)
    
    if(y):
        if nano.isJson(y)== True:
            for i in regex.payload_ssti_1:
                z=jsonInjector.main_(y,i)
                payload=decoder_encoder.encoder_(z)
                link1=url.replace(x,payload)
                try:
                    
                        r = requests.get(link1,verify=False,timeout=13)
                        cont1 = r.content
                        if(re.search(test1, str(cont1))):
                            for i in regex.payload_ssti_2:
                                z=jsonInjector.main_(y,i)
                                payload=decoder_encoder.encoder_(z)
                                link2=url.replace(x,payload)
                                r = requests.get(link2,verify=False,timeout=13)
                                cont2 = r.content
                                if(re.search(test2, str(cont2))):
                                    print("\033[91m Possibly SS template injection vulnerability\033[00m\t"+link2)
                           
                except:
                    pass
        else:
            for i in regex.payload_ssti_1:
                payload=decoder_encoder.encoder_(i)
                link=url.replace(x,payload)

                try:
                    r = requests.get(link1,verify=False,timeout=13)
                    cont1 = r.content
                    if(re.search(test1, str(cont1))):
                            for i in regex.payload_ssti_2:
                                z=jsonInjector.main_(y,i)
                                payload=decoder_encoder.encoder_(z)
                                link2=url.replace(x,payload)
                                r = requests.get(link2,verify=False,timeout=13)
                                cont2 = r.content
                                if(re.search(test2, str(cont2))):
                                    print("\033[91m Possibly SS template injection vulnerability\033[00m\t"+link2)
                except:
                    pass
   
    else:
        for i in regex.payload_ssti_1:
            payload=decoder_encoder.encoder_(i)
            link=url.replace(x,payload)
            try:
                r = requests.get(link1,verify=False,timeout=13)
                cont1 = r.content
                if(re.search(test1, str(cont1))):
                            for i in regex.payload_ssti_2:
                                z=jsonInjector.main_(y,i)
                                payload=decoder_encoder.encoder_(z)
                                link2=url.replace(x,payload)
                                r = requests.get(link2,verify=False,timeout=13)
                                cont2 = r.content
                                if(re.search(test2, str(cont2))):
                                    print("\033[91m Possibly SS template injection vulnerability\033[00m\t"+link2)
            except:
                pass
