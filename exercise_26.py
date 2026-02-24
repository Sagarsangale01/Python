#exercise_26.py
# Generate 3X3 matrix and mathematical operations
import numpy as np

martix1 = np.array([[1,2,3], [4,5,6],[7,8,9]])
print("3X3 Matrix 1: ", martix1)

#transpose : means convert rows into column and colunms into rows 
transpose = martix1.T
print("Transpose matrix: ", transpose)

martix2 = np.array([[9,8,7],[6,5,4],[3,2,1]])

print("\nMatrix1 : \n", martix1)
print("\nMatrix2 : \n", martix2)
print("\nMathematical operations on this two matrix:\n")

print("\nAddition: \n", martix1 + martix2)
print("\nsubtraction: \n", martix1 - martix2)
print("\nMultiplication: \n", martix1 * martix2)
print("\nDivision: \n", martix1 / martix2)