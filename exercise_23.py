#exercise_23.py
# Write a program that counts the number of occurances of a specific word in a text file

import re

def count_word_occurance(filename, word):
    try:
        with open(filename, "r") as file:
            content = file.read()
            word_to_lower = word.lower()
            content_lower = content.lower()
            word_occurance = re.findall(word_to_lower, content_lower)
            count = len(word_occurance)
            print(f"Total word count of {word} is: ", count)
    except FileNotFoundError:
        print(f" Given file {filename} is not found!!")
        
        
count_word_occurance("sample.txt", "YOU")
