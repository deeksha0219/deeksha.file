import pandas as pd

products = [
    {"Product Name": "Laptop", "Category": "Electronics", "Price": 80000},
    {"Product Name": "Phone", "Category": "Electronics", "Price": 50000},
    {"Product Name": "Table", "Category": "Furniture", "Price": 15000}
]

df = pd.DataFrame(products)

df["Discounted Price"] = df["Price"] * 0.9
print(df)