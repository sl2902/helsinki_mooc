# Write your solution here
from this import d


def invert(dictionary: dict) -> dict:
    reference = dictionary.copy()
    dictionary.clear()
    dictionary.update(map(reversed, reference.items()))

if __name__ == '__main__':
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)