#exercise_50.py
# Create a custom aggregation function to calculate the variance for each group
import pandas as pd
import numpy as np

data ={
    "Region": ["North", "South", "East", "West", "North", "East", "West", "East", "West", "North"],
    "Sales_Amount":[25000, 12000,30000,25000,28000,11000,24000,19000,28000,30000]
}

df = pd.DataFrame(data)
print("Original Dataset: \n",df)


def custom_function(series):
    mean = series.mean()
    return ((series - mean) **2).sum() / (len(series) -1)

variance_by_region = df.groupby("Region")["Sales_Amount"].agg(custom_function)
print("\n Varience of Sales by region: \n", variance_by_region)
