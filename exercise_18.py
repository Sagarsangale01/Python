#exercise_18.py
# find and replace all email address in a text using regex

import re
text = input("Enter a string: ")
print("You have entred: ", text)
# Regex pattern for email
pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
# replace all emial IDs with [email]
updated_text = re.sub(pattern, "[email]", text)
print("Text after replacemnt: ", updated_text)


findEmails = re.findall(pattern, text)
print("All Emails: ", findEmails)