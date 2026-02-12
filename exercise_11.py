#exercise_11.py
# manipulate data in dictionary

student ={"name":"Sagar","age":25, "class": "msc","grade":"B"}
print("Initial dictionary is: ", student)

# add new key value pair in dictionary
student["address"] = "123, new street, nashik"
print("Dictionary after new key value added: ", student)

# Update existing key value 
student["grade"] = "A++"
print("Dictionary after Updated existing key value : ", student)

#check is class is present if yes then delete it from Dictionary
if "class" in student:
    del student["class"]
    print("Dictionary after delition of existing key value : ", student)


print("Final Dictionary after All manipulation : ", student)
