import numpy as np
import pandas as pd
# Read data into DataFrame:
df = pd.read_csv("Website Access Data.csv")
inconsistent_formats = ['column5']  # The list of column names contains inconsistent formatting
for column in inconsistent_formats:
    df[column] = pd.to_datetime(df[column], format="%d/%m/%Y")  # Convert format dd/mm/yyyy
    df.dtypes  # Check the format of the columns in the DataFrame
    df.to_csv("data_formatted.csv", index=False)  # Store the converted DataFrame into a CSV file