#Define_functions_using_DEF_keyword

# def function_name(parameters):
   # code block
   # return result
   
   
# function with parameter and return result 

def addition(a, b):
    #c = a+b
    #return c
    return a+b

result = addition(5, 3)
print("Addition of two number is:", result)



# Variable scopes 

#Global 

globalMeg = "Sagar"
def say_hello():
    print(f"Say Hello to {globalMeg} from Say hello function") 

say_hello()
print(f"Say hello to {globalMeg} from outside the function globaly")



#local
def greet():
    message = "Hello World" 
    print("Local scope for message Varibale: ",message)
    

greet()

print("Glogal sope for message veriable: ", message)   
