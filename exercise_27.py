#exercise_27.py
# Generate 4X4 matrix and calculate the sum of its rows and colmns 
import numpy as np

# Generate 4x4 martix with random numbers(1-9)
martix = np.random.randint(1,10, size=(4,4))
print("4x4 martix: \n", martix)

# row sums (axis =1 --> horizontal)
row_sum = np.sum(martix, axis=1)

# column sums (axis = 0 --> vertical)
col_sum = np.sum(martix,axis=0)

print("Row sum =", row_sum)
print("col sum =", col_sum)

print("\n Row Sums: ")
for i, total in enumerate(row_sum):
    print(f"row {i+1} sum = {total}")

print("\n Column Sums: ")
for i, total in enumerate(col_sum):
    print(f"Column {i+1} sum = {total}")