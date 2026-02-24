#exercise_43.py
# Drop columns with more than 50% missing values
import pandas as pd
import numpy as np

# Sample DataFrame
data= ({
    "A": [1,2,np.nan,4,5],
    "B": [np.nan,np.nan,np.nan,4,5],
    "C": [10,20,30,40,50],
    "D":[np.nan,2,np.nan,4,np.nan]
})

df = pd.DataFrame(data)

print("Original Dataframe: \n", df)

#drop columns with more than 50&=% missing values

threshold = len(df) * 0.5

df_clean = df.dropna(axis=1, thresh=threshold)

print("\n Dataframe after dropping columns > 50% missing: \n", df_clean)