# Write your solution here
def read_input(msg: str, lb: int, ub: int) -> int:
    while 1:
        number = input(msg)
        try:
            number = int(number)
            if lb <= number <= ub:
                return number
            else:
                pass
        except ValueError:
            pass
        print(f"You must type in an integer between {lb} and {ub}")
    # read_input(msg, lb, ub)

# number = read_input("Please type in a number: ", 5, 10)
# print("You typed in:", number)

