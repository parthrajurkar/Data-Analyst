import pandas as pd

data={
    "Name":["Ram",None,"Ganshyam","Dhanshyam","Amit","Jagdish","Raj","Simran"],
    "Age":[28,None,22,30,29,40,25,32],
    "Salary":[50000,None,45000,52000,49000,70000,48000,58000],
    "Performance Score":[85,None,78,92,88,95,80,89]
}

df=pd.DataFrame(data)
print(df)

# dropna deletes nan/null value rows or columns
#syntax- dropna(axis=0,inplace=True),axis - 0 means it works on rows,1 means on column
#inplace - True,returns orignal df,false returns copy
df.dropna(inplace=True)
print(df)