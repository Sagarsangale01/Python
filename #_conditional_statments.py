#_conditional_statments

#example 1 : checking a conditions
num = -10 
if num >0:
    print("positive Number")
elif num ==0:
    print("its Zero")
else:
    print("Negative number")


#example 2: Nested conditions

age = 31

if age >1:
    if age <18:
        print("Child")
    elif age >= 18:
        if age < 30:
            print("Young")
        else:
            print("Adult")
