#exercise_32.py
# Create a 3D random array and compute statistics along specific axes
import numpy as np

matrix = np.random.randint(0,11, size=(3,3))
print("original 3x3 Matrix: ", matrix)

rows = np.sum(matrix, axis=1)
print("Row Addition: ", rows)

col = np.sum(matrix,  axis=0)
print("Col Addition: ", col)

