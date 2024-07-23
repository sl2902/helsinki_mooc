# Write your solution here
import random
def roll(die: str) -> str:
    choices = {'A': [3, 3, 3, 3, 3, 6],
    'B': [2, 2, 2, 5, 5, 5],
    'C': [1, 4, 4, 4, 4, 4]}

    return random.choice(choices[die])

def play(die1: str, die2: str, times: int) -> tuple:
    win1, win2, tie = 0, 0, 0
    for _ in range(times):
        r1, r2 = roll(die1), roll(die2)
        if r1 > r2:
            win1 += 1
        elif r2 > r1:
            win2 += 1
        else:
            tie += 1
    return win1, win2, tie


# for i in range(20):
#     print(roll("A"), " ", end="")
# print()
# for i in range(20):
#     print(roll("B"), " ", end="")
# print()
# for i in range(20):
#     print(roll("C"), " ", end="")
# print()

# result = play("A", "C", 1000)
# print(result)
# result = play("B", "B", 1000)
# print(result)
