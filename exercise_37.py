#exercise_37.py
# Load a local excel file and explore its structure

import pandas as pd

df = pd.read_excel("sample_data.xlsx")

print("\nFirst 5 rows: \n ", df.head())
print("\nShape of dataset: \n", df.shape)
print("\n Column Names: \n", df.columns)
print("\n Dataset Info: \n", df.info())
print("\n Summary statistics: \n", df.describe())