#sum of 1/1! + 2/2! + 3/3! + ... n/n!

import math

n=int(input("Enter the value for n"))

result=0
factorial=1

for i in range (1,n+1):
    factorial=factorial * i
    result=result + i/factorial
    
print(result)