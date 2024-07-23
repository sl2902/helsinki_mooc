# Write your solution here
def count_matching_elements(lst, num):
    return sum([ele.count(num) for ele in lst])

if __name__ == "__main__":
    print(count_matching_elements([[1, 2, 1], [0, 3, 4], [1, 0, 0]], 1))