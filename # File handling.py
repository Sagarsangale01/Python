# File handling 
## reading and writing text files
    #1. file opening: -- use built-in open() to open file
        # file opening modes --
        # r -- read
        # w -- write (it overwrite the file if allready exist)
        # a -- append (added data to the end of file) 
        # r+ -- read and write 
    
    #2. File reading :
        # .read() -- to read the entire file content 
        # .readline() -- to just read one line at a time
        # .readlines() -- to read all the lines and give the list of the entire items
        
# with open("sample.txt","r") as file:
#     # read() -- to read the entire file content
#     content = file.read()
#     print("File content: ", content)
#      # readline() -- to just read one line at a time
#     contentline = file.readline()
#     print("File content read one line at a time: ", contentline)
#      # readlines() -- to read all the lines and give the list of the entire items
#     contentlines = file.readlines()
#     print("File content read all the lines and give the list of the entire items: ", contentlines)

        
    #3. Writing Files: -- 
        # .write() -- write a string into a perticular file
        # .writelines() -- to write multiple lines from a list 
        
# with open("sample.txt", "w") as file:
#         # .write() -- write a string into a perticular file        
#         file.write("HEllo sagar. this is the content which is added by me")
#         print("File content after WRITE: ", file)
     
#         # .writelines() -- to write multiple lines from a list 
#         file.writelines(["HEllo sagar", "this is the content which is added by me","Now this using writelines function", "WRITE LINES"])
#         print("File content after WRITE LINES: ", file)
    
## USING With statment for file managment 
# WITH - using with it ensurase the opend file oprperly closed after the operation or even if any exception is occured
# it close file automatically 
# with ADVANTAGES -
    # simplifies code 
    # Reduce the risk of file corruption
    
## Basic exceptions handling for file operations
    #why use exceiption handling: -- 
        # Prevents the program from crashing due to file related errors (e.g. - file not found)
    
# using try - except Blocks
try:
    with open("sample1.txt", "r") as file:
        print("File content: ", file.read())
except FileNotFoundError:
    print("File not found!!!")
    
    
#Common File handing exceptions 

   # FileNotFoundError
   # PermissionError
   # IOError
