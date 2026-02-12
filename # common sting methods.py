##COMMON STRING METHODS
    #1. split() -- it split the string into a list based on the given delimiter 
    # bydefault delimiter is white space 
text = "Python is a very eassy language"
words = text.split()
print("Split using default delimiter which is space: ", words)
text1 = "Python, is a, very, eassy, language"
print("Split using specified delimiter which is (,): ", text1.split(","))
    
    #2. join() -- join elements of a list into a single string
joinWords = " ".join(words)
print("Join operation using JOIN keyword: ", joinWords)    
    
    #3. replace() -- It replace the sub string witht he another one in main string
text = "I love Java"
updated_text = text.replace("Java", "Python")
print("Replace string: ", updated_text)    
    
    #4. strip() -- it removes white space or specifiedd charectores from the biggining and end the string
messy_string = "@@@@     Hello Sagar    @@@"
print("messy string: ", messy_string)
cleaner_text = messy_string.strip("@")
print("cleaner text:", cleaner_text)
cleaner_text2 = cleaner_text.strip()
print("cleaner text2:", cleaner_text2)
    