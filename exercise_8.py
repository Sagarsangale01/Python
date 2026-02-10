#exercise_8.py
# Custom python module and import it in another module

import math_operations as op

print("Choose Menu: ")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

choice = int(input("Enter the choice: "))

if choice == 5:
    print("Exit form the Program. \n Thank you !!!")
    exit()

number1 = int(input("Enter First Number: "))
number2 = int(input("Enter second number: "))

print(f"You have selected {choice} and entered the {number1} and {number2}")

if choice == 1:
    result = op.addition(number1, number2)
    print("Result of Addition is: ", result)
    
elif choice == 2:
    result = op.subtract(number1, number2)
    print("Result of Substraction is: ", result)

elif choice == 3:
    result = op.multiply(number1, number2)
    print("Result of Multiplication is: ", result)

elif choice == 4:
    result = op.divide(number1, number2)
    print("Result of divide is: ", result)
    
else:
    print('Invalid Choice. please try again!!')