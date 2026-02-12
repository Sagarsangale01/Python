#exercise_16.py
# check if string palindrom or not 
def is_palindrom(text):
    text = "".join(char.lower() for char in text if char.isalnum())
    return text == text[::-1]

text = input("Enter the string: ")
print("You have entered the: ", text)

print(f"Given string {text} is palindrom: ", is_palindrom(text))
