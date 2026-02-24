#exercise_41.py
# Merge two datasets and perform data transformations
import pandas as pd
import numpy as np

df1 = pd.DataFrame({
    "Id":[1,2,3,4,5],
    "Name":["Sagar", "Gayatri","Priyanka","Samiksha","Gauri"],
    "Age": [32,25,33,24,25]
})

df2 = pd.DataFrame({
    "Id":[1,2,3],
    "Score":[85,89,65]
})

print("DataFrame 1: \n", df1)
print("DataFrame 2: \n", df2)

#merge dataset
merged = pd.merge(df1, df2, how="inner", on="Id")
print("merged Dataset: \n", merged)

merged["Score_Percentage"] = (merged['Score'] /100) * 100
print("Transformed Dataset: \n", merged)