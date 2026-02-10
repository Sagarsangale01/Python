#exericse_5.py 
# factorial of a number using while loop

num = int(input("Enter a number: "))
ans = 1 
inputVal = num
while num != 0:
    ans = ans * num
    num -= 1

print(f"factorial of {inputVal} is: {ans}")
