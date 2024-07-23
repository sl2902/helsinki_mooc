# Write your solution here
def sum_of_positives(lst):
    return sum(a for a in lst if a > 0)

if __name__ == '__main__':
    print(sum_of_positives([1, -1, 2, -2, 3, -3]))