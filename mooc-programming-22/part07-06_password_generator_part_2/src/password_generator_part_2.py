# Write your solution here
import random
import string

def generate_strong_password(n: int, arg1: bool, arg2: bool) -> str:
    # choice1 = string.ascii_lowercase
    # choice2 = string.digits
    # choice3 = '!?=+-()#'
    if not(arg1 or arg2):
        s = list(string.ascii_lowercase)
        random.shuffle(s)
        return "".join(s)[:n]
    elif arg1 and not arg2:
        s = ''
        choices = [string.ascii_lowercase, string.digits]
        random.shuffle(choices)
        for _ in range(n):
            choice = list(choices[0])
            random.shuffle(choice)
            s += choice[0]
            choices = choices[1:] + choices[:1]
        return s
    elif not arg1 and arg2:
        s = ''
        choices = [string.ascii_lowercase, '!?=+-()#']
        random.shuffle(choices)
        for _ in range(n):
            choice = list(choices[0])
            random.shuffle(choice)
            s += choice[0]
            choices = choices[1:] + choices[:1]
        return s
    else:
        s = ''
        choices = [string.ascii_lowercase, string.digits, '!?=+-()#']
        random.shuffle(choices)
        for _ in range(n):
            choice = list(choices[0])
            random.shuffle(choice)
            s += choice[0]
            choices = choices[1:] + choices[:1]
        return s

for i in range(10):
    print(generate_strong_password(3, False, True))



        