#info(),this fn shows rows,columns,datatypes,non-null values,Memory Usage of Data Set

import pandas as pd

data={
    "Name":["Ram","Shyam","Balram"],
    "Age":[30,20,22],
    "City":["Amravati","Pune","Mumbai"]
    }

df=pd.DataFrame(data)
#print(df)

#Displaying Info of Data Set
print(df.info())