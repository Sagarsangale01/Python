# Introduction to pandas for data Manipulation
# Pandas: Pandas is a powerfull python library for data manipulation and analysis. it provides a eassy to use data structure which is series and data sets.
import pandas as pd

 ## Pandas Data Structures
    #1) Series: Series is a one dimentional labled array. capeble of holding any type of data type
s = pd.Series([10,20,30],  index = ["a","b","c"])
print(s)

    #2) Data Frame: Data frame is a two dimentional labled Data structure.
data = {"Name": ["Alice", "Bob"], "Age": [25, 30]}
df = pd.DataFrame(data)
print(df)
    
# Loading Data from CSV, Excel, and Other Sources
df = pd.read_csv("data.csv")
df = pd.read_excel("data.xlsx")

# Saving Data  save to CSV and save to Excel
df.to_csv("data.xlsx", index=False)
df.to_excel("data.xlsx", index=False)

# Basic Data frame operations
    #1. Viwing data: 
    
print(df.head())   #-- print first 5 rows
print(df.tail(3))  # -- last 3 rows

print(df.info())      #-- information summary of data frame
print(df.describe())  #-- it gives stastical summary for data frame

# selecting and indexing

# select perticular colums
print(df["Name"])  #-- select single column
print(df[["Name", "Age"]])  #-- #select multiple column


# filter rows whose age > is greater than 25
print(df[df["Age"]> 25]) #-- it returns perticulate Data sets based on conditions

# selecting by a perticular position
print(df.iloc[0]) #-- it returns the first row of the postion
print(df.iloc[:, 0]) #-- it returns the first Column of the postion


## Selecting by lable 
print(df.loc[0]) #--it returns first row by index
print(df.loc[:, "Name"]) #--it returns by lable (here name column)

