"""
df['column_name'].mean()
df['column_name'].sum()
df['column_name'].min()
df['column_name'].max()
"""

import pandas as pd

data={
    "Name":['Arun','Varun','Karun'],
    "Age":[38,21,25],
    "Salary":[10000,4000,6000]
}

df=pd.DataFrame(data)
print(df)

print("Summary Functions")

print(df['Age'].mean())
print(df['Age'].sum())
print(df['Age'].min())
print(df['Age'].max())

#Average salary

avg_salary=df['Salary'].mean()
print("Average Salary is",avg_salary)