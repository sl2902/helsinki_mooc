# Write your solution here:
import random
def word_generator(characters: str, length: int, amount: int):
    return ("".join(random.sample(characters, length)) for _ in range(amount)) 

# wordgen = word_generator("abcdefg", 3, 5)
# for word in wordgen:
#     print(word)
