#exercise_28.py
# Write a program to normalize an array (scale values between 0 and 1)
import numpy as np

# example array
arr = np.array([10, 20, 30, 40,50])
print("Original Array: ", arr)

#min-Max Normalizarion

min_val = np.min(arr)
max_val = np.max(arr)

normalized = (arr-min_val) / (max_val - min_val)

print("\n Normalized array (0 to 1): ")
print(normalized)