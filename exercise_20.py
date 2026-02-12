#exercise_20.py
# count words and lines in a file 

try:
    with open("sample.txt", "r") as file:
        lines = file.readlines()
        print("File lines: ", lines)
        line_count = len(lines)
        word_count = sum(len(line.split()) for line in lines)
        
        print(f"Number of lines = {line_count}. \n Number of words == {word_count}.") 
        
except FileNotFoundError:
    print("File not found!!!")
