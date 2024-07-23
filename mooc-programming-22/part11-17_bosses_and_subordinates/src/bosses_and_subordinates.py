# WRITE YOUR SOLUTION HERE:
class Employee:
    def __init__(self, name: str):
        self.name = name
        self.subordinates = []

    def add_subordinate(self, employee: 'Employee'):
        self.subordinates.append(employee)

def count_subordinates(employee: Employee):
    c = len(employee.subordinates)
    for subordinates in employee.subordinates:
        c += count_subordinates(subordinates)
    return c

if __name__ == "__main__":
        t1 = Employee("Sally")
        t2 = Employee("Matthew")
        t3 = Employee("Eric")
        t4 = Employee("Andy")
        t5 = Employee("Emily")
        t6 = Employee("James")
        t7 = Employee("John")
        t8 = Employee("Tina")
        t9 = Employee("Theodore")
        t10 = Employee("Arthur")
        t11 = Employee("Jack")
        t12 = Employee("Lea")
        t1.add_subordinate(t3)
        t1.add_subordinate(t4)
        t1.add_subordinate(t7)
        t3.add_subordinate(t8)
        t3.add_subordinate(t9)
        t3.add_subordinate(t10)
        t3.add_subordinate(t12)
        t9.add_subordinate(t2)
        t2.add_subordinate(t5)
        t2.add_subordinate(t11)
        t5.add_subordinate(t6)
        for t in [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12]:
            print(t, count_subordinates(t))
