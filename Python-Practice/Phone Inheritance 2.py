#Parent Class
class Phone:
    #this constructor will not be executed as Child Class has an Constructor
    def __init__(self,price,brand,camera):
        print("Inside Phone Constructor")
        self.__price=price
        self.brand=brand
        self.camera=camera

#Child Class        
class SmartPhone(Phone):
    #This Constructor will be Executed
    def __init__(self,os,ram):
        print("Inside SmartPhone Constructor")
        self.os=os
        self.ram=ram        
        
s=SmartPhone('Android',8)
print(s.os)
print(s.ram)        
