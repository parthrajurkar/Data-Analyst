import json

with open('demo1.json','r') as f:
    a=json.load(f)
    print(a)
    print(type(a))
    