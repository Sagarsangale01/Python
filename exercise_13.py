#exercise_12.py
# reverce the list and remove dupblicates using set
numbers = [1,2,3,4,2,3,5,2,1,3,4,3,5]
print("Given list is:", numbers)

reverse_list = numbers[::-1]
print("reverce list is:", reverse_list)

uniqueList = set(reverse_list)
print("Unique list using set: ", uniqueList)


