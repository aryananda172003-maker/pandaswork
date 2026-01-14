import pandas as pd
data={"e1":123,"e2":44,"e3":66,"e4":789,"e5":34}
series=pd.Series(data)
print("total",series.sum())
print("max",series.max())
print("min",series.min())