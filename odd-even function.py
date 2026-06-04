# We are creating a function that can print odd even from 1-10

def even(n):
    if type(n)==int:    
        if n%2==0:
            print("Even")
        
        else:
            print("Odd")
    else:print("Number is not an integer")    
    
for i in range(1,11):
    print(i,"is",end=" ")
    even(i)
