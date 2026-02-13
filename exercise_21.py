#exercise_21.py
# Write and read a list of items

def file_write(fileName, content):
    try:
        with open(fileName, "w") as file:
            file.writelines(content)
            print(f"your given content added in the {fileName}")
    except FileNotFoundError:
        print(f"Given file is not found {fileName}")
        
def file_read(fileName):
    try:
        with open(fileName, "r") as file:
            content = file.read()
            print("Your File content is: ", content)
    except FileNotFoundError:
        print(f"Given file is not found {fileName}")
        

content = "Hello Sagar.\n How are you.\n Where are you leaving.\n My location is nashik"

fileName = "sample.txt"


file_write(fileName, content)
file_read(fileName)