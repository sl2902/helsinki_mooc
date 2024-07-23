# Write your solution here
import random
def lottery_numbers(amount: int, lower: int, upper: int) -> list:
    return sorted(random.sample(list(range(lower, upper)), amount))

# for number in lottery_numbers(7, 1, 40):
#     print(number)
