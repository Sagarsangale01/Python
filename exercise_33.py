#exercise_33.py
# Write a program to generate a dataset of random floats and normalize the values between 0 and 1 

import numpy as np

# generate random datasets
data = np.random.uniform(10, 200, size=100)
print("Original Data: \n ", data)

#normalize (min-max scaling)
min_val = np.min(data)
max_val = np.max(data)

normalized_data = (data-min_val) / (max_val - min_val)
print("Normalized Data (0 to 1): ", normalized_data)

# verify
print("\n Min after Normalization: ", np.min(normalized_data))
print("\n Max after normalization: ", np.max(normalized_data))