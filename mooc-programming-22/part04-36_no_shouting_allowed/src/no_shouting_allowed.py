# Write your solution here
def no_shouting(lst):
    return [s for s in lst if not s.isupper()]

if __name__ == '__main__':
    print(no_shouting(["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]))