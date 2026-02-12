#exercise_15.py
# create a text cleaner

import re

def clean_text(text):
    #remove punctuations
    text= re.sub(r"[^\w\s]", "", text)
    
    #remove extra spaces
    text = " ".join(text.split())

    #convert to lower case
    text = text.lower()
    
    return text
    
    
inputText = input("Enter a text for clining: ")

print("Your entered Text: ", inputText)

clearedText = clean_text(inputText)

print("Cleaned Text ===", clearedText)
