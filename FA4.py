students = int(input("Enter number of students: "))
subjects = int(input("Enter number of subjects: "))
score = 0
for x in range (1, students + 1):
    total = 0
    print(f"Student {x}")
    for y in range (1, subjects + 1):

        score = int(input(f"Enter score {y}: "))
        total += score
    stud_avg = total/subjects
    print(f"Average for Student {x} = ", stud_avg)
    score += stud_avg
average = score/students
print(f"Class Average = ", average)