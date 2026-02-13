#Writing clean pythonic code

# what is pythonic code?
# it is best practices its focuses on redablity, simplicity

#Best Practices
    # 1. Use descriptive varible names
    # 2. write modular code with functions and classes
    # 3. follow PEP 8 style guidelines
    # 4. Avoide redundancy: leverage pythons powerfull built-ins

# List comprehensions  -- a concise way to create lists using a single line of code
# syntax   [expression for item in iterable if condition]
#ex - 
    #create a list of squares
squares = [x**2 for x in range(10)]
print("square = ", squares)

# filter even numbers  
evens = [x for x in range(10) if x % 2 ==0]
print("Even =", evens)

# filter odd numbers  
odd = [x for x in range(10) if x % 2 !=0]
print("Odd =", odd)


## Lambda functions
#    what are lambda functions?
#    -- anonymous, single-expression functions defined using the lambda keywords
## syntax   lambda agruments: expression

add = lambda x, y: x+y
print(add(3,5))


## map() -- applies a function to each item in an iterable 
numbers = [1,2,3,4,5]
squares = map(lambda x: x**2, numbers) 
print("MAP==", list(squares))   

##  filter() -- it filters items based on a condition 
evenList = filter(lambda x: x % 2 == 0, numbers)
print("FILTER ==", list(evenList))    

## reduce() -- reduces an iterable to a single value
from functools import reduce

product = reduce(lambda x,y: x*y, numbers)
print("reduce -", product)

## OS modules  -- Provides functions to interact with the operating system
import os 

print(os.getcwd())
# os.mkdir("text3")
# os.removedirs("text.txt")


## SYS module -- provides access to system -specific parameters and functions

import sys

print(sys.argv)
print(sys.version)

