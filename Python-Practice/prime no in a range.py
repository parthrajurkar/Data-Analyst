# Range (1-10) will print all the prime no.s from (1-9)

lower=int(input("Enter a Lower limit"))
upper=int(input("Enter a Upper limit"))

for i in range (lower,upper+1):
    for j in range(2,i):
        if i%j == 0:
            break
        
    else:
            print(i)    