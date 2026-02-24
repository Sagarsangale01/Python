#exercise_36.py
# Select specific columns and filter rows
# https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv

import pandas as pd

# load Dataset
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

selected_columns = df[["species", "sepal_length"]]
print("selected columns: \n", selected_columns)

filtered_rows = df[(df["sepal_length"] > 5.0) & (df["species"] == "setosa")]
print("filtered rows: \n", filtered_rows)
