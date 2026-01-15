import pandas as pd
sales_report = [
    {"date": "2026-01-01", "product": "Laptop", "category": "Electronics", "quantity": 2, "price": 55000, "salesperson": "Anil"},
    {"date": "2026-01-01", "product": "Mouse", "category": "Electronics", "quantity": 5, "price": 500, "salesperson": "Meera"},
    {"date": "2026-01-02", "product": "Chair", "category": "Furniture", "quantity": None, "price": 3500, "salesperson": "Rahul"},
    {"date": "2026-01-02", "product": "Desk", "category": "Furniture", "quantity": 1, "price": None, "salesperson": "Rahul"},
    {"date": "2026-01-03", "product": "Pen", "category": "Stationery", "quantity": 20, "price": 10, "salesperson": None},
    {"date": "2026-01-03", "product": "Notebook", "category": "Stationery", "quantity": 10, "price": 50, "salesperson": "Anil"},
    {"date": None, "product": "Printer", "category": "Electronics", "quantity": 1, "price": 12000, "salesperson": "Meera"},
    {"date": "2026-01-04", "product": "Monitor", "category": "Electronics", "quantity": 2, "price": None, "salesperson": "Anil"},
    {"date": "2026-01-05", "product": None, "category": "Furniture", "quantity": 1, "price": 8000, "salesperson": "Rahul"},
    {"date": "2026-01-05", "product": "Table Lamp", "category": None, "quantity": 3, "price": 1500, "salesperson": "Meera"}
]
df=pd.DataFrame(sales_report)
print(sales_report)
print(df.shape)
print(df.columns)
print(df.info())
print(df.head())
print(df.tail())
print(df.isnull().sum())
most_frequent_date=df["date"].mode()[0]
df["date"].fillna(most_frequent_date,inplace=True)#inplace=true thannittulla data modify cheythal mathi
print(df)
df["product"].fillna("unknown",inplace=True)
print(df)
most_frequent_category=df["category"].mode()[0]
print(most_frequent_category)
df["category"].fillna(most_frequent_category,inplace=True)
print(df)
print(df.isnull().sum())
quantity_fill=df["quantity"].mean()
print(quantity_fill)
df["quantity"].fillna(quantity_fill,inplace=True)
print(df)
print(df.isnull().sum())
price_fill=df["price"].mean()
print(price_fill)
df["price"].fillna(price_fill,inplace=True)
print(df)
#df.dropna(subset=["category"],inplace=True)
#print(df)
df["salesperson"].fillna("arya",inplace=True)
print(df)
# sales count by category=unique count
print(df["category"].value_counts())
#sales count by sales person
print(df["salesperson"].value_counts())
#category electronics and quantity>2
print(df[(df["category"]=="Electronics")&(df["quantity"]>2)])
print(df.groupby("category")["price"].sum())
print(df.groupby("category")["quantity"].sum())
print(df.sort_values(by="price",ascending=False))
print(df.loc[2])#
print(df.iloc[1])#index vech row edukkan
#costly product
print(df.iloc[df["price"].idxmax()])
print(df.iloc[df["price"].idxmin()])
# adding new column
df["revenue"]=df["price"]*df["quantity"]
print(df)
print(df.loc[1,["product","price"]])
#fillna()fill null vales
#dropna(subset=["columnname"])
#isnull().sum()=null count
#group by()=return count of unique values
#sort values()

