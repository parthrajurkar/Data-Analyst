# tupple operations like min,max,sort,count,index

tupple=(1,5,3,4,2)
print(tupple)

print(min(tupple))

print(max(tupple))

print(tupple.count(2))

print(sorted(tupple))

print(tupple.index(5))

#tupple unpacking

(a,b,c)=(1,2,3)
print(a,b,c)

(a,b,*others)=(5,10,20,40,80)  #values in others will be stored in list
print(a,b)
print(others) 