import pandas as pd
students={
    "name":["arya","sree","clarin","varshana","thammana"],
    "age":[22,24,22,22,18],
    "course":["ds","ds","ds","dj","dj"]



}
df=pd.DataFrame(students)
print(df)
print(df[1:3])
print(df[["name","course"]])