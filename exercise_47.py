#exercise_47.py
# Calculate Summary Statistics for Grouped data
import pandas as pd

data ={
    "Class":["A","B","C","A","B"],
    "Score":[85,50,40,60,30],
    "Age":[15,28,34,23,16]
}

# create data frame 
df = pd.DataFrame(data)
print("Original Dataset: ", df)

stats = df.groupby("Class").agg(
    {"Score":["mean","min", "max"], "Age":["min", "max","mean"]}
    )
print("statistics: ", stats)