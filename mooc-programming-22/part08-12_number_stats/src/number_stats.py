# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = []

    def add_number(self, number:int):
        self.numbers.append(number)

    def count_numbers(self):
        return len(self.numbers)
    
    def get_sum(self):
        return sum(self.numbers) if self.count_numbers() > 0 else 0
    
    def average(self):
        return self.get_sum()/self.count_numbers() if self.count_numbers() > 0 else 0

stats = NumberStats()
stats_even = NumberStats()
stats_odd = NumberStats()
print('Please type in integer numbers:')
while 1:
    num = int(input(''))
    if num == -1:
        break
    stats.add_number(num)
    if num%2 == 0:
        stats_even.add_number(num)
    elif num%2 == 1:
        stats_odd.add_number(num)
print("Sum of numbers:", stats.get_sum())
print("Mean of numbers:", stats.average())
print("Sum of even numbers:", stats_even.get_sum())
print("Sum of odd numbers:", stats_odd.get_sum())



# stats = NumberStats()
# stats.add_number(3)
# stats.add_number(5)
# stats.add_number(1)
# stats.add_number(2)
# print("Numbers added:", stats.count_numbers())

# stats = NumberStats()
# stats.add_number(3)
# stats.add_number(5)
# stats.add_number(1)
# stats.add_number(2)
# print("Numbers added:", stats.count_numbers())
# print("Sum of numbers:", stats.get_sum())
# print("Mean of numbers:", stats.average())
