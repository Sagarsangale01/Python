#exercise_49.py
# Use pivot_table to calculate total sales per region and per year
import pandas as pd
import numpy as np

data ={
    "Order_ID": range(101,111),
    "Region": ["North", "South", "East", "West", "North", "East", "West", "East", "West", "North"],
    "Sales_Amount":[25000, 12000,30000,25000,28000,11000,24000,19000,28000,30000],
    "Order_Date": pd.to_datetime([
        "2024-01-10", "2022-03-15", "2026-07-22", "2026-09-30",
        "2024-02-11", "2022-04-18", "2026-06-25", "2026-08-09",
        "2025-01-05", "2025-03-12"
    ])
}

df= pd.DataFrame(data)
print("\nOriginal Dataset: \n", df)

# Extract Year
df["Year"] = df["Order_Date"].dt.year
print("\n After Extract Year: \n", df)


## Pivot Table: Total Sales per Region per year
pivot_table = pd.pivot_table(
    df,
    values="Sales_Amount",
    index="Region",
    columns="Year",
    aggfunc="sum",
    fill_value=0,
    margins_name="Total",
    margins= True
)

print("\n Total Sales per Region per Year: \n", pivot_table)

