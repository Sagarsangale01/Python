#exercise_40.py
# Clean Dataset by Handling Missing values and Renaming
import pandas as pd
import numpy as np

# Create a sample Dataset
data={
    "Name": ["Sagar", "Gayatri", np.nan, "Priya","Sami"],
    "Age": [31,np.nan, 28,32,24],
    "Score":[89,63,np.nan,88,56],
}

df = pd.DataFrame(data)

print("Original Dataframe: \n", df)

# fill missing values

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Score"] = df["Score"].interpolate()

df = df.rename(columns={"Name": "Student_name", "Score":"Exam:Score"})

print("After Fill: \n", df)

