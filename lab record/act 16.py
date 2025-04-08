import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('4laptops.csv')


print(data.head())


plt.figure(figsize=(10, 6))
plt.boxplot(data['Price'])
plt.title('Box Plot of Laptop Prices (Matplotlib)')
plt.ylabel('Price')
plt.grid(axis='y')
plt.show()


plt.figure(figsize=(10, 6))
sns.boxplot(x=data['Price'])
plt.title('Box Plot of Laptop Prices (Seaborn)')
plt.xlabel('Price')
plt.grid(axis='x')
plt.show()
