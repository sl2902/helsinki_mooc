# write your solution here
if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"

with open(student_info, 'r') as f:
    students = {}
    for line in f:
        row = line.strip().split(';')
        if row[0] != 'id':
            students[row[0]] = row[1:]

with open(exercise_data, 'r') as f:
    exercises = {}
    for line in f:
        row = line.strip().split(';')
        if row[0] != 'id':
            exercises[row[0]] = sum([int(i) for i in row[1:]])

for k , v in students.items():
    print(f'{students[k][0]} {students[k][1]} {exercises[k]}')
# print(students)
# print(exercises)







