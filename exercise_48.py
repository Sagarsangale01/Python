#exercise_48.py
# Create a dataset of sales data and group it by region or product category
import pandas as pd

data = {
    "Order_ID": [101,102,103,104,105],
    "Region": ["North", "South", "East", "West", "North"],
    "Product_Category": ["Electronics", "Clothing", "Electronics", "Furniture", "Clothing"],
    "Sales_Amount": [25000, 15000,18000, 12000,20000]    
}

df = pd.DataFrame(data)
print("Original Dataset: \n", df)

# Group by Region 
region_sales = df.groupby("Region")["Sales_Amount"].sum()
print("\n Group by Region: \n", region_sales)

# Group by Product Category
category_sales = df.groupby("Product_Category").agg(
    {"Sales_Amount": ["max", "min", "mean"]}
    )
print("\nGroup by Product Category: \n", category_sales)

## Multiple Aggregation

summary = df.groupby("Region").agg(
    Total_Sales=("Sales_Amount", "sum"),
    Average_Sales =("Sales_Amount", "mean"),
    Number_of_Orders =("Order_ID", "count")
)

print("\n Detailed Region Summary: \n", summary)