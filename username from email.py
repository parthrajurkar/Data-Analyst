# We have to display the username from an valid email,ex:hello@gmail.com,O/P- hello

email=input("Enter Email")

for i in email:
    if i == '@':
        pos=email.index('@')
        print(pos)
        print(email[0:pos])
        break
        
else:
    print("Not a valid Email")    
        
