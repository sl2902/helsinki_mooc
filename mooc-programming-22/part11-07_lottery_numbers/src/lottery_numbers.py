# WRITE YOUR SOLUTION HERE:
class LotteryNumbers:
    def __init__(self, n: int, numbers: list):
        self.n = n
        self.numbers = numbers

    def number_of_hits(self, numbers: list):
        return len(set(self.numbers).intersection(set(numbers)))
    
    def hits_in_place(self, numbers: list):
        return [n if n in self.numbers else -1 for n in numbers]

# week5 = LotteryNumbers(5, [1,2,3,4,5,6,7])
# my_numbers = [1,4,7,11,13,19,24]

# print(week5.number_of_hits(my_numbers))
