# Data Structures -- Tuples
# TUPLES are orderd so we can access it by index like 0, 1,2,...
#TUPLES -- Tuples are similar to list. its orderd imutable collection of data items

### mutable means it can be change (append, delete from this)
## imutable means if we can add then cant be change after words.
### We cant change the tuples once it set
### it will create using rounded brackets ()

# Creating tuple

#multi value
color_tuple = ("red", "blue", "green")

#single vlaue  --  need to add , (comma) after single value in single valued tuple

single_tuple = ("one",)

#Accessing elements 

#by index
print("Accessing tuple by Index: ", color_tuple[0])

#by Negatie index -- it start counting from last element of tuple

print("Accessing element using -ve index: ", color_tuple[-1])
