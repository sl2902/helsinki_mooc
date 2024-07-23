# Write your solution here
# If you use the classes made in the previous exercise, copy them here
class Task:
    initial_val = 0
    def __init__(self, description: str, name: str, n_hours: int):
        self.id = self.inc_id()
        self.description = description
        self.programmer = name
        self.workload = n_hours
        self._is_finish = False
        # Task.initial_val = self.id

    def inc_id(self):
        Task.initial_val += 1
        return  Task.initial_val   
    
    def is_finished(self):
        return self._is_finish
    
    def mark_finished(self):
        self._is_finish = True
    
    def __str__(self):
        if self.is_finished():
            return f'{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} FINISHED'
        return f'{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} NOT FINISHED'

class OrderBook(Task):
    def __init__(self):
        self._orders = []
        # super().__init__(description, name, n_hours)
    
    def add_order(self, description: str, name: str, n_hours: int):
        self._orders.append(Task(description, name, n_hours))

    def all_orders(self):
        return self._orders
    
    def programmers(self):
        return list(set([task.programmer for task in self.all_orders()]))
    
    def mark_finished(self, id: int):
        for task in self.all_orders():
             if task.id == id:
                task.mark_finished()
                break
        else:
            raise ValueError("no id with given task")
    
    def finished_orders(self):
        return [task for task in self.all_orders() if task.is_finished()]
    
    def unfinished_orders(self):
        return [task for task in self.all_orders() if not task.is_finished()]
    
    def status_of_programmer(self, programmer: str):
        if programmer not in self.programmers():
            raise ValueError("no programmer for given task")

        finished_tasks = sum([1 for task in self.finished_orders() if task.programmer == programmer])
        unfinished_tasks = sum([1 for task in self.unfinished_orders() if task.programmer == programmer])
        finished_workloads = sum([task.workload for task in self.finished_orders() if task.programmer == programmer])
        unfinished_workloads = sum([task.workload for task in self.unfinished_orders() if task.programmer == programmer])
        return (
            finished_tasks, 
            unfinished_tasks, 
            finished_workloads,
            unfinished_workloads
        )

class OrderApplication:
    def __init__(self):
        self.order_book = OrderBook()
    
    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")
    
    def add_order(self):
        try:
            description = input("description: ")
            name, n_hours = input("programmer and workload estimate: ").split()
            self.order_book.add_order(description, name, int(n_hours))
            print("added!")
        except:
            print("erroneous input")

    
    def list_finished_tasks(self):
        if len(self.order_book.finished_orders()) == 0:
            print("no finished tasks")
        else:
            for f_task in self.order_book.finished_orders():
                print(f_task)
    
    def list_unfinished_tasks(self):
        for u_task in self.order_book.unfinished_orders():
                print(u_task)
    
    def mark_finished(self):
        try:
            id = int(input("id: "))
            self.order_book.mark_finished(id)
            print("marked as finished")
        except:
            print("erroneous input")
    
    def programmers(self):
        for programmer in self.order_book.programmers():
            print(programmer)
    
    def status_of_programmer(self):
        try: 
            programmer = input("programmer: ")
            status = self.order_book.status_of_programmer(programmer)
            print(f'tasks: finished {status[0]} not finished {status[1]}, hours: done {status[2]} scheduled {status[3]}')
        except:
            print("erroneous input")
    
    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_order()
            elif command == "2":
                self.list_finished_tasks()
            elif command == "3":
                self.list_unfinished_tasks()
            elif command == "4":
                self.mark_finished()
            elif command == "5":
                self.programmers()
            elif command == "6":
                self.status_of_programmer()
            else:
                self.help()
    

application = OrderApplication()
application.execute()