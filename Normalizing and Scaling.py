import numpy as np
import pandas as pd
# Read data into DataFrame:
df = pd.read_csv("Product Data.csv")
columns_to_normalize = df.columns.tolist()  # List of all column names in the table
scaler = StandardScaler()
df[columns_to_normalize] = scaler.fit_transform(df[columns_to_normalize])
df.to_csv("normalized_data.csv", index=False)  # Store the DataFrame with outliers removed into a CSV file
