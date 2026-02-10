#exercise 
# Create a function to calculate factorials
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
def print_factorial(a):
    result = factorial(a)
    print(f"Factorial of {a} is {result}")
    
print_factorial(10)

