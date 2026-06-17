class Person:
    def __init__(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city
        
person=Person('Parth',21,'Amravati')

import json
def show_object(person):
    if isinstance(person,Person):
        return "{},Age-{},City-{}".format(person.name,person.age,person.city)

with open('demo2.json','w') as f:
    json.dump(person,f,default=show_object)