class Customer:
    
    def __init__(self,name,gender,address):
        self.name=name
        self.gender=gender
        self.address=address
        
    def print_address(self):
        print(self.address.get_city(),self.address.pincode,self.address.state)
        
class Address:
    def __init__(self,city,state,pincode):
        self.__city=city
        self.state=state
        self.pincode=pincode
        
    def get_city(self):
        return self.__city
        
add1=Address('Amravati','Maharashtra',444606)
cus=Customer('Parth','Male',add1)

cus.print_address() 