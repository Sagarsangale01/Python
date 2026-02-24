# Introduction to NumPy for numerical computing

#Understanding the role of numPy in data science and AI

# What is numPy?:  numPy or numerical python is a foundational library in python for numerical compitations
                   # it provides a fast and effecient way to perform operation on large datasets using arrays and supports advance matheical functions.

# Why Use numPy in AI? :  
#     1. performance: numPy arrays are more efficient then python list
#     2. Ease to use: built in
#     3. Integration: pandas, 


# Creating and Manipulateing numPy Arrays 

# import NumPy
import numpy as np

#creating array
   #1. From a list
arr = np.array([1,2,3,4,5])
print("Array: ", arr)
    
   #2.  Using built-in functions
   # it prints zeros in 3 rows and 3 columns array 
zeros = np.zeros((3,3))
print("Zeros = ", zeros)

# it prints once in 2 rows and 4 columns array
ones = np.ones((2,4))
print("Once =", ones)

# return evenly spaced values within a given interval.
# (1: start, 100: end, 10: space between numbers like: 1, 11, 21)
range_array = np.arange(1, 100, 10)
print("Range Array =", range_array)

# Return evenly spaced numbers over a specified interval
# (0: start, 1: end, 5: number of value in between start and end)
#res: [0., 0.25, 0.5, 0.75, 1.] 
linspace_array = np.linspace(0,1,5)
print("Linspace array: ", linspace_array)


# Manipulating Arrays
  # Chnage shape
array1 = np.array([1,2,3,4,5,6,7,8,9])
reshape = array1.reshape(3,3)
print("Reshape ==", reshape)   
  
  # Add dimenrions
array2 = np.array([1,2,3])
expanded = array2[:, np.newaxis]
print("dimenrions: ", expanded)


## BASIC OPERATIONS IN ARRAY
    # element-wise Operations 
a = np.array([1,2,3])
b = np.array([4,5,6])

print("Addition of two arrays: ", a+b)
print("Subtraction of two arrays: ", b-a)
print("Multiplication of two arrays: ", a*b)
print("Division of two arrays: ", a/b)
print("module of two arrays: ", a%b)    
    
    # Mathematical Operations
array3 = np.array([4, 16, 25])
print("Square root of: ", np.sqrt(array3))
print("Sum of: ", np.sum(array3))
print("Mean of: ", np.mean(array3))
print("Max of: ", np.max(array3))    

## Array Indexing, Slicing, and Reshaping

    #1. Indexing: its a numbring for the arry of elements. we can access element of arry using index
array4 = np.array([10,20,30,40,50,60])
print("return 2nd index value: ", array4[2])
print("Return last element : ", array4[-1]) 

    #2. Slicing: Array slicing means we create small small array from one array
print("Slice the array4 from 1 to 4 index: ", array4[1:4])
print("slice array from 3 rd index: ", array4[3:])

    #3. Reshaing: reshape the array from existing array
reshaped = array4.reshape(2,3)
print("It Reshapre current 1X1 array into 2X3: ", reshaped)
    
