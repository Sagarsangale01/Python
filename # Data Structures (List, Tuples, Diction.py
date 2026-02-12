# Data Structures - List
# list are orderd so we can access it by index like 0, 1,2,...
# LIST - List are orders, mutable collections that can hold verity of dataTypes
## mutable means it can be change (append, delete from this)
## imutable means if we can add then cant be change after words.
### it will create using square brackets []

#Create list 
numbers = [1,2,3,4,5]

fruits = ["Apple", "Banana", "Orange"]

mixedList = [1,'Apple', True]


#Accessing elements 
    #1 By index
print("By index: ",numbers[2])
print("By index: ",fruits[2])
print("By index: ",mixedList[2])

#2 Negative indexing  -- it start counting from last element of list

print("By Negative indexing: ",numbers[-1])
print("By Negative indexing: ",fruits[-1])
print("By Negative indexing: ",mixedList[-1])

print("Original List: ", fruits)
## MOdifying List
        #1 Add items
        #using append keyword  -- it add new element at the end of list
fruits.append("cheery")
print("Added new item using Append: ", fruits)

    # Add item using insert keyword -- it will add value at specific position
fruits.insert(1, "greps")
print("Added new value using insert: ", fruits)        

    #2 Remove item
        #using remove function  -- it delete by value
fruits.remove("Banana")
print("Remove by value from fruit list which is banana: ", fruits)

        #using del keyword  =-- it delete by indx
        
del fruits[-1]

print("Delete value using index: here need to delete cheery:  ", fruits)
        
    #using pop function  -- it will removes last element
    
fruits.pop()
print("Remove element using POP function it will remove last element form list: ", fruits)


#Slicing List -- get only specific items form list 

newList =['One','two','three','four','five']
sliced_Array = newList[1:3]
print("Return sliced array it will return subarry based on given values: ", sliced_Array)



