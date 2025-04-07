import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# Example dataset
data = {
    'Brand': ['Dell', 'HP', 'Apple', 'Lenovo', 'Dell'],
    'Type': ['Gaming', 'Work', 'Premium', 'Gaming', 'Work'],
    'OS': ['Windows', 'Windows', 'macOS', 'Windows', 'Windows']
}
df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Label Encoding
label_encoder = LabelEncoder()
df['Brand_LabelEncoded'] = label_encoder.fit_transform(df['Brand'])
print("\nLabel Encoded Data:")
print(df[['Brand', 'Brand_LabelEncoded']])

# OneHot Encoding
onehot_encoder = OneHotEncoder()
onehot_encoded = onehot_encoder.fit_transform(df[['Type']]).toarray()
type_categories = onehot_encoder.categories_[0]  # To get the column names
type_column_names = [f"Type_{category}" for category in type_categories]
df_onehot_encoded = pd.DataFrame(onehot_encoded, columns=type_column_names)
df = pd.concat([df, df_onehot_encoded], axis=1)

print("\nOneHot Encoded Data:")
print(df)