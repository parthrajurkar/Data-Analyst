class Customer:
    
    def __init__(self,name,gender,address):
        self.name=name
        self.gender=gender
        self.address=address
        
class Address:
    def __init__(self,city,state,pincode):
        self.city=city
        self.state=state
        self.pincode=pincode
        
add1=Address('Amravati','Maharashtra',444606)
cus=Customer('Parth','Male',add1)