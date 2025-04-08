import pandas as pd

df = pd.read_csv('2Salary.csv')
salary_column = df['Salary']

mean_salary = salary_column.mean()
median_salary = salary_column.median()
mode_salary = salary_column.mode()[0]


variance_salary = salary_column.var()
std_dev_salary = salary_column.std()
min_salary = salary_column.min()
max_salary = salary_column.max()
range_salary = max_salary - min_salary


print(f"Mean: {mean_salary}")
print(f"Median: {median_salary}")
print(f"Mode: {mode_salary}")
print(f"Variance: {variance_salary}")
print(f"Standard Deviation: {std_dev_salary}")
print(f"Minimum Salary: {min_salary}")
print(f"Maximum Salary: {max_salary}")
print(f"Range: {range_salary}")
