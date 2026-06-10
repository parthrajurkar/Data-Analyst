# 'w' means write operation,in new file it writes and in existing file it replaces
f=open('Samplefile1.txt','w')
f.write("Hello")
f.close()
# a - append,It adds input at the end of existing String
f=open('Samplefile1.txt','a')
f.write(" World")
f.close()

# writelines is used here to print multiple lines of a list
L=['Hello\n','Hi\n','How are you\n','I\n','Am\n','Fine']
#In next line, 'w' is replacing/overwritting previous Strings (Hello World)
f=open('Samplefile1.txt','w')
f.writelines(L)
f.close()