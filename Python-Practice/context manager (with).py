#In this,File gets close automatically
with open('Samplefile2.txt','w') as f:
    f.write("Hello,You are using context manager 'with' ")
    
with open('Samplefile2.txt','r') as f:
    print(f.read())