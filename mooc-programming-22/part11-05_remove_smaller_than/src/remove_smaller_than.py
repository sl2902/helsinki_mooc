# WRITE YOUR SOLUTION HERE:
def remove_smaller_than(numbers: list, limit: int) -> list:
    return [n for n in numbers if n >= limit]