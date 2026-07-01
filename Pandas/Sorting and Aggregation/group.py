import pandas as pd

data={
    "Name":['Arun','Varun','Karun','Narun','Marun'],
    "Age":[38,25,25,28,38],
    "Salary":[10000,4000,6000,16000,12000]
}

df=pd.DataFrame(data)
print(df)

#all the similar age persons are grouped together,and fn are performed on this groups

grouped=df.groupby('Age')['Salary'].sum()
print(grouped)