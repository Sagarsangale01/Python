#exercise_12.py
# word frequency counter 

getSentence = str(input("Please enter the sentence: "))
print("Your given sentance is: ", getSentence)

# spilit the sentence into words
words = getSentence.split()
print("Returns the words list from sentence: ", words)

#initialize the empty dictionariy

world_count = {}

for word in words:
    word = word.lower()
    if word in world_count:
        world_count[word] +=1
    else:
        world_count[word] = 1
        
print("final word count form the given Sentence: ", world_count)
