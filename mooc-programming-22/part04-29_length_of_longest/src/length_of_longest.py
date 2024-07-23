# Write your solution here
def length_of_longest(lst):
    return max([len(a) for a in lst])

if __name__ == "__main__":
    print(length_of_longest(["first", "second", "fourth", "eleventh"]))