#exercise_46.py
# Group Data by a categorical column

import pandas as pd

data ={
    "Class":["A","B","C","A","B"],
    "Score":[85,50,40,60,30],
    "Age":[15,28,34,23,16]
}

# create data frame 
df = pd.DataFrame(data)
print("Original Dataset: ", df)

# groupby class and calculate mean
grouped = df.groupby("Class").mean()
print("Group by Class: ", grouped)



