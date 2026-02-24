#exercise_30.py
# Broadcasting operrations 

import numpy as np

martix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("\nOriginal Matrix: \n", martix)
vector = np.array([1, 0, -1])
print("\nOriginal Vector: \n", vector)

result_add = martix + vector
print("\nAdd: \n", result_add)

result_mul = martix * 2
print("Multiplication: ", result_mul)