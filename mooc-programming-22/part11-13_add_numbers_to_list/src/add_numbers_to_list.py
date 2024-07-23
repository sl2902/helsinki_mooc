# WRITE YOUR SOLUTION HERE:
def add_numbers_to_list(numbers: list) -> list:
    if len(numbers) % 5 != 0:
        numbers += [numbers[-1] + 1]
        add_numbers_to_list(numbers)