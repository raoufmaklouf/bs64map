



def main_(jsonstr,payload):
        
        jsonkeys=[]
        final=jsonstr
        jsons=jsonstr
        jsons=jsons.replace('{','')
        jsons=jsons.replace('}','')
        jsonvar=jsons.split(',')
        for md in jsonvar:
              jsonkey=md.split(':')[1]
              if jsonkey not in jsonkeys:
                    jsonkeys.append(jsonkey)
                    

                    
                           
        for k in jsonkeys: 
              
        
               if '"' in k:
                   
                    finalstring=final.replace(k,'"~~~~~~~~~~"')
               elif "'" in k:
                    
                    finalstring=final.replace(k,"'~~~~~~~~~~'")
               else:  
                    finalstring=final.replace(k,"~~~~~~~~~~")
               final=finalstring
        
        final=final.replace("~~~~~~~~~~",payload)
        return final
        
        #return pp.decode("utf-8")
print(main_("{s:'3',g:1,llll:f,der:'desr'}",'<script>alert(10)</script>'))
