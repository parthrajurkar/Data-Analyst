class User:
    def __init__(self):
        self.name='Parth'
        self.gender='Male'
        
    def login(self):
        print("Login")
    
class Student(User):
        
    def enroll(self):
        print("Enroll into the course")
        
u=User()
s=Student()

print(s.name)
s.login()
s.enroll()
