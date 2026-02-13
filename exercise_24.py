#exercise_24.py
# Write a program to log messages with timestamps into a file 
from datetime import datetime

def log_messages(filename, message):
    with open(filename, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")    
          # Format log entry
        log_entry = f"[{timestamp}] {message}\n"
        file.write(log_entry)
        print(f"New log added in {filename}")
    
    read_logs(filename)
    

def read_logs(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            print(f"{filename} Log file content is: \n",content)
            
    except FileNotFoundError:
        print(f" Given file {filename} is not found!!")
        
        
message = input("Please enter log message: ")

log_messages("LogFile.txt",message)