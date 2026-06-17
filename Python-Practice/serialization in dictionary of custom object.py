class Person:
    def __init__(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city
        
person=Person('Parth',21,'Amravati')

import json
def show_object(person):
    if isinstance(person,Person):
        return {'Name':person.name,'Age':person.age,'City':person.city}

with open('demo3.json','w') as f:
    json.dump(person,f,default=show_object,indent=4)