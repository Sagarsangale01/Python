# Data Structures -- Sets
#sets are unorderd collections of unique items 
### it will create using curly brackets {}

#creating sets
numbers ={1,2,3,4,5}
print("set: numbers : ",numbers)
empty_set = set()
print("set: empty_set : ",empty_set)


# add elements in set
numbers.add(6)
print("added new element in numbers set: ", numbers)

empty_set.add(2)
print("added new element in: empty_set : ",empty_set)


# REmove elements from the set

numbers.remove(3)
print("Removed element from numbers set: ", numbers)

empty_set.remove(2)
print("Removed element from empty set: ", empty_set)


#set operations
    #1 union -- using | (pipe symbol)
    # It returns combin sets with unique values
set1 = {1,2,3}
set2 = {3,4,5}
setUnion = set1 | set2
print("Set union: ", setUnion)

    #2 intersection  -- using & (and symbol)
    # it returns only common values from both sets 
setIntersection = set1 & set2
print("Set intersection: ", setIntersection)

    #3 Difference -- using - (minus symbol)
     # it return values from set1 which is not in set2
setDifference = set1 - set2
print("Set Difference: ", setDifference)
    