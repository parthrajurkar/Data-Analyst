import pandas as pd

data={
    "Name":['Arun','Varun','Karun'],
    "Age":[38,21,25],
    "Salary":[6000,4000,10000]
}

df=pd.DataFrame(data)
print(df)

#Used sort_values to sort multiple columns

#In multiple columns when sorting with ascending or desc,first priority will be given to
# first column in column_name list

df.sort_values(by=["Age","Salary"],ascending=True,inplace=True)
print('After Sorting')
print(df)