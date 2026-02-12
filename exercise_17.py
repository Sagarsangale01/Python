#exercise_17.py
# count the number of vowels in string

def count_vowels(text):
    vowels = 'aeiouAEIOU'
    count = 0
    for ch in text:
        if ch in vowels:
            count +=1 
    return count

string = input("Enter the string: ")
print("You enterd: ", string)
print(f"Total number of vowels present in {string} is: ", count_vowels(string))
