# Write your solution here:
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

# t1 = Task("program hello world", "Eric", 3)
# print(t1.id, t1.description, t1.programmer, t1.workload)
# print(t1)
# print(t1.is_finished())
# t1.mark_finished()
# print(t1)
# print(t1.is_finished())
# t2 = Task("program webstore", "Adele", 10)
# t3 = Task("program mobile app for workload accounting", "Eric", 25)
# print(t2)
# print(t3)

# orders = OrderBook()
# orders.add_order("program webstore", "Adele", 10)
# orders.add_order("program mobile app for workload accounting", "Eric", 25)
# orders.add_order("program app for practising mathematics", "Adele", 100)

# for order in orders.all_orders():
#     print(order)

# print()

# for programmer in orders.programmers():
#     print(programmer)

# orders = OrderBook()
# orders.add_order("program webstore", "Adele", 10)
# orders.add_order("program mobile app for workload accounting", "Eric", 25)
# orders.add_order("program app for practising mathematics", "Adele", 100)

# orders.mark_finished(1)
# orders.mark_finished(2)

# for order in orders.all_orders():
#     print(order)

# orders = OrderBook()
# orders.add_order("program webstore", "Adele", 10)
# orders.add_order("program mobile app for workload accounting", "Adele", 25)
# orders.add_order("program app for practising mathematics", "Adele", 100)
# orders.add_order("program the next facebook", "Eric", 1000)

# orders.mark_finished(1)
# orders.mark_finished(2)

# status = orders.status_of_programmer("Adele")
# print(status)

# t = OrderBook()
# t.add_order("program webstore", "Andy", 10)
# t.status_of_programmer("JohnDoe")
