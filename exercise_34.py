#exercise_34.py
# Implement Conditional replacment to create a binary mask for values above a threshold
import numpy as np

# Generate random float dataset

data = np.random.uniform(0, 100, size=(5,5))
print("Original Data: \n", data)

#define threshold 
threshold = 50

# Create binary mask

mask = np.where(data > threshold,1,0)
print("Binary mask Data (1 if > 50, else 0): \n", mask)
