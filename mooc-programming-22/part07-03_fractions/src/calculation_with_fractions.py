# Write your solution here
from fractions import Fraction
def fractionate(amount: int) -> list:

    return [Fraction(1, amount) for _ in range(amount)]