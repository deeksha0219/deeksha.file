import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 70000, 80000]
}
df = pd.DataFrame(data)

print("DataFrame from Scratch:")
print(df)

df['Bonus'] = df['Salary'] * 0.10

print("\nDataFrame after adding 'Bonus' column:")
print(df)