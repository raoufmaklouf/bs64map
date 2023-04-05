import re

def detactor_(item):
    bs64str=''

    match1=re.search("^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{4}|[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)$",item)
    match2=re.search("([^A-Za-z0-9+/]|^)(eyJ|YTo|Tzo|PD[89]|aHR0cHM6L|aHR0cDo|rO0)[%a-zA-Z0-9+/]+={0,2}",item)
    if (match1):
        m=match1.group()
        
        if m.startswith('='):
            m=m[1:]
        if '%' in m :
             m=m.split('%')[0]
            
        
    elif (match2):
        m=match2.group()
        
        
        if m.startswith('='):
            m=m[1:]
        if '%' in m :
            m=m.split('%')[0]
        

    if (match1) or (match2):
               
        bs64str=m
       
    return bs64str
        

