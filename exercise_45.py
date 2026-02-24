#exercise_45.py
# Convert categorical data to numerical using one-hot encoding
import pandas as pd
import numpy as np

data={
    "Name": ["Sagar", "Samiksha", "Gayatri", "Priyanka", "Ashiwini"],
    "Department": ["IT", "Marketing", "Sales", "Finance", "HR"],
    "Gender":["Male", "Female", "Female", "Female", "Female"]
}

df = pd.DataFrame(data)

print("Original DataFrame: \n", df)

# One-hot encoding
# Method 1: uisng pd.get_dummies()
encoded_df = pd.get_dummies(df, columns=["Department", "Gender"])
print("\n One-Hot Encoding DataFrame: \n", encoded_df)

# drop one column (avoid dummy variable Trap)
encoded_df = pd.get_dummies(df,columns=["Department", "Gender"], drop_first=True)

print("\n drop one column (avoid dummy variable Trap): \n", encoded_df)
