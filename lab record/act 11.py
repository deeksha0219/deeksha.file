import pandas as pd

df = pd.read_csv(r"CASHANTIR VU\Programs\Minors\IDA\Activities\Datasets\6Mednull_values.csv")

print("Original DataFrame:")
print(df)

print("\nMissing values in the DataFrame:")
print(df.isnull().sum())

df.fillna(df.mean(numeric_only=True), inplace=True)  
df.fillna(method='ffill', inplace=True)  
print("\nDataFrame after filling all missing values:")
print(df)

df.drop_duplicates(inplace=True)
print("\nDataFrame after dropping duplicates:")
print(df)
