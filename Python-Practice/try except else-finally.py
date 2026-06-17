try:
    f=open('Samplefile10.txt','r')

except FileNotFoundError:
    print("File Not Found")

except Exception:
    print("Error")

#When error not exists,else part is executed,if error found then except part is executed    
else:
    print(f.read())

# Finally will  always get executed,whether error is there or not    
finally:
    print("This will always get executed")