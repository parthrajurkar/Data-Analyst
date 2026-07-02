import pandas as pd

df_customers=pd.DataFrame({
    "CustomerID":[1,2,3],
    "Name":['Ramesh','Suresh','Kalpesh']
})

df_orders=pd.DataFrame({
    "CustomerID":[1,2,4],
    "OrderAmount":[250,450,350]
})

#in right join all values of right df will be kept and matching values
#from another df will be kept

df_merged=pd.merge(df_customers,df_orders,on="CustomerID",how='right')
print(df_merged)