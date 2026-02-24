#exercise_35.py
# Load and Explore a Sample dataset
# https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv

import pandas as pd

# load Dataset 
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# explore Structure 
print("First 5 rows: \n", df.head())
print("Last 5 Rows: \n", df.tail())

print(df.info())
print(df.describe())


