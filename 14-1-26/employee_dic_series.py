import pandas as pd
employee={"id":1234,"name":"arya","age":22,"place":"mukkala"}
series=pd.Series(employee)
print(series["name"])