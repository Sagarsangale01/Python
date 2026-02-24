#exercise_29.py
# Generate a random array and find the minimum and maximum values

import numpy as np

# generate random array of 10 elements between 1 to 100 
array = np.random.randint(1, 101, size =10)
print("random Array: \n", array)

#find minimum and maximum 
min_val = np.min(array)
max_val = np.max(array)

print("\n Minimum value: ", min_val)
print("\n Maximum value: ", max_val)
 
