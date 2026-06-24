"""
head(),default-5,Prints Starting n rows
tail(),default-5,Prints Ending n rows
"""

import pandas as pd

df=pd.read_json("D:\Asus\OneDrive\Desktop\Data-Analyst\Pandas\sample_Data.json")

#print(df)

#Starting 5 rows
print(df.head())

#Ending 5 rows
print(df.tail())