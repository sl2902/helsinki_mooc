# Write your solution here
import random
import string
def generate_password(n: int) -> str:
    s = list(string.ascii_lowercase)
    random.shuffle(s)
    return "".join(s)[:n]

# for i in range(10):
#     print(generate_password(8))

