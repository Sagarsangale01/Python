#exercise_6.py
# Find the large number from the list using for loop
numList = eval(input("Enter multiple numbers using comma sepration: "))
print("Your entered List is : ", numList)
maxValue = 0
for num in numList:
    
    if num > maxValue:
        maxValue = num
    
print("largest number is:", maxValue)