import numpy as np
import pandas as pd
# Read data into DataFrame:
df = pd.read_csv("Product Data.csv")
duplicate_entries = df.duplicated()  # Find duplicate records
df_cleaned = df.drop_duplicates()  # Remove duplicate records
df_cleaned.to_csv("data_cleaned.csv", index=False)  # Store the DataFrame with deduplicated records into a CSV file