#custom_function_string_functions.py

#function for reverse the srting
def revers_string(string):
    res =[]    
    for i in range(len(string)-1,-1,-1):
        res.append(string[i])
    return "".join(res)
    
    

#function for count vovels 
def count_voels(s):
    vovels = 'aeiouAEIOU'
    count = 0

    for ch in s:
        if ch in vovels:
            count +=1
            
    return count        
            

# function for check string is palindromes or not            
def check_palindrom(s):
    text = s.lower()
    left = 0
    right = len(text)-1
    
    while left < right:
        if text[left] != text[right]:
            return False
        left +=1
        right -=1
    return True