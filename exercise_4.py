#exercise_4 : Create a menu driven calculator

#add 
def add(a, b):
    return a+b

#subtract
def sub(a, b):
    return a-b

#multiplication
def multiply(a,b):
    return a*b
#divide
def divide(a,b):
    if b!=0:
        return a/b
    else:
        return "Division by 0 not allowed"
    
while True:
    print('\n Menu: \n')
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "5":
        print("Exiting Program \n THANK YOU!!!")
        break
    
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))
    
    if choice == "1":
        print("\nSelected Operation: Addition")
        print(f"Entered Number: {number1} and {number2}")
        print("Result is: ", add(number1, number2))
    elif choice == "2":
        print("\nSelected Operation: Substraction")
        print(f"Entered Number: {number1} and {number2}")
        print("Result is: ", sub(number1, number2))
    elif choice == "3":
        print("\nSelected Operation: Multiplication")
        print(f"Entered Number: {number1} and {number2}")
        print("Result is: ", multiply(number1, number2))
    elif choice == "4":
        print("\nSelected Operation: Division")
        print(f"Entered Number: {number1} and {number2}")
        print("Result is: ", divide(number1, number2))
    else:
        print("\nInvalid Choice. Please retry again")
        