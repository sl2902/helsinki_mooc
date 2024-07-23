# Write your solution here
def longest(lst):
    max_val = float('-inf')
    max_e = ''
    lst_len = [len(s) for s in lst]
    for i, n in enumerate(lst_len):
        if n > max_val:
            max_val = n
            max_e = lst[i]
    return max_e

if __name__ == "__main__":
    print(longest(["hi", "hiya", "hello", "howdydoody", "hi there"]))