import json

L=[1,2,3,4,5]

with open('demo.json','w') as f:
    json.dump(L,f)
    
    
d={'name':'Parth','age':21,'gender':'male'}

with open('demo1.json','w') as f:
    json.dump(d,f,indent=4)