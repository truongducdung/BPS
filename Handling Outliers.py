import numpy as np
import pandas as pd
# Read data into DataFrame:
df = pd.read_csv("Sales Data.csv")
outlier_columns = ['column17', 'column25']  # List of column names containing outliers
threshold_upper = 8  # Upper threshold for outlier value
outliers = []
for column in outlier_columns:
    z_scores = np.abs((df[column] - df[column].mean()) / df[column].std())  # Calculate z-score for each value
    outliers.extend(df[column][z_scores > threshold_upper].index.tolist())  # Add indexes of outliers that exceed the above threshold
    outliers.extend(df[column][z_scores < threshold_lower].index.tolist())  # Add indexes of outliers below the lower threshold
outliers = list(set(outliers))  # Remove duplicate indexes
df_cleaned = df.drop(outliers)  # Remove rows containing outliers
df_cleaned.to_csv("data_cleaned.csv", index=False)  # Store the DataFrame with outliers removed into a CSV file