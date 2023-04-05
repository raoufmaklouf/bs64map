import base64

def decoder_(i):
    try:
        m=base64.b64decode(i).decode('utf-8')
        return m
    except:
        pass
    
                    
def encoder_(i):
    try:
       i_bytes = i.encode('ascii')
       m = base64.b64encode(i_bytes).decode('ascii')
       return m
    except:
       pass
    

