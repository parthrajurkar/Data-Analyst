import pandas as pd

df_customers=pd.DataFrame({
    "CustomerID":[1,2,3],
    "Name":['Ramesh','Suresh','Kalpesh']
})

df_orders=pd.DataFrame({
    "CustomerID":[1,2,4],
    "OrderAmount":[250,450,350]
})

#in outer join,all values of on="" are merged,even if some doesn't match,
#values not found will be set to nan

df_merged=pd.merge(df_customers,df_orders,on="CustomerID",how='outer')
print(df_merged)