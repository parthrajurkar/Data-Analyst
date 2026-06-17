#ex racecar,malayalam,abba

string=input("Enter String ")
flag=True

for i in range(0,len(string)//2):
    if string[i] != string[len(string)-i-1]:
        flag=False
        print("Not a Pallindrome")
        break
    
if flag:
    print("Palindrome")
        