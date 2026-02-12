# Regular Expressions for pattern matching
 # regular expression is a way to serch match based on pattern like email have some specific pattern 
 # in python predefined re (regular expression) module available 

import re

text = "Hello sagar. my email id sagar@gmail.com. my phone is 123-456-7890" 
 #Common functions
    #1. re.search(pattern, string)   -- it serch pattern in string
    
    
    
    #2. re.findall(pattern, string)  -- find all the ocurance based on pattern
digits = re.findall(r"\d+",text)
print("Regular expression for findall digits bsed on patters: ", digits)
    
    #3. re.sub(pattern, replacement, string) -- it replaces occurances of perticular pattern
updated_text = re.sub(r"\d","x",text) 
print("Regular expression for replace all digits in string: ", updated_text)
   

    
    