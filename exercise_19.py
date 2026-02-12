#exercise_19.py
# reverce the words in a sentence (not the letters)

text = input("Enter the sentence: ")
print("You have etered: ", text)

#make sentence in words using split
words = text.split()
print("sentence in words using split: ", words)
# reverce the words
reverce_words = words[::-1]
print("reverce the words: ", reverce_words)
#join the reverce words
final_text = " ".join(reverce_words)
print("Final reverce string : ", final_text)