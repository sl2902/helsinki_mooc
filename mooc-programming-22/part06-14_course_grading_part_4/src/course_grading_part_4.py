# tee ratkaisu tänne
if 1:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_data = input("Exam points: ")
    course_info = input("Course information: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_data = "exam_points1.csv"
    course_info = "course2.txt"


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

with open(exam_data, 'r') as f:
    exams = {}
    for line in f:
        row = line.strip().split(';')
        if row[0] != 'id':
            exams[row[0]] = sum([int(i) for i in row[1:]])

with open(course_info, 'r') as f:
    courses = []
    for line in f:
        courses.append(line.strip().split(':')[1].strip())

with open('results.csv', 'w') as w1, open('results.txt', 'w') as w2:

    header = f'{"name":30}{"exec_nbr":<10}{"exec_pts.":<10}{"exm_pts.":<10}{"tot_pts.":<10}{"grade":<10}'
    program = f'{courses[0]}, {courses[1]} credits'
    w2.write(program + "\n")
    w2.write("=" * len(program) + "\n")
    w2.write(header + "\n")
    for k , v in students.items():
        tot_points = exercises[k] * 10 // 40 + exams[k]
        if tot_points < 15:
            grade = 0
        elif tot_points < 18:
            grade = 1
        elif tot_points < 21:
            grade = 2
        elif tot_points < 24:
            grade = 3
        elif tot_points < 28:
            grade = 4
        else:
            grade = 5
        #print(f'{students[k][0]} {students[k][1]} {grade}')
        res = f'{students[k][0] + " " + students[k][1]:30}{exercises[k]:<10}{exercises[k] * 10 // 40:<10}{exams[k]:<10}{tot_points:<10}{grade:<10}'
        w2.write(res + "\n")
        w1.write(f'{k};{students[k][0] + " " + students[k][1]};{grade}' + "\n")

print("Results written to files results.txt and results.csv")

