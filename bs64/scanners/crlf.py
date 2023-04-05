import requests
import re
from core import nano
from core import regex
from core import decoder_encoder
from core import jsonInjector
from core import detactor
from requests.packages import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)





def crlf_(url):
    x=detactor.detactor_(url)
    y=decoder_encoder.decoder_(x)
    
    if(y):
        if nano.isJson(y)== True:
            for i in regex.payload_crlf:
                z=jsonInjector.main_(y,i)
                payload=decoder_encoder.encoder_(z)
                link=url.replace(x,payload)

                try:
                    session = requests.Session()
                    session.get(link,verify=False,timeout=13)
                    if 'crlf' in session.cookies.get_dict() and 'injection' in session.cookies.get_dict().values():
                        print('\033[91m Possibly CRLF injection vulnerability\033[00m  '+link)
                except:
                    pass
        else:
            for i in regex.payload_crlf:
                payload=decoder_encoder.encoder_(i)
                link=url.replace(x,payload)

                try:
                    session = requests.Session()
                    session.get(link,verify=False,timeout=13)
                    if 'crlf' in session.cookies.get_dict() and 'injection' in session.cookies.get_dict().values():
                        print('\033[91m Possibly CRLF injection vulnerability\033[00m  '+link)
                except:
                    pass
   
    else:
        for i in regex.payload_crlf:
            payload=decoder_encoder.encoder_(i)
            link=url.replace(x,payload)

            try:
                session = requests.Session()
                session.get(link,verify=False,timeout=13)
                if 'crlf' in session.cookies.get_dict() and 'injection' in session.cookies.get_dict().values():
                    print('\033[91m Possibly CRLF injection vulnerability\033[00m  '+link)
            except:
                pass
