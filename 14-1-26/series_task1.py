import pandas as pd
data=[133,45,67,89,23,46,34,33,40]
series=pd.Series(data)
print(series.head())#first 5 records
print(series.tail())#last 5 records
print(series.shape)#total elements