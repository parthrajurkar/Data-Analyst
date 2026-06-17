#Parent Class
class Phone:
    def __init__(self,price,brand,camera):
        print("Inside Phone Constructor")
        self.price=price
        self.brand=brand
        self.camera=camera
        
    def buy(self):
        print("Buying Phone")

#Child Class        
class SmartPhone(Phone):
    pass

#If child class doesn't have a constructor then constructor of parent class is called
a=SmartPhone(40000,'Samsung',50)
a.buy()
