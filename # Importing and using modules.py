# Importing and using modules

# import an entire module
import math
print(math.sqrt(16))


# import only specific function
from math import sqrt
print(sqrt(16))


# use module name alices insted of full name 
import math as m
print(m.sqrt(16))