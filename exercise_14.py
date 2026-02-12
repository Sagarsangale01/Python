#exercise_14.py
# store the students grade in dictionary and calculate the average grade 

#initialize the empty dictionary
student={}

n = int(input("How many students do you want to add: "))
print("Total number of students: ", n)

while n > 0:
    name = input("Enter Student name: ")
    grade = float(input("Enter students Grade: "))
    student[name] = grade
    n-=1
    
print("final student dictionary is: ", student)

total = len(student)
print("total student count: ", total)

totalGrade = sum(student.values())
print("total Grade: ", totalGrade)

averageGrade = totalGrade/total
print("Average Grade: ", averageGrade)

