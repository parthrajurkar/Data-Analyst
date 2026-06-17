# ex string=Hello World, find no of 'o' in this string,O/P- 2

string=input("Enter String ")
find=input("Enter a character to find its frequency ")

counter=0
for i in string:
    if i==find:
        counter += 1

print("Frequency of",find+" is",counter )        