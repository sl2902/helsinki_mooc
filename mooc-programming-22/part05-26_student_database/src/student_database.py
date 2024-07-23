# Write your solution here
def add_student(students: dict, name: str) -> None:
    if name not in students:
        students[name] = []

def add_course(students: dict, name: str, course: tuple) -> None:
    is_repeated = False
    replace_grade = False
    for idx, (c, g) in enumerate(students[name]):
        if c == course[0] and g > course[1]:
            is_repeated = True
            break
        elif c == course[0] and g < course[1]:
            is_repeated = True
            replace_grade = True
    if not 0 in course:
        if name in students:
            if not is_repeated:
                students[name].append(course)
            elif replace_grade:
                students[name].pop(idx)
                students[name].insert(idx, course)

def summary(students: dict) -> None:
    print(f'students {len(students)}')
    results = sorted([(k, len(v)) for k, v in students.items()], key=lambda x: x[1], reverse=True)[0]
    print(f'most courses completed {results[1]} {results[0]}')
    grades = {}
    for k, v in students.items():
        for _, grade in v:
            if k not in grades:
                grades[k] = grade
            else:
                grades[k] += grade
        grades[k] /= len(v)
    results = sorted(grades.items(), key=lambda x: x[1], reverse=True)[0]
    print(f'best average grade {results[1]} {results[0]}')


def print_student(students: dict, name: str) -> str:
    if name in students:
        print(f'{name}:')
        if len(students[name]) == 0:
            print(' no completed courses')
        else:
            print(f' {len(students[name])} completed courses:')
            total_grade = 0
            for course, grade in students[name]:
                print(f'  {course} {grade}')
                total_grade += grade
            print(f' average grade {total_grade/len(students[name])}')
    else:
        print(f'{name}: no such person in the database')

