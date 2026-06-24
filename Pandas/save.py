import pandas as pd

data={
    "Name":['Ram','Krushna','Balram'],
    "Age":[10,20,30],
    "City":['Amravati','Pune','Mumbai']
}

df=pd.DataFrame(data)
#print(df)

#df.to_csv("Output.csv",index=False)

df.to_excel("Output.xlsx",index=False)

df=pd.read_excel("Output.xlsx")
print(df)