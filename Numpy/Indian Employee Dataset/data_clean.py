import numpy as np
import pandas as pd

#loading the dataset

df=pd.read_csv("Numpy/Indian Employee Dataset/Indian_Employee_Data.csv")
print(df.head())

#checking the missing values

print("Missing Values in each Column")
print(df.isnull().sum())
"""df.isnull().sum(),returns null values in each column"""

#Replace inf with nan
df.replace([np.inf,-np.inf],np.nan,inplace=True)

#replace negative salaries
df.loc[df['Salary']<0,"Salary"]=np.nan

# df['Salary']=np.where(df['Salary']<0,df['Salary'].mean(),df['Salary'])

df['Salary']=df['Salary'].fillna(df['Salary'].mean())

df['Performance_Rating']=df['Performance_Rating'].fillna(df['Performance_Rating'].median())

#remove duplicate records
df.drop_duplicates(inplace=True)

print(df['Salary'])

salary_mean=df['Salary'].mean()
salary_std=df['Salary'].std()
lower_bound=salary_mean-(3*salary_std)
upper_bound=salary_mean+(3*salary_std)

df=df[(df['Salary']>=lower_bound)&(df['Salary']<=upper_bound)]

df.to_csv('Cleaned_Indian_Employee.csv',index=False)
print("data cleaning completed")


