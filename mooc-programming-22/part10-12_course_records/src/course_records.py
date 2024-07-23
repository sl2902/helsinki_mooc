# tee ratkaisusi tänne
class Course:
    def __init__(self, name: str, grade: int, credits: int):
        self._name = name
        self._grade = grade
        self._credits = credits
    
    # def add_grade(self, grade: int):
    #     self._grade = grade
    
    # def add_credits(self, credits: int):
    #     self._credits = credits
    
    # def name(self):
    #     return self._name
    
    def grade(self):
        return self._grade
    
    def credits(self):
        return self._credits
    
    def __str__(self):
        return (f'{self._name} ({self._credits} cr) grade {self._grade}')
    

class CourseWork:
    def __init__(self):
        self.__courses = {}
    
    def add_course(self, name: str, grade: int, credits: int):
        if not name in self.__courses or self.__courses[name].grade() < grade:
            self.__courses[name] = Course(name, grade, credits)
    
    # def add_grade(self, name: str, grade: int):
    #     if not name in self.__courses:
    #         self.__courses[name] = Course(name)
    #     if self.__courses[name].grade() < grade:
    #         self.__courses[name].add_grade(grade)
    
    # def add_credits(self, name: str, credits: int):
    #     if not name in self.__courses:
    #         self.__courses[name] = Course(name)
    #     self.__courses[name].add_credits(credits)
    
    def get_course(self, name: str):
        return self.__courses.get(name, None)
    
    def all_courses(self):
        return self.__courses

class CourseWorkApp:
    def __init__(self):
        self.__course_work = CourseWork()
    
    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")
    
    def add_course(self):
        name = input("course: ")
        grade = int(input("grade: "))
        # self.__course_work.add_grade(name, grade)
        credits = int(input("credits: "))
        # self.__course_work.add_credits(name, credits)
        self.__course_work.add_course(name, grade, credits)
    
    def get_course(self):
        name = input("course: ")
        res = self.__course_work.get_course(name)
        if res is None:
            print("no entry for this course")
        else:
            print(res)
    
    def display_stats(self):
        all_courses = self.__course_work.all_courses()
        num_courses = len(all_courses)
        tot_cr = 0
        avg_gr = 0
        grades = {1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0}
        for name in all_courses:
            tot_cr += all_courses[name].credits()
            avg_gr += all_courses[name].grade()
            if all_courses[name].grade() in grades:
                grades[all_courses[name].grade()] += 1
        avg_gr /= num_courses
        print(f'{num_courses} completed courses, a total of {tot_cr} credits')
        print(f'mean {avg_gr:.1f}')
        print('grade distribution')
        print(f'5: {grades[5] * "x"}')
        print(f'4: {grades[4] * "x"}')
        print(f'3: {grades[3] * "x"}')
        print(f'2: {grades[2] * "x"}')
        print(f'1: {grades[1] * "x"}')
        # print(f'{0:>3}: {grades[0] * "*"}')

    
    def execute(self):
        self.help()
        while 1:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.get_course()
            elif command == "3":
                self.display_stats()
            else:
                self.help()
app = CourseWorkApp()
app.execute()

