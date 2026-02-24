#exercise_31.py
# Generate and filter a random dataset
import numpy as np

np.random.seed(26)

rendom_matrix = np.random.randint(1,50,size=(5,5))
print("\nOriginal Martix: \n", rendom_matrix)

# filter the values which is greater then 25 and replace 0
rendom_matrix[rendom_matrix>25] =0
print("\nmodified_matrix: \n", rendom_matrix)

# calculate summary status
print("Sum: ", np.sum(rendom_matrix))
print("Mean: ", np.mean(rendom_matrix))
print("Max: ", np.max(rendom_matrix))
print("Standerd Deviation: ", np.std(rendom_matrix))


