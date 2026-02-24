#exercise_38.py
# Create a DataFrame from a dictionary and add a new calculated column

import pandas as pd

# step 1: Create Dictionary
data= {
    "Name": ["Amit", "Neha", "Sagar", "Gayatri", "Priya"],
    "Salary": [60000,45000, 75000, 50000,82000],
    "Experience_years": [3,2,5,2,6]
}

# Step2: Create DataFrame
df = pd.DataFrame(data)
print("Original Dataframe: \n", df)

# Step3: Add calculated column (Bonus = 10% of salary)
df["Bonus"] = df["Salary"] * 0.07

print("\n Data frame with Bonus Column: \n", df) 
