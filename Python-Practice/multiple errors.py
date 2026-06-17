try:
    m=5
    f = open('Samplefile2.txt','r')
    print(f.read())
    print(m)
    print(5/2)
    #Above every condition is True(errorless),next condition would be an error
    L=[1,2,3]
    L[100]

except FileNotFoundError:
    print("File Not Found")
    
except NameError:
    print("Variable not defined")
    
except ZeroDivisionError:
    print("Can't be divided by Zero")
 
#When an undefined error is found it is stored in "Exception",print would print error-type   
except Exception as e:
    print(e)