# Data Structures -- Dictionaries
 ## it stores key value pair for fast lookups
 # in Dictionarie we access values using keys not by index
 ### it will create using curly brackets {}
 
 #creating Dictionarie
student = {"name": "Sagar", "age": 25, "location": "Nashik"}

# accessing Dictionarie
print(student)
print(student["age"])
print(student["name"])
print(student["location"])

#modifying Dictionarie
    #1 Add new key value pair
student["subject"] = "Math"

print("Dictionarie after mofification:  Added new key value pair: ", student)

 #2 Update existing key value
 
student["age"] = 32

print("Dictionarie after mofification:  Updated existing key value pair: ", student)

 #3 remove for Dictionarie
 
    #1 USING del keyowrd
del student["age"]
print("Dictionarie after mofification remove item:  USING del keyowrd: ", student)

    #2 using pop     
student.pop("subject")
print("Dictionarie after mofification remove item:  USING POP: ", student)


#Iteration of Dictionarie
for key, value in student.items():
    print(key, value)
    