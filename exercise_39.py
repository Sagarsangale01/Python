#exercise_39.py
# Save filtered data to a new CSV file
import pandas as pd

# sample data 
data = {
    "Name": ["Amit", "Sagar", "Gayatri", "Priya", "Ashwini"],
    "Department": ["IT", "HR", "Finance", "Marketing", "IT"],
    "Salary": [30000, 35000, 40000, 50000, 60000]
}

df = pd.DataFrame(data)

print("Original DataFrame = ", df)

# step1: Filter data (salary > 35000)

filter_df = df[df["Salary"] > 35000]

print("\n Filtered data (salary >35000): \n", filter_df)

#step2: save to CSV
filter_df.to_csv("filtred_csv.csv", index=False)

print("\n Filtered data saved into filtred_csv.csv file")