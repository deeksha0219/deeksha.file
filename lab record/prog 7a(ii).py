import pandas as pd

df = pd.read_csv('1experience.csv')

print("First 6 rows of the DataFrame:")
print(df.head(6))

print("\nColumn names and data types:")
print(df.info())
