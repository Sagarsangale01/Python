#exercise_44.py
# Merge three datasets and analyze relationships between them
import pandas as pd
import numpy as np

#Dataset 1: Employee
employee = pd.DataFrame({
    "EmployeeId": [1,2,3,4,5],
    "Name":["Gayatri", "Samiksha", "Sagar", "Priyanka", "Gauri"],
    "DepartmentId": [101,102,103,104,105],
    "Salary":[50000,60000,70000,80000,90000]
})

print("\n Dataset 1: Employee: \n", employee)

#Dataset 2: Departments
departments = pd.DataFrame({
    "DepartmentId": [101,102,103,104,105],
    "DepartmentName": ['IT', 'HR', 'Finance', 'Marketing','Sales']
}) 
print("\n Dataset 2: Departments: \n", departments)

#Dataset 3: Performance
performance = pd.DataFrame({
    "EmployeeId":[1,2,3,4,5],
    "PerformanceScore": [85,95,30,49,85]
}) 
print("\n Dataset 3: Performance: \n", performance)


# Merge employee with departments
merge1 = pd.merge(employee, departments, on="DepartmentId", how="inner")
print("\n Dataset 4: Merge employee with departments: \n", merge1)

# merge new merge1 with performance dataset
final_df = pd.merge(merge1, performance, on="EmployeeId", how="inner")
print("\n Dataset Final: merge new merge1 with performance dataset: \n", final_df)


## Analyze Relationships

#Average Salary by Department
print("Average Salary by Department: \n", final_df.groupby("DepartmentName")["Salary"].mean())

#Average Performance by Department
print("Average performance by Department: \n", final_df.groupby("DepartmentName")["PerformanceScore"].mean())

# Correlation between salary and performance
print("Correlation between salary and performance: \n", final_df[["Salary", "PerformanceScore"]].corr())