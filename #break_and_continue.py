#break_and_continue
# Break : Terminates the loop permaturely whrn a condition is met

for i in range(10):
    if i ==5:
        break
    print(i)

print("Outside the loop")


#continue :  skips the current iteration and ptoceeds to the next

for i in range(10):
    if i ==7:
        continue
    print(i)
    
print("Outside the loop")

# print only odd numbers 

for i in range(10):
    if i%2 == 0:
        continue
    print(i)