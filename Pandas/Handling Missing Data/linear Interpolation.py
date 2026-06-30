import pandas as pd

data={
    "Time":[1,2,3,4,5],
    "Value":[10,None,30,None,50]
}

df=pd.DataFrame(data)
print("before Interpolation")
print(df)

#interpolate add a missing value by looking at other value trends 
print("After Interpolation")
df['Value']=df["Value"].interpolate(method="linear")
print(df)