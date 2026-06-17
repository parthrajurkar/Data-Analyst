try:
    with open('samplefile10.txt','r') as f:
        print(f.read())
        
except:
    print("File Not Found")