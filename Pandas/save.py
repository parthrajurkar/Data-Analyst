import pandas as pd

data={
    "Name":['Ram','Krushna','Balram'],
    "Age":[10,20,30],
    "City":['Amravati','Pune','Mumbai']
}

df=pd.DataFrame(data)
print(df)