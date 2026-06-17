# length of a string without using len function, ex:Hello World,length = 11

s=input("Enter the String")
counter=0

for i in s:
    counter += 1
    
print("Length of String is",counter)
    