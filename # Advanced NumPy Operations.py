# Advanced NumPy Operations 
 
 # Broadcasting in NumPy: broadcasting allows numPy to perform arithmatic operations on arrays on different shapes.
    # smaller array are automaticlay expaded to match the shapes of larger arrays
 
# Rules of Broadcasting:
        #1. Dimensions are aligned from the right
    # A dimension is compatible if:
        #1. It matches the other arrays dimension
        #2. One of the dimensions is 1 

import numpy as np

# Array and scalar broadcasting
arr = np.array([1,2,3])
print(arr+10)

matrix = np.array([[1,2,3],[4,5,6]])
vector = np.array([1, 0, 1])
print(matrix + vector)


## Aggregation Functions 
# it compute summary statistics for arrays
## Common FUnctions 

array1 = np.array([[1,2,3], [4,5,6]])

print("Sum: ", np.sum(array1))
print("Mean: ", np.mean(array1))
print("Max: ", np.max(array1))
print("Min: ", np.min(array1))
print("standard Devistion: ", np.std(array1))
print("sum along rows: ", np.sum(array1, axis=1))
print("Sum a long columns: ", np.sum(array1, axis=0))


# Boolean Indexing and Filtering:
    # Boolean array or condition for filter arrays 
    
array2 = np.array([1,2,3,4,5,6,7,8,9]) 
# filter and return even numbers
even = array2[array2 % 2 ==0]
print("EVENS = ", even)

# if array2 value is greater than 3 then print it 0 in array
array2[array2 > 3] = 0
print("Modified array: ", array2)
 
 
## Random Number Generation and setting seeds

#Random number generation using np.random

random_array = np.random.rand(3,3)
print("Random Array: ", random_array)

random_int = np.random.randint(1,10, size=(3,2))
print("Random int Array: ", random_int)
 
## Setting Random Seeds:  after seting aseeds as below it cant change the random vlaues 
np.random.seed(26)

random_array1 = np.random.rand(3,3)
print("Seed Random Array: ", random_array1)

random_int2 = np.random.randint(1,10, size=(3,2))
print("Seed Random int Array: ", random_int2)
