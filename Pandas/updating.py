import pandas as pd

data={
    "Name":["Ram","Shyam","Ganshyam","Dhanshyam","Amit","Jagdish","Raj","Simran"],
    "Age":[28,34,22,30,29,40,25,32],
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
    "Performance Score":[85,90,78,92,88,95,80,89]
}

df=pd.DataFrame(data)

# loc is used to access data at any point and we can update data
#syntax- df.loc[row_index,"column_name"]=new_value

#In df,Ram has salary of 50000,we will update it to 60000
df.loc[0,"Salary"]=60000
print(df)