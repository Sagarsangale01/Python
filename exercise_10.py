#exercise_10.py

import custom_function_string_functions as sf

str = input("Enter the string: ")

print("your entered string is: ", str)

# check reverce string
revString = sf.revers_string(str)
print(f"Reverce string for {str} is {revString}")

# check vowels
resVowels = sf.count_voels(str)
print(f"vowels count in given string {str} is {resVowels}")

#check Is palindrom or not
resIsPali = sf.check_palindrom(str)
print(f" {str} is Palindrom: {resIsPali}")
