#exercise_9.py
# check number is even or not 

import custom_function_check_odd_even as odd_even

number = int(input("Enter any number: "))

print("You have entered ", number)

result = odd_even.odd_even(number)
print(f"Given number {number} is {result}")


