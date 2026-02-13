#exercise_22.py
# Write a program to copy the contents from one file to another 

def copy_content(filename1, filename2):
    try:
        with open(filename1,"r") as file:
            content = file.read()
            if len(content) == 0:
                print(f"Ther is no any content in the given {filename1} file")
            else:
                with open(filename2, "w+") as file1:
                    file1.write(content)
                    print(f"We have copy the content from {filename1} into the {filename2} successfully")
                    
    except FileNotFoundError:
        print(f"Given file name {filename1} is not found")
                


def read_files(filename1, filename2):
    
    file_list = [filename1, filename2]
    
    try:
        for file in file_list:
            with open(file, "r") as file1:
                file_content = file1.read()
                print(f"{file} content is: ",file_content)
    except FileNotFoundError:
        print("Given file is not found")


copy_content("sample.txt", "copy_sample.txt")
read_files("sample.txt", "copy_sample.txt")