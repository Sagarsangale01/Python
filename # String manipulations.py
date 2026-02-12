# String manipulations 

#concatenation: -- process of combining multiple strings using + (plus) operator or join method
first = "Hello"
second = "Sagar"
#using + operator
result = first+" "+second
print("srting concatenation: ", result)


# Slicing -- it returns sub string form the main string

text = "Hello sagar how are you? are you learning a python programming"

print("slice for 0 to 5 means it return hello: ", text[0:5])
print("slice for 6 to 11 means it return hello: ", text[6:11])
print("it returns last word: ", text[-11:])

# formating -- it use for dynamic string creation
name = "sagar"
age = 32
print(f"My name is {name} and my age is {age} years old.")
