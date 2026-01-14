import pandas as pd
student_total={"s1":460,"s2":475,"s3":490,"s4":485}
series=pd.Series(student_total)
print(series["s3"])
