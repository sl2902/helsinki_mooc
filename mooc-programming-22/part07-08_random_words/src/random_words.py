# Write your solution here
import random
def words(n: int, beginning: str) -> list:
    word_list = []
    with open('words.txt', 'r') as f:
        for word in f:
            word = word.strip()
            if word.startswith(beginning):
                word_list.append(word)
    if len(word_list) < n:
        raise ValueError("not enough words beginning with the specified string")
    random.shuffle(word_list)
    return word_list[:n]

# word_list = words(3, "ca")
# for word in word_list:
#     print(word)

