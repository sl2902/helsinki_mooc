# Write your solution here
def everything_reversed(lst):
    return [s[::-1] for s in lst][::-1]

if __name__ == '__main__':
    print(everything_reversed(["Hi", "there", "example", "one more"]))